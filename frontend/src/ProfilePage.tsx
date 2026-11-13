import { useState, useEffect, useRef, type FormEvent, type ChangeEvent } from 'react'
import { patch, post, postBinary, request, getApiUrl } from './api'
import { Button, Card, Dialog, FeedbackPanel } from './components'
import {
  ProfileSchema,
  SettingsSchema,
  BackupPreviewSchema,
  RestoreResultSchema,
  ResetResultSchema,
  SafetyBackupListSchema,
  type Profile,
  type Settings,
  type BackupPreview,
  type SafetyBackupItem,
} from './schemas'
import { Download, Upload, RotateCcw, ShieldCheck, Database, FileArchive } from 'lucide-react'

export function ProfilePage({profile,settings,onSaved}:{profile:Profile;settings:Settings;onSaved:(profile:Profile,settings:Settings)=>void}){
 const [name,setName]=useState(profile.name)
 const [timezone,setTimezone]=useState(profile.timezone)
 const [draft,setDraft]=useState(settings)
 const [pending,setPending]=useState(false)
 const [message,setMessage]=useState('')
 const [error,setError]=useState('')
 const fileInputRef = useRef<HTMLInputElement>(null)

 // Backup and restore states
 const [includeSamples, setIncludeSamples] = useState(true)
 const [selectedFile, setSelectedFile] = useState<File | null>(null)
 const [preview, setPreview] = useState<BackupPreview | null>(null)
 const [previewLoading, setPreviewLoading] = useState(false)
 const [restoring, setRestoring] = useState(false)
 const [resetting, setResetting] = useState(false)
 const [showResetDialog, setShowResetDialog] = useState(false)
 const [safetyBackups, setSafetyBackups] = useState<SafetyBackupItem[]>([])

 const dirty=name!==profile.name||timezone!==profile.timezone||JSON.stringify(draft)!==JSON.stringify(settings)

 useEffect(() => {
  loadSafetyBackups()
 }, [])

 async function loadSafetyBackups() {
  try {
   const res = await request('/backup/safety-backups', SafetyBackupListSchema)
   setSafetyBackups(res.backups)
  } catch {
   // Safety backups list failure is non-fatal
  }
 }

 async function save(event:FormEvent){event.preventDefault();setPending(true);setError('');setMessage('');try{
  const savedProfile=await patch('/profile',ProfileSchema,{name,timezone})
  // Reflect the first acknowledged save even if settings need a retry.
  onSaved(savedProfile,settings)
  const savedSettings=await patch('/settings',SettingsSchema,draft)
  onSaved(savedProfile,savedSettings);setDraft(savedSettings);setMessage('Profile and preferences saved to this computer.')
 }catch(err){setError(err instanceof Error?err.message:'Could not save. Keep your input and retry.')}finally{setPending(false)}}

 const change=<K extends keyof Settings>(key:K,value:Settings[K])=>setDraft(previous=>({...previous,[key]:value}))

 function downloadBackup() {
  const url = getApiUrl(`/backup/export?include_samples=${includeSamples}`)
  window.open(url, '_blank')
  setMessage('Backup download initiated. The file contains a complete SQLite-consistent snapshot.')
 }

 async function onFileSelected(e: ChangeEvent<HTMLInputElement>) {
  const file = e.target.files?.[0]
  if (!file) return
  setSelectedFile(file)
  setPreviewLoading(true)
  setError('')
  setMessage('')
  try {
   const buffer = await file.arrayBuffer()
   const res = await postBinary('/backup/preview', BackupPreviewSchema, buffer)
   setPreview(res)
  } catch (err) {
   setError(err instanceof Error ? err.message : 'Could not read backup file.')
   setPreview(null)
  } finally {
   setPreviewLoading(false)
   if (fileInputRef.current) fileInputRef.current.value = ''
  }
 }

 async function confirmRestore() {
  if (!selectedFile) return
  setRestoring(true)
  setError('')
  setMessage('')
  try {
   const buffer = await selectedFile.arrayBuffer()
   const res = await postBinary('/backup/restore?confirm=true', RestoreResultSchema, buffer)
   setName(res.profile.name)
   setTimezone(res.profile.timezone)
   onSaved(res.profile, draft)
   setPreview(null)
   setSelectedFile(null)
   setMessage(`Backup restored successfully from snapshot (${new Date(res.created_at).toLocaleString()}). All local progress has been updated.`)
   await loadSafetyBackups()
  } catch (err) {
   setError(err instanceof Error ? err.message : 'Could not restore backup.')
  } finally {
   setRestoring(false)
  }
 }

 async function confirmReset() {
  setResetting(true)
  setError('')
  setMessage('')
  try {
   const res = await post('/backup/reset', ResetResultSchema, { confirm: true })
   setName(res.profile.name)
   setTimezone(res.profile.timezone)
   const defaultSettings = SettingsSchema.parse({})
   setDraft(defaultSettings)
   onSaved(res.profile, defaultSettings)
   setShowResetDialog(false)
   setMessage('All learning records, review cards, and XP have been reset. A safety backup was saved automatically before resetting.')
   await loadSafetyBackups()
  } catch (err) {
   setError(err instanceof Error ? err.message : 'Could not reset progress.')
  } finally {
   setResetting(false)
  }
 }

 return <><div className="page-heading"><div><h1>Your profile & preferences</h1><p>Choose the support you find useful. Goals never limit study.</p></div></div><form onSubmit={save} className="settings-form"><Card><h2>Your local profile</h2><label>Your name<input value={name} required maxLength={60} onChange={e=>setName(e.target.value)}/></label><label>Timezone<input list="timezones" value={timezone} required onChange={e=>setTimezone(e.target.value)}/><datalist id="timezones"><option value={Intl.DateTimeFormat().resolvedOptions().timeZone}/><option value="Asia/Singapore"/><option value="UTC"/><option value="Asia/Tokyo"/></datalist><span className="field-help">Detected from this browser on first setup. You can use any IANA timezone.</span></label></Card>
 <Card><h2>Reading & comfort</h2><label>Furigana support<select value={draft.furigana} onChange={e=>change('furigana',e.target.value as Settings['furigana'])}><option value="always">Always show readings</option><option value="unfamiliar">Show for unfamiliar material</option><option value="hidden">Hide readings</option></select></label><label className="checkbox"><input type="checkbox" checked={draft.romaji} onChange={e=>change('romaji',e.target.checked)}/>Allow romaji as an early aid</label><label className="checkbox"><input type="checkbox" checked={draft.reduced_motion} onChange={e=>change('reduced_motion',e.target.checked)}/>Reduce interface motion</label><label className="checkbox"><input type="checkbox" checked={draft.sound} onChange={e=>change('sound',e.target.checked)}/>Enable optional interface sounds</label><p className="small">Reading aid preferences apply to the reading tools and are saved locally.</p></Card>
 <Card><h2>An optional daily goal</h2><label className="checkbox"><input type="checkbox" checked={draft.show_goal} onChange={e=>change('show_goal',e.target.checked)}/>Show my optional goal and routine suggestion</label>{draft.show_goal&&<p>A suggested routine: a short lesson and voluntary review when useful. Choose any other activity, or ignore the suggestion entirely.</p>}<label>Suggested XP goal<input type="number" min={1} value={draft.daily_goal??''} onChange={e=>change('daily_goal',e.target.value?Number(e.target.value):null)}/><span className="field-help">Leave blank for no goal. XP arrives with the lesson engine; this is never a cap.</span></label><label>Practice batch suggestion<input type="number" min={1} value={draft.practice_batch} onChange={e=>change('practice_batch',Number(e.target.value))}/><span className="field-help">A convenience preference for future practice. You’ll be able to request more or all.</span></label><label className="checkbox"><input type="checkbox" checked={draft.show_statistics} onChange={e=>change('show_statistics',e.target.checked)}/>Show activity statistics when available</label></Card>

 <Card>
  <h2><Database size={20} style={{verticalAlign:'middle',marginRight:'0.4rem'}} aria-hidden="true"/>Data safety, backup & reset</h2>
  <p>Your learning records, writing drafts, and FSRS schedules are stored on this computer. You can create a complete backup at any time or restore a previous snapshot.</p>
  
  <div className="backup-section">
   <div>
    <h3>Export backup</h3>
    <p className="small">Generates a SQLite-consistent snapshot including all sessions, attempts, XP ledger, writing drafts, and review schedules. Credentials and temporary caches are excluded.</p>
    <label className="checkbox"><input type="checkbox" checked={includeSamples} onChange={e=>setIncludeSamples(e.target.checked)}/>Include handwriting character formation samples</label>
    <div className="backup-row">
     <Button type="button" variant="secondary" onClick={downloadBackup}><Download size={16} aria-hidden="true"/>Download complete backup (.zip)</Button>
    </div>
   </div>

   <hr style={{borderColor:'var(--line)',margin:'0.5rem 0'}}/>

   <div>
    <h3>Restore from backup</h3>
    <p className="small">Restore progress from an existing backup archive. You will be able to review the snapshot contents before confirming. A safety backup of your current database is created automatically prior to restoration.</p>
    <input type="file" ref={fileInputRef} accept=".zip,.trilingo-backup" style={{display:'none'}} onChange={onFileSelected}/>
    <div className="backup-row">
     <Button type="button" variant="secondary" onClick={()=>fileInputRef.current?.click()} pending={previewLoading} pendingLabel="Reading archive…"><Upload size={16} aria-hidden="true"/>Select backup file to restore…</Button>
    </div>

    {preview && <div className="backup-preview-card" role="region" aria-label="Backup snapshot preview">
     <h4>Snapshot preview: {new Date(preview.created_at).toLocaleString()}</h4>
     <p className="small">Profile: <strong>{preview.profile.name}</strong> ({preview.profile.timezone}) · Schema version: <code>{preview.schema_version}</code> {preview.compatible ? <span className="badge mint">Compatible</span> : <span className="badge error">Incompatible</span>}</p>
     
     <dl className="backup-stats-grid">
      <div className="backup-stat"><dt>Total XP</dt><dd>{preview.summary.total_xp}</dd></div>
      <div className="backup-stat"><dt>Sessions</dt><dd>{preview.summary.study_sessions_completed} / {preview.summary.study_sessions_total}</dd></div>
      <div className="backup-stat"><dt>Review cards</dt><dd>{preview.summary.review_cards_count}</dd></div>
      <div className="backup-stat"><dt>Writing drafts</dt><dd>{preview.summary.writing_drafts_count}</dd></div>
      <div className="backup-stat"><dt>Collections</dt><dd>{preview.summary.collections_count}</dd></div>
      <div className="backup-stat"><dt>Drawing samples</dt><dd>{preview.summary.drawing_samples_count}</dd></div>
     </dl>

     <FeedbackPanel kind={preview.compatible ? 'info' : 'error'}>
      {preview.warning}
     </FeedbackPanel>

     <div className="backup-row" style={{marginTop:'0.5rem'}}>
      <Button type="button" variant="danger" onClick={confirmRestore} pending={restoring} pendingLabel="Restoring snapshot…" disabled={!preview.compatible}><ShieldCheck size={16} aria-hidden="true"/>Confirm and replace local data</Button>
      <Button type="button" variant="quiet" onClick={()=>{setPreview(null);setSelectedFile(null)}}>Cancel</Button>
     </div>
    </div>}
   </div>

   {safetyBackups.length > 0 && <details style={{marginTop:'0.5rem'}}>
    <summary><FileArchive size={16} style={{verticalAlign:'middle',marginRight:'0.3rem'}} aria-hidden="true"/>Safety backups saved on this device ({safetyBackups.length})</summary>
    <ul className="safety-backup-list">
     {safetyBackups.map(b => <li key={b.filename} className="safety-backup-item">
      <div>
       <strong>{b.kind === 'pre_restore' ? 'Pre-restore safety backup' : b.kind === 'pre_reset' ? 'Pre-reset safety backup' : 'Safety backup'}</strong>
       <div className="small">{new Date(b.created_at).toLocaleString()} · {(b.size_bytes / 1024).toFixed(1)} KB</div>
      </div>
      <code>{b.filename}</code>
     </li>)}
    </ul>
   </details>}

   <hr style={{borderColor:'var(--line)',margin:'0.5rem 0'}}/>

   <div>
    <h3>Reset progress</h3>
    <p className="small">Permanently clear study progress, XP, review cards, and writing drafts. Course content and published lessons remain untouched. An automatic safety backup will be created before resetting.</p>
    <Button type="button" variant="secondary" onClick={()=>setShowResetDialog(true)}><RotateCcw size={16} aria-hidden="true"/>Reset learning progress…</Button>
   </div>
  </div>
 </Card>

 {error&&<FeedbackPanel kind="error">{error}</FeedbackPanel>}{message&&<FeedbackPanel kind="success">{message}</FeedbackPanel>}<div className="save-row"><Button type="submit" pending={pending}>Save preferences</Button><span role="status">{dirty?'Unsaved changes':'All current preferences are saved'}</span></div></form>

 {showResetDialog && <Dialog title="Reset learning progress?" onClose={()=>setShowResetDialog(false)}>
  <div style={{display:'grid',gap:'1rem',marginTop:'0.5rem'}}>
   <FeedbackPanel kind="error">
    This action will permanently delete all completed study sessions, review cards, FSRS review histories, writing drafts, and earned XP. Course lessons will remain available.
   </FeedbackPanel>
   <p>A safety backup of your current database will be saved to your local backups folder automatically before resetting.</p>
   <div className="backup-row" style={{justifyContent:'flex-end',gap:'0.8rem',marginTop:'1rem'}}>
    <Button variant="secondary" onClick={downloadBackup}><Download size={16} aria-hidden="true"/>Download backup first</Button>
    <Button variant="quiet" onClick={()=>setShowResetDialog(false)}>Cancel</Button>
    <Button variant="danger" onClick={confirmReset} pending={resetting} pendingLabel="Resetting…">Yes, reset all progress</Button>
   </div>
  </div>
 </Dialog>}
 </>
}
