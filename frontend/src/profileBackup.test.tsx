import { renderToStaticMarkup } from 'react-dom/server'
import { expect, it } from 'vitest'
import { ProfilePage } from './ProfilePage'
import { ProfileSchema, SettingsSchema } from './schemas'

const sampleProfile = ProfileSchema.parse({
  id: 'local',
  name: 'Test Learner',
  timezone: 'Asia/Tokyo',
})

const defaultProvider = {
  enabled: false,
  provider: 'disabled',
  base_url: 'http://127.0.0.1:1234',
  model: '',
  voice: '',
  timeout: 20,
}

const sampleSettings = SettingsSchema.parse({
  daily_goal: 20,
  show_goal: true,
  furigana: 'always',
  romaji: true,
  reduced_motion: false,
  sound: false,
  show_statistics: true,
  practice_batch: 10,
  ai: defaultProvider,
  tts: { ...defaultProvider, provider: 'kokoro' },
  stt: defaultProvider,
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
