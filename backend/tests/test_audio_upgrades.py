import json

from alembic import command
from alembic.config import Config as AlembicConfig
from sqlalchemy import select, text
from test_learning import act, start
from test_learning import course as course

from app.db import make_engine, sessions
from app.learning_models import StudyEvent
from app.models import Profile
from app.review_models import QuestAssignment


def test_populated_0010_quest_definitions_preserved(tmp_path, monkeypatch):
    url = "sqlite:///" + (tmp_path / "quest-upgrade.db").as_posix()
    monkeypatch.setenv("DATABASE_URL", url)
    config = AlembicConfig("alembic.ini")
    command.upgrade(config, "0010")
    engine = make_engine(url)
    with sessions(engine)() as db:
        db.add(Profile(id="local", name="Preserved learner", timezone="Asia/Singapore"))
        db.flush()
        db.execute(
            text("""INSERT INTO quest_assignments
            (id,profile_id,kind,target,created_at,baseline_ids,completed_at,source_ids)
            VALUES (:id,'local','writing',3,'2026-10-23T00:00:00+00:00',
            :baseline,NULL,:sources)"""),
            {
                "id": "old-writing-quest",
                "baseline": json.dumps(["baseline-event"]),
                "sources": json.dumps(["prior-writing-event"]),
            },
        )
        db.commit()
    command.upgrade(config, "head")
    command.check(config)
    with sessions(engine)() as db:
        row = db.get(QuestAssignment, "old-writing-quest")
        assert row.kind == row.original_kind == "writing"
        assert row.target == 3 and row.source_ids == ["prior-writing-event"]
        assert row.baseline_ids == ["baseline-event"] and row.completed_at is None
        assert row.revision == 0 and row.definition_history == []
        assert db.get(Profile, "local").name == "Preserved learner"
        assert db.execute(text("SELECT COUNT(*) FROM audio_deliveries")).scalar_one() == 0
    engine.dispose()


def test_legacy_session_receipt_accepts_additive_audio_evidence(client, course):
    session = start(client)
    key = session["next_action_id"]
    exercise = session["exercises"][0]["id"]
    saved = act(client, session, "skip", exercise)
    with sessions(client.app.state.engine)() as db:
        event = db.scalar(select(StudyEvent).where(StudyEvent.request_id == key))
        response = dict(event.response)
        response["evidence"] = {
            eid: {
                field: value
                for field, value in item.items()
                if field
                not in {
                    "audio_cue_ids",
                    "text_fallback",
                    "speech_reference_delivered",
                    "speech_attempts",
                    "transcript_matches",
                    "last_transcript",
                    "last_transcript_matches",
                    "typed_fallbacks",
                }
            }
            for eid, item in response["evidence"].items()
        }
        event.response = response
        db.commit()
    repeated = client.post(
        f"/api/v1/sessions/{session['id']}/actions",
        json={"request_id": key, "expected_revision": 0, "action": "skip", "exercise_id": exercise},
    )
    assert repeated.status_code == 200, repeated.text
    assert repeated.json() == saved
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_populated_0012_speaking_contract_preserves_original_json_and_receipts(
    tmp_path, monkeypatch
):
    from pathlib import Path
    from uuid import uuid4

    from app.config import ROOT
    from app.learning import start_session
    from app.learning_models import StudySession
    from app.learning_schemas import StartRequest
    from app.services import import_content, load_content

    url = "sqlite:///" + (tmp_path / "speaking-upgrade.db").as_posix()
    monkeypatch.setenv("DATABASE_URL", url)
    config = AlembicConfig("alembic.ini")
    command.upgrade(config, "0012")
    engine = make_engine(url)
    with sessions(engine)() as db:
        import_content(db, load_content(Path(ROOT) / "content/courses/ja/starter.json"))
        saved = start_session(
            db,
            "ja-starter",
            StartRequest(
                request_id=str(uuid4()),
                source_id="ja-greetings-hello",
            ),
        )
        row = db.get(StudySession, saved["id"])
        # Represent a pre-speaking session without retroactive activity claims.
        row.evidence = {
            key: {
                field: value
                for field, value in item.items()
                if field
                not in {
                    "speech_reference_delivered",
                    "speech_attempts",
                    "transcript_matches",
                    "last_transcript",
                    "last_transcript_matches",
                    "typed_fallbacks",
                }
            }
            for key, item in row.evidence.items()
        }
        db.commit()
        before = db.execute(text("SELECT evidence, metadata_json FROM study_sessions")).all()
        receipts = db.execute(text("SELECT request, response FROM study_events")).all()
    command.upgrade(config, "head")
    command.check(config)
    with sessions(engine)() as db:
        assert (
            db.execute(text("SELECT evidence, metadata_json FROM study_sessions")).all() == before
        )
        assert db.execute(text("SELECT request, response FROM study_events")).all() == receipts
        assert db.execute(text("SELECT COUNT(*) FROM xp_ledger")).scalar_one() == 0
        assert db.execute(text("SELECT COUNT(*) FROM review_events")).scalar_one() == 0
    engine.dispose()


