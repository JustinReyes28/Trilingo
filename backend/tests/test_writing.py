from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from uuid import uuid4

import pytest
from alembic import command
from alembic.config import Config as AlembicConfig
from fastapi.testclient import TestClient
from sqlalchemy import func, select
from test_learning import course as course
from test_learning import start

from app.config import Config
from app.db import make_engine, sessions
from app.learning import get_session
from app.learning_models import StudySession, XpEntry
from app.learning_schemas import ExerciseEvidence
from app.main import create_app
from app.reading_models import ReadingItem
from app.services import import_content, local_profile
from app.writing_models import WritingConflict, WritingRevision

pytestmark = pytest.mark.usefixtures("course")
BASE = "/api/v1/courses/ja-starter/writing"


def create(client, task="ja-write-intro", **extra):
    response = client.post(
        BASE + "/drafts",
        json={"request_id": str(uuid4()), "task_id": task, "preview_draft": True, **extra},
    )
    assert response.status_code == 200, response.text
    return response.json()


def save_body(draft, text, **extra):
    return {
        "request_id": str(uuid4()),
        "expected_revision_id": draft["current"]["id"],
        "text": text,
        **extra,
    }


def save(client, draft, text, **extra):
    response = client.post(
        "/api/v1/writing/drafts/" + draft["id"] + "/revisions", json=save_body(draft, text, **extra)
    )
    assert response.status_code == 200, response.text
    return response.json()


def test_writing_catalog_direct_tasks_draft_guard_and_idempotent_creation(client):
    assert client.get(BASE).json()["tasks"] == []
    tasks = client.get(BASE + "?include_drafts=true").json()["tasks"]
    assert len([task for task in tasks if task["stage"] == "stage-b"]) == 3
    assert all(task["status"] == "draft" for task in tasks)
    body = {"request_id": str(uuid4()), "task_id": "ja-write-message"}
    assert client.post(BASE + "/drafts", json=body).status_code == 404
    body["preview_draft"] = True
    first = client.post(BASE + "/drafts", json=body).json()
    assert client.post(BASE + "/drafts", json=body).json() == first
    assert first["assessment"] == "not_assessed"
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    for task in tasks:
        assert create(client, task["id"])["task"]["id"] == task["id"]


def test_drafts_save_recover_and_keep_revision_and_model_provenance(client, database):
    draft = create(client)
    body = save_body(
        draft, "アキです。", checklist=[draft["task"]["checklist"][0]], model_revealed=True
    )
    url = "/api/v1/writing/drafts/" + draft["id"]
    saved = client.post(url + "/revisions", json=body).json()
    assert client.post(url + "/revisions", json=body).json() == saved
    changed = save(client, saved, "アキです。シンガポールに住んでいます。", model_revealed=False)
    assert changed["current"]["model_revealed"]
    assert changed["current"]["id"] != saved["current"]["id"]
    with TestClient(create_app(Config(database_url=database))) as restarted:
        assert restarted.get(url).json() == changed
        history = restarted.get(url + "/history?limit=1").json()
        assert history["revisions"][0]["text"] == changed["current"]["text"]
        assert history["has_more_revisions"]
        older = restarted.get(url + "/history?offset=1&limit=100").json()["revisions"]
        assert [revision["text"] for revision in older] == ["アキです。", ""]
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_conflicting_tabs_preserve_both_texts_and_retry_conflict_idempotently(client):
    draft = create(client)
    url = "/api/v1/writing/drafts/" + draft["id"]
    bodies = [save_body(draft, "タブAの文章。"), save_body(draft, "タブBの文章。")]
    with ThreadPoolExecutor(max_workers=2) as pool:
        replies = list(pool.map(lambda body: client.post(url + "/revisions", json=body), bodies))
    assert sorted(reply.status_code for reply in replies) == [200, 409]
    conflict_body = bodies[
        next(index for index, reply in enumerate(replies) if reply.status_code == 409)
    ]
    assert client.post(url + "/revisions", json=conflict_body).status_code == 409
    current = client.get(url).json()
    history = client.get(url + "/history").json()
    assert len(history["conflicts"]) == 1
    assert {current["current"]["text"], history["conflicts"][0]["text"]} == {
        "タブAの文章。",
        "タブBの文章。",
    }
    merged = save(
        client, current, current["current"]["text"] + "\n" + history["conflicts"][0]["text"]
    )
    assert "タブA" in merged["current"]["text"] and "タブB" in merged["current"]["text"]
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(WritingConflict)) == 1
        assert db.scalar(select(func.count()).select_from(WritingRevision)) == 3
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_open_submissions_are_unassessed_optional_review_uncapped_and_idempotent(client):
    draft = create(client, "ja-write-message")
    url = "/api/v1/writing/drafts/" + draft["id"]
    empty = {"request_id": str(uuid4()), "revision_id": draft["current"]["id"]}
    assert client.post(url + "/submissions", json=empty).status_code == 422
    # A short nonempty practice submission is valid without a language-score threshold.
    draft = save(client, draft, "Practice draft: お茶。")
    body = {
        "request_id": str(uuid4()),
        "revision_id": draft["current"]["id"],
        "self_reviewed": False,
    }
    with ThreadPoolExecutor(max_workers=3) as pool:
        replies = list(pool.map(lambda _: client.post(url + "/submissions", json=body), range(3)))
    assert all(reply.status_code == 200 for reply in replies)
    assert all(reply.json() == replies[0].json() for reply in replies)
    result = replies[0].json()
    assert result["xp_awarded"] == 5 and result["assessment"] == "not_assessed"
    assert result["evidence_mode"] == "open_writing" and "correct" not in result
    for _ in range(3):
        new = client.post(
            url + "/submissions", json={**body, "request_id": str(uuid4()), "self_reviewed": True}
        ).json()
        assert new["xp_awarded"] == 5 and new["assessment"] == "self_reviewed"
    assert client.get("/api/v1/progress").json()["total_xp"] == 20
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(XpEntry)) == 4


