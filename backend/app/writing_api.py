from collections.abc import Callable, Iterator
from typing import Annotated

from fastapi import Depends, FastAPI, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import handwriting, writing
from app.content_extensions import CharacterEntry
from app.content_schema import License
from app.schemas import StrictModel
from app.writing_schemas import (
    DraftCreate,
    DraftOut,
    DraftSave,
    DraftSubmit,
    HandwritingCommit,
    HandwritingOut,
    SampleOut,
    StrokeGuide,
    SubmissionOut,
    WritingCatalog,
    WritingHistory,
)


class GuideOut(StrictModel):
    character: CharacterEntry
    content_version: str
    guide: StrokeGuide | None
    license: License | None
    message: str


class DeleteOut(StrictModel):
    deleted: bool


def register_writing_routes(app: FastAPI, get_db: Callable[[], Iterator[Session]]) -> None:
    DB = Annotated[Session, Depends(get_db)]
    Offset = Annotated[int, Query(ge=0)]
    Limit = Annotated[int, Query(ge=1, le=10000)]

    @app.get("/api/v1/courses/{course_id}/writing", response_model=WritingCatalog)
    def catalog(
        course_id: str, db: DB, include_drafts: bool = False, offset: Offset = 0, limit: Limit = 20
    ) -> dict:
        return writing.catalog(db, course_id, include_drafts, offset, limit)

    @app.post("/api/v1/courses/{course_id}/writing/drafts", response_model=DraftOut)
    def create(course_id: str, body: DraftCreate, db: DB):
        result, status = writing.create_draft(db, course_id, body)
        return JSONResponse(content=result, status_code=status)

    @app.get("/api/v1/writing/drafts/{draft_id}", response_model=DraftOut)
    def get(draft_id: str, db: DB) -> dict:
        return writing.get_draft(db, draft_id)

    @app.post("/api/v1/writing/drafts/{draft_id}/revisions", response_model=DraftOut)
    def save(draft_id: str, body: DraftSave, db: DB):
        result, status = writing.save_draft(db, draft_id, body)
        return JSONResponse(content=result, status_code=status)

    @app.get("/api/v1/writing/drafts/{draft_id}/history", response_model=WritingHistory)
    def history(draft_id: str, db: DB, offset: Offset = 0, limit: Limit = 20) -> dict:
        return writing.history(db, draft_id, offset, limit)

    @app.post("/api/v1/writing/drafts/{draft_id}/submissions", response_model=SubmissionOut)
    def submit(draft_id: str, body: DraftSubmit, db: DB):
        result, status = writing.submit_draft(db, draft_id, body)
        return JSONResponse(content=result, status_code=status)

    @app.get(
        "/api/v1/courses/{course_id}/writing/characters/{character_id}", response_model=GuideOut
    )
    def guide(course_id: str, character_id: str, db: DB, preview_draft: bool = False) -> dict:
        return handwriting.guide_view(db, course_id, character_id, preview_draft)

    @app.post("/api/v1/courses/{course_id}/writing/handwriting", response_model=HandwritingOut)
    def commit(course_id: str, body: HandwritingCommit, db: DB):
        result, status = handwriting.commit(db, course_id, body)
        return JSONResponse(content=result, status_code=status)

    @app.get(
        "/api/v1/writing/receipts/{request_id}",
        response_model=DraftOut | SubmissionOut | HandwritingOut,
    )
    def receipt(request_id: str, db: DB) -> JSONResponse:
        result, status = writing.get_receipt(db, request_id)
        return JSONResponse(content=result, status_code=status)

    @app.get("/api/v1/writing/samples", response_model=list[SampleOut])
    def samples(db: DB, offset: Offset = 0, limit: Limit = 20) -> list[dict]:
        return handwriting.list_samples(db, offset, limit)

    @app.delete("/api/v1/writing/samples/{sample_id}", response_model=DeleteOut)
    def delete(sample_id: str, db: DB) -> dict:
        return handwriting.delete_sample(db, sample_id)
