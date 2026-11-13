import logging
from collections.abc import Iterator
from contextlib import asynccontextmanager
from typing import Annotated, Literal
from uuid import UUID

from alembic.config import Config as AlembicConfig
from alembic.script import ScriptDirectory
from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from app import services
from app.audio_api import register_audio_routes
from app.backup_api import register_backup_routes
from app.config import ROOT, Config
from app.db import make_engine, sessions
from app.learning_api import register_learning_routes
from app.middleware import RequestBodyLimit
from app.practice_api import register_practice_routes
from app.public_schemas import (
    AssistanceOut,
    CourseMap,
    CourseSummary,
    EnrollmentOut,
    HealthOut,
    LibraryOut,
    PublicLesson,
)
from app.reading_api import register_reading_routes
from app.schemas import ProfileOut, ProfilePatch, Settings, SettingsPatch, timezone_name
from app.writing_api import register_writing_routes

logger = logging.getLogger("trilingo")


def create_app(config: Config | None = None) -> FastAPI:
    config = config or Config()
    engine = make_engine(config.database_url)
    factory = sessions(engine)
    expected_schema = ScriptDirectory.from_config(
        AlembicConfig(str(ROOT / "backend" / "alembic.ini"))
    ).get_current_head()

    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        logger.info("Trilingo starting; local SQLite; bundled audio=%s", config.audio_pack_enabled)
        yield
        engine.dispose()

    app = FastAPI(title="Trilingo local API", version="0.1.0", lifespan=lifespan)
    app.state.engine = engine
    app.state.session_factory = factory
    app.state.config = config
    app.add_middleware(RequestBodyLimit)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors_origins,
        allow_methods=["GET", "PATCH", "POST", "DELETE"],
        allow_headers=["Content-Type"],
    )

    def get_db() -> Iterator[Session]:
        with factory() as db:
            yield db

    DB = Annotated[Session, Depends(get_db)]

    @app.exception_handler(HTTPException)
    async def http_error(_request: Request, error: HTTPException) -> JSONResponse:
        code = {404: "not_found", 405: "method_not_allowed"}.get(error.status_code, "http_error")
        message = (
            error.detail
            if isinstance(error.detail, str)
            else "The local API could not complete this request."
        )
        return JSONResponse(
            status_code=error.status_code,
            content={"error": {"code": code, "message": message}},
            headers=error.headers,
        )

    @app.exception_handler(Exception)
    async def unexpected_error(_request: Request, error: Exception) -> JSONResponse:
        # Last-resort HTTP boundary logs the failure; it never exposes a traceback to clients.
        logger.error(
            "Unexpected local API failure; inspect server logs and app versions", exc_info=error
        )
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "code": "internal_error",
                    "message": "The local service failed. Check its logs, then retry.",
                }
            },
        )

    @app.exception_handler(services.DomainError)
    async def domain_error(_request: Request, error: services.DomainError) -> JSONResponse:
        return JSONResponse(
            status_code=error.status,
            content={"error": {"code": error.code, "message": error.message}},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_error(_request: Request, error: RequestValidationError) -> JSONResponse:
        details = [
            {"field": ".".join(str(x) for x in e["loc"]), "message": e["msg"]}
            for e in error.errors()
        ]
        return JSONResponse(
            status_code=422,
            content={
                "error": {
                    "code": "validation",
                    "message": "Check the request fields and retry.",
                    "details": details,
                }
            },
        )

    @app.exception_handler(SQLAlchemyError)
    async def database_error(_request: Request, error: SQLAlchemyError) -> JSONResponse:
        logger.error(
            "Database operation failed; check migrations and configured DB location", exc_info=error
        )
        return JSONResponse(
            status_code=503,
            content={
                "error": {
                    "code": "database_unavailable",
                    "message": "Database unavailable. Run migrations, then retry.",
                }
            },
        )

    @app.get("/api/v1/health", response_model=HealthOut)
    def health(db: DB) -> dict[str, object]:
        revision = db.execute(text("SELECT version_num FROM alembic_version")).scalar_one()
        if revision != expected_schema:
            raise services.DomainError(
                503,
                "migrations_required",
                "Database schema is out of date. Run migrations, then retry.",
            )
        return {
            "status": "ok",
            "database": "ready",
            "schema_version": revision,
            "qa_mode": config.qa_mode,
            "features": {"lessons": True},
        }

    @app.get("/api/v1/profile", response_model=ProfileOut)
    def profile(db: DB, timezone: str = "UTC") -> ProfileOut:
        try:
            detected_timezone = timezone_name(timezone)
        except ValueError as error:
            raise services.DomainError(422, "timezone", str(error)) from error
        return services.profile_out(services.local_profile(db, detected_timezone))

    @app.patch("/api/v1/profile", response_model=ProfileOut)
    def update_profile(patch: ProfilePatch, db: DB) -> ProfileOut:
        return services.patch_profile(db, patch)

    @app.get("/api/v1/settings", response_model=Settings)
    def settings(db: DB) -> Settings:
        return services.get_settings(db)

    @app.patch("/api/v1/settings", response_model=Settings)
    def update_settings(patch: SettingsPatch, db: DB) -> Settings:
        return services.patch_settings(db, patch)

    @app.get("/api/v1/courses", response_model=list[CourseSummary])
    def courses(db: DB) -> list[dict]:
        return services.list_courses(db)

    @app.get("/api/v1/courses/{course_id}", response_model=CourseMap)
    @app.get("/api/v1/courses/{course_id}/map", response_model=CourseMap)
    def course(course_id: str, db: DB) -> dict:
        return services.course_map(db, course_id)

    @app.post("/api/v1/courses/{course_id}/enrollment", response_model=EnrollmentOut)
    def enrollment(course_id: str, db: DB) -> dict:
        return services.enroll(db, course_id)

    @app.get("/api/v1/courses/{course_id}/lessons/{lesson_id}", response_model=PublicLesson)
    def lesson(course_id: str, lesson_id: str, db: DB) -> dict:
        _, content = services.current_content(db, course_id)
        return services.public_lesson(content, lesson_id)

    class AssistanceRequest(BaseModel):
        model_config = ConfigDict(extra="forbid")
        event_id: UUID
        action: Literal["hint", "reveal"]

    @app.post(
        "/api/v1/courses/{course_id}/exercises/{exercise_id}/assistance",
        response_model=AssistanceOut,
        response_model_exclude_none=True,
    )
    def assistance(course_id: str, exercise_id: str, body: AssistanceRequest, db: DB) -> dict:
        return services.reveal(db, course_id, exercise_id, str(body.event_id), body.action)

    @app.get("/api/v1/courses/{course_id}/library", response_model=LibraryOut)
    def library(course_id: str, db: DB) -> dict:
        _, content = services.current_content(db, course_id)
        return {
            "concepts": [c.model_dump() for c in content.concepts],
            "vocabulary": [v.model_dump() for v in content.vocabulary if v.status == "published"],
            "writing_tasks": [w.model_dump() for w in content.writing_tasks],
            "licenses": [item.model_dump() for item in content.licenses],
        }

    register_learning_routes(app, get_db)
    register_practice_routes(app, get_db)
    register_audio_routes(app, get_db, config)
    register_reading_routes(app, get_db)
    register_writing_routes(app, get_db)
    register_backup_routes(app, get_db, config)
    return app


app = create_app()
