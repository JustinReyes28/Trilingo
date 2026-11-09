from collections.abc import Callable, Iterator
from typing import Annotated, Literal

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import reading
from app.reading_schemas import ReadingItemOut, ReadingItemPatch, ReadingLibrary


def register_reading_routes(app: FastAPI, get_db: Callable[[], Iterator[Session]]) -> None:
    DB = Annotated[Session, Depends(get_db)]

    @app.get("/api/v1/courses/{course_id}/reading", response_model=ReadingLibrary)
    def library(course_id: str, db: DB, include_drafts: bool = False) -> dict:
        return reading.library(db, course_id, include_drafts)

    @app.patch(
        "/api/v1/courses/{course_id}/reading/items/{kind}/{item_id}", response_model=ReadingItemOut
    )
    def item(
        course_id: str,
        kind: Literal["word", "character", "grammar"],
        item_id: str,
        body: ReadingItemPatch,
        db: DB,
    ) -> dict:
        return reading.patch_item(db, course_id, kind, item_id, body)
