import { expect, it } from 'vitest'
import { collectionMembersReducer, initialCollectionMembers, type CollectionMembersState } from './collectionMembers'

const page=(id:string)=>({items:[{id,surface:id,reading:'よみ',gloss:'a saved word'}],has_more:false,offset:0})
const scope=(state:CollectionMembersState)=>({collectionId:state.collectionId,requestId:state.requestId})

it('clears the previous collection immediately while a different collection is loading or fails',()=>{
 let state=collectionMembersReducer(initialCollectionMembers,{type:'select',collectionId:'first'})
 state=collectionMembersReducer(state,{type:'loaded',...scope(state),page:page('first-word')})
 expect(state.items.map(item=>item.id)).toEqual(['first-word'])
 const previous=scope(state)
 state=collectionMembersReducer(state,{type:'select',collectionId:'second'})
 const pending=scope(state)
 expect(state.status).toBe('loading')
 expect(state.items).toEqual([])
 expect(state.hasMore).toBe(false)
 state=collectionMembersReducer(state,{type:'loaded',...previous,page:page('stale-first-word')})
 expect(state.items).toEqual([])
 state=collectionMembersReducer(state,{type:'failed',...pending,message:'The local service is unavailable.'})
 expect(state.collectionId).toBe('second')
 expect(state.status).toBe('error')
 expect(state.items).toEqual([])
 expect(state.error).toBe('The local service is unavailable.')
 state=collectionMembersReducer(state,{type:'retry'})
 expect(state.requestId).toBe(pending.requestId+1)
 expect(state.status).toBe('loading')
 expect(state.error).toBe('')
 state=collectionMembersReducer(state,{type:'failed',...pending,message:'A stale error'})
 expect(state.status).toBe('loading')
 expect(state.error).toBe('')
 state=collectionMembersReducer(state,{type:'loaded',...scope(state),page:page('second-word')})
 expect(state.items.map(item=>item.id)).toEqual(['second-word'])
})

it('ignores out-of-order responses even after returning to the same collection',async()=>{
 let state=initialCollectionMembers
 const waiting:Array<()=>void>=[]
 function start(collectionId:string,wordId:string){
  state=collectionMembersReducer(state,{type:'select',collectionId})
  const requestScope=scope(state)
  const response=new Promise<ReturnType<typeof page>>(resolve=>waiting.push(()=>resolve(page(wordId))))
  return response.then(result=>{state=collectionMembersReducer(state,{type:'loaded',...requestScope,page:result})})
 }
 const first=start('first','outdated-first-word')
 const second=start('second','second-word')
 const latest=start('first','current-first-word')
 waiting[1]()
 await second
 expect(state.collectionId).toBe('first')
 expect(state.status).toBe('loading')
 expect(state.items).toEqual([])
 waiting[0]()
 await first
 expect(state.status).toBe('loading')
 expect(state.items).toEqual([])
 waiting[2]()
 await latest
 expect(state.status).toBe('ready')
 expect(state.items.map(item=>item.id)).toEqual(['current-first-word'])
})

it('keeps pagination bound to its selection and preserves reachable unique words',()=>{
 let state=collectionMembersReducer(initialCollectionMembers,{type:'select',collectionId:'first'})
 state=collectionMembersReducer(state,{type:'loaded',...scope(state),page:{...page('one'),has_more:true}})
 const first=scope(state)
 state=collectionMembersReducer(state,{type:'append',...first,page:{items:[...page('one').items,...page('two').items],has_more:false,offset:1}})
 expect(state.items.map(item=>item.id)).toEqual(['one','two'])
 expect(state.hasMore).toBe(false)
 state=collectionMembersReducer(state,{type:'select',collectionId:'second'})
 state=collectionMembersReducer(state,{type:'loaded',...scope(state),page:page('three')})
 state=collectionMembersReducer(state,{type:'append',...first,page:page('stale-extra')})
 expect(state.items.map(item=>item.id)).toEqual(['three'])
 state=collectionMembersReducer(state,{type:'select',collectionId:''})
 expect(state.status).toBe('idle')
 expect(state.items).toEqual([])
})