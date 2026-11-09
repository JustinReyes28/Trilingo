from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from uuid import uuid4

import pytest
from alembic import command
from alembic.config import Config as AlembicConfig
from fastapi.testclient import TestClient
from sqlalchemy import func, select

from app import learning
from app.config import ROOT, Config
from app.content_schema import CourseContent, Policy
from app.db import sessions
from app.grading import grade, normalize_text
from app.learning_models import StudyEvent, StudySession, XpEntry
from app.main import create_app
from app.services import DomainError, import_content, load_content


@pytest.fixture
def course(client):
    content = load_content(ROOT / "content/courses/ja/starter.json")
    with sessions(client.app.state.engine)() as db:
        import_content(db, content)
    return content


def start(client, lesson="ja-greetings-hello", **fields):
    body = {"request_id": str(uuid4()), "source_id": lesson, **fields}
    response = client.post("/api/v1/courses/ja-starter/sessions", json=body)
    assert response.status_code == 200, response.text
    return response.json()


def action_body(session, action, exercise=None, **fields):
    value = {
        "request_id": session["next_action_id"],
        "expected_revision": session["revision"],
        "action": action,
        **fields,
    }
    if exercise is not None:
        value["exercise_id"] = exercise
    return value


def act(client, session, action, exercise=None, **fields):
    response = client.post(
        f"/api/v1/sessions/{session['id']}/actions",
        json=action_body(session, action, exercise, **fields),
    )
    assert response.status_code == 200, response.text
    return response.json()


def skip_all(client, session):
    for exercise in session["exercises"]:
        session = act(client, session, "skip", exercise["id"])
    return session


def complete(client, lesson="ja-greetings-hello", **fields):
    return act(client, skip_all(client, start(client, lesson, **fields)), "finish")


def expected(exercise):
    return getattr(exercise, "answer", getattr(exercise, "answers", [None])[0])


def test_all_authored_graders_and_invalid_shapes(course):
    for unit in course.units:
        for lesson in unit.lessons:
            for exercise in lesson.exercises:
                assert grade(exercise, expected(exercise)) is True
                if exercise.type in {"translation", "fill_blank"}:
                    assert grade(exercise, "definitely incorrect") is False
                    for alternate in exercise.answers:
                        assert grade(exercise, alternate)
                    invalid = ["bad"]
                elif exercise.type == "multiple_choice":
                    other = next(c.id for c in exercise.choices if c.id != exercise.answer)
                    assert grade(exercise, other) is False
                    invalid = "missing-choice"
                elif exercise.type == "sentence_ordering":
                    assert not grade(exercise, list(reversed(exercise.answer)))
                    invalid = [exercise.answer[0]] * len(exercise.answer)
                else:
                    values = list(exercise.answer.values())
                    wrong = dict(zip(exercise.answer, values[1:] + values[:1], strict=True))
                    assert not grade(exercise, wrong)
                    invalid = {}
                with pytest.raises(DomainError):
                    grade(exercise, invalid)


@pytest.mark.parametrize(
    "expected_text,accepted,rejected",
    [
        ("が", "か\u3099", "か"),
        ("ゃ", "ゃ", "や"),
        ("がっこう", "がっこう", "がこう"),
        ("おばあさん", "おばあさん", "おばさん"),
        ("コーヒー", "コーヒー", "コヒ"),
        ("カ", "カ", "ｶ"),
    ],
)
def test_normalization_preserves_required_distinctions(course, expected_text, accepted, rejected):
    exercise = course.units[0].lessons[0].exercises[1].model_copy(deep=True)
    exercise.answers = [expected_text]
    exercise.policy.script = "japanese"
    assert grade(exercise, accepted)
    assert not grade(exercise, rejected)


