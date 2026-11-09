import { renderToStaticMarkup } from 'react-dom/server'
import { expect, it } from 'vitest'
import { ExerciseSchema } from './schemas'
import { answerReady, ExerciseRenderer } from './ExerciseRenderer'
const base={id:'listen',prompt:'Listen',objective:'Recognize the authored phrase',concepts:['politeness'],difficulty:1,skill:'listening',preparation:[],policy:{script:'any',normalization:'NFC',trim:true,punctuation:'ignore_terminal',case_sensitive:false,strategy:'choice',spacing:'preserve',hint_policy:'always_available',required_distinctions:[]},audio:[{id:'reference',label:'Clip A'}]}
it('audio selection and contrast retain stable choice IDs and explicit text fallback',()=>{
 for(const type of ['listening_selection','audio_contrast']){
  const exercise=ExerciseSchema.parse({...base,type,choices:[{id:'a',text:'Aki'},{id:'b',text:'Haru'}]})
  expect(answerReady(exercise,'a')).toBe(true)
  expect(answerReady(exercise,'invented')).toBe(false)
  const html=renderToStaticMarkup(<ExerciseRenderer exercise={exercise} value="" onChange={()=>{}} disabled={false} onComposition={()=>{}}/>)
  expect(html).toContain('Use text alternative')
  expect(html).toContain('Prepare Clip A')
  expect(html).toContain('not proof of hearing')
 }
})
it('dictation is typed with IME guidance and does not require audio success to enter an answer',()=>{
 const exercise=ExerciseSchema.parse({...base,type:'dictation'})
 expect(answerReady(exercise,'')).toBe(false)
 expect(answerReady(exercise,'ありがとうございます')).toBe(true)
 const html=renderToStaticMarkup(<ExerciseRenderer exercise={exercise} value="" onChange={()=>{}} disabled={false} onComposition={()=>{}}/>)
 expect(html).toContain('IME conversion')
 expect(html).toContain('lang="ja"')
 expect(html).not.toContain('autoplay')
})
