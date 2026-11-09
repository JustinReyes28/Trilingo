"""Thin grammar/review/personal API routes."""

from collections.abc import Callable, Iterator
from typing import Annotated, Literal

from fastapi import Depends, FastAPI, Query
from pydantic import Field, field_validator
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import collections, review
from app.content_extensions import GrammarNote
from app.content_schema import Concept, Vocabulary
from app.learning import exercise_map
from app.learning_models import Mistake
from app.learning_schemas import RequestId, StudyOut
from app.reading import available_exercise_ids
from app.review_models import ReviewCard
from app.review_schemas import (
    CardAdd,
    CardOut,
    CardsOut,
    CollectionRecall,
    PersonalOut,
    QuestFallback,
    QuestOut,
    QuestRequest,
    RatingRequest,
    RecallStart,
    TimingHistory,
)
from app.schemas import StrictModel
from app.services import current_content, get_settings


class ScenarioSummary(StrictModel):
    speaking_available: bool = False
    id: str
    title: str
    kind: str
    status: str
    objectives: list[str]


class GuideUnit(StrictModel):
    id: str
    title: str
    status: str


class GrammarOut(StrictModel):
    units: list[GuideUnit]
    concepts: list[Concept]
    notes: list[GrammarNote]
    scenarios: list[ScenarioSummary]
    content_version: str
    review_note: str


class CollectionRequest(StrictModel):
    request_id: RequestId
    name: str = Field(min_length=1, max_length=80)

    @field_validator("name")
    @classmethod
    def visible_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Give the collection a name")
        return value.strip()


class MembershipRequest(StrictModel):
    item_id: str = Field(min_length=1, max_length=100)
    saved: bool


class CollectionOut(StrictModel):
    id: str
    name: str
    item_count: int
    created_at: str


class CollectionItemsOut(StrictModel):
    items: list[Vocabulary]
    has_more: bool
    offset: int


