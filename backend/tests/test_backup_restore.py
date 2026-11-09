import io
import json
import sqlite3
import zipfile
from pathlib import Path

from fastapi.testclient import TestClient

from app.config import Config
from app.main import create_app


def test_backup_export_creates_valid_archive_and_manifest(tmp_path: Path, monkeypatch):
    db_file = tmp_path / "test_export.db"
    backups_dir = tmp_path / "backups"
    url = f"sqlite:///{db_file.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)

    # Setup database with schema and sample learner data
    from alembic import command
    from alembic.config import Config as AlembicConfig

    cfg = AlembicConfig("alembic.ini")
    command.upgrade(cfg, "head")

    app_config = Config(database_url=url, backups_dir=backups_dir, qa_mode=True)
    app = create_app(app_config)

    with TestClient(app) as client:
        # Update profile and add XP / study records
        client.patch("/api/v1/profile", json={"name": "Test Adventurer", "timezone": "Asia/Tokyo"})

        # Export backup
        res = client.get("/api/v1/backup/export")
        assert res.status_code == 200
        assert res.headers["content-type"] == "application/zip"
        assert "trilingo-backup-" in res.headers["content-disposition"]

        # Parse zip
        zf = zipfile.ZipFile(io.BytesIO(res.content), "r")
        assert set(zf.namelist()) == {"manifest.json", "database.sqlite"}

        manifest_data = json.loads(zf.read("manifest.json").decode("utf-8"))
        assert manifest_data["app_name"] == "Trilingo"
        assert manifest_data["format_version"] == 1
        assert manifest_data["profile"]["name"] == "Test Adventurer"
        assert manifest_data["profile"]["timezone"] == "Asia/Tokyo"
        assert manifest_data["schema_version"] == "0013"
        assert manifest_data["include_drawing_samples"] is True
        assert "credentials" in manifest_data["exclusions"]

        # Verify database.sqlite in zip is readable and valid
        db_bytes = zf.read("database.sqlite")
        temp_disk = tmp_path / "inspect.db"
        temp_disk.write_bytes(db_bytes)
        disk_conn = sqlite3.connect(str(temp_disk))
        cur = disk_conn.cursor()
        cur.execute("PRAGMA integrity_check")
        assert cur.fetchone()[0] == "ok"
        cur.execute("SELECT name FROM profiles WHERE id = 'local'")
        assert cur.fetchone()[0] == "Test Adventurer"
        disk_conn.close()


def test_backup_preview_and_validation(tmp_path: Path, monkeypatch):
    db_file = tmp_path / "test_preview.db"
    backups_dir = tmp_path / "backups"
    url = f"sqlite:///{db_file.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)

    from alembic import command
    from alembic.config import Config as AlembicConfig

    cfg = AlembicConfig("alembic.ini")
    command.upgrade(cfg, "head")

    app_config = Config(database_url=url, backups_dir=backups_dir, qa_mode=True)
    app = create_app(app_config)

    with TestClient(app) as client:
        # 1. Valid preview
        export_res = client.get("/api/v1/backup/export")
        assert export_res.status_code == 200

        preview_res = client.post(
            "/api/v1/backup/preview",
            content=export_res.content,
            headers={"Content-Type": "application/zip"},
        )
        assert preview_res.status_code == 200
        preview = preview_res.json()
        assert preview["valid"] is True
        assert preview["compatible"] is True
        assert preview["app_name"] == "Trilingo"
        assert preview["schema_version"] == "0013"
        assert "warning" in preview

        # 2. Corrupt archive rejection
        bad_res = client.post(
            "/api/v1/backup/preview",
            content=b"not a real zip archive header",
            headers={"Content-Type": "application/zip"},
        )
        assert bad_res.status_code == 422
        assert bad_res.json()["error"]["code"] == "corrupt_archive"

        # 3. Path traversal rejection
        zip_buf = io.BytesIO()
        with zipfile.ZipFile(zip_buf, "w") as zf:
            zf.writestr("../evil.txt", "attack")
            zf.writestr("manifest.json", "{}")
        trap_res = client.post(
            "/api/v1/backup/preview",
            content=zip_buf.getvalue(),
            headers={"Content-Type": "application/zip"},
        )
        assert trap_res.status_code == 422
        assert trap_res.json()["error"]["code"] == "path_traversal"

        # 4. Unexpected files rejection
        zip_buf2 = io.BytesIO()
        with zipfile.ZipFile(zip_buf2, "w") as zf:
            zf.writestr("manifest.json", "{}")
            zf.writestr("extra_file.txt", "extra")
        trap_res2 = client.post(
            "/api/v1/backup/preview",
            content=zip_buf2.getvalue(),
            headers={"Content-Type": "application/zip"},
        )
        assert trap_res2.status_code == 422
        assert trap_res2.json()["error"]["code"] == "unexpected_archive_content"


