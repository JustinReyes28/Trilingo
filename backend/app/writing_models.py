"""Versioned writing drafts, preserved conflicts and optional local drawing samples."""

from sqlalchemy import JSON, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class WritingDraft(Base):
    __tablename__ = "writing_drafts"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), index=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    course_version_id: Mapped[str] = mapped_column(ForeignKey("course_versions.id"))
    task_id: Mapped[str] = mapped_column(String)
    current_revision_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)
    updated_at: Mapped[str] = mapped_column(String)


class WritingRevision(Base):
    __tablename__ = "writing_revisions"
    __table_args__ = (UniqueConstraint("draft_id", "number"),)
    id: Mapped[str] = mapped_column(String, primary_key=True)
    draft_id: Mapped[str] = mapped_column(ForeignKey("writing_drafts.id"), index=True)
    number: Mapped[int]
    text: Mapped[str] = mapped_column(String)
    checklist: Mapped[list] = mapped_column(JSON)
    model_revealed: Mapped[bool]
    created_at: Mapped[str] = mapped_column(String)


class WritingConflict(Base):
    __tablename__ = "writing_conflicts"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    draft_id: Mapped[str] = mapped_column(ForeignKey("writing_drafts.id"), index=True)
    expected_revision_id: Mapped[str] = mapped_column(String)
    server_revision_id: Mapped[str] = mapped_column(ForeignKey("writing_revisions.id"))
    text: Mapped[str] = mapped_column(String)
    checklist: Mapped[list] = mapped_column(JSON)
    model_revealed: Mapped[bool]
    created_at: Mapped[str] = mapped_column(String)


class WritingSubmission(Base):
    __tablename__ = "writing_submissions"
    id: Mapped[str] = mapped_column(ForeignKey("study_sessions.id"), primary_key=True)
    draft_id: Mapped[str] = mapped_column(ForeignKey("writing_drafts.id"), index=True)
    revision_id: Mapped[str] = mapped_column(ForeignKey("writing_revisions.id"))
    self_reviewed: Mapped[bool]
    created_at: Mapped[str] = mapped_column(String)


class WritingEvent(Base):
    __tablename__ = "writing_events"
    request_id: Mapped[str] = mapped_column(String, primary_key=True)
    request: Mapped[dict] = mapped_column(JSON)
    response: Mapped[dict] = mapped_column(JSON)
    status_code: Mapped[int]
    created_at: Mapped[str] = mapped_column(String)


class DrawingSample(Base):
    __tablename__ = "drawing_samples"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), index=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"))
    course_version_id: Mapped[str] = mapped_column(ForeignKey("course_versions.id"))
    character_id: Mapped[str] = mapped_column(String)
    mode: Mapped[str] = mapped_column(String)
    strokes: Mapped[list] = mapped_column(JSON)
    created_at: Mapped[str] = mapped_column(String)
