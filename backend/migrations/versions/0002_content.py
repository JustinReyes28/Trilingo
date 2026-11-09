"""Immutable course versions, enrollments, and explicit assistance evidence."""

import sqlalchemy as sa
from alembic import op

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "courses",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("current_version", sa.String(), nullable=False),
    )
    op.create_table(
        "course_versions",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("course_id", sa.String(), sa.ForeignKey("courses.id"), nullable=False),
        sa.Column("version", sa.String(), nullable=False),
        sa.Column("digest", sa.String(), nullable=False),
        sa.Column("data", sa.JSON(), nullable=False),
        sa.UniqueConstraint("course_id", "version"),
    )
    op.create_index("ix_course_versions_course_id", "course_versions", ["course_id"])
    op.create_table(
        "enrollments",
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), primary_key=True),
        sa.Column("course_id", sa.String(), sa.ForeignKey("courses.id"), primary_key=True),
    )
    op.create_table(
        "content_assistance",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), nullable=False),
        sa.Column(
            "course_version_id", sa.String(), sa.ForeignKey("course_versions.id"), nullable=False
        ),
        sa.Column("exercise_id", sa.String(), nullable=False),
        sa.Column("action", sa.String(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("content_assistance")
    op.drop_table("enrollments")
    op.drop_index("ix_course_versions_course_id", "course_versions")
    op.drop_table("course_versions")
    op.drop_table("courses")