def test_populated_0013_removes_tts_settings_and_preserves_learner_data(tmp_path, monkeypatch):
    from fastapi.testclient import TestClient

    from app.config import Config
    from app.main import create_app
    from app.models import Preferences

    url = "sqlite:///" + (tmp_path / "tts-removal-upgrade.db").as_posix()
    monkeypatch.setenv("DATABASE_URL", url)
    config = AlembicConfig("alembic.ini")
    command.upgrade(config, "0013")
    engine = make_engine(url)

    legacy_prefs = {
        "daily_goal": 40,
        "show_goal": True,
        "furigana": "hidden",
        "romaji": False,
        "reduced_motion": False,
        "sound": False,
        "show_statistics": True,
        "practice_batch": 15,
        "interests": ["travel"],
        "preferred_focus": "mixed",
        "accent": "plum",
        "show_quests": True,
        "monthly_quest_target": 20,
        "show_timer": False,
        "show_reminder": False,
        "retention": 0.9,
        "ai": {
            "enabled": True,
            "provider": "lm-studio",
            "base_url": "http://127.0.0.1:1234",
            "model": "qwen-local",
            "voice": "unused-ai-voice",
            "timeout": 25,
        },
        "tts": {
            "enabled": True,
            "provider": "kokoro",
            "base_url": "http://127.0.0.1:8880",
            "model": "kokoro-v1",
            "voice": "jf_alpha",
            "timeout": 20,
        },
        "stt": {
            "enabled": True,
            "provider": "openai-compatible",
            "base_url": "http://127.0.0.1:9000",
            "model": "whisper-ja",
            "voice": "unused-stt-voice",
            "timeout": 30,
        },
    }
    legacy_delivery_provider = {
        "enabled": True,
        "provider": "kokoro",
        "base_url": "http://127.0.0.1:8880",
        "model": "kokoro-v1",
        "voice": "jf_alpha",
        "timeout": 20,
    }
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO profiles VALUES ('local', 'Kept learner', 'Asia/Tokyo')"))
        conn.execute(
            text("INSERT INTO preferences (profile_id, data) VALUES ('local', :data)"),
            {"data": json.dumps(legacy_prefs)},
        )
        conn.execute(text("INSERT INTO courses VALUES ('ja-starter', '0.1.21')"))
        conn.execute(
            text(
                "INSERT INTO course_versions "
                "VALUES ('ja-starter@0.1.21', 'ja-starter', '0.1.21', 'd', '{}')"
            )
        )
        conn.execute(
            text("""INSERT INTO study_sessions
            (id,profile_id,course_version_id,course_id,source_kind,source_id,kind,title,status,
             cursor,revision,next_action_id,exercise_ids,evidence,metadata_json,created_at,
             completed_at)
            VALUES ('s1','local','ja-starter@0.1.21','ja-starter','lesson','l1','lesson',
            'Lesson 1','completed',0,1,'next','[]','{}','{}',
            '2026-11-01T00:00:00+00:00','2026-11-01T00:05:00+00:00')""")
        )
        conn.execute(
            text("""INSERT INTO xp_ledger VALUES
            ('xp1','s1','local',15,'2026-11-01T00:05:00+00:00','2026-11-01','Asia/Tokyo')""")
        )
        conn.execute(
            text("""INSERT INTO audio_deliveries VALUES
            ('req1','s1','{"session_id":"s1"}',:provider,'{"id":"reference"}',
             '{"id":"s1"}','2026-11-01T00:01:00+00:00')"""),
            {"provider": json.dumps(legacy_delivery_provider)},
        )

    command.upgrade(config, "head")
    command.check(config)

    with sessions(engine)() as db:
        prefs = db.get(Preferences, "local")
        assert prefs is not None
        assert "tts" not in prefs.data
        assert "voice" not in prefs.data["ai"]
        assert "voice" not in prefs.data["stt"]
        assert prefs.data["daily_goal"] == 40
        assert prefs.data["furigana"] == "hidden"
        assert prefs.data["ai"]["model"] == "qwen-local"
        assert prefs.data["stt"]["model"] == "whisper-ja"
        assert db.get(Profile, "local").name == "Kept learner"
        assert db.execute(text("SELECT SUM(amount) FROM xp_ledger")).scalar_one() == 15
        assert db.execute(text("SELECT COUNT(*) FROM audio_deliveries")).scalar_one() == 1

    with TestClient(create_app(Config(database_url=url))) as upgraded:
        health = upgraded.get("/api/v1/health")
        assert health.status_code == 200
        assert health.json()["schema_version"] == "0014"
        loaded = upgraded.get("/api/v1/settings")
        assert loaded.status_code == 200, loaded.text
        assert loaded.json()["daily_goal"] == 40
        patched = upgraded.patch("/api/v1/settings", json={"daily_goal": 45})
        assert patched.status_code == 200, patched.text
        assert patched.json()["daily_goal"] == 45

    engine.dispose()
