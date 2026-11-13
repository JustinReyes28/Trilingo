"""Local-only phase 7–9 engineering QA. Uses an existing browser; no downloads."""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

from playwright.sync_api import expect, sync_playwright
from qa_helpers import api_matches

sys.stdout.reconfigure(encoding="utf-8")
parser = argparse.ArgumentParser()
parser.add_argument("--base", default="http://127.0.0.1:5187")
parser.add_argument("--api", default="http://127.0.0.1:8017/api/v1")
parser.add_argument("--browser", default="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
args = parser.parse_args()
for url in [args.base, args.api]:
    if urlparse(url).hostname not in {"127.0.0.1", "localhost"}:
        raise RuntimeError("Only isolated loopback QA is supported")
with urlopen(args.api + "/health", timeout=5) as response:
    assert json.load(response)["qa_mode"], "Refusing a non-QA database"
root = Path(__file__).resolve().parents[1]
output = root / "artifacts/phase789"
output.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path=args.browser)
    context = browser.new_context(viewport={"width":390,"height":900})
    errors, external, layouts = [], [], []
    def local(route):
        if urlparse(route.request.url).hostname in {"localhost", "127.0.0.1"} and api_matches(route.request.url, args.api):
            route.continue_()
        else:
            external.append(route.request.url)
            route.abort()
    context.route("**/*", local)
    page = context.new_page()
    health = page.request.get(args.api + "/health").json()
    assert health["schema_version"] == "0015" and health["features"] == {"lessons": True}
    audio_pack = page.request.get(args.api + "/audio/status").json()["audio_pack"]
    page.set_default_timeout(12000)
    page.on("pageerror", lambda error: errors.append(str(error)))
    def capture(name):
        for width in [320,390,768,1280]:
            page.set_viewport_size({"width":width,"height":900})
            assert not page.evaluate("document.documentElement.scrollWidth > innerWidth"), (name,width)
            page.evaluate("window.scrollTo(0,0)")
            page.screenshot(path=str(output / f"{name}-{width}.png"), full_page=True)
            page.screenshot(path=str(output / f"{name}-{width}-viewport.png"))
            layouts.append({"surface":name,"width":width,"overflow":False})
    page.goto(args.base + "/#grammar")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("heading", name="Patterns for everyday Japanese")).to_be_visible()
    page.get_by_label("Show unreviewed draft guides and scenarios").check()
    expect(page.locator(".authored-note")).to_have_count(16)
    expect(page.locator(".scenario-row")).to_have_count(6)
    page.get_by_label("Find a pattern").fill("particle-de")
    expect(page.locator(".grammar-note")).to_have_count(3)
    bookmark = page.locator("#guide-de").get_by_role("button", name=re.compile("grammar bookmark|Bookmark grammar"))
    if "Remove" in bookmark.inner_text(): bookmark.click()
    expect(bookmark).to_have_text("Bookmark grammar")
    bookmark.click()
    expect(bookmark).to_have_text("Remove grammar bookmark")
    capture("grammar-search")
    (output / "rendered-grammar.html").write_text(page.content(),encoding="utf-8")
    page.get_by_label("Find a pattern").fill("")
    scene = page.locator(".scenario-row").filter(has=page.get_by_role("heading", name="Meeting someone", exact=True))
    scene.get_by_role("button").click()
    expect(page.get_by_role("heading", name="Meeting someone", exact=True)).to_be_visible()
    page.get_by_role("button", name="おやすみなさい。", exact=True).click()
    page.get_by_role("button", name="Check answer", exact=True).click()
    expect(page.get_by_text("Not yet", exact=True)).to_be_visible()
    page.get_by_role("button", name="Continue story · skip unchecked prompts", exact=True).click()
    expect(page.get_by_text("Partner · clarification", exact=True)).to_be_visible()
    capture("dialogue-branch")
    page.get_by_role("button", name="Show optional elapsed time", exact=True).click()
    expect(page.get_by_role("button", name="Pause elapsed time", exact=True)).to_be_visible()
    page.get_by_role("button", name="Pause elapsed time", exact=True).click()
    page.get_by_role("button", name="Hide elapsed time", exact=True).click()
    expect(page.get_by_role("button", name="Show elapsed time", exact=True)).to_be_visible()
    page.get_by_role("button", name="Pause and leave", exact=True).click()
    page.wait_for_url("**/#learn")
    page.goto(args.base + "/#practice")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Resume session", exact=True).first.click()
    expect(page.get_by_text("Partner · clarification", exact=True)).to_be_visible()
    page.get_by_role("button", name="Finish story & save", exact=True).click()
    expect(page.get_by_role("heading", name="Session saved", exact=True)).to_be_visible()
    for title, answer in [("Ordering a drink", "お水をください。"), ("A small purchase", "これをお願いします。")]:
        page.goto(args.base + "/#grammar")
        page.get_by_label("Show unreviewed draft guides and scenarios").check()
        scene=page.locator(".scenario-row").filter(has=page.get_by_role("heading", name=title, exact=True))
        scene.get_by_role("button", name="Try draft dialogue", exact=True).click()
        page.get_by_label("Your answer", exact=True).fill(answer)
        page.get_by_role("button", name="Check answer", exact=True).click()
        expect(page.get_by_text("Correct", exact=True)).to_be_visible()
        page.get_by_role("button", name="Finish story & save", exact=True).click()
        expect(page.get_by_role("heading", name="Session saved", exact=True)).to_be_visible()
    page.goto(args.base + "/#review")
    page.wait_for_load_state("networkidle")
    page.get_by_label("Suggested target", exact=True).fill("1")
    page.get_by_label("Practice to notice", exact=True).select_option("reviews")
    with page.expect_response(lambda response: response.url == args.api + "/quests" and response.request.method == "POST") as assignment_response:
        page.get_by_role("button", name="Add personal quest", exact=True).click()
    assignment_id=assignment_response.value.json()["id"]
    assignment=page.locator('[data-quest-id="'+assignment_id+'"]')
    expect(assignment).to_contain_text("reviews: 0 / 1")
    page.get_by_text("Personal vocabulary collections", exact=True).click()
    page.get_by_label("Collection name", exact=True).fill("Browser phrases " + str(__import__('time').time_ns()))
    page.get_by_role("button", name="Create collection", exact=True).click()
    expect(page.get_by_role("button", name="Add selected word to collection", exact=True)).to_be_visible()
    page.get_by_role("button", name="Add selected word to collection", exact=True).click()
    expect(page.get_by_role("button", name="Review this word", exact=True)).to_be_visible()
    before_import = page.request.get(args.api + "/progress").json()["total_xp"]
    page.get_by_role("button", name="Add saved mistakes to recall", exact=True).click()
    expect(page.get_by_text("Mistake cards added without changing", exact=False)).to_be_visible()
    assert page.request.get(args.api + "/progress").json()["total_xp"] == before_import
    page.get_by_role("button", name="Add or open card", exact=True).click()
    expect(page.get_by_role("button", name="Reveal answer", exact=True)).to_be_visible()
    capture("review-before-reveal")
    baseline=page.request.get(args.api + "/progress").json()["total_xp"]
    page.get_by_role("button", name="Reveal answer", exact=True).click()
    page.get_by_role("button", name="Good", exact=True).click()
    expect(page.get_by_text("Review saved.", exact=False)).to_be_visible()
    expect(assignment).to_have_text("reviews: 1 / 1 · Complete")
    expect(page.get_by_role("button", name="Reveal answer", exact=True)).to_be_visible()
    page.get_by_role("button", name="Reveal answer", exact=True).click()
    page.get_by_role("button", name="Easy", exact=True).click()
    expect(page.get_by_role("button", name="Reveal answer", exact=True)).to_be_visible()
    assert page.request.get(args.api + "/progress").json()["total_xp"] == baseline + 10
    before=page.request.get(args.api + "/courses/ja-starter/review/cards").json()
    page.get_by_role("button", name="Skip card · keep schedule", exact=True).click()
    assert page.request.get(args.api + "/courses/ja-starter/review/cards").json() == before
    page.get_by_label("Installed accent", exact=True).select_option("plum")
    expect(page.locator("html")).to_have_attribute("data-accent", "plum")
    capture("review-personal")
    (output / "rendered-review.html").write_text(page.content(),encoding="utf-8")
    page.reload()
    expect(page.get_by_label("Installed accent", exact=True)).to_have_value("plum")
    page.goto(args.base + "/#audio")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Prepare reference audio", exact=True).click()
    if audio_pack["bundled_reference"]:
        expect(page.get_by_label("Bundled reference audio", exact=True)).to_be_visible()
    else:
        expect(page.get_by_role("alert")).to_be_visible()
    page.get_by_role("button", name="Reveal transcript / use text alternative", exact=True).click()
    expect(page.locator(".recall-sheet .dialog-japanese")).to_have_text("こんにちは")
    capture("audio-reference-text-alternative")
    page.get_by_label("Include draft stories, dialogues", exact=False).check()
    expect(page.get_by_label("Reference phrase", exact=True).locator("option").filter(has_text="audio_episode")).to_have_count(2)
    page.get_by_label("Reference phrase", exact=True).select_option("ja-audio-first-introduction")
    page.get_by_role("button", name="Reveal transcript / use text alternative", exact=True).click()
    capture("audio-episode-draft")
    (output / "rendered-audio.html").write_text(page.content(),encoding="utf-8")
    page.goto(args.base + "/#learn")
    page.locator(".lesson-node").last.click()
    page.get_by_role("button", name="Start lesson", exact=True).click()
    expect(page.get_by_role("button", name="Skip prompt", exact=True)).to_be_visible()
    capture("published-lesson-local-only")
    for _ in range(5):
        page.get_by_role("button", name="Skip prompt", exact=True).click()
    page.get_by_role("button", name="Finish and save session", exact=True).click()
    expect(page.get_by_role("heading", name="Session saved", exact=True)).to_be_visible()
    # Keyboard reachability and skip link; this is DOM evidence, not a screen-reader certification.
    page = context.new_page()
    page.goto(args.base + "/#review")
    page.wait_for_load_state("networkidle")
    page.keyboard.press("Tab")
    expect(page.get_by_role("link", name="Skip to content", exact=True)).to_be_focused()
    page.keyboard.press("Enter")
    expect(page.locator("#main")).to_be_focused()
    assert not errors, errors
    assert not external, external
    (output / "results.json").write_text(json.dumps({"layouts":layouts,"page_errors":errors,"external_requests":external,"audio_pack":audio_pack,"physical_ime":"unverified","providers":"Zero runtime AI, STT, microphone capture, or TTS (schema 0015)"},indent=2),encoding="utf-8")
    print(json.dumps({"layouts":len(layouts),"errors":errors,"external_requests":external}))
    browser.close()
