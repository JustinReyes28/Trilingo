import { expect, it } from 'vitest'
import { renderToStaticMarkup } from 'react-dom/server'
import { JapaneseText } from './JapaneseText'
import { CharacterSchema, ReadingItemSchema, ReadingWordSchema, type ReadingItem } from './readingSchemas'
import { resolveSavedReadingItems, SavedReadingItems } from './SavedReadingItems'
import { StorySchema } from './studySchemas'
const segments=[{surface:'日本',reading:'にほん',vocabulary_id:'japan'},{surface:'です。'}]
it('omits hidden readings from markup and accessible text',()=>{const html=renderToStaticMarkup(<JapaneseText segments={segments} furigana="hidden"/>);expect(html).toContain('日本');expect(html).not.toContain('にほん');expect(html).not.toContain('<rt>')})
it('shows unfamiliar readings only for words without explicit familiar self-report',()=>{expect(renderToStaticMarkup(<JapaneseText segments={segments} furigana="unfamiliar" familiarIds={new Set(['japan'])}/>)).not.toContain('にほん');expect(renderToStaticMarkup(<JapaneseText segments={segments} furigana="unfamiliar"/>)).toContain('<rt>にほん</rt>')})
it('omits optional romaji rather than hiding it in an accessible label',()=>{const sample=[{surface:'あ',reading:'a'}];expect(renderToStaticMarkup(<JapaneseText segments={sample} furigana="always"/>)).not.toContain('<rt>');expect(renderToStaticMarkup(<JapaneseText segments={sample} furigana="always" romaji/>)).toContain('<rt>a</rt>')})
it('requires honest saved evidence and validated story turn structure',()=>{expect(ReadingItemSchema.safeParse({item_kind:'word',item_id:'x',saved:true,familiar:false,evidence:'mastered',updated_at:'today'}).success).toBe(false);expect(StorySchema.safeParse({current:{id:'turn',text:'arbitrary html'}}).success).toBe(false)})

const savedCharacter=CharacterSchema.parse({id:'kana-a',surface:'あ',script:'hiragana',form:'basic',contextual_readings:['あ'],romaji:'a',meaning:null,notes:'',vocabulary_ids:[],practice_exercise_ids:['kana-check'],components:[],status:'draft'})
const savedWord=ReadingWordSchema.parse({id:'word-japan',surface:'日本',reading:'にほん',gloss:'Japan',example:[],practice_exercise_ids:[],status:'published'})
function readingBookmark(item_kind:ReadingItem['item_kind'],item_id:string,saved=true):ReadingItem {
 return {item_kind,item_id,saved,familiar:false,evidence:'self_reported',updated_at:'2026-10-25T12:00:00Z'}
}
const savedLibrary={characters:[savedCharacter],vocabulary:[savedWord],items:[readingBookmark('character','kana-a'),readingBookmark('word','word-japan'),readingBookmark('word','hidden-draft'),readingBookmark('grammar','grammar-note'),readingBookmark('word','not-saved',false)]}
const savedActions={onCharacter:()=>{},onWord:()=>{},onPractice:()=>{}}

it('resolves saved navigation by item kind and current visibility without exposing hidden drafts',()=>{
 const result=resolveSavedReadingItems(savedLibrary)
 expect(result.targets.map(target=>target.kind==='character'?target.character.id:target.word.id)).toEqual(['kana-a','word-japan'])
 expect(result.hiddenCount).toBe(1)
 const withoutDrafts=resolveSavedReadingItems({...savedLibrary,characters:[]})
 expect(withoutDrafts.targets.map(target=>target.kind)).toEqual(['word'])
 expect(withoutDrafts.hiddenCount).toBe(2)
})
it('offers individually named saved-item navigation and expandable convenience batches',()=>{
 const first=renderToStaticMarkup(<SavedReadingItems library={savedLibrary} batch={1} busy={false} {...savedActions}/>)
 expect(first).toContain('Open saved character: あ')
 expect(first).not.toContain('Find saved word: 日本')
 expect(first).toContain('Showing 1 of 2 available saved items.')
 expect(first).toContain('Show more saved items')
 expect(first).toContain('Show all saved items')
 expect(first).toContain('1 other saved items are unavailable in this view.')
 expect(first).toContain('Draft · Review pending')
 const all=renderToStaticMarkup(<SavedReadingItems library={savedLibrary} batch={20} busy={false} {...savedActions}/>)
 expect(all).toContain('Find saved word: 日本')
 expect(all).toContain('Japan · Technical practice')
 expect(all).not.toContain('Show all saved items')
})
it('keeps unavailable bookmarks out of enabled practice controls and explains the empty view',()=>{
 const hiddenOnly={characters:[],vocabulary:[],items:[readingBookmark('character','hidden-draft')]}
 const html=renderToStaticMarkup(<SavedReadingItems library={hiddenOnly} batch={10} busy={false} {...savedActions}/>)
 expect(html).toContain('0 saved items available in this view.')
 expect(html).toContain('Enable draft practice to include unreviewed entries.')
 expect(html).toContain('Save a character or word from this reading library to find it here.')
 expect(html).toMatch(/disabled=""[^>]*>Practice related saved items/)
 expect(html).not.toContain('Open saved character:')
})