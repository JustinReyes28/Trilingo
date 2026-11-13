"""Voluntary any-time FSRS, with server-owned scheduling and atomic receipts."""

import base64
import binascii
import json
from datetime import datetime, timedelta, timezone
from importlib.metadata import version as package_version
from uuid import uuid4
from zoneinfo import ZoneInfo

from fsrs import Card, Rating, Scheduler
from sqlalchemy import func, select, text, tuple_
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from app import learning, timing
from app.content_schema import CourseContent
from app.learning import complete_practice_activity, exercise_map, study_transaction
from app.learning_models import Mistake, StudySession, XpEntry
from app.models import Course, CourseVersion
from app.reading import available_exercise_ids
from app.review_models import PersonalBadge, QuestAssignment, ReviewCard, ReviewEvent
from app.review_schemas import CardAdd, QuestRequest, RatingRequest
from app.services import DomainError, current_content, get_settings, local_profile


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def scheduler_config() -> dict:
    scheduler = Scheduler(enable_fuzzing=False)
    return {
        "library": "fsrs",
        "version": package_version("fsrs"),
        "parameters": list(scheduler.parameters),
        "desired_retention": 0.9,
        "enable_fuzzing": False,
    }


def card_out(db: Session, row: ReviewCard, content: CourseContent | None = None) -> dict:
    if content is None:
        snapshot = db.get(CourseVersion, row.course_version_id)
        assert snapshot is not None
        content = CourseContent.model_validate(snapshot.data)
    audio_cues = []
    reference_text = None
    if row.item_kind == "word":
        word = next(word for word in content.vocabulary if word.id == row.item_id)
        prompt = word.gloss if row.direction in {"typing", "speaking"} else word.surface
        if row.direction in {"listening", "speaking"}:
            audio_cues = [{"id": "reference", "label": "saved word reference"}]
        if row.direction == "listening":
            prompt = "Listen, then recall the meaning. Reveal text whenever useful."
        answer = (
            word.gloss
            if row.direction == "meaning"
            else word.reading
            if row.direction == "reading"
            else word.surface
        )
        if row.direction == "listening":
            answer = word.gloss
            reference_text = word.surface
    else:
        exercise = exercise_map(content)[row.item_id]
        audio_cues = [{"id": cue.id, "label": cue.label} for cue in getattr(exercise, "audio", [])]
        prompt = exercise.prompt
        raw = getattr(exercise, "answer", getattr(exercise, "answers", []))
        if exercise.type == "speaking":
            answer = exercise.audio[0].transcript
        elif hasattr(exercise, "choices"):
            answer = next(choice.text for choice in exercise.choices if choice.id == raw)
        elif hasattr(exercise, "tokens"):
            labels = {token.id: token.text for token in exercise.tokens}
            answer = "".join(labels[key] for key in raw)
        elif hasattr(exercise, "left"):
            left = {choice.id: choice.text for choice in exercise.left}
            right = {choice.id: choice.text for choice in exercise.right}
            answer = " · ".join(left[key] + " → " + right[value] for key, value in raw.items())
        else:
            answer = " / ".join(raw)
    return {
        "id": row.id,
        "audio_cues": audio_cues,
        "reference_text": reference_text,
        "content_version": content.version,
        "item_id": row.item_id,
        "item_kind": row.item_kind,
        "direction": row.direction,
        "prompt": prompt,
        "answer": answer,
        "due": row.due,
        "revision": row.revision,
        "scheduled": bool(row.state),
        "state": row.state,
        "scheduler": row.scheduler,
    }


