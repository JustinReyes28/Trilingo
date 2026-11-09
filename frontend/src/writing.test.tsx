import { afterEach, expect, it, vi } from 'vitest'
import { normalizedPoint, simplifyStrokes } from './DrawingPad'
import { commitDraft, commitSubmission, pendingDrawingReceipt, writingRequests } from './writingApi'
import { DraftSchema, HandwritingResultSchema } from './writingSchemas'
const revision={id:'rev',number:0,text:'',checklist:[],model_revealed:false,created_at:'now'}
const draft={id:'draft',course_id:'course',content_version:'1.0.0',task:{id:'task',stage:'stage-a',genre:'fixture',prompt:'fixture',model:'あ',alternatives:[],checklist:[],status:'draft',rubric_version:'test',exercise_ids:[]},current:revision,created_at:'now',updated_at:'now',assessment:'not_assessed'}
function storage(){const data=new Map<string,string>();vi.stubGlobal('localStorage',{getItem:(key:string)=>data.get(key)??null,setItem:(key:string,value:string)=>data.set(key,value),removeItem:(key:string)=>data.delete(key)})}
afterEach(()=>vi.unstubAllGlobals())
it('normalizes pointer coordinates independently of grid size and clamps edge motion',()=>{expect(normalizedPoint(60,120,{left:10,top:20,width:100,height:200},5)).toEqual({x:.5,y:.5,t:5});expect(normalizedPoint(110,220,{left:10,top:20,width:200,height:400},5)).toEqual({x:.5,y:.5,t:5});expect(normalizedPoint(-20,500,{left:10,top:20,width:100,height:100},8)).toEqual({x:0,y:1,t:8})})
it('bounds optional sample points while preserving endpoints and chronology',()=>{const original=Array.from({length:20},(_,stroke)=>Array.from({length:200},(_,index)=>({x:index/200,y:.5,t:stroke*200+index})));const reduced=simplifyStrokes(original);expect(reduced.flat().length).toBeLessThanOrEqual(1200);expect(reduced[0][0]).toEqual(original[0][0]);expect(reduced[19].at(-1)).toEqual(original[19].at(-1));expect(reduced.flat().map(point=>point.t)).toEqual([...reduced.flat().map(point=>point.t)].sort((a,b)=>a-b))})
it('retains exact draft text/revision across lost acknowledgement and clears after retry',async()=>{storage();vi.stubGlobal('fetch',vi.fn().mockRejectedValueOnce(new TypeError('lost')).mockResolvedValueOnce(new Response(JSON.stringify(draft))));const operation={path:'/writing/drafts/draft/revisions',body:{request_id:'same',expected_revision_id:'old',text:'日本語の文章。',checklist:[],model_revealed:false}};await expect(commitDraft(operation)).rejects.toThrow();expect(writingRequests.pending(operation.path)).toEqual(operation);expect(await commitDraft(operation)).toEqual(DraftSchema.parse(draft));expect(writingRequests.list()).toEqual([])})
it('keeps submission identity for retry and rejects invented handwriting correctness',async()=>{storage();vi.stubGlobal('fetch',vi.fn().mockRejectedValue(new TypeError('lost')));const operation={path:'/writing/drafts/draft/submissions',body:{request_id:'submission',revision_id:'saved',self_reviewed:false}};await expect(commitSubmission(operation)).rejects.toThrow();expect(writingRequests.pending()?.body.request_id).toBe('submission');expect(HandwritingResultSchema.safeParse({objective_correctness:true,evidence:'mastered'}).success).toBe(false)})

it('keeps independent receipt references without storing raw drawing points',async()=>{storage();const {drawingReceipts}=await import('./writingApi');drawingReceipts.remember({path:'/writing/receipts/first',body:{request_id:'first',character_id:'character'}});drawingReceipts.remember({path:'/writing/receipts/second',body:{request_id:'second',character_id:'character'}});drawingReceipts.clear('first');expect(drawingReceipts.list()).toEqual([{path:'/writing/receipts/second',body:{request_id:'second',character_id:'character'}}]);expect(JSON.stringify(drawingReceipts.list())).not.toContain('strokes')})

it('recovers only the selected character receipt and preserves other drawing confirmations',async()=>{
 storage()
 const {drawingReceipts}=await import('./writingApi')
 drawingReceipts.remember({path:'/writing/receipts/other',body:{request_id:'other',character_id:'other-character'}})
 drawingReceipts.remember({path:'/writing/receipts/selected',body:{request_id:'selected',character_id:'selected-character'}})
 expect(pendingDrawingReceipt('selected-character')).toBe('selected')
 expect(pendingDrawingReceipt('missing-character')).toBeNull()
 drawingReceipts.clear('selected')
 expect(pendingDrawingReceipt('selected-character')).toBeNull()
 expect(pendingDrawingReceipt('other-character')).toBe('other')
 expect(drawingReceipts.list()).toHaveLength(1)
})
