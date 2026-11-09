"""Writing/formation browser QA. Loopback and disposable-QA guard; no downloads."""
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
args = parser.parse_args()
if urlparse(args.base).hostname not in {'localhost', '127.0.0.1'}:
    raise RuntimeError('Use a loopback QA frontend')
os.environ['TRILINGO_QA_API_BASE_URL'] = args.api
api = qa_api()
root = Path(__file__).resolve().parents[1]
output = root / 'artifacts/screenshots'
output.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, channel=os.environ.get('TRILINGO_QA_BROWSER_CHANNEL'))
    context = browser.new_context(viewport={'width':390, 'height':844})
    errors, external, layouts = [], [], []
    def local_only(route):
        if urlparse(route.request.url).hostname in {'127.0.0.1', 'localhost'} and api_matches(route.request.url, api):
            route.continue_()
        else:
            external.append(route.request.url)
            route.abort()
    context.route('**/*', local_only)
    def setup(page):
        page.set_default_timeout(10000)
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('dialog', lambda dialog: dialog.accept())
    page = context.new_page()
    setup(page)
    def capture(label, target=page):
        for width in (320,390,768,1280):
            target.set_viewport_size({'width':width, 'height':900})
            assert not target.evaluate('document.documentElement.scrollWidth>innerWidth'), (label,width)
            target.screenshot(path=str(output/(label+'-'+str(width)+'.png')), full_page=True)
            layouts.append({'surface':label,'width':width,'overflow':False})
    def saved(target=page):
        expect(target.locator('#draft-status')).to_contain_text('Saved revision')
    page.goto(args.base+'/#writing')
    expect(page.get_by_text('No published writing tasks yet.',exact=False)).to_be_visible()
    page.get_by_text('Try Japanese input & read the Windows guide',exact=True).click()
    ime = page.get_by_label('Japanese input test · not saved or graded',exact=True)
    ime.fill('にほん')
    ime.dispatch_event('compositionstart')
    ime.press('Enter')
    expect(page.get_by_text('IME composition in progress.',exact=False)).to_be_visible()
    ime.dispatch_event('compositionend')
    ime.fill('日本\nかな')
    expect(ime).to_have_value('日本\nかな')
    page.get_by_label('Include draft writing tasks',exact=False).check()
    expect(page.locator('.writing-task')).to_have_count(7)
    capture('writing-home')
    task = page.locator('.writing-task').filter(has=page.get_by_role('heading',name='Introduction',exact=True))
    task.get_by_role('button',name='Start an unassessed draft',exact=True).click()
    page.wait_for_url('**/#writing/*')
    editor_url = page.url
    draft_id = editor_url.split('/')[-1]
    editor = page.get_by_label('Your Japanese draft',exact=True)
    expect(editor).to_have_value('')
    baseline = page.request.get(api+'/progress').json()['total_xp']
    editor.dispatch_event('compositionstart')
    editor.fill('アキです。')
    editor.press('Enter')
    page.wait_for_timeout(1100)
    assert page.request.get(api+'/writing/drafts/'+draft_id).json()['current']['text'] == ''
    editor.dispatch_event('compositionend')
    saved()
    expect(editor).to_have_value('アキです。\n')
    page.get_by_role('button',name='Show draft writing model',exact=True).click()
    saved()
    capture('writing-editor')
    page.get_by_role('button',name='Hide writing model',exact=True).click()
    # Lost acknowledgement: retry must save the exact request; later typing gets a later revision.
    dropped=[False]
    def lose_save(route):
        if not dropped[0]:
            dropped[0]=True
            route.fetch()
            route.abort()
        else:
            route.continue_()
    page.route('**/writing/drafts/*/revisions',lose_save)
    editor.fill('アキです。\nシンガポールに住んでいます。')
    expect(page.get_by_role('button',name='Retry interrupted writing action',exact=True)).to_be_visible()
    editor.fill('アキです。\nシンガポールに住んでいます。\nお茶が好きです。')
    page.unroute('**/writing/drafts/*/revisions',lose_save)
    page.get_by_role('button',name='Retry interrupted writing action',exact=True).click()
    saved()
    assert page.request.get(api+'/writing/drafts/'+draft_id).json()['current']['text'].endswith('お茶が好きです。')
    assert page.request.get(api+'/progress').json()['total_xp'] == baseline
    # A separate tab has its own unsaved recovery buffer and stale base revision.
    second=context.new_page()
    setup(second)
    second.goto(editor_url)
    other=second.get_by_label('Your Japanese draft',exact=True)
    expect(other).to_have_value('アキです。\nシンガポールに住んでいます。\nお茶が好きです。')
    editor.fill('タブAで保存した文章。')
    saved()
    other.fill('タブBで書いた文章。')
    expect(second.get_by_role('heading',name='Keep both, then choose your revision',exact=True)).to_be_visible()
    expect(second.get_by_label('Saved text from the other revision',exact=True)).to_have_value('タブAで保存した文章。')
    expect(other).to_have_value('タブBで書いた文章。')
    capture('writing-conflict',second)
    second.reload()
    expect(second.get_by_role('heading',name='Keep both, then choose your revision',exact=True)).to_be_visible()
    expect(second.get_by_label('Your Japanese draft',exact=True)).to_have_value('タブBで書いた文章。')
    second.get_by_role('button',name='Save my editor text as a new revision',exact=True).click()
    saved(second)
    history=second.request.get(api+'/writing/drafts/'+draft_id+'/history').json()
    assert any(rev['text']=='タブAで保存した文章。' for rev in history['revisions'])
    assert any(item['text']=='タブBで書いた文章。' for item in history['conflicts'])
    # A committed submission's lost response cannot duplicate the reward.
    dropped_submit=[False]
    def lose_submit(route):
        if not dropped_submit[0]:
            dropped_submit[0]=True
            route.fetch()
            route.abort()
        else:
            route.continue_()
    second.route('**/writing/drafts/*/submissions',lose_submit)
    second.get_by_role('button',name='Submit saved writing practice',exact=True).click()
    expect(second.get_by_role('button',name='Retry interrupted writing action',exact=True)).to_be_visible()
    second.get_by_label('Your Japanese draft',exact=True).fill('タブBの次の下書き。')
    second.unroute('**/writing/drafts/*/submissions',lose_submit)
    second.get_by_role('button',name='Retry interrupted writing action',exact=True).click()
    saved(second)
    assert second.request.get(api+'/progress').json()['total_xp'] == baseline+5
    with second.expect_response(lambda response: response.url.endswith('/submissions') and response.request.method=='POST') as new_submission:
        second.get_by_role('button',name='Submit again as a new practice session',exact=True).click()
    assert new_submission.value.status==200
    expect(second.get_by_text('Practice saved · +5 XP',exact=True)).to_be_visible()
    assert second.request.get(api+'/progress').json()['total_xp'] == baseline+10
    capture('writing-submitted',second)
    second.close()
    # Aid support is acknowledged before display and is recorded again for each prompt.
    from uuid import uuid4
    started=page.request.post(api+'/courses/ja-starter/sessions',data=json.dumps({'request_id':str(uuid4()),'source_id':'ja-greetings-hello'}),headers={'Content-Type':'application/json'}).json()
    exercise_id=started['exercises'][1]['id']
    visit=page.request.post(api+'/sessions/'+started['id']+'/actions',data=json.dumps({'request_id':started['next_action_id'],'expected_revision':started['revision'],'action':'visit','exercise_id':exercise_id}),headers={'Content-Type':'application/json'})
    assert visit.status==200
    page.goto(args.base+'/#session/'+started['id'])
    page.get_by_text('On-screen kana input aid · draft reference',exact=True).click()
    def fail_support(route):
        route.fulfill(status=503,content_type='application/json',body=json.dumps({'error':{'code':'qa_unavailable','message':'QA support unavailable.'}}))
    page.route('**/sessions/*/actions',fail_support)
    page.get_by_role('button',name='Load draft kana input aid',exact=True).click()
    expect(page.get_by_text('Support was not saved.',exact=False)).to_be_visible()
    expect(page.locator('.kana-input-grid')).to_have_count(0)
    page.unroute('**/sessions/*/actions',fail_support)
    page.get_by_role('button',name='Reload saved session',exact=True).click()
    expect(page.get_by_role('button',name='Load draft kana input aid',exact=True)).to_be_enabled()
    page.get_by_role('button',name='Load draft kana input aid',exact=True).click()
    expect(page.locator('.kana-input-grid')).to_be_visible()
    page.get_by_role('button',name='Skip prompt',exact=True).click()
    expect(page.locator('.kana-input-grid')).to_have_count(0)
    page.get_by_text('On-screen kana input aid · draft reference',exact=True).click()
    page.get_by_role('button',name='Load draft kana input aid',exact=True).click()
    page.get_by_role('button',name='Insert ち',exact=True).click()
    expect(page.get_by_label('Your answer',exact=True)).to_have_value('ち')
    page.get_by_role('button',name='Insert は',exact=True).click()
    expect(page.get_by_label('Your answer',exact=True)).to_have_value('ちは')
    with page.expect_response(lambda response: response.url.endswith('/actions') and response.request.method=='POST') as checked:
        page.get_by_role('button',name='Check answer',exact=True).click()
    aid_result=checked.value.json()
    assert aid_result['feedback']['kind']=='correct'
    assert aid_result['evidence'][aid_result['exercises'][2]['id']]['first_assisted']
    page.goto(args.base+'/#writing/drawing')
    page.get_by_label('Include draft character templates',exact=False).check()
    expect(page.locator('.drawing-pad').first).to_be_visible()
    expect(page.get_by_role('heading',name='い',exact=True)).to_be_visible()
    capture('writing-formation')
    page.set_viewport_size({'width':390,'height':900})
    pad=page.locator('.drawing-pad').first
    pad.scroll_into_view_if_needed()
    box=pad.bounding_box()
    assert box
    for start,end in [((.3,.2),(.35,.75)),((.65,.25),(.70,.60))]:
        page.mouse.move(box['x']+box['width']*start[0],box['y']+box['height']*start[1])
        page.mouse.down()
        page.mouse.move(box['x']+box['width']*end[0],box['y']+box['height']*end[1],steps=12)
        page.mouse.up()
    expect(page.get_by_text('2 strokes · pointer coordinates',exact=False)).to_be_visible()
    # Character and preview transitions protect the unsaved grid.
    page.get_by_label('Character to practice',exact=True).select_option(label='こ · hiragana · Draft guide')
    expect(page.get_by_role('dialog',name='Leave the current drawing?',exact=True)).to_be_visible()
    page.get_by_role('button',name='Keep current drawing',exact=True).click()
    expect(page.get_by_role('heading',name='い',exact=True)).to_be_visible()
    page.get_by_label('Include draft character templates',exact=False).click()
    expect(page.get_by_role('dialog',name='Leave the current drawing?',exact=True)).to_be_visible()
    page.get_by_role('button',name='Keep current drawing',exact=True).click()
    expect(page.get_by_label('Include draft character templates',exact=False)).to_be_checked()
    page.get_by_role('button',name='Clear drawing',exact=True).click()
    expect(page.get_by_role('dialog',name='Clear this unsaved drawing?',exact=True)).to_be_visible()
    page.get_by_role('button',name='Keep drawing',exact=True).click()
    page.get_by_role('button',name='Replay my strokes',exact=True).click()
    expect(page.get_by_role('button',name='Stop stroke replay',exact=True)).to_be_visible()
    page.get_by_role('button',name='Stop stroke replay',exact=True).click()
    page.get_by_label('Keep an optional local drawing sample',exact=True).check()
    drawing_dropped=[False]
    def lose_drawing(route):
        if not drawing_dropped[0]:
            drawing_dropped[0]=True
            route.fetch()
            route.abort()
        else:
            route.continue_()
    page.route('**/writing/handwriting',lose_drawing)
    page.get_by_role('button',name='Record this practice activity',exact=True).click()
    expect(page.get_by_role('button',name='Retry recording this activity',exact=True)).to_be_visible()
    expect(page.get_by_label('Keep an optional local drawing sample',exact=True)).to_be_disabled()
    expect(page.get_by_label('Keep an optional local drawing sample',exact=True)).to_be_checked()
    expect(page.get_by_label('Your self-check',exact=True)).to_be_disabled()
    expect(page.get_by_label('Character to practice',exact=True)).to_be_disabled()
    expect(page.get_by_label('Include draft character templates',exact=False)).to_be_disabled()
    raw_pending=page.evaluate('Object.fromEntries(Object.entries(localStorage).filter(([key])=>key.includes("drawing")))')
    assert all('strokes' not in value for value in raw_pending.values())
    page.unroute('**/writing/handwriting',lose_drawing)
    page.get_by_role('button',name='Retry recording this activity',exact=True).click()
    expect(page.get_by_text('Activity saved · +5 XP',exact=True)).to_be_visible()
    assert page.request.get(api+'/progress').json()['total_xp']==baseline+15
    expect(page.get_by_text('Guided tracing feedback:',exact=False)).to_be_visible()
    # Browser recovery stores only the receipt identity, never raw drawing coordinates.
    raw=page.evaluate('Object.fromEntries(Object.entries(localStorage).filter(([key])=>key.includes("drawing")))')
    assert all('strokes' not in value for value in raw.values())
    page.get_by_role('button',name='Load saved drawing samples',exact=True).click()
    expect(page.locator('.drawing-samples article')).to_have_count(1)
    page.get_by_role('button',name='Delete optional sample',exact=True).click()
    expect(page.get_by_role('dialog',name='Delete this optional sample?',exact=True)).to_be_visible()
    page.get_by_role('button',name='Delete this sample',exact=True).click()
    expect(page.get_by_text('No saved drawing samples.',exact=False)).to_be_visible()
    page.get_by_label('Practice mode',exact=True).select_option('accessible_sequence')
    page.get_by_role('button',name='Start new mode with a clear grid',exact=True).click()
    page.get_by_role('button',name='Select stroke 2',exact=True).focus()
    page.keyboard.press('Enter')
    page.get_by_role('button',name='Select stroke 1',exact=True).click()
    page.get_by_role('button',name='Record this practice activity',exact=True).click()
    expect(page.get_by_text('This keyboard activity does not measure handwriting.',exact=False)).to_be_visible()
    capture('writing-sequence')
    page.evaluate("document.documentElement.style.fontSize='200%'")
    page.set_viewport_size({'width':390,'height':900})
    assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
    page.screenshot(path=str(output/'writing-zoom-390.png'),full_page=True)
    page.evaluate("document.documentElement.style.fontSize=''")
    (root/'artifacts/writing-rendered.html').write_text(page.content(),encoding='utf-8')
    assert not errors, errors
    assert not external, external
    (root/'artifacts/writing-ui-results.json').write_text(json.dumps({'layouts':layouts,'page_errors':errors,'external_requests':external,'checks':['draft guard','IME Enter/autosave','lost save acknowledgement','typing during retry','two-tab conflict/reload/merge','idempotent submission','new genuine submission XP','pointer strokes/replay/confirmed clear','optional sample/delete','keyboard sequence','raw drawing recovery privacy','acknowledged kana aid per prompt/failure recovery','confirmed character/preview changes','frozen pending drawing choices','200% text']},indent=2),encoding='utf-8')
    context.close()
    browser.close()
print('Writing browser QA passed: '+str(len(layouts))+' layouts; no external requests.')
