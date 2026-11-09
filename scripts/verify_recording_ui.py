"""Simulated microphone QA only; no real recording or provider success is claimed."""
import base64
import io
import json
import sys
import wave
from pathlib import Path
from urllib.request import urlopen
from playwright.sync_api import expect, sync_playwright
from qa_helpers import api_matches
from urllib.parse import urlparse
sys.stdout.reconfigure(encoding="utf-8")
BASE="http://127.0.0.1:5187"
API="http://127.0.0.1:8017/api/v1"
with urlopen(API+"/health",timeout=5) as response:
    assert json.load(response)["qa_mode"]
root=Path(__file__).resolve().parents[1]
output=root/"artifacts/phase789"
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",args=["--use-fake-device-for-media-stream","--use-fake-ui-for-media-stream"])
    context=browser.new_context(viewport={"width":390,"height":900},accept_downloads=True)
    context.grant_permissions(["microphone"],origin=BASE)
    external=[]
    def local(route):
        if urlparse(route.request.url).hostname in {"localhost","127.0.0.1"} and api_matches(route.request.url,API): route.continue_()
        else:
            external.append(route.request.url)
            route.abort()
    context.route("**/*",local)
    page=context.new_page()
    page.goto(BASE+"/#audio")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button",name="Record microphone",exact=True).click()
    expect(page.get_by_role("button",name="Stop recording",exact=True)).to_be_visible()
    page.wait_for_timeout(1200)
    page.get_by_role("button",name="Stop recording",exact=True).click()
    recording=page.get_by_label("Your microphone recording",exact=True)
    expect(recording).to_be_visible()
    assert recording.get_attribute("src").startswith("blob:")
    assert page.get_by_role("link",name="Save recording to this computer",exact=True).count()==0
    page.get_by_label("Keep my own copy",exact=True).check()
    with page.expect_download() as saved:
        page.get_by_role("link",name="Save recording to this computer",exact=True).click()
    saved.value.save_as(str(output/"simulated-microphone.webm"))
    with page.expect_request(lambda request: request.url==API+"/audio/transcriptions") as submitted:
        page.get_by_role("button",name="Send to local Japanese STT",exact=True).click()
    payload=submitted.value.post_data_json
    data=base64.b64decode(payload["audio_base64"])
    with wave.open(io.BytesIO(data),"rb") as audio:
        assert audio.getframerate()==16000 and audio.getsampwidth()==2 and audio.getnchannels()==1
        duration=audio.getnframes()/audio.getframerate()
        assert 0<duration<=20
    expect(page.locator(".recorder [role=alert]")).to_be_visible()
    expect(recording).to_be_visible()
    page.get_by_role("button",name="Delete recording",exact=True).click()
    expect(recording).to_have_count(0)
    page.get_by_role("button",name="Record microphone",exact=True).click()
    expect(page.get_by_role("button",name="Cancel recording",exact=True)).to_be_visible()
    page.get_by_role("button",name="Cancel recording",exact=True).click()
    expect(recording).to_have_count(0)
    assert not external
    page.screenshot(path=str(output/"recording-simulated-390.png"),full_page=True)
    (output/"recording-results.json").write_text(json.dumps({"source":"browser fake media device; not human microphone evidence","wav_rate":16000,"wav_channels":1,"duration":duration,"retention":"explicit local download tested; delete/cancel remove tab copy","stt":"disabled fallback; no real transcription","external_requests":external},indent=2),encoding="utf-8")
    print("PASS: simulated capture/playback URL, WAV conversion, explicit retention, disabled-STT fallback, delete and cancel")
    browser.close()
