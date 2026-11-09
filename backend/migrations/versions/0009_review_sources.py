"""Distinguish vocabulary and historical exercise recall; existing cards remain words."""

import sqlalchemy as sa
from alembic import op

revision = "0009"
down_revision = "0008"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "review_cards", sa.Column("item_kind", sa.String(), nullable=False, server_default="word")
    )


def downgrade() -> None:
    with op.batch_alter_table("review_cards") as batch:
        batch.drop_column("item_kind")
