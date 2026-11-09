"""Durable reference delivery receipts; additive exercise evidence remains backwards compatible."""

import sqlalchemy as sa
from alembic import op

revision = "0010"
down_revision = "0009"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "audio_deliveries",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("session_id", sa.String(), sa.ForeignKey("study_sessions.id"), nullable=False),
        sa.Column("request", sa.JSON(), nullable=False),
        sa.Column("provider", sa.JSON(), nullable=False),
        sa.Column("cue", sa.JSON(), nullable=False),
        sa.Column("result", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )
    op.create_index("ix_audio_deliveries_session_id", "audio_deliveries", ["session_id"])


def downgrade() -> None:
    op.drop_index("ix_audio_deliveries_session_id", "audio_deliveries")
    op.drop_table("audio_deliveries")
