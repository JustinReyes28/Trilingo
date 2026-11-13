"""Transactional study engine shared by lessons and optional assessment/practice."""

from collections.abc import Iterator
from contextlib import contextmanager
from copy import deepcopy
from datetime import date, datetime, timedelta, timezone
from uuid import uuid4
from zoneinfo import ZoneInfo

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app import stories, timing
from app.content_schema import CourseContent, Exercise
from app.grading import grade
from app.learning_models import Mistake, StudyEvent, StudySession, XpEntry
from app.learning_schemas import ActionRequest, ExerciseEvidence, StartRequest, StudyOut
from app.models import CourseVersion
from app.reading import available_exercise_ids, practice_source
from app.services import (
    DomainError,
    current_content,
    get_settings,
    local_profile,
    public_exercise,
    public_lesson,
)

FIRST_LESSON_XP = 20
PRACTICE_XP = 5


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


@contextmanager
def study_transaction(db: Session) -> Iterator[None]:
    local_profile(db)
    db.commit()
    # Serialize SQLite read-modify-write, including across independent server processes.
    # This protects first-completion rewards and lost-response retries in different tabs.
    db.connection().exec_driver_sql("BEGIN IMMEDIATE")
    try:
        yield
        db.commit()
    except BaseException:
        db.rollback()
        raise


def _session(db: Session, session_id: str) -> StudySession:
    row = db.get(StudySession, session_id)
    if row is None or row.profile_id != "local":
        raise DomainError(404, "session_missing", "Study session not found. Choose a lesson.")
    return row


def _content(db: Session, row: StudySession) -> CourseContent:
    version = db.get(CourseVersion, row.course_version_id)
    assert version is not None
    return CourseContent.model_validate(version.data)


def exercise_map(content: CourseContent) -> dict[str, Exercise]:
    return {
        e.id: e
        for e in (
            [e for unit in content.units for lesson in unit.lessons for e in lesson.exercises]
            + content.practice_exercises
        )
    }


def _view(db: Session, row: StudySession) -> dict:
    content = _content(db, row)
    exercises = exercise_map(content)
    xp = db.scalar(select(XpEntry.amount).where(XpEntry.session_id == row.id)) or 0
    assessed = [
        e
        for e in row.evidence.values()
        if e["first_correct"] is not None and not e["first_assisted"]
    ]
    coverage: dict[str, int] = {}
    for exercise_id, evidence in row.evidence.items():
        if evidence["responses"]:
            for concept in exercises[exercise_id].concepts:
                coverage[concept] = coverage.get(concept, 0) + 1
    return StudyOut.model_validate(
        {
            "id": row.id,
            "course_id": row.course_id,
            "content_version": content.version,
            "source_kind": row.source_kind,
            "source_id": row.source_id,
            "kind": row.kind,
            "title": row.title,
            "status": row.status,
            "cursor": row.cursor,
            "revision": row.revision,
            "next_action_id": row.next_action_id,
            "exercises": [public_exercise(exercises[key]) for key in row.exercise_ids],
            "evidence": row.evidence,
            "preview_draft": row.metadata_json["preview_draft"],
            "mode": row.metadata_json["mode"],
            "feedback": row.metadata_json.get("feedback"),
            "xp_awarded": xp,
            "created_at": row.created_at,
            "completed_at": row.completed_at,
            "recommendation": placement_recommendation(content, row),
            "story": stories.view(content, row),
            "timer": timing.view(row, now_utc()),
            "initial_correct": sum(e["first_correct"] is True for e in assessed),
            "assessed_count": len(assessed),
            "concept_coverage": coverage,
        }
    ).model_dump(mode="json")


def get_session(db: Session, session_id: str) -> dict:
    return _view(db, _session(db, session_id))


def _receipt(db: Session, key: str, request: dict) -> dict | None:
    event = db.scalar(select(StudyEvent).where(StudyEvent.request_id == key))
    if event is None:
        return None
    if event.request != request:
        raise DomainError(
            409, "request_conflict", "This action ID was already used for another request."
        )
    return event.response


