import { renderToStaticMarkup } from 'react-dom/server'
import { expect, it } from 'vitest'
import { ExerciseSchema } from './schemas'
import { answerReady, ExerciseRenderer } from './ExerciseRenderer'
import { CardSchema, PersonalSchema } from './practiceSchemas'
import { ReviewMedia } from './ReviewMedia'
import { SessionCompletion } from './SessionCompletion'
import { StudySchema } from './studySchemas'

it('speaking exposes authored models, bundled audio cues and typed practice without microphone recording',()=>{
 const exercise=ExerciseSchema.parse({id:'speak',type:'speaking',prompt:'Ask for water',objective:'Practice a polite request',concepts:['politeness'],difficulty:1,skill:'speaking',preparation:[],policy:{script:'japanese',normalization:'NFC',trim:true,punctuation:'ignore_terminal',case_sensitive:false,strategy:'exact',spacing:'ignore',hint_policy:'always_available',required_distinctions:[]},audio:[{id:'reference',label:'model response'}],reference_text:'水をください。'})
 expect(answerReady(exercise,'')).toBe(false)
 expect(answerReady(exercise,'水をください。')).toBe(true)
 const html=renderToStaticMarkup(<ExerciseRenderer exercise={exercise} value="" onChange={()=>{}} disabled={false} onComposition={()=>{}}/>)
 expect(html).not.toContain('Record microphone')
 expect(html).not.toContain('Your recording')
 expect(html).not.toContain('local Japanese STT')
 expect(html).toContain('Typed practice · no speech assessed')
 expect(html).toContain('IME conversion')
 expect(html).toContain('水をください。')
 expect(html).toContain('Bundled reference audio · human Japanese listening review pending.')
 expect(html).not.toContain('Synthetic')
 expect(html).not.toContain('autoplay')
 // Listening cue controls must never submit the surrounding exercise form.
 expect(html.match(/<button /g)?.length).toBe(html.match(/<button type="button"/g)?.length)
})

it('ReviewMedia keeps bundled reference playback and text reveal without microphone recording',()=>{
 const card=CardSchema.parse({id:'card-speak',item_id:'water',item_kind:'word',direction:'speaking',prompt:'water',answer:'みず',due:null,revision:0,scheduled:false,state:{},scheduler:{},audio_cues:[{id:'reference',label:'Japanese'}],reference_text:'水をください。'})
 const html=renderToStaticMarkup(<ReviewMedia card={card} disabled={false} onReveal={()=>{}}/>)
 expect(html).toContain('Prepare Japanese')
 expect(html).toContain('Use text alternative')
 expect(html).not.toContain('Record microphone')
 expect(html).not.toContain('Try a spoken recall')
 expect(html).not.toContain('transcript feedback')
})

it('retains compatibility with legacy StudySchema and PersonalSchema evidence and reports typed responses on completion',()=>{
 const saved=StudySchema.parse({timer:null,id:'s',course_id:'ja',content_version:'0.1.16',source_kind:'speaking',source_id:'d',kind:'speaking',title:'Speaking',status:'completed',cursor:0,revision:1,next_action_id:'next',exercises:[],evidence:{speak:{responses:2,first_correct:null,first_assisted:false,last_correct:null,assisted:false,revealed:false,skipped:false,answer:null,speech_attempts:1,transcript_matches:0,typed_fallbacks:2,last_transcript:'水',last_transcript_matches:false}},preview_draft:true,mode:'supported',feedback:{exercise_id:'speak',kind:'recorded',message:'Saved typed practice',explanation:'Pronunciation unassessed',answer:null},xp_awarded:10,completed_at:'now',created_at:'now',initial_correct:0,assessed_count:0,concept_coverage:{}})
 expect(saved.evidence.speak.typed_fallbacks).toBe(2)
 expect(saved.evidence.speak.first_correct).toBeNull()
 expect(saved.feedback?.kind).toBe('recorded')

 const completionHtml=renderToStaticMarkup(<SessionCompletion session={saved} busy={false} heading={null} onReplay={()=>{}} onExit={()=>{}}/>)
 expect(completionHtml).toContain('2 typed practice responses. Pronunciation is not assessed.')
 expect(completionHtml).not.toContain('saved speech attempts')

 const personal=PersonalSchema.parse({
  skill_evidence:{
   speaking:{objective_checks:0,initial_correct:0,assisted:0,skipped:0,self_rated_reviews:1,typed_fallbacks:3},
   legacy_speaking:{objective_checks:0,initial_correct:0,assisted:0,skipped:0,self_rated_reviews:0,speech_attempts:2,transcript_matches:1,typed_fallbacks:1},
  },
  objective_checks:0,initial_correct:0,assisted_prompts:0,skipped_prompts:0,
  review_directions:{speaking:1},badges:[],weeks:[],best_week_xp:0,review_count:1,
  quests_completed:0,monthly_badges:[],level:1,provenance:'local',
 })
 expect(personal.skill_evidence.speaking.speech_attempts).toBe(0)
 expect(personal.skill_evidence.speaking.typed_fallbacks).toBe(3)
 expect(personal.skill_evidence.legacy_speaking.speech_attempts).toBe(2)
})
