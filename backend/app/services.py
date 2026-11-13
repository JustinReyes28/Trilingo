import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from app.content_schema import CourseContent, Exercise
from app.models import Assistance, Course, CourseVersion, Enrollment, Preferences, Profile
from app.schemas import ProfileOut, ProfilePatch, Settings, SettingsPatch


class DomainError(Exception):
    def __init__(self, status: int, code: str, message: str):
        self.status, self.code, self.message = status, code, message


def local_profile(db: Session, detected_timezone: str = "UTC") -> Profile:
    profile = db.get(Profile, "local")
    if profile is None:
        # Atomic first-use setup is safe when two browser tabs connect together.
        db.execute(
            insert(Profile)
            .values(id="local", name="Learner", timezone=detected_timezone)
            .on_conflict_do_nothing(index_elements=["id"])
        )
        db.execute(
            insert(Preferences)
            .values(profile_id="local", data=Settings().model_dump())
            .on_conflict_do_nothing(index_elements=["profile_id"])
        )
        db.commit()
        profile = db.get(Profile, "local")
        assert profile is not None
    return profile


def profile_out(profile: Profile) -> ProfileOut:
    return ProfileOut(id=profile.id, name=profile.name, timezone=profile.timezone)


def patch_profile(db: Session, patch: ProfilePatch) -> ProfileOut:
    profile = local_profile(db)
    for key, value in patch.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(profile, key, value)
    db.commit()
    return profile_out(profile)


def _normalize_settings_data(raw: dict) -> dict:
    """Return a copied settings mapping with deprecated TTS/voice keys removed."""
    data = dict(raw)
    data.pop("tts", None)
    for key in ("ai", "stt"):
        provider = data.get(key)
        if isinstance(provider, dict) and "voice" in provider:
            cleaned = dict(provider)
            cleaned.pop("voice", None)
            data[key] = cleaned
    return data


def get_settings(db: Session) -> Settings:
    profile = local_profile(db)
    prefs = db.get(Preferences, profile.id)
    assert prefs is not None
    return Settings.model_validate(_normalize_settings_data(prefs.data))


def patch_settings(db: Session, patch: SettingsPatch) -> Settings:
    settings = get_settings(db)
    value = Settings.model_validate(
        _normalize_settings_data(
            {**settings.model_dump(), **patch.model_dump(exclude_unset=True)}
        )
    )
    prefs = db.get(Preferences, "local")
    assert prefs is not None
    prefs.data = value.model_dump()
    db.commit()
    return value


def load_content(filename: Path) -> CourseContent:
    content = CourseContent.model_validate_json(filename.read_text(encoding="utf-8"))
    directory = filename.parent.resolve()
    for asset in content.assets:
        resolved = (directory / asset.path).resolve()
        if not resolved.is_relative_to(directory) or not resolved.is_file():
            raise ValueError(f"{asset.id}: missing asset or path outside content directory")
        if asset.sha256 and hashlib.sha256(resolved.read_bytes()).hexdigest() != asset.sha256:
            raise ValueError(f"{asset.id}: asset digest differs from the versioned manifest")
    return content


