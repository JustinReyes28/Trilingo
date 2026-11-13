import base64
from collections.abc import Callable, Iterator
from typing import Annotated, Literal

from fastapi import Depends, FastAPI
from pydantic import Field
from sqlalchemy.orm import Session

from app import audio_learning, audio_pack, providers, review_media, scenario_practice, speaking
from app.config import Config
from app.content_schema import Policy
from app.grading import normalize_text
from app.learning import _content, _session, exercise_map
from app.learning_schemas import RequestId, StudyOut
from app.schemas import StrictModel
from app.services import DomainError, current_content, get_settings, list_courses


class AudioRequest(StrictModel):
    course_id: str = Field(min_length=1, max_length=100)
    item_id: str = Field(min_length=1, max_length=100)
    turn_id: str | None = Field(default=None, max_length=100)
    speed: Literal[0.75, 1.0] = 1.0
    language: Literal["ja", "en"] = "ja"
    preview_draft: bool = False


class SpeechRequest(AudioRequest):
    audio_base64: str = Field(max_length=1_400_000)


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


class StudySpeechRequest(StrictModel):
    request_id: RequestId
    expected_revision: int = Field(ge=0)
    audio_base64: str = Field(min_length=1, max_length=1_400_000)


class ReviewAudioRequest(StrictModel):
    speed: Literal[0.75, 1.0] = 1.0


class ReviewSpeechRequest(StrictModel):
    audio_base64: str = Field(min_length=1, max_length=1_400_000)


class StudyAudioOut(AudioOut):
    session: StudyOut


class TranscriptOut(StrictModel):
    text: str
    target: str
    agrees: bool
    label: str


class ExplanationRequest(StrictModel):
    session_id: str
    exercise_id: str


class ExplanationOut(StrictModel):
    authored: str
    generated: str | None = None
    status: str


class ProviderCapability(StrictModel):
    enabled: bool
    provider: str
    verified: bool
    message: str


class AudioPackStatus(StrictModel):
    bundled_reference: bool = False
    bundled_reviewed: bool = False
    course_version: str | None = None
    message: str


class ProviderStatus(StrictModel):
    ai: ProviderCapability
    stt: ProviderCapability
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


def authored_reference(
    db: Session, body: AudioRequest
) -> tuple[str, str | None, Literal["ja", "en"]]:
    text, pronunciation, language, _ = _authored_reference_with_version(db, body)
    return text, pronunciation, language


def authored_text(db: Session, body: AudioRequest) -> str:
    return authored_reference(db, body)[0]


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

    @app.post(
        "/api/v1/sessions/{session_id}/exercises/{exercise_id}/speech",
        response_model=StudyOut,
    )
    def study_speech(session_id: str, exercise_id: str, body: StudySpeechRequest, db: DB) -> dict:
        return speaking.submit(
            db,
            config,
            session_id,
            exercise_id,
            body.request_id,
            body.expected_revision,
            body.audio_base64,
        )

    @app.post("/api/v1/review/cards/{card_id}/audio/{cue_id}", response_model=AudioOut)
    def recall_audio(card_id: str, cue_id: str, body: ReviewAudioRequest, db: DB) -> dict:
        return review_media.prepare(db, config, card_id, cue_id, body.speed)

    @app.post("/api/v1/review/cards/{card_id}/transcriptions", response_model=TranscriptOut)
    def recall_transcript(card_id: str, body: ReviewSpeechRequest, db: DB) -> dict:
        return review_media.transcribe(db, config, card_id, body.audio_base64)

    @app.post(
        "/api/v1/scenarios/transcriptions", response_model=scenario_practice.ScenarioTranscript
    )
    def scenario_transcript(body: scenario_practice.ScenarioRecordingRequest, db: DB) -> dict:
        return scenario_practice.transcribe_reply(db, config, body)

    @app.get("/api/v1/providers/status", response_model=ProviderStatus)
    def status(db: DB, course_id: str | None = None) -> dict:
        settings = get_settings(db)
        course = course_id or next((item["id"] for item in list_courses(db)), "")
        pack_summary = audio_pack.summary(config, course)
        bundled = pack_summary is not None
        reviewed = pack_summary.reviewed if pack_summary else False
        return {
            **{
                kind: {
                    "enabled": (
                        getattr(config, kind + "_enabled") and getattr(settings, kind).enabled
                    ),
                    "provider": getattr(settings, kind).provider,
                    "verified": False,
                    "message": (
                        "Configured capability is not a real playback/transcription verification."
                    ),
                }
                for kind in ("ai", "stt")
            },
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

    @app.post("/api/v1/audio/transcriptions", response_model=TranscriptOut)
    def transcription(body: SpeechRequest, db: DB) -> dict:
        if body.language != "ja":
            raise DomainError(
                422,
                "audio_reference",
                "Japanese transcript comparison requires a Japanese reference phrase.",
            )
        target = authored_text(db, body)
        provider = get_settings(db).stt
        providers.require_enabled(config, provider, "stt")
        try:
            text = providers.transcribe(provider, body.audio_base64)
        except providers.PROVIDER_ERRORS as error:
            raise providers.provider_failure("stt", error) from error
        policy = Policy(spacing="ignore")
        return {
            "text": text,
            "target": target,
            "agrees": normalize_text(text, policy) == normalize_text(target, policy),
            "label": (
                "Transcript comparison only. Recognition may be wrong; this does not assess "
                "phonemes, pronunciation or pitch accent. Recording is not retained by Trilingo."
            ),
        }

    @app.post("/api/v1/scenarios/practice", response_model=scenario_practice.ScenarioOut)
    def scenario(body: scenario_practice.ScenarioRequest, db: DB) -> dict:
        return scenario_practice.practice(db, config, body)

    @app.post("/api/v1/explanations", response_model=ExplanationOut)
    def explanation(body: ExplanationRequest, db: DB) -> dict:
        row = _session(db, body.session_id)
        if body.exercise_id not in row.exercise_ids:
            raise DomainError(404, "exercise_missing", "Choose an exercise in this session.")
        evidence = row.evidence[body.exercise_id]
        if not (evidence["responses"] or evidence["revealed"]):
            raise DomainError(
                409,
                "explanation_reveal",
                "Check an answer or choose Reveal first. Assistance remains freely available.",
            )
        exercise = exercise_map(_content(db, row))[body.exercise_id]
        provider = get_settings(db).ai
        result = {
            "authored": exercise.explanation,
            "generated": None,
            "status": "Authored fallback · AI disabled",
        }
        if (
            not config.ai_enabled
            or not provider.enabled
            or provider.provider not in {"lm-studio", "openai-compatible"}
        ):
            return result
        try:
            result["generated"] = providers.explain(provider, exercise.model_dump_json())
            result["status"] = "Generated explanation · advisory and unverified"
        except providers.PROVIDER_ERRORS as error:
            providers.provider_failure("ai", error)
            result["status"] = "Authored fallback · local AI unavailable or incompatible"
        return result
