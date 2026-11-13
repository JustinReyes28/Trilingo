import { renderToStaticMarkup } from 'react-dom/server'
import { expect, it } from 'vitest'
import { AudioControls, AudioPage, audioBadgeLabel } from './AudioPage'
import { ListeningCues, playbackRate, type PreparedAudio } from './ListeningExercise'
import { AudioSchema, AudioStatusSchema } from './practiceSchemas'
import { StudySchema } from './studySchemas'
import type { Library } from './schemas'

const sampleLibrary: Library = {
 concepts: [],
 writing_tasks: [],
 licenses: [],
 vocabulary: [
  {
   id:'ja-word-hello',
   surface:'こんにちは',
   reading:'こんにちは',
   gloss:'hello',
   part_of_speech:'expression',
   entry_kind:'word',
   register:'polite',
   example:[],
   concepts:[],
   stage:'stage-a',
   status:'published',
   audio:null,
  },
 ],
}

it('accepts bundled MP3 pack responses and rejects runtime WAV payloads', () => {
 const bundled = AudioSchema.parse({audio_base64:'AAAA',mime:'audio/mpeg',cached:true,source:'pack',label:'Bundled'})
 expect(bundled.source).toBe('pack')
 expect(bundled.mime).toBe('audio/mpeg')
 expect(AudioSchema.safeParse({audio_base64:'AAAA',mime:'audio/wav',cached:false,label:'Runtime'}).success).toBe(false)
 expect(AudioSchema.safeParse({audio_base64:'AAAA',mime:'audio/mpeg',cached:false,source:'runtime',label:'Runtime'}).success).toBe(false)
 expect(AudioSchema.safeParse({audio_base64:'AAAA',mime:'audio/ogg',cached:false,source:'pack',label:'No'}).success).toBe(false)
})

it('uses client-side 0.75x slow playback for bundled clips', () => {
 expect(playbackRate(false)).toBe(1)
 expect(playbackRate(true)).toBe(0.75)
})

it('reads bundled pack availability and review status without AI or STT provider fields', () => {
 const status = AudioStatusSchema.parse({
  audio_pack:{bundled_reference:true,bundled_reviewed:false,course_version:'0.1.21',message:'bundled'},
 })
 expect(status.audio_pack.bundled_reference).toBe(true)
 expect(status.audio_pack.bundled_reviewed).toBe(false)
 expect(status.audio_pack.course_version).toBe('0.1.21')
 const reviewed = AudioStatusSchema.parse({
  audio_pack:{bundled_reference:true,bundled_reviewed:true,course_version:'0.1.21',message:'bundled reviewed'},
 })
 expect(reviewed.audio_pack.bundled_reviewed).toBe(true)
 const strippedLegacy = AudioStatusSchema.parse({
  ai:{enabled:false,provider:'disabled',verified:false,message:'off'},
  stt:{enabled:false,provider:'disabled',verified:false,message:'off'},
  audio_pack:{bundled_reference:true,bundled_reviewed:false,course_version:'0.1.21',message:'bundled'},
 })
 expect('ai' in strippedLegacy).toBe(false)
 expect('stt' in strippedLegacy).toBe(false)
 expect(AudioStatusSchema.safeParse({
  tts:{enabled:false,provider:'kokoro',verified:false,message:'off'},
 }).success).toBe(false)
})

