"""Learner-selected reading support, separate from objective assessment evidence."""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class ReadingItem(Base):
    __tablename__ = "reading_items"
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), primary_key=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), primary_key=True)
    item_kind: Mapped[str] = mapped_column(String, primary_key=True)
    item_id: Mapped[str] = mapped_column(String, primary_key=True)
    course_version_id: Mapped[str] = mapped_column(ForeignKey("course_versions.id"))
    saved: Mapped[bool]
    familiar: Mapped[bool]
    updated_at: Mapped[str] = mapped_column(String)
