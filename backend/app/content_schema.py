import unicodedata
from typing import Annotated, Literal

from pydantic import Field, field_validator, model_validator

from app.content_extensions import (
    AssessmentBank,
    AudioCue,
    CharacterEntry,
    ContentAsset,
    GrammarNote,
    Narrative,
    Segment,
)
from app.schemas import StrictModel

Status = Literal["draft", "reviewed", "published"]
ID = Annotated[str, Field(pattern=r"^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,99}$")]


class Policy(StrictModel):
    script: Literal["any", "hiragana", "katakana", "japanese", "english"] = "any"
    normalization: Literal["NFC", "NFKC"] = "NFC"
    trim: bool = True
    punctuation: Literal["exact", "ignore_terminal"] = "ignore_terminal"
    case_sensitive: bool = False
    strategy: Literal["exact", "choice", "tokens", "pairs"] = "exact"
    spacing: Literal["preserve", "ignore"] = "preserve"
    hint_policy: Literal["always_available"] = "always_available"
    required_distinctions: list[
        Literal["voicing", "kana_size", "vowel_length", "target_script"]
    ] = []


class Choice(StrictModel):
    id: ID
    text: str = Field(min_length=1)

    @field_validator("text")
    @classmethod
    def visible_text(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Choice/token text must be visible")
        return value


class ExerciseBase(StrictModel):
    id: ID
    prompt: str = Field(min_length=1)
    objective: str = Field(min_length=1)
    concepts: list[ID] = Field(min_length=1)
    difficulty: int = Field(ge=1, le=5)
    explanation: str = Field(min_length=1)
    hint: str = Field(min_length=1)
    policy: Policy
    skill: Literal["recognition", "meaning", "typing", "reading", "listening", "speaking"]
    preparation: list[ID] = []
    response_feedback: dict[str, str] = {}


class MultipleChoice(ExerciseBase):
    type: Literal["multiple_choice"]
    choices: list[Choice] = Field(min_length=2)
    answer: ID

    @model_validator(mode="after")
    def choices_valid(self):
        ids = [c.id for c in self.choices]
        labels = [unicodedata.normalize("NFC", c.text.strip()) for c in self.choices]
        if len(set(ids)) != len(ids) or len(set(labels)) != len(labels):
            raise ValueError(f"{self.id}: choice IDs and labels must be unique")
        if self.answer not in ids:
            raise ValueError(f"{self.id}: answer must identify a choice")
        return self


class Translation(ExerciseBase):
    type: Literal["translation"]
    answers: list[str] = Field(min_length=1)


class FillBlank(ExerciseBase):
    type: Literal["fill_blank"]
    answers: list[str] = Field(min_length=1)


class SentenceOrdering(ExerciseBase):
    type: Literal["sentence_ordering"]
    tokens: list[Choice] = Field(min_length=2)
    answer: list[ID] = Field(min_length=2)

    @model_validator(mode="after")
    def token_ids_valid(self):
        ids = [t.id for t in self.tokens]
        if len(set(ids)) != len(ids) or sorted(ids) != sorted(self.answer):
            raise ValueError(f"{self.id}: answer must use each unique token ID once")
        return self


class Matching(ExerciseBase):
    type: Literal["matching"]
    left: list[Choice] = Field(min_length=2)
    right: list[Choice] = Field(min_length=2)
    answer: dict[str, str]

    @model_validator(mode="after")
    def pairs_valid(self):
        left, right = [c.id for c in self.left], [c.id for c in self.right]
        for side in [self.left, self.right]:
            labels = [unicodedata.normalize("NFC", choice.text.strip()) for choice in side]
            if len(set(labels)) != len(labels):
                raise ValueError(f"{self.id}: matching labels must be distinguishable")
        if (
            len(set(left)) != len(left)
            or len(set(right)) != len(right)
            or sorted(self.answer) != sorted(left)
            or sorted(self.answer.values()) != sorted(right)
        ):
            raise ValueError(f"{self.id}: matching requires a one-to-one complete answer")
        return self


class ResponseSelection(MultipleChoice):
    type: Literal["response_selection"]


class DialogueCompletion(Translation):
    type: Literal["dialogue_completion"]


class ListeningSelection(MultipleChoice):
    type: Literal["listening_selection"]
    audio: list[AudioCue] = Field(min_length=1, max_length=1)

    @model_validator(mode="after")
    def audio_valid(self):
        if self.skill != "listening" or len({cue.id for cue in self.audio}) != len(self.audio):
            raise ValueError("Listening drills require listening skill and unique audio cue IDs")
        return self


class AudioContrast(ListeningSelection):
    type: Literal["audio_contrast"]
    audio: list[AudioCue] = Field(min_length=2, max_length=4)


class Dictation(Translation):
    type: Literal["dictation"]
    audio: list[AudioCue] = Field(min_length=1, max_length=1)

    @model_validator(mode="after")
    def audio_valid(self):
        if self.skill != "listening":
            raise ValueError("Dictation records listening evidence; text fallback is assisted")
        return self


class Speaking(ExerciseBase):
    type: Literal["speaking"]
    audio: list[AudioCue] = Field(min_length=1, max_length=2)

    @model_validator(mode="after")
    def speaking_valid(self):
        if self.skill != "speaking" or len({cue.id for cue in self.audio}) != len(self.audio):
            raise ValueError("Speaking prompts require speaking evidence")
        return self


class ConstrainedRoleplay(Translation):
    type: Literal["constrained_roleplay"]


Exercise = Annotated[
    MultipleChoice
    | Translation
    | FillBlank
    | SentenceOrdering
    | Matching
    | ResponseSelection
    | DialogueCompletion
    | ConstrainedRoleplay
    | ListeningSelection
    | AudioContrast
    | Dictation
    | Speaking,
    Field(discriminator="type"),
]


class Concept(StrictModel):
    id: ID
    title: str
    explanation: str


class Vocabulary(StrictModel):
    id: ID
    surface: str
    reading: str
    gloss: str
    part_of_speech: str
    entry_kind: Literal["word", "phrase"] = "word"
    usage_register: str = Field(alias="register")
    example: list[Segment]
    concepts: list[ID]
    stage: ID
    status: Status
    audio: str | None = None
    pronunciation_override: str | None = Field(default=None, min_length=1, max_length=500)
    practice_exercise_ids: list[ID] = []


class Lesson(StrictModel):
    id: ID
    title: str
    japanese_title: str
    objective: str
    order: int = Field(ge=1)
    status: Status
    preparation: list[ID] = []
    exercises: list[Exercise]


class Unit(StrictModel):
    id: ID
    title: str
    japanese_title: str
    description: str
    guide: str
    order: int = Field(ge=1)
    stage: ID
    status: Status
    lessons: list[Lesson]


class Stage(StrictModel):
    id: ID
    title: str
    release: str
    can_do: list[str]
    status: Status
    word_target: int = Field(ge=0)
    kanji_target: int = Field(ge=0)


class WritingTask(StrictModel):
    id: ID
    exercise_ids: list[ID] = []
    stage: ID
    genre: str
    prompt: str
    model: str
    alternatives: list[str]
    checklist: list[str]
    revision_before: str | None = None
    revision_after: str | None = None
    revision_note: str | None = None
    status: Status = "draft"
    rubric_version: str


class License(StrictModel):
    id: ID
    source: str
    license: str
    attribution: str


class CourseContent(StrictModel):
    id: ID
    version: str = Field(pattern=r"^\d+\.\d+\.\d+$")
    title: str
    language: str
    teaching_language: str
    description: str
    status: Status
    review_note: str
    licenses: list[License] = Field(min_length=1)
    stages: list[Stage] = Field(min_length=1)
    concepts: list[Concept] = Field(min_length=1)
    vocabulary: list[Vocabulary]
    units: list[Unit] = Field(min_length=1)
    assets: list[ContentAsset] = []
    characters: list[CharacterEntry] = []
    grammar_notes: list[GrammarNote] = []
    narratives: list[Narrative] = []
    assessment_banks: list[AssessmentBank] = []
    writing_tasks: list[WritingTask]
    practice_exercises: list[Exercise] = []

    @model_validator(mode="after")
    def references_valid(self):
        all_ids = [self.id]
        all_ids += [
            x.id
            for seq in [self.stages, self.concepts, self.vocabulary, self.units, self.writing_tasks]
            for x in seq
        ]
        lessons = [lesson for u in self.units for lesson in u.lessons]
        exercises = [e for lesson in lessons for e in lesson.exercises] + self.practice_exercises
        all_ids += [x.id for x in lessons + exercises]
        all_ids += [
            x.id
            for seq in [
                self.assets,
                self.characters,
                self.grammar_notes,
                self.narratives,
                self.assessment_banks,
            ]
            for x in seq
        ]
        if len(all_ids) != len(set(all_ids)):
            raise ValueError("All content IDs must be unique across the course")
        concepts, stages = {c.id for c in self.concepts}, {s.id for s in self.stages}
        lesson_ids = {item.id for item in lessons}
        lexical_keys = [
            (
                unicodedata.normalize("NFC", item.surface),
                unicodedata.normalize("NFC", item.reading),
                item.part_of_speech,
            )
            for item in self.vocabulary
        ]
        if len(lexical_keys) != len(set(lexical_keys)):
            raise ValueError("Duplicate lexical entries: reuse a stable word ID for variants")
        graph = {lesson.id: lesson.preparation for lesson in lessons}
        complete, visiting = set(), set()

        def visit(lesson_id: str) -> None:
            if lesson_id in visiting:
                raise ValueError("Advisory preparation has a cycle")
            if lesson_id in complete:
                return
            visiting.add(lesson_id)
            for reference in graph.get(lesson_id, []):
                visit(reference)
            visiting.remove(lesson_id)
            complete.add(lesson_id)

        for lesson_id in graph:
            visit(lesson_id)

        for item in self.vocabulary + exercises:
            if not set(item.concepts) <= concepts:
                raise ValueError(f"{item.id}: broken concept reference")
        for item in self.units + self.vocabulary + self.writing_tasks:
            if item.stage not in stages:
                raise ValueError(f"{item.id}: broken stage reference")
        exercise_ids = {exercise.id for exercise in exercises}
        for note in self.grammar_notes:
            if not set(note.unit_ids) <= {unit.id for unit in self.units}:
                raise ValueError(f"{note.id}: broken unit-guide reference")
            if not set(note.practice_exercise_ids) <= exercise_ids:
                raise ValueError(f"{note.id}: broken grammar practice reference")
        for task in self.writing_tasks:
            if not set(task.exercise_ids) <= exercise_ids:
                raise ValueError(f"{task.id}: broken constrained-writing exercise reference")
        vocabulary_ids = {word.id for word in self.vocabulary}
        asset_ids = {asset.id for asset in self.assets}
        licenses = {license.id for license in self.licenses}
        for asset in self.assets:
            if asset.license_id not in licenses:
                raise ValueError(f"{asset.id}: missing asset license")
        for item in self.characters + self.narratives:
            if item.stage not in stages:
                raise ValueError(f"{item.id}: broken stage reference")
        for item in self.characters + self.grammar_notes + self.narratives + self.assessment_banks:
            if not set(item.concepts) <= concepts:
                raise ValueError(f"{item.id}: broken concept reference")
        character_keys = [(item.script, item.surface) for item in self.characters]
        if len(character_keys) != len(set(character_keys)):
            raise ValueError("Duplicate character/script entry")
        for item in self.characters + self.vocabulary:
            if not set(item.practice_exercise_ids) <= exercise_ids:
                raise ValueError(f"{item.id}: broken practice exercise reference")
        character_by_id = {item.id: item for item in self.characters}
        for item in self.characters:
            if any(key not in character_by_id for key in item.components):
                raise ValueError(f"{item.id}: missing character component")
            if (
                item.components
                and "".join(character_by_id[key].surface for key in item.components) != item.surface
            ):
                raise ValueError(f"{item.id}: components must reproduce the authored surface")
            if not set(item.vocabulary_ids) <= vocabulary_ids:
                raise ValueError(f"{item.id}: broken character vocabulary reference")
            if item.stroke_asset_id and item.stroke_asset_id not in asset_ids:
                raise ValueError(f"{item.id}: missing stroke asset")
        for item in self.assessment_banks:
            if not set(item.exercise_ids) <= exercise_ids:
                raise ValueError(f"{item.id}: broken assessment exercise reference")
        segments = [segment for word in self.vocabulary for segment in word.example]
        segments += [
            segment for story in self.narratives for turn in story.turns for segment in turn.text
        ]
        if any(
            segment.vocabulary_id and segment.vocabulary_id not in vocabulary_ids
            for segment in segments
        ):
            raise ValueError("Rich text contains a missing vocabulary reference")
        exercises_by_id = {exercise.id: exercise for exercise in exercises}
        for story in self.narratives:
            turns = {turn.id for turn in story.turns}
            if len(turns) != len(story.turns):
                raise ValueError(f"{story.id}: duplicate turn IDs")
            if (
                not set(story.vocabulary_ids) <= vocabulary_ids
                or not set(story.preparation) <= lesson_ids
            ):
                raise ValueError(f"{story.id}: broken vocabulary/preparation reference")
            if not set(story.speaking_exercise_ids) <= exercise_ids or any(
                exercises_by_id[key].type != "speaking" for key in story.speaking_exercise_ids
            ):
                raise ValueError(f"{story.id}: speaking references need authored speaking prompts")
            if not set(story.recap_exercise_ids) <= exercise_ids:
                raise ValueError(f"{story.id}: broken recap reference")
            if story.audio_asset_id and story.audio_asset_id not in asset_ids:
                raise ValueError(f"{story.id}: missing audio asset")
            for turn in story.turns:
                if (
                    not set(turn.next_turn_ids) <= turns
                    or not set(turn.response_transitions.values()) <= set(turn.next_turn_ids)
                    or not set(turn.exercise_ids) <= exercise_ids
                ):
                    raise ValueError(f"{turn.id}: broken dialogue transition/checkpoint")
                if turn.response_transitions:
                    if len(turn.exercise_ids) != 1:
                        raise ValueError(f"{turn.id}: response branches need one checkpoint")
                    checkpoint = exercises_by_id[turn.exercise_ids[0]]
                    responses = {choice.id for choice in getattr(checkpoint, "choices", [])}
                    responses.update(getattr(checkpoint, "answers", []))
                    if not set(turn.response_transitions) <= responses:
                        raise ValueError(
                            f"{turn.id}: response branch must reference a valid response"
                        )
        for exercise in exercises:
            if hasattr(exercise, "choices") and not set(exercise.response_feedback) <= {
                choice.id for choice in exercise.choices
            }:
                raise ValueError(
                    f"{exercise.id}: response feedback must identify an authored choice"
                )
            if any(not value.strip() for value in exercise.response_feedback.values()):
                raise ValueError(f"{exercise.id}: response feedback cannot be blank")
            if not set(exercise.preparation) <= concepts:
                raise ValueError(f"{exercise.id}: broken preparation reference")
            if any(not answer.strip() for answer in getattr(exercise, "answers", [])):
                raise ValueError(f"{exercise.id}: answers cannot be blank")
        for unit in self.units:
            orders = [lesson.order for lesson in unit.lessons]
            if len(set(orders)) != len(orders):
                raise ValueError(f"{unit.id}: duplicate lesson order")
            for lesson in unit.lessons:
                if not set(lesson.preparation) <= lesson_ids or lesson.id in lesson.preparation:
                    raise ValueError(f"{lesson.id}: invalid advisory preparation")
                if lesson.status == "published" and (
                    not lesson.exercises or unit.status != "published"
                ):
                    raise ValueError(
                        f"{lesson.id}: published lesson needs exercises and a published unit"
                    )
                for exercise in lesson.exercises:
                    if not set(exercise.preparation) <= concepts:
                        raise ValueError(f"{exercise.id}: broken preparation reference")
                    answers = getattr(exercise, "answers", [])
                    if any(not a.strip() for a in answers):
                        raise ValueError(f"{exercise.id}: answers cannot be blank")
        unit_orders = [u.order for u in self.units]
        if len(set(unit_orders)) != len(unit_orders):
            raise ValueError("Duplicate unit order")
        return self
