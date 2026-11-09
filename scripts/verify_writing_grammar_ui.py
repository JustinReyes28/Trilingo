"""Focused grammar recovery and unsaved-drawing safety in disposable loopback QA."""

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
    if urlparse(args.base).hostname not in {"127.0.0.1", "localhost"}:
        raise RuntimeError("Use a loopback QA frontend")
    os.environ["TRILINGO_QA_API_BASE_URL"] = args.api
    api = qa_api()
    root = Path(__file__).resolve().parents[1]
    output = root / "artifacts/writing-grammar-extension-20261025"
    output.mkdir(parents=True, exist_ok=True)
    content = json.loads((root / "content/courses/ja/starter.json").read_text(encoding="utf-8"))
    exercises = {item["id"]: item for item in content["practice_exercises"]}
    for unit in content["units"]:
        for lesson in unit["lessons"]:
            exercises.update({item["id"]: item for item in lesson["exercises"]})
    errors, external, layouts, scenes = [], [], [], []
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
        page.on("dialog", lambda dialog: dialog.accept())

        def call(method, path, data=None):
            response = context.request.fetch(api + path, method=method, data=data)
            assert response.ok, (path, response.status, response.text())
            return response.json()

        def capture(label, locator):
            for width in (320, 390, 768, 1280):
                page.set_viewport_size({"width": width, "height": 900})
                locator.scroll_into_view_if_needed()
                assert not page.evaluate("document.documentElement.scrollWidth > innerWidth"), (
                    label,
                    width,
                )
                page.screenshot(path=str(output / f"{label}-{width}.png"))
                layouts.append({"screen": label, "width": width, "overflow": False})
            page.set_viewport_size({"width": 390, "height": 900})

        health = call("GET", "/health")
        assert health["qa_mode"] and not any(
            health["features"][key] for key in ("ai", "tts", "stt")
        )
        assert call("GET", "/progress")["total_xp"] == 0, "Use a new disposable QA DB"
        grammar = call("GET", "/courses/ja-starter/grammar?include_drafts=true")
        held = []
        mode = ["pass"]

        def grammar_view(route):
            if mode[0] == "hold":
                held.append(route)
            else:
                route.continue_()

        page.route("**/courses/ja-starter/grammar?include_drafts=*", grammar_view)
        page.goto(args.base + "/#grammar")
        drafts = page.get_by_label("Show unreviewed draft guides and scenarios", exact=True)
        drafts.check()
        expect(page.locator(".authored-note")).to_have_count(len(grammar["notes"]))
        mode[0] = "hold"
        drafts.uncheck()
        expect(page.get_by_role("status").filter(has_text="Loading guides")).to_be_visible()
        expect(page.locator(".authored-note")).to_have_count(0)
        expect(page.locator(".scenario-row")).to_have_count(0)
        assert held, "The pending grammar request must be held before testing stale actions"
        held.pop().fulfill(
            status=503,
            content_type="application/json",
            body=json.dumps(
                {"error": {"code": "qa_unavailable", "message": "QA grammar view unavailable."}}
            ),
        )
        expect(page.get_by_role("alert")).to_contain_text("QA grammar view unavailable.")
        expect(page.get_by_role("status")).to_contain_text("Guides unavailable.")
        expect(page.locator(".authored-note")).to_have_count(0)
        expect(page.locator(".scenario-row")).to_have_count(0)
        capture("grammar-load-error", page.get_by_role("alert"))
        mode[0] = "pass"
        reload = page.get_by_role("button", name="Reload grammar", exact=True)
        reload.focus()
        reload.press("Enter")
        expect(page.get_by_text("No matching published guides.", exact=False)).to_be_visible()
        drafts.check()
        expect(page.locator(".authored-note")).to_have_count(len(grammar["notes"]))
        note = next(item for item in grammar["notes"] if item["id"] == "guide-de")
        page.get_by_label("Unit guide", exact=True).select_option(note["unit_ids"][0])
        page.get_by_label("Find a pattern", exact=True).fill(note["title"])
        selected = page.locator('[id="guide-de"]')
        expect(selected).to_be_visible()
        selected.get_by_role("button", name="Bookmark grammar", exact=True).click()
        expect(
            selected.get_by_role("button", name="Remove grammar bookmark", exact=True)
        ).to_be_visible()
        page.reload()
        drafts.check()
        expect(
            page.locator('[id="guide-de"]').get_by_role(
                "button",
                name="Remove grammar bookmark",
                exact=True,
            )
        ).to_be_visible()
        assert any(
            item["item_id"] == "guide-de" and item["saved"]
            for item in call(
                "GET",
                "/courses/ja-starter/reading",
            )["items"]
        )

        def action(session_id, label):
            with page.expect_response(
                lambda response: (
                    response.request.method == "POST"
                    and response.url == api + "/sessions/" + session_id + "/actions"
                )
            ) as pending:
                page.get_by_role("button", name=label, exact=True).click()
            response = pending.value
            assert response.ok, response.text()
            return response.json(), response.request.post_data_json

        def answer(exercise):
            if exercise["type"] in {"multiple_choice", "response_selection"}:
                choice = next(
                    item for item in exercise["choices"] if item["id"] == exercise["answer"]
                )
                page.get_by_role("button", name=choice["text"], exact=True).click()
            else:
                page.get_by_label("Your answer", exact=True).fill(exercise["answers"][-1])
            page.get_by_role("button", name="Check answer", exact=True).click()
            expect(page.get_by_text("Correct", exact=True)).to_be_visible()

        page.locator('[id="guide-de"]').get_by_role(
            "button",
            name="Practice this pattern",
            exact=True,
        ).click()
        page.wait_for_url("**/#session/*")
        pattern_id = page.url.split("#session/")[1]
        pattern = call("GET", "/sessions/" + pattern_id)
        assert pattern["source_kind"] == "grammar" and pattern["source_id"] == "guide-de"
        answer(exercises[pattern["exercises"][0]["id"]])
        pattern, _ = action(pattern_id, "Continue")
        for _ in pattern["exercises"][1:]:
            pattern, _ = action(pattern_id, "Skip prompt")
        pattern, pattern_finish = action(pattern_id, "Finish and save session")
        assert pattern["xp_awarded"] == 5 and pattern["initial_correct"] == 1
        assert call("POST", "/sessions/" + pattern_id + "/actions", pattern_finish) == pattern
        page.goto(args.base + "/#grammar")
        drafts.check()

        for index, scene in enumerate(
            [item for item in grammar["scenarios"] if item["kind"] == "dialogue"][:3]
        ):
            if index:
                page.goto(args.base + "/#grammar")
                drafts.check()
            row = page.locator(".scenario-row").filter(
                has=page.get_by_role("heading", name=scene["title"], exact=True)
            )
            row.get_by_role("button", name="Try draft dialogue", exact=True).click()
            page.wait_for_url("**/#session/*")
            session_id = page.url.split("#session/")[1]
            current = call("GET", "/sessions/" + session_id)
            if index == 0:
                current, _ = action(session_id, "Pause and leave")
                assert current["status"] == "paused"
                page.goto(args.base + "/#session/" + session_id)
                current, _ = action(session_id, "Resume study")
                assert current["status"] == "active"
            while True:
                for exercise_id in current["story"]["current"]["exercise_ids"]:
                    answer(exercises[exercise_id])
                if current["story"]["at_end"]:
                    break
                current, _ = action(session_id, "Continue story · skip unchecked prompts")
            saved, finish_body = action(session_id, "Finish story & save")
            assert saved["status"] == "completed" and saved["xp_awarded"] == 5
            assert saved["initial_correct"] == saved["assessed_count"] == 1
            assert call("POST", "/sessions/" + session_id + "/actions", finish_body) == saved
            scenes.append({"id": scene["id"], "session_id": session_id, "correct": 1, "xp": 5})
        assert call("GET", "/progress")["total_xp"] == 20

        first_character, second_character = "ja-char-hiragana-3044", "ja-char-hiragana-3053"
        receipts = []
        for character in (second_character, first_character):
            request_id = str(uuid4())
            saved = call(
                "POST",
                "/courses/ja-starter/writing/handwriting",
                {
                    "request_id": request_id,
                    "character_id": character,
                    "preview_draft": True,
                    "mode": "guided_trace",
                    "strokes": [[{"x": 0.3, "y": 0.2, "t": 0}, {"x": 0.35, "y": 0.75, "t": 100}]],
                    "sequence": [],
                    "reference_revealed": True,
                    "self_rating": "practiced",
                    "keep_sample": True,
                },
            )
            assert saved["sample_id"] and saved["xp_awarded"] == 5
            receipts.append(
                {
                    "path": "/writing/receipts/" + request_id,
                    "body": {"request_id": request_id, "character_id": character},
                }
            )
        before_confirmation = call("GET", "/progress")["total_xp"]
        page.evaluate(
            "value => localStorage.setItem('trilingo.drawing-receipts', JSON.stringify(value))",
            receipts,
        )
        page.goto(args.base + "/#writing/drawing")
        page.get_by_label("Include draft character templates", exact=False).check()
        expect(page.get_by_role("heading", name="い", exact=True)).to_be_visible()
        pad = page.locator(".drawing-pad").first
        pad.scroll_into_view_if_needed()
        box = pad.bounding_box()
        assert box
        page.mouse.move(box["x"] + 0.4 * box["width"], box["y"] + 0.2 * box["height"])
        page.mouse.down()
        page.mouse.move(box["x"] + 0.5 * box["width"], box["y"] + 0.8 * box["height"], steps=12)
        page.mouse.up()
        expect(page.get_by_text("1 strokes · pointer coordinates", exact=False)).to_be_visible()
        page.get_by_role("button", name="Check earlier drawing receipt", exact=True).click()
        expect(
            page.get_by_text(
                "Earlier drawing activity confirmed · +5 XP already recorded", exact=True
            )
        ).to_be_visible()
        expect(page.get_by_text("Your current drawing is separate.", exact=False)).to_be_visible()
        expect(
            page.get_by_role("button", name="Record this practice activity", exact=True)
        ).to_be_enabled()
        assert call("GET", "/progress")["total_xp"] == before_confirmation
        pending = page.evaluate("JSON.parse(localStorage.getItem('trilingo.drawing-receipts'))")
        assert pending == [receipts[0]], "The other character's receipt must remain pending"
        page.get_by_label("Character to practice", exact=True).select_option(second_character)
        warning = page.get_by_role("dialog", name="Leave the current drawing?", exact=True)
        expect(warning).to_be_visible()
        capture("receipt-preserves-unsaved-grid", warning)
        page.get_by_role("button", name="Keep current drawing", exact=True).click()
        expect(page.get_by_role("heading", name="い", exact=True)).to_be_visible()
        expect(page.get_by_text("1 strokes · pointer coordinates", exact=False)).to_be_visible()
        page.get_by_label("Keep an optional local drawing sample", exact=True).check()
        with page.expect_response(
            lambda response: (
                response.request.method == "POST" and response.url.endswith("/writing/handwriting")
            )
        ) as pending:
            page.get_by_role("button", name="Record this practice activity", exact=True).click()
        response = pending.value
        assert response.ok, response.text()
        current_result, body = response.json(), response.request.post_data_json
        assert body["character_id"] == first_character and len(body["strokes"]) == 1
        assert current_result["sample_id"] and current_result["objective_correctness"] is None
        assert call("POST", "/courses/ja-starter/writing/handwriting", body) == current_result
        assert call("GET", "/progress")["total_xp"] == before_confirmation + 5 == 35
        assert not errors and not external, (errors, external)
        result = {
            "status": "pass",
            "content_version": content["version"],
            "qa_mode": True,
            "grammar_scope_loading_and_failure": True,
            "keyboard_reload": True,
            "grammar_search_unit_filter_and_bookmark_reload": True,
            "targeted_pattern_correct_skip_finish_and_retry": True,
            "authored_scenarios": scenes,
            "first_dialogue_pause_resume": True,
            "authored_alternatives_checked": True,
            "exact_finish_retries_idempotent": True,
            "old_receipt_does_not_save_current_grid": True,
            "character_scoped_receipts": True,
            "unsaved_switch_warning_and_keep_strokes": True,
            "receipt_confirmation_xp": 0,
            "new_drawing_commit_xp": 5,
            "new_drawing_exact_retry_idempotent": True,
            "total_xp": 35,
            "layouts": layouts,
            "javascript_errors": errors,
            "external_page_requests": external,
            "limitations": [
                "Scripted mouse/keyboard; physical IME, touch/stylus, screen reader "
                "and real providers unverified"
            ],
        }
        (output / "report.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(json.dumps(result, ensure_ascii=False))
        browser.close()


if __name__ == "__main__":
    main()
