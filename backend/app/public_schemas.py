from typing import Annotated, Literal

from pydantic import Field

from app.content_schema import (
    Choice,
    Concept,
    License,
    Policy,
    Stage,
    Status,
    Vocabulary,
    WritingTask,
)
from app.schemas import StrictModel


class Features(StrictModel):
    lessons: bool = False
    ai: bool = False
    stt: bool = False


class HealthOut(StrictModel):
    status: Literal["ok"]
    database: Literal["ready"]
    schema_version: str
    qa_mode: bool
    features: Features


class CourseSummary(StrictModel):
    id: str
    title: str
    language: str
    teaching_language: str
    description: str
    version: str


class PublicExerciseBase(StrictModel):
    id: str
    prompt: str
    objective: str
    concepts: list[str]
    difficulty: int
    policy: Policy
    skill: str
    preparation: list[str]


class PublicChoice(PublicExerciseBase):
    type: Literal["multiple_choice"]
    choices: list[Choice]


class PublicTranslation(PublicExerciseBase):
    type: Literal["translation"]


class PublicFillBlank(PublicExerciseBase):
    type: Literal["fill_blank"]


class PublicOrdering(PublicExerciseBase):
    type: Literal["sentence_ordering"]
    tokens: list[Choice]


class PublicMatching(PublicExerciseBase):
    type: Literal["matching"]
    left: list[Choice]
    right: list[Choice]


class PublicResponseSelection(PublicChoice):
    type: Literal["response_selection"]


class PublicDialogueCompletion(PublicTranslation):
    type: Literal["dialogue_completion"]


class PublicConstrainedRoleplay(PublicTranslation):
    type: Literal["constrained_roleplay"]


class PublicAudioCue(StrictModel):
    id: str
    label: str


class PublicListeningSelection(PublicChoice):
    type: Literal["listening_selection"]
    audio: list[PublicAudioCue]


class PublicAudioContrast(PublicListeningSelection):
    type: Literal["audio_contrast"]


class PublicDictation(PublicTranslation):
    type: Literal["dictation"]
    audio: list[PublicAudioCue]


class PublicSpeaking(PublicExerciseBase):
    type: Literal["speaking"]
    audio: list[PublicAudioCue]
    reference_text: str


PublicExercise = Annotated[
    PublicChoice
    | PublicTranslation
    | PublicFillBlank
    | PublicOrdering
    | PublicMatching
    | PublicResponseSelection
    | PublicDialogueCompletion
    | PublicConstrainedRoleplay
    | PublicListeningSelection
    | PublicAudioContrast
    | PublicDictation
    | PublicSpeaking,
    Field(discriminator="type"),
]


class LessonMetadata(StrictModel):
    id: str
    title: str
    japanese_title: str
    objective: str
    order: int
    status: Status
    preparation: list[str]


class PublicLesson(LessonMetadata):
    exercises: list[PublicExercise]


class MapLesson(LessonMetadata):
    exercise_count: int
    available: bool
    study_state: Literal["not_started", "visited", "studied", "assisted", "skipped"]


class MapUnit(StrictModel):
    id: str
    title: str
    japanese_title: str
    description: str
    guide: str
    order: int
    stage: str
    status: Status
    lessons: list[MapLesson]


class Inventory(StrictModel):
    published_words: int
    published_phrases: int
    published_kanji: int
    published_lessons: int
    target_words: int
    target_kanji: int
    coverage: str


class CourseMap(StrictModel):
    id: str
    title: str
    version: str
    description: str
    review_note: str
    stages: list[Stage]
    units: list[MapUnit]
    inventory: Inventory


class LibraryOut(StrictModel):
    concepts: list[Concept]
    vocabulary: list[Vocabulary]
    writing_tasks: list[WritingTask]
    licenses: list[License]


class EnrollmentOut(StrictModel):
    course_id: str
    enrolled: bool


class AssistanceOut(StrictModel):
    exercise_id: str
    action: Literal["hint", "reveal"]
    evidence: Literal["assisted"]
    hint: str
    answer: str | list[str] | dict[str, str] | None = None
    explanation: str | None = None
