import { renderToStaticMarkup } from 'react-dom/server'
import { expect, it } from 'vitest'
import { ExerciseSchema } from './schemas'
import { answerReady, ExerciseRenderer } from './ExerciseRenderer'
import { CardSchema } from './practiceSchemas'
import { PracticeChoices } from './PracticeChoices'
const base={id:'dialogue',prompt:'Choose a polite response',objective:'Make a first introduction',concepts:['politeness'],difficulty:1,skill:'meaning',preparation:[],policy:{script:'any',normalization:'NFC',trim:true,punctuation:'ignore_terminal',case_sensitive:false,strategy:'choice',spacing:'preserve',hint_policy:'always_available',required_distinctions:[]}}
it('renders stable-ID response selection and requires an actual listed option',()=>{
 const exercise=ExerciseSchema.parse({...base,type:'response_selection',choices:[{id:'polite',text:'ミナです。'},{id:'other',text:'おやすみなさい。'}]})
 expect(answerReady(exercise,'polite')).toBe(true)
 expect(answerReady(exercise,'invented')).toBe(false)
 const html=renderToStaticMarkup(<ExerciseRenderer exercise={exercise} value="polite" onChange={()=>{}} disabled={false} onComposition={()=>{}}/>)
 expect(html).toContain('aria-pressed="true"')
 expect(html).toContain('ミナです。')
 expect(ExerciseSchema.safeParse({...base,type:'response_selection'}).success).toBe(false)
})
it('constrained authored replies use Japanese typing and retain IME instructions',()=>{
 for(const type of ['dialogue_completion','constrained_roleplay']){
  const exercise=ExerciseSchema.parse({...base,type})
  expect(answerReady(exercise,'')).toBe(false)
  expect(answerReady(exercise,'水をください。')).toBe(true)
  const html=renderToStaticMarkup(<ExerciseRenderer exercise={exercise} value="水をください。" onChange={()=>{}} disabled={false} onComposition={()=>{}}/>)
  expect(html).toContain('lang="ja"')
  expect(html).toContain('IME conversion')
 }
})
it('rejects unknown review sources and malformed scheduler receipts',()=>{
 const card={id:'card',item_id:'word',item_kind:'word',direction:'meaning',prompt:'こんにちは',answer:'Hello',due:null,revision:0,scheduled:false,state:{},scheduler:{version:'6.3.2'}}
 const parsed=CardSchema.safeParse(card)
 expect(parsed.success).toBe(true)
 if(parsed.success)expect('supports_recording' in parsed.data).toBe(false)
 expect(CardSchema.safeParse({...card,item_kind:'ai-generated'}).success).toBe(false)
 expect(CardSchema.safeParse({...card,revision:'client-supplied'}).success).toBe(false)
})
it('describes speaking practice honestly without recording or transcript claims',()=>{
 const html=renderToStaticMarkup(<PracticeChoices courseId="ja-starter"/>)
 expect(html).toContain('Bundled reference models, self-practice aloud and typed practice. No pronunciation score.')
 expect(html).not.toContain('Local recording')
 expect(html).not.toContain('transcript comparison')
})
