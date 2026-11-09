import hashlib
import io
import json
import logging
import os
import sqlite3
import tempfile
import threading
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from alembic.config import Config as AlembicConfig
from alembic.script import ScriptDirectory
from sqlalchemy import text

from app.backup_schemas import (
    BackupManifest,
    BackupPreviewOut,
    BackupProfile,
    BackupSummary,
    ResetResultOut,
    RestoreResultOut,
    SafetyBackupItem,
    SafetyBackupListOut,
)
from app.config import ROOT, Config
from app.db import make_engine
from app.models import Preferences, Profile
from app.schemas import Settings
from app.services import DomainError

logger = logging.getLogger("trilingo.backup")

_backup_lock = threading.RLock()

MAX_BACKUP_BYTES = 50_000_000
MAX_UNCOMPRESSED_BYTES = 150_000_000
MAX_SAFETY_BACKUPS = 10

INCLUDED_ENTITIES = [
    "profiles",
    "preferences",
    "study_sessions",
    "study_events",
    "xp_ledger",
    "study_mistakes",
    "reading_items",
    "writing_drafts",
    "writing_revisions",
    "writing_conflicts",
    "writing_submissions",
    "writing_events",
    "drawing_samples",
    "review_cards",
    "review_events",
    "quest_assignments",
    "personal_badges",
    "vocabulary_collections",
    "collection_members",
    "audio_deliveries",
    "content_assistance",
    "enrollments",
    "courses",
    "course_versions",
]

EXCLUSIONS = [
    "credentials",
    "transient_recordings",
    "audio_cache",
]

TABLES_TO_CLEAR_ON_RESET = [
    "writing_submissions",
    "writing_conflicts",
    "writing_revisions",
    "writing_drafts",
    "writing_events",
    "drawing_samples",
    "study_events",
    "study_mistakes",
    "xp_ledger",
    "audio_deliveries",
    "study_sessions",
    "reading_items",
    "review_events",
    "review_cards",
    "collection_members",
    "vocabulary_collections",
    "quest_assignments",
    "personal_badges",
    "content_assistance",
    "enrollments",
]


def get_database_path(config: Config) -> Path | None:
    if config.database_url == "sqlite:///:memory:":
        return None
    raw = config.database_url.removeprefix("sqlite:///")
    path = Path(raw)
    return path if path.is_absolute() else ROOT / path


def get_expected_schema_head() -> str:
    alembic_ini = ROOT / "backend" / "alembic.ini"
    if not alembic_ini.is_file():
        alembic_ini = ROOT / "alembic.ini"
    return ScriptDirectory.from_config(AlembicConfig(str(alembic_ini))).get_current_head()


def query_summary_from_connection(conn: sqlite3.Connection) -> BackupSummary:
    cur = conn.cursor()

    def count(table: str, condition: str = "") -> int:
        try:
            sql = f"SELECT COUNT(*) FROM {table}"
            if condition:
                sql += f" WHERE {condition}"
            cur.execute(sql)
            row = cur.fetchone()
            return int(row[0]) if row and row[0] is not None else 0
        except sqlite3.OperationalError:
            return 0

    def sum_val(table: str, col: str) -> int:
        try:
            cur.execute(f"SELECT COALESCE(SUM({col}), 0) FROM {table}")
            row = cur.fetchone()
            return int(row[0]) if row and row[0] is not None else 0
        except sqlite3.OperationalError:
            return 0

    return BackupSummary(
        total_xp=sum_val("xp_ledger", "amount"),
        study_sessions_completed=count("study_sessions", "status = 'completed'"),
        study_sessions_total=count("study_sessions"),
        review_cards_count=count("review_cards"),
        writing_drafts_count=count("writing_drafts"),
        writing_revisions_count=count("writing_revisions"),
        collections_count=count("vocabulary_collections"),
        drawing_samples_count=count("drawing_samples"),
        reading_items_saved=count("reading_items", "saved = 1"),
        reading_items_familiar=count("reading_items", "familiar = 1"),
        audio_deliveries_count=count("audio_deliveries"),
        quests_count=count("quest_assignments"),
        badges_count=count("personal_badges"),
        mistakes_count=count("study_mistakes"),
    )


