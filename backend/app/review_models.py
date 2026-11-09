"""Actual FSRS state, immutable rating receipts, and optional quest assignments."""

from sqlalchemy import JSON, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class ReviewCard(Base):
    __tablename__ = "review_cards"
    __table_args__ = (UniqueConstraint("profile_id", "course_id", "item_id", "direction"),)
    id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"))
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"))
    course_version_id: Mapped[str] = mapped_column(ForeignKey("course_versions.id"))
    item_id: Mapped[str] = mapped_column(String)
    item_kind: Mapped[str] = mapped_column(String, default="word", server_default="word")
    direction: Mapped[str] = mapped_column(String)
    state: Mapped[dict] = mapped_column(JSON)
    due: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
    revision: Mapped[int]
    scheduler: Mapped[dict] = mapped_column(JSON)


class ReviewEvent(Base):
    __tablename__ = "review_events"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    card_id: Mapped[str] = mapped_column(ForeignKey("review_cards.id"), index=True)
    request: Mapped[dict] = mapped_column(JSON)
    response: Mapped[dict] = mapped_column(JSON)
    transition: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[str] = mapped_column(String)


class QuestAssignment(Base):
    __tablename__ = "quest_assignments"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"))
    kind: Mapped[str] = mapped_column(String)
    target: Mapped[int]
    created_at: Mapped[str] = mapped_column(String)
    original_kind: Mapped[str] = mapped_column(String, server_default="sessions")
    revision: Mapped[int] = mapped_column(default=0, server_default="0")
    definition_history: Mapped[list] = mapped_column(JSON, default=list, server_default="[]")
    baseline_ids: Mapped[list] = mapped_column(JSON)
    completed_at: Mapped[str | None] = mapped_column(String, nullable=True)
    source_ids: Mapped[list] = mapped_column(JSON)


class PersonalBadge(Base):
    __tablename__ = "personal_badges"
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), primary_key=True)
    badge_id: Mapped[str] = mapped_column(String, primary_key=True)
    earned_at: Mapped[str] = mapped_column(String)
    source_session_id: Mapped[str] = mapped_column(ForeignKey("study_sessions.id"))
    details: Mapped[dict] = mapped_column(JSON)


class VocabularyCollection(Base):
    __tablename__ = "vocabulary_collections"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), index=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"))
    name: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)


class CollectionMember(Base):
    __tablename__ = "collection_members"
    collection_id: Mapped[str] = mapped_column(
        ForeignKey("vocabulary_collections.id"), primary_key=True
    )
    item_id: Mapped[str] = mapped_column(String, primary_key=True)
    course_version_id: Mapped[str] = mapped_column(ForeignKey("course_versions.id"))