def register_practice_routes(app: FastAPI, get_db: Callable[[], Iterator[Session]]) -> None:
    DB = Annotated[Session, Depends(get_db)]

    @app.get("/api/v1/courses/{course_id}/grammar", response_model=GrammarOut)
    def grammar(
        course_id: str,
        db: DB,
        search: str = Query("", max_length=200),
        include_drafts: bool = False,
        unit_id: str | None = Query(None, max_length=100),
    ) -> dict:
        _, content = current_content(db, course_id)
        query = search.strip().casefold()
        return {
            "units": [
                {"id": unit.id, "title": unit.title, "status": unit.status}
                for unit in sorted(content.units, key=lambda unit: unit.order)
            ],
            "concepts": [
                concept.model_dump()
                for concept in content.concepts
                if query
                in (concept.id + " " + concept.title + " " + concept.explanation).casefold()
            ],
            "content_version": content.version,
            "review_note": content.review_note,
            "notes": [
                note.model_dump()
                for note in content.grammar_notes
                if (include_drafts or note.status == "published")
                and (unit_id is None or unit_id in note.unit_ids)
                and query
                in " ".join(
                    [
                        note.title,
                        note.explanation,
                        note.register_note,
                        note.culture_note,
                        *note.concepts,
                        *note.common_mistakes,
                        *(segment.surface for example in note.examples for segment in example),
                        *(
                            segment.reading or ""
                            for example in note.examples
                            for segment in example
                        ),
                    ]
                ).casefold()
            ],
            "scenarios": [
                {
                    **{
                        key: getattr(story, key)
                        for key in ("id", "title", "kind", "status", "objectives")
                    },
                    "speaking_available": bool(story.speaking_exercise_ids),
                }
                for story in content.narratives
                if story.kind in {"dialogue", "audio_episode"}
                and (include_drafts or story.status == "published")
            ],
        }

    @app.get("/api/v1/courses/{course_id}/practice-suggestion")
    def suggestion(course_id: str, db: DB) -> dict:
        _, content = current_content(db, course_id)
        settings = get_settings(db)
        due = db.scalar(
            select(ReviewCard)
            .where(
                ReviewCard.profile_id == "local",
                ReviewCard.course_id == course_id,
                ReviewCard.due <= review.now_utc().isoformat(),
            )
            .order_by(ReviewCard.due, ReviewCard.id)
            .limit(1)
        )
        if due:
            return {
                "destination": "review",
                "title": "A saved recall card is due",
                "reason": "FSRS suggests a return. Any card or another activity is available.",
            }
        available = available_exercise_ids(content)
        mistake = db.scalar(
            select(Mistake)
            .where(
                Mistake.profile_id == "local",
                Mistake.course_id == course_id,
                Mistake.exercise_id.in_(available),
            )
            .order_by(Mistake.updated_at.desc())
            .limit(1)
        )
        if mistake:
            exercise = exercise_map(content)[mistake.exercise_id]
            return {
                "destination": "grammar?concept=" + exercise.concepts[0],
                "title": "Revisit a pattern from a saved mistake",
                "reason": "This suggestion uses an actual saved response. You can skip it.",
            }
        destination = (
            "reading"
            if settings.preferred_focus == "reading"
            else "writing"
            if settings.preferred_focus == "typing"
            else "learn"
        )
        return {
            "destination": destination,
            "title": "Choose a small practice session",
            "reason": "Start with your preferred focus, or choose any published material.",
        }

    @app.post("/api/v1/courses/{course_id}/review/cards", response_model=CardOut)
    def add_card(course_id: str, body: CardAdd, db: DB) -> dict:
        return review.add_card(db, course_id, body)

    @app.post("/api/v1/courses/{course_id}/review/mistakes", response_model=CardsOut)
    def import_mistakes(
        course_id: str, db: DB, offset: int = Query(0, ge=0), limit: int = Query(20, ge=1)
    ) -> dict:
        return review.import_mistakes(db, course_id, offset, limit)

    @app.get("/api/v1/courses/{course_id}/review/cards", response_model=CardsOut)
    def cards(
        course_id: str,
        db: DB,
        offset: int = Query(0, ge=0),
        limit: int = Query(20, ge=1),
        due_only: bool = False,
    ) -> dict:
        return review.cards(db, course_id, offset, limit, due_only)

    @app.get("/api/v1/review/cards/{card_id}", response_model=CardOut)
    def card(card_id: str, db: DB) -> dict:
        return review.get_card(db, card_id)

    @app.post("/api/v1/review/cards/{card_id}/session", response_model=StudyOut)
    def recall(card_id: str, body: RecallStart, db: DB) -> dict:
        return review.open_recall(db, card_id, body.request_id)

    @app.post("/api/v1/review/cards/{card_id}/ratings", response_model=CardOut)
    def rate(card_id: str, body: RatingRequest, db: DB) -> dict:
        return review.rate(db, card_id, body)

    @app.get("/api/v1/review/cards/{card_id}/history")
    def history(
        card_id: str, db: DB, offset: int = Query(0, ge=0), limit: int = Query(20, ge=1)
    ) -> list[dict]:
        return review.review_history(db, card_id, offset, limit)

    @app.post("/api/v1/quests", response_model=QuestOut)
    def create_quest(body: QuestRequest, db: DB) -> dict:
        return review.create_quest(db, body)

    @app.post("/api/v1/quests/{assignment_id}/fallback", response_model=QuestOut)
    def quest_fallback(assignment_id: str, body: QuestFallback, db: DB) -> dict:
        return review.fallback_quest(db, assignment_id, body.request_id, body.expected_revision)

    @app.get("/api/v1/quests", response_model=list[QuestOut])
    def quests(db: DB, offset: int = Query(0, ge=0), limit: int = Query(20, ge=1)) -> list[dict]:
        return review.quests(db, offset, limit)

    @app.get("/api/v1/courses/{course_id}/collections", response_model=list[CollectionOut])
    def collection_list(
        course_id: str, db: DB, offset: int = Query(0, ge=0), limit: int = Query(20, ge=1)
    ) -> list[dict]:
        return collections.listing(db, course_id, offset, limit)

    @app.post("/api/v1/courses/{course_id}/collections", response_model=CollectionOut)
    def collection_create(course_id: str, body: CollectionRequest, db: DB) -> dict:
        return collections.create(db, course_id, body.request_id, body.name)

    @app.patch("/api/v1/collections/{collection_id}/members", response_model=CollectionOut)
    def collection_membership(collection_id: str, body: MembershipRequest, db: DB) -> dict:
        return collections.membership(db, collection_id, body.item_id, body.saved)

    @app.get("/api/v1/collections/{collection_id}/members", response_model=CollectionItemsOut)
    def collection_members(
        collection_id: str, db: DB, offset: int = Query(0, ge=0), limit: int = Query(20, ge=1)
    ) -> dict:
        return collections.members(db, collection_id, offset, limit)

    @app.post("/api/v1/collections/{collection_id}/recall", response_model=CardsOut)
    def collection_recall(
        collection_id: str,
        body: CollectionRecall,
        db: DB,
        offset: int = Query(0, ge=0),
        limit: int = Query(20, ge=1),
    ) -> dict:
        return collections.recall(db, collection_id, body, offset, limit)

    @app.get("/api/v1/personal", response_model=PersonalOut)
    def personal(db: DB) -> dict:
        return review.personal(db)

    @app.get("/api/v1/personal/timing", response_model=TimingHistory)
    def timing_history(
        db: DB,
        limit: int = Query(20, ge=1, le=100),
        cursor: str | None = Query(None, max_length=512),
        page: Literal["next", "previous", "last"] = "next",
        source_kind: str | None = Query(None, min_length=1, max_length=100),
    ) -> dict:
        return review.timing_history(db, limit, cursor, page, source_kind)
