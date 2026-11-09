"""Validated contracts for content introduced by later renderers; not runnable modes yet."""

import unicodedata
from pathlib import PurePosixPath
from typing import Literal

from pydantic import Field, field_validator, model_validator

from app.schemas import StrictModel


class Segment(StrictModel):
    surface: str = Field(min_length=1)
    reading: str | None = Field(default=None, min_length=1)
    vocabulary_id: str | None = None


class ContentAsset(StrictModel):
    id: str
    path: str = Field(min_length=1)
    license_id: str
    kind: Literal["stroke", "audio", "illustration"]
    sha256: str | None = Field(default=None, pattern=r"^[0-9a-f]{64}$")

    @field_validator("path")
    @classmethod
    def relative_asset(cls, value: str) -> str:
        p = PurePosixPath(value)
        if p.is_absolute() or ".." in p.parts or ":" in value or "\\" in value:
            raise ValueError("Asset path must stay relative to the content directory")
        return value


class CharacterEntry(StrictModel):
    id: str
    surface: str = Field(min_length=1, max_length=3)
    script: Literal["hiragana", "katakana", "kanji"]
    contextual_readings: list[str] = Field(min_length=1)
    form: Literal["basic", "voiced", "semi_voiced", "combination", "small", "mark", "kanji"] = (
        "basic"
    )
    romaji: str | None = None
    meaning: str | None = None
    notes: str = ""
    vocabulary_ids: list[str] = []
    practice_exercise_ids: list[str] = []
    components: list[str] = []
    stage: str
    concepts: list[str]
    stroke_asset_id: str | None = None
    status: Literal["draft", "reviewed", "published"] = "draft"

    @field_validator("surface")
    @classmethod
    def canonical_surface(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Character surface must be visible")
        return unicodedata.normalize("NFC", value)

    @field_validator("contextual_readings")
    @classmethod
    def visible_readings(cls, value: list[str]) -> list[str]:
        if any(not reading.strip() for reading in value):
            raise ValueError("Character readings must be visible")
        return value

    @model_validator(mode="after")
    def script_and_components(self):
        if self.script == "kanji":
            valid = len(self.surface) == 1 and "\u4e00" <= self.surface <= "\u9fff"
        else:
            low, high = ("\u3041", "\u309f") if self.script == "hiragana" else ("\u30a0", "\u30ff")
            valid = all(low <= char <= high for char in self.surface)
        if not valid:
            raise ValueError("Character surface must match its declared script")
        if self.form == "basic" and len(self.surface) != 1:
            raise ValueError("Basic kana must contain one character")
        if self.form == "combination" and len(self.components) < 2:
            raise ValueError("A combination needs ordered component references")
        return self


class AudioCue(StrictModel):
    id: str = Field(pattern=r"^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,99}$")
    label: str = Field(min_length=1, max_length=80)
    transcript: str = Field(min_length=1, max_length=500)
    pronunciation_override: str | None = Field(default=None, min_length=1, max_length=500)
    language: str = Field(default="ja", pattern=r"^[a-z]{2,3}$")


class GrammarNote(StrictModel):
    unit_ids: list[str] = []
    practice_exercise_ids: list[str] = []
    common_mistakes: list[str] = []
    culture_note: str = ""
    id: str
    title: str
    explanation: str
    examples: list[list[Segment]]
    concepts: list[str]
    register_note: str
    status: Literal["draft", "reviewed", "published"] = "draft"


class ScriptTurn(StrictModel):
    pronunciation_override: str | None = Field(default=None, min_length=1, max_length=500)
    id: str
    speaker: str
    text: list[Segment]
    next_turn_ids: list[str] = []
    response_transitions: dict[str, str] = {}
    exercise_ids: list[str] = []


class Narrative(StrictModel):
    id: str
    kind: Literal["story", "audio_episode", "dialogue", "reading_passage"]
    title: str
    stage: str
    difficulty: int = Field(ge=1, le=5)
    objectives: list[str] = Field(min_length=1)
    turns: list[ScriptTurn] = Field(min_length=1)
    concepts: list[str]
    vocabulary_ids: list[str]
    preparation: list[str] = []
    speaking_exercise_ids: list[str] = []
    recap_exercise_ids: list[str] = []
    transcript_policy: Literal["visible", "deliberate_reveal"] = "visible"
    audio_asset_id: str | None = None
    status: Literal["draft", "reviewed", "published"] = "draft"


class AssessmentBank(StrictModel):
    id: str
    kind: Literal["recap", "placement", "mastery"]
    title: str
    concepts: list[str]
    exercise_ids: list[str] = Field(min_length=1)
    scoring_policy: str
    badge_criteria: str | None = None
    status: Literal["draft", "reviewed", "published"] = "draft"
