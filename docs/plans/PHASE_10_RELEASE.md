# Phase 10 — Trilingo Reliability, Backup, and Local Release

Status: Not started. Depends on: [Phase09](PHASE_09_REVIEW_PROGRESS.md) and the complete applicable [Plan9.2 handoff](PLAN_09_2_COMPLETION.md), including its qualified-content, supported-setup and real provider/device gates. Next: [Phase11 — Open-source GitHub release and launch](PHASE_11_OPEN_SOURCE_LAUNCH.md); maintain the verified beginner release and deliver later stages under their own gates.

## Goal

Make Trilingo safe and straightforward to use every day on the target Windows computer, with verifiable reading, writing, speaking, persistence, and restore behavior.

This file owns backup/restore, reliability and the local release gate. Windows installer implementation lives in [its separate EXE plan](WINDOWS_EXE_SETUP_PLAN.md); Android implementation lives in [its separate port plan](ANDROID_PORT_PLAN.md). Do not load or execute those tracks for a Phase10-only task. Use [the short continuation index](../AGENT_CONTINUATION_GUIDE.md) to select the current task and read other contracts only when a dependency requires them.

## Start here and execution order

Follow the current user instruction and any time/check bounds; do not inherit expired allowances. Use isolated stores and preserved originals. Before any download/upload, follow the exact source/destination/scope and total estimated network MB/GB approval rule in the remaining-work plan; progress replacement/deletion and public actions have separate authorization requirements.

1. **R0 — Confirm the release baseline.** Read current HANDOFF/source/schema and map the applicable Plan9.2 prerequisite evidence. Record the exact candidate and unresolved gates; do not repeat unchanged broad tests or treat missing qualified/device evidence as passed. If the full handoff is incomplete, report it before claiming Phase10 readiness. Early EXE/Android feasibility remains in its separate track.
2. **R1 — Specify the backup/restore contract.** Inspect all durable models, files and existing services; define the versioned manifest, inclusion/exclusion list, snapshot semantics, archive limits, compatibility and quiesce/staging/commit/recovery sequence below. Write the contract before building the API/UI. Keep optional data inclusion explicit.
3. **R2 — Implement data safety.** Add focused services, thin validated APIs, accessible export/restore/reset controls and required migrations. Test clean/populated round trips, old-version semantics, cancellation, malformed inputs and interrupted/concurrent recovery on disposable data before using the contract for any installer update or cross-platform transfer.
4. **R3 — Harden the local workflow.** Address measured security/performance issues, actual reminder delivery, source-launch/update/shutdown/offline behavior and major UI/accessibility findings. Preserve working grading, snapshots, rewards, FSRS and provider-disabled study; avoid speculative refactors.
5. **R4 — Verify the frozen candidate.** Run relevant final gates and the fifteen-step critical flow below, including real input/providers and backup recovery. Record unresolved requirements honestly; only the exact fully verified declared release can close this phase. Packaging/source changes afterward require their affected verification again.

Create evidence under `docs/verification/local-release/<candidate>/` when execution begins: `readiness.md` (baseline/prerequisites), `backup-contract.md`, `verification.md` (commands, results, physical/provider details), and `release-notes.md` (shipped scope/limitations/recovery). These paths are proposed artifacts, not existing proof. Update this phase/HANDOFF with their actual paths and the next task; the checklist below owns acceptance.

## Deliverables

