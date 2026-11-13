import { renderToStaticMarkup } from 'react-dom/server'
import { expect, it } from 'vitest'
import { ProfilePage } from './ProfilePage'
import { ProfileSchema, SettingsSchema } from './schemas'

const sampleProfile = ProfileSchema.parse({
  id: 'local',
  name: 'Test Learner',
  timezone: 'Asia/Tokyo',
})

const sampleSettings = SettingsSchema.parse({
  daily_goal: 20,
  show_goal: true,
  furigana: 'always',
  romaji: true,
  reduced_motion: false,
  sound: false,
  show_statistics: true,
  practice_batch: 10,
})

it('renders profile preferences without optional AI, STT, or TTS provider settings', () => {
  const html = renderToStaticMarkup(
    <ProfilePage profile={sampleProfile} settings={sampleSettings} onSaved={() => {}} />
  )

  expect(html).not.toContain('Optional local providers')
  expect(html).not.toContain('AI_ENABLED')
  expect(html).not.toContain('STT_ENABLED')
  expect(html).not.toContain('lm-studio')
  expect(html).not.toContain('AI explanations')
  expect(html).not.toContain('Japanese speech recognition')
  expect(html).not.toContain('Japanese speech output')
  expect(html).not.toContain('TTS_ENABLED')
  expect(html).not.toContain('kokoro')
  expect(html).not.toContain('jf_/jm_')
  expect(html).not.toContain('>Voice<')
  expect(html).not.toContain('Transient audio recordings')
  expect(html).toContain('Credentials and temporary caches are excluded.')
})

it('renders backup export, restore, and reset controls on profile page', () => {
  const html = renderToStaticMarkup(
    <ProfilePage profile={sampleProfile} settings={sampleSettings} onSaved={() => {}} />
  )

  expect(html).toContain('Data safety, backup &amp; reset')
  expect(html).toContain('Export backup')
  expect(html).toContain('Download complete backup')
  expect(html).toContain('Include handwriting character formation samples')
  expect(html).toContain('Restore from backup')
  expect(html).toContain('Select backup file to restore…')
  expect(html).toContain('Reset progress')
  expect(html).toContain('Reset learning progress…')
})

it('mentions safety backup generation and SQLite consistency', () => {
  const html = renderToStaticMarkup(
    <ProfilePage profile={sampleProfile} settings={sampleSettings} onSaved={() => {}} />
  )

  expect(html).toContain('SQLite-consistent snapshot')
  expect(html).toContain('safety backup of your current database is created automatically')
  expect(html).toContain('Course content and published lessons remain untouched')
})
