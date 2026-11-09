"""Local writing workflows; autosaves never grade or award XP."""

from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.content_schema import CourseContent, WritingTask
from app.learning import PRACTICE_XP, complete_practice_activity, now_utc, study_transaction
from app.models import CourseVersion
from app.services import DomainError, current_content
from app.writing_models import (
    WritingConflict,
    WritingDraft,
    WritingEvent,
    WritingRevision,
    WritingSubmission,
)
from app.writing_schemas import DraftCreate, DraftOut, DraftSave, DraftSubmit, SubmissionOut


def _task(content: CourseContent, task_id: str) -> WritingTask:
    task = next((entry for entry in content.writing_tasks if entry.id == task_id), None)
    if task is None:
        raise DomainError(404, "writing_task", "Writing task not found. Choose another task.")
    return task


def _draft(db: Session, draft_id: str) -> WritingDraft:
    row = db.get(WritingDraft, draft_id)
    if row is None or row.profile_id != "local":
        raise DomainError(
            404, "writing_draft", "Draft not found. Open a saved draft or start a new one."
        )
    return row


def _content(db: Session, draft: WritingDraft) -> CourseContent:
    version = db.get(CourseVersion, draft.course_version_id)
    assert version is not None
    return CourseContent.model_validate(version.data)


def _revision_out(row: WritingRevision) -> dict:
    return {
        key: getattr(row, key)
        for key in ("id", "number", "text", "checklist", "model_revealed", "created_at")
    }


def draft_out(db: Session, row: WritingDraft) -> dict:
    content = _content(db, row)
    revision = db.get(WritingRevision, row.current_revision_id)
    assert revision is not None
    return DraftOut.model_validate(
        {
            "id": row.id,
            "course_id": row.course_id,
            "content_version": content.version,
            "task": _task(content, row.task_id).model_dump(),
            "current": _revision_out(revision),
            "created_at": row.created_at,
            "updated_at": row.updated_at,
        }
    ).model_dump(mode="json")


def get_draft(db: Session, draft_id: str) -> dict:
    return draft_out(db, _draft(db, draft_id))


def catalog(
    db: Session, course_id: str, include_drafts: bool = False, offset: int = 0, limit: int = 20
) -> dict:
    _, content = current_content(db, course_id)
    rows = db.scalars(
        select(WritingDraft)
        .where(WritingDraft.profile_id == "local", WritingDraft.course_id == course_id)
        .order_by(WritingDraft.updated_at.desc(), WritingDraft.id)
        .offset(offset)
        .limit(limit + 1)
    ).all()
    versions = {
        row.id: CourseContent.model_validate(row.data)
        for row in db.scalars(
            select(CourseVersion).where(
                CourseVersion.id.in_({row.course_version_id for row in rows})
            )
        ).all()
    }
    return {
        "tasks": [
            task.model_dump()
            for task in content.writing_tasks
            if include_drafts or task.status == "published"
        ],
        "drafts": [
            {
                "id": row.id,
                "task_id": row.task_id,
                "title": _task(versions[row.course_version_id], row.task_id).genre,
                "content_version": versions[row.course_version_id].version,
                "updated_at": row.updated_at,
            }
            for row in rows[:limit]
        ],
        "offset": offset,
        "has_more": len(rows) > limit,
        "includes_drafts": include_drafts,
        "content_version": content.version,
    }


def receipt(db: Session, request_id: str, request: dict) -> tuple[dict, int] | None:
    prior = db.get(WritingEvent, request_id)
    if prior:
        if prior.request != request:
            raise DomainError(
                409, "request_conflict", "This action ID belongs to another writing request."
            )
        return prior.response, prior.status_code
    return None


def record(
    db: Session, request_id: str, request: dict, response: dict, status: int = 200
) -> tuple[dict, int]:
    db.add(
        WritingEvent(
            request_id=request_id,
            request=request,
            response=response,
            status_code=status,
            created_at=now_utc().isoformat(),
        )
    )
    return response, status


def get_receipt(db: Session, request_id: str) -> tuple[dict, int]:
    with study_transaction(db):
        event = db.get(WritingEvent, request_id)
        if event is None:
            raise DomainError(
                404,
                "writing_receipt",
                "No confirmed writing activity for this request yet. "
                "Retry checking or start a fresh activity deliberately.",
            )
        return event.response, event.status_code


def create_draft(db: Session, course_id: str, body: DraftCreate) -> tuple[dict, int]:
    request = {"action": "create_draft", "course_id": course_id, **body.model_dump()}
    with study_transaction(db):
        prior = receipt(db, body.request_id, request)
        if prior:
            return prior
        version, content = current_content(db, course_id)
        task = _task(content, body.task_id)
        if task.status != "published" and not body.preview_draft:
            raise DomainError(
                404, "draft_task", "Enable draft practice to inspect this unreviewed task."
            )
        now = now_utc().isoformat()
        revision_id = str(uuid4())
        draft = WritingDraft(
            id=str(uuid4()),
            profile_id="local",
            course_id=course_id,
            course_version_id=version.id,
            task_id=task.id,
            current_revision_id=revision_id,
            created_at=now,
            updated_at=now,
        )
        db.add(draft)
        db.flush()
        db.add(
            WritingRevision(
                id=revision_id,
                draft_id=draft.id,
                number=0,
                text="",
                checklist=[],
                model_revealed=False,
                created_at=now,
            )
        )
        db.flush()
        return record(db, body.request_id, request, draft_out(db, draft))