def test_normalization_policy_is_explicit(course):
    policy = Policy(normalization="NFC", punctuation="exact", trim=False, case_sensitive=True)
    assert normalize_text(" A。 ", policy) == " A。 "
    assert normalize_text("Ａ", policy) != "A"
    assert normalize_text("Ａ", policy.model_copy(update={"normalization": "NFKC"})) == "A"
    assert normalize_text(" a b! ", Policy(spacing="ignore")) == "ab"
    exercise = course.units[0].lessons[0].exercises[1].model_copy(deep=True)
    exercise.answers, exercise.policy.script = ["カ"], "katakana"
    assert not grade(exercise, "ｶ")
    exercise.policy.normalization = "NFKC"
    assert grade(exercise, "ｶ")
    exercise.answers, exercise.policy.script = ["あ"], "hiragana"
    assert not grade(exercise, "ア")


def test_start_every_published_lesson_without_history(client, course):
    for unit in course.units:
        for lesson in unit.lessons:
            if unit.status != "published" or lesson.status != "published":
                response = client.post(
                    "/api/v1/courses/ja-starter/sessions",
                    json={"request_id": str(uuid4()), "source_id": lesson.id},
                )
                assert response.status_code == 404
                continue
            session = start(client, lesson.id)
            assert session["source_id"] == lesson.id
            assert session["xp_awarded"] == 0
            assert session["status"] == "active"
            for exercise in session["exercises"]:
                assert not {"answer", "answers", "explanation", "hint"} & exercise.keys()
    denied = client.post(
        "/api/v1/courses/ja-starter/sessions",
        json={
            "request_id": str(uuid4()),
            "source_id": "unpublished",
        },
    )
    assert denied.status_code == 404
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_start_and_answer_receipts_are_immutable(client, course):
    key = str(uuid4())
    session = start(client, request_id=key)
    again = start(client, request_id=key)
    assert again == session
    exercise = session["exercises"][0]
    body = action_body(session, "answer", exercise["id"], answer="c1")
    url = f"/api/v1/sessions/{session['id']}/actions"
    first = client.post(url, json=body).json()
    assert first["feedback"]["kind"] == "incorrect"
    later = act(client, first, "hint", exercise["id"])
    assert client.post(url, json=body).json() == first
    assert first["revision"] < later["revision"]
    changed = {**body, "answer": "c0"}
    assert client.post(url, json=changed).status_code == 409
    assert client.post(url, json={**body, "request_id": str(uuid4())}).status_code == 409
    assert client.get("/api/v1/courses/ja-starter/mistakes").json()[0]["occurrences"] == 1


def test_wrong_retry_hint_reveal_skip_continue_finish(client, course):
    session = start(client)
    exercise_id = session["exercises"][0]["id"]
    for _ in range(4):
        session = act(client, session, "answer", exercise_id, answer="c1")
    session = act(client, session, "hint", exercise_id)
    assert session["feedback"]["answer"] is None
    session = act(client, session, "reveal", exercise_id)
    assert session["feedback"]["answer"] == "c0"
    session = act(client, session, "answer", exercise_id, answer="c0")
    evidence = session["evidence"][exercise_id]
    assert evidence["first_correct"] is False and evidence["last_correct"] is True
    assert evidence["responses"] == 5 and evidence["assisted"]
    session = act(client, session, "continue", exercise_id)
    assert session["cursor"] == 1
    for exercise in session["exercises"][1:]:
        session = act(client, session, "skip", exercise["id"])
    session = act(client, session, "finish")
    assert session["xp_awarded"] == 20 and session["assessed_count"] == 1
    assert session["initial_correct"] == 0
    assert len(session["concept_coverage"]) > 0
    course_map = client.get("/api/v1/courses/ja-starter/map").json()
    assert course_map["units"][0]["lessons"][0]["study_state"] == "assisted"
    assert start(client, "ja-hiragana-sounds")["status"] == "active"
    mistakes = client.get("/api/v1/courses/ja-starter/mistakes").json()
    assert mistakes[0]["occurrences"] == 4
    practice = start(client, "mistakes", source_kind="mistakes")
    assert practice["kind"] == "practice"
    assert act(client, skip_all(client, practice), "finish")["xp_awarded"] == 5


