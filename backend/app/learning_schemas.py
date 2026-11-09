from typing import Annotated, Literal

from pydantic import Field, model_validator

from app.content_extensions import Segment
from app.content_schema import ID
from app.public_schemas import PublicExercise
from app.schemas import StrictModel

RequestId = Annotated[str, Field(pattern=r"^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$")]
Answer = str | list[str] | dict[str, str]


class StartRequest(StrictModel):
    request_id: RequestId
    source_kind: Literal[
        "lesson",
        "assessment",
        "mistakes",
        "character",
        "saved_items",
        "story",
        "story_recap",
        "writing_task",
        "grammar",
        "listening",
        "speaking",
    ] = "lesson"
    source_id: ID
    preview_draft: bool = False
    mode: Literal["supported", "unassisted"] = "supported"


class ActionRequest(StrictModel):
    request_id: RequestId
    expected_revision: int = Field(ge=0)
    action: Literal[
        "answer",
        "audio_text",
        "hint",
        "reveal",
        "skip",
        "continue",
        "pause",
        "resume",
        "visit",
        "support",
        "finish",
        "story_visit",
        "story_continue",
        "show_readings",
        "hide_readings",
        "glossary",
        "timer_start",
        "timer_pause",
        "timer_resume",
        "timer_hide",
        "timer_show",
    ]
    exercise_id: ID | None = None
    answer: Answer | None = None
    turn_id: ID | None = None
    vocabulary_id: ID | None = None

    @model_validator(mode="after")
    def payload_valid(self):
        if self.action == "answer":
            if self.answer is None:
                raise ValueError("Provide an answer to check")
            strings = (
                [self.answer]
                if isinstance(self.answer, str)
                else list(self.answer.values())
                if isinstance(self.answer, dict)
                else self.answer
            )
            if len(strings) > 1000 or any(len(value) > 8192 for value in strings):
                raise ValueError("Answer payload is too large")
        elif self.answer is not None:
            raise ValueError("Only an answer action accepts answer data")
        if self.action in {"answer", "audio_text", "hint", "reveal", "skip", "continue", "visit"}:
            if self.exercise_id is None:
                raise ValueError("Choose an exercise for this action")
        elif self.exercise_id is not None:
            raise ValueError("This session action does not accept an exercise ID")
        if (self.turn_id is not None) != (self.action == "story_visit"):
            raise ValueError("Only story_visit requires a turn ID")
        if (self.vocabulary_id is not None) != (self.action == "glossary"):
            raise ValueError("Only glossary requires a vocabulary ID")
        return self


class ExerciseEvidence(StrictModel):
    speech_reference_delivered: bool = False
    speech_attempts: int = 0
    transcript_matches: int = 0
    last_transcript: str | None = None
    last_transcript_matches: bool | None = None
    typed_fallbacks: int = 0
    audio_cue_ids: list[str] = []
    text_fallback: bool = False
    responses: int = 0
    first_correct: bool | None = None
    first_assisted: bool = False
    last_correct: bool | None = None
    assisted: bool = False
    revealed: bool = False
    skipped: bool = False
    answer: Answer | None = None


class Feedback(StrictModel):
    exercise_id: str
    kind: Literal["correct", "incorrect", "hint", "reveal", "skipped", "recorded"]
    message: str
    explanation: str | None = None
    answer: Answer | None = None


class Recommendation(StrictModel):
    lesson_id: str
    title: str
    reason: str


class StoryTurnOut(StrictModel):
    id: str
    speaker: str
    text: list[Segment]
    next_turn_ids: list[str]
    response_transitions: dict[str, str] = {}
    exercise_ids: list[str]


class StoryGlossary(StrictModel):
    id: str
    surface: str
    reading: str | None = None
    gloss: str | None = None


class StoryOut(StrictModel):
    current: StoryTurnOut
    turns: list[dict[str, str]]
    visited_turn_ids: list[str]
    assisted_turn_ids: list[str]
    reading_aids: bool
    glossary: list[StoryGlossary]
    at_end: bool
    recap_available: bool


class TimerOut(StrictModel):
    visible: bool
    running: bool
    elapsed_seconds: float
    valid: bool


class StudyOut(StrictModel):
    timer: TimerOut | None = None
    id: str
    course_id: str
    content_version: str
    source_kind: str
    source_id: str
    kind: str
    title: str
    status: Literal["active", "paused", "completed"]
    cursor: int
    revision: int
    next_action_id: str
    exercises: list[PublicExercise]
    evidence: dict[str, ExerciseEvidence]
    preview_draft: bool
    mode: Literal["supported", "unassisted"]
    feedback: Feedback | None = None
    xp_awarded: int
    completed_at: str | None
    created_at: str
    story: StoryOut | None = None
    recommendation: Recommendation | None = None
    initial_correct: int
    assessed_count: int
    concept_coverage: dict[str, int]


class SessionSummary(StrictModel):
    id: str
    course_id: str
    source_id: str
    title: str
    status: str
    kind: str
    created_at: str
    completed_at: str | None


class ProgressOut(StrictModel):
    total_xp: int
    today_xp: int
    current_streak: int
    longest_streak: int
    activity_dates: list[str]
    daily_goal: int | None
    show_goal: bool
    goal_met: bool
    sessions: list[SessionSummary]
    offset: int
    has_more: bool


class MistakeOut(StrictModel):
    concepts: list[str]
    exercise_id: str
    prompt: str
    skill: str
    occurrences: int
    updated_at: str


class AssessmentOut(StrictModel):
    id: str
    title: str
    kind: str
    status: str
    exercise_count: int
    scoring_policy: str
