"""Named vocabulary collections; word snapshots preserve historical references."""

import sqlalchemy as sa
from alembic import op

revision = "0008"
down_revision = "0007"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "vocabulary_collections",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("profile_id", sa.String(), sa.ForeignKey("profiles.id"), nullable=False),
        sa.Column("course_id", sa.String(), sa.ForeignKey("courses.id"), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )
    op.create_index(
        "ix_vocabulary_collections_profile_id", "vocabulary_collections", ["profile_id"]
    )
    op.create_table(
        "collection_members",
        sa.Column(
            "collection_id",
            sa.String(),
            sa.ForeignKey("vocabulary_collections.id"),
            primary_key=True,
        ),
        sa.Column("item_id", sa.String(), primary_key=True),
        sa.Column(
            "course_version_id", sa.String(), sa.ForeignKey("course_versions.id"), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_table("collection_members")
    op.drop_index("ix_vocabulary_collections_profile_id", "vocabulary_collections")
    op.drop_table("vocabulary_collections")
