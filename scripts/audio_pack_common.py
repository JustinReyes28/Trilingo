"""Shared authored-content extraction for the audio pack build/check scripts."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))

from app import audio_pack  # noqa: E402
from app.content_schema import CourseContent  # noqa: E402


def _add(
    items: dict[str, dict],
    kind: str,
    item_id: str,
    language: str,
    text: str,
    override: str | None,
    required: bool,
    voice_ja: str,
    voice_en: str,
    model: str,
    cue_id: str | None = None,
    turn_id: str | None = None,
) -> None:
    value = text
    if not value.strip():
        return
    if len(value) > 500:
        raise ValueError(f"{item_id}: audio text exceeds the 500-character pack limit")
    voice = voice_ja if language == "ja" else voice_en
    key = audio_pack.pack_key(value, language, voice, model, override)
    existing = items.get(key)
    if existing is not None:
        existing["required"] = existing["required"] or required
        return
    items[key] = {
        "key": key,
        "kind": kind,
        "item_id": item_id,
        "cue_id": cue_id,
        "turn_id": turn_id,
        "language": language,
        "text": value,
        "pronunciation_override": override,
        "required": required,
    }


def _required_practice_exercise_ids(content: CourseContent) -> set[str]:
    required: set[str] = set()
    for story in content.narratives:
        if story.status == "published":
            required.update(story.speaking_exercise_ids)
            required.update(story.recap_exercise_ids)
            for turn in story.turns:
                required.update(turn.exercise_ids)
    for note in content.grammar_notes:
        if note.status == "published":
            required.update(note.practice_exercise_ids)
    for entry in [*content.characters, *content.vocabulary]:
        if entry.status == "published":
            required.update(entry.practice_exercise_ids)
    for item in [*content.writing_tasks, *content.assessment_banks]:
        if item.status == "published":
            required.update(item.exercise_ids)
    return required


def speakable_items(
    content: CourseContent, voice_ja: str, voice_en: str, model: str
) -> dict[str, dict]:
    """Return one entry per unique synthesis key, with a required flag for release checks."""
    items: dict[str, dict] = {}
    for word in content.vocabulary:
        required = word.status == "published"
        _add(
            items,
            "word",
            word.id,
            "ja",
            word.surface,
            word.pronunciation_override,
            required,
            voice_ja,
            voice_en,
            model,
        )
        _add(
            items, "gloss", word.id, "en", word.gloss, None, required, voice_ja, voice_en, model
        )
    for unit in content.units:
        for lesson in unit.lessons:
            required = lesson.status == unit.status == "published"
            for exercise in lesson.exercises:
                for cue in getattr(exercise, "audio", []):
                    _add(
                        items,
                        "cue",
                        exercise.id,
                        cue.language,
                        cue.transcript,
                        cue.pronunciation_override,
                        required,
                        voice_ja,
                        voice_en,
                        model,
                        cue_id=cue.id,
                    )
    required_practice_ids = _required_practice_exercise_ids(content)
    for exercise in content.practice_exercises:
        required = exercise.id in required_practice_ids
        for cue in getattr(exercise, "audio", []):
            _add(
                items,
                "cue",
                exercise.id,
                cue.language,
                cue.transcript,
                cue.pronunciation_override,
                required,
                voice_ja,
                voice_en,
                model,
                cue_id=cue.id,
            )
    for story in content.narratives:
        required = story.status == "published"
        for turn in story.turns:
            _add(
                items,
                "turn",
                story.id,
                "ja",
                "".join(segment.surface for segment in turn.text),
                turn.pronunciation_override,
                required,
                voice_ja,
                voice_en,
                model,
                turn_id=turn.id,
            )
    return items
