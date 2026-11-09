import { useEffect, useState } from 'react'
import { request } from './api'
import { Button, FeedbackPanel } from './components'
import { TimingHistorySchema } from './practiceSchemas'
import type { z } from 'zod'

const modes: Record<string, string> = {
  lesson: 'Lessons', review: 'Self-rated recall', story: 'Stories',
  story_recap: 'Story recaps', listening: 'Listening', speaking: 'Speaking', writing: 'Compositions',
  writing_task: 'Constrained writing', handwriting: 'Formation',
  character: 'Characters', grammar: 'Grammar', assessment: 'Optional assessments',
  mistakes: 'Mistake practice', saved_items: 'Saved items',
}

function duration(seconds: number): string {
  const total = Math.round(seconds)
  const hours = Math.floor(total / 3600)
  const minutes = Math.floor(total % 3600 / 60)
  return `${hours ? hours + 'h ' : ''}${minutes}m ${total % 60}s`
}

export function TimingHistory({ refresh }: { refresh: number }) {
  const [open, setOpen] = useState(false)
  const [source, setSource] = useState('')
  const [limit, setLimit] = useState(5)
  const [query, setQuery] = useState<{ page: 'next' | 'previous' | 'last'; cursor?: string }>({ page: 'next' })
  const [history, setHistory] = useState<z.infer<typeof TimingHistorySchema> | null>(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const [retry, setRetry] = useState(0)

  useEffect(() => {
    if (!open) return
    let active = true
    setBusy(true)
    setError('')
    const params = new URLSearchParams({ limit: String(limit), page: query.page })
    if (query.cursor) params.set('cursor', query.cursor)
    if (source) params.set('source_kind', source)
    void request('/personal/timing?' + params, TimingHistorySchema).then(value => {
      if (active) setHistory(value)
    }).catch((error: unknown) => {
      if (active) setError(error instanceof Error ? error.message : 'History could not load. Retry this page.')
    }).finally(() => { if (active) setBusy(false) })
    return () => { active = false }
  }, [open, source, query, refresh, retry, limit])

  function filter(value: string) {
    setSource(value)
    setHistory(null)
    setQuery({ page: 'next' })
  }

  function navigation(label: string) {
    if (!history) return null
    return <nav className="inline-actions" aria-label={label}>
      <Button variant="quiet" disabled={busy || !history.previous_cursor} onClick={() => setQuery({ page: 'next' })}>First</Button>
      <Button variant="quiet" disabled={busy || !history.previous_cursor} onClick={() => setQuery({ page: 'previous', cursor: history.previous_cursor ?? undefined })}>Previous</Button>
      <Button variant="secondary" disabled={busy || !history.next_cursor} onClick={() => setQuery({ page: 'next', cursor: history.next_cursor ?? undefined })}>Next</Button>
      <Button variant="quiet" disabled={busy || !history.next_cursor} onClick={() => setQuery({ page: 'last' })}>Last</Button>
    </nav>
  }

  return <details onToggle={event => setOpen(event.currentTarget.open)}>
    <summary>Timed session history</summary>
    <p className="small">Saved active time excludes pauses. Timing and self-ratings describe practice. Invalid clock records are omitted; learning and XP are retained.</p>
    <label>History activity<select aria-label="History activity" value={source} disabled={busy} onChange={event => filter(event.target.value)}>
      <option value="">All activities</option>
      {Object.entries(modes).map(([value, label]) => <option key={value} value={value}>{label}</option>)}
    </select></label>
    <label>Records per page<select aria-label="Records per page" value={limit} disabled={busy} onChange={event => { setLimit(Number(event.target.value)); setQuery({ page: 'next' }) }}>
      {[5, 20, 50, 100].map(size => <option key={size} value={size}>{size}</option>)}
    </select></label>
    {busy && <p role="status">Loading timing history…</p>}
    {error && <FeedbackPanel kind="error">{error}<Button variant="quiet" onClick={() => setRetry(value => value + 1)}>Retry history page</Button></FeedbackPanel>}
    {history && <>
      <p role="status">{history.total} saved timed sessions in this view. Showing {history.records.length}.</p>
      {navigation('Timing history pages')}
      {!history.records.length && <p>No valid completed timed sessions in this view. Try all activities or start an optional timer during practice.</p>}
      <ol className="timing-history" aria-label="Saved timed sessions" aria-busy={busy}>
        {history.records.map(record => <li key={record.id} data-session-id={record.id}>
          <strong>{record.title}</strong>
          <p className="small"><time dateTime={record.completed_at}>{new Date(record.completed_at).toLocaleString()}</time> · {modes[record.source_kind] ?? record.source_kind} · {record.kind} · {record.mode}</p>
          <p>Active {duration(record.elapsed_seconds)} · {record.paused_seconds === null ? 'Pause duration was not recorded' : 'Paused ' + duration(record.paused_seconds)}</p>
          <p className="small">{record.assisted} assisted · {record.skipped} skipped{record.rating ? ` · ${record.direction ?? 'recall'} · ${record.rating} (self-rated)` : ''}</p>
        </li>)}
      </ol>
      {history.records.length > 5 && navigation('Timing history pages at end')}
    </>}
  </details>
}