def add_card(db: Session, course_id: str, body: CardAdd) -> dict:
    with study_transaction(db):
        snapshot, content = current_content(db, course_id)
        if body.item_kind == "word":
            valid = any(
                word.id == body.item_id and word.status == "published"
                for word in content.vocabulary
            )
            if body.direction not in {"reading", "meaning", "typing", "listening", "speaking"}:
                valid = False
        else:
            exercise = exercise_map(content).get(body.item_id)
            valid = body.item_id in available_exercise_ids(content) and exercise is not None
            valid = valid and body.direction == exercise.skill
        if not valid:
            raise DomainError(
                404, "review_item", "Choose a published item and its supported recall direction."
            )
        row = db.scalar(
            select(ReviewCard).where(
                ReviewCard.profile_id == "local",
                ReviewCard.course_id == course_id,
                ReviewCard.item_id == body.item_id,
                ReviewCard.direction == body.direction,
            )
        )
        if row is None:
            row = ReviewCard(
                id=str(uuid4()),
                profile_id="local",
                course_id=course_id,
                course_version_id=snapshot.id,
                item_id=body.item_id,
                item_kind=body.item_kind,
                direction=body.direction,
                state={},
                due=None,
                revision=0,
                scheduler=scheduler_config(),
            )
            db.add(row)
            db.flush()
        return card_out(db, row)


def import_mistakes(db: Session, course_id: str, offset: int, limit: int) -> dict:
    with study_transaction(db):
        _, content = current_content(db, course_id)
        filters = [
            Mistake.profile_id == "local",
            Mistake.course_id == course_id,
            Mistake.exercise_id.in_(available_exercise_ids(content)),
        ]
        total = db.scalar(select(func.count()).select_from(Mistake).where(*filters)) or 0
        mistakes = db.scalars(
            select(Mistake)
            .where(*filters)
            .order_by(Mistake.exercise_id)
            .offset(offset)
            .limit(limit + 1)
        ).all()
        snapshots = {
            version.id: version
            for version in db.scalars(
                select(CourseVersion).where(
                    CourseVersion.id.in_(
                        {mistake.course_version_id for mistake in mistakes[:limit]}
                    )
                )
            ).all()
        }
        contents = {
            key: CourseContent.model_validate(snapshot.data) for key, snapshot in snapshots.items()
        }
        exercises = {key: exercise_map(content) for key, content in contents.items()}
        existing = {
            (row.item_id, row.direction): row
            for row in db.scalars(
                select(ReviewCard).where(
                    ReviewCard.profile_id == "local",
                    ReviewCard.course_id == course_id,
                    ReviewCard.item_id.in_({mistake.exercise_id for mistake in mistakes[:limit]}),
                )
            ).all()
        }
        result = []
        for mistake in mistakes[:limit]:
            snapshot = snapshots[mistake.course_version_id]
            exercise = exercises[snapshot.id][mistake.exercise_id]
            row = existing.get((mistake.exercise_id, exercise.skill))
            if row is None:
                row = ReviewCard(
                    id=str(uuid4()),
                    profile_id="local",
                    course_id=course_id,
                    course_version_id=snapshot.id,
                    item_id=exercise.id,
                    item_kind="exercise",
                    direction=exercise.skill,
                    state={},
                    due=None,
                    revision=0,
                    scheduler=scheduler_config(),
                )
                db.add(row)
                db.flush()
            result.append(card_out(db, row, contents[snapshot.id]))
        return {
            "cards": result,
            "has_more": len(mistakes) > limit,
            "offset": offset,
            "total": total,
        }


def cards(db: Session, course_id: str, offset: int, limit: int, due_only: bool) -> dict:
    local_profile(db)
    filters = [ReviewCard.profile_id == "local", ReviewCard.course_id == course_id]
    if due_only:
        filters.append(ReviewCard.due <= now_utc().isoformat())
    query = select(ReviewCard).where(*filters).order_by(ReviewCard.due, ReviewCard.id)
    rows = db.scalars(query.offset(offset).limit(limit + 1)).all()
    total = db.scalar(select(func.count()).select_from(ReviewCard).where(*filters)) or 0
    snapshots = db.scalars(
        select(CourseVersion).where(
            CourseVersion.id.in_({row.course_version_id for row in rows[:limit]})
        )
    ).all()
    contents = {version.id: CourseContent.model_validate(version.data) for version in snapshots}
    return {
        "cards": [card_out(db, row, contents[row.course_version_id]) for row in rows[:limit]],
        "offset": offset,
        "has_more": len(rows) > limit,
        "total": total,
    }


