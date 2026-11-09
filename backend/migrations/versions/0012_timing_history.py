"""Index complete timing history; new timers also retain optional paused intervals.

Historical timer JSON and immutable receipts remain unchanged. Absence of
paused_seconds means unknown, never zero; no duration is inferred or backfilled.
"""

from alembic import op

revision = "0012"
down_revision = "0011"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(
        "ix_study_timing_history", "study_sessions", ["profile_id", "status", "completed_at", "id"]
    )


def downgrade() -> None:
    op.drop_index("ix_study_timing_history", table_name="study_sessions")