def create_backup(config: Config, include_samples: bool = True) -> tuple[bytes, BackupManifest]:
    with _backup_lock:
        db_path = get_database_path(config)
        is_memory = db_path is None

        temp_dump_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        temp_dump_path = Path(temp_dump_file.name)
        temp_dump_file.close()

        try:
            if is_memory:
                source_conn = sqlite3.connect(":memory:")
            else:
                source_conn = sqlite3.connect(str(db_path), timeout=10)

            dump_conn = sqlite3.connect(str(temp_dump_path))
            try:
                source_conn.backup(dump_conn)
            finally:
                source_conn.close()

            cur = dump_conn.cursor()
            try:
                cur.execute("SELECT version_num FROM alembic_version")
                schema_row = cur.fetchone()
                schema_version = schema_row[0] if schema_row else "unknown"
            except sqlite3.OperationalError:
                schema_version = "unknown"

            try:
                cur.execute("SELECT id, name, timezone FROM profiles WHERE id = 'local'")
                prof_row = cur.fetchone()
                if prof_row:
                    profile = BackupProfile(id=prof_row[0], name=prof_row[1], timezone=prof_row[2])
                else:
                    profile = BackupProfile(id="local", name="Learner", timezone="UTC")
            except sqlite3.OperationalError:
                profile = BackupProfile(id="local", name="Learner", timezone="UTC")

            course_id = None
            course_version = None
            try:
                cur.execute("SELECT id, current_version FROM courses LIMIT 1")
                course_row = cur.fetchone()
                if course_row:
                    course_id = course_row[0]
                    course_version = course_row[1]
            except sqlite3.OperationalError:
                pass

            if not include_samples:
                try:
                    cur.execute("DELETE FROM drawing_samples")
                    dump_conn.commit()
                    cur.execute("VACUUM")
                except sqlite3.OperationalError:
                    pass

            summary = query_summary_from_connection(dump_conn)
            dump_conn.close()

            db_bytes = temp_dump_path.read_bytes()
            sha256 = hashlib.sha256(db_bytes).hexdigest()
            size_bytes = len(db_bytes)

            manifest = BackupManifest(
                format_version=1,
                app_name="Trilingo",
                app_version="0.1.0",
                created_at=datetime.now(timezone.utc).isoformat(),
                schema_version=schema_version,
                course_id=course_id,
                course_version=course_version,
                database_sha256=sha256,
                database_size_bytes=size_bytes,
                profile=profile,
                summary=summary,
                included_entities=INCLUDED_ENTITIES,
                exclusions=EXCLUSIONS,
                include_drawing_samples=include_samples,
            )

            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
                manifest_json = manifest.model_dump_json(indent=2)
                zf.writestr("manifest.json", manifest_json.encode("utf-8"))
                zf.writestr("database.sqlite", db_bytes)

            return zip_buffer.getvalue(), manifest

        finally:
            if temp_dump_path.exists():
                try:
                    temp_dump_path.unlink()
                except OSError:
                    pass


