"""Isolated server-recorded recall timing checks; no real provider required."""
import json,sys
from pathlib import Path
from urllib.request import urlopen
from playwright.sync_api import expect,sync_playwright
sys.stdout.reconfigure(encoding='utf-8')
BASE='http://127.0.0.1:5187';API='http://127.0.0.1:8017/api/v1'
with urlopen(API+'/health',timeout=5) as response:assert json.load(response)['qa_mode']
output=Path(__file__).resolve().parents[1]/'artifacts/phase789-followup';output.mkdir(parents=True,exist_ok=True)
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
    page=browser.new_page(viewport={'width':390,'height':900});page.set_default_timeout(12000)
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)));layouts=[]
    def capture(name):
        (output/f'{name}.html').write_text(page.content(),encoding='utf-8')
        for width in [320,390,768,1280]:
            page.set_viewport_size({'width':width,'height':900})
            assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),(name,width)
            page.screenshot(path=str(output/f'{name}-{width}.png'),full_page=True)
            layouts.append({'surface':name,'width':width,'overflow':False})
    page.goto(BASE+'/#review');page.wait_for_load_state('networkidle')
    page.get_by_role('button',name='Add or open card',exact=True).click()
    before=page.request.get(API+'/progress').json()['total_xp']
    with page.expect_response(lambda r:'/session' in r.url and r.request.method=='POST') as saved:
        page.get_by_role('button',name='Start optional recall timer',exact=True).click()
    timer=saved.value.json();identity=timer['id'];card=timer['source_id']
    page.get_by_role('button',name='Pause elapsed time',exact=True).click()
    expect(page.get_by_role('button',name='Resume elapsed time',exact=True)).to_be_visible()
    page.get_by_role('button',name='Hide elapsed time',exact=True).click()
    capture('recall-timer-hidden')
    page.goto(BASE+'/#session/'+identity);page.wait_for_load_state('networkidle')
    page.get_by_role('link',name='Return to this recall card',exact=True).click()
    expect(page.get_by_role('button',name='Show elapsed time',exact=True)).to_be_visible()
    page.get_by_role('button',name='Show elapsed time',exact=True).click()
    page.get_by_role('button',name='Resume elapsed time',exact=True).click()
    page.get_by_role('button',name='Reveal answer',exact=True).click()
    page.get_by_role('button',name='Good',exact=True).click()
    expect(page.get_by_text('Review saved.',exact=False)).to_be_visible()
    assert page.request.get(API+'/progress').json()['total_xp']==before+5
    done=page.request.get(API+'/sessions/'+identity).json()
    assert done['status']=='completed' and not done['timer']['running']
    page.get_by_text('Timed session history',exact=True).click()
    assert any(row['id']==identity for row in page.request.get(API+'/personal').json()['timing_records'])
    expect(page.get_by_text('Voluntary recall · self-rated',exact=True).first).to_be_visible()
    capture('recall-timing-personal-record')
    schedule=page.request.get(API+'/review/cards/'+card).json()
    page.get_by_role('button',name='Start optional recall timer',exact=True).click()
    page.get_by_role('button',name='Skip card · keep schedule',exact=True).click()
    expect(page.get_by_role('button',name='Reveal answer',exact=True)).not_to_be_visible()
    assert page.request.get(API+'/review/cards/'+card).json()==schedule
    assert page.request.get(API+'/progress').json()['total_xp']==before+5
    assert not errors,errors
    (output/'recall-results.json').write_text(json.dumps({'layouts':layouts,'page_errors':errors,'timing':'server intervals; hide/pause/resume/reopen/rating; skip has no schedule or XP change'},indent=2),encoding='utf-8')
    print(json.dumps({'layouts':len(layouts),'errors':errors}));browser.close()
