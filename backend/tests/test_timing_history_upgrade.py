"""Forward upgrades preserve timer evidence and immutable completion receipts."""

import json

from alembic import command
from alembic.config import Config
from sqlalchemy import inspect, text

from app.db import make_engine


def test_populated_0011_timer_metadata_receipts_and_ledger_preserved(tmp_path, monkeypatch):
    url = "sqlite:///" + (tmp_path / "timing-upgrade.db").as_posix()
    monkeypatch.setenv("DATABASE_URL", url)
    config = Config("alembic.ini")
    command.upgrade(config, "0011")
    engine = make_engine(url)
    metadata = {
        "timer": {"elapsed_seconds": 42, "valid": True, "active_since": None, "visible": False}
    }
    receipt = {"timer": metadata["timer"], "xp_awarded": 5, "id": "session"}
    with engine.begin() as db:
        db.execute(text("INSERT INTO profiles VALUES ('local','Kept learner','UTC')"))
        db.execute(text("INSERT INTO courses VALUES ('course','1.0.0')"))
        db.execute(
            text("INSERT INTO course_versions VALUES ('version','course','1.0.0','digest','{}')")
        )
        db.execute(
            text("""INSERT INTO study_sessions
            (id,profile_id,course_version_id,course_id,source_kind,source_id,kind,title,status,
             cursor,revision,next_action_id,exercise_ids,evidence,metadata_json,created_at,completed_at)
            VALUES ('session','local','version','course','review','card','review','Kept',
            'completed',
            0,1,'next','[]','{}',:metadata,'2026-10-23T00:00:00+00:00','2026-10-23T00:01:00+00:00')"""),
            {"metadata": json.dumps(metadata)},
        )
        db.execute(
            text("""INSERT INTO study_events VALUES
            ('event','request','session','{}',:response,'2026-10-23T00:01:00+00:00')"""),
            {"response": json.dumps(receipt)},
        )
        db.execute(
            text("""INSERT INTO xp_ledger VALUES
            ('xp','session','local',5,'2026-10-23T00:01:00+00:00','2026-10-23','UTC')""")
        )
    command.upgrade(config, "head")
    command.check(config)
    with engine.connect() as db:
        assert json.loads(db.scalar(text("SELECT metadata_json FROM study_sessions"))) == metadata
        assert json.loads(db.scalar(text("SELECT response FROM study_events"))) == receipt
        assert db.scalar(text("SELECT SUM(amount) FROM xp_ledger")) == 5
        assert db.scalar(text("SELECT name FROM profiles")) == "Kept learner"
    assert "ix_study_timing_history" in {
        item["name"] for item in inspect(engine).get_indexes("study_sessions")
    }
    engine.dispose()
