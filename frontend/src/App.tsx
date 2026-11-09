import { useEffect, useState } from 'react'
import { ArrowRight, BookOpen, ChevronRight, Compass, Flower2, LibraryBig, Map, Settings2, Sprout, UserRound } from 'lucide-react'
import { request } from './api'
import { Badge, Button, Card, Dialog, FeedbackPanel, PageContainer } from './components'
import { CoursesSchema, HealthSchema, LibrarySchema, MapSchema, ProfileSchema, SettingsSchema, type CourseMap, type Library, type Profile, type Settings, type Unit } from './schemas'
import { LessonDetails } from './LessonDetails'
import { ProfilePage } from './ProfilePage'
import { PreviewPage } from './PreviewPage'
import { LessonNode } from './LessonNode'
import { ExerciseSession } from './ExerciseSession'
import { PracticeChoices } from './PracticeChoices'
import { AudioPage } from './AudioPage'
import { GrammarPage } from './GrammarPage'
import { ReviewPage } from './ReviewPage'
import { StudyHub } from './StudyHub'
import { ReadingPage } from './ReadingPage'
import { WritingPage } from './WritingPage'
import { ReadingLibrarySchema } from './readingSchemas'
import { JapaneseText } from './JapaneseText'
import { ProgressSchema, type Progress } from './studySchemas'

type Page = 'learn'|'practice'|'library'|'profile'|'preview'|'session'|'reading'|'writing'|'grammar'|'review'|'audio'
const destinations = [{id:'learn',label:'Learn',icon:Map},{id:'practice',label:'Practice',icon:Compass},{id:'library',label:'Library',icon:LibraryBig},{id:'profile',label:'Profile',icon:UserRound}] as const
function currentPage(hash=location.hash):Page {const value=hash.slice(1).split('?')[0];if(value.startsWith('grammar?'))return 'grammar';if(value.startsWith('session/'))return 'session';if(value.startsWith('writing/'))return 'writing';return ['learn','practice','library','profile','preview','reading','writing','grammar','review','audio'].includes(value)?value as Page:'learn'}
type Data={profile:Profile;settings:Settings;map:CourseMap|null;library:Library|null;progress:Progress}

