import argparse
import base64
import hashlib
import json
import sys
from pathlib import Path
from uuid import uuid4

import httpx
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from test_learning import start

from app import audio_pack
from app.config import ROOT, Config
from app.content_schema import CourseContent
from app.db import sessions
from app.main import create_app
from app.services import import_content, load_content

COURSE = "ja-starter"
VERSION = "0.1.21"
VOICE_JA = "jf_fixture"
VOICE_EN = "af_fixture"
MODEL = "kokoro-fixture"


def _exercises(content: CourseContent):
    yield from content.practice_exercises
    for unit in content.units:
        for lesson in unit.lessons:
            yield from lesson.exercises


def _item(kind: str, item_id: str, language: str, text: str, override, cue_id=None) -> dict:
    voice = VOICE_JA if language == "ja" else VOICE_EN
    key = audio_pack.pack_key(text, language, voice, MODEL, override)
    data = f"ID3 fixture {kind} {language} {item_id}".encode()
    return {
        "key": key,
        "kind": kind,
        "item_id": item_id,
        "cue_id": cue_id,
        "turn_id": None,
        "language": language,
        "text": text,
        "pronunciation_override": override,
        "file": f"{language}/{key[:2]}/{key}.mp3",
        "bytes": len(data),
        "duration_seconds": 0.5,
        "file_sha256": hashlib.sha256(data).hexdigest(),
        "_data": data,
    }