def save_safety_backup(config: Config, reason: str = "safety") -> str:
    config.backups_dir.mkdir(parents=True, exist_ok=True)
    zip_bytes, _ = create_backup(config, include_samples=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    filename = f"trilingo-{reason}-{timestamp}.zip"
    target_path = config.backups_dir / filename
    target_path.write_bytes(zip_bytes)

    # Prune old safety backups if exceeding limit
    try:
        backups = sorted(
            config.backups_dir.glob("trilingo-*.zip"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        for old in backups[MAX_SAFETY_BACKUPS:]:
            try:
                old.unlink()
            except OSError:
                pass
    except Exception as exc:
        logger.warning("Could not prune old safety backups: %s", exc)

    return filename


def validate_backup_archive(archive_bytes: bytes) -> tuple[BackupManifest, bytes]:
    if len(archive_bytes) > MAX_BACKUP_BYTES:
        limit_mb = MAX_BACKUP_BYTES // 1_000_000
        raise DomainError(
            413,
            "backup_too_large",
            f"Backup archive exceeds the maximum allowed size of {limit_mb}MB.",
        )

    try:
        zf = zipfile.ZipFile(io.BytesIO(archive_bytes), "r")
    except zipfile.BadZipFile as error:
        raise DomainError(
            422, "corrupt_archive", "The uploaded file is not a valid zip archive."
        ) from error

    with zf:
        namelist = zf.namelist()
        total_uncompressed = 0
        for info in zf.infolist():
            total_uncompressed += info.file_size
            filename = info.filename
            if ".." in filename or filename.startswith(("/", "\\")):
                raise DomainError(
                    422, "path_traversal", "Archive contains an unsafe path traversal file name."
                )
            if filename not in {"manifest.json", "database.sqlite"}:
                raise DomainError(
                    422,
                    "unexpected_archive_content",
                    f"Unexpected entry '{filename}'. Expected manifest.json and database.sqlite.",
                )

        if total_uncompressed > MAX_UNCOMPRESSED_BYTES:
            raise DomainError(
                422, "backup_too_large", "Uncompressed archive content exceeds safety limits."
            )

        if "manifest.json" not in namelist or "database.sqlite" not in namelist:
            raise DomainError(
                422,
                "missing_required_files",
                "Backup archive must contain both manifest.json and database.sqlite.",
            )

        try:
            manifest_bytes = zf.read("manifest.json")
            manifest_dict = json.loads(manifest_bytes.decode("utf-8"))
            manifest = BackupManifest.model_validate(manifest_dict)
        except Exception as error:
            raise DomainError(
                422, "invalid_manifest", f"The backup manifest is invalid or malformed: {error}"
            ) from error

        if manifest.format_version != 1 or manifest.app_name != "Trilingo":
            raise DomainError(
                422, "unsupported_backup", "Unsupported backup format or application name."
            )

        db_bytes = zf.read("database.sqlite")
        computed_sha = hashlib.sha256(db_bytes).hexdigest()
        if computed_sha != manifest.database_sha256:
            raise DomainError(
                422,
                "checksum_mismatch",
                "Database file checksum does not match manifest. The backup may be corrupted.",
            )

        temp_check = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        temp_check_path = Path(temp_check.name)
        temp_check.write(db_bytes)
        temp_check.close()

        try:
            conn = sqlite3.connect(str(temp_check_path))
            try:
                cur = conn.cursor()
                cur.execute("PRAGMA integrity_check")
                rows = cur.fetchall()
                if not rows or rows[0][0] != "ok":
                    raise DomainError(
                        422,
                        "database_integrity_failed",
                        "SQLite integrity check failed on the backup.",
                    )

                cur.execute("SELECT version_num FROM alembic_version")
                schema_row = cur.fetchone()
                if not schema_row or not schema_row[0]:
                    raise DomainError(
                        422,
                        "missing_schema_version",
                        "Backup database missing alembic_version record.",
                    )
            finally:
                conn.close()
        except sqlite3.OperationalError as error:
            raise DomainError(
                422, "invalid_database", f"Database validation error: {error}"
            ) from error
        finally:
            if temp_check_path.exists():
                try:
                    temp_check_path.unlink()
                except OSError:
                    pass

        return manifest, db_bytes


def preview_backup(archive_bytes: bytes) -> BackupPreviewOut:
    manifest, _ = validate_backup_archive(archive_bytes)
    expected_head = get_expected_schema_head()

    # Verify schema version is not newer than our current schema head
    compatible = manifest.schema_version <= expected_head

    warning = (
        "Restoring this point-in-time snapshot will replace all current learning progress "
        "on this device. A safety backup of your current data is saved before restoring."
    )
    if not compatible:
        warning = (
            f"Incompatible backup schema '{manifest.schema_version}'. "
            f"This application supports schema head '{expected_head}'."
        )

    return BackupPreviewOut(
        valid=True,
        created_at=manifest.created_at,
        app_name=manifest.app_name,
        app_version=manifest.app_version,
        schema_version=manifest.schema_version,
        compatible=compatible,
        profile=manifest.profile,
        summary=manifest.summary,
        course_id=manifest.course_id,
        course_version=manifest.course_version,
        include_drawing_samples=manifest.include_drawing_samples,
        warning=warning,
    )


def restore_backup(
    engine,
    session_factory,
    config: Config,
    archive_bytes: bytes,
    confirm: bool,
) -> RestoreResultOut:
    if not confirm:
        raise DomainError(
            422,
            "confirmation_required",
            "Explicit confirmation is required to restore a backup and replace local records.",
        )

    with _backup_lock:
        manifest, db_bytes = validate_backup_archive(archive_bytes)
        expected_head = get_expected_schema_head()

        if manifest.schema_version > expected_head:
            msg = f"Cannot restore schema '{manifest.schema_version}' (head: '{expected_head}')."
            raise DomainError(422, "incompatible_schema", msg)

        db_path = get_database_path(config)

        # 1. Create safety backup first
        safety_file = save_safety_backup(config, reason="pre-restore")

        # 2. If in-memory, restore directly via SQLite backup API
        if db_path is None:
            temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
            temp_db.write(db_bytes)
            temp_db.close()
            try:
                disk_conn = sqlite3.connect(temp_db.name)
                # Dispose existing engine
                engine.dispose()
                with session_factory() as session:
                    raw_conn = session.connection().connection.driver_connection
                    disk_conn.backup(raw_conn)
                    session.commit()
                disk_conn.close()
            finally:
                if Path(temp_db.name).exists():
                    Path(temp_db.name).unlink()
        else:
            # 3. For file database: quiesce engine and replace file atomically
            engine.dispose()

            staging_path = db_path.with_suffix(".restore_staging")
            staging_path.write_bytes(db_bytes)

            wal_path = Path(str(db_path) + "-wal")
            shm_path = Path(str(db_path) + "-shm")
            if wal_path.exists():
                try:
                    wal_path.unlink()
                except OSError:
                    pass
            if shm_path.exists():
                try:
                    shm_path.unlink()
                except OSError:
                    pass

            # Atomic replace
            os.replace(staging_path, db_path)

            # Reconfigure engine and session factory
            new_engine = make_engine(config.database_url)
            session_factory.configure(bind=new_engine)

        return RestoreResultOut(
            restored=True,
            created_at=manifest.created_at,
            profile=manifest.profile,
            summary=manifest.summary,
            safety_backup_file=safety_file,
        )


def reset_learner_progress(
    engine,
    session_factory,
    config: Config,
    confirm: bool,
) -> ResetResultOut:
    if not confirm:
        raise DomainError(
            422,
            "confirmation_required",
            "Explicit confirmation is required to reset local learning progress.",
        )

    with _backup_lock:
        # Create safety backup before destroying any records
        safety_file = save_safety_backup(config, reason="pre-reset")

        with session_factory() as db:
            for table in TABLES_TO_CLEAR_ON_RESET:
                try:
                    db.execute(text(f"DELETE FROM {table}"))
                except Exception as err:
                    logger.warning("Could not clear table %s: %s", table, err)

            # Reset profile to clean state
            profile = db.get(Profile, "local")
            if profile is not None:
                profile.name = "Learner"
                profile.timezone = "UTC"
            else:
                db.add(Profile(id="local", name="Learner", timezone="UTC"))

            # Reset preferences to default settings
            prefs = db.get(Preferences, "local")
            default_settings = Settings().model_dump()
            if prefs is not None:
                prefs.data = default_settings
            else:
                db.add(Preferences(profile_id="local", data=default_settings))

            db.commit()

        # Run VACUUM to reclaim storage and refresh SQLite pages
        try:
            with engine.connect() as conn:
                conn.execution_options(isolation_level="AUTOCOMMIT").execute(text("VACUUM"))
        except Exception as exc:
            logger.warning("Vacuum after reset encountered non-fatal notice: %s", exc)

        return ResetResultOut(
            reset=True,
            profile=BackupProfile(id="local", name="Learner", timezone="UTC"),
            message=(
                "All learning progress, review schedules, and drafts have been reset. "
                "A safety backup was created before resetting."
            ),
            safety_backup_file=safety_file,
        )


def list_safety_backups(config: Config) -> SafetyBackupListOut:
    backups_dir = config.backups_dir
    if not backups_dir.is_dir():
        return SafetyBackupListOut(backups=[])

    items: list[SafetyBackupItem] = []
    for file_path in backups_dir.glob("trilingo-*.zip"):
        try:
            stat = file_path.stat()
            name = file_path.name
            kind = "manual"
            if "pre-restore" in name:
                kind = "pre_restore"
            elif "pre-reset" in name:
                kind = "pre_reset"

            items.append(
                SafetyBackupItem(
                    filename=name,
                    size_bytes=stat.st_size,
                    created_at=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                    kind=kind,
                )
            )
        except OSError:
            continue

    items.sort(key=lambda item: item.created_at, reverse=True)
    return SafetyBackupListOut(backups=items)