def _record(db: Session, row: StudySession, key: str, request: dict) -> dict:
    response = _view(db, row)
    db.add(
        StudyEvent(
            id=str(uuid4()),
            request_id=key,
            session_id=row.id,
            request=request,
            response=response,
            created_at=now_utc().isoformat(),
        )
    )
    return response


def _source(db: Session, content: CourseContent, body: StartRequest) -> tuple[str, list[str], str]:
    if body.source_kind == "lesson":
        lesson = public_lesson(content, body.source_id)
        prior = db.scalar(
            select(StudySession.id)
            .where(
                StudySession.profile_id == "local",
                StudySession.course_id == content.id,
                StudySession.source_kind == "lesson",
                StudySession.source_id == body.source_id,
                StudySession.status == "completed",
            )
            .limit(1)
        )
        return (
            lesson["title"],
            [e["id"] for e in lesson["exercises"]],
            "replay" if prior else "lesson",
        )
    if body.source_kind == "writing_task":
        task = next((item for item in content.writing_tasks if item.id == body.source_id), None)
        if task is None or (task.status != "published" and not body.preview_draft):
            raise DomainError(
                404, "writing_task", "Choose an available writing task or enable draft practice."
            )
        return task.genre.capitalize() + " · Typed check", task.exercise_ids, "typed_writing"
    if body.source_kind in {"story", "story_recap"}:
        story = stories.source(content, body.source_id, body.preview_draft)
        ids = (
            story.recap_exercise_ids
            if body.source_kind == "story_recap"
            else [key for turn in story.turns for key in turn.exercise_ids]
        )
        return (
            story.title + (" · Recap" if body.source_kind == "story_recap" else ""),
            ids,
            "dialogue" if story.kind == "dialogue" else "reading",
        )
    if body.source_kind == "grammar":
        note = next((item for item in content.grammar_notes if item.id == body.source_id), None)
        if note is None or (note.status != "published" and not body.preview_draft):
            raise DomainError(404, "grammar_missing", "Choose an available guide or labeled draft.")
        return note.title + " · Pattern practice", note.practice_exercise_ids, "grammar"
    if body.source_kind == "speaking":
        story = stories.source(content, body.source_id, body.preview_draft)
        return story.title + " · Speaking", story.speaking_exercise_ids, "speaking"
    if body.source_kind == "listening":
        story = stories.source(content, body.source_id, body.preview_draft)
        exercises = exercise_map(content)
        ids = list(
            dict.fromkeys(
                [key for turn in story.turns for key in turn.exercise_ids]
                + story.recap_exercise_ids
            )
        )
        ids = [
            key
            for key in ids
            if exercises[key].type in {"listening_selection", "dictation", "audio_contrast"}
        ]
        return story.title + " · Listening", ids, "listening"
    if body.source_kind in {"character", "saved_items"}:
        return practice_source(db, content, body.source_kind, body.source_id, body.preview_draft)
    available = available_exercise_ids(content, body.preview_draft)
    if body.source_kind == "assessment":
        bank = next((b for b in content.assessment_banks if b.id == body.source_id), None)
        if bank is None or (bank.status != "published" and not body.preview_draft):
            raise DomainError(404, "assessment_missing", "Choose an available assessment.")
        if not set(bank.exercise_ids) <= available:
            raise DomainError(
                404, "assessment_content", "This assessment includes unpublished lessons."
            )
        return bank.title, bank.exercise_ids, "assessment"
    rows = db.scalars(
        select(Mistake)
        .where(
            Mistake.profile_id == "local",
            Mistake.course_id == content.id,
        )
        .order_by(Mistake.updated_at.desc())
    ).all()
    ids = [row.exercise_id for row in rows if row.exercise_id in available]
    if not ids:
        raise DomainError(
            404, "no_mistakes", "No available mistakes yet. You can choose any lesson."
        )
    return "Practice from your mistakes", ids, "practice"