export default function App(){
 const [route,setRoute]=useState(location.hash)
 const page=currentPage(route)
 const [data,setData]=useState<Data|null>(null)
 const [error,setError]=useState('')
 const [revision,setRevision]=useState(0)
 const [guide,setGuide]=useState<Unit|null>(null)
 const [lesson,setLesson]=useState<string|null>(null)
 useEffect(()=>{const update=()=>{setRoute(location.hash);setLesson(null)};window.addEventListener('hashchange',update);return()=>window.removeEventListener('hashchange',update)},[])
 useEffect(()=>{let active=true;async function load(){try{
  await request('/health',HealthSchema)
  const timezone=Intl.DateTimeFormat().resolvedOptions().timeZone
  const profile=await request('/profile?timezone='+encodeURIComponent(timezone),ProfileSchema)
  const [settings,courses,progress]=await Promise.all([request('/settings',SettingsSchema),request('/courses',CoursesSchema),request('/progress',ProgressSchema)])
  const [map,library]=courses.length?await Promise.all([request('/courses/'+courses[0].id+'/map',MapSchema),request('/courses/'+courses[0].id+'/library',LibrarySchema)]):[null,null]
  if(active){setData({profile,settings,map,library,progress});setError('')}
 }catch(err){if(active)setError(err instanceof Error?err.message:'The local service could not open. Retry.')}}void load();return()=>{active=false}},[revision])
 useEffect(()=>{document.documentElement.dataset.motion=data?.settings.reduced_motion?'reduced':'system';document.documentElement.dataset.accent=data?.settings.accent??'path'},[data?.settings.reduced_motion,data?.settings.accent])
 function navigate(next:Page){location.hash=next}
 function openSession(id:string){setLesson(null);location.hash='session/'+id}
 function refreshProgress(){setRevision(value=>value+1)}
 async function saveProfile(profile:Profile,settings:Settings){setData(old=>old?{...old,profile,settings}:old);refreshProgress()}
 return <div className="app-shell">
  <a className="skip-link" href="#main" onClick={event=>{event.preventDefault();document.getElementById('main')?.focus();document.getElementById('main')?.scrollIntoView()}}>Skip to content</a>
  <aside className="navigation"><a className="wordmark" href="#learn"><Flower2 size={32} strokeWidth={2.5} aria-hidden="true"/><span>trilingo<span className="wordmark-dot">.</span></span></a><p className="nav-caption">A little Japanese, your way.</p>
   <nav aria-label="Main navigation">{destinations.map(({id,label,icon:Icon})=><a key={id} href={'#'+id} aria-current={page===id?'page':undefined}><Icon size={23} aria-hidden="true"/><span>{label}</span>{page===id&&<ChevronRight size={18} className="nav-chevron" aria-hidden="true"/>}</a>)}</nav>
   <div className="nav-footer"><span className={'connection-dot '+(data?'connected':'')} aria-hidden="true"/><span>{data?'Local service connected':'Connecting locally'}</span><small>Personal Japanese workspace</small></div>
  </aside>
  <div className="workspace"><header className="topbar"><div className="course-label"><span lang="ja">日本語</span><span>Japanese <small>English explanations</small></span></div><a href="#profile" className="profile-link" aria-label="Open profile settings"><UserRound size={20} aria-hidden="true"/><span>{data?.profile.name??'Profile'}</span></a></header>
   <PageContainer id="main" tabIndex={-1}>
    {error?<Card><FeedbackPanel kind="error">{error}</FeedbackPanel><Button onClick={()=>{setError('');setRevision(r=>r+1)}}>Retry connection</Button></Card>:!data?<div role="status" aria-label="Loading your workspace" className="skeleton"><div/><div/><div/><p>Opening your local workspace…</p></div>:<>
    {page==='learn'&&<><div className="page-heading"><div><h1>Start with a small hello<span className="punctuation">。</span></h1><p>Follow the trail, or choose what catches your curiosity.</p></div><Badge tone="mint">Beginner · Starter slice</Badge></div>
     {!data.map?<Card><h2>No course imported yet</h2><p>Import the starter collection using the README, then refresh this page.</p><Button onClick={()=>setRevision(r=>r+1)}>Refresh courses</Button></Card>:<div className="learn-layout"><div className="path-column"><div className="study-note"><Sprout size={20} aria-hidden="true"/><p>There’s no wrong place to begin. Every published lesson is yours to explore.</p></div>{data.map.units.filter(u=>u.status==='published').map((unit,index)=><section className="unit" key={unit.id} aria-labelledby={unit.id}><div className="unit-header"><div><span className="unit-number">Unit {unit.order} · Stage {unit.stage.slice(-1).toUpperCase()}</span><h2 id={unit.id}>{unit.title}</h2><p>{unit.description}</p></div><Button variant="secondary" onClick={()=>setGuide(unit)} aria-label={'Open guide for '+unit.title}><BookOpen size={18} aria-hidden="true"/>Guide</Button></div><ol className="lesson-path">{unit.lessons.map((item,j)=><li key={item.id} className={'path-stop stop-'+j}><LessonNode title={item.title} japanese={item.japanese_title} number={j+1} state={lesson===item.id?'current':item.study_state!=='not_started'?item.study_state:index===0&&j===0?'suggested':'available'} onClick={()=>setLesson(item.id)}/><div className="node-copy"><strong>{item.title}</strong><span>{index===0&&j===0?'Suggested first step':'Available to explore'}</span><small>{item.exercise_count} short exercises · {item.study_state.replaceAll('_',' ')}</small></div></li>)}</ol></section>)}<section className="course-next"><div><span className="eyebrow">A little further along</span><h2>More everyday Japanese</h2><p>{data.map.units.filter(u=>u.status!=='published').length} unit outlines are being written. They’ll appear here when published.</p></div><Button variant="quiet" onClick={()=>navigate('library')}>See the syllabus <ArrowRight size={18}/></Button></section></div>
     <aside className="course-sidebar" aria-label="Course notes"><Card className="welcome-note">{data.settings.show_statistics&&<p className="progress-summary">{data.progress.total_xp} XP saved · {data.progress.current_streak} active-day streak</p>}{data.settings.show_goal&&data.settings.daily_goal!==null&&<p className="small">Today: {data.progress.today_xp} / {data.settings.daily_goal} XP suggested goal{data.progress.goal_met?' · Met':''}. You can keep studying freely.</p>}<span className="japanese-sample" lang="ja">一歩ずつ。</span><h2>One step at a time.</h2><p>A greeting today. A sentence next. Keep your own pace.</p><span className="note-line"/><p className="small">Reading, writing and speaking will grow together.</p></Card><Card><div className="section-label"><BookOpen size={18}/><h2>Inside this starter</h2></div><dl className="inventory"><div><dt>Published lessons</dt><dd>{data.map.inventory.published_lessons}</dd></div><div><dt>Core word entries</dt><dd>{data.map.inventory.published_words}</dd></div><div><dt>Useful expressions</dt><dd>{data.map.inventory.published_phrases}</dd></div></dl><p className="small">Practice content with internal review; independent Japanese-language review is pending. This is a partial collection. The full beginner target is {data.map.inventory.target_words.toLocaleString()} words and {data.map.inventory.target_kanji} kanji.</p><Button variant="quiet" onClick={()=>navigate('library')}>Explore the library <ChevronRight size={16}/></Button></Card><p className="sidebar-footnote"><Settings2 size={16} aria-hidden="true"/>Reading aids and your optional goal live in Profile.</p></aside></div>}
     <p className="phase-note">Your sessions, assistance and activity are saved locally. Every published lesson remains directly available.</p></>}
    {page==='practice'&&<><div className="page-heading"><div><h1>Your practice space</h1><p>Choose a mode, resume a saved session or revisit a mistake.</p></div></div>{data.map&&<><PracticeChoices courseId={data.map.id}/><StudyHub key={route} courseId={data.map.id} progress={data.progress} batch={data.settings.practice_batch} onOpen={openSession}/></>}</>}
    {page==='grammar'&&data.map&&<GrammarPage courseId={data.map.id} onOpen={openSession} settings={data.settings} onChanged={refreshProgress}/>}
    {page==='review'&&data.map&&data.library&&<ReviewPage key={route} courseId={data.map.id} library={data.library} settings={data.settings} onChanged={refreshProgress}/>}
    {page==='audio'&&data.map&&data.library&&<AudioPage courseId={data.map.id} library={data.library} onOpen={openSession}/>}
    {page==='writing'&&data.map&&<WritingPage key={route} courseId={data.map.id} destination={route.startsWith('#writing/')?route.slice('#writing/'.length):''} onOpen={openSession} onChanged={refreshProgress}/>}
    {page==='reading'&&data.map&&<ReadingPage key={route} courseId={data.map.id} settings={data.settings} onOpen={openSession}/>}
    {page==='library'&&<LibraryPage data={data} onGuide={setGuide} onLesson={setLesson}/>}
    {page==='profile'&&<ProfilePage profile={data.profile} settings={data.settings} onSaved={saveProfile}/>}
    {page==='preview'&&<PreviewPage/>}
    {page==='session'&&<ExerciseSession key={route} sessionId={route.slice('#session/'.length)} onExit={()=>{navigate('learn');refreshProgress()}} onChanged={refreshProgress} onOpen={openSession}/>}
    </>}
   </PageContainer><footer className="workspace-footer"><span>Made for your own pace.</span><a href="#preview">Development previews</a></footer>
  </div>
  {guide&&<Dialog title={guide.title+' · Unit guide'} onClose={()=>setGuide(null)}><p className="dialog-japanese" lang="ja">{guide.japanese_title}</p>{guide.guide.split('\n\n').map((text,i)=><p key={i}>{text}</p>)}<p className="small">Suggested preparation is advice. You can browse every published lesson.</p><Button onClick={()=>setGuide(null)}>Back to the path</Button></Dialog>}
  {lesson&&data?.map&&<LessonDetails courseId={data.map.id} lessonId={lesson} onClose={()=>setLesson(null)} onStart={openSession}/>}
 </div>
}

