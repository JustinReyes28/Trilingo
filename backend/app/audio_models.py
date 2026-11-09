"""Idempotent prepared reference audio; no learner recordings are retained."""

from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class AudioDelivery(Base):
    __tablename__ = "audio_deliveries"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    session_id: Mapped[str] = mapped_column(ForeignKey("study_sessions.id"), index=True)
    request: Mapped[dict] = mapped_column(JSON)
    provider: Mapped[dict] = mapped_column(JSON)
    cue: Mapped[dict] = mapped_column(JSON)
    result: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[str] = mapped_column(String)
