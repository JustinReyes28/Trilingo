"""Bounded fixture history regression; never uses a learner database."""

from datetime import datetime, timedelta, timezone

import pytest
from sqlalchemy import event, insert
from test_learning import course as course

from app import learning, review
from app.db import sessions
from app.learning_models import StudySession, XpEntry

pytestmark = pytest.mark.usefixtures("course")


def test_large_history_keeps_complete_totals_paginated_access_and_bounded_queries(
    client, course, monkeypatch
):
    now = datetime(2026, 10, 23, 12, tzinfo=timezone.utc)
    monkeypatch.setattr(learning, "now_utc", lambda: now)
    monkeypatch.setattr(review, "now_utc", lambda: now)
    client.get("/api/v1/profile?timezone=UTC")
    records, ledger = [], []
    for index in range(1200):
        instant = now - timedelta(minutes=index)
        identity = f"isolated-history-{index}"
        records.append(
            {
                "id": identity,
                "profile_id": "local",
                "course_id": course.id,
                "course_version_id": f"{course.id}@{course.version}",
                "source_kind": "fixture_history" if index % 2 == 0 else "fixture_other",
                "source_id": "fixture",
                "kind": "practice",
                "title": "Isolated history fixture",
                "status": "completed",
                "cursor": 0,
                "revision": 0,
                "next_action_id": f"unused-{index}",
                "exercise_ids": [],
                "evidence": {},
                "metadata_json": {
                    "preview_draft": False,
                    "mode": "supported",
                    "timer": {
                        "visible": False,
                        "active_since": None,
                        "elapsed_seconds": float(index + 1),
                        "valid": True,
                    },
                },
                "created_at": instant.isoformat(),
                "completed_at": instant.isoformat(),
            }
        )
        ledger.append(
            {
                "id": identity,
                "session_id": identity,
                "profile_id": "local",
                "amount": 5,
                "occurred_at": instant.isoformat(),
                "activity_date": instant.date().isoformat(),
                "timezone": "UTC",
            }
        )
    with sessions(client.app.state.engine)() as db:
        db.execute(insert(StudySession), records)
        db.execute(insert(XpEntry), ledger)
        db.commit()
    first = client.get("/api/v1/progress?limit=20").json()
    assert first["total_xp"] == 6000 and len(first["sessions"]) == 20 and first["has_more"]
    last = client.get("/api/v1/progress?offset=1190&limit=20").json()
    assert len(last["sessions"]) == 10 and not last["has_more"]
    assert (
        client.get("/api/v1/progress?limit=1200").json()["sessions"][-1]["id"]
        == "isolated-history-1199"
    )
    queries = []

    def track(_connection, _cursor, statement, _parameters, _context, _many):
        queries.append(statement)

    event.listen(client.app.state.engine, "before_cursor_execute", track)
    try:
        personal = client.get("/api/v1/personal").json()
    finally:
        event.remove(client.app.state.engine, "before_cursor_execute", track)
    assert sum(day["xp"] for day in personal["activity_calendar"]) == 6000
    assert sum(day["sessions"] for day in personal["activity_calendar"]) == 1200
    assert personal["objective_checks"] == personal["review_count"] == 0
    assert len(personal["timing_records"]) == 20
    assert personal["timing_records"][0]["id"] == "isolated-history-0"
    assert len(queries) <= 15, "Personal history must aggregate instead of fetching per session"
    first_page = client.get("/api/v1/personal/timing?limit=73").json()
    assert first_page["total"] == 1200 and first_page["previous_cursor"] is None
    assert first_page["records"][0]["paused_seconds"] is None  # Historical pauses are unknown.
    seen = [record["id"] for record in first_page["records"]]
    # A new completion must not shift older keyset pages or repeat an existing record.
    newest = {
        **records[0],
        "id": "new-completion",
        "completed_at": (now + timedelta(seconds=1)).isoformat(),
    }
    with sessions(client.app.state.engine)() as db:
        db.execute(insert(StudySession), [newest])
        db.commit()
    page = first_page
    while page["next_cursor"]:
        page = client.get(
            "/api/v1/personal/timing", params={"limit": 73, "cursor": page["next_cursor"]}
        ).json()
        seen.extend(record["id"] for record in page["records"])
    assert len(seen) == len(set(seen)) == 1200
    assert seen[-1] == "isolated-history-1199" and "new-completion" not in seen
    final = client.get("/api/v1/personal/timing?page=last&limit=20").json()
    assert final["records"][-1]["id"] == seen[-1] and final["next_cursor"] is None
    previous = client.get(
        "/api/v1/personal/timing",
        params={"page": "previous", "limit": 20, "cursor": final["previous_cursor"]},
    ).json()
    assert not {row["id"] for row in previous["records"]} & {row["id"] for row in final["records"]}
    filtered = client.get("/api/v1/personal/timing?source_kind=fixture_other&page=last").json()
    assert filtered["total"] == 600
    assert all(row["source_kind"] == "fixture_other" for row in filtered["records"])
    assert client.get("/api/v1/personal/timing?source_kind=missing").json() == {
        "records": [],
        "total": 0,
        "next_cursor": None,
        "previous_cursor": None,
    }
    for query in ("cursor=broken", "page=previous", "limit=101", "page=unknown"):
        assert client.get("/api/v1/personal/timing?" + query).status_code == 422


