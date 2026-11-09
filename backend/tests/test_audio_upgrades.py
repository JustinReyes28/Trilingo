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
