"""Reading-library data and learner-selected support, with explicit draft previews."""

from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.content_schema import CourseContent
from app.reading_models import ReadingItem
from app.reading_schemas import ReadingItemOut, ReadingItemPatch
from app.services import DomainError, current_content, local_profile


def item_out(row: ReadingItem) -> dict:
    return ReadingItemOut(
        item_kind=row.item_kind,
        item_id=row.item_id,
        saved=row.saved,
        familiar=row.familiar,
        updated_at=row.updated_at,
    ).model_dump()


def library(db: Session, course_id: str, include_drafts: bool = False) -> dict:
    _, content = current_content(db, course_id)
    local_profile(db)
    characters = [
        entry for entry in content.characters if include_drafts or entry.status == "published"
    ]
    vocabulary = [
        entry for entry in content.vocabulary if include_drafts or entry.status == "published"
    ]
    stories = [
        story
        for story in content.narratives
        if story.kind in {"story", "reading_passage"}
        and (include_drafts or story.status == "published")
    ]
    items = db.scalars(
        select(ReadingItem)
        .where(
            ReadingItem.profile_id == "local",
            ReadingItem.course_id == course_id,
        )
        .order_by(ReadingItem.updated_at.desc(), ReadingItem.item_id)
    ).all()
    first_release = content.stages[0].release
    return {
        "content_version": content.version,
        "characters": [entry.model_dump() for entry in characters],
        "vocabulary": [entry.model_dump() for entry in vocabulary],
        "stories": [
            {
                "id": story.id,
                "title": story.title,
                "kind": story.kind,
                "status": story.status,
                "stage": story.stage,
                "difficulty": story.difficulty,
                "objectives": story.objectives,
                "turn_count": len(story.turns),
                "checkpoint_count": sum(len(turn.exercise_ids) for turn in story.turns),
            }
            for story in stories
        ],
        "items": [item_out(item) for item in items],
        "includes_drafts": include_drafts,
        "inventory": {
            "basic_hiragana": sum(
                entry.script == "hiragana" and entry.form == "basic" for entry in characters
            ),
            "basic_katakana": sum(
                entry.script == "katakana" and entry.form == "basic" for entry in characters
            ),
            "variants": sum(
                entry.script != "kanji" and entry.form != "basic" for entry in characters
            ),
            "published_characters": sum(entry.status == "published" for entry in characters),
            "authored_kanji": sum(entry.script == "kanji" for entry in characters),
            "published_kanji": sum(
                entry.script == "kanji" and entry.status == "published" for entry in characters
            ),
            "target_kanji": sum(
                stage.kanji_target for stage in content.stages if stage.release == first_release
            ),
        },
        "review_note": content.review_note,
        "guides": [
            entry.model_dump()
            for entry in content.concepts
            if entry.id in {key for character in characters for key in character.concepts}
        ],
    }


def _owner(content: CourseContent, kind: str, item_id: str):
    source = (
        content.vocabulary
        if kind == "word"
        else content.grammar_notes
        if kind == "grammar"
        else content.characters
    )
    return next((item for item in source if item.id == item_id), None)


def patch_item(
    db: Session, course_id: str, kind: str, item_id: str, body: ReadingItemPatch
) -> dict:
    # Import lazily so reading and lesson services share one transaction implementation.
    from app.learning import study_transaction

    with study_transaction(db):
        version, content = current_content(db, course_id)
        if kind not in {"word", "character", "grammar"}:
            raise DomainError(422, "item_kind", "Choose a word or character.")
        owner = _owner(content, kind, item_id)
        if owner is None or (owner.status != "published" and not body.preview_draft):
            raise DomainError(
                404,
                "reading_item",
                "This reading item is unavailable. Enable draft preview when appropriate.",
            )
        row = db.get(ReadingItem, ("local", course_id, kind, item_id))
        if row is None:
            row = ReadingItem(
                profile_id="local",
                course_id=course_id,
                item_kind=kind,
                item_id=item_id,
                course_version_id=version.id,
                saved=False,
                familiar=False,
                updated_at=datetime.now(timezone.utc).isoformat(),
            )
            db.add(row)
        for key in body.model_fields_set & {"saved", "familiar"}:
            setattr(row, key, getattr(body, key))
        row.updated_at = datetime.now(timezone.utc).isoformat()
        db.flush()
        return item_out(row)


def available_exercise_ids(content: CourseContent, include_drafts: bool = False) -> set[str]:
    ids = {
        exercise.id
        for unit in content.units
        if include_drafts or unit.status == "published"
        for lesson in unit.lessons
        if include_drafts or lesson.status == "published"
        for exercise in lesson.exercises
    }
    for owner in content.characters + content.vocabulary:
        if include_drafts or owner.status == "published":
            ids.update(owner.practice_exercise_ids)
    for note in content.grammar_notes:
        if include_drafts or note.status == "published":
            ids.update(note.practice_exercise_ids)
    for task in content.writing_tasks:
        if include_drafts or task.status == "published":
            ids.update(task.exercise_ids)
    for story in content.narratives:
        if include_drafts or story.status == "published":
            ids.update(key for turn in story.turns for key in turn.exercise_ids)
            ids.update(story.recap_exercise_ids)
            ids.update(story.speaking_exercise_ids)
    return ids


def practice_source(
    db: Session, content: CourseContent, kind: str, item_id: str, preview_draft: bool
) -> tuple[str, list[str], str]:
    if kind == "character":
        character = _owner(content, "character", item_id)
        if character is None or (character.status != "published" and not preview_draft):
            raise DomainError(
                404, "character_missing", "Choose an available character or enable draft preview."
            )
        return (
            character.script.capitalize() + " character practice",
            character.practice_exercise_ids,
            "practice",
        )
    saved = db.scalars(
        select(ReadingItem)
        .where(
            ReadingItem.profile_id == "local",
            ReadingItem.course_id == content.id,
            ReadingItem.saved.is_(True),
        )
        .order_by(ReadingItem.updated_at.desc(), ReadingItem.item_id)
    ).all()
    available = available_exercise_ids(content, preview_draft)
    ids = []
    for item in saved:
        owner = _owner(content, item.item_kind, item.item_id)
        if owner is not None and (owner.status == "published" or preview_draft):
            ids.extend(
                key
                for key in getattr(owner, "practice_exercise_ids", [])
                if key in available and key not in ids
            )
    if not ids:
        raise DomainError(
            404,
            "no_saved_drills",
            "No related drills for these saved items yet. Choose any available lesson.",
        )
    return "Related practice from saved reading items", ids, "practice"
