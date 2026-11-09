from uuid import uuid4

import pytest
from pydantic import ValidationError
from sqlalchemy import func, select

from app.config import ROOT
from app.content_schema import CourseContent
from app.db import sessions
from app.models import Assistance, CourseVersion, Enrollment
from app.services import DomainError, import_content, load_content


@pytest.fixture
def content():
    return load_content(ROOT / "content/courses/ja/starter.json")


def seed(client, content):
    with sessions(client.app.state.engine)() as db:
        return import_content(db, content)


def test_idempotent_seed_and_first_slice(client, content):
    assert seed(client, content)
    assert not seed(client, content)
    listing = client.get("/api/v1/courses").json()
    assert len(listing) == 1
    course = client.get("/api/v1/courses/ja-starter/map").json()
    assert len(course["units"]) == 10
    assert course["inventory"]["published_lessons"] == 6
    assert course["inventory"]["published_words"] == 8
    assert course["inventory"]["target_words"] == 2000
    assert course["inventory"]["coverage"] == "partial_starter_slice"
    assert set(e.type for u in content.units for lesson in u.lessons for e in lesson.exercises) == {
        "multiple_choice",
        "translation",
        "fill_blank",
        "sentence_ordering",
        "matching",
    }


def test_new_learner_accesses_all_published_without_enrollment(client, content):
    seed(client, content)
    for unit in content.units:
        for lesson in unit.lessons:
            response = client.get(f"/api/v1/courses/{content.id}/lessons/{lesson.id}")
            if unit.status != "published" or lesson.status != "published":
                assert response.status_code == 404
                continue
            assert response.status_code == 200
            for exercise in response.json()["exercises"]:
                assert not {"answer", "answers", "explanation", "hint"} & exercise.keys()
    assert client.get("/api/v1/courses/ja-starter/lessons/unpublished").status_code == 404
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(Enrollment)) == 0


def test_reveal_hint_idempotency_and_no_access_effect(client, content):
    seed(client, content)
    exercise = content.units[0].lessons[0].exercises[0]
    url = f"/api/v1/courses/ja-starter/exercises/{exercise.id}/assistance"
    event = str(uuid4())
    first = client.post(url, json={"event_id": event, "action": "reveal"})
    assert first.status_code == 200
    assert first.json()["answer"] == exercise.answer
    assert first.json()["evidence"] == "assisted"
    assert client.post(url, json={"event_id": event, "action": "reveal"}).json() == first.json()
    assert client.post(url, json={"event_id": event, "action": "hint"}).status_code == 409
    hint = client.post(url, json={"event_id": str(uuid4()), "action": "hint"}).json()
    assert "answer" not in hint
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(Assistance)) == 2
    assert client.get("/api/v1/courses/ja-starter/lessons/ja-hiragana-sounds").status_code == 200


def test_versions_preserve_historical_evidence(client, content):
    seed(client, content)
    client.post("/api/v1/courses/ja-starter/enrollment")
    old_id = content.units[0].lessons[0].exercises[0].id
    client.post(
        f"/api/v1/courses/ja-starter/exercises/{old_id}/assistance",
        json={"event_id": str(uuid4()), "action": "reveal"},
    )
    changed = content.model_dump()
    changed["title"] = "An updated original course"
    with sessions(client.app.state.engine)() as db:
        with pytest.raises(DomainError, match="increment"):
            import_content(db, CourseContent.model_validate(changed))
    changed["version"] = "0.2.0"
    seed(client, CourseContent.model_validate(changed))
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(CourseVersion)) == 2
        assistance = db.scalar(select(Assistance))
        assert assistance.course_version_id == f"ja-starter@{content.version}"
        assert db.get(CourseVersion, assistance.course_version_id).data["title"] == content.title
        assert db.get(Enrollment, ("local", "ja-starter")) is not None
    assert client.get("/api/v1/courses/ja-starter").json()["version"] == "0.2.0"
    assert not seed(client, content)  # Historical reimport cannot roll back current content.
    assert client.get("/api/v1/courses/ja-starter").json()["version"] == "0.2.0"


@pytest.mark.parametrize(
    "fault",
    ["duplicate", "concept", "preparation", "choice", "token", "pair", "blank", "order", "license"],
)
def test_invalid_content_rejected(content, fault):
    data = content.model_dump()
    lesson = data["units"][0]["lessons"][0]
    if fault == "duplicate":
        data["units"][1]["id"] = data["units"][0]["id"]
    if fault == "concept":
        lesson["exercises"][0]["concepts"] = ["missing"]
    if fault == "preparation":
        lesson["preparation"] = ["missing"]
    if fault == "choice":
        lesson["exercises"][0]["answer"] = "missing"
    if fault == "token":
        lesson["exercises"][3]["answer"] = ["missing", "missing"]
    if fault == "pair":
        lesson["exercises"][4]["answer"] = {"l0": "r0"}
    if fault == "blank":
        lesson["exercises"][1]["answers"] = [" "]
    if fault == "order":
        data["units"][1]["order"] = 1
    if fault == "license":
        data["licenses"] = []
    with pytest.raises(ValidationError):
        CourseContent.model_validate(data)


def test_draft_course_never_published_by_import(client, content):
    data = content.model_dump()
    data["status"] = "draft"
    seed(client, CourseContent.model_validate(data))
    assert client.get("/api/v1/courses").json() == []
    assert client.get("/api/v1/courses/ja-starter").status_code == 404