def import_content(db: Session, content: CourseContent) -> bool:
    data = content.model_dump(mode="json")
    digest = hashlib.sha256(
        json.dumps(data, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()
    revision_id = f"{content.id}@{content.version}"
    existing = db.get(CourseVersion, revision_id)
    if existing:
        if existing.digest != digest:
            # Additive schema defaults may change canonical serialization of an old snapshot.
            # Compare validated semantics without rewriting its original data or digest.
            if CourseContent.model_validate(existing.data).model_dump(mode="json") == data:
                return False
            raise DomainError(
                409,
                "immutable_version",
                "Content changed: increment the content version before importing.",
            )
        return False
    course = db.get(Course, content.id)
    if course is None:
        course = Course(id=content.id, current_version=content.version)
        db.add(course)
        db.flush()
    else:
        if tuple(map(int, content.version.split("."))) <= tuple(
            map(int, course.current_version.split("."))
        ):
            raise DomainError(
                409,
                "older_version",
                "Import a newer content version; historical versions are preserved.",
            )
        course.current_version = content.version
    db.add(
        CourseVersion(
            id=revision_id, course_id=content.id, version=content.version, digest=digest, data=data
        )
    )
    db.commit()
    return True


def current_content(db: Session, course_id: str) -> tuple[CourseVersion, CourseContent]:
    course = db.get(Course, course_id)
    if course is None:
        raise DomainError(
            404, "course_missing", "Course not found. Import the starter course, then retry."
        )
    version = db.get(CourseVersion, f"{course.id}@{course.current_version}")
    assert version is not None
    content = CourseContent.model_validate(version.data)
    if content.status != "published":
        raise DomainError(404, "unpublished", "This course has not been published.")
    return version, content


def public_exercise(exercise: Exercise) -> dict:
    data = exercise.model_dump(
        exclude={"answer", "answers", "explanation", "hint", "response_feedback"}
    )
    if hasattr(exercise, "audio"):
        data["audio"] = [{"id": cue.id, "label": cue.label} for cue in exercise.audio]
    if exercise.type == "speaking":
        data["reference_text"] = exercise.audio[0].transcript
    return data


def public_lesson(content: CourseContent, lesson_id: str) -> dict:
    for unit in content.units:
        for lesson in unit.lessons:
            if lesson.id == lesson_id and unit.status == lesson.status == "published":
                return {
                    **lesson.model_dump(exclude={"exercises"}),
                    "exercises": [public_exercise(e) for e in lesson.exercises],
                }
    raise DomainError(
        404,
        "lesson_missing",
        "This lesson is missing or not yet published. Choose another published lesson.",
    )


def _published_exercise(content: CourseContent, exercise_id: str) -> Exercise:
    exercise = next(
        (
            exercise
            for unit in content.units
            if unit.status == "published"
            for lesson in unit.lessons
            if lesson.status == "published"
            for exercise in lesson.exercises
            if exercise.id == exercise_id
        ),
        None,
    )
    if exercise is None:
        raise DomainError(404, "exercise_missing", "Published exercise not found.")
    return exercise


def _assistance_result(
    db: Session, record: Assistance, course_id: str, exercise_id: str, action: str
) -> dict:
    version = db.get(CourseVersion, record.course_version_id)
    if (
        version is None
        or version.course_id != course_id
        or record.profile_id != "local"
        or record.exercise_id != exercise_id
        or record.action != action
    ):
        raise DomainError(
            409, "event_conflict", "Use a new event ID for a different assistance request."
        )
    # Re-delivery uses the original immutable content, even after a course update.
    exercise = _published_exercise(CourseContent.model_validate(version.data), exercise_id)
    data = {
        "exercise_id": exercise_id,
        "action": action,
        "evidence": "assisted",
        "hint": exercise.hint,
    }
    if action == "reveal":
        data.update(
            answer=getattr(exercise, "answer", getattr(exercise, "answers", [])),
            explanation=exercise.explanation,
        )
    return data


def reveal(db: Session, course_id: str, exercise_id: str, event_id: str, action: str) -> dict:
    existing = db.get(Assistance, event_id)
    if existing:
        return _assistance_result(db, existing, course_id, exercise_id, action)
    version, content = current_content(db, course_id)
    _published_exercise(content, exercise_id)
    local_profile(db)
    db.execute(
        insert(Assistance)
        .values(
            id=event_id,
            profile_id="local",
            course_version_id=version.id,
            exercise_id=exercise_id,
            action=action,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        .on_conflict_do_nothing(index_elements=["id"])
    )
    db.commit()
    record = db.get(Assistance, event_id)
    assert record is not None
    return _assistance_result(db, record, course_id, exercise_id, action)


def enroll(db: Session, course_id: str) -> dict:
    current_content(db, course_id)
    local_profile(db)
    db.execute(
        insert(Enrollment)
        .values(profile_id="local", course_id=course_id)
        .on_conflict_do_nothing(index_elements=["profile_id", "course_id"])
    )
    db.commit()
    return {"course_id": course_id, "enrolled": True}


def list_courses(db: Session) -> list[dict]:
    rows = (
        db.execute(
            select(CourseVersion).join(
                Course,
                (Course.id == CourseVersion.course_id)
                & (Course.current_version == CourseVersion.version),
            )
        )
        .scalars()
        .all()
    )
    return [
        {
            k: row.data[k]
            for k in ("id", "title", "language", "teaching_language", "description", "version")
        }
        for row in rows
        if row.data["status"] == "published"
    ]


def course_map(db: Session, course_id: str) -> dict:
    from app.learning import study_states

    _, content = current_content(db, course_id)
    states = study_states(db, course_id)
    return {
        "id": content.id,
        "title": content.title,
        "version": content.version,
        "description": content.description,
        "review_note": content.review_note,
        "stages": [s.model_dump() for s in content.stages],
        "units": [
            {
                **u.model_dump(exclude={"lessons"}),
                "lessons": [
                    {
                        **lesson.model_dump(exclude={"exercises"}),
                        "exercise_count": len(lesson.exercises),
                        "available": u.status == lesson.status == "published",
                        "study_state": states.get(lesson.id, "not_started"),
                    }
                    for lesson in sorted(u.lessons, key=lambda item: item.order)
                ],
            }
            for u in sorted(content.units, key=lambda item: item.order)
        ],
        "inventory": {
            "published_words": sum(
                v.status == "published" and v.entry_kind == "word" for v in content.vocabulary
            ),
            "published_phrases": sum(
                v.status == "published" and v.entry_kind == "phrase" for v in content.vocabulary
            ),
            "published_kanji": len(
                {
                    char
                    for v in content.vocabulary
                    if v.status == "published"
                    for char in v.surface
                    if "\u4e00" <= char <= "\u9fff"
                }
            ),
            "published_lessons": sum(
                lesson.status == u.status == "published"
                for u in content.units
                for lesson in u.lessons
            ),
            "target_words": sum(
                s.word_target for s in content.stages if s.release == content.stages[0].release
            ),
            "target_kanji": sum(
                s.kanji_target for s in content.stages if s.release == content.stages[0].release
            ),
            "coverage": "partial_starter_slice",
        },
    }
