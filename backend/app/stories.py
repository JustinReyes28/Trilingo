"""Original narrative navigation using shared study sessions and evidence."""

from copy import deepcopy

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.content_extensions import Narrative
from app.content_schema import CourseContent
from app.learning_models import StudySession
from app.learning_schemas import ActionRequest, StartRequest
from app.reading_models import ReadingItem
from app.services import DomainError, get_settings

STORY_ACTIONS = {"story_visit", "story_continue", "show_readings", "hide_readings", "glossary"}


def source(content: CourseContent, story_id: str, preview: bool) -> Narrative:
    story = next((entry for entry in content.narratives if entry.id == story_id), None)
    if (
        story is None
        or story.kind not in {"story", "reading_passage", "dialogue", "audio_episode"}
        or (story.status != "published" and not preview)
    ):
        raise DomainError(
            404, "story_missing", "Choose an available story or enable draft preview."
        )
    return story


def start_state(db: Session, content: CourseContent, body: StartRequest) -> dict:
    story = source(content, body.source_id, body.preview_draft)
    settings = get_settings(db)
    familiar = db.scalars(
        select(ReadingItem.item_id).where(
            ReadingItem.profile_id == "local",
            ReadingItem.course_id == content.id,
            ReadingItem.item_kind == "word",
            ReadingItem.familiar.is_(True),
        )
    ).all()
    return {
        "turn_id": story.turns[0].id,
        "visited": [story.turns[0].id],
        "assisted": [],
        "glossary": [],
        "at_end": False,
        "reading_mode": settings.furigana if body.mode == "supported" else "hidden",
        "familiar": list(familiar),
    }


def _reading_visible(segment: dict, state: dict) -> bool:
    return bool(
        segment.get("reading")
        and state["reading_mode"] != "hidden"
        and (
            state["reading_mode"] == "always"
            or segment.get("vocabulary_id") not in state["familiar"]
        )
    )


def note_aids(content: CourseContent, row: StudySession, metadata: dict) -> None:
    story = source(content, row.source_id, metadata["preview_draft"])
    state = metadata["story"]
    turn = next(entry for entry in story.turns if entry.id == state["turn_id"])
    if state["glossary"] or any(
        _reading_visible(segment.model_dump(), state) for segment in turn.text
    ):
        if turn.id not in state["assisted"]:
            state["assisted"].append(turn.id)
    if turn.id in state["assisted"]:
        evidence = deepcopy(row.evidence)
        for key in turn.exercise_ids:
            evidence[key]["assisted"] = True
        row.evidence = evidence


def view(content: CourseContent, row: StudySession) -> dict | None:
    state = row.metadata_json.get("story")
    if state is None:
        return None
    story = source(content, row.source_id, row.metadata_json["preview_draft"])
    turn = next(entry for entry in story.turns if entry.id == state["turn_id"])
    text = []
    for segment in turn.text:
        data = segment.model_dump()
        if not _reading_visible(data, state):
            data["reading"] = None
        text.append(data)
    return {
        "current": {**turn.model_dump(exclude={"pronunciation_override"}), "text": text},
        "turns": [{"id": entry.id, "speaker": entry.speaker} for entry in story.turns],
        "visited_turn_ids": state["visited"],
        "assisted_turn_ids": state["assisted"],
        "reading_aids": state["reading_mode"] != "hidden",
        "at_end": state["at_end"],
        "recap_available": bool(story.recap_exercise_ids),
        "glossary": [
            {
                "id": word.id,
                "surface": word.surface,
                "reading": word.reading if word.id in state["glossary"] else None,
                "gloss": word.gloss if word.id in state["glossary"] else None,
            }
            for word in content.vocabulary
            if word.id in story.vocabulary_ids
        ],
    }


def act(content: CourseContent, row: StudySession, body: ActionRequest, metadata: dict) -> None:
    if row.source_kind != "story" or "story" not in metadata:
        raise DomainError(422, "story_action", "This action is only available in a story session.")
    story = source(content, row.source_id, metadata["preview_draft"])
    state = metadata["story"]
    turn = next(entry for entry in story.turns if entry.id == state["turn_id"])
    target = None
    if body.action == "story_visit":
        target = next((entry for entry in story.turns if entry.id == body.turn_id), None)
        if target is None:
            raise DomainError(404, "story_turn", "Choose a turn in this story.")
    elif body.action == "story_continue":
        evidence = deepcopy(row.evidence)
        for key in turn.exercise_ids:
            if not (evidence[key]["responses"] or evidence[key]["revealed"]):
                evidence[key]["skipped"] = True
        row.evidence = evidence
        answer = (
            row.evidence.get(turn.exercise_ids[0], {}).get("answer") if turn.exercise_ids else None
        )
        next_id = turn.response_transitions.get(answer) if isinstance(answer, str) else None
        next_id = next_id or (turn.next_turn_ids[0] if turn.next_turn_ids else None)
        target = next((entry for entry in story.turns if entry.id == next_id), None)
        state["at_end"] = target is None
    elif body.action in {"show_readings", "hide_readings"}:
        state["reading_mode"] = "always" if body.action == "show_readings" else "hidden"
        if body.action == "show_readings":
            metadata["mode"] = "supported"
    elif body.action == "glossary":
        metadata["mode"] = "supported"
        if body.vocabulary_id not in story.vocabulary_ids:
            raise DomainError(404, "story_word", "Choose a word in this story's glossary.")
        if body.vocabulary_id not in state["glossary"]:
            state["glossary"].append(body.vocabulary_id)
        if turn.id not in state["assisted"]:
            state["assisted"].append(turn.id)
    if target:
        state["turn_id"] = target.id
        state["at_end"] = False
        if target.id not in state["visited"]:
            state["visited"].append(target.id)
        row.cursor = (
            row.exercise_ids.index(target.exercise_ids[0])
            if target.exercise_ids
            else len(row.exercise_ids)
        )
    note_aids(content, row, metadata)
    metadata["feedback"] = None
