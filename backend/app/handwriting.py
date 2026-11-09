"""Bounded local drawing practice; geometric feedback is never handwriting recognition."""

import hashlib
import json
import logging
import math
from uuid import uuid4

from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import ROOT
from app.content_extensions import CharacterEntry
from app.content_schema import CourseContent
from app.learning import PRACTICE_XP, complete_practice_activity, now_utc, study_transaction
from app.services import DomainError, current_content
from app.writing import receipt, record
from app.writing_models import DrawingSample
from app.writing_schemas import HandwritingCommit, HandwritingOut, StrokeGuide

logger = logging.getLogger("trilingo")


def character(content: CourseContent, character_id: str, preview: bool) -> CharacterEntry:
    entry = next((item for item in content.characters if item.id == character_id), None)
    if entry is None or (entry.status != "published" and not preview):
        raise DomainError(
            404, "writing_character", "Choose an available character or enable draft practice."
        )
    return entry


def load_guide(content: CourseContent, character_id: str) -> StrokeGuide | None:
    entry = next((item for item in content.characters if item.id == character_id), None)
    asset = next(
        (item for item in content.assets if entry and item.id == entry.stroke_asset_id), None
    )
    if asset is None or asset.kind != "stroke":
        return None
    directory = (ROOT / "content/courses" / content.language).resolve()
    base = (ROOT / "content/courses").resolve()
    resolved = (directory / asset.path).resolve()
    if not directory.is_relative_to(base) or not resolved.is_relative_to(directory):
        logger.error("Stroke asset path rejected: %s", asset.id)
        return None
    try:
        raw = resolved.read_bytes()
        if asset.sha256 and hashlib.sha256(raw).hexdigest() != asset.sha256:
            raise ValueError("Asset digest differs from versioned manifest")
        guide = StrokeGuide.model_validate(json.loads(raw))
        if (
            guide.id != asset.id
            or guide.character_id != character_id
            or guide.license_id != asset.license_id
        ):
            raise ValueError("Stroke asset identity/license does not match its manifest")
        return guide
    except (OSError, ValueError, ValidationError) as error:
        logger.warning("Stroke guide unavailable for %s: %s", character_id, error)
        return None


def guide_view(db: Session, course_id: str, character_id: str, preview: bool) -> dict:
    _, content = current_content(db, course_id)
    entry = character(content, character_id, preview)
    guide = load_guide(content, character_id)
    license = next(
        (item.model_dump() for item in content.licenses if guide and item.id == guide.license_id),
        None,
    )
    return {
        "character": entry.model_dump(),
        "content_version": content.version,
        "guide": guide.model_dump() if guide else None,
        "license": license,
        "message": "Draft schematic: Japanese stroke review pending."
        if guide and guide.status == "draft"
        else "Stroke guide ready."
        if guide
        else (
            "No usable stroke guide. Freehand self-check, typing and composition remain available."
        ),
    }


def _distance(x: float, y: float, a: tuple[float, float], b: tuple[float, float]) -> float:
    dx, dy = b[0] - a[0], b[1] - a[1]
    fraction = (
        max(0.0, min(1.0, ((x - a[0]) * dx + (y - a[1]) * dy) / (dx * dx + dy * dy)))
        if dx or dy
        else 0.0
    )
    return math.hypot(x - (a[0] + fraction * dx), y - (a[1] + fraction * dy))


def trace_feedback(body: HandwritingCommit, guide: StrokeGuide) -> str:
    near = total = starts = 0
    for index, stroke in enumerate(body.strokes):
        total += len(stroke)
        if index >= len(guide.strokes):
            continue
        path = guide.strokes[index].points
        starts += math.hypot(stroke[0].x - path[0].x, stroke[0].y - path[0].y) <= 0.12
        segments = [((a.x, a.y), (b.x, b.y)) for a, b in zip(path, path[1:])]
        near += sum(
            min(_distance(point.x, point.y, a, b) for a, b in segments) <= 0.08 for point in stroke
        )
    return (
        f"Guided tracing feedback: {len(body.strokes)} strokes drawn; "
        f"template has {len(guide.strokes)}. "
        f"{starts} stroke starts near the matching template start; "
        f"{round(100 * near / total)}% of sampled points near its paths. "
        "This describes geometry against a draft template, "
        "not handwriting recognition or calligraphy quality."
    )