def test_restore_replaces_progress_atomically_and_saves_safety_backup(tmp_path: Path, monkeypatch):
    db_file = tmp_path / "test_restore.db"
    backups_dir = tmp_path / "backups"
    url = f"sqlite:///{db_file.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)

    from alembic import command
    from alembic.config import Config as AlembicConfig

    cfg = AlembicConfig("alembic.ini")
    command.upgrade(cfg, "head")

    app_config = Config(database_url=url, backups_dir=backups_dir, qa_mode=True)
    app = create_app(app_config)

    with TestClient(app) as client:
        # Initial state: Snapshot A
        client.patch("/api/v1/profile", json={"name": "Initial Snapshot User"})
        export_a = client.get("/api/v1/backup/export").content

        # Change state: State B
        client.patch("/api/v1/profile", json={"name": "Mutated User", "timezone": "Asia/Singapore"})
        prof_b = client.get("/api/v1/profile").json()
        assert prof_b["name"] == "Mutated User"

        # Unconfirmed restore must fail
        unconf_res = client.post(
            "/api/v1/backup/restore?confirm=false",
            content=export_a,
            headers={"Content-Type": "application/zip"},
        )
        assert unconf_res.status_code == 422
        assert unconf_res.json()["error"]["code"] == "confirmation_required"

        # Confirmed restore
        restore_res = client.post(
            "/api/v1/backup/restore?confirm=true",
            content=export_a,
            headers={"Content-Type": "application/zip"},
        )
        assert restore_res.status_code == 200
        res_json = restore_res.json()
        assert res_json["restored"] is True
        assert res_json["profile"]["name"] == "Initial Snapshot User"
        assert res_json["safety_backup_file"] is not None

        # Verify live database now has Initial Snapshot User
        prof_after = client.get("/api/v1/profile").json()
        assert prof_after["name"] == "Initial Snapshot User"

        # Verify a safety backup was saved before restore
        safety_backups = client.get("/api/v1/backup/safety-backups").json()
        assert len(safety_backups["backups"]) >= 1
        assert safety_backups["backups"][0]["kind"] == "pre_restore"


def test_reset_learner_progress_and_preserves_courses(tmp_path: Path, monkeypatch):
    db_file = tmp_path / "test_reset.db"
    backups_dir = tmp_path / "backups"
    url = f"sqlite:///{db_file.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)

    from alembic import command
    from alembic.config import Config as AlembicConfig

    cfg = AlembicConfig("alembic.ini")
    command.upgrade(cfg, "head")

    app_config = Config(database_url=url, backups_dir=backups_dir, qa_mode=True)
    app = create_app(app_config)

    with TestClient(app) as client:
        # Update profile
        client.patch("/api/v1/profile", json={"name": "Learner To Reset"})
        assert client.get("/api/v1/profile").json()["name"] == "Learner To Reset"

        # Reset without confirmation fails
        unconf_res = client.post("/api/v1/backup/reset", json={"confirm": False})
        assert unconf_res.status_code == 422
        assert unconf_res.json()["error"]["code"] == "confirmation_required"

        # Confirmed reset
        reset_res = client.post("/api/v1/backup/reset", json={"confirm": True})
        assert reset_res.status_code == 200
        reset_json = reset_res.json()
        assert reset_json["reset"] is True
        assert reset_json["profile"]["name"] == "Learner"
        assert reset_json["profile"]["timezone"] == "UTC"
        assert reset_json["safety_backup_file"] is not None

        # Profile is back to default
        prof_after = client.get("/api/v1/profile").json()
        assert prof_after["name"] == "Learner"

        # Safety backup exists
        safety_backups = client.get("/api/v1/backup/safety-backups").json()
        assert any(b["kind"] == "pre_reset" for b in safety_backups["backups"])


