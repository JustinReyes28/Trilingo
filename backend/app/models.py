from sqlalchemy import JSON, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Profile(Base):
    __tablename__ = "profiles"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    timezone: Mapped[str] = mapped_column(String)


class Preferences(Base):
    __tablename__ = "preferences"
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), primary_key=True)
    data: Mapped[dict] = mapped_column(JSON)


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    current_version: Mapped[str] = mapped_column(String)


class CourseVersion(Base):
    __tablename__ = "course_versions"
    __table_args__ = (UniqueConstraint("course_id", "version"),)
    id: Mapped[str] = mapped_column(String, primary_key=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), index=True)
    version: Mapped[str] = mapped_column(String)
    digest: Mapped[str] = mapped_column(String)
    data: Mapped[dict] = mapped_column(JSON)


class Enrollment(Base):
    __tablename__ = "enrollments"
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"), primary_key=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("courses.id"), primary_key=True)


class Assistance(Base):
    __tablename__ = "content_assistance"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_id: Mapped[str] = mapped_column(ForeignKey("profiles.id"))
    course_version_id: Mapped[str] = mapped_column(ForeignKey("course_versions.id"))
    exercise_id: Mapped[str] = mapped_column(String)
    action: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)