def test_revealed_answer_is_not_unassisted_recall(client, course):
    session = start(client)
    key = session["exercises"][0]["id"]
    session = act(client, session, "reveal", key)
    session = act(client, session, "answer", key, answer="c0")
    assert session["initial_correct"] == session["assessed_count"] == 0
    assert session["evidence"][key]["first_assisted"] is True


def test_unfinished_no_reward_client_xp_rejected(client, course):
    session = start(client)
    url = f"/api/v1/sessions/{session['id']}/actions"
    assert client.post(url, json=action_body(session, "finish")).status_code == 409
    body = action_body(session, "answer", session["exercises"][0]["id"], answer="c0")
    for extra in [{"xp": 50000}, {"is_correct": True}, {"xp_award": 10}]:
        assert client.post(url, json={**body, **extra}).status_code == 422
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_unlimited_new_sessions_and_duplicate_completion(client, course):
    assert complete(client)["xp_awarded"] == 20
    for _ in range(12):
        session = skip_all(client, start(client))
        body = action_body(session, "finish")
        url = f"/api/v1/sessions/{session['id']}/actions"
        first = client.post(url, json=body)
        assert first.status_code == 200 and first.json()["xp_awarded"] == 5
        assert client.post(url, json=body).json() == first.json()
    progress = client.get("/api/v1/progress?limit=2").json()
    assert progress["total_xp"] == 80 and progress["today_xp"] == 80
    assert progress["goal_met"] and progress["has_more"] and len(progress["sessions"]) == 2
    assert client.get("/api/v1/progress?limit=1000").json()["has_more"] is False
    client.patch("/api/v1/settings", json={"daily_goal": None, "show_goal": False})
    assert client.get("/api/v1/progress").json()["goal_met"] is False
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(XpEntry)) == 13
        assert db.scalar(select(func.sum(XpEntry.amount))) == 80


def test_concurrent_delivery_and_distinct_first_completions(client, course):
    first, second = [skip_all(client, start(client)) for _ in range(2)]
    url = f"/api/v1/sessions/{first['id']}/actions"
    body = action_body(first, "finish")
    with ThreadPoolExecutor(max_workers=4) as pool:
        responses = list(pool.map(lambda _: client.post(url, json=body), range(4)))
    assert all(r.status_code == 200 and r.json() == responses[0].json() for r in responses)
    assert act(client, second, "finish")["xp_awarded"] == 5
    assert client.get("/api/v1/progress").json()["total_xp"] == 25


def test_finish_rollback_keeps_attempt_and_ledger_consistent(client, course, monkeypatch):
    session = skip_all(client, start(client))
    record = learning._record

    def fail(*_args):
        raise RuntimeError("injected receipt failure")

    monkeypatch.setattr(learning, "_record", fail)
    with pytest.raises(RuntimeError, match="injected"):
        act(client, session, "finish")
    monkeypatch.setattr(learning, "_record", record)
    assert client.get(f"/api/v1/sessions/{session['id']}").json()["status"] == "active"
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    assert act(client, session, "finish")["xp_awarded"] == 20


def test_pause_restart_content_update_and_history(client, course, database):
    session = start(client)
    key = session["exercises"][0]["id"]
    session = act(client, session, "answer", key, answer="c0")
    session = act(client, session, "continue", key)
    session = act(client, session, "pause")
    newer = course.model_dump()
    newer["version"] = "0.2.0"
    newer["units"][0]["lessons"][0]["exercises"][0]["answer"] = "c1"
    with sessions(client.app.state.engine)() as db:
        import_content(db, CourseContent.model_validate(newer))
    with TestClient(create_app(Config(database_url=database))) as restarted:
        saved = restarted.get(f"/api/v1/sessions/{session['id']}").json()
        assert saved == session and saved["cursor"] == 1
        assert saved["content_version"] == course.version
        assert act(restarted, saved, "resume")["status"] == "active"
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(StudyEvent)) == 5
    finished = complete(client)
    newest = dict(newer)
    newest["version"] = "0.2.1"
    with sessions(client.app.state.engine)() as db:
        import_content(db, CourseContent.model_validate(newest))
        assert db.get(StudySession, finished["id"]).status == "completed"
    assert client.get(f"/api/v1/sessions/{finished['id']}").json() == finished