def rate(db: Session, card_id: str, body: RatingRequest) -> dict:
    request = {"card_id": card_id, **body.model_dump(exclude_none=True)}
    with study_transaction(db):
        prior = db.get(ReviewEvent, body.request_id)
        if prior:
            if prior.request != request:
                raise DomainError(409, "event_conflict", "Use a new ID for a different review.")
            return prior.response
        row = db.get(ReviewCard, card_id)
        if row is None or row.profile_id != "local":
            raise DomainError(404, "review_missing", "Review card missing. Choose another word.")
        if row.revision != body.expected_revision:
            raise DomainError(
                409, "stale_review", "Another review was saved. Reload this card and retry."
            )
        if row.scheduler["version"] != package_version("fsrs"):
            raise DomainError(
                409,
                "scheduler_version",
                (
                    "Review scheduler changed. Preserve this card and "
                    "migrate its state before rating. "
                    "Other study remains available."
                ),
            )
        now = now_utc()
        before = row.state
        card = Card.from_dict(before) if before else Card(due=now)
        row.scheduler = {**row.scheduler, "desired_retention": get_settings(db).retention}
        scheduler = Scheduler(
            parameters=row.scheduler["parameters"],
            desired_retention=row.scheduler["desired_retention"],
            enable_fuzzing=False,
        )
        updated, log = scheduler.review_card(card, Rating[body.rating], review_datetime=now)
        row.state, row.due = updated.to_dict(), updated.due.isoformat()
        row.revision += 1
        if body.recall_session_id is not None:
            session = learning._session(db, body.recall_session_id)
            if (
                session.source_kind != "review"
                or session.source_id != row.id
                or session.status == "completed"
            ):
                raise DomainError(
                    409,
                    "recall_session",
                    "Choose this card's unfinished recall timer or start a new review.",
                )
            from copy import deepcopy

            metadata = deepcopy(session.metadata_json)
            timing.freeze(metadata, now)
            metadata.update(rating=body.rating, direction=row.direction)
            session.metadata_json = metadata
            learning._finish(db, session)
            session.revision += 1
            session.next_action_id = str(uuid4())
        else:
            session = complete_practice_activity(
                db,
                row.course_id,
                row.course_version_id,
                "review",
                row.id,
                "review",
                "Voluntary recall · self-rated",
                {"rating": body.rating, "direction": row.direction},
            )
        response = card_out(db, row)
        db.add(
            ReviewEvent(
                id=body.request_id,
                card_id=row.id,
                request=request,
                response=response,
                transition={
                    "before": before,
                    "after": row.state,
                    "log": log.to_dict(),
                    "session_id": session.id,
                    "scheduler": row.scheduler,
                },
                created_at=now.isoformat(),
            )
        )
        db.flush()
        return response


def get_card(db: Session, card_id: str) -> dict:
    row = db.get(ReviewCard, card_id)
    if row is None or row.profile_id != "local":
        raise DomainError(404, "review_missing", "Choose a saved recall card.")
    return card_out(db, row)


def open_recall(db: Session, card_id: str, request_id: str) -> dict:
    request = {"action": "open_recall", "card_id": card_id}
    with study_transaction(db):
        prior = learning._receipt(db, request_id, request)
        if prior is not None:
            return prior
        card = db.get(ReviewCard, card_id)
        if card is None or card.profile_id != "local":
            raise DomainError(404, "review_missing", "Choose a saved recall card.")
        metadata = {"preview_draft": False, "mode": "supported", "evidence": "self-reported recall"}
        timing.act(metadata, "timer_start", now_utc())
        row = StudySession(
            id=str(uuid4()),
            profile_id="local",
            course_id=card.course_id,
            course_version_id=card.course_version_id,
            source_kind="review",
            source_id=card.id,
            kind="review",
            title="Voluntary recall · self-rated",
            status="active",
            cursor=0,
            revision=0,
            next_action_id=str(uuid4()),
            exercise_ids=[],
            evidence={},
            metadata_json=metadata,
            created_at=now_utc().isoformat(),
            completed_at=None,
        )
        db.add(row)
        db.flush()
        return learning._record(db, row, request_id, request)


