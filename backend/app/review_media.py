"""Explicit transient audio for self-rated recall, always from the saved card snapshot."""

import base64

from sqlalchemy.orm import Session

from app import audio_pack
from app.config import Config
from app.content_extensions import AudioCue
from app.content_schema import CourseContent
from app.learning import exercise_map
from app.models import CourseVersion
from app.review_models import ReviewCard
from app.services import DomainError


def reference(db: Session, card_id: str) -> tuple[list[AudioCue], CourseContent]:
    row = db.get(ReviewCard, card_id)
    if row is None or row.profile_id != "local":
        raise DomainError(404, "review_missing", "Choose a saved recall card.")
    snapshot = db.get(CourseVersion, row.course_version_id)
    assert snapshot is not None
    content = CourseContent.model_validate(snapshot.data)
    if row.direction not in {"listening", "speaking"}:
        raise DomainError(422, "review_audio", "Choose a listening or speaking recall direction.")
    if row.item_kind == "word":
        word = next(word for word in content.vocabulary if word.id == row.item_id)
        return (
            [
                AudioCue(
                    id="reference",
                    label="saved word reference",
                    transcript=word.surface,
                    pronunciation_override=word.pronunciation_override,
                )
            ],
            content,
        )
    exercise = exercise_map(content)[row.item_id]
    cues = getattr(exercise, "audio", [])
    if not cues:
        raise DomainError(422, "review_audio", "This saved exercise has no authored audio cues.")
    return cues, content


def prepare(db: Session, config: Config, card_id: str, cue_id: str, speed: float) -> dict:
    cues, content = reference(db, card_id)
    cue = next((cue for cue in cues if cue.id == cue_id), None)
    if cue is None:
        raise DomainError(404, "audio_cue", "Choose a cue from this saved card.")
    clip = audio_pack.lookup(
        config,
        content.id,
        cue.transcript,
        cue.language,
        cue.pronunciation_override,
        preferred_version=content.version,
    )
    if clip is None:
        raise DomainError(
            503,
            "audio_unavailable",
            "Bundled saved-card audio is unavailable. Reveal text or self-rate directly.",
        )
    return {
        "audio_base64": base64.b64encode(clip.data).decode(),
        "mime": clip.mime,
        "cached": True,
        "source": "pack",
        "label": (
            audio_pack.label(clip, cue.language)
            + " Preparation changes no recall, schedule, evidence or XP."
        ),
    }
