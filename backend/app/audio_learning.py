"""Prepare authored listening cues with revision-safe, idempotent evidence."""

import base64
from copy import deepcopy
from uuid import uuid4

from sqlalchemy.orm import Session

from app import learning, providers
from app.audio_models import AudioDelivery
from app.config import Config
from app.schemas import Provider
from app.services import DomainError, get_settings


def prepare(
    db: Session,
    config: Config,
    session_id: str,
    exercise_id: str,
    cue_id: str,
    request_id: str,
    expected_revision: int,
    speed: float,
) -> dict:
    request = {
        "session_id": session_id,
        "exercise_id": exercise_id,
        "cue_id": cue_id,
        "expected_revision": expected_revision,
        "speed": speed,
    }
    prior = db.get(AudioDelivery, request_id)
    if prior is not None:
        if prior.request != request:
            raise DomainError(
                409, "request_conflict", "This audio action ID was used for a different request."
            )
        provider = Provider.model_validate(prior.provider)
        cue = prior.cue
        result = prior.result
        providers.require_enabled(config, get_settings(db).tts, "tts")
    else:
        row = learning._session(db, session_id)
        if row.revision != expected_revision or row.status == "completed":
            raise DomainError(
                409, "stale_revision", "Reload this saved session before preparing audio."
            )
        if exercise_id not in row.exercise_ids:
            raise DomainError(404, "exercise_missing", "Choose a prompt in this session.")
        exercise = learning.exercise_map(learning._content(db, row))[exercise_id]
        reference = next(
            (item for item in getattr(exercise, "audio", []) if item.id == cue_id), None
        )
        if reference is None:
            raise DomainError(404, "audio_reference", "Choose an authored audio cue.")
        cue = reference.model_dump()
        provider = get_settings(db).tts
        providers.require_enabled(config, provider, "tts")
        result = None
    # Network I/O must not hold SQLite's write lock.
    db.commit()
    try:
        data, cached = providers.synthesize(
            provider,
            cue["transcript"],
            speed,
            cache_dir=config.audio_cache_dir,
            pronunciation_override=cue["pronunciation_override"],
            language=cue["language"],
        )
    except providers.PROVIDER_ERRORS as error:
        raise providers.provider_failure("tts", error) from error
    if result is None:
        with learning.study_transaction(db):
            prior = db.get(AudioDelivery, request_id)
            if prior is not None:
                if prior.request != request:
                    raise DomainError(
                        409, "request_conflict", "Audio action conflict. Reload this session."
                    )
                result = prior.result
            else:
                row = learning._session(db, session_id)
                db.refresh(row)
                if row.revision != expected_revision or row.status == "completed":
                    raise DomainError(
                        409,
                        "stale_revision",
                        "Another action was saved. Reload; no listening evidence was added.",
                    )
                evidence = deepcopy(row.evidence)
                item = evidence[exercise_id]
                item["audio_cue_ids"] = list(
                    dict.fromkeys(item.get("audio_cue_ids", []) + [cue_id])
                )
                row.evidence = evidence
                row.revision += 1
                row.next_action_id = str(uuid4())
                result = learning._view(db, row)
                db.add(
                    AudioDelivery(
                        id=request_id,
                        session_id=session_id,
                        request=request,
                        provider=provider.model_dump(),
                        cue=cue,
                        result=result,
                        created_at=learning.now_utc().isoformat(),
                    )
                )
    return {
        "audio_base64": base64.b64encode(data).decode(),
        "mime": "audio/wav",
        "cached": cached,
        "label": "Synthetic reference prepared · Japanese listening review pending",
        "session": result,
    }
