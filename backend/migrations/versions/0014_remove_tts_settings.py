"""Remove deprecated runtime TTS and provider voice keys from preferences.

Preserves all learner progress, XP, FSRS schedules, study sessions, collections,
and writing drafts. Existing AI and STT provider configs stay intact minus any
legacy voice field.
"""

import json

import sqlalchemy as sa
from alembic import op

revision = "0014"
down_revision = "0013"
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
    if "tts" in data:
        del data["tts"]
        changed = True
    for key in ("ai", "stt"):
        provider = data.get(key)
        if isinstance(provider, dict) and "voice" in provider:
            cleaned = dict(provider)
            del cleaned["voice"]
            data[key] = cleaned
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
    """Preserve cleaned preferences rather than inventing removed TTS configs."""
