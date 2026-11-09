from pydantic import Field

from app.schemas import StrictModel


class BackupProfile(StrictModel):
    id: str
    name: str
    timezone: str


class BackupSummary(StrictModel):
    total_xp: int = 0
    study_sessions_completed: int = 0
    study_sessions_total: int = 0
    review_cards_count: int = 0
    writing_drafts_count: int = 0
    writing_revisions_count: int = 0
    collections_count: int = 0
    drawing_samples_count: int = 0
    reading_items_saved: int = 0
    reading_items_familiar: int = 0
    audio_deliveries_count: int = 0
    quests_count: int = 0
    badges_count: int = 0
    mistakes_count: int = 0


class BackupManifest(StrictModel):
    format_version: int = 1
    app_name: str = "Trilingo"
    app_version: str = "0.1.0"
    created_at: str
    schema_version: str
    course_id: str | None = None
    course_version: str | None = None
    database_sha256: str
    database_size_bytes: int
    profile: BackupProfile
    summary: BackupSummary
    included_entities: list[str]
    exclusions: list[str]
    include_drawing_samples: bool = True


class BackupPreviewOut(StrictModel):
    valid: bool
    created_at: str
    app_name: str
    app_version: str
    schema_version: str
    compatible: bool
    profile: BackupProfile
    summary: BackupSummary
    course_id: str | None = None
    course_version: str | None = None
    include_drawing_samples: bool
    warning: str


class RestoreResultOut(StrictModel):
    restored: bool
    created_at: str
    profile: BackupProfile
    summary: BackupSummary
    safety_backup_file: str | None = None


class ResetRequest(StrictModel):
    confirm: bool = Field(default=False)


class ResetResultOut(StrictModel):
    reset: bool
    profile: BackupProfile
    message: str
    safety_backup_file: str | None = None


class SafetyBackupItem(StrictModel):
    filename: str
    size_bytes: int
    created_at: str
    kind: str


class SafetyBackupListOut(StrictModel):
    backups: list[SafetyBackupItem]
