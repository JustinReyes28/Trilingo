from typing import Annotated, Literal
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from pydantic import BaseModel, ConfigDict, Field, field_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid", strict=True, serialize_by_alias=True, populate_by_name=True
    )


def timezone_name(value: str) -> str:
    try:
        ZoneInfo(value)
    except (ZoneInfoNotFoundError, ValueError) as error:
        raise ValueError("Choose a valid IANA timezone, for example Asia/Singapore") from error
    return value


class ProfileOut(StrictModel):
    id: str
    name: str
    timezone: str


class ProfilePatch(StrictModel):
    name: str | None = Field(default=None, min_length=1, max_length=60)
    timezone: str | None = None

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, value: str | None) -> str | None:
        if value is not None and not value.strip():
            raise ValueError("Name cannot be blank")
        return value.strip() if value else value

    @field_validator("timezone")
    @classmethod
    def validate_timezone(cls, value: str | None) -> str | None:
        return timezone_name(value) if value else value


class Settings(StrictModel):
    daily_goal: int | None = Field(default=20, ge=1)
    show_goal: bool = True
    furigana: Literal["always", "unfamiliar", "hidden"] = "always"
    romaji: bool = True
    reduced_motion: bool = False
    sound: bool = False
    show_statistics: bool = True
    practice_batch: int = Field(default=10, ge=1)
    interests: list[Annotated[str, Field(min_length=1, max_length=100)]] = Field(
        default_factory=list, max_length=20
    )
    preferred_focus: Literal["mixed", "reading", "typing", "meaning"] = "mixed"
    accent: Literal["path", "plum"] = "path"
    show_quests: bool = True
    monthly_quest_target: int = Field(default=20, ge=1)
    show_timer: bool = False
    show_reminder: bool = False
    retention: float = Field(default=0.9, ge=0.7, le=0.97)


class SettingsPatch(StrictModel):
    interests: list[str] | None = Field(default=None, max_length=20)
    preferred_focus: Literal["mixed", "reading", "typing", "meaning"] | None = None
    accent: Literal["path", "plum"] | None = None
    show_quests: bool | None = None
    monthly_quest_target: int | None = Field(default=None, ge=1)
    show_timer: bool | None = None
    show_reminder: bool | None = None
    retention: float | None = Field(default=None, ge=0.7, le=0.97)
    daily_goal: int | None = Field(default=None, ge=1)
    show_goal: bool | None = None
    furigana: Literal["always", "unfamiliar", "hidden"] | None = None
    romaji: bool | None = None
    reduced_motion: bool | None = None
    sound: bool | None = None
    show_statistics: bool | None = None
    practice_batch: int | None = Field(default=None, ge=1)

    @field_validator(
        "interests",
        "preferred_focus",
        "accent",
        "show_timer",
        "show_reminder",
        "retention",
        "show_quests",
        "monthly_quest_target",
        "show_goal",
        "furigana",
        "romaji",
        "reduced_motion",
        "sound",
        "show_statistics",
        "practice_batch",
    )
    @classmethod
    def no_explicit_null(cls, value):
        if value is None:
            raise ValueError("This setting cannot be null")
        return value