def start_session(db: Session, course_id: str, body: StartRequest) -> dict:
    request = {"course_id": course_id, "action": "start", **body.model_dump()}
    with study_transaction(db):
        prior = _receipt(db, body.request_id, request)
        if prior is not None:
            return prior
        version, content = current_content(db, course_id)
        title, exercise_ids, kind = _source(db, content, body)
        if not exercise_ids and body.source_kind != "story":
            raise DomainError(404, "empty_activity", "This activity has no available exercises.")
        row = StudySession(
            id=str(uuid4()),
            profile_id="local",
            course_id=course_id,
            course_version_id=version.id,
            source_kind=body.source_kind,
            source_id=body.source_id,
            kind=kind,
            title=title,
            status="active",
            cursor=0,
            revision=0,
            next_action_id=str(uuid4()),
            exercise_ids=exercise_ids,
            evidence={key: ExerciseEvidence().model_dump() for key in exercise_ids},
            metadata_json={"preview_draft": body.preview_draft, "mode": body.mode},
            created_at=now_utc().isoformat(),
            completed_at=None,
        )
        if body.source_kind == "speaking":
            row.metadata_json = {
                **row.metadata_json,
                "evidence_mode": (
                    "speaking practice; authored audio model and typed practice; "
                    "pronunciation unassessed"
                ),
            }
        if get_settings(db).show_timer:
            timing.act(row.metadata_json, "timer_start", now_utc())
        if body.source_kind == "story":
            metadata = deepcopy(row.metadata_json)
            metadata["story"] = stories.start_state(db, content, body)
            stories.note_aids(content, row, metadata)
            row.metadata_json = metadata
            first = stories.source(content, body.source_id, body.preview_draft).turns[0]
            row.cursor = (
                exercise_ids.index(first.exercise_ids[0])
                if first.exercise_ids
                else len(exercise_ids)
            )
        db.add(row)
        db.flush()
        return _record(db, row, body.request_id, request)


def _mistake(db: Session, row: StudySession, exercise_id: str) -> None:
    record = db.get(Mistake, ("local", row.course_id, exercise_id))
    if record is None:
        record = Mistake(
            profile_id="local",
            course_id=row.course_id,
            exercise_id=exercise_id,
            course_version_id=row.course_version_id,
            last_session_id=row.id,
            occurrences=0,
            updated_at=now_utc().isoformat(),
        )
        db.add(record)
    record.occurrences += 1
    record.last_session_id = row.id
    record.course_version_id = row.course_version_id
    record.updated_at = now_utc().isoformat()


def _finish(db: Session, row: StudySession) -> None:
    if row.source_kind == "review" and "rating" not in row.metadata_json:
        raise DomainError(
            409,
            "review_rating",
            "Save with an intentional recall rating, or leave without changing its schedule.",
        )
    if row.source_kind == "story":
        evidence = deepcopy(row.evidence)
        for item in evidence.values():
            if not (item["responses"] or item["revealed"]):
                item["skipped"] = True
        row.evidence = evidence
    if any(not (e["responses"] or e["revealed"] or e["skipped"]) for e in row.evidence.values()):
        raise DomainError(
            409, "unfinished", "Answer, reveal or explicitly skip the remaining prompts."
        )
    prior = db.scalar(
        select(StudySession.id)
        .where(
            StudySession.profile_id == "local",
            StudySession.course_id == row.course_id,
            StudySession.source_id == row.source_id,
            StudySession.source_kind == "lesson",
            StudySession.status == "completed",
            StudySession.id != row.id,
        )
        .limit(1)
    )
    amount = FIRST_LESSON_XP if row.source_kind == "lesson" and prior is None else PRACTICE_XP
    profile = local_profile(db)
    now = now_utc()
    row.status, row.completed_at = "completed", now.isoformat()
    db.add(
        XpEntry(
            id=str(uuid4()),
            session_id=row.id,
            profile_id=profile.id,
            amount=amount,
            occurred_at=now.isoformat(),
            activity_date=now.astimezone(ZoneInfo(profile.timezone)).date().isoformat(),
            timezone=profile.timezone,
        )
    )
    db.flush()
    from app.review import credit_quests

    credit_quests(db, row)


