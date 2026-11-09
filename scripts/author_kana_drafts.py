"""Author original draft kana metadata/drills locally; never imports or touches a learner DB.

Run only when intentionally creating a new content revision. Existing non-kana data stays intact.
The generated material requires qualified review before reviewed/publication claims.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'content/courses/ja/starter.json'
ROWS = [
    ('あいうえお', ['a','i','u','e','o']), ('かきくけこ', ['ka','ki','ku','ke','ko']),
    ('さしすせそ', ['sa','shi','su','se','so']), ('たちつてと', ['ta','chi','tsu','te','to']),
    ('なにぬねの', ['na','ni','nu','ne','no']), ('はひふへほ', ['ha','hi','fu','he','ho']),
    ('まみむめも', ['ma','mi','mu','me','mo']), ('やゆよ', ['ya','yu','yo']),
    ('らりるれろ', ['ra','ri','ru','re','ro']), ('わを', ['wa','wo']), ('ん', ['n']),
]
VOICED = [
    ('がぎぐげご', ['ga','gi','gu','ge','go']), ('ざじずぜぞ', ['za','ji','zu','ze','zo']),
    ('だぢづでど', ['da','ji','zu','de','do']), ('ばびぶべぼ', ['ba','bi','bu','be','bo']),
]
COMBINATIONS = [('き','ky'),('ぎ','gy'),('し','sh'),('じ','j'),('ち','ch'),('に','ny'),
                ('ひ','hy'),('び','by'),('ぴ','py'),('み','my'),('り','ry')]

def katakana(text):
    return ''.join(chr(ord(char)+0x60) for char in text)


def main():
    course = json.loads(SOURCE.read_text(encoding='utf-8'))
    if course['version'] != '0.1.5':
        raise SystemExit('Expected source0.1.5. Review changes and choose a new revision explicitly.')
    # Stable original あ ID is retained; this is authoring, not a progress reset.
    course['characters'] = [item for item in course['characters'] if item['id'] != 'ja-char-a']
    drills = course.setdefault('practice_exercises', [])
    for script in ('hiragana','katakana'):
        convert = (lambda text:text) if script == 'hiragana' else katakana
        basics = [(convert(char),reading) for row,readings in ROWS for char,reading in zip(row,readings,strict=True)]
        variants = [(convert(char),reading,'voiced') for row,readings in VOICED for char,reading in zip(row,readings,strict=True)]
        variants += [(convert(char),reading,'semi_voiced') for char,reading in zip('ぱぴぷぺぽ',['pa','pi','pu','pe','po'],strict=True)]
        variants += [(convert(base+small),prefix+vowel,'combination') for base,prefix in COMBINATIONS for small,vowel in zip('ゃゅょ','auo',strict=True)]
        variants += [(convert(char),None,'small') for char in 'ぁぃぅぇぉゃゅょっ']
        for index,(surface,reading,form) in enumerate([(char,reading,'basic') for char,reading in basics]+variants):
            char_id = 'ja-char-a' if script=='hiragana' and surface=='あ' else 'ja-char-'+script+'-'+''.join(format(ord(char),'x') for char in surface)
            note = ''
            if surface in {'ぢ','づ','ヂ','ヅ'}:
                note = 'This is a d-row voiced form. A shared romanization does not make spellings interchangeable; learn their word context.'
            if surface in {'っ','ッ'}:
                note = 'Small tsu marks a following consonant closure/doubling in taught contexts; it is distinct from full-size tsu.'
            if form=='combination':
                note = 'The second kana is small. Keep it distinct from the two full-size kana sequence.'
            entry = {'id':char_id,'surface':surface,'script':script,'contextual_readings':[reading or surface],
                     'form':form,'romaji':reading,'meaning':None,'notes':note,'stage':'stage-a',
                     'concepts':['kana'],'vocabulary_ids':[],'practice_exercise_ids':[],
                     'stroke_asset_id':None,'status':'draft'}
            if form=='basic':
                recognition_id,typing_id=char_id+'-recognize',char_id+'-type'
                entry['practice_exercise_ids']=[recognition_id,typing_id]
                common={'objective':f'Recognize and type the {script} form for {reading}.','concepts':['kana'],
                        'difficulty':1,'preparation':[],'hint':f'Look for the taught {script} form for {reading}.',
                        'explanation':f'The taught {script} form for {reading} is {surface}.'}
                distractors=[basics[(index+1)%46][0],basics[(index+7)%46][0]]
                choices=[{'id':'c0','text':surface},{'id':'c1','text':distractors[0]},{'id':'c2','text':distractors[1]}]
                # Rotate positions deterministically rather than always presenting the key first.
                rotation=index%3
                choices=choices[rotation:]+choices[:rotation]
                drills.append({**common,'id':recognition_id,'type':'multiple_choice','skill':'recognition',
                               'prompt':f'Choose the {script} for {reading}.','choices':choices,'answer':'c0',
                               'policy':{'strategy':'choice'}})
                drills.append({**common,'id':typing_id,'type':'translation','skill':'typing',
                               'prompt':f'Type the {script} for {reading}.','answers':[surface],
                               'policy':{'strategy':'exact','script':script,'normalization':'NFC',
                                         'punctuation':'exact','spacing':'preserve',
                                         'required_distinctions':['voicing','kana_size','vowel_length','target_script']}})
            course['characters'].append(entry)
    by_surface={(entry['script'],entry['surface']):entry['id'] for entry in course['characters']}
    for entry in course['characters']:
        entry['components']=[by_surface[(entry['script'],char)] for char in entry['surface']] if entry['form']=='combination' else []
    course['version']='0.1.6'
    SOURCE.write_text(json.dumps(course,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'version':course['version'],'basic_kana':sum(c['form']=='basic' for c in course['characters']),
                      'all_character_entries':len(course['characters']),'draft_drills':len(drills),'publication':'draft only'}))

if __name__=='__main__':
    main()
