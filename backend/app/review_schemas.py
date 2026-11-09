from typing import Literal

from pydantic import Field

from app.learning_schemas import RequestId
from app.public_schemas import PublicAudioCue
from app.schemas import StrictModel


class CardAdd(StrictModel):
    item_kind: Literal["word", "exercise"] = "word"
    item_id: str = Field(min_length=1, max_length=100)
    direction: Literal["reading", "meaning", "typing", "recognition", "listening", "speaking"] = (
        "meaning"
    )


class RecallStart(StrictModel):
    request_id: RequestId


class RatingRequest(StrictModel):
    recall_session_id: str | None = Field(default=None, max_length=100)
    request_id: RequestId
    expected_revision: int = Field(ge=0)
    rating: Literal["Again", "Hard", "Good", "Easy"]


class CardOut(StrictModel):
    audio_cues: list[PublicAudioCue] = []
    supports_recording: bool = False
    reference_text: str | None = None
    content_version: str = ""
    item_kind: Literal["word", "exercise"] = "word"
    id: str
    item_id: str
    direction: str
    prompt: str
    answer: str
    due: str | None
    revision: int
    scheduled: bool
    state: dict
    scheduler: dict


class CardsOut(StrictModel):
    cards: list[CardOut]
    has_more: bool
    offset: int
    total: int


class CollectionRecall(StrictModel):
    direction: Literal["reading", "meaning", "typing", "listening", "speaking"] = "meaning"
    item_id: str | None = Field(default=None, min_length=1, max_length=100)


class QuestRequest(StrictModel):
    request_id: RequestId
    kind: Literal["sessions", "reviews", "writing", "listening", "speaking"] = "sessions"
    target: int = Field(default=3, ge=1)


class QuestFallback(StrictModel):
    request_id: RequestId
    expected_revision: int = Field(ge=0)


class QuestOut(StrictModel):
    revision: int = 0
    original_kind: str = "sessions"
    definition_history: list[dict] = []
    id: str
    kind: str
    target: int
    progress: int
    completed_at: str | None
    source_ids: list[str]


class WeeklyOut(StrictModel):
    week: str
    xp: int


class BadgeOut(StrictModel):
    id: str
    earned_at: str
    details: dict


class CalendarDay(StrictModel):
    day: str
    xp: int
    sessions: int


class TimingRecord(StrictModel):
    id: str
    source_id: str
    title: str
    kind: str
    elapsed_seconds: float
    completed_at: str
    assisted: int
    skipped: int
    source_kind: str = ""
    mode: str = "supported"
    direction: str | None = None
    rating: Literal["Again", "Hard", "Good", "Easy"] | None = None
    paused_seconds: float | None = None


class TimingHistory(StrictModel):
    records: list[TimingRecord]
    total: int
    next_cursor: str | None
    previous_cursor: str | None


class SkillSummary(StrictModel):
    speech_attempts: int = 0
    transcript_matches: int = 0
    typed_fallbacks: int = 0
    objective_checks: int
    initial_correct: int
    assisted: int
    skipped: int
    self_rated_reviews: int


class WorkflowSummary(StrictModel):
    source_kind: str
    kind: str
    evidence: str
    draft: bool
    self_reviewed: bool | None
    count: int


class StageCoverage(StrictModel):
    course_id: str
    content_version: str
    stage: str
    title: str
    release: str
    status: str
    word_target: int
    kanji_target: int
    published_word_records: int
    published_kanji: int
    independent_review: str


class PersonalOut(StrictModel):
    skill_evidence: dict[str, SkillSummary] = {}
    completed_workflows: list[WorkflowSummary] = []
    curriculum_coverage: list[StageCoverage] = []
    activity_calendar: list[CalendarDay] = []
    timing_records: list[TimingRecord] = []
    objective_checks: int
    initial_correct: int
    assisted_prompts: int
    skipped_prompts: int
    review_directions: dict[str, int]
    badges: list[BadgeOut]
    weeks: list[WeeklyOut]
    best_week_xp: int
    review_count: int
    quests_completed: int
    monthly_badges: list[str]
    level: int
    provenance: str
