import { pendingRequestStore, type PendingRequest } from './pendingRequests'
import { StudySchema } from './studySchemas'
const store=pendingRequestStore('trilingo.pending-study',/^\/(courses\/[^/]+\/sessions|sessions\/[^/]+\/actions)$/)
export type PendingStudy=PendingRequest
export const pendingStudies=store.list
export const pendingStudy=store.pending
export const clearPendingStudy=store.clear
export const commitStudy=(operation:PendingStudy)=>store.commit(operation,StudySchema)
export function startStudy(courseId:string,sourceId:string,requestId:string,sourceKind='lesson',previewDraft=false,mode:'supported'|'unassisted'='supported'){
 return commitStudy({path:'/courses/'+courseId+'/sessions',body:{request_id:requestId,source_id:sourceId,source_kind:sourceKind,preview_draft:previewDraft,mode}})
}