def complete_practice_activity(
    db: Session,
    course_id: str,
    version_id: str,
    source_kind: str,
    source_id: str,
    kind: str,
    title: str,
    metadata: dict,
) -> StudySession:
    """Complete one genuine workflow inside the caller's shared transaction."""
    row = StudySession(
        id=str(uuid4()),
        profile_id="local",
        course_id=course_id,
        course_version_id=version_id,
        source_kind=source_kind,
        source_id=source_id,
        kind=kind,
        title=title,
        status="active",
        cursor=0,
        revision=0,
        next_action_id=str(uuid4()),
        exercise_ids=[],
        evidence={},
        metadata_json={"preview_draft": False, "mode": "supported", **metadata},
        created_at=now_utc().isoformat(),
        completed_at=None,
    )
    db.add(row)
    db.flush()
    _finish(db, row)
    return row


def _exercise_action(db: Session, row: StudySession, body: ActionRequest) -> dict | None:
    exercise_id = body.exercise_id
    if exercise_id not in row.exercise_ids:
        raise DomainError(404, "exercise_missing", "Choose an exercise in this session.")
    assert exercise_id is not None
    exercise = exercise_map(_content(db, row))[exercise_id]
    evidence = deepcopy(row.evidence)
    item = evidence[exercise_id]
    if row.source_kind == "story" and row.metadata_json["story"]["glossary"]:
        item["assisted"] = True
    index = row.exercise_ids.index(exercise_id)
    row.cursor = index
    feedback = None
    if body.action == "answer":
        assert body.answer is not None
        if hasattr(exercise, "audio") and not {cue.id for cue in exercise.audio} <= set(
            item.get("audio_cue_ids", [])
        ):
            item["assisted"] = True
            item["text_fallback"] = True
        if exercise.type == "speaking":
            if not isinstance(body.answer, str) or not body.answer.strip():
                raise DomainError(
                    422, "typed_fallback", "Enter text or explicitly skip this prompt."
                )
            item.update(
                responses=item["responses"] + 1,
                answer=body.answer,
                typed_fallbacks=item.get("typed_fallbacks", 0) + 1,
                assisted=True,
                first_assisted=True,
                text_fallback=True,
            )
            row.evidence = evidence
            return {
                "exercise_id": exercise_id,
                "kind": "recorded",
                "message": "Typed practice saved. Pronunciation is not assessed.",
                "explanation": exercise.explanation,
            }
        correct = grade(exercise, body.answer)
        if item["responses"] == 0:
            item["first_correct"], item["first_assisted"] = correct, item["assisted"]
        item.update(responses=item["responses"] + 1, last_correct=correct, answer=body.answer)
        if not correct:
            _mistake(db, row, exercise_id)
        feedback = {
            "exercise_id": exercise_id,
            "kind": "correct" if correct else "incorrect",
            "message": "Matches the authored answer."
            if correct
            else "Try again or continue at your pace.",
            "explanation": exercise.response_feedback.get(str(body.answer), exercise.explanation),
        }
    elif body.action == "audio_text":
        if not hasattr(exercise, "audio"):
            raise DomainError(422, "audio_missing", "This prompt has no audio reference.")
        item["assisted"], item["text_fallback"] = True, True
        feedback = {
            "exercise_id": exercise_id,
            "kind": "hint",
            "message": "Text alternative · "
            + " / ".join(cue.label + ": " + cue.transcript for cue in exercise.audio),
        }
    elif body.action in {"hint", "reveal"}:
        item["assisted"] = True
        feedback = {"exercise_id": exercise_id, "kind": body.action, "message": exercise.hint}
        if body.action == "reveal":
            item["revealed"] = True
            feedback.update(
                answer=exercise.audio[0].transcript
                if exercise.type == "speaking"
                else getattr(exercise, "answer", getattr(exercise, "answers", [])),
                explanation=exercise.explanation,
            )
    elif body.action == "skip":
        item["skipped"] = True
        row.cursor = min(index + 1, len(row.exercise_ids))
    elif body.action == "continue":
        if not (item["responses"] or item["revealed"] or item["skipped"]):
            raise DomainError(409, "untouched", "Use Skip to leave this prompt unassessed.")
        row.cursor = min(index + 1, len(row.exercise_ids))
    row.evidence = evidence
    return feedback


