from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config as AlembicConfig
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy import inspect

from app.config import Config
from app.db import make_engine, sessions
from app.main import create_app
from app.models import Profile


def test_health_and_settings_persist(client, database):
    assert client.get("/api/v1/health").json()["schema_version"] == "0013"
    profile = client.get("/api/v1/profile?timezone=Asia/Singapore").json()
    assert profile["timezone"] == "Asia/Singapore"
    assert (
        client.patch("/api/v1/profile", json={"name": "Aki", "timezone": "Asia/Tokyo"}).status_code
        == 200
    )
    value = client.patch(
        "/api/v1/settings", json={"daily_goal": None, "practice_batch": 5000, "furigana": "hidden"}
    )
    assert value.status_code == 200
    assert value.json()["practice_batch"] == 5000
    with TestClient(create_app(Config(database_url=database))) as restarted:
        assert restarted.get("/api/v1/profile").json()["name"] == "Aki"
        assert restarted.get("/api/v1/profile?timezone=UTC").json()["timezone"] == "Asia/Tokyo"
        assert restarted.get("/api/v1/settings").json()["daily_goal"] is None
        assert restarted.get("/api/v1/settings").json()["furigana"] == "hidden"


@pytest.mark.parametrize(
    "path,body",
    [
        ("profile", {"name": " "}),
        ("profile", {"timezone": "Not/AZone"}),
        ("profile", {"xp": 200}),
        ("settings", {"practice_batch": 0}),
        ("settings", {"daily_goal": 0}),
        ("settings", {"furigana": "invented"}),
        ("settings", {"show_goal": None}),
        ("settings", {"ai": {"base_url": "https://example.com"}}),
        ("settings", {"ai": {"base_url": "http://user:secret@localhost"}}),
    ],
)
def test_invalid_input(client, path, body):
    response = client.patch("/api/v1/" + path, json=body)
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "validation"
    assert "details" in response.json()["error"]


def test_invalid_detected_timezone(client):
    assert client.get("/api/v1/profile?timezone=invalid").status_code == 422


def test_local_cors_and_disabled_providers(client):
    response = client.get("/api/v1/health", headers={"Origin": "https://outside.example"})
    assert "access-control-allow-origin" not in response.headers
    allowed = client.get("/api/v1/health", headers={"Origin": "http://127.0.0.1:5173"})
    assert allowed.headers["access-control-allow-origin"] == "http://127.0.0.1:5173"
    assert response.json()["features"] == {
        "lessons": True,
        "ai": False,
        "tts": False,
        "stt": False,
    }


def test_migrations_missing_is_actionable(tmp_path):
    with TestClient(
        create_app(Config(database_url=f"sqlite:///{tmp_path.as_posix()}/empty.db"))
    ) as client:
        response = client.get("/api/v1/health")
        assert response.status_code == 503
        assert "migrations" in response.json()["error"]["message"]
        assert "Traceback" not in response.text


def test_populated_foundation_upgrade(tmp_path, monkeypatch):
    url = f"sqlite:///{tmp_path.as_posix()}/upgrade.db"
    monkeypatch.setenv("DATABASE_URL", url)
    alembic = AlembicConfig("alembic.ini")
    command.upgrade(alembic, "0001")
    engine = make_engine(url)
    with sessions(engine)() as db:
        db.add(Profile(id="preserved", name="Keep this", timezone="Asia/Singapore"))
        db.commit()
    command.upgrade(alembic, "head")
    command.check(alembic)
    with sessions(engine)() as db:
        assert db.get(Profile, "preserved").name == "Keep this"
    assert "courses" in inspect(engine).get_table_names()
    engine.dispose()


def test_config_rejects_external_db_and_cors():
    with pytest.raises(ValidationError):
        Config(database_url="postgresql://example/db")
    with pytest.raises(ValidationError):
        Config(cors_origins=["https://external.example"])


def test_request_limit_prevents_mutation(client):
    client.get("/api/v1/profile")
    response = client.patch(
        "/api/v1/profile",
        content=b'{"name":"' + b"x" * 70000 + b'"}',
        headers={"content-type": "application/json"},
    )
    assert response.status_code == 413
    assert response.json()["error"]["code"] == "request_too_large"
    assert client.get("/api/v1/profile").json()["name"] == "Learner"


def test_parallel_first_profile_setup(client):
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=4) as pool:
        responses = list(
            pool.map(lambda _: client.get("/api/v1/profile?timezone=Asia/Singapore"), range(4))
        )
    assert all(response.status_code == 200 for response in responses)
    assert all(response.json()["timezone"] == "Asia/Singapore" for response in responses)


def test_selected_fsrs_dependency_is_deterministic():
    from datetime import datetime, timezone

    from fsrs import Card, Rating, Scheduler

    now = datetime(2026, 10, 23, 0, 0, tzinfo=timezone.utc)
    for rating in Rating:
        scheduler = Scheduler(enable_fuzzing=False)
        first, _ = scheduler.review_card(Card(card_id=42, due=now), rating, review_datetime=now)
        second, _ = scheduler.review_card(Card(card_id=42, due=now), rating, review_datetime=now)
        assert (first.state, first.step, first.due, first.stability, first.difficulty) == (
            second.state,
            second.step,
            second.due,
            second.stability,
            second.difficulty,
        )
        assert first.due.tzinfo is not None


def test_future_migration_template(database, tmp_path):
    import shutil

    migration_copy = tmp_path / "migration-scripts"
    shutil.copytree(Path("migrations"), migration_copy)
    config = AlembicConfig("alembic.ini")
    config.set_main_option("script_location", str(migration_copy))
    revision = command.revision(config, message="temporary template smoke", autogenerate=True)
    assert Path(revision.path).is_file()
    assert "def upgrade()" in Path(revision.path).read_text()


def test_health_rejects_outdated_schema(tmp_path, monkeypatch):
    url = f"sqlite:///{tmp_path.as_posix()}/outdated.db"
    monkeypatch.setenv("DATABASE_URL", url)
    command.upgrade(AlembicConfig("alembic.ini"), "0001")
    with TestClient(create_app(Config(database_url=url))) as client:
        response = client.get("/api/v1/health")
        assert response.status_code == 503
        assert response.json()["error"]["code"] == "migrations_required"


def test_qa_mode_cannot_use_personal_database():
    with pytest.raises(ValidationError, match="disposable"):
        Config(qa_mode=True, database_url=Config.model_fields["database_url"].default)


def test_framework_errors_use_the_public_error_shape(client):
    missing = client.get("/api/v1/missing")
    assert missing.status_code == 404
    assert missing.json()["error"]["code"] == "not_found"
    wrong_method = client.post("/api/v1/settings", json={})
    assert wrong_method.status_code == 405
    assert wrong_method.json()["error"]["code"] == "method_not_allowed"


def test_unexpected_failure_is_logged_not_exposed(database, monkeypatch, caplog):
    from app import services

    def fail(_db):
        raise RuntimeError("test-only internal failure")

    monkeypatch.setattr(services, "list_courses", fail)
    with TestClient(
        create_app(Config(database_url=database)), raise_server_exceptions=False
    ) as client:
        response = client.get("/api/v1/courses")
    assert response.status_code == 500
    assert response.json()["error"]["code"] == "internal_error"
    assert "test-only" not in response.text
    assert "Unexpected local API failure" in caplog.text