def review_history(db: Session, card_id: str, offset: int, limit: int) -> list[dict]:
    row = db.get(ReviewCard, card_id)
    if row is None or row.profile_id != "local":
        raise DomainError(404, "review_missing", "Review card not found.")
    return [
        {"id": event.id, "created_at": event.created_at, **event.transition}
        for event in db.scalars(
            select(ReviewEvent)
            .where(ReviewEvent.card_id == card_id)
            .order_by(ReviewEvent.created_at.desc(), ReviewEvent.id)
            .offset(offset)
            .limit(limit)
        ).all()
    ]


def quest_out(row: QuestAssignment) -> dict:
    return {
        "id": row.id,
        "kind": row.kind,
        "revision": row.revision,
        "original_kind": row.original_kind,
        "definition_history": [
            {key: value for key, value in change.items() if key != "response"}
            for change in row.definition_history
        ],
        "target": row.target,
        "progress": len(row.source_ids),
        "completed_at": row.completed_at,
        "source_ids": row.source_ids,
    }


def listening_completed(session: StudySession) -> bool:
    return (
        session.source_kind == "listening"
        and bool(session.evidence)
        and all(
            item["responses"] > 0
            and not item["assisted"]
            and not item["skipped"]
            and bool(item.get("audio_cue_ids"))
            for item in session.evidence.values()
        )
    )


def speaking_completed(session: StudySession) -> bool:
    """Recorded STT attempts with delivered models, never pronunciation/mastery evidence."""
    return (
        session.source_kind == "speaking"
        and bool(session.evidence)
        and all(
            item.get("speech_attempts", 0) > 0
            and item.get("typed_fallbacks", 0) == 0
            and not item["text_fallback"]
            and not item["skipped"]
            and item.get("speech_reference_delivered", False)
            for item in session.evidence.values()
        )
    )


def fallback_quest(
    db: Session, assignment_id: str, request_id: str, expected_revision: int
) -> dict:
    with study_transaction(db):
        row = db.get(QuestAssignment, assignment_id)
        if row is None or row.profile_id != "local":
            raise DomainError(404, "quest_missing", "Choose a saved quest assignment.")
        for change in row.definition_history:
            if change["request_id"] == request_id:
                if change["expected_revision"] != expected_revision:
                    raise DomainError(
                        409, "request_conflict", "This fallback ID was used for another revision."
                    )
                return change["response"]
        if (
            row.completed_at
            or row.kind not in {"listening", "speaking"}
            or row.revision != expected_revision
        ):
            raise DomainError(
                409,
                "quest_changed",
                "Reload the quest. Only unfinished listening or speaking quests "
                "can switch to core sessions.",
            )
        change = {
            "request_id": request_id,
            "expected_revision": expected_revision,
            "from": row.kind,
            "to": "sessions",
            "at": now_utc().isoformat(),
            "prior_source_ids": list(row.source_ids),
        }
        row.kind = "sessions"
        row.revision += 1
        # Every previously credited audio workflow is a genuine completed core session.
        # Keep its source ID once; future core completions fill the remaining target.
        row.definition_history = [*row.definition_history, change]
        response = quest_out(row)
        row.definition_history = [*row.definition_history[:-1], {**change, "response": response}]
        return response