def apply_action(db: Session, session_id: str, body: ActionRequest) -> dict:
    request = {"session_id": session_id, **body.model_dump()}
    with study_transaction(db):
        prior = _receipt(db, body.request_id, request)
        if prior is not None:
            return prior
        row = _session(db, session_id)
        if row.revision != body.expected_revision or row.next_action_id != body.request_id:
            raise DomainError(
                409,
                "stale_revision",
                "Another action was saved. Reload the session; your input is preserved.",
            )
        if row.status == "completed":
            raise DomainError(
                409, "completed", "This session is complete. Start a new replay to keep studying."
            )
        metadata = deepcopy(row.metadata_json)
        if body.action.startswith("timer_"):
            timing.act(metadata, body.action, now_utc())
        elif body.action in stories.STORY_ACTIONS:
            row.status = "active"
            stories.act(_content(db, row), row, body, metadata)
        elif body.action == "finish":
            timing.freeze(metadata, now_utc())
            _finish(db, row)
            metadata["feedback"] = None
        elif body.action == "support":
            metadata["mode"] = "supported"
        elif body.action in {"pause", "resume"}:
            row.status = "paused" if body.action == "pause" else "active"
            if body.action == "pause":
                timing.freeze(metadata, now_utc(), pause=True)
        else:
            row.status = "active"
            metadata["feedback"] = _exercise_action(db, row, body)
            if body.action in {"hint", "reveal", "audio_text"}:
                metadata["mode"] = "supported"
        row.metadata_json = metadata
        row.revision += 1
        row.next_action_id = str(uuid4())
        db.flush()
        return _record(db, row, body.request_id, request)


def streaks(days: list[date], today: date) -> tuple[int, int]:
    ordered = sorted(set(days))
    longest = run = 0
    previous = None
    for day in ordered:
        run = run + 1 if previous and day == previous + timedelta(days=1) else 1
        longest, previous = max(longest, run), day
    current = run if ordered and ordered[-1] in {today, today - timedelta(days=1)} else 0
    return current, longest


def progress(db: Session, offset: int = 0, limit: int = 20) -> dict:
    profile = local_profile(db)
    settings = get_settings(db)
    today = now_utc().astimezone(ZoneInfo(profile.timezone)).date()
    total = db.scalar(select(func.sum(XpEntry.amount)).where(XpEntry.profile_id == profile.id)) or 0
    today_xp = (
        db.scalar(
            select(func.sum(XpEntry.amount)).where(
                XpEntry.profile_id == profile.id,
                XpEntry.activity_date == today.isoformat(),
            )
        )
        or 0
    )
    days = db.scalars(
        select(XpEntry.activity_date)
        .where(
            XpEntry.profile_id == profile.id,
        )
        .distinct()
        .order_by(XpEntry.activity_date)
    ).all()
    current, longest = streaks([date.fromisoformat(day) for day in days], today)
    rows = db.scalars(
        select(StudySession)
        .where(StudySession.profile_id == profile.id)
        .order_by(StudySession.created_at.desc(), StudySession.id)
        .offset(offset)
        .limit(limit + 1)
    ).all()
    return {
        "total_xp": total,
        "today_xp": today_xp,
        "current_streak": current,
        "longest_streak": longest,
        "activity_dates": days,
        "daily_goal": settings.daily_goal,
        "show_goal": settings.show_goal,
        "goal_met": settings.daily_goal is not None and today_xp >= settings.daily_goal,
        "sessions": [
            {
                key: getattr(row, key)
                for key in (
                    "id",
                    "course_id",
                    "source_id",
                    "title",
                    "status",
                    "kind",
                    "created_at",
                    "completed_at",
                )
            }
            for row in rows[:limit]
        ],
        "offset": offset,
        "has_more": len(rows) > limit,
    }


