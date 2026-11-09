from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import pytest
from alembic import command
from alembic.config import Config as AlembicConfig
from fastapi.testclient import TestClient
from fsrs import Card, Rating, Scheduler
from sqlalchemy import select, text
from test_learning import act, complete, start
from test_learning import course as course

from app import review
from app.config import Config
from app.db import make_engine, sessions
from app.main import create_app
from app.models import Profile
from app.review_models import ReviewCard, ReviewEvent
from app.services import import_content

pytestmark = pytest.mark.usefixtures("course")
BASE = "/api/v1/courses/ja-starter/review/cards"


def add(client, direction="meaning"):
    response = client.post(BASE, json={"item_id": "ja-word-hello", "direction": direction})
    assert response.status_code == 200, response.text
    return response.json()


def rate(client, card, rating="Good", request_id=None):
    payload = {
        "request_id": request_id or str(uuid4()),
        "expected_revision": card["revision"],
        "rating": rating,
    }
    return client.post(f"/api/v1/review/cards/{card['id']}/ratings", json=payload)


@pytest.mark.parametrize("rating", ["Again", "Hard", "Good", "Easy"])
def test_real_deterministic_fsrs_all_ratings_and_early_review(client, monkeypatch, rating):
    now = datetime(2026, 10, 23, 4, tzinfo=timezone.utc)
    monkeypatch.setattr(review, "now_utc", lambda: now)
    card = add(client)
    assert not card["scheduled"] and card["due"] is None
    response = rate(client, card, rating)
    assert response.status_code == 200, response.text
    saved = response.json()
    expected, _ = Scheduler(enable_fuzzing=False).review_card(
        Card(due=now), Rating[rating], review_datetime=now
    )
    for field in ("state", "step", "stability", "difficulty", "due", "last_review"):
        assert saved["state"][field] == expected.to_dict()[field]
    assert saved["revision"] == 1
    assert rate(client, saved, "Good").status_code == 200  # Future-due is deliberate and allowed.
    assert client.get("/api/v1/progress").json()["total_xp"] == 10


def test_duplicate_concurrent_receipts_stale_conflicts_and_browse_preserve_state(client, database):
    card = add(client)
    assert add(client)["id"] == card["id"]
    assert add(client, "reading")["id"] != card["id"]
    assert add(client, "typing")["id"] != card["id"]
    assert client.get(BASE).json()["total"] == 3
    with sessions(client.app.state.engine)() as db:
        before = deepcopy(db.get(ReviewCard, card["id"]).state)
    client.get(BASE + "?limit=1")
    assert client.get(BASE + "?limit=1&offset=1").json()["has_more"]
    with sessions(client.app.state.engine)() as db:
        assert db.get(ReviewCard, card["id"]).state == before
    key = str(uuid4())
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda _: rate(client, card, request_id=key), range(2)))
    assert all(result.status_code == 200 for result in results)
    assert results[0].json() == results[1].json()
    assert rate(client, card).status_code == 409
    assert client.get("/api/v1/progress").json()["total_xp"] == 5
    history = client.get(f"/api/v1/review/cards/{card['id']}/history").json()
    assert len(history) == 1 and history[0]["before"] == {}
    with TestClient(create_app(Config(database_url=database))) as restarted:
        assert restarted.get(BASE).json()["total"] == 3
        assert len(restarted.get(f"/api/v1/review/cards/{card['id']}/history").json()) == 1
    with sessions(client.app.state.engine)() as db:
        assert len(db.scalars(select(ReviewEvent)).all()) == 1


def test_real_learning_relearning_and_retention_snapshot(client, monkeypatch):
    now = datetime(2026, 10, 23, 4, tzinfo=timezone.utc)
    monkeypatch.setattr(review, "now_utc", lambda: now)
    card = add(client)
    for rating in ("Good", "Good", "Again", "Easy"):
        card = rate(client, card, rating).json()
        now = datetime.fromisoformat(card["due"]) + timedelta(seconds=1)
    assert card["state"]["last_review"]
    assert client.patch("/api/v1/settings", json={"retention": 0.85}).status_code == 200
    card = rate(client, card).json()
    assert card["scheduler"]["desired_retention"] == 0.85
    history = client.get(f"/api/v1/review/cards/{card['id']}/history").json()
    assert len(history) == 5
    assert {entry["after"]["state"] for entry in history} >= {1, 2, 3}


def test_optional_repeatable_quests_truthful_records_and_every_free_accent(client):
    for accent in ("path", "plum"):
        assert client.patch("/api/v1/settings", json={"accent": accent}).json()["accent"] == accent
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    key = str(uuid4())
    body = {"request_id": key, "kind": "reviews", "target": 2}
    quest = client.post("/api/v1/quests", json=body).json()
    assert quest["progress"] == 0
    complete(client)
    assert client.get("/api/v1/quests").json()[0]["progress"] == 0
    card = add(client)
    for _ in range(2):
        card = rate(client, card).json()
    quest = client.get("/api/v1/quests").json()[0]
    assert quest["progress"] == 2 and quest["completed_at"] and len(set(quest["source_ids"])) == 2
    assert client.post("/api/v1/quests", json=body).json() == quest
    for _ in range(5):
        body["request_id"] = str(uuid4())
        assert client.post("/api/v1/quests", json=body).json()["progress"] == 0
    personal = client.get("/api/v1/personal").json()
    assert personal["review_count"] == 2 and personal["quests_completed"] == 1
    assert personal["best_week_xp"] == 30
    assert client.get("/api/v1/courses/ja-starter/lessons/ja-greetings-hello").status_code == 200


