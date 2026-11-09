from datetime import datetime, timedelta, timezone
from uuid import uuid4

import pytest
from test_learning import act, action_body
from test_learning import course as course
from test_review_progress import add

from app import learning, review

pytestmark = pytest.mark.usefixtures("course")


def open_timer(client, card, key=None):
    result = client.post(
        f"/api/v1/review/cards/{card['id']}/session", json={"request_id": key or str(uuid4())}
    )
    assert result.status_code == 200, result.text
    return result.json()


def test_optional_recall_time_pause_resume_restart_and_rating_idempotency(client, monkeypatch):
    now = datetime(2026, 10, 23, 7, tzinfo=timezone.utc)
    monkeypatch.setattr(review, "now_utc", lambda: now)
    monkeypatch.setattr(learning, "now_utc", lambda: now)
    card = add(client)
    key = str(uuid4())
    session = open_timer(client, card, key)
    assert open_timer(client, card, key) == session
    now += timedelta(seconds=11)
    session = act(client, session, "timer_pause")
    assert session["timer"]["elapsed_seconds"] == 11
    now += timedelta(days=100)
    assert client.get(f"/api/v1/sessions/{session['id']}").json()["timer"]["elapsed_seconds"] == 11
    session = act(client, session, "timer_resume")
    session = act(client, session, "timer_hide")
    now += timedelta(seconds=4)
    body = {
        "request_id": str(uuid4()),
        "expected_revision": card["revision"],
        "rating": "Good",
        "recall_session_id": session["id"],
    }
    route = f"/api/v1/review/cards/{card['id']}/ratings"
    saved = client.post(route, json=body)
    assert saved.status_code == 200, saved.text
    assert client.post(route, json=body).json() == saved.json()
    result = client.get(f"/api/v1/sessions/{session['id']}").json()
    assert result["status"] == "completed" and result["xp_awarded"] == 5
    assert result["timer"]["elapsed_seconds"] == 15 and not result["timer"]["running"]
    records = client.get("/api/v1/personal").json()["timing_records"]
    assert records[0]["id"] == session["id"] and records[0]["kind"] == "review"
    history = client.get("/api/v1/personal/timing?source_kind=review").json()
    record = history["records"][0]
    assert history["total"] == 1
    assert record["rating"] == "Good" and record["direction"] == card["direction"]
    assert record["paused_seconds"] == 100 * 86400
    assert record["elapsed_seconds"] == 15 and record["mode"] == "supported"
    assert client.get("/api/v1/personal").json()["objective_checks"] == 0
    assert (
        client.post(
            route,
            json={
                **body,
                "request_id": str(uuid4()),
                "expected_revision": saved.json()["revision"],
            },
        ).status_code
        == 409
    )
    assert client.get("/api/v1/progress").json()["total_xp"] == 5


def test_open_pause_skip_never_changes_schedule_or_rewards(client):
    card = add(client)
    session = open_timer(client, card)
    result = client.post(
        f"/api/v1/sessions/{session['id']}/actions", json=action_body(session, "finish")
    )
    assert result.status_code == 409 and result.json()["error"]["code"] == "review_rating"
    session = act(client, session, "pause")
    assert client.get(f"/api/v1/review/cards/{card['id']}").json() == card
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    assert client.get("/api/v1/personal").json()["timing_records"] == []
    assert client.get("/api/v1/personal/timing").json()["records"] == []
    assert client.get(f"/api/v1/sessions/{session['id']}").json()["status"] == "paused"


def test_recall_rating_rollback_keeps_original_timer_card_and_xp(client, monkeypatch):
    card = add(client)
    session = open_timer(client, card)
    body = {
        "request_id": str(uuid4()),
        "expected_revision": 0,
        "rating": "Good",
        "recall_session_id": session["id"],
    }
    with monkeypatch.context() as patch:

        def fail(*args):
            raise RuntimeError("credit rollback")

        patch.setattr(review, "credit_quests", fail)
        with pytest.raises(RuntimeError, match="credit rollback"):
            client.post(f"/api/v1/review/cards/{card['id']}/ratings", json=body)
    assert client.get(f"/api/v1/review/cards/{card['id']}").json() == card
    saved = client.get(f"/api/v1/sessions/{session['id']}").json()
    assert saved["status"] == "active" and saved["timer"]["running"]
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    assert client.post(f"/api/v1/review/cards/{card['id']}/ratings", json=body).status_code == 200