def credit_quests(db: Session, session: StudySession) -> None:
    """Credit committed source IDs inside the same session/XP transaction."""
    assignments = db.scalars(
        select(QuestAssignment).where(
            QuestAssignment.profile_id == session.profile_id,
            QuestAssignment.completed_at.is_(None),
        )
    ).all()
    for row in assignments:
        if session.id in row.source_ids or session.id in row.baseline_ids:
            continue
        valid = (
            row.kind == "sessions"
            or (row.kind == "reviews" and session.source_kind == "review")
            or (row.kind == "writing" and session.source_kind == "writing")
            or (row.kind == "listening" and listening_completed(session))
            or (row.kind == "speaking" and speaking_completed(session))
        )
        if valid:
            row.source_ids = [*row.source_ids, session.id]
            row.revision += 1
            if len(row.source_ids) >= row.target:
                row.completed_at = session.completed_at
    db.flush()
    badges = [("first-session", {})]
    if session.source_kind == "review":
        badges.append(("first-review", {"evidence": "self-reported recall"}))
    if session.source_kind == "writing":
        badges.append(("first-composition", {"evidence": "unassessed submission"}))
    ledger = db.scalar(select(XpEntry).where(XpEntry.session_id == session.id))
    assert ledger is not None
    month = ledger.activity_date[:7]
    completed = (
        db.scalar(
            select(func.count())
            .select_from(QuestAssignment)
            .join(
                XpEntry,
                XpEntry.session_id == func.json_extract(QuestAssignment.source_ids, "$[#-1]"),
            )
            .where(
                QuestAssignment.profile_id == session.profile_id,
                QuestAssignment.completed_at.is_not(None),
                XpEntry.activity_date.like(month + "%"),
            )
        )
        or 0
    )
    target = get_settings(db).monthly_quest_target
    if completed >= target:
        badges.append(
            (
                "monthly-" + month,
                {
                    "target": target,
                    "completed_quests": completed,
                    "timezone": ledger.timezone,
                    "local_month": month,
                },
            )
        )
    for badge_id, details in badges:
        db.execute(
            insert(PersonalBadge)
            .values(
                profile_id=session.profile_id,
                badge_id=badge_id,
                earned_at=session.completed_at,
                source_session_id=session.id,
                details=details,
            )
            .on_conflict_do_nothing(index_elements=["profile_id", "badge_id"])
        )


def create_quest(db: Session, body: QuestRequest) -> dict:
    with study_transaction(db):
        row = db.get(QuestAssignment, body.request_id)
        if row:
            if row.original_kind != body.kind or row.target != body.target:
                raise DomainError(409, "quest_conflict", "Use a new ID for another assignment.")
        else:
            row = QuestAssignment(
                id=body.request_id,
                profile_id="local",
                kind=body.kind,
                original_kind=body.kind,
                revision=0,
                definition_history=[],
                target=body.target,
                created_at=now_utc().isoformat(),
                baseline_ids=[],
                completed_at=None,
                source_ids=[],
            )
            db.add(row)
        return quest_out(row)


def quests(db: Session, offset: int, limit: int) -> list[dict]:
    with study_transaction(db):
        return [
            quest_out(row)
            for row in db.scalars(
                select(QuestAssignment)
                .where(QuestAssignment.profile_id == "local")
                .order_by(QuestAssignment.created_at.desc(), QuestAssignment.id)
                .offset(offset)
                .limit(limit)
            ).all()
        ]


def timing_record(row: StudySession) -> dict:
    """Describe recorded practice without turning timing or self-ratings into grades."""
    metadata = row.metadata_json
    return {
        "id": row.id,
        "source_id": row.source_id,
        "source_kind": row.source_kind,
        "title": row.title,
        "kind": row.kind,
        "mode": metadata.get("mode", "supported"),
        "direction": metadata.get("direction"),
        "rating": metadata.get("rating"),
        "elapsed_seconds": metadata["timer"]["elapsed_seconds"],
        "paused_seconds": metadata["timer"].get("paused_seconds"),
        "completed_at": row.completed_at,
        "assisted": sum(bool(item["assisted"]) for item in row.evidence.values()),
        "skipped": sum(bool(item["skipped"]) for item in row.evidence.values()),
    }


