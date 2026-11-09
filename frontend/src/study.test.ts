import { afterEach, expect, it, vi } from 'vitest'
import { commitStudy, pendingStudies } from './studyApi'
import { StudySchema } from './studySchemas'

const receipt={timer:null,id:'session',course_id:'course',content_version:'1.0.0',source_kind:'lesson',source_id:'lesson',kind:'lesson',title:'Test fixture',status:'active',cursor:0,revision:0,next_action_id:'next',exercises:[],evidence:{},preview_draft:false,mode:'supported',feedback:null,xp_awarded:0,completed_at:null,created_at:'2026-10-23',initial_correct:0,assessed_count:0,concept_coverage:{},recommendation:null,story:null}
function storage(){const values=new Map<string,string>();vi.stubGlobal('localStorage',{getItem:(key:string)=>values.get(key)??null,setItem:(key:string,value:string)=>values.set(key,value),removeItem:(key:string)=>values.delete(key)})}
afterEach(()=>vi.unstubAllGlobals())
it('rejects fabricated grade and missing session identity at the boundary',()=>{expect(StudySchema.safeParse({...receipt,id:undefined}).success).toBe(false);expect(StudySchema.safeParse({...receipt,feedback:{kind:'perfect'}}).success).toBe(false)})
it('retains the exact action when the response is lost and clears only after acknowledgement',async()=>{
 storage();const fetcher=vi.fn().mockRejectedValueOnce(new TypeError('lost response')).mockResolvedValueOnce(new Response(JSON.stringify(receipt)));vi.stubGlobal('fetch',fetcher)
 const operation={path:'/sessions/session/actions',body:{request_id:'original',expected_revision:0,action:'answer',answer:'あ'}}
 await expect(commitStudy(operation)).rejects.toMatchObject({code:'connection'})
 expect(pendingStudies()).toEqual([operation]);expect(await commitStudy(pendingStudies()[0])).toEqual(receipt)
 expect(fetcher.mock.calls[0][1].body).toBe(fetcher.mock.calls[1][1].body);expect(pendingStudies()).toEqual([])
})
it('keeps independent interrupted actions when another session saves successfully',async()=>{
 storage();vi.stubGlobal('fetch',vi.fn().mockRejectedValueOnce(new TypeError('offline')).mockResolvedValueOnce(new Response(JSON.stringify(receipt))))
 const first={path:'/sessions/first/actions',body:{request_id:'first',action:'skip'}}
 await expect(commitStudy(first)).rejects.toThrow();await commitStudy({path:'/sessions/second/actions',body:{request_id:'second',action:'skip'}})
 expect(pendingStudies()).toEqual([first])
})
it('preserves an unapplied answer on revision conflicts for explicit recovery',async()=>{
 storage();vi.stubGlobal('fetch',vi.fn().mockResolvedValue(new Response(JSON.stringify({error:{code:'stale_revision',message:'Reload saved work.'}}),{status:409})))
 const operation={path:'/sessions/session/actions',body:{request_id:'same',answer:'自分の答え'}}
 await expect(commitStudy(operation)).rejects.toMatchObject({code:'stale_revision'});expect(pendingStudies()[0].body.answer).toBe('自分の答え')
})
it('remains usable when browser storage is unavailable',async()=>{
 vi.stubGlobal('localStorage',{getItem:()=>{throw Error('unavailable')},setItem:()=>{throw Error('unavailable')}});vi.stubGlobal('fetch',vi.fn().mockResolvedValue(new Response(JSON.stringify(receipt))));expect(await commitStudy({path:'/sessions/session/actions',body:{request_id:'safe'}})).toEqual(receipt)
})
