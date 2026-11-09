"""Add actual FSRS state/logs and optional quest assignments; no progress rewrite."""

import sqlalchemy as sa
from alembic import op

revision = "0006"
down_revision = "0005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "review_cards",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), nullable=False),
        sa.Column("course_id", sa.String(), sa.ForeignKey("courses.id"), nullable=False),
        sa.Column(
            "course_version_id", sa.String(), sa.ForeignKey("course_versions.id"), nullable=False
        ),
        sa.Column("item_id", sa.String(), nullable=False),
        sa.Column("direction", sa.String(), nullable=False),
        sa.Column("state", sa.JSON(), nullable=False),
        sa.Column("due", sa.String(), nullable=True),
        sa.Column("revision", sa.Integer(), nullable=False),
        sa.Column("scheduler", sa.JSON(), nullable=False),
        sa.UniqueConstraint("profile_id", "course_id", "item_id", "direction"),
    )
    op.create_index("ix_review_cards_due", "review_cards", ["due"])
    op.create_table(
        "review_events",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("card_id", sa.String(), sa.ForeignKey("review_cards.id"), nullable=False),
        sa.Column("request", sa.JSON(), nullable=False),
        sa.Column("response", sa.JSON(), nullable=False),
        sa.Column("transition", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )
    op.create_index("ix_review_events_card_id", "review_events", ["card_id"])
    op.create_table(
        "quest_assignments",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), nullable=False),
        sa.Column("kind", sa.String(), nullable=False),
        sa.Column("target", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
        sa.Column("baseline_ids", sa.JSON(), nullable=False),
        sa.Column("completed_at", sa.String(), nullable=True),
        sa.Column("source_ids", sa.JSON(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("quest_assignments")
    op.drop_index("ix_review_events_card_id", "review_events")
    op.drop_table("review_events")
    op.drop_index("ix_review_cards_due", "review_cards")
    op.drop_table("review_cards")