def test_writing_rejects_foreign_revisions_fabricated_grades_and_checklists(client):
    first, second = create(client), create(client)
    url = "/api/v1/writing/drafts/" + first["id"]
    for payload in [
        save_body(first, "x", is_correct=True),
        save_body(first, "x", xp=500),
        save_body(first, "x", checklist=["invented"]),
        save_body(first, "x", expected_revision_id=second["current"]["id"]),
    ]:
        assert client.post(url + "/revisions", json=payload).status_code == 422
    assert (
        client.post(
            url + "/submissions",
            json={"request_id": str(uuid4()), "revision_id": second["current"]["id"]},
        ).status_code
        == 422
    )
    assert client.get(url).json()["current"]["text"] == ""
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_old_draft_keeps_content_task_and_rubric_snapshot(client, course):
    draft = create(client)
    updated = deepcopy(course)
    updated.version = "99.0.0"
    next(
        task for task in updated.writing_tasks if task.id == "ja-write-intro"
    ).model = "Changed newer model"
    with sessions(client.app.state.engine)() as db:
        import_content(db, updated)
    old = client.get("/api/v1/writing/drafts/" + draft["id"]).json()
    assert old == draft and old["content_version"] == course.version
    assert create(client)["task"]["model"] == "Changed newer model"


def test_constrained_typing_uses_shared_authoritative_grader(client):
    for task, answer in [
        ("ja-write-character-a", "あ"),
        ("ja-write-word-house", "いえ"),
        ("ja-write-fixed-message", "こんにちは。アキです。"),
    ]:
        session = start(client, task, source_kind="writing_task", preview_draft=True)
        exercise = session["exercises"][0]
        from test_learning import act

        assert session["kind"] == "typed_writing" and session["story"] is None
        assert (
            act(client, session, "answer", exercise["id"], answer=answer)["feedback"]["kind"]
            == "correct"
        )
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_writing_migration_preserves_existing_study_and_reading(tmp_path, monkeypatch, course):
    url = f"sqlite:///{(tmp_path / 'populated-0004.db').as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)
    config = AlembicConfig("alembic.ini")
    command.upgrade(config, "0004")
    engine = make_engine(url)
    with sessions(engine)() as db:
        import_content(db, course)
    # Seed the previous schema directly. Current services correctly require newer tables;
    # an old-version fixture must not execute future business logic before upgrading.
    with sessions(engine)() as db:
        local_profile(db)
        lesson = course.units[0].lessons[0]
        stamp = "2026-10-20T04:00:00+00:00"
        row = StudySession(
            id=str(uuid4()),
            profile_id="local",
            course_id=course.id,
            course_version_id=f"{course.id}@{course.version}",
            source_kind="lesson",
            source_id=lesson.id,
            kind="lesson",
            title=lesson.title,
            status="completed",
            cursor=len(lesson.exercises),
            revision=6,
            next_action_id=str(uuid4()),
            exercise_ids=[exercise.id for exercise in lesson.exercises],
            evidence={
                exercise.id: ExerciseEvidence(skipped=True).model_dump()
                for exercise in lesson.exercises
            },
            metadata_json={"preview_draft": False, "mode": "supported", "feedback": None},
            created_at=stamp,
            completed_at=stamp,
        )
        db.add(row)
        db.flush()
        db.add(
            XpEntry(
                id=str(uuid4()),
                session_id=row.id,
                profile_id="local",
                amount=20,
                occurred_at=stamp,
                activity_date="2026-10-20",
                timezone="UTC",
            )
        )
        db.add(
            ReadingItem(
                profile_id="local",
                course_id=course.id,
                item_kind="word",
                item_id="ja-word-house",
                course_version_id=row.course_version_id,
                saved=True,
                familiar=False,
                updated_at=stamp,
            )
        )
        db.commit()
        studied = get_session(db, row.id)
    command.upgrade(config, "head")
    command.check(config)
    with TestClient(create_app(Config(database_url=url))) as upgraded:
        assert upgraded.get("/api/v1/sessions/" + studied["id"]).json() == studied
        assert upgraded.get("/api/v1/progress").json()["total_xp"] == 20
        assert upgraded.get("/api/v1/courses/ja-starter/reading").json()["items"][0]["saved"]
        assert create(upgraded)["current"]["text"] == ""
    engine.dispose()