- [ ] Preserve the confirmed project name **Trilingo** in visible app/browser identity, app metadata, README/setup documentation and local-release materials. Use a `trilingo-` prefix for distributed app/backup filenames where appropriate; version numbers and descriptive subtitles must keep Trilingo identifiable. Remove generic template names before the release handoff.
- [ ] Finish and audit the published beginner curriculum from Phase 3; reconcile the inventory with what the UI actually offers and label any unfinished extension.
- [ ] For a full A-B starter release, audit 92 basic kana plus taught patterns, 300 distinct contextual kanji, and 2,000 unique reviewed core word entries under the curriculum counting rules. A smaller playable slice is labeled partial and cannot claim full inventory coverage.
- [ ] Declare the release's learning scope using the [curriculum roadmap](../CURRICULUM_ROADMAP.md): first release A-B, later intermediate C-D and advanced E-F. Audit each later release's reviewed language/content/workshop requirements before advertising essay coverage.
- [ ] Audit the required `ui-ux-pro-max`/`frontend-design`/`design-skill` workflow against the [design brief](../DESIGN_BRIEF.md), recorded shared tokens, rendered screenshots, and resolved major visual/interaction findings. Include real Japanese reading and draft feedback surfaces.
- [ ] Audit unrestricted study across the feature inventory: directly selectable published content, unlimited skip/reveal/retry/replay, optional assessments/goals/quests/badges, freely selected cosmetics, any-time review, and non-expiring elapsed-time records.
- [x] Add local data export/backup and validated restore with a preview of profile/content/schema versions before applying changes.
- [x] Back up a live SQLite database with a consistent backup mechanism; do not copy only the main file while ignoring an active WAL.
- [x] Include studied/assessment/assistance/skip records, attempts, XP ledger, settings, actual activity history, optional quests/badges/personal records, cosmetic preferences, FSRS state/logs, and owned custom content in backups. No resource, purchase, or access-eligibility state is needed.
- [x] Include saved writing drafts, submissions/revisions, task/rubric versions, feedback provenance, portfolio/source notes for implemented stages, and clear personal-data inclusion notes in the backup contract.
- [x] Exclude credentials and transient recordings by default; document what is omitted, regenerable audio caches, and optional retained writing/audio samples.
- [x] Validate backup structure, schema version, sizes, checksums where provided, IDs, and reference integrity before changing live data.
- [x] Restore into a temporary location, verify it, create a pre-restore backup, then switch atomically using a documented recovery procedure.
- [x] Implement reset/restore replacement with explicit destructive-action confirmation; cancel leaves data intact. Export is available before reset.
- [ ] Harden API input, local CORS/binding, HTML rendering, media/file handling, URL settings, and bounded provider work; verify no secrets are committed or logged.
- [ ] Add appropriate DB indexes, paginated histories, measured course map/stats queries, lazy media loading, and measured startup/provider latency.
- [ ] Provide a verified PowerShell launcher or equally simple local launch process, port-conflict errors, graceful shutdown, and provider troubleshooting.
- [ ] Add configurable local in-app study reminders and optional permission-based notifications, with quiet hours and a truthful availability note. Use a documented local notification mechanism; a browser-only reminder works only while its supported app/service is running. No email, cloud push, or system scheduled task is installed during this planning task.
- [ ] Document installation, dependency versions, migrations, seeding, update, backup/restore, tests, providers, licenses, and troubleshooting in README.
- [ ] Verify local use with the internet disconnected after dependencies/content/provider models are installed. The local backend must remain running.
- [ ] Treat an installable PWA as a separately gated optional extension; cache the shell only if it cannot produce stale or fake progression. Never claim offline writes sync safely without implementing and testing conflict handling.
- [ ] Complete accessibility, responsive, visual, content, and critical-flow audits; remove misleading upcoming controls and misleading statistics.

## Intended implementation areas

Backup/import services and APIs, settings/danger-zone UI, Windows scripts, README, end-to-end tests, DB indexes/migrations, accessibility fixes, and release documentation.

## Data and API contracts

- Backup manifests are versioned and declare source schema/app/content versions, creation time, included files/entities, and omitted sensitive data.
- The inclusion inventory must explicitly account for immutable imported course versions/definitions and historical task/rubric snapshots, saved-item/collection membership and saved content snapshots, request/action/idempotency receipts and their stable IDs, active/paused/completed session/timer state, and optional retained drawing samples. Preserve old replay/grade/FSRS references and reward-retry semantics across restore. Document any intentional exclusion and its learner-visible effect; do not assume these records are covered by a generic progress total.
- Reject unsupported/future/corrupt backups before mutation. Offer no implicit merge semantics; v1 restore replaces a selected local profile/database only after explicit preview/confirmation and safety backup.
- Restore has point-in-time snapshot semantics: an older backup reinstates its saved progress, XP/activity, preferences, and review state, replacing later records. Show the snapshot date and rollback effect before explicit confirmation; there is no implicit merge or separate anti-rollback ledger.
- Prevent path traversal/archive expansion attacks and oversized imports. Import writes cannot target arbitrary filesystem locations.
- Restore/update replacement must quiesce new writes, await bounded in-flight transactions, and close all relevant SQLite/file handles before the same-volume switch. Use an exclusive operation owner and crash-recoverable state marker; reject/defer simultaneous restore/reset/update and ordinary mutations with useful recovery guidance. An interrupted switch must select a validated complete store on restart, never merge halves or leave two writers. Read-only UI/status access must not report success before the live replacement is acknowledged.
- Deleting progress cannot delete installed course assets or unrelated Docker volumes. Provider disk images are outside app reset scope.
- Document forward migration and recovery compatibility. Reversibility is best-effort; use backups before changes that cannot safely downgrade.
- If backup export itself includes personal recordings/writing, show that explicitly and apply the retention/export setting chosen by the learner.

## Tests and manual verification