function LibraryPage({data,onGuide,onLesson}:{data:Data;onGuide:(unit:Unit)=>void;onLesson:(id:string)=>void}){
 const [search,setSearch]=useState('')
 const [familiar,setFamiliar]=useState(new Set<string>())
 const [aidError,setAidError]=useState('')
 const courseId=data.map?.id
 useEffect(()=>{let active=true;if(courseId)void request('/courses/'+courseId+'/reading',ReadingLibrarySchema).then(value=>{if(active)setFamiliar(new Set(value.items.filter(item=>item.item_kind==='word'&&item.familiar).map(item=>item.item_id)))}).catch(()=>{if(active)setAidError('Familiarity preferences could not load. Readings are shown for unknown words; retry by reopening Library.')});return()=>{active=false}},[courseId])
 const words=data.library?.vocabulary.filter(v=>(v.surface+' '+v.reading+' '+v.gloss).toLowerCase().includes(search.toLowerCase()))??[]
 return <><div className="page-heading"><div><h1>Your Japanese library</h1><p>Original course words, guides and the road ahead.</p></div><Badge tone="mint">{data.library?.vocabulary.length??0} published entries</Badge></div>
 {!data.library||!data.map?<Card><h2>Your library is empty</h2><p>Import a course to see its published vocabulary and guides.</p></Card>:<><section className="library-words"><h2>A first handful of words & phrases</h2><label className="search-label">Find a word<input type="search" value={search} onChange={event=>setSearch(event.target.value)} placeholder="Japanese, reading or English"/></label>{aidError&&<p role="status" className="small">{aidError}</p>}<div className="word-list">{words.length?words.map(word=><article className="word-entry" key={word.id}><div><span className="word-surface"><JapaneseText segments={[{surface:word.surface,reading:word.reading,vocabulary_id:word.id}]} furigana={data.settings.furigana} familiarIds={familiar}/></span></div><div><strong>{word.gloss}</strong><small>{word.part_of_speech} · {word.register}</small></div></article>):<p role="status">No matching words. Try another spelling or English meaning.</p>}</div></section><section className="syllabus"><h2>The beginner syllabus</h2><p>Ten topic outlines span first sounds to everyday messages. Only the first two units contain the starter slice.</p>{data.map.units.map(unit=><details key={unit.id}><summary><span>{unit.order}. {unit.title}</span><Badge tone={unit.status==='published'?'mint':'muted'}>{unit.status==='published'?'Published slice':'Not published'}</Badge></summary><p>{unit.description}</p>{unit.status==='published'?<div className="inline-actions"><Button variant="secondary" onClick={()=>onGuide(unit)}>Read unit guide</Button>{unit.lessons.map(lesson=><Button variant="quiet" key={lesson.id} onClick={()=>onLesson(lesson.id)}>{lesson.title}</Button>)}</div>:<p className="small">Content is being authored. No lesson completion will be required to access it once published.</p>}</details>)}</section><Card><h2>From first sentences to complex essays</h2><ol className="stages">{data.map.stages.map(stage=><li key={stage.id}><strong>{stage.id.slice(-1).toUpperCase()} · {stage.title}</strong><span>{stage.release} release · Planned</span></li>)}</ol><p>Beginner writing aids include {data.library.writing_tasks.length} draft task outlines. They remain unpublished pending Japanese review. Open Writing from Practice to try the draft tools.</p></Card><p className="small">{data.map.review_note}</p>{data.library.licenses.map(license=><p key={license.id} className="small">{license.attribution} · {license.license}. {license.source}</p>)}</>}
 </>
}