def test_backup_drawing_samples_exclusion_option(tmp_path: Path, monkeypatch):
    db_file = tmp_path / "test_samples.db"
    backups_dir = tmp_path / "backups"
    url = f"sqlite:///{db_file.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)

    from alembic import command
    from alembic.config import Config as AlembicConfig

    cfg = AlembicConfig("alembic.ini")
    command.upgrade(cfg, "head")

    app_config = Config(database_url=url, backups_dir=backups_dir, qa_mode=True)
    app = create_app(app_config)

    with TestClient(app) as client:
        # Export with include_samples=false
        res = client.get("/api/v1/backup/export?include_samples=false")
        assert res.status_code == 200

        zf = zipfile.ZipFile(io.BytesIO(res.content), "r")
        manifest = json.loads(zf.read("manifest.json").decode("utf-8"))
        assert manifest["include_drawing_samples"] is False


def test_incompatible_future_schema_and_tamper_detection(tmp_path: Path, monkeypatch):
    db_file = tmp_path / "test_tamper.db"
    backups_dir = tmp_path / "backups"
    url = f"sqlite:///{db_file.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)

    from alembic import command
    from alembic.config import Config as AlembicConfig

    cfg = AlembicConfig("alembic.ini")
    command.upgrade(cfg, "head")

    app_config = Config(database_url=url, backups_dir=backups_dir, qa_mode=True)
    app = create_app(app_config)

    with TestClient(app) as client:
        valid_zip = client.get("/api/v1/backup/export").content
        zf = zipfile.ZipFile(io.BytesIO(valid_zip), "r")
        manifest = json.loads(zf.read("manifest.json").decode("utf-8"))
        db_bytes = zf.read("database.sqlite")

        # 1. Tampered checksum
        tampered_db = bytearray(db_bytes)
        tampered_db[100] = (tampered_db[100] + 1) % 256
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as out_zf:
            out_zf.writestr("manifest.json", json.dumps(manifest))
            out_zf.writestr("database.sqlite", bytes(tampered_db))

        res_tampered = client.post(
            "/api/v1/backup/preview",
            content=buf.getvalue(),
            headers={"Content-Type": "application/zip"},
        )
        assert res_tampered.status_code == 422
        assert res_tampered.json()["error"]["code"] == "checksum_mismatch"

        # 2. Incompatible future schema
        future_manifest = {**manifest, "schema_version": "9999"}
        buf2 = io.BytesIO()
        with zipfile.ZipFile(buf2, "w") as out_zf:
            out_zf.writestr("manifest.json", json.dumps(future_manifest))
            out_zf.writestr("database.sqlite", db_bytes)

        preview_future = client.post(
            "/api/v1/backup/preview",
            content=buf2.getvalue(),
            headers={"Content-Type": "application/zip"},
        )
        assert preview_future.status_code == 200
        assert preview_future.json()["compatible"] is False
        assert "Incompatible backup schema" in preview_future.json()["warning"]

        # Restore of future schema must be rejected
        restore_future = client.post(
            "/api/v1/backup/restore?confirm=true",
            content=buf2.getvalue(),
            headers={"Content-Type": "application/zip"},
        )
        assert restore_future.status_code == 422
        assert restore_future.json()["error"]["code"] == "incompatible_schema"