def _write_pack(root: Path, content: CourseContent) -> dict[str, dict]:
    word = next(word for word in content.vocabulary if word.status == "published")
    exercise, cue = next(
        (exercise, cue)
        for exercise in _exercises(content)
        for cue in getattr(exercise, "audio", [])
    )
    pack_dir = root / COURSE / VERSION
    items = [
        _item("word", word.id, "ja", word.surface, word.pronunciation_override),
        _item("gloss", word.id, "en", word.gloss, None),
        _item("cue", exercise.id, "ja", cue.transcript, cue.pronunciation_override, cue.id),
    ]
    seen = {item["key"] for item in items}
    for candidate in _exercises(content):
        for candidate_cue in getattr(candidate, "audio", []):
            item = _item(
                "cue",
                candidate.id,
                candidate_cue.language,
                candidate_cue.transcript,
                candidate_cue.pronunciation_override,
                candidate_cue.id,
            )
            if item["key"] in seen:
                continue
            seen.add(item["key"])
            items.append(item)
    for item in items:
        path = pack_dir / item["file"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(item.pop("_data"))
    source = (ROOT / "content" / "courses" / "ja" / "starter.json").read_bytes()
    manifest = {
        "format_version": 1,
        "course_id": COURSE,
        "course_version": VERSION,
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "generated_at": "2026-11-12T00:00:00Z",
        "status": "draft",
        "review": {},
        "engine": {
            "provider": "kokoro",
            "model": MODEL,
            "voice_ja": VOICE_JA,
            "voice_en": VOICE_EN,
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
    return {
        "word": {**items[0], "data": (pack_dir / items[0]["file"]).read_bytes()},
        "gloss": {**items[1], "data": (pack_dir / items[1]["file"]).read_bytes()},
        "cue": {**items[2], "data": (pack_dir / items[2]["file"]).read_bytes()},
        "word_id": word.id,
    }


@pytest.fixture
def pack_client(database, tmp_path):
    audio_pack.clear_cache()
    content = load_content(ROOT / "content" / "courses" / "ja" / "starter.json")
    expected = _write_pack(tmp_path / "audio_pack", content)
    app = create_app(
        Config(
            database_url=database,
            audio_pack_dir=tmp_path / "audio_pack",
            audio_pack_enabled=True,
        )
    )
    with TestClient(app) as client:
        with app.state.session_factory() as db:
            import_content(db, content)
        yield client, expected
    audio_pack.clear_cache()


def test_pack_hit_plays_with_providers_disabled(pack_client):
    client, expected = pack_client
    response = client.post(
        "/api/v1/audio/speech",
        json={"course_id": COURSE, "item_id": expected["word_id"]},
    )
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["source"] == "pack"
    assert body["mime"] == "audio/mpeg"
    assert body["cached"] is True
    assert base64.b64decode(body["audio_base64"]) == expected["word"]["data"]


def test_english_gloss_uses_the_english_bundled_voice(pack_client):
    client, expected = pack_client
    response = client.post(
        "/api/v1/audio/speech",
        json={"course_id": COURSE, "item_id": expected["word_id"], "language": "en"},
    )
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["source"] == "pack"
    assert base64.b64decode(body["audio_base64"]) == expected["gloss"]["data"]


def test_missing_english_clip_returns_audio_unavailable(pack_client):
    client, expected = pack_client
    other = next(
        word
        for word in load_content(ROOT / "content" / "courses" / "ja" / "starter.json").vocabulary
        if word.status == "published" and word.id != expected["word_id"]
    )
    response = client.post(
        "/api/v1/audio/speech",
        json={"course_id": COURSE, "item_id": other.id, "language": "en"},
    )
    assert response.status_code == 503
    assert response.json()["error"]["code"] == "audio_unavailable"
    assert "Bundled reference audio is unavailable" in response.json()["error"]["message"]


def test_missing_japanese_clip_returns_audio_unavailable(pack_client):
    client, expected = pack_client
    other = next(
        word
        for word in load_content(ROOT / "content" / "courses" / "ja" / "starter.json").vocabulary
        if word.status == "published" and word.id != expected["word_id"]
    )
    response = client.post(
        "/api/v1/audio/speech",
        json={"course_id": COURSE, "item_id": other.id},
    )
    assert response.status_code == 503
    assert response.json()["error"]["code"] == "audio_unavailable"


def test_provider_status_reports_the_bundled_pack(pack_client):
    client, _ = pack_client
    status = client.get("/api/v1/providers/status?course_id=" + COURSE).json()
    assert "tts" not in status
    assert status["audio_pack"]["bundled_reference"] is True
    assert status["audio_pack"]["bundled_reviewed"] is False
    assert status["audio_pack"]["course_version"] == VERSION
    assert status["ai"]["verified"] is False
    assert status["stt"]["verified"] is False


def test_listening_pack_hit_records_delivery_without_providers(pack_client):
    client, _ = pack_client
    session = start(
        client, "ja-audio-thanks-contexts", source_kind="listening", preview_draft=True
    )
    exercise = next(item for item in session["exercises"] if item.get("audio"))
    cue_id = exercise["audio"][0]["id"]
    body = {
        "request_id": str(uuid4()),
        "expected_revision": session["revision"],
        "speed": 1,
    }
    route = (
        f"/api/v1/sessions/{session['id']}/exercises/{exercise['id']}"
        f"/audio/{cue_id}"
    )
    response = client.post(route, json=body)
    assert response.status_code == 200, response.text
    saved = response.json()
    assert saved["source"] == "pack"
    assert saved["mime"] == "audio/mpeg"
    assert cue_id in saved["session"]["evidence"][exercise["id"]]["audio_cue_ids"]
    assert client.post(route, json=body).json() == saved


def test_review_card_pack_hit_uses_the_saved_word(pack_client):
    client, expected = pack_client
    card = client.post(
        "/api/v1/courses/ja-starter/review/cards",
        json={"item_id": expected["word_id"], "direction": "listening"},
    ).json()
    response = client.post(
        f"/api/v1/review/cards/{card['id']}/audio/reference", json={"speed": 1}
    )
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["source"] == "pack"
    assert body["mime"] == "audio/mpeg"
    assert base64.b64decode(body["audio_base64"]) == expected["word"]["data"]


def test_pack_rejects_unsafe_paths_and_duplicate_keys():
    item = _item("word", "word", "ja", "こんにちは", None)
    with pytest.raises(ValidationError):
        audio_pack.PackItem.model_validate({**item, "file": "../escape.mp3"})
    with pytest.raises(ValidationError):
        audio_pack.PackItem.model_validate({**item, "file": "C:/absolute.mp3"})
    manifest = {
        "format_version": 1,
        "course_id": COURSE,
        "course_version": VERSION,
        "source_sha256": "0" * 64,
        "generated_at": "2026-11-12T00:00:00Z",
        "status": "draft",
        "review": {},
        "engine": {
            "provider": "kokoro",
            "model": MODEL,
            "voice_ja": VOICE_JA,
            "voice_en": VOICE_EN,
            "format": "mp3",
            "sample_rate": 24000,
            "bitrate_kbps": 64,
        },
        "licenses": manifest_license(),
        "counts": {},
        "items": [item, item],
    }
    with pytest.raises(ValidationError):
        audio_pack.PackManifest.model_validate(manifest)


def manifest_license() -> list[dict]:
    return [
        {
            "id": "fixture",
            "source": "Synthetic fixture audio",
            "license": "test-only",
            "attribution": "test fixture",
        }
    ]


def _minimal_mp3() -> bytes:
    # Valid MPEG1 Layer III 128 kbps 44.1 kHz frames (>= 1024 bytes, >= 0.2s for mutagen).
    return (b"\xff\xfb\x90\x00" + b"\x00" * 413) * 10


def _write_pack_version(
    root: Path,
    course_id: str,
    version: str,
    items: list[dict],
    source_bytes: bytes,
    status: str = "draft",
) -> Path:
    pack_dir = root / course_id / version
    pack_dir.mkdir(parents=True, exist_ok=True)
    written: list[dict] = []
    for raw in items:
        item = dict(raw)
        data = item.pop("_data", None)
        if data is not None:
            path = pack_dir / item["file"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        written.append(item)
    manifest = {
        "format_version": 1,
        "course_id": course_id,
        "course_version": version,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "generated_at": "2026-11-12T00:00:00Z",
        "status": status,
        "review": {},
        "engine": {
            "provider": "kokoro",
            "model": MODEL,
            "voice_ja": VOICE_JA,
            "voice_en": VOICE_EN,
            "format": "mp3",
            "sample_rate": 24000,
            "bitrate_kbps": 64,
        },
        "licenses": manifest_license(),
        "counts": {
            "ja": sum(item["language"] == "ja" for item in written),
            "en": sum(item["language"] == "en" for item in written),
            "files": len(written),
            "total_bytes": sum(item["bytes"] for item in written),
            "total_seconds": len(written) * 0.5,
        },
        "items": written,
    }
    (pack_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return pack_dir


def _item_with_bytes(
    kind: str,
    item_id: str,
    language: str,
    text: str,
    override: str | None,
    data: bytes,
    cue_id: str | None = None,
    turn_id: str | None = None,
) -> dict:
    voice = VOICE_JA if language == "ja" else VOICE_EN
    key = audio_pack.pack_key(text, language, voice, MODEL, override)
    return {
        "key": key,
        "kind": kind,
        "item_id": item_id,
        "cue_id": cue_id,
        "turn_id": turn_id,
        "language": language,
        "text": text,
        "pronunciation_override": override,
        "file": f"{language}/{key[:2]}/{key}.mp3",
        "bytes": len(data),
        "duration_seconds": 0.5,
        "file_sha256": hashlib.sha256(data).hexdigest(),
        "_data": data,
    }


def _build_practice_test_course() -> CourseContent:
    def practice_ex(ex_id: str, ex_type: str, transcript: str) -> dict:
        skill = "speaking" if ex_type == "speaking" else "listening"
        base = {
            "id": ex_id,
            "type": ex_type,
            "prompt": f"Prompt {ex_id}",
            "objective": "Practice audio",
            "concepts": ["c1"],
            "difficulty": 1,
            "explanation": "Explanation",
            "hint": "Hint",
            "policy": {},
            "skill": skill,
            "audio": [{"id": "cue-1", "label": "Listen", "transcript": transcript}],
        }
        if ex_type != "speaking":
            base["answers"] = [transcript]
        return base

    raw = {
        "id": "ja-test",
        "version": "0.1.0",
        "title": "Test Course",
        "language": "ja",
        "teaching_language": "en",
        "description": "Course fixture for audio pack script tests",
        "status": "published",
        "review_note": "Fixture",
        "licenses": [
            {
                "id": "lic-1",
                "source": "Trilingo fixture",
                "license": "CC-BY-4.0",
                "attribution": "Trilingo",
            }
        ],
        "stages": [
            {
                "id": "s1",
                "title": "Stage 1",
                "release": "0.1.0",
                "can_do": ["Greet"],
                "status": "published",
                "word_target": 1,
                "kanji_target": 0,
            }
        ],
        "concepts": [{"id": "c1", "title": "Concept 1", "explanation": "Basic"}],
        "vocabulary": [
            {
                "id": "w1",
                "surface": "私",
                "reading": "わたし",
                "gloss": "I",
                "part_of_speech": "pronoun",
                "register": "polite",
                "example": [{"surface": "私"}],
                "concepts": ["c1"],
                "stage": "s1",
                "status": "published",
                "pronunciation_override": "わたしわ",
                "practice_exercise_ids": ["p-vocab"],
            }
        ],
        "units": [
            {
                "id": "u1",
                "title": "Unit 1",
                "japanese_title": "ユニット1",
                "description": "Unit 1",
                "guide": "Guide",
                "order": 1,
                "stage": "s1",
                "status": "published",
                "lessons": [
                    {
                        "id": "l1",
                        "title": "Lesson 1",
                        "japanese_title": "レッスン1",
                        "objective": "Objective",
                        "order": 1,
                        "status": "published",
                        "exercises": [
                            {
                                "id": "e1",
                                "type": "multiple_choice",
                                "prompt": "Choose",
                                "objective": "Choose",
                                "concepts": ["c1"],
                                "difficulty": 1,
                                "explanation": "Exp",
                                "hint": "Hint",
                                "policy": {},
                                "skill": "recognition",
                                "choices": [
                                    {"id": "a", "text": "A"},
                                    {"id": "b", "text": "B"},
                                ],
                                "answer": "a",
                            }
                        ],
                    }
                ],
            }
        ],
        "characters": [
            {
                "id": "ch1",
                "surface": "あ",
                "script": "hiragana",
                "contextual_readings": ["a"],
                "stage": "s1",
                "concepts": ["c1"],
                "practice_exercise_ids": ["p-char"],
                "status": "published",
            }
        ],
        "grammar_notes": [
            {
                "id": "g1",
                "title": "Grammar 1",
                "explanation": "Explanation",
                "examples": [[{"surface": "あ"}]],
                "concepts": ["c1"],
                "register_note": "polite",
                "unit_ids": ["u1"],
                "practice_exercise_ids": ["p-grammar"],
                "status": "published",
            }
        ],
        "narratives": [
            {
                "id": "n-pub",
                "kind": "story",
                "title": "Published Story",
                "stage": "s1",
                "difficulty": 1,
                "objectives": ["Listen"],
                "turns": [
                    {
                        "id": "t1",
                        "speaker": "Aki",
                        "text": [{"surface": "今日は"}],
                        "pronunciation_override": "きょうは",
                        "exercise_ids": ["p-story-turn"],
                    }
                ],
                "concepts": ["c1"],
                "vocabulary_ids": ["w1"],
                "speaking_exercise_ids": ["p-story-speak"],
                "recap_exercise_ids": ["p-story-recap"],
                "status": "published",
            },
            {
                "id": "n-draft",
                "kind": "story",
                "title": "Draft Story",
                "stage": "s1",
                "difficulty": 1,
                "objectives": ["Listen"],
                "turns": [{"id": "t2", "speaker": "Haru", "text": [{"surface": "またね"}]}],
                "concepts": ["c1"],
                "vocabulary_ids": ["w1"],
                "speaking_exercise_ids": ["p-draft-speak"],
                "status": "draft",
            },
        ],
        "writing_tasks": [
            {
                "id": "wt1",
                "exercise_ids": ["p-writing"],
                "stage": "s1",
                "genre": "note",
                "prompt": "Write",
                "model": "私",
                "alternatives": [],
                "checklist": ["check"],
                "status": "published",
                "rubric_version": "1",
            }
        ],
        "assessment_banks": [
            {
                "id": "ab1",
                "kind": "recap",
                "title": "Bank",
                "concepts": ["c1"],
                "exercise_ids": ["p-bank"],
                "scoring_policy": "any",
                "status": "published",
            }
        ],
        "practice_exercises": [
            practice_ex("p-story-speak", "speaking", "話す練習一"),
            practice_ex("p-story-recap", "dictation", "復習練習二"),
            practice_ex("p-story-turn", "dictation", "会話練習三"),
            practice_ex("p-grammar", "dictation", "文法練習四"),
            practice_ex("p-char", "dictation", "文字練習五"),
            practice_ex("p-vocab", "dictation", "語彙練習六"),
            practice_ex("p-writing", "dictation", "作文練習七"),
            practice_ex("p-bank", "dictation", "テスト練習八"),
            practice_ex("p-draft-speak", "speaking", "下書き練習九"),
            practice_ex("p-standalone", "dictation", "独立練習十"),
        ],
    }
    return CourseContent.model_validate(raw)


def test_provider_status_rejects_course_id_traversal_without_probing_parent(
    database, tmp_path, monkeypatch
):
    audio_pack.clear_cache()
    content = load_content(ROOT / "content" / "courses" / "ja" / "starter.json")
    source_bytes = (ROOT / "content" / "courses" / "ja" / "starter.json").read_bytes()
    word = next(w for w in content.vocabulary if w.status == "published")
    pack_root = tmp_path / "audio_pack"
    pack_root.mkdir(parents=True, exist_ok=True)
    outside = tmp_path / "outside"
    _write_pack_version(
        tmp_path,
        "outside",
        "0.1.0",
        [_item_with_bytes("word", word.id, "ja", word.surface, None, b"outside")],
        source_bytes,
    )
    _write_pack_version(
        tmp_path,
        ".",
        "0.1.0",
        [_item_with_bytes("word", word.id, "ja", word.surface, None, b"root")],
        source_bytes,
    )
    probed: list[Path] = []
    real_iterdir = Path.iterdir

    def tracked_iterdir(self: Path):
        probed.append(self.resolve())
        return real_iterdir(self)

    monkeypatch.setattr(Path, "iterdir", tracked_iterdir)
    app = create_app(
        Config(database_url=database, audio_pack_dir=pack_root, audio_pack_enabled=True)
    )
    with TestClient(app) as client:
        with app.state.session_factory() as db:
            import_content(db, content)
        for bad_id in [
            "../outside",
            "../../outside",
            str(outside),
            "C:\\Windows\\System32",
            "..",
            ".",
            "ja-starter/../../outside",
        ]:
            response = client.get("/api/v1/providers/status", params={"course_id": bad_id})
            assert response.status_code == 200
            payload = response.json()
            assert "tts" not in payload
            pack = payload["audio_pack"]
            assert pack["bundled_reference"] is False
            assert pack["bundled_reviewed"] is False
            assert pack["course_version"] is None
    assert probed == []
    audio_pack.clear_cache()


def test_speech_respects_preferred_version_and_slow_speed_returns_pack(database, tmp_path):
    audio_pack.clear_cache()
    content = load_content(ROOT / "content" / "courses" / "ja" / "starter.json")
    source_bytes = (ROOT / "content" / "courses" / "ja" / "starter.json").read_bytes()
    word = next(w for w in content.vocabulary if w.status == "published")
    pack_root = tmp_path / "audio_pack"
    v_current = b"ID3 clip current version"
    v_newer = b"ID3 clip newer version"
    _write_pack_version(
        pack_root,
        COURSE,
        VERSION,
        [
            _item_with_bytes(
                "word", word.id, "ja", word.surface, word.pronunciation_override, v_current
            )
        ],
        source_bytes,
    )
    _write_pack_version(
        pack_root,
        COURSE,
        "99.0.0",
        [
            _item_with_bytes(
                "word", word.id, "ja", word.surface, word.pronunciation_override, v_newer
            )
        ],
        source_bytes,
    )
    assert sorted(
        ["1.0.0", "1.0.0-alpha", "0.10.0", "0.2.0"], key=audio_pack._version_key
    ) == ["0.2.0", "0.10.0", "1.0.0", "1.0.0-alpha"]

    app = create_app(
        Config(database_url=database, audio_pack_dir=pack_root, audio_pack_enabled=True)
    )
    with TestClient(app) as client:
        with sessions(app.state.engine)() as db:
            import_content(db, content)
        slow = client.post(
            "/api/v1/audio/speech",
            json={"course_id": COURSE, "item_id": word.id, "speed": 0.75},
        )
        assert slow.status_code == 200, slow.text
        body = slow.json()
        assert body["source"] == "pack"
        assert body["mime"] == "audio/mpeg"
        assert base64.b64decode(body["audio_base64"]) == v_current

        updated = content.model_copy(deep=True)
        updated.version = "99.0.0"
        with sessions(app.state.engine)() as db:
            import_content(db, updated)
        switched = client.post(
            "/api/v1/audio/speech",
            json={"course_id": COURSE, "item_id": word.id, "speed": 1.0},
        )
        assert switched.status_code == 200, switched.text
        assert base64.b64decode(switched.json()["audio_base64"]) == v_newer
    audio_pack.clear_cache()


def test_story_turn_pack_hit_with_providers_disabled(database, tmp_path):
    audio_pack.clear_cache()
    content = load_content(ROOT / "content" / "courses" / "ja" / "starter.json")
    source_bytes = (ROOT / "content" / "courses" / "ja" / "starter.json").read_bytes()
    story = content.narratives[0]
    turn = story.turns[0]
    turn_text = "".join(segment.surface for segment in turn.text)
    turn_bytes = b"ID3 story turn clip"
    pack_root = tmp_path / "audio_pack"
    _write_pack_version(
        pack_root,
        COURSE,
        VERSION,
        [
            _item_with_bytes(
                "turn",
                story.id,
                "ja",
                turn_text,
                turn.pronunciation_override,
                turn_bytes,
                turn_id=turn.id,
            )
        ],
        source_bytes,
    )
    app = create_app(
        Config(database_url=database, audio_pack_dir=pack_root, audio_pack_enabled=True)
    )
    with TestClient(app) as client:
        with sessions(app.state.engine)() as db:
            import_content(db, content)
        response = client.post(
            "/api/v1/audio/speech",
            json={
                "course_id": COURSE,
                "item_id": story.id,
                "turn_id": turn.id,
                "preview_draft": True,
            },
        )
        assert response.status_code == 200, response.text
        body = response.json()
        assert body["source"] == "pack"
        assert body["mime"] == "audio/mpeg"
        assert base64.b64decode(body["audio_base64"]) == turn_bytes
    audio_pack.clear_cache()


def test_pronunciation_override_matching_hit_and_mismatch_miss(database, tmp_path):
    audio_pack.clear_cache()
    base = load_content(ROOT / "content" / "courses" / "ja" / "starter.json")
    modified = base.model_copy(deep=True)
    modified.version = "99.0.0"
    word = next(w for w in modified.vocabulary if w.status == "published")
    word.pronunciation_override = "こんにちはー"
    pack_root = tmp_path / "audio_pack"
    clip_bytes = b"ID3 override clip"
    _write_pack_version(
        pack_root,
        COURSE,
        "99.0.0",
        [_item_with_bytes("word", word.id, "ja", word.surface, "こんにちはー", clip_bytes)],
        b"source",
    )
    cfg = Config(database_url=database, audio_pack_dir=pack_root, audio_pack_enabled=True)
    app = create_app(cfg)
    with TestClient(app) as client:
        with sessions(app.state.engine)() as db:
            import_content(db, modified)
        hit = client.post(
            "/api/v1/audio/speech",
            json={"course_id": COURSE, "item_id": word.id},
        )
        assert hit.status_code == 200, hit.text
        assert hit.json()["source"] == "pack"
        assert base64.b64decode(hit.json()["audio_base64"]) == clip_bytes

        assert audio_pack.lookup(cfg, COURSE, word.surface, "ja", "こんにちはっ") is None
        assert audio_pack.lookup(cfg, COURSE, word.surface, "ja", None) is None

        diverged = modified.model_copy(deep=True)
        diverged.version = "99.0.1"
        diverged_word = next(w for w in diverged.vocabulary if w.id == word.id)
        diverged_word.pronunciation_override = "こんにちはっ"
        with sessions(app.state.engine)() as db:
            import_content(db, diverged)
        miss = client.post(
            "/api/v1/audio/speech",
            json={"course_id": COURSE, "item_id": word.id},
        )
        assert miss.status_code == 503
        assert miss.json()["error"]["code"] == "audio_unavailable"
    audio_pack.clear_cache()


def test_corrupt_sha256_size_mismatch_missing_clip_and_oversized_manifest_fallback(
    database, tmp_path, monkeypatch
):
    audio_pack.clear_cache()
    content = load_content(ROOT / "content" / "courses" / "ja" / "starter.json")
    source_bytes = (ROOT / "content" / "courses" / "ja" / "starter.json").read_bytes()
    word = next(w for w in content.vocabulary if w.status == "published")
    original = b"ID3 valid clip bytes"
    item = _item_with_bytes(
        "word", word.id, "ja", word.surface, word.pronunciation_override, original
    )
    pack_root = tmp_path / "audio_pack"
    pack_dir = _write_pack_version(pack_root, COURSE, VERSION, [item], source_bytes)
    clip_path = pack_dir / item["file"]

    app = create_app(
        Config(database_url=database, audio_pack_dir=pack_root, audio_pack_enabled=True)
    )
    with TestClient(app) as client:
        with sessions(app.state.engine)() as db:
            import_content(db, content)

        # Corrupt SHA-256 (exact same length, different bytes)
        clip_path.write_bytes(b"X" * len(original))
        audio_pack.clear_cache()
        corrupt = client.post(
            "/api/v1/audio/speech", json={"course_id": COURSE, "item_id": word.id}
        )
        assert corrupt.status_code == 503
        assert corrupt.json()["error"]["code"] == "audio_unavailable"

        # Size mismatch
        clip_path.write_bytes(b"short")
        audio_pack.clear_cache()
        sized = client.post("/api/v1/audio/speech", json={"course_id": COURSE, "item_id": word.id})
        assert sized.status_code == 503
        assert sized.json()["error"]["code"] == "audio_unavailable"

        # Missing clip file on disk
        clip_path.unlink()
        audio_pack.clear_cache()
        missing = client.post(
            "/api/v1/audio/speech", json={"course_id": COURSE, "item_id": word.id}
        )
        assert missing.status_code == 503
        assert missing.json()["error"]["code"] == "audio_unavailable"

        # Oversized manifest ignored cleanly
        clip_path.write_bytes(original)
        audio_pack.clear_cache()
        monkeypatch.setattr(audio_pack, "MAX_MANIFEST_BYTES", 10)
        oversized = client.post(
            "/api/v1/audio/speech", json={"course_id": COURSE, "item_id": word.id}
        )
        assert oversized.status_code == 503
        assert oversized.json()["error"]["code"] == "audio_unavailable"
    audio_pack.clear_cache()


def test_transcriptions_rejects_english_with_422(pack_client):
    client, expected = pack_client
    response = client.post(
        "/api/v1/audio/transcriptions",
        json={
            "course_id": COURSE,
            "item_id": expected["word_id"],
            "language": "en",
            "audio_base64": "invalid",
        },
    )
    assert response.status_code == 422
    error = response.json()["error"]
    assert error["code"] == "audio_reference"
    assert "Japanese transcript comparison" in error["message"]


def test_provider_status_bundled_reviewed_reflects_manifest_status(database, tmp_path):
    audio_pack.clear_cache()
    content = load_content(ROOT / "content" / "courses" / "ja" / "starter.json")
    source_bytes = (ROOT / "content" / "courses" / "ja" / "starter.json").read_bytes()
    word = next(w for w in content.vocabulary if w.status == "published")
    item = _item_with_bytes(
        "word", word.id, "ja", word.surface, word.pronunciation_override, b"ID3"
    )
    pack_root = tmp_path / "audio_pack"
    _write_pack_version(pack_root, COURSE, VERSION, [item], source_bytes, status="draft")

    app = create_app(
        Config(database_url=database, audio_pack_dir=pack_root, audio_pack_enabled=True)
    )
    with TestClient(app) as client:
        with sessions(app.state.engine)() as db:
            import_content(db, content)
        draft_status = client.get("/api/v1/providers/status", params={"course_id": COURSE}).json()
        assert "tts" not in draft_status
        assert draft_status["audio_pack"]["bundled_reference"] is True
        assert draft_status["audio_pack"]["bundled_reviewed"] is False
        assert draft_status["audio_pack"]["course_version"] == VERSION
        assert "bundled_reviewed" not in draft_status["ai"]
        assert "bundled_reviewed" not in draft_status["stt"]

        _write_pack_version(pack_root, COURSE, VERSION, [item], source_bytes, status="reviewed")
        audio_pack.clear_cache()
        reviewed_status = client.get(
            "/api/v1/providers/status", params={"course_id": COURSE}
        ).json()
        assert reviewed_status["audio_pack"]["bundled_reference"] is True
        assert reviewed_status["audio_pack"]["bundled_reviewed"] is True
        assert reviewed_status["audio_pack"]["course_version"] == VERSION
        assert "bundled_reviewed" not in reviewed_status["ai"]
        assert "bundled_reviewed" not in reviewed_status["stt"]
    audio_pack.clear_cache()


def test_speakable_items_practice_exercise_required_flags():
    scripts_dir = str(ROOT / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import audio_pack_common

    content = _build_practice_test_course()
    items = audio_pack_common.speakable_items(content, VOICE_JA, VOICE_EN, MODEL)
    by_item_id = {
        entry["item_id"]: entry["required"]
        for entry in items.values()
        if entry["kind"] == "cue"
    }
    for required_id in [
        "p-story-speak",
        "p-story-recap",
        "p-story-turn",
        "p-grammar",
        "p-char",
        "p-vocab",
        "p-writing",
        "p-bank",
    ]:
        assert by_item_id[required_id] is True, required_id
    assert by_item_id["p-draft-speak"] is False
    assert by_item_id["p-standalone"] is False


def test_build_and_check_audio_pack_scripts(tmp_path, monkeypatch, capsys):
    scripts_dir = str(ROOT / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import build_audio_pack
    import check_audio_pack

    course = _build_practice_test_course()
    course_file = tmp_path / "course.json"
    course_file.write_text(course.model_dump_json(by_alias=True, indent=2), encoding="utf-8")
    out_root = tmp_path / "audio_out"

    recorded_inputs: list[tuple[str, str]] = []
    mp3_bytes = _minimal_mp3()

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.url.host == "127.0.0.1"
        assert request.url.path == "/v1/audio/speech"
        payload = json.loads(request.content)
        recorded_inputs.append((payload["voice"], payload["input"]))
        return httpx.Response(200, content=mp3_bytes, headers={"content-type": "audio/mpeg"})

    real_client = httpx.Client
    monkeypatch.setattr(
        build_audio_pack.httpx,
        "Client",
        lambda **kwargs: real_client(transport=httpx.MockTransport(handle), **kwargs),
    )

    build_args = argparse.Namespace(
        course=course_file,
        output=out_root,
        version=None,
        base_url="http://127.0.0.1:8880",
        model=MODEL,
        voice_ja=VOICE_JA,
        voice_en=VOICE_EN,
        timeout=10.0,
        retries=0,
        sample_rate=24000,
        bitrate_kbps=64,
        force=False,
        dry_run=False,
        progress=False,
        limit=None,
        license=build_audio_pack.DEFAULT_LICENSE,
    )
    report = build_audio_pack.build_pack(build_args)
    pack_dir = Path(report["pack"])
    assert list(pack_dir.rglob("*.tmp")) == []

    spoken_texts = [text for _, text in recorded_inputs]
    assert "わたしわ" in spoken_texts
    assert "私" not in spoken_texts
    assert "きょうは" in spoken_texts
    assert "今日は" not in spoken_texts

    manifest_data = json.loads((pack_dir / "manifest.json").read_text(encoding="utf-8"))
    word_entry = next(entry for entry in manifest_data["items"] if entry["kind"] == "word")
    assert word_entry["text"] == "私"
    assert word_entry["pronunciation_override"] == "わたしわ"
    turn_entry = next(entry for entry in manifest_data["items"] if entry["kind"] == "turn")
    assert turn_entry["text"] == "今日は"
    assert turn_entry["pronunciation_override"] == "きょうは"

    # Strict check passes cleanly on generated pack
    check_args = argparse.Namespace(course=course_file, pack=pack_dir, strict=True)
    clean_report = check_audio_pack.check(check_args)
    assert clean_report["ok"] is True
    assert clean_report["counts"]["unreferenced"] == 0
    assert clean_report["errors"] == []
    assert clean_report["warnings"] == []

    # Unreferenced MP3 file on disk produces warning normally and error under --strict
    stray = pack_dir / "ja" / "00" / "stray.mp3"
    stray.parent.mkdir(parents=True, exist_ok=True)
    stray.write_bytes(mp3_bytes)
    non_strict = check_audio_pack.check(
        argparse.Namespace(course=course_file, pack=pack_dir, strict=False)
    )
    assert non_strict["ok"] is True
    assert non_strict["counts"]["unreferenced"] == 1
    assert non_strict["warnings"] == ["Unreferenced MP3 file in pack: ja/00/stray.mp3"]

    strict_report = check_audio_pack.check(
        argparse.Namespace(course=course_file, pack=pack_dir, strict=True)
    )
    assert strict_report["ok"] is False
    assert strict_report["counts"]["unreferenced"] == 1
    assert "Unreferenced MP3 file in pack: ja/00/stray.mp3" in strict_report["errors"]

    # Malformed manifest JSON and schema-invalid manifest emit structured JSON and exit 1
    for bad_text in ["{not valid json", "{}"]:
        (pack_dir / "manifest.json").write_text(bad_text, encoding="utf-8")
        monkeypatch.setattr(
            sys,
            "argv",
            ["check_audio_pack.py", "--course", str(course_file), "--pack", str(pack_dir)],
        )
        capsys.readouterr()
        with pytest.raises(SystemExit) as exc_info:
            check_audio_pack.main()
        assert exc_info.value.code == 1
        emitted = json.loads(capsys.readouterr().out)
        assert emitted["ok"] is False
        assert len(emitted["errors"]) == 1
