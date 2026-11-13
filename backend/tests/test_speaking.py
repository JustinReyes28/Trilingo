import json
from datetime import datetime, timezone
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select
from test_learning import act, action_body, complete, start
from test_learning import course as course
from test_listening import audio

from app.config import ROOT, Config
from app.content_schema import CourseContent
from app.db import sessions
from app.learning_models import StudyEvent, StudySession, XpEntry
from app.main import create_app
from app.review_models import QuestAssignment
from app.services import import_content, load_content

pytestmark = pytest.mark.usefixtures("course")


def speaking(client: TestClient) -> dict:
    return start(client, "dialogue-food", source_kind="speaking", preview_draft=True)


def test_speaking_typed_practice_skip_reveal_finish_replay_and_removed_speech_endpoint(
    client: TestClient,
) -> None:
    draft_guard = client.post(
        "/api/v1/courses/ja-starter/sessions",
        json={
            "request_id": str(uuid4()),
            "source_kind": "speaking",
            "source_id": "dialogue-food",
        },
    )
    assert draft_guard.status_code == 404

    quest_rejected = client.post(
        "/api/v1/quests",
        json={"request_id": str(uuid4()), "kind": "speaking", "target": 2},
    )
    assert quest_rejected.status_code == 422

    session = speaking(client)
    assert session["source_kind"] == "speaking"
    assert "pronunciation_override" not in str(session["exercises"])
    first = session["exercises"][0]
    second = session["exercises"][1]
    assert first["type"] == "speaking"
    assert first["reference_text"] == "水をください。"
    assert second["type"] == "speaking"

    removed_speech = client.post(
        f"/api/v1/sessions/{session['id']}/exercises/{first['id']}/speech",
        json={"expected_revision": session["revision"], "transcript": first["reference_text"]},
    )
    assert removed_speech.status_code == 404

    empty_answer = client.post(
        f"/api/v1/sessions/{session['id']}/actions",
        json=action_body(session, "answer", first["id"], answer="   "),
    )
    assert empty_answer.status_code == 422

    hinted = act(client, session, "hint", first["id"])
    assert hinted["feedback"]["kind"] == "hint"

    text_alt = act(client, hinted, "audio_text", first["id"])
    assert text_alt["feedback"]["kind"] == "hint"
    assert "Text alternative" in text_alt["feedback"]["message"]

    answered = act(client, text_alt, "answer", first["id"], answer=first["reference_text"])
    assert answered["feedback"]["kind"] == "recorded"
    assert answered["feedback"]["message"] == "Typed practice saved. Pronunciation is not assessed."
    assert answered["evidence"][first["id"]]["typed_fallbacks"] == 1
    assert answered["evidence"][first["id"]]["speech_attempts"] == 0

    revealed = act(client, answered, "reveal", second["id"])
    assert revealed["feedback"]["kind"] == "reveal"
    assert revealed["feedback"]["answer"] == second["reference_text"]

    skipped = act(client, revealed, "skip", second["id"])
    assert skipped["feedback"] is None
    assert skipped["evidence"][second["id"]]["skipped"] is True

    paused = act(client, skipped, "pause")
    assert paused["status"] == "paused"

    fetched = client.get(f"/api/v1/sessions/{paused['id']}").json()
    resumed = act(client, fetched, "resume")
    assert resumed["status"] == "active"

    finish_body = action_body(resumed, "finish")
    first_finish_res = client.post(f"/api/v1/sessions/{resumed['id']}/actions", json=finish_body)
    assert first_finish_res.status_code == 200, first_finish_res.text
    finished = first_finish_res.json()
    assert finished["status"] == "completed"
    assert finished["xp_awarded"] == 5

    duplicate_finish = client.post(f"/api/v1/sessions/{resumed['id']}/actions", json=finish_body)
    assert duplicate_finish.status_code == 200
    assert duplicate_finish.json() == finished

    replay = speaking(client)
    assert replay["id"] != session["id"]
    replay_ex0 = replay["exercises"][0]
    replay_ex1 = replay["exercises"][1]
    replay = act(client, replay, "answer", replay_ex0["id"], answer=replay_ex0["reference_text"])
    replay = act(client, replay, "answer", replay_ex1["id"], answer=replay_ex1["reference_text"])
    replay_finished = act(client, replay, "finish")
    assert replay_finished["xp_awarded"] == 5

    personal = client.get("/api/v1/personal")
    assert personal.status_code == 200
    speaking_summary = personal.json()["skill_evidence"]["speaking"]
    assert speaking_summary["typed_fallbacks"] >= 3
    assert speaking_summary["speech_attempts"] == 0

    with sessions(client.app.state.engine)() as db:
        row = db.get(StudySession, session["id"])
        assert row is not None
        assert row.metadata_json["evidence_mode"] == (
            "speaking practice; authored audio model and typed practice; "
            "pronunciation unassessed"
        )
        xp_rows = db.execute(select(XpEntry).order_by(XpEntry.occurred_at)).scalars().all()
        assert sum(entry.amount for entry in xp_rows) == 10
        events = db.execute(select(StudyEvent)).scalars().all()
        assert len(events) > 0


