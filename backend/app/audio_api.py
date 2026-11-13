import base64
from collections.abc import Callable, Iterator
from typing import Annotated, Literal

from fastapi import Depends, FastAPI
from pydantic import Field
from sqlalchemy.orm import Session

from app import audio_learning, audio_pack, review_media
from app.config import Config
from app.learning_schemas import RequestId, StudyOut
from app.schemas import StrictModel
from app.services import DomainError, current_content, list_courses


class AudioRequest(StrictModel):
    course_id: str = Field(min_length=1, max_length=100)
    item_id: str = Field(min_length=1, max_length=100)
    turn_id: str | None = Field(default=None, max_length=100)
    speed: Literal[0.75, 1.0] = 1.0
    language: Literal["ja", "en"] = "ja"
    preview_draft: bool = False


class AudioOut(StrictModel):
    audio_base64: str
    mime: Literal["audio/mpeg"]
    cached: bool
    source: Literal["pack"]
    label: str


class StudyAudioRequest(StrictModel):
    request_id: RequestId
    expected_revision: int = Field(ge=0)
    speed: Literal[0.75, 1.0] = 1.0


class ReviewAudioRequest(StrictModel):
    speed: Literal[0.75, 1.0] = 1.0


class StudyAudioOut(AudioOut):
    session: StudyOut


class AudioPackStatus(StrictModel):
    bundled_reference: bool = False
    bundled_reviewed: bool = False
    course_version: str | None = None
    message: str


class AudioStatus(StrictModel):
    audio_pack: AudioPackStatus


class AudioTurn(StrictModel):
    id: str
    text: str


class AudioNarrative(StrictModel):
    id: str
    title: str
    kind: str
    status: str
    turns: list[AudioTurn]
    speaking_available: bool = False


def _authored_reference_with_version(
    db: Session, body: AudioRequest
) -> tuple[str, str | None, Literal["ja", "en"], str]:
    _, content = current_content(db, body.course_id)
    word = next((word for word in content.vocabulary if word.id == body.item_id), None)
    if word and (word.status == "published" or body.preview_draft):
        if body.language == "en":
            return word.gloss, None, "en", content.version
        return word.surface, word.pronunciation_override, "ja", content.version
    if body.language == "en":
        raise DomainError(
            404,
            "audio_reference",
            "Choose an available vocabulary word for English reference audio.",
        )
    story = next((story for story in content.narratives if story.id == body.item_id), None)
    if story and (story.status == "published" or body.preview_draft):
        turn = next((turn for turn in story.turns if turn.id == body.turn_id), None)
        if turn:
            text = "".join(segment.surface for segment in turn.text)
            if len(text) <= 500:
                return text, turn.pronunciation_override, "ja", content.version
    raise DomainError(
        404, "audio_reference", "Choose an available authored word or short story turn."
    )


def register_audio_routes(
    app: FastAPI, get_db: Callable[[], Iterator[Session]], config: Config
) -> None:
    DB = Annotated[Session, Depends(get_db)]

    @app.post(
        "/api/v1/sessions/{session_id}/exercises/{exercise_id}/audio/{cue_id}",
        response_model=StudyAudioOut,
    )
    def study_audio(
        session_id: str, exercise_id: str, cue_id: str, body: StudyAudioRequest, db: DB
    ) -> dict:
        return audio_learning.prepare(
            db,
            config,
            session_id,
            exercise_id,
            cue_id,
            body.request_id,
            body.expected_revision,
            body.speed,
        )

    @app.post("/api/v1/review/cards/{card_id}/audio/{cue_id}", response_model=AudioOut)
    def recall_audio(card_id: str, cue_id: str, body: ReviewAudioRequest, db: DB) -> dict:
        return review_media.prepare(db, config, card_id, cue_id, body.speed)

    @app.get("/api/v1/audio/status", response_model=AudioStatus)
    def status(db: DB, course_id: str | None = None) -> dict:
        course = course_id or next((item["id"] for item in list_courses(db)), "")
        pack_summary = audio_pack.summary(config, course)
        bundled = pack_summary is not None
        reviewed = pack_summary.reviewed if pack_summary else False
        return {
            "audio_pack": {
                "bundled_reference": bundled,
                "bundled_reviewed": reviewed,
                "course_version": pack_summary.course_version if pack_summary else None,
                "message": (
                    (
                        "Bundled authored reference audio is available and human reviewed."
                        if reviewed
                        else "Bundled authored reference audio is available; human review pending."
                    )
                    if bundled
                    else "Bundled authored reference audio is unavailable. Use text alternatives."
                ),
            },
        }

    @app.get("/api/v1/courses/{course_id}/audio/library", response_model=list[AudioNarrative])
    def library(course_id: str, db: DB, include_drafts: bool = False) -> list[dict]:
        _, content = current_content(db, course_id)
        return [
            {
                "id": story.id,
                "title": story.title,
                "kind": story.kind,
                "status": story.status,
                "speaking_available": bool(story.speaking_exercise_ids),
                "turns": [
                    {"id": turn.id, "text": "".join(part.surface for part in turn.text)}
                    for turn in story.turns
                ],
            }
            for story in content.narratives
            if include_drafts or story.status == "published"
        ]

    @app.post("/api/v1/audio/speech", response_model=AudioOut)
    def speech(body: AudioRequest, db: DB) -> dict:
        text, pronunciation, language, content_version = _authored_reference_with_version(db, body)
        clip = audio_pack.lookup(
            config,
            body.course_id,
            text,
            language,
            pronunciation,
            preferred_version=content_version,
        )
        if clip is None:
            raise DomainError(
                503,
                "audio_unavailable",
                "Bundled reference audio is unavailable for this item. Use the text alternative.",
            )
        return {
            "audio_base64": base64.b64encode(clip.data).decode(),
            "mime": clip.mime,
            "cached": True,
            "source": "pack",
            "label": audio_pack.label(clip, language),
        }