@pytest.mark.parametrize("bank_kind", ["recap", "placement", "mastery"])
def test_optional_assessment_has_no_history_or_score_requirement(client, course, bank_kind):
    data = course.model_dump()
    data["version"] = "0.2.0"
    bank = data["assessment_banks"][0]
    bank["status"] = "published"
    bank["kind"] = bank_kind
    with sessions(client.app.state.engine)() as db:
        import_content(db, CourseContent.model_validate(data))
    for _ in range(3):
        result = complete(client, bank["id"], source_kind="assessment", mode="unassisted")
        assert result["kind"] == "assessment" and result["xp_awarded"] == 5
        assert result["assessed_count"] == 0
    session = start(client, bank["id"], source_kind="assessment", mode="unassisted")
    session = act(client, session, "reveal", session["exercises"][0]["id"])
    assert session["evidence"][session["exercises"][0]["id"]]["assisted"]
    assert session["mode"] == "supported"
    assert start(client, "ja-hiragana-sounds")["status"] == "active"


def test_draft_assessment_requires_explicit_preview(client, course):
    bank = course.assessment_banks[0]
    response = client.post(
        "/api/v1/courses/ja-starter/sessions",
        json={
            "request_id": str(uuid4()),
            "source_kind": "assessment",
            "source_id": bank.id,
        },
    )
    assert response.status_code == 404
    assert start(client, bank.id, source_kind="assessment", preview_draft=True)["preview_draft"]


@pytest.mark.parametrize(
    "days,today,current,longest",
    [
        ([], "2026-10-23", 0, 0),
        (["2026-10-23"], "2026-10-23", 1, 1),
        (["2026-10-22", "2026-10-23", "2026-10-23"], "2026-10-23", 2, 2),
        (["2026-10-20", "2026-10-21"], "2026-10-23", 0, 2),
        (["2026-10-20", "2026-10-21", "2026-10-23"], "2026-10-23", 1, 2),
    ],
)
def test_streak_date_sequences(days, today, current, longest):
    assert learning.streaks([date.fromisoformat(d) for d in days], date.fromisoformat(today)) == (
        current,
        longest,
    )


def test_timezone_boundaries_dst_changes_and_missed_day_preserve_work(client, course, monkeypatch):
    client.get("/api/v1/profile?timezone=America/New_York")
    instants = [
        "2026-03-07T23:00:00+00:00",
        "2026-03-08T06:59:00+00:00",
        "2026-03-08T07:01:00+00:00",
        "2026-03-09T04:01:00+00:00",
    ]
    for instant in instants:
        now = datetime.fromisoformat(instant)
        monkeypatch.setattr(learning, "now_utc", lambda: now)
        complete(client)
    progress = client.get("/api/v1/progress").json()
    assert progress["activity_dates"] == ["2026-03-07", "2026-03-08", "2026-03-09"]
    assert progress["current_streak"] == progress["longest_streak"] == 3
    assert progress["total_xp"] == 35
    client.patch("/api/v1/profile", json={"timezone": "Asia/Singapore"})
    now = datetime(2026, 3, 11, tzinfo=timezone.utc)
    later = client.get("/api/v1/progress").json()
    assert later["current_streak"] == 0 and later["total_xp"] == 35
    assert client.get("/api/v1/courses/ja-starter/lessons/ja-hiragana-sounds").status_code == 200
    with sessions(client.app.state.engine)() as db:
        assert set(db.scalars(select(XpEntry.timezone))) == {"America/New_York"}
    complete(client)
    assert "2026-03-11" in client.get("/api/v1/progress").json()["activity_dates"]


def test_migration_drift_on_full_study_schema(database):
    command.check(AlembicConfig("alembic.ini"))


