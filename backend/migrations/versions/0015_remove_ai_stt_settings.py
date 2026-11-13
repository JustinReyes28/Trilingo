"""Remove deprecated AI, STT, and TTS provider keys from preferences.

Preserves all learner progress, XP, FSRS schedules, study sessions, study events,
review cards, review events, quests, badges, collections, writing drafts,
handwriting samples, and audio deliveries untouched.
"""

import json

import sqlalchemy as sa
from alembic import op

revision = "0015"
down_revision = "0014"
branch_labels = None
depends_on = None


def _clean_preferences(raw: object) -> tuple[dict, bool]:
    if isinstance(raw, str):
        data = json.loads(raw)
    elif isinstance(raw, dict):
        data = dict(raw)
    else:
        return {}, False
    if not isinstance(data, dict):
        return {}, False

    changed = False
    for key in ("ai", "stt", "tts"):
        if key in data:
            del data[key]
            changed = True
    return data, changed


def upgrade() -> None:
    conn = op.get_bind()
    rows = conn.execute(sa.text("SELECT profile_id, data FROM preferences")).fetchall()
    for profile_id, raw_data in rows:
        cleaned, changed = _clean_preferences(raw_data)
        if changed:
            conn.execute(
                sa.text("UPDATE preferences SET data = :data WHERE profile_id = :profile_id"),
                {"data": json.dumps(cleaned), "profile_id": profile_id},
            )


def downgrade() -> None:
    """Preserve cleaned preferences rather than inventing removed provider configs."""