def test_timing_pages_keep_equal_timestamp_records_reachable_after_new_completion(client, course):
    """Timestamp ties must not lose/repeat records in either navigation direction."""
    instant = "2026-10-23T12:00:00+00:00"
    client.get("/api/v1/profile?timezone=UTC")

    def add_fixture(identity):
        with sessions(client.app.state.engine)() as db:
            db.add(
                StudySession(
                    id=identity,
                    profile_id="local",
                    course_id=course.id,
                    course_version_id=f"{course.id}@{course.version}",
                    source_kind="fixture_tied_history",
                    source_id="fixture",
                    kind="practice",
                    title="Isolated equal-timestamp fixture",
                    status="completed",
                    cursor=0,
                    revision=0,
                    next_action_id=f"unused-{identity}",
                    exercise_ids=[],
                    evidence={},
                    metadata_json={
                        "preview_draft": False,
                        "mode": "supported",
                        "timer": {
                            "visible": False,
                            "active_since": None,
                            "elapsed_seconds": 10.0,
                            "paused_seconds": 3.0,
                            "valid": True,
                        },
                    },
                    created_at=instant,
                    completed_at=instant,
                )
            )
            db.flush()
            db.add(
                XpEntry(
                    id=identity,
                    session_id=identity,
                    profile_id="local",
                    amount=5,
                    occurred_at=instant,
                    activity_date="2026-10-23",
                    timezone="UTC",
                )
            )
            db.commit()

    for identity in ("tie-a", "tie-c", "tie-b", "tie-d"):
        add_fixture(identity)
    route = "/api/v1/personal/timing"
    first = client.get(route, params={"limit": 2}).json()
    assert [row["id"] for row in first["records"]] == ["tie-d", "tie-c"]
    assert first["total"] == 4 and first["previous_cursor"] is None
    add_fixture("tie-e")
    second = client.get(route, params={"limit": 2, "cursor": first["next_cursor"]}).json()
    assert [row["id"] for row in second["records"]] == ["tie-b", "tie-a"]
    assert second["total"] == 5 and second["next_cursor"] is None
    previous = client.get(
        route,
        params={
            "limit": 2,
            "page": "previous",
            "cursor": second["previous_cursor"],
        },
    ).json()
    assert [row["id"] for row in previous["records"]] == ["tie-d", "tie-c"]
    last = client.get(route, params={"limit": 2, "page": "last"}).json()
    assert last["records"] == second["records"] and last["next_cursor"] is None
    refreshed = client.get(route, params={"limit": 2}).json()
    assert [row["id"] for row in refreshed["records"]] == ["tie-e", "tie-d"]
    assert all(row["paused_seconds"] == 3.0 for row in refreshed["records"])
    assert client.get("/api/v1/progress").json()["total_xp"] == 25
