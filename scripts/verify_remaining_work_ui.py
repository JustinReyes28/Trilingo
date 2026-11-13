"""Focused installed-browser QA for additive drafts and saved-item navigation.

Requires the isolated qa_plan92.py instance; never installs a browser or calls an
external service. Simulated HTTP failure verifies recovery, not provider success.
"""

import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlparse
from uuid import uuid4

from playwright.sync_api import expect, sync_playwright
from qa_helpers import api_matches, qa_api


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="http://127.0.0.1:5192")
    parser.add_argument("--api", default="http://127.0.0.1:8022/api/v1")
    args = parser.parse_args()
    if urlparse(args.base).hostname not in {"localhost", "127.0.0.1"}:
        raise RuntimeError("Use a loopback QA frontend")
    os.environ["TRILINGO_QA_API_BASE_URL"] = args.api
    api = qa_api()
    root = Path(__file__).resolve().parents[1]
    output = root / "artifacts/remaining-work-20261025"
    output.mkdir(parents=True, exist_ok=True)
    content = json.loads((root / "content/courses/ja/starter.json").read_text(encoding="utf-8"))
    report = json.loads(
        (root / "content/authoring/ja/stage-b-expansion-20261025-result.json").read_text(
            encoding="utf-8"
        )
    )
    words = {word["id"]: word for word in content["vocabulary"]}
    target = next(
        row
        for row in report["accepted"]
        if len(words[row["word_id"]]["practice_exercise_ids"]) == 2
    )
    exercise_map = {
        exercise["id"]: exercise
        for unit in content["units"]
        for lesson in unit["lessons"]
        for exercise in lesson["exercises"]
    }
    reading_key = exercise_map[words[target["word_id"]]["practice_exercise_ids"][1]]["answers"][0]
    errors, external, layouts, finish_payloads = [], [], [], []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
            args=[
                "--disable-background-networking",
                "--disable-component-update",
                "--no-first-run",
            ],
        )
        context = browser.new_context(viewport={"width": 390, "height": 900})

        def local_only(route):
            parsed = urlparse(route.request.url)
            if (
                parsed.hostname in {"127.0.0.1", "localhost"}
                and parsed.port in {urlparse(args.base).port, urlparse(api).port}
                and api_matches(route.request.url, api)
            ):
                route.continue_()
            else:
                external.append(route.request.url)
                route.abort()

        context.route("**/*", local_only)
        page = context.new_page()
        page.set_default_timeout(15000)
        page.on("pageerror", lambda error: errors.append(str(error)))

        def record_finish(request):
            if request.method == "POST" and request.url.endswith("/actions"):
                body = request.post_data_json
                if body.get("action") == "finish":
                    finish_payloads.append(body)

        page.on("request", record_finish)

        def call(method, path, data=None):
            response = context.request.fetch(api + path, method=method, data=data)
            assert response.ok, (path, response.status, response.text())
            return response.json()

        def capture(label, target_locator):
            for width in (320, 390, 768, 1280):
                page.set_viewport_size({"width": width, "height": 900})
                target_locator.scroll_into_view_if_needed()
                assert not page.evaluate("document.documentElement.scrollWidth > innerWidth"), (
                    label,
                    width,
                )
                page.screenshot(path=str(output / f"{label}-{width}.png"))
                layouts.append({"screen": label, "width": width, "overflow": False})
            page.set_viewport_size({"width": 390, "height": 900})

        def reading_page():
            page.goto(args.base + "/#reading?section=words")
            page.reload()
            page.wait_for_load_state("networkidle")
            page.get_by_label("Include draft practice · Japanese review pending").check()
            expect(page.get_by_role("heading", name="Words in context", exact=True)).to_be_visible()

        health = call("GET", "/health")
        assert (
            health["qa_mode"]
            and health["schema_version"] == "0015"
            and health["features"] == {"lessons": True}
        )
        assert call("GET", "/courses/ja-starter")["version"] == report["target_version"]
        reading_page()
        search = page.get_by_label("Find a word by Japanese, reading or meaning")
        search.fill(target["surface"])
        card = page.locator(".reading-word").filter(has_text=target["gloss"])
        expect(card).to_have_count(1)
        expect(card).to_contain_text("Draft practice")
        page.get_by_role("button", name="Save: " + target["surface"], exact=True).click()
        saved_word = page.get_by_role(
            "button", name="Find saved word: " + target["surface"], exact=True
        )
        saved_word.focus()
        saved_word.press("Enter")
        expect(search).to_be_focused()
        expect(search).to_have_value(target["surface"])
        capture("new-draft-context", card)
        page.get_by_role("button", name="Practice related saved items", exact=True).click()
        page.wait_for_url("**/#session/*")
        session_id = page.url.split("#session/")[1]
        page.get_by_role("button", name=target["gloss"], exact=True).click()
        page.get_by_role("button", name="Check answer", exact=True).click()
        expect(page.get_by_text("Correct", exact=True)).to_be_visible()
        page.get_by_role("button", name="Continue", exact=True).click()
        answer = page.get_by_label("Your answer", exact=True)
        answer.fill(reading_key)
        check = page.get_by_role("button", name="Check answer", exact=True)
        check.focus()
        check.press("Enter")
        expect(page.get_by_text("Correct", exact=True)).to_be_visible()
        page.get_by_role("button", name="Continue", exact=True).click()
        page.get_by_role("button", name="Finish and save session", exact=True).click()
        expect(page.get_by_role("heading", name="Session saved", exact=True)).to_be_visible()
        saved = call("GET", f"/sessions/{session_id}")
        assert saved["xp_awarded"] == 5 and saved["initial_correct"] == 2
        assert call("POST", f"/sessions/{session_id}/actions", finish_payloads[-1]) == saved

        reading_page()
        page.locator(".kana-button").first.click()
        character_dialog = page.get_by_role("dialog")
        page.get_by_role("button", name="Save for practice", exact=True).click()
        page.get_by_role("button", name="Close dialog", exact=True).click()
        reopen = page.get_by_role("button", name="Open saved character:", exact=False)
        reopen.focus()
        reopen.press("Enter")
        expect(character_dialog).to_be_visible()
        page.get_by_role("button", name="Close dialog", exact=True).click()
        capture("saved-items", page.locator(".saved-reading"))
        page.get_by_label("Include draft practice · Japanese review pending").uncheck()
        expect(page.locator(".saved-reading")).to_contain_text("0 saved items available")
        expect(
            page.get_by_role("button", name="Practice related saved items", exact=True)
        ).to_be_disabled()
        expect(page.locator(".saved-reading")).to_contain_text("unavailable in this view")
        call("PATCH", "/settings", {"practice_batch": 1})
        reading_page()
        expect(page.get_by_role("button", name="Show more saved items", exact=True)).to_be_visible()
        page.get_by_role("button", name="Show more saved items", exact=True).click()
        expect(page.locator(".saved-reading")).to_contain_text("Showing 2 of 2")
        reading_page()
        page.get_by_role("button", name="Show all saved items", exact=True).click()
        expect(page.locator(".saved-reading")).to_contain_text("Showing 2 of 2")

        collection_base = "/courses/ja-starter/collections"
        first = call(
            "POST", collection_base, {"request_id": str(uuid4()), "name": "QA first collection"}
        )
        second = call(
            "POST", collection_base, {"request_id": str(uuid4()), "name": "QA second collection"}
        )
        call(
            "PATCH",
            f"/collections/{first['id']}/members",
            {"item_id": "ja-word-hello", "saved": True},
        )
        call(
            "PATCH",
            f"/collections/{second['id']}/members",
            {"item_id": "ja-word-school", "saved": True},
        )
        page.goto(args.base + "/#review")
        page.get_by_text("Personal vocabulary collections", exact=True).click()
        picker = page.get_by_role("combobox", name="Choose a collection", exact=True)
        picker.select_option(first["id"])
        expect(page.get_by_role("button", name="Review this word", exact=True)).to_have_count(1)
        pending = []
        member_url = api + f"/collections/{second['id']}/members"

        def delay_members(route):
            pending.append(route)

        page.route(member_url, delay_members)
        picker.select_option(second["id"])
        expect(
            page.get_by_text("Loading words in QA second collection…", exact=True)
        ).to_be_visible()
        expect(page.get_by_role("button", name="Review this word", exact=True)).to_have_count(0)
        expect(
            page.get_by_role("button", name="Open collection recall", exact=True)
        ).to_be_disabled()
        assert pending
        pending.pop().fulfill(
            status=503,
            content_type="application/json",
            body=json.dumps(
                {
                    "error": {
                        "code": "qa_unavailable",
                        "message": "QA simulated local interruption",
                        "recovery": "Retry this collection.",
                    }
                }
            ),
        )
        retry = page.get_by_role("button", name="Retry collection words", exact=True)
        expect(retry).to_be_visible()
        expect(page.get_by_role("button", name="Remove bookmark", exact=True)).to_have_count(0)
        capture("collection-recovery", page.locator(".vocabulary-collections"))
        page.unroute(member_url, delay_members)
        retry.click()
        expect(page.get_by_role("button", name="Review this word", exact=True)).to_have_count(1)
        expect(page.locator(".vocabulary-collections")).to_contain_text(
            words["ja-word-school"]["gloss"]
        )
        assert not errors and not external, {"errors": errors, "external": external}
        result = {
            "source_version": report["target_version"],
            "source_sha256": report["source_sha256"],
            "new_word": target["surface"],
            "session_id": session_id,
            "xp": saved["xp_awarded"],
            "correct": saved["initial_correct"],
            "duplicate_finish_preserved": True,
            "saved_word_keyboard_navigation": True,
            "saved_character_reopened": True,
            "hidden_draft_practice_disabled": True,
            "saved_batches_expand": True,
            "collection_pending_and_failure_hide_stale_actions": True,
            "collection_retry": True,
            "layouts": layouts,
            "browser_errors": errors,
            "external_requests": external,
            "limits": (
                "Simulated HTTP failure; no physical IME, screen reader, "
                "touch/stylus or qualified human audio/curriculum review."
            ),
        }
        (output / "report.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(json.dumps(result, ensure_ascii=True))
        browser.close()


if __name__ == "__main__":
    main()
