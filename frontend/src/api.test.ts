import { afterEach, describe, expect, it, vi } from 'vitest'
import { z } from 'zod'
import { request } from './api'
import { ExerciseSchema, HealthSchema, MapSchema, SettingsSchema } from './schemas'

afterEach(()=>vi.unstubAllGlobals())
describe('local API boundary',()=>{
 it('validates successful data',async()=>{vi.stubGlobal('fetch',vi.fn().mockResolvedValue(new Response(JSON.stringify({value:3}))));expect(await request('/test',z.object({value:z.number()}))).toEqual({value:3})})
 it('rejects unexpected successful data',async()=>{vi.stubGlobal('fetch',vi.fn().mockResolvedValue(new Response(JSON.stringify({value:'wrong'}))));await expect(request('/test',z.object({value:z.number()}))).rejects.toThrow('unexpected data')})
 it('shows actionable connection recovery',async()=>{vi.stubGlobal('fetch',vi.fn().mockRejectedValue(new TypeError('network')));await expect(request('/test',z.object({}))).rejects.toThrow('Start the backend')})
 it('rejects unreadable JSON instead of mislabeling it as connection failure',async()=>{vi.stubGlobal('fetch',vi.fn().mockResolvedValue(new Response('invalid-json')));await expect(request('/test',z.object({}))).rejects.toMatchObject({code:'invalid_response'})})
 it('preserves structured server errors',async()=>{vi.stubGlobal('fetch',vi.fn().mockResolvedValue(new Response(JSON.stringify({error:{code:'conflict',message:'Reload the saved revision and retry.'}}),{status:409})));await expect(request('/test',z.object({}))).rejects.toMatchObject({code:'conflict',message:'Reload the saved revision and retry.'})})
 it('handles malformed error responses',async()=>{vi.stubGlobal('fetch',vi.fn().mockResolvedValue(new Response('{}',{status:503})));await expect(request('/test',z.object({}))).rejects.toThrow('local service')})
})
describe('external content contracts',()=>{
 it('rejects unsupported exercise dispatch',()=>{expect(ExerciseSchema.safeParse({type:'made_up'}).success).toBe(false)})
 it('does not accept malformed map data',()=>{expect(MapSchema.safeParse({units:[]}).success).toBe(false)})
 it('requires complete durable settings and matches pack-only health/settings contracts',()=>{
  expect(SettingsSchema.safeParse({daily_goal:20}).success).toBe(false)
  const parsed=SettingsSchema.parse({
   daily_goal:20,show_goal:true,furigana:'always',romaji:true,reduced_motion:false,sound:false,
   show_statistics:true,practice_batch:10,
  })
  expect('tts' in parsed).toBe(false)
  expect('ai' in parsed).toBe(false)
  expect('stt' in parsed).toBe(false)
  const legacyProvider={enabled:false,provider:'disabled',base_url:'http://127.0.0.1:1234',model:'',timeout:20}
  const strippedSettings=SettingsSchema.parse({
   daily_goal:20,show_goal:true,furigana:'always',romaji:true,reduced_motion:false,sound:false,
   show_statistics:true,practice_batch:10,ai:legacyProvider,stt:legacyProvider,
  })
  expect('ai' in strippedSettings).toBe(false)
  expect('stt' in strippedSettings).toBe(false)
  const health=HealthSchema.parse({
   status:'ok',database:'ready',schema_version:'0014',qa_mode:false,
   features:{lessons:true},
  })
  expect(health.features).toEqual({lessons:true})
  expect('ai' in health.features).toBe(false)
  expect('stt' in health.features).toBe(false)
  const strippedHealth=HealthSchema.parse({
   status:'ok',database:'ready',schema_version:'0014',
   features:{lessons:true,ai:false,stt:false},
  })
  expect(strippedHealth.features).toEqual({lessons:true})
  expect('ai' in strippedHealth.features).toBe(false)
  expect('stt' in strippedHealth.features).toBe(false)
 })
})


it('invalid API configuration stays recoverable instead of crashing module startup',async()=>{
 vi.stubEnv('VITE_API_BASE_URL','not-a-url')
 vi.resetModules()
 try {
  const api=await import('./api')
  await expect(api.request('/health',z.object({}))).rejects.toMatchObject({code:'configuration'})
 } finally {
  vi.unstubAllEnvs()
  vi.resetModules()
 }
})
