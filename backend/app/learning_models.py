"""Durable study records. Content revisions and past evidence remain immutable."""

from sqlalchemy import JSON, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class StudySession(Base):
    __tablename__ = "study_sessions"
    __table_args__ = (
        Index("ix_study_timing_history", "profile_id", "status", "completed_at", "id"),
    )
    id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), index=True)
    course_version_id: Mapped[str] = mapped_column(ForeignKey("course_versions.id"))
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    source_kind: Mapped[str] = mapped_column(String)
    source_id: Mapped[str] = mapped_column(String)
    kind: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    cursor: Mapped[int]
    revision: Mapped[int]
    next_action_id: Mapped[str] = mapped_column(String)
    exercise_ids: Mapped[list] = mapped_column(JSON)
    evidence: Mapped[dict] = mapped_column(JSON)
    metadata_json: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[str] = mapped_column(String)
    completed_at: Mapped[str | None] = mapped_column(String, nullable=True)


class StudyEvent(Base):
    __tablename__ = "study_events"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    request_id: Mapped[str] = mapped_column(String, unique=True)
    session_id: Mapped[str] = mapped_column(ForeignKey("study_sessions.id"), index=True)
    request: Mapped[dict] = mapped_column(JSON)
    response: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[str] = mapped_column(String)


class XpEntry(Base):
    __tablename__ = "xp_ledger"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    session_id: Mapped[str] = mapped_column(ForeignKey("study_sessions.id"), unique=True)
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), index=True)
    amount: Mapped[int]
    occurred_at: Mapped[str] = mapped_column(String)
    activity_date: Mapped[str] = mapped_column(String, index=True)
    timezone: Mapped[str] = mapped_column(String)


class Mistake(Base):
    __tablename__ = "study_mistakes"
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), primary_key=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), primary_key=True)
    exercise_id: Mapped[str] = mapped_column(String, primary_key=True)
    course_version_id: Mapped[str] = mapped_column(ForeignKey("course_versions.id"))
    last_session_id: Mapped[str] = mapped_column(ForeignKey("study_sessions.id"))
    occurrences: Mapped[int]
    updated_at: Mapped[str] = mapped_column(String)