def test_lexical_counts_and_cycles(client, content):
    seed(client, content)
    inventory = client.get("/api/v1/courses/ja-starter").json()["inventory"]
    assert inventory["published_words"] == 8
    assert inventory["published_phrases"] == 5
    assert inventory["published_kanji"] == 0
    data = content.model_dump()
    duplicate = dict(data["vocabulary"][0])
    duplicate["id"] = "duplicate-word-id"
    data["vocabulary"].append(duplicate)
    with pytest.raises(ValidationError, match="Duplicate lexical"):
        CourseContent.model_validate(data)
    data = content.model_dump()
    first, second = data["units"][0]["lessons"][:2]
    first["preparation"] = [second["id"]]
    with pytest.raises(ValidationError, match="cycle"):
        CourseContent.model_validate(data)


def test_extension_references_and_assets(content):
    from app.content_extensions import ContentAsset

    with pytest.raises(ValidationError):
        ContentAsset(id="bad", path="../private.file", license_id="original", kind="audio")
    data = content.model_dump()
    data["assessment_banks"] = [
        {
            "id": "bank",
            "kind": "recap",
            "title": "Recap",
            "concepts": ["kana"],
            "exercise_ids": ["missing"],
            "scoring_policy": "Record actual results",
        }
    ]
    with pytest.raises(ValidationError, match="assessment"):
        CourseContent.model_validate(data)


def test_suggested_order_comes_from_metadata(client, content):
    data = content.model_dump()
    data["units"] = list(reversed(data["units"]))
    for unit in data["units"]:
        unit["lessons"] = list(reversed(unit["lessons"]))
    seed(client, CourseContent.model_validate(data))
    units = client.get("/api/v1/courses/ja-starter/map").json()["units"]
    assert [unit["order"] for unit in units] == list(range(1, 11))
    assert [lesson["order"] for lesson in units[0]["lessons"]] == list(
        range(1, len(next(unit for unit in content.units if unit.order == 1).lessons) + 1)
    )


def test_reveal_retry_uses_original_snapshot_after_update(client, content):
    seed(client, content)
    exercise_id = content.units[0].lessons[0].exercises[0].id
    url = f"/api/v1/courses/ja-starter/exercises/{exercise_id}/assistance"
    body = {"event_id": str(uuid4()), "action": "reveal"}
    first = client.post(url, json=body)
    assert first.status_code == 200
    newer = content.model_dump()
    newer["version"] = "0.2.0"
    newer["units"][0]["lessons"][0]["exercises"][0]["explanation"] = "An updated explanation."
    seed(client, CourseContent.model_validate(newer))
    retry = client.post(url, json=body)
    assert retry.status_code == 200
    assert retry.json() == first.json()


def test_concurrent_reveal_delivery_is_idempotent(client, content):
    from concurrent.futures import ThreadPoolExecutor

    seed(client, content)
    client.get("/api/v1/profile")
    exercise_id = content.units[0].lessons[0].exercises[0].id
    url = f"/api/v1/courses/ja-starter/exercises/{exercise_id}/assistance"
    body = {"event_id": str(uuid4()), "action": "reveal"}
    with ThreadPoolExecutor(max_workers=4) as pool:
        responses = list(pool.map(lambda _: client.post(url, json=body), range(4)))
    assert all(response.status_code == 200 for response in responses)
    assert all(response.json() == responses[0].json() for response in responses)
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(Assistance)) == 1


def test_concurrent_enrollment_is_idempotent(client, content):
    from concurrent.futures import ThreadPoolExecutor

    seed(client, content)
    client.get("/api/v1/profile")
    with ThreadPoolExecutor(max_workers=4) as pool:
        responses = list(
            pool.map(lambda _: client.post("/api/v1/courses/ja-starter/enrollment"), range(4))
        )
    assert all(response.status_code == 200 for response in responses)
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(Enrollment)) == 1


def test_indistinguishable_matching_and_blank_tokens_rejected(content):
    data = content.model_dump()
    matching = data["units"][0]["lessons"][0]["exercises"][4]
    matching["right"][1]["text"] = matching["right"][0]["text"] + " "
    with pytest.raises(ValidationError, match="distinguishable"):
        CourseContent.model_validate(data)
    data = content.model_dump()
    data["units"][0]["lessons"][0]["exercises"][3]["tokens"][0]["text"] = " "
    with pytest.raises(ValidationError, match="visible"):
        CourseContent.model_validate(data)


def test_draft_audio_scripts_and_beginner_writing_scope(content):
    episodes = [item for item in content.narratives if item.kind == "audio_episode"]
    assert len(episodes) >= 2
    lessons = [lesson for unit in content.units for lesson in unit.lessons]
    exercise_ids = {exercise.id for lesson in lessons for exercise in lesson.exercises}
    exercise_ids.update(exercise.id for exercise in content.practice_exercises)
    for episode in episodes:
        assert episode.status == "draft"
        assert episode.audio_asset_id is None
        assert episode.transcript_policy == "deliberate_reveal"
        assert episode.objectives and episode.vocabulary_ids
        assert episode.recap_exercise_ids
        assert set(episode.recap_exercise_ids) <= exercise_ids
        assert any(turn.exercise_ids for turn in episode.turns)
    stage_a = [task for task in content.writing_tasks if task.stage == "stage-a"]
    assert {task.genre for task in stage_a} >= {
        "constrained character practice",
        "constrained word practice",
        "first sentence",
    }
    stage_b = [task for task in content.writing_tasks if task.stage == "stage-b"]
    assert len(stage_b) >= 3
    assert all(task.model and task.alternatives and task.checklist for task in stage_b)
    assert any(
        task.revision_before and task.revision_after and task.revision_note for task in stage_b
    )
    assert all(task.status == "draft" for task in stage_a + stage_b)