def _timing_filters(source_kind: str | None = None) -> list:
    filters = [
        StudySession.profile_id == "local",
        StudySession.status == "completed",
        func.json_extract(StudySession.metadata_json, "$.timer.valid") == 1,
        func.json_extract(StudySession.metadata_json, "$.timer.elapsed_seconds") > 0,
    ]
    if source_kind is not None:
        filters.append(StudySession.source_kind == source_kind)
    return filters


def _timing_cursor(row: StudySession) -> str:
    return base64.urlsafe_b64encode(
        json.dumps([row.completed_at, row.id], separators=(",", ":")).encode()
    ).decode()


def timing_history(
    db: Session, limit: int, cursor: str | None, page: str, source_kind: str | None
) -> dict:
    """Keyset pages remain stable when new completions are inserted between requests."""
    boundary = None
    if cursor is not None:
        try:
            value = json.loads(base64.b64decode(cursor, altchars=b"-_", validate=True))
            if (
                not isinstance(value, list)
                or len(value) != 2
                or not all(isinstance(item, str) for item in value)
                or not 1 <= len(value[1]) <= 100
                or datetime.fromisoformat(value[0]).tzinfo is None
            ):
                raise ValueError("Invalid timing boundary")
            boundary = tuple(value)
        except (ValueError, TypeError, binascii.Error, UnicodeDecodeError):
            raise DomainError(
                422, "timing_cursor", "Reload the first page of timing history."
            ) from None
    if (page == "previous" and boundary is None) or (page == "last" and boundary is not None):
        raise DomainError(
            422, "timing_page", "Choose the first, next, previous or last history page."
        )
    filters = _timing_filters(source_kind)
    position = tuple_(StudySession.completed_at, StudySession.id)
    query = select(StudySession).where(*filters)
    ascending = page in {"previous", "last"}
    if boundary is not None:
        query = query.where(position > boundary if ascending else position < boundary)
    order = (
        (StudySession.completed_at.asc(), StudySession.id.asc())
        if ascending
        else (StudySession.completed_at.desc(), StudySession.id.desc())
    )
    rows = list(db.scalars(query.order_by(*order).limit(limit)).all())
    if ascending:
        rows.reverse()
    total = db.scalar(select(func.count()).select_from(StudySession).where(*filters)) or 0

    def has_records(boundary_row: StudySession, newer: bool) -> bool:
        key = (boundary_row.completed_at, boundary_row.id)
        return (
            db.scalar(
                select(StudySession.id)
                .where(*filters, position > key if newer else position < key)
                .limit(1)
            )
            is not None
        )

    return {
        "records": [timing_record(row) for row in rows],
        "total": total,
        "previous_cursor": _timing_cursor(rows[0]) if rows and has_records(rows[0], True) else None,
        "next_cursor": _timing_cursor(rows[-1]) if rows and has_records(rows[-1], False) else None,
    }


