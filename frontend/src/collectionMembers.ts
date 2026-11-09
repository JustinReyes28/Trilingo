import { z } from 'zod'

export const CollectionMembersSchema=z.object({items:z.array(z.object({id:z.string(),surface:z.string(),reading:z.string(),gloss:z.string()})),has_more:z.boolean(),offset:z.number()})
type MemberPage=z.infer<typeof CollectionMembersSchema>
export type CollectionMembersState={
 collectionId:string
 requestId:number
 status:'idle'|'loading'|'ready'|'error'
 items:MemberPage['items']
 hasMore:boolean
 error:string
}
export const initialCollectionMembers:CollectionMembersState={collectionId:'',requestId:0,status:'idle',items:[],hasMore:false,error:''}
type Scope={collectionId:string;requestId:number}
export type CollectionMembersAction=
 | {type:'select';collectionId:string}
 | {type:'retry'}
 | ({type:'loaded'|'append';page:MemberPage}&Scope)
 | ({type:'failed';message:string}&Scope)

export function collectionMembersReducer(state:CollectionMembersState,action:CollectionMembersAction):CollectionMembersState {
 if(action.type==='select')return {collectionId:action.collectionId,requestId:state.requestId+1,status:action.collectionId?'loading':'idle',items:[],hasMore:false,error:''}
 if(action.type==='retry')return state.collectionId?{...state,requestId:state.requestId+1,status:'loading',items:[],hasMore:false,error:''}:state
 if(action.collectionId!==state.collectionId||action.requestId!==state.requestId)return state
 if(action.type==='failed')return {...state,status:'error',items:[],hasMore:false,error:action.message}
 if(action.type==='append') {
  if(state.status!=='ready')return state
  return {...state,items:[...new Map([...state.items,...action.page.items].map(item=>[item.id,item])).values()],hasMore:action.page.has_more}
 }
 return {...state,status:'ready',items:action.page.items,hasMore:action.page.has_more,error:''}
}