def commit(db: Session, course_id: str, body: HandwritingCommit) -> tuple[dict, int]:
    request = {"action": "handwriting", "course_id": course_id, **body.model_dump()}
    safe_request = {**request, "strokes": []}
    safe_request["stroke_digest"] = hashlib.sha256(
        json.dumps(request["strokes"], sort_keys=True).encode()
    ).hexdigest()
    with study_transaction(db):
        prior = receipt(db, body.request_id, safe_request)
        if prior:
            return prior
        version, content = current_content(db, course_id)
        entry = character(content, body.character_id, body.preview_draft)
        guide = load_guide(content, entry.id)
        if body.mode in {"guided_trace", "accessible_sequence"} and guide is None:
            raise DomainError(
                409, "stroke_guide", "Guide unavailable. Choose freehand self-check or typing."
            )
        if body.mode == "freehand_self_check" and not body.reference_revealed:
            raise DomainError(
                422, "self_check", "Reveal the reference before recording a freehand self-check."
            )
        if body.mode == "accessible_sequence":
            assert guide is not None
            expected = list(range(1, len(guide.strokes) + 1))
            if sorted(body.sequence) != expected:
                raise DomainError(
                    422, "stroke_sequence", "Select every numbered demonstration stroke once."
                )
            feedback = (
                "Selected sequence matches the demonstration."
                if body.sequence == expected
                else "Compare your selected order with the numbered demonstration."
            )
            feedback += " This keyboard activity does not measure handwriting."
        elif body.mode == "guided_trace":
            assert guide is not None
            feedback = trace_feedback(body, guide)
        else:
            feedback = (
                "Freehand self-check recorded from your own comparison. "
                "Handwriting quality was not assessed."
            )
        sample_id = None
        if body.keep_sample:
            sample_id = str(uuid4())
            db.add(
                DrawingSample(
                    id=sample_id,
                    profile_id="local",
                    course_id=course_id,
                    course_version_id=version.id,
                    character_id=entry.id,
                    mode=body.mode,
                    strokes=[[point.model_dump() for point in stroke] for stroke in body.strokes],
                    created_at=now_utc().isoformat(),
                )
            )
        session = complete_practice_activity(
            db,
            course_id,
            version.id,
            "handwriting",
            entry.id,
            "handwriting",
            "Character formation practice",
            {
                "preview_draft": body.preview_draft,
                "evidence_mode": body.mode,
                "self_rating": body.self_rating,
                "reference_revealed": body.reference_revealed or body.mode != "freehand_self_check",
                "sample_id": sample_id,
                "objective_correctness": None,
            },
        )
        output = HandwritingOut(
            id=session.id,
            character_id=entry.id,
            mode=body.mode,
            self_rating=body.self_rating,
            feedback=feedback,
            xp_awarded=PRACTICE_XP,
            sample_id=sample_id,
        ).model_dump()
        # Never retain raw strokes in an idempotency receipt when the learner did not keep a sample.
        return record(db, body.request_id, safe_request, output)


def list_samples(db: Session, offset: int = 0, limit: int = 20) -> list[dict]:
    rows = db.scalars(
        select(DrawingSample)
        .where(DrawingSample.profile_id == "local")
        .order_by(DrawingSample.created_at.desc(), DrawingSample.id)
        .offset(offset)
        .limit(limit)
    ).all()
    return [
        {key: getattr(row, key) for key in ("id", "character_id", "mode", "strokes", "created_at")}
        for row in rows
    ]


def delete_sample(db: Session, sample_id: str) -> dict:
    with study_transaction(db):
        row = db.get(DrawingSample, sample_id)
        if row is not None:
            if row.profile_id != "local":
                raise DomainError(404, "drawing_sample", "Sample not found.")
            db.delete(row)
    return {"deleted": True}
