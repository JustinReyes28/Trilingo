import { pendingRequestStore, type PendingRequest } from './pendingRequests'
import { DraftSchema, SubmissionSchema } from './writingSchemas'
export const writingRequests=pendingRequestStore('trilingo.pending-writing',/^\/(courses\/[^/]+\/writing\/drafts|writing\/drafts\/[^/]+\/(revisions|submissions))$/)
export type WritingRequest=PendingRequest
export const commitDraft=(operation:WritingRequest)=>writingRequests.commit(operation,DraftSchema)
export const commitSubmission=(operation:WritingRequest)=>writingRequests.commit(operation,SubmissionSchema)

export const drawingReceipts=pendingRequestStore('trilingo.drawing-receipts',/^\/writing\/receipts\/[^/]+$/)
export function pendingDrawingReceipt(characterId:string):string|null{
 const saved=drawingReceipts.list().find(item=>item.body.character_id===characterId&&typeof item.body.request_id==='string')
 return saved?String(saved.body.request_id):null
}
