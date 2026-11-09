from copy import deepcopy
from uuid import uuid4

from test_learning import act, skip_all, start
from test_learning import course as course

from app.db import sessions
from app.services import import_content


def test_cold_start_and_later_stage_coverage_never_imply_assessment(client, course):
    personal = client.get("/api/v1/personal").json()
    assert personal["skill_evidence"] == {} and personal["completed_workflows"] == []
    coverage = {row["stage"]: row for row in personal["curriculum_coverage"]}
    assert coverage["stage-a"]["published_word_records"] == 8
    assert coverage["stage-a"]["word_target"] == 500
    assert coverage["stage-b"]["word_target"] == 1500
    assert all(row["published_kanji"] == 0 for row in coverage.values())
    assert all(
        row["published_word_records"] == 0 for key, row in coverage.items() if key != "stage-a"
    )
    assert all("pending" in row["independent_review"] for row in coverage.values())


def test_skill_totals_use_original_snapshots_and_keep_self_ratings_separate(client, course):
    lesson = course.units[0].lessons[0]
    session = start(client)
    first, second = lesson.exercises[:2]
    session = act(client, session, "answer", first.id, answer=first.answer)
    session = act(client, session, "answer", second.id, answer="incorrect response")
    session = act(client, session, "reveal", second.id)
    act(client, skip_all(client, session), "finish")
    card = client.post(
        "/api/v1/courses/ja-starter/review/cards",
        json={"item_id": "ja-word-school", "direction": "typing"},
    ).json()
    client.post(
        f"/api/v1/review/cards/{card['id']}/ratings",
        json={"request_id": str(uuid4()), "expected_revision": 0, "rating": "Easy"},
    )
    personal = client.get("/api/v1/personal").json()
    assert personal["skill_evidence"][first.skill]["initial_correct"] == 1
    assert personal["skill_evidence"]["typing"]["self_rated_reviews"] == 1
    assert (
        sum(row["objective_checks"] for row in personal["skill_evidence"].values())
        == personal["objective_checks"]
        == 2
    )
    assert sum(row["count"] for row in personal["completed_workflows"]) == 2
    assert (
        next(row for row in personal["completed_workflows"] if row["source_kind"] == "review")[
            "evidence"
        ]
        == "self-rated recall"
    )
    newer = deepcopy(course)
    newer.version = "99.2.0"
    newer.units[0].lessons[0].exercises[0].skill = "speaking"
    with sessions(client.app.state.engine)() as db:
        import_content(db, newer)
    after = client.get("/api/v1/personal").json()
    assert after["skill_evidence"] == personal["skill_evidence"]
    assert "speaking" not in after["skill_evidence"]
    assert client.get("/api/v1/progress").json()["total_xp"] == 25
