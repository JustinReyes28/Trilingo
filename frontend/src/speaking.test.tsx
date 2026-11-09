import { renderToStaticMarkup } from 'react-dom/server'
import { expect, it } from 'vitest'
import { ExerciseSchema } from './schemas'
import { answerReady, ExerciseRenderer } from './ExerciseRenderer'
import { StudySchema } from './studySchemas'

it('speaking exposes authored models, explicit recording and a separate typed fallback',()=>{
 const exercise=ExerciseSchema.parse({id:'speak',type:'speaking',prompt:'Ask for water',objective:'Practice a polite request',concepts:['politeness'],difficulty:1,skill:'speaking',preparation:[],policy:{script:'japanese',normalization:'NFC',trim:true,punctuation:'ignore_terminal',case_sensitive:false,strategy:'exact',spacing:'ignore',hint_policy:'always_available',required_distinctions:[]},audio:[{id:'reference',label:'model response'}],reference_text:'水をください。'})
 expect(answerReady(exercise,'')).toBe(false)
 expect(answerReady(exercise,'水をください。')).toBe(true)
 const html=renderToStaticMarkup(<ExerciseRenderer exercise={exercise} value="" onChange={()=>{}} disabled={false} onComposition={()=>{}}/>)
 expect(html).toContain('Record microphone')
 expect(html).toContain('Typed practice · no speech assessed')
 expect(html).toContain('IME conversion')
 expect(html).toContain('水をください。')
 expect(html).not.toContain('autoplay')
 // Recorder controls must never submit the surrounding exercise form.
 expect(html.match(/<button /g)?.length).toBe(html.match(/<button type="button"/g)?.length)
})

it('saved speech feedback keeps transcript evidence outside objective grades',()=>{
 const saved=StudySchema.parse({timer:null,id:'s',course_id:'ja',content_version:'0.1.16',source_kind:'speaking',source_id:'d',kind:'speaking',title:'Speaking',status:'active',cursor:0,revision:1,next_action_id:'next',exercises:[],evidence:{speak:{responses:1,first_correct:null,first_assisted:false,last_correct:null,assisted:false,revealed:false,skipped:false,answer:null,speech_attempts:1,transcript_matches:0,last_transcript:'水',last_transcript_matches:false}},preview_draft:true,mode:'supported',feedback:{exercise_id:'speak',kind:'recorded',message:'Transcript differs',explanation:'Pronunciation unassessed',answer:null},xp_awarded:0,completed_at:null,created_at:'now',initial_correct:0,assessed_count:0,concept_coverage:{}})
 expect(saved.evidence.speak.typed_fallbacks).toBe(0)
 expect(saved.evidence.speak.first_correct).toBeNull()
 expect(saved.feedback?.kind).toBe('recorded')
})
