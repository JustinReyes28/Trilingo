from collections.abc import Callable, Iterator
from typing import Annotated

from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from app import learning
from app.learning_schemas import (
    ActionRequest,
    AssessmentOut,
    MistakeOut,
    ProgressOut,
    StartRequest,
    StudyOut,
)
from app.services import current_content


def register_learning_routes(app: FastAPI, get_db: Callable[[], Iterator[Session]]) -> None:
    DB = Annotated[Session, Depends(get_db)]

    @app.post("/api/v1/courses/{course_id}/sessions", response_model=StudyOut)
    def start(course_id: str, body: StartRequest, db: DB) -> dict:
        return learning.start_session(db, course_id, body)

    @app.get("/api/v1/sessions/{session_id}", response_model=StudyOut)
    def detail(session_id: str, db: DB) -> dict:
        return learning.get_session(db, session_id)

    @app.post("/api/v1/sessions/{session_id}/actions", response_model=StudyOut)
    def action(session_id: str, body: ActionRequest, db: DB) -> dict:
        return learning.apply_action(db, session_id, body)

    @app.get("/api/v1/progress", response_model=ProgressOut)
    def progress(db: DB, offset: int = Query(0, ge=0), limit: int = Query(20, ge=1)) -> dict:
        return learning.progress(db, offset, limit)

    @app.get("/api/v1/courses/{course_id}/mistakes", response_model=list[MistakeOut])
    def mistakes(
        course_id: str, db: DB, offset: int = Query(0, ge=0), limit: int = Query(20, ge=1)
    ) -> list[dict]:
        return learning.mistakes(db, course_id, offset, limit)

    @app.get("/api/v1/courses/{course_id}/assessments", response_model=list[AssessmentOut])
    def assessments(course_id: str, db: DB) -> list[dict]:
        _, content = current_content(db, course_id)
        return [
            {
                "id": bank.id,
                "title": bank.title,
                "kind": bank.kind,
                "status": bank.status,
                "exercise_count": len(bank.exercise_ids),
                "scoring_policy": bank.scoring_policy,
            }
            for bank in content.assessment_banks
        ]