def test_populated_0005_forward_upgrade_preserves_profile(tmp_path, monkeypatch):
    url = "sqlite:///" + (tmp_path / "phase789-upgrade.db").as_posix()
    monkeypatch.setenv("DATABASE_URL", url)
    config = AlembicConfig("alembic.ini")
    command.upgrade(config, "0005")
    engine = make_engine(url)
    with sessions(engine)() as db:
        db.add(Profile(id="local", name="Preserved learner", timezone="Asia/Singapore"))
        db.commit()
    command.upgrade(config, "head")
    command.check(config)
    with sessions(engine)() as db:
        assert db.get(Profile, "local").name == "Preserved learner"
        assert db.execute(text("SELECT COUNT(*) FROM review_cards")).scalar_one() == 0
    engine.dispose()


def test_snapshot_card_survives_content_update(client, course):
    card = add(client)
    revised = deepcopy(course)
    revised.version = "99.0.0"
    next(word for word in revised.vocabulary if word.id == card["item_id"]).gloss = "changed gloss"
    with sessions(client.app.state.engine)() as db:
        import_content(db, revised)
    assert client.get(BASE).json()["cards"][0]["answer"] == card["answer"]


def test_mistake_import_deduplicates_without_losing_history_or_scheduling(client):
    session = start(client)
    exercise = session["exercises"][0]
    session = act(client, session, "answer", exercise["id"], answer="c1")
    assert session["feedback"]["kind"] == "incorrect"
    before = client.get("/api/v1/courses/ja-starter/mistakes").json()
    response = client.post("/api/v1/courses/ja-starter/review/mistakes?limit=1").json()
    assert response["total"] == 1
    card = response["cards"][0]
    assert card["item_kind"] == "exercise" and not card["scheduled"]
    assert card["due"] is None and card["revision"] == 0
    assert (
        client.post("/api/v1/courses/ja-starter/review/mistakes?limit=1").json()["cards"][0] == card
    )
    assert client.get("/api/v1/courses/ja-starter/mistakes").json() == before
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    assert rate(client, card).status_code == 200
    assert client.get("/api/v1/progress").json()["total_xp"] == 5


def test_aggregate_objective_evidence_is_separate_from_self_ratings(client):
    session = start(client)
    first, second, third = session["exercises"][:3]
    session = act(client, session, "answer", first["id"], answer="c0")
    session = act(client, session, "skip", second["id"])
    session = act(client, session, "reveal", third["id"])
    card = add(client)
    assert rate(client, card).status_code == 200
    stats = client.get("/api/v1/personal").json()
    assert stats["objective_checks"] == stats["initial_correct"] == 1
    assert stats["assisted_prompts"] == stats["skipped_prompts"] == 1
    assert stats["review_directions"] == {"meaning": 1}


def test_0006_existing_card_upgrades_with_word_meaning_preserved(tmp_path, monkeypatch, course):
    import json

    from app.review import scheduler_config
    from app.services import local_profile

    url = "sqlite:///" + (tmp_path / "existing-review-0006.db").as_posix()
    monkeypatch.setenv("DATABASE_URL", url)
    config = AlembicConfig("alembic.ini")
    command.upgrade(config, "0006")
    engine = make_engine(url)
    state = Card(due=datetime(2026, 10, 23, tzinfo=timezone.utc)).to_dict()
    with sessions(engine)() as db:
        import_content(db, course)
        local_profile(db)
        db.execute(
            text("""INSERT INTO review_cards
            (id, profile_id, course_id, course_version_id, item_id, direction,
             state, due, revision, scheduler)
            VALUES (:id, 'local', :course, :snapshot, 'ja-word-hello', 'meaning',
                    :state, :due, 3, :scheduler)"""),
            {
                "id": "historical-card",
                "course": course.id,
                "snapshot": f"{course.id}@{course.version}",
                "state": json.dumps(state),
                "due": state["due"],
                "scheduler": json.dumps(scheduler_config()),
            },
        )
        db.commit()
    command.upgrade(config, "head")
    command.check(config)
    with sessions(engine)() as db:
        row = db.get(ReviewCard, "historical-card")
        assert row.item_kind == "word" and row.state == state and row.revision == 3
        assert row.due == state["due"]
    engine.dispose()


def test_failed_optional_credit_rolls_back_rating_schedule_log_xp_and_badges(client, monkeypatch):
    card = add(client)
    with monkeypatch.context() as patch:

        def fail(_db, _session):
            raise RuntimeError("simulated credit failure")

        patch.setattr(review, "credit_quests", fail)
        with pytest.raises(RuntimeError, match="simulated credit failure"):
            rate(client, card)
    after = client.get(BASE).json()["cards"][0]
    assert after == card
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    assert client.get("/api/v1/personal").json()["badges"] == []
    assert client.get(f"/api/v1/review/cards/{card['id']}/history").json() == []
    assert rate(client, card).status_code == 200


def test_legacy_word_rating_receipt_uses_additive_source_default(client):
    card = add(client)
    key = str(uuid4())
    saved = rate(client, card, request_id=key).json()
    # Reproduce an immutable receipt created before item_kind existed.
    with sessions(client.app.state.engine)() as db:
        event = db.get(ReviewEvent, key)
        event.response = {field: value for field, value in saved.items() if field != "item_kind"}
        db.commit()
    assert rate(client, card, request_id=key).json() == saved
    assert client.get("/api/v1/progress").json()["total_xp"] == 5