def mistakes(db: Session, course_id: str, offset: int = 0, limit: int = 20) -> list[dict]:
    _, content = current_content(db, course_id)
    exercises = exercise_map(content)
    available = available_exercise_ids(content)
    rows = db.scalars(
        select(Mistake)
        .where(
            Mistake.profile_id == "local",
            Mistake.course_id == course_id,
            Mistake.exercise_id.in_(available),
        )
        .order_by(Mistake.updated_at.desc(), Mistake.exercise_id)
        .offset(offset)
        .limit(limit)
    ).all()
    return [
        {
            "exercise_id": row.exercise_id,
            "prompt": exercises[row.exercise_id].prompt,
            "skill": exercises[row.exercise_id].skill,
            "concepts": exercises[row.exercise_id].concepts,
            "occurrences": row.occurrences,
            "updated_at": row.updated_at,
        }
        for row in rows
        if row.exercise_id in exercises
    ]


def study_states(db: Session, course_id: str) -> dict[str, str]:
    rows = db.scalars(
        select(StudySession).where(
            StudySession.profile_id == "local",
            StudySession.course_id == course_id,
            StudySession.source_kind == "lesson",
        )
    ).all()
    states: dict[str, str] = {}
    rank = {"visited": 1, "skipped": 2, "assisted": 3, "studied": 4}
    for row in rows:
        state = "visited"
        if row.status == "completed":
            values = row.evidence.values()
            state = (
                "skipped"
                if all(e["skipped"] and not e["responses"] for e in values)
                else "assisted"
                if any(e["assisted"] for e in values)
                else "studied"
            )
        if rank[state] > rank.get(states.get(row.source_id, ""), 0):
            states[row.source_id] = state
    return states


def placement_recommendation(content: CourseContent, row: StudySession) -> dict | None:
    bank = next((item for item in content.assessment_banks if item.id == row.source_id), None)
    if (
        row.source_kind != "assessment"
        or row.status != "completed"
        or not bank
        or bank.kind != "placement"
    ):
        return None
    lessons = [
        lesson
        for unit in sorted(content.units, key=lambda item: item.order)
        if unit.status == "published"
        for lesson in sorted(unit.lessons, key=lambda item: item.order)
        if lesson.status == "published"
    ]
    missed = {
        key
        for key, item in row.evidence.items()
        if item["responses"] and not item["first_assisted"] and not item["first_correct"]
    }
    unchecked = {
        key for key, item in row.evidence.items() if not item["responses"] or item["first_assisted"]
    }
    candidates, reason = (
        missed,
        "A starting suggestion from a prompt you missed on the first unassisted check.",
    )
    if not candidates:
        candidates, reason = (
            unchecked,
            "A starting suggestion from an area you skipped or studied with support.",
        )
    for lesson in lessons:
        if any(exercise.id in candidates for exercise in lesson.exercises):
            return {
                "lesson_id": lesson.id,
                "title": lesson.title,
                "reason": reason + " You can still choose any lesson.",
            }
    # Matching the sampled questions does not certify a level. Suggest an unsampled lesson.
    for lesson in lessons:
        if not any(exercise.id in row.exercise_ids for exercise in lesson.exercises):
            return {
                "lesson_id": lesson.id,
                "title": lesson.title,
                "reason": "You matched the sampled checks. Try another area or choose any lesson.",
            }
    return (
        {
            "lesson_id": lessons[0].id,
            "title": lessons[0].title,
            "reason": "You matched the sampled checks. Replay or choose another activity.",
        }
        if lessons
        else None
    )
