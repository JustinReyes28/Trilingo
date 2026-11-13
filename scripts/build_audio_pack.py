"""Optional maintainer-only generator for future versioned MP3 packs (e.g., 0.1.22+).

Normal runtime, local development, and CI use the committed 0.1.21 bundled MP3 pack
and never require a Kokoro container or TTS model downloads. Run this historical
build-time script only when regenerating authored reference clips after content,
pronunciation-override, or voice updates with a local Kokoro-FastAPI service running.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import httpx
from mutagen.mp3 import MP3

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
sys.path.insert(0, str(ROOT / "scripts"))

from audio_pack_common import speakable_items  # noqa: E402

from app import audio_pack  # noqa: E402
from app.services import load_content  # noqa: E402

MAX_BYTES = 1_000_000
MIN_BYTES = 1024
MIN_SECONDS = 0.2
MAX_SECONDS = 60.0
DEFAULT_LICENSE = {
    "id": "kokoro-82m",
    "source": "Kokoro-82M v1.0 model and voice pack",
    "license": "Apache-2.0",
    "attribution": (
        "Kokoro-82M v1.0 by hexgrad (https://huggingface.co/hexgrad/Kokoro-82M), "
        "Apache-2.0. Voices: jf_alpha (Japanese) and af_heart (English). The model "
        "card lists Koniwa tnc (CC BY 3.0) and SIWIS (CC BY 4.0) audio in the v1.0 "
        "training data; see VOICES.md. Generated performances are Trilingo-authored "
        "content under CC-BY-4.0."
    ),
}
GENERATED_LICENSE = {
    "id": "trilingo-generated-audio",
    "source": "Kokoro-generated performances of Trilingo authored text",
    "license": "CC-BY-4.0",
    "attribution": "Trilingo original course contributors",
}


def speech_url(base_url: str) -> str:
    parsed = urlsplit(base_url)
    if (
        parsed.scheme not in {"http", "https"}
        or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
        or parsed.username
        or parsed.password
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError("Use a local Kokoro base URL without credentials/query/fragment")
    base = base_url.rstrip("/")
    return base + ("" if base.endswith("/v1") else "/v1") + "/audio/speech"


def validate_mp3(data: bytes) -> tuple[float, int, int]:
    if not MIN_BYTES <= len(data) <= MAX_BYTES:
        raise ValueError("MP3 size is outside the allowed range")
    audio = MP3(io.BytesIO(data))
    duration = float(audio.info.length)
    if not MIN_SECONDS <= duration <= MAX_SECONDS:
        raise ValueError("MP3 duration is outside the allowed range")
    return duration, int(audio.info.sample_rate), round(int(audio.info.bitrate) / 1000)


def synthesize(client: httpx.Client, url: str, model: str, voice: str, text: str) -> bytes:
    with client.stream(
        "POST",
        url,
        json={
            "model": model,
            "voice": voice,
            "input": text,
            "response_format": "mp3",
            "speed": 1.0,
        },
    ) as response:
        response.raise_for_status()
        content_type = response.headers.get("content-type", "").split(";")[0]
        if content_type not in {"audio/mpeg", "audio/mp3", "application/octet-stream"}:
            raise ValueError("Kokoro did not return MP3 audio")
        data = bytearray()
        for chunk in response.iter_bytes():
            data.extend(chunk)
            if len(data) > MAX_BYTES:
                raise ValueError("Generated MP3 exceeds the local size limit")
    return bytes(data)


def build_pack(args: argparse.Namespace) -> dict:
    content = load_content(args.course)
    if args.version is not None and args.version != content.version:
        raise ValueError("The requested pack version does not match the course version")
    items = speakable_items(content, args.voice_ja, args.voice_en, args.model)
    if args.limit is not None:
        items = dict(list(items.items())[: args.limit])
    counts = {
        "ja": sum(item["language"] == "ja" for item in items.values()),
        "en": sum(item["language"] == "en" for item in items.values()),
        "entities": len(items),
    }
    if args.dry_run:
        return {"dry_run": True, "counts": counts, "items": len(items)}

    pack_dir = args.output / content.id / content.version
    pack_dir.mkdir(parents=True, exist_ok=True)
    generated = reused = 0
    total_bytes = 0
    total_seconds = 0.0
    sample_rate = 0
    bitrate = 0
    manifest_items: list[dict] = []
    url = speech_url(args.base_url)
    timeout = httpx.Timeout(args.timeout)
    with httpx.Client(timeout=timeout, follow_redirects=False, trust_env=False) as client:
        for index, item in enumerate(items.values(), start=1):
            language_dir = item["language"]
            relative = Path(language_dir) / item["key"][:2] / (item["key"] + ".mp3")
            path = pack_dir / relative
            data: bytes | None = None
            if path.is_file() and not args.force:
                try:
                    data = path.read_bytes()
                    duration, rate, kbps = validate_mp3(data)
                    reused += 1
                except (OSError, ValueError):
                    data = None
            if data is None:
                voice = args.voice_ja if item["language"] == "ja" else args.voice_en
                last_error: Exception | None = None
                for attempt in range(args.retries + 1):
                    try:
                        spoken = item["pronunciation_override"] or item["text"]
                        data = synthesize(client, url, args.model, voice, spoken)
                        duration, rate, kbps = validate_mp3(data)
                        break
                    except (httpx.HTTPError, ValueError, OSError) as error:
                        last_error = error
                        if attempt < args.retries:
                            time.sleep(min(2**attempt, 8))
                else:
                    raise RuntimeError(
                        f"{item['kind']} {item['item_id']}: {type(last_error).__name__}"
                    ) from last_error
                path.parent.mkdir(parents=True, exist_ok=True)
                temporary = path.with_name(path.name + ".tmp")
                temporary.write_bytes(data)
                temporary.replace(path)
                generated += 1
            total_bytes += len(data)
            total_seconds += duration
            sample_rate = sample_rate or rate
            bitrate = bitrate or kbps
            manifest_items.append(
                {
                    "key": item["key"],
                    "kind": item["kind"],
                    "item_id": item["item_id"],
                    "cue_id": item["cue_id"],
                    "turn_id": item["turn_id"],
                    "language": item["language"],
                    "text": item["text"],
                    "pronunciation_override": item["pronunciation_override"],
                    "file": relative.as_posix(),
                    "bytes": len(data),
                    "duration_seconds": round(duration, 3),
                    "file_sha256": hashlib.sha256(data).hexdigest(),
                }
            )
            if args.progress and index % 50 == 0:
                print(
                    f"{index}/{len(items)} clips · {generated} generated · "
                    f"{reused} reused · {total_bytes / 1_000_000:.1f} MB",
                    flush=True,
                )
    if not generated and not reused:
        raise RuntimeError("No audio clips were produced; check the content and filters")
    manifest = {
        "format_version": audio_pack.PACK_FORMAT_VERSION,
        "course_id": content.id,
        "course_version": content.version,
        "source_sha256": hashlib.sha256(args.course.read_bytes()).hexdigest(),
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "draft",
        "review": {
            "reviewed_by": None,
            "reviewed_at": None,
            "note": "Human Japanese listening and English voice spot-check pending",
        },
        "engine": {
            "provider": "kokoro",
            "model": args.model,
            "voice_ja": args.voice_ja,
            "voice_en": args.voice_en,
            "format": "mp3",
            "sample_rate": sample_rate or args.sample_rate,
            "bitrate_kbps": bitrate or args.bitrate_kbps,
        },
        "licenses": [args.license, GENERATED_LICENSE],
        "counts": {
            **counts,
            "files": len(manifest_items),
            "total_bytes": total_bytes,
            "total_seconds": round(total_seconds, 1),
        },
        "items": manifest_items,
    }
    manifest_tmp = pack_dir / "manifest.json.tmp"
    manifest_tmp.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    manifest_tmp.replace(pack_dir / "manifest.json")
    audio_pack.clear_cache()
    return {
        "pack": str(pack_dir),
        "counts": manifest["counts"],
        "generated": generated,
        "reused": reused,
        "engine": manifest["engine"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the Trilingo authored-audio MP3 pack")
    parser.add_argument(
        "--course", type=Path, default=ROOT / "content/courses/ja/starter.json"
    )
    parser.add_argument("--output", type=Path, default=ROOT / "content/audio")
    parser.add_argument("--version", default=None)
    parser.add_argument("--base-url", default="http://127.0.0.1:8880")
    parser.add_argument("--model", default="kokoro")
    parser.add_argument("--voice-ja", default="jf_alpha")
    parser.add_argument("--voice-en", default="af_heart")
    parser.add_argument("--timeout", type=float, default=60)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--sample-rate", type=int, default=24000)
    parser.add_argument("--bitrate-kbps", type=int, default=64)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--license-id", default=DEFAULT_LICENSE["id"])
    parser.add_argument("--license-source", default=DEFAULT_LICENSE["source"])
    parser.add_argument("--license", dest="license_name", default=DEFAULT_LICENSE["license"])
    parser.add_argument("--attribution", default=DEFAULT_LICENSE["attribution"])
    args = parser.parse_args()
    args.course = args.course.resolve()
    args.output = args.output.resolve()
    args.license = {
        "id": args.license_id,
        "source": args.license_source,
        "license": args.license_name,
        "attribution": args.attribution,
    }
    report = build_pack(args)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
