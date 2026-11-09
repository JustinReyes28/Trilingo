"""Plan 9.2 history, batch and input-guide checks using only an isolated QA app."""

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
    parser.add_argument("--browser", default="msedge")
    parser.add_argument("--executable", type=Path)
    args = parser.parse_args()
    if urlparse(args.base).hostname not in {"localhost", "127.0.0.1"}:
        raise RuntimeError("Use a loopback QA frontend")
    os.environ["TRILINGO_QA_API_BASE_URL"] = args.api
    api = qa_api()
    output = Path(__file__).resolve().parents[1] / "artifacts/plan-9-2"
    output.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        executable = args.executable
        system_edge = Path(
            "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
        )
        if executable is None and args.browser == "msedge" and system_edge.is_file():
            executable = system_edge
        browser = playwright.chromium.launch(
            headless=True,
            executable_path=str(executable) if executable else None,
            channel=None if executable else args.browser,
        )
        context = browser.new_context(viewport={"width": 390, "height": 900})
        errors: list[str] = []
        external: list[str] = []
        layouts: list[dict] = []

        def local_only(route):
            url = route.request.url
            if urlparse(url).hostname in {"127.0.0.1", "localhost"} and api_matches(
                url, api
            ):
                route.continue_()
            else:
                external.append(url)
                route.abort()

        context.route("**/*", local_only)
        page = context.new_page()
        page.set_default_timeout(12000)
        page.on("pageerror", lambda error: errors.append(str(error)))

        def call(method, path, data=None):
            response = context.request.fetch(api + path, method=method, data=data)
            assert response.ok, (path, response.status, response.text())
            return response.json()

        def capture(label):
            (output / f"{label}.html").write_text(page.content(), encoding="utf-8")
            for width in (320, 390, 768, 1280):
                page.set_viewport_size({"width": width, "height": 900})
                assert not page.evaluate(
                    "document.documentElement.scrollWidth > innerWidth"
                ), (label, width)
                page.screenshot(
                    path=str(output / f"{label}-{width}.png"), full_page=True
                )
                page.screenshot(path=str(output / f"{label}-{width}-viewport.png"))
                layouts.append({"surface": label, "width": width, "overflow": False})

        call("PATCH", "/settings", {"show_statistics": True, "show_timer": False})
        page.goto(args.base + "/#review")
        page.wait_for_load_state("networkidle")
        page.get_by_text("Timed session history", exact=True).click()
        page.get_by_role("combobox", name="History activity", exact=True).select_option(
            "writing"
        )
        expect(
            page.get_by_text("No valid completed timed sessions", exact=False)
        ).to_be_visible()
        capture("history-empty")
        words = call("GET", "/courses/ja-starter/library")["vocabulary"]
        cards = []
        for word in [word for word in words if word["entry_kind"] == "word"]:
            for direction in ("meaning", "reading", "typing"):
                cards.append(
                    call(
                        "POST",
                        "/courses/ja-starter/review/cards",
                        {"item_id": word["id"], "direction": direction},
                    )
                )
        card = cards[0]
        for _ in range(25):
            session = call(
                "POST",
                f"/review/cards/{card['id']}/session",
                {"request_id": str(uuid4())},
            )
            paused = call(
                "POST",
                f"/sessions/{session['id']}/actions",
                {
                    "request_id": session["next_action_id"],
                    "expected_revision": session["revision"],
                    "action": "timer_pause",
                },
            )
            assert not paused["timer"]["running"]
            card = call(
                "POST",
                f"/review/cards/{card['id']}/ratings",
                {
                    "request_id": str(uuid4()),
                    "expected_revision": card["revision"],
                    "rating": "Good",
                    "recall_session_id": session["id"],
                },
            )
        page.reload()
        page.wait_for_load_state("networkidle")
        page.get_by_label("Cards per batch", exact=True).fill("2")
        card_rows = page.locator(".grammar-layout > section > ul.session-list > li")
        expect(card_rows).to_have_count(2)
        page.get_by_role("button", name="Show more", exact=True).click()
        expect(card_rows).to_have_count(4)
        page.wait_for_load_state("networkidle")
        expect(card_rows).to_have_count(4)
        page.get_by_role("button", name="Show all", exact=True).click()
        expect(card_rows).to_have_count(
            call("GET", "/courses/ja-starter/review/cards")["total"]
        )
        page.wait_for_load_state("networkidle")
        expected_cards = call("GET", "/courses/ja-starter/review/cards")["total"]
        expect(card_rows).to_have_count(expected_cards)
        collection = call(
            "POST",
            "/courses/ja-starter/collections",
            {
                "request_id": str(uuid4()),
                "name": "Plan 9.2 browser collection " + str(uuid4()),
            },
        )
        for word in [word for word in words if word["entry_kind"] == "word"][:3]:
            call(
                "PATCH",
                f"/collections/{collection['id']}/members",
                {"item_id": word["id"], "saved": True},
            )
        page.reload()
        page.wait_for_load_state("networkidle")
        page.get_by_text("Personal vocabulary collections", exact=True).click()
        page.get_by_role(
            "combobox", name="Choose a collection", exact=True
        ).select_option(collection["id"])
        page.get_by_role("button", name="Open collection recall", exact=True).click()
        page.get_by_label("Cards per batch", exact=True).fill("20")
        expect(card_rows).to_have_count(3)
        expect(page.get_by_text(collection["name"], exact=True)).to_be_visible()
        page.get_by_role("combobox", name="Recall direction", exact=True).select_option(
            "typing"
        )
        expect(card_rows).to_have_count(3)
        before_browse = call("GET", "/progress")["total_xp"]
        card_rows.first.get_by_role("button", name="Review now", exact=True).click()
        page.get_by_label("Optional recall notes", exact=True).fill("日本語")
        page.get_by_role("button", name="Skip card · keep schedule", exact=True).click()
        assert call("GET", "/progress")["total_xp"] == before_browse
        capture("collection-recall")
        page.get_by_role("button", name="Show all saved cards", exact=True).click()
        page.get_by_text("Timed session history", exact=True).click()
        page.get_by_label("Records per page", exact=True).select_option("20")
        total_records = call("GET", "/personal/timing")["total"]
        rows = page.locator(".timing-history > li")
        expect(rows).to_have_count(20)
        first_ids = rows.evaluate_all("rows => rows.map(row => row.dataset.sessionId)")
        history_nav = page.get_by_role("navigation", name="Timing history pages", exact=True)
        history_nav.get_by_role("button", name="Next", exact=True).focus()
        with page.expect_response(lambda response: "/personal/timing?" in response.url):
            page.keyboard.press("Enter")
        expect(rows.first).not_to_have_attribute("data-session-id", first_ids[0])
        expect(rows).to_have_count(min(20, total_records - 20))
        assert not set(first_ids) & set(
            rows.evaluate_all("rows => rows.map(row => row.dataset.sessionId)")
        )
        if history_nav.get_by_role("button", name="Last", exact=True).is_enabled():
            history_nav.get_by_role("button", name="Last", exact=True).click()
        page.wait_for_load_state("networkidle")
        expect(
            history_nav.get_by_role("button", name="Next", exact=True)
        ).to_be_disabled()
        capture("history-final-page")
        history_nav.get_by_role("button", name="First", exact=True).click()
        page.wait_for_load_state("networkidle")
        expect(rows).to_have_count(20)
        history_nav.get_by_role("button", name="Last", exact=True).click()
        page.wait_for_load_state("networkidle")
        expect(
            history_nav.get_by_role("button", name="Next", exact=True)
        ).to_be_disabled()
        expect(rows).to_have_count(20)
        page.get_by_role("combobox", name="History activity", exact=True).select_option(
            "review"
        )
        expect(rows).to_have_count(20)
        expect(rows.first).to_contain_text("Good (self-rated)")
        expect(rows.first).to_contain_text("Paused")
        capture("history-recall-filter")
        page.get_by_role("combobox", name="History activity", exact=True).select_option(
            "writing"
        )
        expect(rows).to_have_count(0)
        capture("history-filter-empty")
        page.route("**/personal/timing?**", lambda route: route.abort())
        page.get_by_role("combobox", name="History activity", exact=True).select_option(
            ""
        )
        expect(
            page.get_by_role("button", name="Retry history page", exact=True)
        ).to_be_visible()
        capture("history-error")
        page.unroute("**/personal/timing?**")
        page.get_by_role("button", name="Retry history page", exact=True).click()
        expect(rows).to_have_count(20)
        page.get_by_label("Records per page", exact=True).select_option("5")
        expect(rows).to_have_count(5)
        for label in ("Evidence by skill", "Completed practice workflows", "Published curriculum coverage"):
            page.get_by_text(label, exact=True).click()
        expect(page.get_by_text("Full beginner coverage and qualified review remain pending.", exact=False)).to_be_visible()
        capture("personal-provenance")
        page.goto(args.base + "/#writing")
        page.wait_for_load_state("networkidle")
        page.get_by_text(
            "Try Japanese input & read the Windows guide", exact=True
        ).click()
        expect(
            page.get_by_role("link", name="Microsoft Japanese input guide", exact=True)
        ).to_have_attribute(
            "href", "https://learn.microsoft.com/en-us/globalization/input/japanese-ime"
        )
        tester = page.get_by_label(
            "Japanese input test · not saved or graded", exact=True
        )
        tester.fill("にほん")
        tester.dispatch_event("compositionstart")
        tester.press("Enter")
        expect(
            page.get_by_text("IME composition in progress.", exact=False)
        ).to_be_visible()
        tester.dispatch_event("compositionend")
        tester.fill("日本\nかな")
        expect(tester).to_have_value("日本\nかな")
        capture("ime-guide")
        page.goto(args.base + "/#grammar")
        page.wait_for_load_state("networkidle")
        page.get_by_label(
            "Show unreviewed draft guides and scenarios", exact=True
        ).check()
        expect(page.locator(".authored-note")).to_have_count(16)
        for index in range(1, 11):
            page.get_by_role("combobox", name="Unit guide", exact=True).select_option(
                f"ja-unit-{index}"
            )
            assert page.locator(".authored-note").count() >= 1
        page.get_by_role("combobox", name="Unit guide", exact=True).select_option(
            "ja-unit-5"
        )
        page.get_by_label("Find a pattern", exact=True).fill("よじ")
        expect(page.locator(".authored-note")).to_have_count(1)
        capture("unit-guide-search")
        page.get_by_role("button", name="Practice this pattern", exact=True).click()
        expect(
            page.get_by_role(
                "heading",
                name="Choose the taught reading of 四時 (four o’clock).",
                exact=True,
            )
        ).to_be_visible()
        page.get_by_role("button", name="よんじ", exact=True).click()
        page.get_by_role("button", name="Check answer", exact=True).click()
        expect(page.get_by_text("Not yet", exact=True)).to_be_visible()
        expect(
            page.get_by_text(
                "よん is used in other number contexts, but 四時 is よじ here.",
                exact=True,
            )
        ).to_be_visible()
        capture("draft-guide-feedback")
        before_finish = call("GET", "/progress")["total_xp"]
        for _ in range(3):
            page.get_by_role("button", name="Skip prompt", exact=True).click()
        page.get_by_role("button", name="Finish and save session", exact=True).click()
        expect(
            page.get_by_role("heading", name="Session saved", exact=True)
        ).to_be_visible()
        assert call("GET", "/progress")["total_xp"] == before_finish + 5
        assert not errors, errors
        assert not external, external
        result = {
            "layouts": layouts,
            "page_errors": errors,
            "external_requests": external,
            "records": 25,
            "card_batch": len(cards),
            "input": "synthetic composition only; physical IME unverified",
        }
        (output / "results.json").write_text(
            json.dumps(result, indent=2), encoding="utf-8"
        )
        print(
            json.dumps(
                {
                    "layouts": len(layouts),
                    "errors": errors,
                    "external_requests": external,
                }
            )
        )
        browser.close()


if __name__ == "__main__":
    main()
