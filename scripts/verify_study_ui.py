"""Real Phase 4 browser flow. Requires a migrated disposable QA instance; never installs assets."""
import argparse
import json
import os
import re
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import expect, sync_playwright

from qa_helpers import api_matches, qa_api

parser = argparse.ArgumentParser()
parser.add_argument('--base', default='http://127.0.0.1:5184')
parser.add_argument('--api', default='http://127.0.0.1:8014/api/v1')
parser.add_argument('--browser-executable')
args = parser.parse_args()
if urlparse(args.base).hostname not in {'localhost', '127.0.0.1'}:
    raise RuntimeError('Use a loopback QA frontend')
os.environ['TRILINGO_QA_API_BASE_URL'] = args.api
api = qa_api()
root = Path(__file__).resolve().parents[1]
output = root / 'artifacts/screenshots'
output.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path=args.browser_executable, channel=None if args.browser_executable else os.environ.get('TRILINGO_QA_BROWSER_CHANNEL'))
    page = browser.new_page(viewport={'width': 390, 'height': 844})
    page.set_default_timeout(7000)
    errors, external, layouts = [], [], []
    page.on('pageerror', lambda error: errors.append(str(error)))
    def local_only(route):
        url = route.request.url
        if urlparse(url).hostname in {'127.0.0.1', 'localhost'} and api_matches(url, api):
            route.continue_()
        else:
            external.append(url)
            route.abort()
    page.route('**/*', local_only)
    page.goto(args.base)
    page.wait_for_load_state('networkidle')
    page.get_by_role('button', name=re.compile(r'^Notice sound differences\.')).click()
    page.get_by_role('button', name='Start lesson', exact=True).click()
    page.wait_for_url('**/#session/*')
    page.locator('.question-frame').wait_for()
    later_url = page.url
    page.get_by_role('button', name='Pause and leave', exact=True).click()
    page.wait_for_url('**/#learn')
    page.get_by_role('button', name=re.compile(r'^Say hello\.')).click()
    page.get_by_role('button', name='Start lesson', exact=True).click()
    page.wait_for_url('**/#session/*')
    page.locator('.question-frame').wait_for()
    session_url = page.url
    session_id = session_url.split('/')[-1]
    initial = page.request.get(api + '/sessions/' + session_id).json()
    baseline = page.request.get(api + '/progress').json()['total_xp']
    def click_action(name):
        with page.expect_response(lambda r: '/sessions/' in r.url and r.url.endswith('/actions') and r.request.method == 'POST') as response:
            page.get_by_role('button', name=name, exact=True).click()
        assert response.value.status == 200, response.value.text()
        return response.value.json()
    def capture(label):
        for width in (320, 390, 640, 768, 1024, 1280, 1440, 1536):
            page.set_viewport_size({'width': width, 'height': 900})
            assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'), (label, width)
            page.screenshot(path=str(output / f'{label}-{width}.png'), full_page=True)
            layouts.append({'surface': label, 'width': width, 'overflow': False})
    capture('study-choice')
    page.get_by_role('button', name='ありがとう', exact=True).click()
    dropped = [False]
    def lost_response(route):
        if not dropped[0]:
            dropped[0] = True
            route.fetch()
            route.abort()
        else:
            route.continue_()
    page.route('**/sessions/*/actions', lost_response)
    page.get_by_role('button', name='Check answer', exact=True).click()
    expect(page.get_by_role('button', name='Retry saved action')).to_be_visible()
    page.unroute('**/sessions/*/actions', lost_response)
    saved = click_action('Retry saved action')
    first_key = saved['exercises'][0]['id']
    assert saved['evidence'][first_key]['responses'] == 1
    for _ in range(2):
        saved = click_action('Check answer')
    assert saved['evidence'][first_key]['responses'] == 3
    click_action('Show hint')
    revealed = click_action('Reveal answer & explanation')
    assert revealed['evidence'][first_key]['assisted']
    expect(page.get_by_text('Answer revealed', exact=True)).to_be_visible()
    click_action('Continue')
    field = page.get_by_label('Your answer')
    field.fill('こんにちは')
    field.dispatch_event('compositionstart')
    field.press('Enter')
    expect(page.get_by_role('button', name='Check answer', exact=True)).to_be_disabled()
    field.dispatch_event('compositionend')
    field.fill('こんにちは')
    typed = click_action('Check answer')
    assert typed['feedback']['kind'] == 'correct'
    page.reload()
    expect(page.get_by_label('Your answer')).to_have_value('こんにちは')
    field = page.get_by_label('Your answer')
    field.fill('まだ')
    expect(page.get_by_text('Changes are not checked or saved. Use Check answer when ready.', exact=True)).to_be_visible()
    expect(page.get_by_text('Previous saved result: Correct', exact=True)).to_be_visible()
    field.fill('こんにちは')
    capture('study-typed')
    click_action('Continue')
    # A deliberate skip remains unassessed and never blocks the remaining prompts.
    click_action('Skip prompt')
    page.get_by_role('button', name='Add part 1: 。', exact=True).click()
    page.get_by_role('button', name='Add part 2: こんにちは', exact=True).click()
    assert click_action('Check answer')['feedback']['kind'] == 'incorrect'
    page.get_by_role('button', name='Move part 2 earlier', exact=True).focus()
    page.keyboard.press('Enter')
    assert click_action('Check answer')['feedback']['kind'] == 'correct'
    capture('study-ordering')
    click_action('Continue')
    page.get_by_label('こんにちは', exact=True).select_option(label='Hello')
    page.get_by_label('さようなら', exact=True).select_option(label='Goodbye')
    assert click_action('Check answer')['feedback']['kind'] == 'correct'
    capture('study-matching')
    click_action('Continue')
    complete = click_action('Finish and save session')
    amount = 5 if initial['kind'] == 'replay' else 20
    assert complete['xp_awarded'] == amount
    expect(page.get_by_role('heading', name='Session saved', exact=True)).to_be_visible()
    page.reload()
    expect(page.get_by_role('heading', name='Session saved', exact=True)).to_be_visible()
    assert page.request.get(api + '/progress').json()['total_xp'] == baseline + amount
    capture('study-completed')
    page.get_by_role('button', name='Start a new replay', exact=True).click()
    page.wait_for_url(lambda url: '#session/' in url and url != session_url)
    for _ in range(5):
        click_action('Skip prompt')
    replay = click_action('Finish and save session')
    assert replay['xp_awarded'] == 5
    assert page.request.get(api + '/progress').json()['total_xp'] == baseline + amount + 5
    page.goto(args.base + '/#practice')
    expect(page.get_by_role('heading', name='Mistakes you can revisit')).to_be_visible()
    capture('study-practice')
    page.get_by_label('Self-check support', exact=True).select_option('unassisted')
    page.get_by_role('button', name='Try draft self-check', exact=True).first.click()
    page.wait_for_url('**/#session/*')
    expect(page.get_by_text('Draft practice · Japanese review pending', exact=True)).to_be_visible()
    click_action('Use supported practice')
    expect(page.get_by_role('button', name='Use supported practice', exact=True)).to_have_count(0)
    page.goto(args.base + '/#practice')
    placement = page.locator('.assessment-row').filter(has=page.get_by_role('heading', name='Find a useful starting point', exact=True))
    placement.get_by_role('button', name='Try draft self-check', exact=True).click()
    page.wait_for_url('**/#session/*')
    for _ in range(4):
        click_action('Skip prompt')
    placed = click_action('Finish and save session')
    assert placed['recommendation'] and 'skipped' in placed['recommendation']['reason']
    capture('study-placement')
    page.get_by_role('button', name='Start suggested lesson', exact=True).click()
    page.wait_for_url(lambda url: '#session/' in url and url.split('/')[-1] != placed['id'])
    page.locator('.question-frame').wait_for()
    page.goto(session_url)
    expect(page.get_by_role('heading', name='Session saved', exact=True)).to_be_visible()
    page.set_viewport_size({'width': 320, 'height': 900})
    page.add_style_tag(content='html{font-size:200% !important}')
    assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
    page.screenshot(path=str(output / 'study-text-200.png'), full_page=True)
    # Hold real requests so pending state cannot impersonate an empty result.
    page.add_style_tag(content='html{font-size:100% !important}')
    pending_routes = []
    holding = [True]
    practice_pattern = re.compile(r'/api/v1/courses/[^/]+/(assessments|mistakes)(\?.*)?$')
    def hold_practice(route):
        if holding[0]:
            pending_routes.append(route)
        else:
            route.fulfill(status=200, content_type='application/json', body='[]')
    page.route(practice_pattern, hold_practice)
    page.goto(args.base + '/#practice')
    expect(page.get_by_text('Loading your saved mistakes…', exact=True)).to_be_visible()
    expect(page.get_by_text('No incorrect responses recorded yet. Skips and assisted answers are separate evidence.', exact=True)).to_have_count(0)
    expect(page.get_by_text('No self-checks in this course yet.', exact=True)).to_have_count(0)
    holding[0] = False
    for route in pending_routes:
        route.fulfill(status=200, content_type='application/json', body='[]')
    expect(page.get_by_text('No self-checks in this course yet.', exact=True)).to_be_visible()
    expect(page.get_by_text('No incorrect responses recorded yet. Skips and assisted answers are separate evidence.', exact=True)).to_be_visible()
    page.unroute(practice_pattern)
    detail_url = api + '/sessions/' + session_id
    page.route(detail_url, lambda route: route.abort())
    page.goto(session_url)
    expect(page.get_by_text('Use Reload saved session to try opening this session again.', exact=True)).to_be_visible()
    expect(page.get_by_text('Opening your saved session…', exact=True)).to_have_count(0)
    page.unroute(detail_url)
    page.get_by_role('button', name='Reload saved session', exact=True).click()
    expect(page.get_by_role('heading', name='Session saved', exact=True)).to_be_visible()
    back_link = page.get_by_role('link', name='Course path', exact=True)
    back_link.focus()
    assert back_link.bounding_box()['height'] >= 44
    (root / 'artifacts/study-rendered.html').write_text(page.content(), encoding='utf-8')
    assert not errors, errors
    assert not external, external
    result={'layouts': layouts, 'errors': errors, 'external_requests': external,
            'saved_session': session_url, 'later_session': later_url,
            'lost_response_recovery': True, 'ime_composition_guard': True,
            'all_five_renderers': True, 'replay_xp': 5,
            'loading_empty_error_recovery': True, 'edited_answer_state': True}
    (root / 'artifacts/study-ui-results.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({**{k:v for k,v in result.items() if k!='layouts'}, 'layouts_checked':len(layouts)}, indent=2))
    browser.close()