Include concurrent restore/reset/update attempts, mutations during quiescence, open-handle/locked-file failures and interruption at each backup/staging/switch/restart step. Prove acknowledged writes are not lost through races or failed operations; intentional rollback is limited to the explicitly previewed/confirmed snapshot replacement. Old request receipts remain idempotent, and cancelled/failed operations leave a usable original or documented verified recovery store. These cases supplement the existing checklist; use disposable copies only.

- [ ] Run full frontend lint, typecheck, tests, production build, backend tests, clean-database migration, migration drift check, and API smoke tests.
- [ ] Run end-to-end tests against isolated data, not the real local profile DB. Cover the critical flow below.
- [ ] Test valid export/restore round trip, changed schema, unsupported version, malformed archive, broken references, interrupted restore, and cancelled reset.
- [ ] Compare restored study/skip/assistance records, XP/activity dates, and FSRS card/log state to the selected snapshot.
- [ ] Compare restored optional quest/badge/assessment/personal-record evidence and cosmetic preferences; events already credited inside the snapshot remain idempotent. Restoring old history never restricts current access to published content.
- [ ] Verify writing draft/revision/feedback round trips, Unicode/IME text, stale-save conflicts, and no duplicate composition rewards. Later releases must verify their essay workflow with AI disabled.
- [ ] Check 320px, 390px, approximately 768px, and desktop layouts; keyboard-only use, focus, zoom, Japanese ruby, screen-reader labels, contrast, and reduced motion.
- [ ] Run real Japanese TTS and microphone/STT checks on the target computer and record actual engine/model/voice/version evidence from Phase 8.
- [ ] Restart app/backend/providers, disconnect external internet, verify authored learning and installed local providers work, and verify optional-provider failures do not lose answers.
- [ ] Follow README from a clean environment or fresh temporary checkout/folder with documented prerequisites. Record anything that cannot be tested.
- [ ] Inspect logs, browser console, media retention, dependency licenses, and source tree for secrets/generated user data.
- [ ] Test reminder opt-out, permission denial, quiet hours, timezone changes, app restart, and closed-app limitations without fabricating delivered notifications.
- [ ] Test unrestricted direct access to all published material, continued study after repeated mistakes/skips, new sessions/replays beyond earlier quotas, voluntary early reviews, and preserved XP/work/access after a missed goal/day. No countdown ends an activity.

## Manual critical flow

1. Create the beginner profile and choose timezone, aids, and goal.
2. Open a later published lesson directly with a new profile, in both UI and API, without completing prior units or placement.
3. Answer correctly and incorrectly several times; inspect feedback and freely retry/reveal/skip/continue without losing XP or access.
4. Refresh/resume, finish with honest response/assistance/skip evidence, then choose any other published activity immediately.
5. Try a duplicate completion request and confirm the ledger does not change again.
6. Read kana and a short kanji-supported passage with aids on/off.
7. Enter Japanese with IME; perform a guided writing task and inspect its honest evidence label.
8. Complete an authored everyday dialogue, listen to Japanese output, record a phrase, and inspect the real STT transcript.
9. Disable providers and finish a core lesson using the documented fallback without fabricated speaking/listening assessment.
10. Review a due item/mistake, apply a rating, restart, and verify progress and FSRS persistence.
11. Try optional recap/mastery and story/audio practice in any order, use assistance or skip, and confirm the result never controls another activity.
12. Finish several genuine replays/practice sessions the same day and receive normal XP for each; compare optional personal timing without an expiry and select an available cosmetic directly.
13. Hide/edit optional goals/streak/reminder displays, miss a test day/goal under an isolated clock, and confirm XP, saved work, and access remain intact.
14. Write a guided paragraph, refresh/resume, optionally self-review, and submit; preserve honest evidence and uncapped new-session rewards. Test later workshop features against the declared release scope.
15. Export/restore isolated learning, optional feedback, preferences, and writing records; compare the snapshot and cancel a destructive reset to confirm no change.

## Completion gate

Complete for the declared release only after quality gates, real Japanese provider checks, combined feature/content-scope and rendered design audits, documented startup, backup round trip, and manual critical flow succeed. The first release claims A-B only; C-F require their own audited releases. Record incomplete checks and leave the relevant gate open. An editor, AI score, mocked provider, or unaudited syllabus cannot satisfy advanced essay coverage.

## Later extensions

Intermediate/advanced writing through complex essays is now approved staged scope in the curriculum roadmap, not an unspecified future idea. Richer handwriting recognition, specialized pronunciation assessment, adaptive difficulty beyond the current selector, additional course/profile management UI, authoring tools, and browser-offline synchronization remain separate possible extensions. The generic engine/data model must accommodate these without implementing all interfaces now.
