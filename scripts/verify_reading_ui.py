"""Loopback-only reading/story QA against a disposable migrated QA database."""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import expect, sync_playwright
from qa_helpers import api_matches, qa_api

parser = argparse.ArgumentParser()
parser.add_argument('--base', default='http://127.0.0.1:5184')
parser.add_argument('--api', default='http://127.0.0.1:8014/api/v1')
args = parser.parse_args()
if urlparse(args.base).hostname not in {'127.0.0.1', 'localhost'}:
    raise RuntimeError('Use a loopback QA frontend')
os.environ['TRILINGO_QA_API_BASE_URL'] = args.api
api = qa_api()
root = Path(__file__).resolve().parents[1]
output = root / 'artifacts/screenshots'
output.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, channel=os.environ.get('TRILINGO_QA_BROWSER_CHANNEL'))
    page = browser.new_page(viewport={'width': 390, 'height': 844})
    page.set_default_timeout(8000)
    errors, external, layouts = [], [], []
    page.on('pageerror', lambda error: errors.append(str(error)))
    def local_only(route):
        if urlparse(route.request.url).hostname in {'127.0.0.1', 'localhost'} and api_matches(route.request.url, api):
            route.continue_()
        else:
            external.append(route.request.url)
            route.abort()
    page.route('**/*', local_only)
    def capture(label):
        for width in (320, 390, 768, 1280):
            page.set_viewport_size({'width': width, 'height': 900})
            assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'), (label, width)
            page.screenshot(path=str(output / (label+'-'+str(width)+'.png')), full_page=True)
            layouts.append({'surface': label, 'width': width, 'overflow': False})
    def action(name):
        with page.expect_response(lambda r: '/sessions/' in r.url and r.url.endswith('/actions') and r.request.method == 'POST') as response:
            page.get_by_role('button', name=name, exact=True).click()
        assert response.value.status == 200, response.value.text()
        return response.value.json()
    setup = page.request.patch(api+'/courses/ja-starter/reading/items/character/ja-char-a', data=json.dumps({'saved':False,'preview_draft':True}), headers={'Content-Type':'application/json'})
    assert setup.status == 200
    page.request.patch(api+'/settings', data=json.dumps({'practice_batch':12}), headers={'Content-Type':'application/json'})
    page.goto(args.base+'/#reading')
    expect(page.get_by_text('No hiragana in this collection/filter yet.', exact=False)).to_be_visible()
    capture('reading-empty')
    page.get_by_label('Include draft practice', exact=False).check()
    expect(page.locator('.kana-grid li')).to_have_count(46)
    capture('reading-kana')
    # Convenience batches never cap access; local search spans the full library.
    expect(page.locator('.reading-word')).to_have_count(12)
    page.get_by_role('button', name='Show more words', exact=True).click()
    expect(page.locator('.reading-word')).to_have_count(24)
    page.get_by_role('button', name='Show all words', exact=True).click()
    expect(page.locator('.reading-word')).to_have_count(291)
    search = page.get_by_label('Find a word by Japanese, reading or meaning', exact=True)
    for term in ('皿', 'さら', 'plate; dish'):
        search.fill(term)
        expect(page.locator('.reading-word')).to_have_count(1)
        expect(page.locator('.reading-word')).to_contain_text('plate; dish')
    capture('reading-word-search')
    search.fill('no matching word exists')
    expect(page.locator('.reading-word')).to_have_count(0)
    expect(page.get_by_text('No words match this search.', exact=False)).to_be_visible()
    capture('reading-word-empty-search')
    page.get_by_role('button', name='Clear word search', exact=True).click()
    expect(search).to_be_focused()
    expect(page.locator('.reading-word')).to_have_count(12)
    first = page.locator('.kana-grid button').first
    first.focus()
    page.keyboard.press('Enter')
    expect(page.get_by_role('dialog')).to_be_visible()
    page.get_by_role('button', name='Save for practice', exact=True).click()
    expect(page.get_by_role('button', name='Saved for practice', exact=True)).to_be_visible()
    capture('reading-character')
    def fail_save(route):
        route.fulfill(status=503, content_type='application/json', body=json.dumps({'error':{'code':'qa_unavailable','message':'QA save temporarily unavailable. Retry.'}}))
    page.route('**/reading/items/character/*', fail_save)
    page.get_by_role('button', name='Saved for practice', exact=True).click()
    expect(page.get_by_role('dialog').get_by_role('alert')).to_contain_text('QA save temporarily unavailable')
    page.unroute('**/reading/items/character/*', fail_save)
    page.keyboard.press('Escape')
    expect(first).to_be_focused()
    page.reload()
    page.get_by_label('Include draft practice', exact=False).check()
    expect(page.locator('.kana-grid li')).to_have_count(46)
    page.locator('.kana-grid button').first.click()
    expect(page.get_by_role('button', name='Saved for practice', exact=True)).to_be_visible()
    page.get_by_role('button', name='Practice this character', exact=True).click()
    page.wait_for_url('**/#session/*')
    expect(page.get_by_role('heading', name='Hiragana character practice', exact=True)).to_be_visible()
    page.goto(args.base+'/#reading')
    page.get_by_label('Include draft practice', exact=False).check()
    page.get_by_label('Script', exact=True).select_option('kanji')
    page.get_by_label('Forms', exact=True).select_option('all')
    expect(page.locator('.kana-grid li')).to_have_count(300)
    page.locator('.kana-grid button').first.click()
    capture('reading-kanji')
    page.keyboard.press('Escape')
    page.get_by_role('button', name='皿 · kanji · kanji', exact=True).click()
    expect(page.get_by_role('dialog')).to_contain_text('皿（さら）')
    page.get_by_role('button', name='Practice this character', exact=True).click()
    page.wait_for_url('**/#session/*')
    page.get_by_role('button', name='さら', exact=True).click()
    assert action('Check answer')['feedback']['kind'] == 'correct'
    page.goto(args.base+'/#reading')
    page.get_by_label('Include draft practice', exact=False).check()
    page.get_by_role('button', name='Read Water or tea?', exact=True).click()
    page.wait_for_url('**/#session/*')
    expect(page.locator('.story-passage')).to_contain_text('水')
    session_url = page.url
    capture('reading-story')
    action('Hide readings')
    expect(page.locator('.story-passage rt')).to_have_count(0)
    action('Show readings')
    expect(page.locator('.story-passage rt')).to_have_count(1)
    page.get_by_role('button', name='Tea', exact=True).click()
    wrong = action('Check answer')
    assert wrong['feedback']['kind'] == 'incorrect'
    action('Continue story · skip unchecked prompts')
    page.get_by_text('Vocabulary help · records support', exact=True).click()
    aid = action('Explain お茶')
    assert aid['story']['assisted_turn_ids']
    page.get_by_role('button', name='Save word: お茶', exact=True).click()
    expect(page.get_by_role('button', name='Saved: お茶', exact=True)).to_be_visible()
    page.reload()
    expect(page.locator('.story-passage')).to_contain_text('お茶')
    action('Continue story · skip unchecked prompts')
    action('Continue story · skip unchecked prompts')
    expect(page.get_by_role('button', name='Continue story · skip unchecked prompts')).to_be_disabled()
    result = action('Finish story & save')
    assert result['xp_awarded'] == 5
    assert result['evidence']['ja-story-drink-tea']['skipped']
    capture('reading-story-complete')
    page.get_by_role('button', name='Start a new replay', exact=True).click()
    page.wait_for_url(lambda url: '#session/' in url and url != session_url)
    expect(page.locator('.story-passage')).to_contain_text('水')
    page.goto(args.base+'/#reading')
    page.get_by_label('Include draft practice', exact=False).check()
    # Explicit familiar-word state controls ruby; romaji is absent when disabled.
    page.request.patch(api+'/settings', data=json.dumps({'furigana':'unfamiliar','romaji':False}), headers={'Content-Type':'application/json'})
    page.request.patch(api+'/courses/ja-starter/reading/items/word/ja-word-japan', data=json.dumps({'familiar':True,'preview_draft':True}), headers={'Content-Type':'application/json'})
    page.reload()
    page.get_by_label('Include draft practice', exact=False).check()
    expect(page.locator('.kana-grid small')).to_have_count(0)
    page.get_by_label('Find a word by Japanese, reading or meaning', exact=True).fill('日本')
    japan = page.locator('.reading-word').filter(has=page.get_by_role('heading', name='日本', exact=True))
    expect(japan.locator('h3 rt')).to_have_count(0)
    page.evaluate("document.documentElement.style.fontSize='200%'")
    page.set_viewport_size({'width':390,'height':900})
    assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
    page.screenshot(path=str(output/'reading-zoom-390.png'), full_page=True)
    page.evaluate("document.documentElement.style.fontSize=''")
    # Exercise library failure and recovery; failure never masquerades as empty content.
    def fail_library(route):
        route.fulfill(status=503, content_type='application/json', body=json.dumps({'error':{'code':'qa_unavailable','message':'QA reading temporarily unavailable.'}}))
    page.route('**/reading?*', fail_library)
    page.reload()
    expect(page.get_by_role('alert')).to_contain_text('QA reading temporarily unavailable.')
    page.unroute('**/reading?*', fail_library)
    page.get_by_role('button', name='Reload reading library', exact=True).click()
    expect(page.get_by_text('No hiragana in this collection/filter yet.', exact=False)).to_be_visible()
    # Return isolated QA settings to predictable defaults for other scripts.
    page.request.patch(api+'/settings', data=json.dumps({'furigana':'always','romaji':True,'practice_batch':20}), headers={'Content-Type':'application/json'})
    (root/'artifacts/reading-rendered.html').write_text(page.content(), encoding='utf-8')
    assert not errors, errors
    assert not external, external
    (root/'artifacts/reading-ui-results.json').write_text(json.dumps({'layouts':layouts,'page_errors':errors,'external_requests':external,'checks':['draft guard','keyboard dialog/focus','save/reload','character practice','kanji context','story wrong/skip/help','resume/replay','acknowledged XP','unfamiliar ruby','hidden romaji','200% text','300 distinct draft kanji','Stage B direct practice','word search Japanese/kana/meaning','unrestricted Show more/all','search empty/clear/focus']}, indent=2), encoding='utf-8')
    browser.close()
print('Reading/story browser QA passed: '+str(len(layouts))+' layouts; no external requests.')
