"""Durable sessions, immutable action receipts, mistakes and XP/activity ledger."""

import sqlalchemy as sa
from alembic import op

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "study_sessions",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), nullable=False),
        sa.Column(
            "course_version_id", sa.String(), sa.ForeignKey("course_versions.id"), nullable=False
        ),
        sa.Column("course_id", sa.String(), sa.ForeignKey("courses.id"), nullable=False),
        sa.Column("source_kind", sa.String(), nullable=False),
        sa.Column("source_id", sa.String(), nullable=False),
        sa.Column("kind", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("cursor", sa.Integer(), nullable=False),
        sa.Column("revision", sa.Integer(), nullable=False),
        sa.Column("next_action_id", sa.String(), nullable=False),
        sa.Column("exercise_ids", sa.JSON(), nullable=False),
        sa.Column("evidence", sa.JSON(), nullable=False),
        sa.Column("metadata_json", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
        sa.Column("completed_at", sa.String(), nullable=True),
    )
    op.create_index("ix_study_sessions_profile_id", "study_sessions", ["profile_id"])
    op.create_index("ix_study_sessions_course_id", "study_sessions", ["course_id"])
    op.create_table(
        "study_events",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("request_id", sa.String(), nullable=False, unique=True),
        sa.Column("session_id", sa.String(), sa.ForeignKey("study_sessions.id"), nullable=False),
        sa.Column("request", sa.JSON(), nullable=False),
        sa.Column("response", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )
    op.create_index("ix_study_events_session_id", "study_events", ["session_id"])
    op.create_table(
        "xp_ledger",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column(
            "session_id",
            sa.String(),
            sa.ForeignKey("study_sessions.id"),
            unique=True,
            nullable=False,
        ),
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("occurred_at", sa.String(), nullable=False),
        sa.Column("activity_date", sa.String(), nullable=False),
        sa.Column("timezone", sa.String(), nullable=False),
    )
    op.create_index("ix_xp_ledger_profile_id", "xp_ledger", ["profile_id"])
    op.create_index("ix_xp_ledger_activity_date", "xp_ledger", ["activity_date"])
    op.create_table(
        "study_mistakes",
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), primary_key=True),
        sa.Column("course_id", sa.String(), sa.ForeignKey("courses.id"), primary_key=True),
        sa.Column("exercise_id", sa.String(), primary_key=True),
        sa.Column(
            "course_version_id", sa.String(), sa.ForeignKey("course_versions.id"), nullable=False
        ),
        sa.Column(
            "last_session_id", sa.String(), sa.ForeignKey("study_sessions.id"), nullable=False
        ),
        sa.Column("occurrences", sa.Integer(), nullable=False),
        sa.Column("updated_at", sa.String(), nullable=False),
    )


def downgrade() -> None:
    # Explicit downgrade only; normal startup never drops learning records.
    op.drop_table("study_mistakes")
    op.drop_index("ix_xp_ledger_activity_date", "xp_ledger")
    op.drop_index("ix_xp_ledger_profile_id", "xp_ledger")
    op.drop_table("xp_ledger")
    op.drop_index("ix_study_events_session_id", "study_events")
    op.drop_table("study_events")
    op.drop_index("ix_study_sessions_course_id", "study_sessions")
    op.drop_index("ix_study_sessions_profile_id", "study_sessions")
    op.drop_table("study_sessions")
