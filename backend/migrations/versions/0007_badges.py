"""Durable evidence badges with timestamps; no XP or access changes."""

import sqlalchemy as sa
from alembic import op

revision = "0007"
down_revision = "0006"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "personal_badges",
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), primary_key=True),
        sa.Column("badge_id", sa.String(), primary_key=True),
        sa.Column("earned_at", sa.String(), nullable=False),
        sa.Column(
            "source_session_id", sa.String(), sa.ForeignKey("study_sessions.id"), nullable=False
        ),
        sa.Column("details", sa.JSON(), nullable=False),
    )
    # Backfill real first events without inventing a timestamp or changing progress.
    for badge_id, source in [
        ("first-session", None),
        ("first-review", "review"),
        ("first-composition", "writing"),
    ]:
        condition = "" if source is None else " AND s.source_kind = :source"
        op.get_bind().execute(
            sa.text(
                """
            INSERT INTO personal_badges
                (profile_id, badge_id, earned_at, source_session_id, details)
            SELECT profile_id, :badge, occurred_at, session_id, '{}' FROM (
                SELECT x.profile_id, x.occurred_at, x.session_id,
                    ROW_NUMBER() OVER (
                        PARTITION BY x.profile_id ORDER BY x.occurred_at, x.id
                    ) AS position
                FROM xp_ledger x
                JOIN study_sessions s ON s.id = x.session_id
                WHERE s.status = 'completed'
            """
                + condition
                + ") WHERE position = 1"
            ),
            {"badge": badge_id, "source": source},
        )


def downgrade() -> None:
    op.drop_table("personal_badges")