it('renders bundled review status badges and summary text on AudioPage without AI, STT, or Recorder UI', () => {
 const unbundled = AudioStatusSchema.parse({
  audio_pack:{bundled_reference:false,bundled_reviewed:true,course_version:null,message:'none'},
 })
 const pending = AudioStatusSchema.parse({
  audio_pack:{bundled_reference:true,bundled_reviewed:false,course_version:'0.1.21',message:'bundled'},
 })
 const reviewed = AudioStatusSchema.parse({
  audio_pack:{bundled_reference:true,bundled_reviewed:true,course_version:'0.1.21',message:'bundled'},
 })
 expect(audioBadgeLabel(null)).toBe('Bundled audio · unverified')
 expect(audioBadgeLabel(unbundled)).toBe('Bundled audio · unavailable')
 expect(audioBadgeLabel(pending)).toBe('Bundled audio · human review pending')
 expect(audioBadgeLabel(reviewed)).toBe('Bundled audio · reviewed')

 const unbundledHtml = renderToStaticMarkup(<AudioPage courseId="ja-starter" library={sampleLibrary} onOpen={()=>{}} initialStatus={unbundled}/>)
 expect(unbundledHtml).toContain('Bundled audio · unavailable')
 expect(unbundledHtml).toContain('no bundled pack found')
 expect(unbundledHtml).not.toContain('Runtime TTS')
 expect(unbundledHtml).not.toContain('kokoro')
 expect(unbundledHtml).not.toContain('STT:')
 expect(unbundledHtml).not.toContain('AI:')
 expect(unbundledHtml).not.toContain('Record microphone')
 expect(unbundledHtml).not.toContain('Your recording')

 const pendingHtml = renderToStaticMarkup(<AudioPage courseId="ja-starter" library={sampleLibrary} onOpen={()=>{}} initialStatus={pending}/>)
 expect(pendingHtml).toContain('Bundled audio · human review pending')
 expect(pendingHtml).toContain('bundled files available')
 expect(pendingHtml).toContain('0.1.21')
 expect(pendingHtml).not.toContain('Bundled audio · reviewed')
 expect(pendingHtml).not.toContain('Runtime TTS')
 expect(pendingHtml).not.toContain('kokoro')
 expect(pendingHtml).not.toContain('STT:')
 expect(pendingHtml).not.toContain('AI:')
 expect(pendingHtml).not.toContain('Record microphone')

 const reviewedHtml = renderToStaticMarkup(<AudioPage courseId="ja-starter" library={sampleLibrary} onOpen={()=>{}} initialStatus={reviewed}/>)
 expect(reviewedHtml).toContain('Bundled audio · reviewed')
 expect(reviewedHtml).toContain('bundled files available')
 expect(reviewedHtml).toContain('0.1.21')
 expect(reviewedHtml).not.toContain('Bundled audio · human review pending')
 expect(reviewedHtml).not.toContain('Runtime TTS')
 expect(reviewedHtml).not.toContain('STT:')
 expect(reviewedHtml).not.toContain('AI:')
 expect(reviewedHtml).not.toContain('Record microphone')
})

it('renders pack-only AudioControls with slow toggle for Japanese and English references', () => {
 const jaHtml = renderToStaticMarkup(<AudioControls reference={{course_id:'ja-starter',item_id:'ja-word-hello',language:'ja',preview_draft:false}}/>)
 expect(jaHtml).toContain('Prepare reference audio')
 expect(jaHtml).toContain('Slow reference')
 expect(jaHtml).not.toContain('Prepare generated reply audio')
 expect(jaHtml).not.toContain('Synthetic')

 const enHtml = renderToStaticMarkup(<AudioControls reference={{course_id:'ja-starter',item_id:'ja-word-hello',language:'en',preview_draft:false}}/>)
 expect(enHtml).toContain('Prepare English meaning audio')
 expect(enHtml).toContain('Slow reference')
})

it('parses AudioSchema extended with StudySchema and supports optional prepared labels', () => {
 const StudyAudioSchema = AudioSchema.extend({session: StudySchema})
 const parsed = StudyAudioSchema.parse({
  audio_base64:'AAAA',
  mime:'audio/mpeg',
  cached:true,
  source:'pack',
  label:'Bundled synthetic Japanese reference · reviewed',
  session:{
   timer:null,id:'session',course_id:'ja-starter',content_version:'0.1.16',
   source_kind:'listening',source_id:'ep-1',kind:'listening',title:'Episode 1',
   status:'active',cursor:0,revision:1,next_action_id:'next',exercises:[],
   evidence:{},preview_draft:true,mode:'supported',feedback:null,xp_awarded:0,
   completed_at:null,created_at:'2026-11-13',initial_correct:0,assessed_count:0,
   concept_coverage:{},recommendation:null,story:null,
  },
 })
 expect(parsed.source).toBe('pack')
 expect(parsed.label).toBe('Bundled synthetic Japanese reference · reviewed')
 expect(parsed.session.revision).toBe(1)
 const prepared: PreparedAudio = {url:'blob:test',label:parsed.label}
 expect(prepared.label).toBe('Bundled synthetic Japanese reference · reviewed')
 const cuesHtml = renderToStaticMarkup(<ListeningCues cues={[{id:'reference',label:'Clip A'}]} disabled={false}/>)
 expect(cuesHtml).toContain('Bundled reference audio · human Japanese listening review pending.')
 expect(cuesHtml).toContain('Preparing audio records delivery, not proof of hearing it. Text-assisted checks are recorded separately.')
 expect(cuesHtml).not.toContain('Bundled or synthetic')
})

it('offers a Japanese or English reference for vocabulary without offering it for stories', () => {
 const html = renderToStaticMarkup(<AudioPage courseId="ja-starter" library={sampleLibrary} onOpen={()=>{}}/>)
 expect(html).toContain('checking bundled pack')
 expect(html).toContain('Reference language')
 expect(html).toContain('English meaning')
 expect(html).toContain('こんにちは · hello')
 expect(html).not.toContain('autoplay')
})