def save_draft(db: Session, draft_id: str, body: DraftSave) -> tuple[dict, int]:
    request = {"action": "save_draft", "draft_id": draft_id, **body.model_dump()}
    with study_transaction(db):
        prior = receipt(db, body.request_id, request)
        if prior:
            return prior
        draft = _draft(db, draft_id)
        task = _task(_content(db, draft), draft.task_id)
        if len(set(body.checklist)) != len(body.checklist) or not set(body.checklist) <= set(
            task.checklist
        ):
            raise DomainError(
                422, "writing_checklist", "Choose self-review points from this task's checklist."
            )
        now = now_utc().isoformat()
        current = db.get(WritingRevision, draft.current_revision_id)
        assert current is not None
        if body.expected_revision_id != draft.current_revision_id:
            expected = db.get(WritingRevision, body.expected_revision_id)
            if expected is None or expected.draft_id != draft.id:
                raise DomainError(
                    422, "writing_revision", "Choose a revision belonging to this draft."
                )
            db.add(
                WritingConflict(
                    id=body.request_id,
                    draft_id=draft.id,
                    expected_revision_id=body.expected_revision_id,
                    server_revision_id=current.id,
                    text=body.text,
                    checklist=body.checklist,
                    model_revealed=body.model_revealed,
                    created_at=now,
                )
            )
            return record(
                db,
                body.request_id,
                request,
                {
                    "error": {
                        "code": "writing_conflict",
                        "message": (
                            "Another revision was saved. Both texts are preserved. "
                            "Review the saved text and conflict history before merging."
                        ),
                    }
                },
                409,
            )
        revision = WritingRevision(
            id=str(uuid4()),
            draft_id=draft.id,
            number=current.number + 1,
            text=body.text,
            checklist=body.checklist,
            model_revealed=current.model_revealed or body.model_revealed,
            created_at=now,
        )
        db.add(revision)
        draft.current_revision_id, draft.updated_at = revision.id, now
        db.flush()
        return record(db, body.request_id, request, draft_out(db, draft))


def history(db: Session, draft_id: str, offset: int = 0, limit: int = 20) -> dict:
    draft = _draft(db, draft_id)
    revisions = db.scalars(
        select(WritingRevision)
        .where(WritingRevision.draft_id == draft.id)
        .order_by(WritingRevision.number.desc())
        .offset(offset)
        .limit(limit + 1)
    ).all()
    conflicts = db.scalars(
        select(WritingConflict)
        .where(WritingConflict.draft_id == draft.id)
        .order_by(WritingConflict.created_at.desc(), WritingConflict.id)
        .offset(offset)
        .limit(limit + 1)
    ).all()
    return {
        "revisions": [_revision_out(row) for row in revisions[:limit]],
        "conflicts": [
            {
                key: getattr(row, key)
                for key in (
                    "id",
                    "text",
                    "checklist",
                    "model_revealed",
                    "expected_revision_id",
                    "server_revision_id",
                    "created_at",
                )
            }
            for row in conflicts[:limit]
        ],
        "has_more_revisions": len(revisions) > limit,
        "has_more_conflicts": len(conflicts) > limit,
        "offset": offset,
    }


def submit_draft(db: Session, draft_id: str, body: DraftSubmit) -> tuple[dict, int]:
    request = {"action": "submit_draft", "draft_id": draft_id, **body.model_dump()}
    with study_transaction(db):
        prior = receipt(db, body.request_id, request)
        if prior:
            return prior
        draft = _draft(db, draft_id)
        revision = db.get(WritingRevision, body.revision_id)
        if revision is None or revision.draft_id != draft.id:
            raise DomainError(422, "writing_revision", "Choose a saved revision of this draft.")
        if not revision.text.strip():
            raise DomainError(422, "empty_writing", "Write and save the text you intend to submit.")
        content = _content(db, draft)
        task = _task(content, draft.task_id)
        session = complete_practice_activity(
            db,
            draft.course_id,
            draft.course_version_id,
            "writing",
            draft.task_id,
            "open_writing",
            "Writing practice · " + task.genre,
            {
                "preview_draft": task.status != "published",
                "draft_id": draft.id,
                "revision_id": revision.id,
                "rubric_version": task.rubric_version,
                "evidence_mode": "open_writing",
                "self_reviewed": body.self_reviewed,
                "model_revealed": revision.model_revealed,
                "objective_correctness": None,
            },
        )
        db.add(
            WritingSubmission(
                id=session.id,
                draft_id=draft.id,
                revision_id=revision.id,
                self_reviewed=body.self_reviewed,
                created_at=session.completed_at,
            )
        )
        result = SubmissionOut(
            id=session.id,
            draft_id=draft.id,
            revision_id=revision.id,
            xp_awarded=PRACTICE_XP,
            assessment="self_reviewed" if body.self_reviewed else "not_assessed",
            message=(
                "Writing practice saved. Language quality is not assessed; self-review is advisory."
            ),
        ).model_dump()
        return record(db, body.request_id, request, result)