def personal(db: Session) -> dict:
    profile = local_profile(db)
    totals: dict[str, int] = {}
    days: dict[str, tuple[int, int]] = {}
    for day, amount, count in db.execute(
        select(XpEntry.activity_date, func.sum(XpEntry.amount), func.count())
        .where(XpEntry.profile_id == "local")
        .group_by(XpEntry.activity_date)
    ):
        days[day] = (amount, count)
        date = datetime.fromisoformat(day).date()
        week = (date - timedelta(days=date.weekday())).isoformat()
        totals[week] = totals.get(week, 0) + amount
    completed = (
        db.scalar(
            select(func.count())
            .select_from(QuestAssignment)
            .where(QuestAssignment.profile_id == "local", QuestAssignment.completed_at.is_not(None))
        )
        or 0
    )
    awards = db.scalars(
        select(PersonalBadge)
        .where(PersonalBadge.profile_id == "local")
        .order_by(PersonalBadge.earned_at, PersonalBadge.badge_id)
    ).all()
    objective = (
        db.execute(
            text("""
        SELECT
            COALESCE(SUM(CASE WHEN json_extract(e.value, '$.first_assisted') = 0
                AND json_extract(e.value, '$.first_correct') IS NOT NULL
                THEN 1 ELSE 0 END), 0) assessed,
            COALESCE(SUM(CASE WHEN json_extract(e.value, '$.first_assisted') = 0
                AND json_extract(e.value, '$.first_correct') = 1
                THEN 1 ELSE 0 END), 0) correct,
            COALESCE(SUM(CASE WHEN json_extract(e.value, '$.assisted') = 1
                THEN 1 ELSE 0 END), 0) assisted,
            COALESCE(SUM(CASE WHEN json_extract(e.value, '$.skipped') = 1
                THEN 1 ELSE 0 END), 0) skipped
        FROM study_sessions s, json_each(s.evidence) e WHERE s.profile_id = :profile
    """),
            {"profile": "local"},
        )
        .mappings()
        .one()
    )
    directions = dict(
        db.execute(
            select(ReviewCard.direction, func.count(ReviewEvent.id))
            .join(ReviewEvent, ReviewEvent.card_id == ReviewCard.id)
            .where(ReviewCard.profile_id == "local")
            .group_by(ReviewCard.direction)
        ).all()
    )
    # Join each response to its immutable authored snapshot, rather than the
    # current exercise definition or a client-supplied skill/correctness flag.
    skills = {}
    for item in db.execute(
        text("""
        WITH versions AS (
            SELECT id, data FROM course_versions WHERE id IN (
                SELECT DISTINCT course_version_id FROM study_sessions WHERE profile_id = :profile
            )
        ), authored AS (
            SELECT v.id version_id, json_extract(e.value, '$.id') exercise_id,
                json_extract(e.value, '$.skill') skill
            FROM versions v, json_each(v.data, '$.practice_exercises') e
            UNION ALL
            SELECT v.id, json_extract(e.value, '$.id'), json_extract(e.value, '$.skill')
            FROM versions v, json_each(v.data, '$.units') u,
                json_each(u.value, '$.lessons') l, json_each(l.value, '$.exercises') e
        )
        SELECT a.skill,
            SUM(CASE WHEN json_extract(e.value, '$.first_assisted') = 0
                AND json_extract(e.value, '$.first_correct') IS NOT NULL
                THEN 1 ELSE 0 END) assessed,
            SUM(CASE WHEN json_extract(e.value, '$.first_assisted') = 0
                AND json_extract(e.value, '$.first_correct') = 1 THEN 1 ELSE 0 END) correct,
            SUM(CASE WHEN json_extract(e.value, '$.assisted') = 1 THEN 1 ELSE 0 END) assisted,
            SUM(CASE WHEN json_extract(e.value, '$.skipped') = 1 THEN 1 ELSE 0 END) skipped,
            SUM(COALESCE(json_extract(e.value, '$.speech_attempts'), 0)) speech_attempts,
            SUM(COALESCE(json_extract(e.value, '$.transcript_matches'), 0)) transcript_matches,
            SUM(COALESCE(json_extract(e.value, '$.typed_fallbacks'), 0)) typed_fallbacks
        FROM study_sessions s, json_each(s.evidence) e
        JOIN authored a ON a.version_id = s.course_version_id AND a.exercise_id = e.key
        WHERE s.profile_id = :profile GROUP BY a.skill
    """),
        {"profile": "local"},
    ).mappings():
        skills[item["skill"]] = {
            "speech_attempts": item["speech_attempts"],
            "transcript_matches": item["transcript_matches"],
            "typed_fallbacks": item["typed_fallbacks"],
            "objective_checks": item["assessed"],
            "initial_correct": item["correct"],
            "assisted": item["assisted"],
            "skipped": item["skipped"],
            "self_rated_reviews": 0,
        }
    for direction, count in directions.items():
        skills.setdefault(
            direction,
            {
                "objective_checks": 0,
                "initial_correct": 0,
                "assisted": 0,
                "skipped": 0,
                "self_rated_reviews": 0,
            },
        )["self_rated_reviews"] = count
    workflows = (
        db.execute(
            text("""
        SELECT s.source_kind, s.kind,
            COALESCE(json_extract(s.metadata_json, '$.evidence_mode'),
                'study workflow') evidence_label,
            COALESCE(json_extract(s.metadata_json, '$.preview_draft'), 0) draft,
            json_extract(s.metadata_json, '$.self_reviewed') self_reviewed,
            COUNT(*) count
        FROM study_sessions s JOIN xp_ledger x ON x.session_id = s.id
        WHERE s.profile_id = :profile AND s.status = 'completed'
        GROUP BY s.source_kind, s.kind, evidence_label, draft, self_reviewed
        ORDER BY s.source_kind, s.kind, evidence_label, draft, self_reviewed
    """),
            {"profile": "local"},
        )
        .mappings()
        .all()
    )
    coverage = []
    for snapshot in db.scalars(
        select(CourseVersion).join(
            Course,
            (Course.id == CourseVersion.course_id)
            & (Course.current_version == CourseVersion.version),
        )
    ).all():
        content = CourseContent.model_validate(snapshot.data)
        for stage in content.stages:
            words = [
                word
                for word in content.vocabulary
                if word.stage == stage.id and word.entry_kind == "word"
            ]
            kanji = [
                entry
                for entry in content.characters
                if entry.stage == stage.id and entry.script == "kanji"
            ]
            coverage.append(
                {
                    "course_id": content.id,
                    "content_version": content.version,
                    "stage": stage.id,
                    "title": stage.title,
                    "release": stage.release,
                    "status": stage.status,
                    "word_target": stage.word_target,
                    "kanji_target": stage.kanji_target,
                    "published_word_records": sum(word.status == "published" for word in words),
                    "published_kanji": sum(entry.status == "published" for entry in kanji),
                    "independent_review": "not recorded; qualified review pending",
                }
            )
    today = now_utc().astimezone(ZoneInfo(profile.timezone)).date()
    calendar = []
    for offset in range(83, -1, -1):
        day = (today - timedelta(days=offset)).isoformat()
        amount, count = days.get(day, (0, 0))
        calendar.append({"day": day, "xp": amount, "sessions": count})
    timed = db.scalars(
        select(StudySession)
        .where(*_timing_filters())
        .order_by(StudySession.completed_at.desc(), StudySession.id)
        .limit(20)
    ).all()
    return {
        "skill_evidence": skills,
        "completed_workflows": [
            {
                "source_kind": item["source_kind"],
                "kind": item["kind"],
                "evidence": "self-rated recall"
                if item["source_kind"] == "review"
                else item["evidence_label"],
                "draft": bool(item["draft"]),
                "count": item["count"],
                "self_reviewed": None
                if item["self_reviewed"] is None
                else bool(item["self_reviewed"]),
            }
            for item in workflows
        ],
        "curriculum_coverage": coverage,
        "activity_calendar": calendar,
        "timing_records": [timing_record(row) for row in timed],
        "objective_checks": objective["assessed"],
        "initial_correct": objective["correct"],
        "assisted_prompts": objective["assisted"],
        "skipped_prompts": objective["skipped"],
        "review_directions": directions,
        "badges": [
            {"id": badge.badge_id, "earned_at": badge.earned_at, "details": badge.details}
            for badge in awards
        ],
        "weeks": [{"week": week, "xp": totals[week]} for week in sorted(totals)[-52:]],
        "best_week_xp": max(totals.values(), default=0),
        "review_count": db.scalar(select(func.count()).select_from(ReviewEvent)) or 0,
        "quests_completed": completed,
        "monthly_badges": [
            badge.badge_id.removeprefix("monthly-")
            for badge in awards
            if badge.badge_id.startswith("monthly-")
        ],
        "level": 1 + sum(totals.values()) // 100,
        "provenance": (
            "XP and self-reported recall describe practice, not Japanese proficiency. "
            "Monthly badge records the chosen target and real completion events."
        ),
    }
