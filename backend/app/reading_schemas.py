from typing import Literal

from pydantic import model_validator

from app.content_extensions import CharacterEntry
from app.content_schema import Vocabulary
from app.schemas import StrictModel


class ReadingItemPatch(StrictModel):
    saved: bool | None = None
    familiar: bool | None = None
    preview_draft: bool = False

    @model_validator(mode="after")
    def explicit_flags(self):
        flags = self.model_fields_set & {"saved", "familiar"}
        if not flags or any(getattr(self, key) is None for key in flags):
            raise ValueError("Choose saved or self-reported familiar state using true/false")
        return self


class ReadingItemOut(StrictModel):
    item_kind: Literal["word", "character", "grammar"]
    item_id: str
    saved: bool
    familiar: bool
    evidence: Literal["self_reported"] = "self_reported"
    updated_at: str


class StorySummary(StrictModel):
    id: str
    title: str
    kind: str
    status: str
    stage: str
    difficulty: int
    objectives: list[str]
    turn_count: int
    checkpoint_count: int


class ReadingInventory(StrictModel):
    basic_hiragana: int
    basic_katakana: int
    variants: int
    published_characters: int
    authored_kanji: int
    published_kanji: int
    target_kanji: int


class ReadingLibrary(StrictModel):
    content_version: str
    characters: list[CharacterEntry]
    vocabulary: list[Vocabulary]
    stories: list[StorySummary]
    items: list[ReadingItemOut]
    inventory: ReadingInventory
    includes_drafts: bool
    review_note: str
    guides: list[dict[str, str]]
