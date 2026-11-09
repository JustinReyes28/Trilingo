"""Saved difficult reading items and explicitly self-reported familiarity."""

import sqlalchemy as sa
from alembic import op

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "reading_items",
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), primary_key=True),
        sa.Column("course_id", sa.String(), sa.ForeignKey("courses.id"), primary_key=True),
        sa.Column("item_kind", sa.String(), primary_key=True),
        sa.Column("item_id", sa.String(), primary_key=True),
        sa.Column(
            "course_version_id", sa.String(), sa.ForeignKey("course_versions.id"), nullable=False
        ),
        sa.Column("saved", sa.Boolean(), nullable=False),
        sa.Column("familiar", sa.Boolean(), nullable=False),
        sa.Column("updated_at", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("reading_items")
