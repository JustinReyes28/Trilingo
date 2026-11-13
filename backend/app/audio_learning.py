"""Prepare authored listening cues with revision-safe, idempotent evidence."""

import base64
from copy import deepcopy
from uuid import uuid4

from sqlalchemy.orm import Session

from app import audio_pack, learning
from app.audio_models import AudioDelivery
from app.config import Config
from app.services import DomainError


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
    row = learning._session(db, session_id)
    content = learning._content(db, row)
    course_id = content.id
    if prior is not None:
        if prior.request != request:
            raise DomainError(
                409, "request_conflict", "This audio action ID was used for a different request."
            )
        cue = prior.cue
        result = prior.result
    else:
        if row.revision != expected_revision or row.status == "completed":
            raise DomainError(
                409, "stale_revision", "Reload this saved session before preparing audio."
            )
        if exercise_id not in row.exercise_ids:
            raise DomainError(404, "exercise_missing", "Choose a prompt in this session.")
        exercise = learning.exercise_map(content)[exercise_id]
        reference = next(
            (item for item in getattr(exercise, "audio", []) if item.id == cue_id), None
        )
        if reference is None:
            raise DomainError(404, "audio_reference", "Choose an authored audio cue.")
        cue = reference.model_dump()
        result = None
    clip = audio_pack.lookup(
        config,
        course_id,
        cue["transcript"],
        cue["language"],
        cue["pronunciation_override"],
        preferred_version=content.version,
    )
    if clip is None:
        raise DomainError(
            503,
            "audio_unavailable",
            "Bundled reference audio is unavailable for this cue. Use the text alternative.",
        )
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
                        provider={"source": "pack", "course_version": clip.course_version},
                        cue=cue,
                        result=result,
                        created_at=learning.now_utc().isoformat(),
                    )
                )
    return {
        "audio_base64": base64.b64encode(clip.data).decode(),
        "mime": clip.mime,
        "cached": True,
        "source": "pack",
        "label": audio_pack.label(clip, cue["language"]),
        "session": result,
    }
