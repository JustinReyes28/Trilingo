"""Preserve original quest definitions and explicit same-assignment fallback history."""

import sqlalchemy as sa
from alembic import op

revision = "0011"
down_revision = "0010"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "quest_assignments",
        sa.Column("original_kind", sa.String(), nullable=False, server_default="sessions"),
    )
    op.add_column(
        "quest_assignments", sa.Column("revision", sa.Integer(), nullable=False, server_default="0")
    )
    op.add_column(
        "quest_assignments",
        sa.Column("definition_history", sa.JSON(), nullable=False, server_default="[]"),
    )
    op.execute("UPDATE quest_assignments SET original_kind = kind")


def downgrade() -> None:
    with op.batch_alter_table("quest_assignments") as batch:
        batch.drop_column("definition_history")
        batch.drop_column("revision")
        batch.drop_column("original_kind")
