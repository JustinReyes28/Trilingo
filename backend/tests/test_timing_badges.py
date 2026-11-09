from datetime import datetime, timedelta, timezone
from uuid import uuid4

import pytest
from test_learning import act, action_body, complete, skip_all, start
from test_learning import course as course

from app import learning
from app.db import sessions
from app.review_models import PersonalBadge

pytestmark = pytest.mark.usefixtures("course")


def test_elapsed_time_pause_resume_hide_no_expiry_and_invalid_clock(client, monkeypatch):
    now = datetime(2026, 10, 23, 5, tzinfo=timezone.utc)
    monkeypatch.setattr(learning, "now_utc", lambda: now)
    session = start(client)
    assert session["timer"] is None
    session = act(client, session, "timer_start")
    now += timedelta(seconds=17)
    session = act(client, session, "timer_pause")
    assert session["timer"]["elapsed_seconds"] == 17
    now += timedelta(days=100)
    session = act(client, session, "timer_resume")
    session = act(client, session, "timer_hide")
    assert not session["timer"]["visible"] and session["timer"]["running"]
    now += timedelta(seconds=3)
    session = act(client, session, "pause")
    assert session["timer"]["elapsed_seconds"] == 20
    session = act(client, session, "resume")
    assert not session["timer"]["running"]
    session = act(client, session, "timer_resume")
    now -= timedelta(seconds=10)
    session = act(client, session, "timer_pause")
    assert not session["timer"]["valid"]
    session = act(client, skip_all(client, session), "finish")
    assert session["xp_awarded"] == 20 and session["status"] == "completed"
    assert not session["timer"]["valid"]


def test_timing_retry_preference_and_completion_freeze(client, monkeypatch):
    assert client.patch("/api/v1/settings", json={"show_timer": True}).status_code == 200
    session = start(client)
    assert session["timer"]["running"]
    request = action_body(session, "timer_pause")
    url = "/api/v1/sessions/" + session["id"] + "/actions"
    paused = client.post(url, json=request).json()
    assert client.post(url, json=request).json() == paused
    completed = act(client, skip_all(client, paused), "finish")
    assert not completed["timer"]["running"]


def test_optional_monthly_badges_are_atomic_and_preserved_after_missed_days(client, monkeypatch):
    now = datetime(2026, 10, 23, 5, tzinfo=timezone.utc)
    monkeypatch.setattr(learning, "now_utc", lambda: now)
    client.patch("/api/v1/profile", json={"timezone": "Asia/Singapore"})
    client.patch("/api/v1/settings", json={"monthly_quest_target": 1})
    quest = client.post(
        "/api/v1/quests", json={"request_id": str(uuid4()), "target": 1, "kind": "sessions"}
    ).json()
    finished = complete(client)
    with sessions(client.app.state.engine)() as db:
        badge = db.get(PersonalBadge, ("local", "monthly-2026-10"))
        assert badge is not None and badge.details["target"] == 1
        assert badge.source_session_id == finished["id"]
    quests = client.get("/api/v1/quests").json()
    assert next(row for row in quests if row["id"] == quest["id"])["progress"] == 1
    before = client.get("/api/v1/personal").json()["badges"]
    now += timedelta(days=70)
    assert client.get("/api/v1/personal").json()["badges"] == before
    assert client.get("/api/v1/progress").json()["total_xp"] == 20
    assert client.get("/api/v1/courses/ja-starter/lessons/ja-greetings-hello").status_code == 200
    assert (
        client.patch(
            "/api/v1/settings", json={"show_quests": False, "show_statistics": False}
        ).status_code
        == 200
    )


def test_activity_calendar_local_dates_and_only_valid_saved_timing(client, monkeypatch):
    from app import review

    now = datetime(2026, 10, 23, 23, 59, tzinfo=timezone.utc)
    monkeypatch.setattr(learning, "now_utc", lambda: now)
    monkeypatch.setattr(review, "now_utc", lambda: now)
    client.patch("/api/v1/profile", json={"timezone": "Asia/Singapore"})
    client.patch("/api/v1/settings", json={"show_timer": True, "show_reminder": True})
    session = start(client)
    now += timedelta(seconds=9)
    session = act(client, skip_all(client, session), "finish")
    personal = client.get("/api/v1/personal").json()
    assert len(personal["activity_calendar"]) == 84
    assert personal["activity_calendar"][-1] == {"day": "2026-10-24", "xp": 20, "sessions": 1}
    assert personal["timing_records"][0]["id"] == session["id"]
    assert personal["timing_records"][0]["elapsed_seconds"] == 9
    assert personal["timing_records"][0]["skipped"] == len(session["exercises"])
    invalid = start(client)
    now -= timedelta(seconds=3)
    invalid = act(client, skip_all(client, invalid), "finish")
    personal = client.get("/api/v1/personal").json()
    assert len(personal["timing_records"]) == 1
    assert personal["activity_calendar"][-1]["xp"] == 25
    assert client.get("/api/v1/settings").json()["show_reminder"] is True
    assert client.patch("/api/v1/settings", json={"show_reminder": None}).status_code == 422
    client.patch("/api/v1/profile", json={"timezone": "UTC"})
    assert client.get("/api/v1/progress").json()["activity_dates"] == ["2026-10-24"]
