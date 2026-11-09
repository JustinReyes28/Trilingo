"""Explicit transient audio for self-rated recall, always from the saved card snapshot."""

import base64

from sqlalchemy.orm import Session

from app import providers
from app.config import Config
from app.content_extensions import AudioCue
from app.content_schema import CourseContent, Policy
from app.grading import normalize_text
from app.learning import exercise_map
from app.models import CourseVersion
from app.review_models import ReviewCard
from app.services import DomainError, get_settings


def reference(db: Session, card_id: str) -> tuple[list[AudioCue], Policy, bool]:
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
            Policy(spacing="ignore"),
            row.direction == "speaking",
        )
    exercise = exercise_map(content)[row.item_id]
    cues = getattr(exercise, "audio", [])
    if not cues:
        raise DomainError(422, "review_audio", "This saved exercise has no authored audio cues.")
    return cues, exercise.policy, exercise.type == "speaking"


def prepare(db: Session, config: Config, card_id: str, cue_id: str, speed: float) -> dict:
    cues, _, _ = reference(db, card_id)
    cue = next((cue for cue in cues if cue.id == cue_id), None)
    if cue is None:
        raise DomainError(404, "audio_cue", "Choose a cue from this saved card.")
    provider = get_settings(db).tts
    providers.require_enabled(config, provider, "tts")
    db.commit()
    try:
        data, cached = providers.synthesize(
            provider,
            cue.transcript,
            speed,
            cache_dir=config.audio_cache_dir,
            pronunciation_override=cue.pronunciation_override,
            language=cue.language,
        )
    except providers.PROVIDER_ERRORS as error:
        raise providers.provider_failure("tts", error) from error
    return {
        "audio_base64": base64.b64encode(data).decode(),
        "mime": "audio/wav",
        "cached": cached,
        "label": (
            "Synthetic saved-card reference. Human Japanese review pending. "
            "Preparation changes no recall, schedule, evidence or XP."
        ),
    }


def transcribe(db: Session, config: Config, card_id: str, encoded: str) -> dict:
    cues, policy, speaking = reference(db, card_id)
    if not speaking:
        raise DomainError(
            422, "review_recording", "Choose a speaking recall card to compare a recording."
        )
    provider = get_settings(db).stt
    providers.require_enabled(config, provider, "stt")
    db.commit()
    try:
        text = providers.transcribe(provider, encoded)
    except providers.PROVIDER_ERRORS as error:
        raise providers.provider_failure("stt", error) from error
    target = cues[0].transcript
    return {
        "text": text,
        "target": target,
        "agrees": normalize_text(text, policy) == normalize_text(target, policy),
        "label": (
            "Transient transcript comparison only; pronunciation is unassessed. "
            "No speech evidence, schedule or XP is saved. "
            "An intentional recall rating is a self-report. Trilingo retains "
            "neither this recording nor this transcript; the STT service has "
            "its own retention settings."
        ),
    }
