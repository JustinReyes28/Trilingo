from datetime import datetime, timezone

from fastapi import APIRouter, FastAPI, Query, Request, Response

from app import backup_service
from app.backup_schemas import (
    BackupPreviewOut,
    ResetRequest,
    ResetResultOut,
    RestoreResultOut,
    SafetyBackupListOut,
)
from app.config import Config
from app.services import DomainError


def register_backup_routes(app: FastAPI, get_db, config: Config) -> None:
    router = APIRouter(prefix="/api/v1/backup", tags=["backup"])

    @router.get("/export")
    def export_backup(include_samples: bool = Query(default=True)):
        zip_bytes, _ = backup_service.create_backup(config, include_samples=include_samples)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        filename = f"trilingo-backup-{timestamp}.zip"
        return Response(
            content=zip_bytes,
            media_type="application/zip",
            headers={
                "Content-Disposition": f'attachment; filename="{filename}"',
                "Cache-Control": "no-store",
            },
        )

    @router.post("/preview", response_model=BackupPreviewOut)
    async def preview_backup(request: Request):
        body_bytes = await request.body()
        if not body_bytes:
            raise DomainError(422, "empty_body", "Upload a non-empty backup archive.")
        return backup_service.preview_backup(body_bytes)

    @router.post("/restore", response_model=RestoreResultOut)
    async def restore_backup(
        request: Request,
        confirm: bool = Query(default=False),
    ):
        body_bytes = await request.body()
        if not body_bytes:
            raise DomainError(422, "empty_body", "Upload a non-empty backup archive to restore.")
        engine = app.state.engine
        factory = app.state.session_factory
        return backup_service.restore_backup(
            engine=engine,
            session_factory=factory,
            config=config,
            archive_bytes=body_bytes,
            confirm=confirm,
        )

    @router.post("/reset", response_model=ResetResultOut)
    def reset_progress(body: ResetRequest):
        engine = app.state.engine
        factory = app.state.session_factory
        return backup_service.reset_learner_progress(
            engine=engine,
            session_factory=factory,
            config=config,
            confirm=body.confirm,
        )

    @router.get("/safety-backups", response_model=SafetyBackupListOut)
    def get_safety_backups():
        return backup_service.list_safety_backups(config)

    app.include_router(router)