def test_explicit_supported_switch_is_saved_without_fabricating_answers(client, course):
    session = start(
        client,
        course.assessment_banks[0].id,
        source_kind="assessment",
        preview_draft=True,
        mode="unassisted",
    )
    supported = act(client, session, "support")
    assert supported["mode"] == "supported" and supported["assessed_count"] == 0
    assert all(
        item["responses"] == 0 and not item["assisted"] for item in supported["evidence"].values()
    )


def test_repeated_ordering_labels_keep_distinct_token_ids(course):
    from app.content_schema import SentenceOrdering

    data = course.units[0].lessons[0].exercises[3].model_dump()
    data.update(tokens=[{"id": "a", "text": "と"}, {"id": "b", "text": "と"}], answer=["a", "b"])
    exercise = SentenceOrdering.model_validate(data)
    assert grade(exercise, ["a", "b"]) and not grade(exercise, ["b", "a"])
    with pytest.raises(DomainError):
        grade(exercise, ["a", "a"])


def test_populated_content_upgrade_retains_settings_snapshots_and_assistance(tmp_path, monkeypatch):
    from app.db import make_engine
    from app.models import Assistance, CourseVersion
    from app.schemas import ProfilePatch, SettingsPatch
    from app.services import local_profile, patch_profile, patch_settings, reveal

    url = f"sqlite:///{(tmp_path / 'populated.db').as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)
    config = AlembicConfig("alembic.ini")
    command.upgrade(config, "0002")
    engine = make_engine(url)
    content = load_content(ROOT / "content/courses/ja/starter.json")
    key = str(uuid4())
    with sessions(engine)() as db:
        import_content(db, content)
        local_profile(db)
        patch_profile(db, ProfilePatch(name="Keep my profile"))
        patch_settings(db, SettingsPatch(furigana="hidden"))
        reveal(db, content.id, content.units[0].lessons[0].exercises[0].id, key, "hint")
    command.upgrade(config, "head")
    command.check(config)
    with TestClient(create_app(Config(database_url=url))) as upgraded:
        assert upgraded.get("/api/v1/profile").json()["name"] == "Keep my profile"
        assert upgraded.get("/api/v1/settings").json()["furigana"] == "hidden"
        assert start(upgraded)["content_version"] == content.version
    with sessions(engine)() as db:
        assert db.get(Assistance, key) is not None
        assert db.get(CourseVersion, f"{content.id}@{content.version}") is not None
    engine.dispose()


def test_placement_recommendation_uses_actual_missed_or_unassessed_prompts(client, course):
    bank = next(item for item in course.assessment_banks if item.kind == "placement")
    session = start(client, bank.id, source_kind="assessment", preview_draft=True)
    first = session["exercises"][0]
    session = act(client, session, "answer", first["id"], answer="c1")
    session = act(client, skip_all(client, session), "finish")
    suggestion = session["recommendation"]
    assert suggestion["lesson_id"] == "ja-greetings-hello"
    assert "missed" in suggestion["reason"] and "any lesson" in suggestion["reason"]
    assert start(client, suggestion["lesson_id"])["status"] == "active"
    skipped = complete(client, bank.id, source_kind="assessment", preview_draft=True)
    assert "skipped" in skipped["recommendation"]["reason"]


def test_successful_placement_suggests_other_sampled_scope_without_certifying_level(client, course):
    bank = next(item for item in course.assessment_banks if item.kind == "placement")
    session = start(client, bank.id, source_kind="assessment", preview_draft=True)
    exercises = learning.exercise_map(course)
    for exercise_id in [item["id"] for item in session["exercises"]]:
        session = act(
            client, session, "answer", exercise_id, answer=expected(exercises[exercise_id])
        )
    result = act(client, session, "finish")
    assert result["initial_correct"] == result["assessed_count"] == len(bank.exercise_ids)
    assert "matched the sampled checks" in result["recommendation"]["reason"]
    assert result["recommendation"]["lesson_id"] == "ja-greetings-names"
