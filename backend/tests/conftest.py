import hashlib
import json
import os
import shutil
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config as AlembicConfig
from fastapi.testclient import TestClient

from app import audio_pack
from app.config import ROOT, Config
from app.main import create_app
from app.services import load_content


def write_fixture_audio_pack(root: Path, status: str = "draft") -> Path:
    content = load_content(ROOT / "content" / "courses" / "ja" / "starter.json")
    voice_ja, voice_en, model = "jf_fixture", "af_fixture", "kokoro-fixture"
    word = next(item for item in content.vocabulary if item.status == "published")
    entries: list[tuple[str, str, str, str, str | None, str | None]] = [
        ("word", word.id, "ja", word.surface, word.pronunciation_override, None),
        ("gloss", word.id, "en", word.gloss, None, None),
    ]
    for exercise in content.practice_exercises:
        for cue in getattr(exercise, "audio", []):
            entries.append(
                (
                    "cue",
                    exercise.id,
                    cue.language,
                    cue.transcript,
                    cue.pronunciation_override,
                    cue.id,
                )
            )
    for unit in content.units:
        for lesson in unit.lessons:
            for exercise in lesson.exercises:
                for cue in getattr(exercise, "audio", []):
                    entries.append(
                        (
                            "cue",
                            exercise.id,
                            cue.language,
                            cue.transcript,
                            cue.pronunciation_override,
                            cue.id,
                        )
                    )
    pack_dir = root / content.id / content.version
    items: list[dict] = []
    seen: set[str] = set()
    for kind, item_id, language, text, override, cue_id in entries:
        voice = voice_ja if language == "ja" else voice_en
        key = audio_pack.pack_key(text, language, voice, model, override)
        if key in seen:
            continue
        seen.add(key)
        data = f"ID3 fixture {kind} {language} {item_id}".encode()
        rel = f"{language}/{key[:2]}/{key}.mp3"
        file_path = pack_dir / rel
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_bytes(data)
        items.append(
            {
                "key": key,
                "kind": kind,
                "item_id": item_id,
                "cue_id": cue_id,
                "turn_id": None,
                "language": language,
                "text": text,
                "pronunciation_override": override,
                "file": rel,
                "bytes": len(data),
                "duration_seconds": 0.5,
                "file_sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    source = (ROOT / "content" / "courses" / "ja" / "starter.json").read_bytes()
    manifest = {
        "format_version": 1,
        "course_id": content.id,
        "course_version": content.version,
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "generated_at": "2026-11-12T00:00:00Z",
        "status": status,
        "review": {},
        "engine": {
            "provider": "kokoro",
            "model": model,
            "voice_ja": voice_ja,
            "voice_en": voice_en,
            "format": "mp3",
            "sample_rate": 24000,
            "bitrate_kbps": 64,
        },
        "licenses": [
            {
                "id": "fixture",
                "source": "Synthetic fixture audio",
                "license": "test-only",
                "attribution": "test fixture",
            }
        ],
        "counts": {
            "ja": sum(item["language"] == "ja" for item in items),
            "en": sum(item["language"] == "en" for item in items),
            "files": len(items),
            "total_bytes": sum(item["bytes"] for item in items),
            "total_seconds": len(items) * 0.5,
        },
        "items": items,
    }
    pack_dir.mkdir(parents=True, exist_ok=True)
    (pack_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return root


@pytest.fixture
def fixture_audio_pack(tmp_path: Path):
    audio_pack.clear_cache()
    pack_root = write_fixture_audio_pack(tmp_path / "audio_pack")
    yield pack_root
    audio_pack.clear_cache()


@pytest.fixture(scope="session")
def _migrated_template_db(tmp_path_factory: pytest.TempPathFactory) -> Path:
    temp_dir = tmp_path_factory.mktemp("db_template")
    template_path = temp_dir / "template.db"
    url = f"sqlite:///{template_path.as_posix()}"
    old_env = os.environ.get("DATABASE_URL")
    os.environ["DATABASE_URL"] = url
    try:
        ini_path = str(ROOT / "backend" / "alembic.ini")
        alembic = AlembicConfig(ini_path if Path(ini_path).is_file() else "alembic.ini")
        command.upgrade(alembic, "head")
    finally:
        if old_env is not None:
            os.environ["DATABASE_URL"] = old_env
        else:
            os.environ.pop("DATABASE_URL", None)
    return template_path


@pytest.fixture(autouse=True)
def _isolate_audio_pack(monkeypatch):
    # Keep tests isolated from the real bundled pack under content/audio/ unless explicitly enabled.
    monkeypatch.setenv("AUDIO_PACK_ENABLED", "false")


@pytest.fixture
def database(tmp_path: Path, monkeypatch, _migrated_template_db: Path) -> str:
    target = tmp_path / "isolated.db"
    shutil.copyfile(_migrated_template_db, target)
    url = f"sqlite:///{target.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)
    return url


@pytest.fixture
def client(database):
    app = create_app(Config(database_url=database, audio_pack_enabled=False))
    with TestClient(app) as client:
        yield client
