"""Optional server-recorded active time. It never expires or fails study."""

from datetime import datetime

from app.learning_models import StudySession


def freeze(metadata: dict, now: datetime, *, pause: bool = False) -> None:
    timer = metadata.get("timer")
    if timer is None:
        return
    if timer.get("paused_since") is not None:
        delta = (now - datetime.fromisoformat(timer["paused_since"])).total_seconds()
        if delta < 0:
            timer["valid"] = False
        elif timer.get("paused_seconds") is not None:
            timer["paused_seconds"] += delta
    if timer["active_since"] is not None:
        delta = (now - datetime.fromisoformat(timer["active_since"])).total_seconds()
        if delta < 0:
            timer["valid"] = False
        else:
            timer["elapsed_seconds"] += delta
    timer["active_since"] = None
    timer["paused_since"] = now.isoformat() if pause else None


def act(metadata: dict, action: str, now: datetime) -> None:
    if "timer" not in metadata:
        metadata["timer"] = {
            "visible": True,
            "active_since": None,
            "elapsed_seconds": 0.0,
            "paused_seconds": 0.0,
            "paused_since": None,
            "valid": True,
        }
    timer = metadata["timer"]
    if action == "timer_pause":
        freeze(metadata, now, pause=True)
    elif action in {"timer_start", "timer_resume"}:
        if timer["active_since"] is None:
            freeze(metadata, now)
            timer["active_since"] = now.isoformat()
        timer["visible"] = True
    elif action == "timer_hide":
        timer["visible"] = False
    elif action == "timer_show":
        timer["visible"] = True


def view(row: StudySession, now: datetime) -> dict | None:
    timer = row.metadata_json.get("timer")
    if timer is None:
        return None
    elapsed = timer["elapsed_seconds"]
    valid = timer["valid"]
    if timer["active_since"]:
        delta = (now - datetime.fromisoformat(timer["active_since"])).total_seconds()
        valid = valid and delta >= 0
        elapsed += max(delta, 0)
    return {
        "visible": timer["visible"],
        "running": timer["active_since"] is not None,
        "elapsed_seconds": elapsed,
        "valid": valid,
    }
