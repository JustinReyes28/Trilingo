"""Explicit local STT submissions saved through the shared study event transaction."""

import base64
import hashlib
from copy import deepcopy
from uuid import uuid4

from sqlalchemy.orm import Session

from app import learning, providers
from app.config import Config
from app.grading import normalize_text
from app.learning_models import StudySession
from app.services import DomainError, get_settings

TRANSCRIPT_LABEL = (
    "Transcript comparison only. Recognition may be wrong; this does not assess "
    "phonemes, pronunciation or pitch accent. Trilingo saves the transcript and "
    "comparison, never the recording. The configured STT service has its own retention settings."
)


def _ready(db: Session, session_id: str, exercise_id: str, revision: int, key: str) -> StudySession:
    row = learning._session(db, session_id)
    if row.revision != revision or row.next_action_id != key:
        raise DomainError(
            409,
            "stale_revision",
            "Another action was saved. Reload; your recording stays in this tab.",
        )
    if row.status == "completed":
        raise DomainError(409, "completed", "Start a new speaking replay to keep practicing.")
    if exercise_id not in row.exercise_ids:
        raise DomainError(404, "exercise_missing", "Choose a prompt in this session.")
    exercise = learning.exercise_map(learning._content(db, row))[exercise_id]
    if exercise.type != "speaking":
        raise DomainError(
            422, "speaking_prompt", "Recording feedback is available for authored speaking prompts."
        )
    return row


def submit(
    db: Session,
    config: Config,
    session_id: str,
    exercise_id: str,
    request_id: str,
    expected_revision: int,
    encoded: str,
) -> dict:
    try:
        audio = base64.b64decode(encoded, validate=True)
        providers.validate_wav(audio, maximum_seconds=20)
    except ValueError as error:
        raise DomainError(422, "recording_invalid", str(error)) from error
    request = {
        "session_id": session_id,
        "exercise_id": exercise_id,
        "action": "speech",
        "request_id": request_id,
        "expected_revision": expected_revision,
        "audio_sha256": hashlib.sha256(audio).hexdigest(),
    }
    prior = learning._receipt(db, request_id, request)
    if prior is not None:
        return prior
    row = _ready(db, session_id, exercise_id, expected_revision, request_id)
    exercise = learning.exercise_map(learning._content(db, row))[exercise_id]
    target, policy = exercise.audio[0].transcript, exercise.policy
    provider = get_settings(db).stt
    providers.require_enabled(config, provider, "stt")
    db.commit()  # Never hold a write transaction while waiting for a local provider.
    try:
        transcript = providers.transcribe(provider, encoded)
    except providers.PROVIDER_ERRORS as error:
        raise providers.provider_failure("stt", error) from error
    # Validate even custom adapters; an empty/malformed result is never a saved speech attempt.
    if not isinstance(transcript, str) or not transcript.strip() or len(transcript) > 4000:
        raise DomainError(
            503,
            "provider_unavailable",
            "No usable transcript returned. Retry or use typed practice.",
        )
    transcript = transcript.strip()
    matches = normalize_text(transcript, policy) == normalize_text(target, policy)
    with learning.study_transaction(db):
        prior = learning._receipt(db, request_id, request)
        if prior is not None:
            return prior
        row = learning._session(db, session_id)
        db.refresh(row)
        _ready(db, session_id, exercise_id, expected_revision, request_id)
        if get_settings(db).stt != provider:
            raise DomainError(
                409,
                "provider_changed",
                "STT settings changed. Reload and explicitly resend if useful.",
            )
        evidence = deepcopy(row.evidence)
        item = evidence[exercise_id]
        item.update(
            responses=item["responses"] + 1,
            speech_attempts=item.get("speech_attempts", 0) + 1,
            speech_reference_delivered=item.get("speech_reference_delivered", False)
            or exercise.audio[0].id in item.get("audio_cue_ids", []),
            transcript_matches=item.get("transcript_matches", 0) + int(matches),
            last_transcript=transcript,
            last_transcript_matches=matches,
        )
        row.evidence = evidence
        metadata = deepcopy(row.metadata_json)
        metadata["feedback"] = {
            "exercise_id": exercise_id,
            "kind": "recorded",
            "message": "Transcript agrees with the reference text."
            if matches
            else "Transcript differs from the reference. Check recognition or retry freely.",
            "explanation": TRANSCRIPT_LABEL,
        }
        row.metadata_json = metadata
        row.status = "active"
        row.cursor = row.exercise_ids.index(exercise_id)
        row.revision += 1
        row.next_action_id = str(uuid4())
        db.flush()
        return learning._record(db, row, request_id, request)
