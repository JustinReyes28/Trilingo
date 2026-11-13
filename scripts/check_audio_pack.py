"""Validate the committed bundled MP3 pack against current content and file hashes.

Active CI and release verification check for the bundled-audio-only architecture;
requires zero runtime TTS services.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT / "scripts"))

from audio_pack_common import speakable_items  # noqa: E402
from build_audio_pack import validate_mp3  # noqa: E402

from app import audio_pack  # noqa: E402
from app.services import load_content  # noqa: E402


def _invalid_manifest_report(pack: Path, message: str) -> dict:
    return {
        "pack": str(pack),
        "status": "invalid",
        "course_version": None,
        "counts": {
            "expected": 0,
            "manifest": 0,
            "missing": 0,
            "missing_required": 0,
            "extra": 0,
            "unreferenced": 0,
            "errors": 1,
            "warnings": 0,
        },
        "errors": [message],
        "warnings": [],
        "ok": False,
    }


def check(args: argparse.Namespace) -> dict:
    manifest_path = args.pack / "manifest.json"
    if not manifest_path.is_file():
        return _invalid_manifest_report(args.pack, f"Pack manifest is missing: {manifest_path}")
    try:
        manifest = audio_pack.PackManifest.model_validate_json(
            manifest_path.read_text(encoding="utf-8")
        )
    except (OSError, ValueError) as error:
        return _invalid_manifest_report(
            args.pack, f"Invalid pack manifest ({type(error).__name__}): {error}"
        )
    content = load_content(args.course)
    errors: list[str] = []
    warnings: list[str] = []
    if manifest.course_id != content.id:
        errors.append("Manifest course_id does not match the course")
    if manifest.course_version != content.version:
        errors.append("Manifest course_version does not match the course version")
    source_hash = hashlib.sha256(args.course.read_bytes()).hexdigest()
    if manifest.source_sha256 != source_hash:
        errors.append("Manifest source_sha256 does not match the current content file")
    expected = speakable_items(
        content,
        manifest.engine.voice_ja,
        manifest.engine.voice_en,
        manifest.engine.model,
    )
    actual = {item.key: item for item in manifest.items}
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    for key in missing:
        item = expected[key]
        message = f"Missing audio: {item['kind']} {item['item_id']} ({item['language']})"
        if item["required"]:
            errors.append(message)
        else:
            warnings.append(message)
    for key in extra:
        warnings.append(f"Stale audio not used by current content: {actual[key].file}")
    pack_root = args.pack.resolve()
    referenced_files: set[Path] = set()
    for item in manifest.items:
        path = (pack_root / item.file).resolve()
        if not path.is_relative_to(pack_root) or not path.is_file():
            errors.append(f"Missing or unsafe pack file: {item.file}")
            continue
        referenced_files.add(path)
        data = path.read_bytes()
        if len(data) != item.bytes:
            errors.append(f"Size mismatch: {item.file}")
            continue
        if hashlib.sha256(data).hexdigest() != item.file_sha256:
            errors.append(f"Checksum mismatch: {item.file}")
            continue
        try:
            duration, _, _ = validate_mp3(data)
        except (OSError, ValueError) as error:
            errors.append(f"Invalid MP3 {item.file}: {type(error).__name__}")
            continue
        if abs(duration - item.duration_seconds) > 0.15:
            errors.append(f"Duration mismatch: {item.file}")
    unreferenced = 0
    for mp3_path in sorted(args.pack.rglob("*.mp3")):
        resolved_mp3 = mp3_path.resolve()
        if resolved_mp3 not in referenced_files:
            unreferenced += 1
            try:
                relative = resolved_mp3.relative_to(pack_root).as_posix()
            except ValueError:
                relative = mp3_path.relative_to(args.pack).as_posix()
            warnings.append(f"Unreferenced MP3 file in pack: {relative}")
    if args.strict:
        errors.extend(warnings)
        warnings = []
    counts = {
        "expected": len(expected),
        "manifest": len(manifest.items),
        "missing": len(missing),
        "missing_required": sum(expected[key]["required"] for key in missing),
        "extra": len(extra),
        "unreferenced": unreferenced,
        "errors": len(errors),
        "warnings": len(warnings),
    }
    return {
        "pack": str(args.pack),
        "status": manifest.status,
        "course_version": manifest.course_version,
        "counts": counts,
        "errors": errors[:50],
        "warnings": warnings[:50],
        "ok": not errors,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the Trilingo authored-audio pack")
    parser.add_argument(
        "--course", type=Path, default=ROOT / "content/courses/ja/starter.json"
    )
    parser.add_argument("--pack", type=Path, required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    args.course = args.course.resolve()
    args.pack = args.pack.resolve()
    report = check(args)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
