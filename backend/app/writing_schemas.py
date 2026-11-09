from typing import Literal

from pydantic import Field, model_validator

from app.content_schema import ID, WritingTask
from app.learning_schemas import RequestId
from app.schemas import StrictModel


class DraftCreate(StrictModel):
    request_id: RequestId
    task_id: ID
    preview_draft: bool = False


class DraftSave(StrictModel):
    request_id: RequestId
    expected_revision_id: RequestId
    text: str = Field(max_length=24000)
    checklist: list[str] = Field(default_factory=list, max_length=30)
    model_revealed: bool = False


class DraftSubmit(StrictModel):
    request_id: RequestId
    revision_id: RequestId
    self_reviewed: bool = False


class RevisionOut(StrictModel):
    id: str
    number: int
    text: str
    checklist: list[str]
    model_revealed: bool
    created_at: str


class ConflictOut(StrictModel):
    id: str
    text: str
    checklist: list[str]
    model_revealed: bool
    expected_revision_id: str
    server_revision_id: str
    created_at: str


class DraftOut(StrictModel):
    id: str
    course_id: str
    content_version: str
    task: WritingTask
    current: RevisionOut
    created_at: str
    updated_at: str
    assessment: Literal["not_assessed"] = "not_assessed"


class DraftSummary(StrictModel):
    id: str
    task_id: str
    title: str
    content_version: str
    updated_at: str


class WritingCatalog(StrictModel):
    tasks: list[WritingTask]
    drafts: list[DraftSummary]
    has_more: bool
    offset: int
    includes_drafts: bool
    content_version: str


class WritingHistory(StrictModel):
    revisions: list[RevisionOut]
    conflicts: list[ConflictOut]
    has_more_revisions: bool
    has_more_conflicts: bool
    offset: int


class SubmissionOut(StrictModel):
    id: str
    draft_id: str
    revision_id: str
    xp_awarded: int
    evidence_mode: Literal["open_writing"] = "open_writing"
    assessment: Literal["not_assessed", "self_reviewed"]
    message: str


class StrokePoint(StrictModel):
    x: float = Field(ge=0, le=1, allow_inf_nan=False)
    y: float = Field(ge=0, le=1, allow_inf_nan=False)
    t: int = Field(ge=0, le=86400000)


class GuidePoint(StrictModel):
    x: float = Field(ge=0, le=1, allow_inf_nan=False)
    y: float = Field(ge=0, le=1, allow_inf_nan=False)


class StrokePath(StrictModel):
    points: list[GuidePoint] = Field(min_length=2, max_length=100)
    instruction: str = Field(min_length=1)


class StrokeGuide(StrictModel):
    id: ID
    character_id: ID
    version: str
    license_id: ID
    source: str
    status: Literal["draft", "reviewed"]
    strokes: list[StrokePath] = Field(min_length=1, max_length=40)


class HandwritingCommit(StrictModel):
    request_id: RequestId
    character_id: ID
    preview_draft: bool = False
    mode: Literal["guided_trace", "freehand_self_check", "accessible_sequence"]
    strokes: list[list[StrokePoint]] = Field(default_factory=list, max_length=200)
    sequence: list[int] = Field(default_factory=list, max_length=40)
    reference_revealed: bool = False
    self_rating: Literal["practiced", "needs_practice"]
    keep_sample: bool = False

    @model_validator(mode="after")
    def bounds(self):
        if sum(len(stroke) for stroke in self.strokes) > 1200:
            raise ValueError(
                "A saved sample supports up to1200 points; simplify or keep practicing unsaved"
            )
        if any(len(stroke) < 2 for stroke in self.strokes):
            raise ValueError("Each stroke needs at least two points")
        times = [point.t for stroke in self.strokes for point in stroke]
        if times != sorted(times):
            raise ValueError("Stroke times must be ordered")
        if self.mode == "accessible_sequence":
            if self.strokes or self.keep_sample or not self.sequence:
                raise ValueError("Sequence mode uses numbered selections, without drawing samples")
        elif self.sequence or not self.strokes:
            raise ValueError("Drawing modes need strokes and no sequence selections")
        return self


class HandwritingOut(StrictModel):
    id: str
    character_id: str
    mode: str
    evidence: Literal["self_reported_practice"] = "self_reported_practice"
    self_rating: str
    feedback: str
    xp_awarded: int
    sample_id: str | None
    objective_correctness: None = None


class SampleOut(StrictModel):
    id: str
    character_id: str
    mode: str
    strokes: list[list[StrokePoint]]
    created_at: str
