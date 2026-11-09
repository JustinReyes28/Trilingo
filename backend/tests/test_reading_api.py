from concurrent.futures import ThreadPoolExecutor

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import func, select
from test_learning import act, complete, skip_all, start
from test_learning import course as course

from app.config import Config
from app.db import sessions
from app.main import create_app
from app.reading_models import ReadingItem

pytestmark = pytest.mark.usefixtures("course")


def test_reading_library_requires_explicit_draft_preview(client):
    base = "/api/v1/courses/ja-starter/reading"
    ordinary = client.get(base).json()
    assert ordinary["characters"] == [] and ordinary["stories"] == []
    assert not ordinary["includes_drafts"]
    assert ordinary["inventory"]["published_characters"] == 0
    preview = client.get(base + "?include_drafts=true").json()
    assert preview["includes_drafts"]
    assert preview["inventory"]["basic_hiragana"] == 46
    assert preview["inventory"]["basic_katakana"] == 46
    assert preview["inventory"]["target_kanji"] == 300
    assert preview["inventory"]["published_kanji"] == 0
    assert len(preview["characters"]) == 227 + preview["inventory"]["authored_kanji"]
    assert preview["inventory"]["authored_kanji"] == 300
    assert all(item["status"] == "draft" for item in preview["characters"])
    assert all(not {"answer", "answers"} & item.keys() for item in preview["characters"])


def test_saved_familiar_items_are_self_reported_persisted_and_reward_nothing(
    client, course, database
):
    url = "/api/v1/courses/ja-starter/reading/items/character/ja-char-a"
    assert client.patch(url, json={"saved": True}).status_code == 404
    body = {"saved": True, "familiar": True, "preview_draft": True}
    for _ in range(3):
        response = client.patch(url, json=body)
        assert response.status_code == 200
        assert response.json()["evidence"] == "self_reported"
    assert client.get("/api/v1/progress").json()["total_xp"] == 0
    client.patch("/api/v1/settings", json={"furigana": "unfamiliar", "romaji": False})
    with TestClient(create_app(Config(database_url=database))) as restarted:
        value = restarted.get("/api/v1/courses/ja-starter/reading?include_drafts=true").json()
        assert value["items"][0]["saved"] and value["items"][0]["familiar"]
        assert restarted.get("/api/v1/settings").json()["furigana"] == "unfamiliar"
        assert restarted.get("/api/v1/settings").json()["romaji"] is False
    with sessions(client.app.state.engine)() as db:
        assert db.scalar(select(func.count()).select_from(ReadingItem)) == 1
    assert (
        client.patch(
            url, json={"saved": False, "familiar": False, "preview_draft": True}
        ).status_code
        == 200
    )
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_reading_item_flags_are_validated_without_correctness_claims(client):
    url = "/api/v1/courses/ja-starter/reading/items/word/ja-word-house"
    for payload in [{}, {"saved": None}, {"familiar": 1}, {"is_correct": True}, {"xp": 5}]:
        assert client.patch(url, json=payload).status_code == 422
    assert client.patch(url, json={"saved": True, "familiar": True}).status_code == 200
    assert (
        client.get("/api/v1/courses/ja-starter/reading").json()["items"][0]["evidence"]
        == "self_reported"
    )
    assert client.get("/api/v1/progress").json()["total_xp"] == 0


def test_parallel_reading_flag_edits_merge_without_duplicate_records(client):
    client.get("/api/v1/profile")
    url = "/api/v1/courses/ja-starter/reading/items/word/ja-word-house"
    with ThreadPoolExecutor(max_workers=2) as pool:
        replies = list(
            pool.map(
                lambda body: client.patch(url, json=body), [{"saved": True}, {"familiar": True}]
            )
        )
    assert all(reply.status_code == 200 for reply in replies)
    item = client.get("/api/v1/courses/ja-starter/reading").json()["items"][0]
    assert item["saved"] and item["familiar"]


def test_character_and_saved_item_practice_reuse_authoritative_engine(client):
    url = "/api/v1/courses/ja-starter/sessions"
    from uuid import uuid4

    denied = client.post(
        url, json={"request_id": str(uuid4()), "source_kind": "character", "source_id": "ja-char-a"}
    )
    assert denied.status_code == 404
    session = start(client, "ja-char-a", source_kind="character", preview_draft=True)
    assert len(session["exercises"]) == 2
    assert session["preview_draft"] and session["kind"] == "practice"
    assert not {"answer", "answers", "explanation", "hint"} & session["exercises"][0].keys()
    session = act(client, session, "answer", session["exercises"][0]["id"], answer="c0")
    assert session["feedback"]["kind"] == "correct"
    session = act(client, session, "skip", session["exercises"][1]["id"])
    finished = act(client, session, "finish")
    assert finished["xp_awarded"] == 5
    assert (
        complete(client, "ja-char-a", source_kind="character", preview_draft=True)["xp_awarded"]
        == 5
    )
    saved_url = "/api/v1/courses/ja-starter/reading/items/character/ja-char-a"
    client.patch(saved_url, json={"saved": True, "preview_draft": True})
    related = start(client, "saved", source_kind="saved_items", preview_draft=True)
    assert related["exercises"] == session["exercises"]
    assert act(client, skip_all(client, related), "finish")["xp_awarded"] == 5
    assert client.get("/api/v1/progress").json()["total_xp"] == 15


def test_character_quiz_title_and_public_ids_do_not_supply_the_answer(client, course):
    for character in [entry for entry in course.characters if entry.form == "basic"]:
        session = start(client, character.id, source_kind="character", preview_draft=True)
        assert character.surface not in session["title"]
        for exercise in session["exercises"]:
            if exercise["type"] == "multiple_choice":
                assert all(choice["id"] in {"c0", "c1", "c2"} for choice in exercise["choices"])
                assert not {"answer", "answers"} & exercise.keys()
        # No answer-bearing title or prior correct flag.
        assert not session["evidence"][character.practice_exercise_ids[0]]["assisted"]