def test_speaking_bundled_audio_playback_and_snapshot_isolation(
    database, fixture_audio_pack
) -> None:
    course_data = json.loads(
        (ROOT / "content" / "courses" / "ja" / "starter.json").read_text(encoding="utf-8")
    )

    with TestClient(
        create_app(
            Config(
                database_url=database,
                audio_pack_dir=fixture_audio_pack,
                audio_pack_enabled=True,
            )
        )
    ) as enabled:
        with sessions(enabled.app.state.engine)() as db:
            import_content(db, load_content(ROOT / "content" / "courses" / "ja" / "starter.json"))

        session = speaking(enabled)
        first = session["exercises"][0]
        original_reference = first["reference_text"]
        original_prompt = first["prompt"]

        # Re-import modified version to verify session snapshot isolation.
        for item in course_data.get("practice_exercises", []):
            if item["id"] == first["id"]:
                item["audio"][0]["transcript"] = "お茶をください。"
                item["prompt"] = "Changed prompt"
        course_data["version"] = "0.1.99"
        with sessions(enabled.app.state.engine)() as db:
            import_content(db, CourseContent.model_validate(course_data))

        request_body = {
            "request_id": str(uuid4()),
            "expected_revision": session["revision"],
            "speed": 1,
        }
        played_res = audio(
            enabled, session, cue="reference", exercise=first["id"], body=request_body
        )
        assert played_res.status_code == 200, played_res.text
        played_body = played_res.json()
        assert played_body["source"] == "pack"
        assert played_body["mime"] == "audio/mpeg"
        played = played_body["session"]
        assert played["evidence"][first["id"]]["audio_cue_ids"] == ["reference"]
        assert played["evidence"][first["id"]]["speech_reference_delivered"] is False

        retried = audio(enabled, session, cue="reference", exercise=first["id"], body=request_body)
        assert retried.status_code == 200
        assert retried.json()["session"] == played

        stale = audio(
            enabled,
            session,
            cue="reference",
            exercise=first["id"],
            body={"request_id": str(uuid4()), "expected_revision": session["revision"], "speed": 1},
        )
        assert stale.status_code == 409

        replayed_cue = audio(enabled, played, cue="reference", exercise=first["id"])
        assert replayed_cue.status_code == 200
        replayed_session = replayed_cue.json()["session"]
        assert replayed_session["revision"] == played["revision"] + 1
        assert replayed_session["exercises"][0]["prompt"] == original_prompt
        assert replayed_session["exercises"][0]["reference_text"] == original_reference


def test_pre_upgrade_speaking_quest_can_still_fallback_to_sessions(client: TestClient) -> None:
    assert client.get("/api/v1/profile").status_code == 200
    quest_id = str(uuid4())
    with sessions(client.app.state.engine)() as db:
        db.add(
            QuestAssignment(
                id=quest_id,
                profile_id="local",
                kind="speaking",
                original_kind="speaking",
                target=1,
                created_at=datetime.now(timezone.utc).isoformat(),
                baseline_ids=[],
                completed_at=None,
                source_ids=[],
            )
        )
        db.commit()

    session = speaking(client)
    ex0 = session["exercises"][0]
    ex1 = session["exercises"][1]
    session = act(client, session, "answer", ex0["id"], answer=ex0["reference_text"])
    session = act(client, session, "answer", ex1["id"], answer=ex1["reference_text"])
    act(client, session, "finish")

    before = client.get("/api/v1/quests").json()[0]
    assert before["kind"] == "speaking"
    assert before["progress"] == 0

    fallback_body = {"request_id": str(uuid4()), "expected_revision": before["revision"]}
    switched = client.post(f"/api/v1/quests/{quest_id}/fallback", json=fallback_body)
    assert switched.status_code == 200, switched.text
    assert switched.json()["kind"] == "sessions"

    switched_again = client.post(f"/api/v1/quests/{quest_id}/fallback", json=fallback_body)
    assert switched_again.status_code == 200
    assert switched_again.json() == switched.json()

    conflict = client.post(
        f"/api/v1/quests/{quest_id}/fallback",
        json={"request_id": str(uuid4()), "expected_revision": before["revision"]},
    )
    assert conflict.status_code == 409

    complete(client)

    after = client.get("/api/v1/quests").json()[0]
    assert after["kind"] == "sessions"
    assert after["progress"] == 1
    assert after["completed_at"] is not None

    already_completed = client.post(
        f"/api/v1/quests/{quest_id}/fallback",
        json={"request_id": str(uuid4()), "expected_revision": after["revision"]},
    )
    assert already_completed.status_code == 409
