"""Version the additive speaking-evidence JSON contract without rewriting learner history.

New study writes may include speech attempts, transcript comparisons and typed
fallback counts. Existing evidence and immutable action receipts deliberately
remain byte-for-byte unchanged: API schemas supply explicit zero/null defaults
for absent fields. No old answer is reclassified as speech or pronunciation.
There are no relational column/index changes and no data backfill is needed.
"""

revision = "0013"
down_revision = "0012"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Advance the evidence contract; preserve all historical JSON and receipts."""


def downgrade() -> None:
    """Preserve additive evidence rather than delete a learner's transcripts."""
