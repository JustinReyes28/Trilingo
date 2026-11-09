# Trilingo — Android Port Plan

Created: **2026-10-25**. Status: **planned; no Android project, APK, device build or port is implemented or verified**. This file owns the Android track. Start with [the short routing guide](../AGENT_CONTINUATION_GUIDE.md), [AGENTS.md](../../AGENTS.md), current [handoff](../../HANDOFF.md) and A0/A1 below. Consult desktop service/backup plans when parity or transfer requires them; do not load Windows packaging or public-launch details for Android feasibility. This supplement preserves the existing eleven phases, reviewed-content gates and unrestricted-study rules.

## Target and planning assumptions

The user confirmed an **independent, local-first Android app**: after installation and approved content provisioning, core lessons, deterministic grading, writing, saved progress, normal XP and real FSRS work with airplane mode enabled and no PC. A Windows-connected companion would require a separate scope decision. An APK that displays the UI but needs a Windows server has not met this target.

Reuse original Trilingo content and the React/strict TypeScript/Zod UI where suitable. Keep grading, transaction rules, idempotency, rewards, schedules and durable records in a device-local service/database layer. A WebView is a renderer, not permission to move authoritative progress into localStorage. Optional AI/TTS/STT remain capability-based; core study works when all are disabled. No account, cloud backend, subscription, forced sync or study restriction is introduced.

Initial distribution target is a **signed sideloadable APK** for the agreed physical phone. A Play Store AAB is a later distribution decision with its own account, policy and upload approvals. Decide minimum OS/device/ABI coverage from the actual phone and selected supported toolchain; no device was inspected for this plan. Start with arm64 hardware if appropriate; add an emulator ABI only when its validation value justifies the download/storage cost.

## Architecture and the first decision

The proposed shell is **Capacitor with bundled production React assets and a narrow Kotlin bridge**. Capacitor supports communication between web code and native Java/Kotlin; its `webDir` points to compiled assets. This supports UI reuse, but does not supply Trilingo's Python services. See [Capacitor Android](https://capacitorjs.com/docs/android) and [configuration](https://capacitorjs.com/docs/config).

The current app depends on FastAPI/Pydantic/SQLAlchemy/Alembic and **py-fsrs6.3.2**, plus compiled dependencies including **pydantic_core2.50.1**. Windows wheels, `.venv`, Uvicorn processes and the Vite development server cannot simply be copied into an APK. The present `http://127.0.0.1:8000/api/v1` default points at the phone itself on Android; it is not a PC discovery mechanism.

**Chosen decision order:** first prove whether the existing Python learning services can run embedded through Chaquopy behind the native bridge. This preserves authoritative behavior if the exact required dependencies work. Chaquopy documents Python/ABI/build requirements and package support varying by Python version; those facts do not prove compatibility with this project's lockfile. [Official Gradle/Python packaging documentation](https://chaquo.com/chaquopy/doc/current/android.html).

If the dependency and lifecycle spike fails, record the exact blocking package/version/ABI and use the fallback: implement the same service contracts in Kotlin over Android SQLite. This is an explicit domain-engine port, not a thin UI wrapper. Do not weaken validation, substitute an approximate scheduler, loosen the desktop lockfile or spend multiple sessions trying unrelated runtimes. Make the A1 decision before building the full port; implement only the selected path.

No embedded HTTP server is required by the proposed Android design. Use an asynchronous native service bridge for domain calls, preserving the public request/result/error shapes. If a technical spike proposes a loopback server instead, justify startup/process-death/security/resource costs and validate them before selecting it. A remote service, permanently running PC or hosted database changes the independent-app target and needs an explicit scope decision.

## A0 — Confirm scope and prerequisites

Record the intended phone model/Android version, available physical device, supported ABI/minimum OS, distribution channel, application-ID owner and signing-key custodian. Use a legitimate reverse-domain application ID; do not invent ownership of `com.trilingo`. The visible product name stays **Trilingo**.

Inventory installed JDK/Android SDK/Gradle/Android Studio/ADB and existing caches without installing, auto-updating or scanning personal device data. Identify the compatible Capacitor/Android Gradle plugin/JDK/SDK/Python versions from official documentation at implementation time, then pin them. Do not pin this plan's documentation snapshot as a tested toolchain. Device connection/debugging and installation require the user's intended device, not an arbitrary attached phone.

Prepare a transfer proposal before missing toolchain/plugin/wheel/SDK/emulator/model retrieval: exact versions and sources, cache coverage, transitive network MB/GB, installed disk requirement, uncertainty and offline alternative. No `npm install`, `npx` cache miss, Gradle dependency resolution, SDK auto-install or ADB installation is executed by this document.

**Exit:** scope/device/toolchain inventory and bounded transfer requirements are concrete. Unknown prerequisites stay named; no APK success is claimed.

## A1 — Prove the device-local engine choice

In a disposable Android spike, use synthetic data to prove the full required service dependency graph, not merely `print()` from Python. For the embedded-Python path, verify supported Android wheels or explicitly budgeted builds for Pydantic core and every required native extension; SQLite/SQLAlchemy/Alembic resource paths; timezone data; py-fsrs; UTF-8 content and original assets. Separate runtime requirements from development/test tools; document any packaging-specific lock without silently changing desktop requirements.

Run a minimal bridge operation that migrates an isolated database, imports a validated source, grades one exercise, commits one session/XP event and schedules/reloads one real review. Kill/reopen the app and verify persisted results. Measure cold start, resident memory, APK/native-library size and latency on the target device. Exercise error propagation and transaction rollback. Record exact versions/ABIs/licenses and Android background/lifecycle behavior.

If that fails on a required dependency or acceptable lifecycle/performance, close the spike with evidence and choose Kotlin services. Candidate [Java-FSRS](https://github.com/open-spaced-repetition/java-fsrs) supports real scheduler/card/log objects, but its existence or JSON serialization does not establish compatibility with stored py-fsrs state. Require A2 parity before reusing learner schedules.

**Exit:** one written architecture decision with an executable device proof and measured costs, or an explicit native-port work breakdown. No broad mobile implementation proceeds on an unproven Python dependency assumption.

## A2 — Freeze portable contracts and prove behavioral parity

Inventory the existing API/schema/service surface in `backend/app/learning*`, `reading*`, `writing*`, `handwriting.py`, `stories.py`, `review*`, `collections.py`, `practice_api.py`, `schemas.py`, `content_schema.py` and frontend Zod schemas. Preserve the backend's public/private answer boundary, assistance receipts, source snapshots and error semantics. Add a narrow transport interface at the existing `frontend/src/api.ts` boundary: HTTP for desktop/browser, native dispatch for Android, with the same response validation. Keep feature pages and language content independent of platform selection.

Create shared deterministic fixtures from synthetic authoritative Python results. Cover accepted/rejected Japanese normalization, small kana/dakuten/long vowels, answer alternatives, wrong/correct/assisted/skipped evidence, every shipped exercise type and dialogue transition, resumable writing/conflicts/submissions, collections/snapshots, optional quests, timing and statistics. Compare complete effects and errors, not only a displayed score.

For FSRS pin algorithm/library version, parameters/retention, fuzzing behavior, units, UTC precision and state serialization. Prove Again/Hard/Good/Easy, learning/relearning, early review, repeated genuine reviews, missed-day/timezone/DST histories, duplicate/stale/concurrent requests, receipts and rollback. Preserve uncapped new-session XP versus one-event network/native retries. Newer scheduler defaults are not a migration strategy. If parity is impossible, stop the affected import and define an explicit versioned conversion with preservation evidence; never discard or reset schedules to make a test pass.

**Exit:** selected Android engine and desktop reference pass the same behavior/effect fixtures, including negative cases. A native implementation is complete only when the supported service surface is accounted for; unsupported modes remain explicitly unavailable, not simulated.

## A3 — Persist all learning data and handle Android lifecycle

Store the database and owned samples in app-private storage, with explicit cache and bundled-resource separation. Implement versioned migrations and transactional related writes; do not mix Alembic and native migration owners on the same database. If Kotlin is selected, define its migration/backup schema mapping and test old-to-new upgrades; a shared JSON contract does not prove byte-compatible SQLite files.

Persist sessions/attempts, XP ledger/activity, timezone history, FSRS state/logs/receipts, settings, goals/quests/badges, saved items/collections/content snapshots, writing revisions/conflicts/submissions and optional drawing samples. Treat recordings/cache separately. Reconcile interrupted bridge calls after rotation, backgrounding, process death, low storage or a lost acknowledgement; stable request IDs prevent duplicate rewards. Restore editor buffers safely without making browser recovery the sole durable copy.

Android removes app-specific storage on uninstall. Provide a user-visible export path and explain uninstall/data-clear effects; do not promise Windows-style retained data. [Android app-specific storage](https://developer.android.com/training/data-storage/app-specific). Default the learner store and private samples to backup-excluded app-private storage, with explicit backup/data-extraction rules; keep recordings, credentials and provider endpoints out of automatic cloud/device backup. Test actual supported-OS/OEM behavior and document platform limits rather than promising control over every system backup mechanism. Any optional exported backup uses the user's explicit destination/transfer approval. [Android backup rules](https://developer.android.com/identity/data/autobackup).

**Exit:** isolated clean install/forward upgrade/process-death/low-storage recovery tests pass without reset or duplicate events. Uninstall limitations and export availability are accurate.

## A4 — Port the complete declared study surface

Bundle the matching content/asset manifest; retain immutable IDs/versions and reviewed/draft distinctions. Port course browsing, shared exercise renderer, stories/grammar, reading aids/search/saved items, writing editor/checklists/history/conflicts, formation/optional samples, review/collections, settings and personal records. Keep all published activities directly selectable and ordinary hint/reveal/skip/retry/replay/pause/finish controls available.

Use the established Trilingo tokens and required UI skills. Test physical Japanese IME conversion and Enter, paste, keyboard dismissal, back navigation, autosave, rotation, display cutouts/insets, small screens/tablets/landscape, font scaling, Japanese ruby and TalkBack order/voice. A desktop responsive screenshot does not prove Android behavior. Preserve keyboard/accessible formation alternatives; assess real touch/stylus independently. Confirm WebView/native capabilities rather than assuming browser MediaRecorder or permission behavior matches desktop Edge.

Keep privileged bridge methods narrowly allowlisted and validated. Remote pages must not gain access to database/file/microphone methods; open external links outside the privileged WebView. Production loads bundled assets, not a developer `server.url`; avoid general-purpose file access, arbitrary SQL execution or executable generated HTML.

**Exit:** every feature claimed in the APK has real device evidence and accurate unavailable/loading/error states. An intentionally reduced preview must be declared separately; it cannot be advertised as the complete port.

## A5 — Audio, microphone, reminders and optional providers

Keep the all-providers-disabled route usable in airplane mode. Select Android recording/playback/TTS/STT adapters using actual capability checks, privacy behavior, language availability, CPU/memory and licenses. A Japanese system voice or recognizer is not automatically an offline equivalent of the verified desktop provider. SpeechRecognizer may use remote services; use supported on-device capability checks and prove Japanese behavior before an offline claim. [Android SpeechRecognizer](https://developer.android.com/reference/android/speech/SpeechRecognizer), [TTS Voice network requirement](https://developer.android.com/reference/android/speech/tts/Voice).

Request microphone/notification permissions only for the requested feature. Handle denial/revocation, interrupted recordings, missing Japanese voices/models, audio focus, backgrounding and cleanup with typing/transcript/retry fallbacks. Do not auto-download voices or model packs; obtain the same sized transfer approval as other assets. Label transcript comparison as transcript feedback, never phoneme/pitch scoring. No missing provider removes earned XP or study access.

Do not copy Windows `localhost` provider settings as a working phone endpoint. Optional PC/LAN providers require a separate authenticated, encrypted, explicitly configured connection; keep the desktop default loopback-only. Do not expose the present FastAPI service through `0.0.0.0`, relax CORS globally or enable broad cleartext traffic to make a demo work. Define per-endpoint network security and record the chosen provider's real behavior. [Android network security configuration](https://developer.android.com/privacy-and-security/security-config).

Implement optional local reminders with platform-appropriate permissions/scheduling, quiet hours and timezone handling. Notifications are advisory; denial, force-stop or OS scheduling limitations never block study and must be explained accurately.

**Exit:** tested permissions/capabilities/failure paths and real Japanese integration evidence for each claimed audio feature. Core offline scope remains independently verified.

## A6 — Windows/Android transfer without automatic synchronization

Reuse the versioned backup contract owned by [Phase10](PHASE_10_RELEASE.md) and [Windows setup](WINDOWS_EXE_SETUP_PLAN.md). Define a platform-neutral manifest with schema/content/engine versions, supported entities, checksums, included optional samples and explicit exclusions. Add a validated conversion only if schemas differ; raw SQLite copying is allowed only after compatibility is proved. Exclude credentials, machine paths, provider runtime state and transient recordings by default.

Use the Android system file picker for an intentional export/import, validate bounded archives/references, restore into a temporary store, create a pre-restore backup, then commit atomically. Reuse explicit replacement/confirmation/cancel semantics. Do not introduce a silent merge of two diverged histories or recalculate XP to fit a second device. Prove Windows→Android→Windows round trips with Unicode drafts/conflicts, snapshots, FSRS transitions and receipt identity. Unsupported/future backups must fail before live mutation. [Storage Access Framework](https://developer.android.com/training/data-storage/shared/documents-files).

File providers can be remote/cloud-backed: choosing the system picker does not waive the user's cellular/upload approval. Offer a clear local destination and identify any network destination before transfer. Real-time synchronization, user accounts and a cloud service remain separately scoped future work.

**Exit:** cross-platform export/restore either passes for an explicitly supported version pair or is clearly disabled. Progress never silently disappears during a format or device transition.

## A7 — Reproducible signed APK and distribution

Add versioned Android project/build scripts, pinned dependencies/checksums, licenses/notices, original Trilingo icons and a release manifest. Keep package identity, content version, schema and engine version distinct. Build on an authorized/cached toolchain; Gradle offline mode is useful only after all dependencies exist. Record cold-start/memory/storage/APK size and chosen supported devices; do not invent an APK MB estimate before a build exists.

Protect the signing keystore/password outside the repository and logs; establish an owner-controlled local backup and recovery procedure. Android installation/update requires signed APKs; future updates must retain a compatible signing identity. [Official signing guidance](https://developer.android.com/studio/publish/app-signing). Verify signed-package metadata and install/upgrade with disposable app data on the intended test device, with user-approved device actions and payload size. Debug installation is not a verified release APK.

For Play distribution later, separately confirm current target-SDK/store policies, account ownership, signing/AAB workflow, privacy/data-safety declarations, testing requirements and exact upload sizes. No store account, telemetry, crash upload, hosted service or publication is authorized by this planning request.

**Exit:** a signed installable artifact with SHA-256, size, version/ABI manifest, reproducible instructions and evidence for the declared scope; distribution remains a separate approved action.

## A8 — Final device release gate

- [ ] Standalone cold start and all core study work in airplane mode with no PC.
- [ ] Clean install, populated forward upgrade, app restart/process death, storage failure and owned-resource cleanup preserve progress.
- [ ] All declared service contracts, private answer boundaries, grading, honest evidence, unlimited genuine-session XP and idempotent retries match the desktop reference.
- [ ] FSRS versions/state/logs/timezones and supported backup transfers pass deterministic parity and recovery tests.
- [ ] Real Japanese IME, TalkBack, touch/stylus alternatives, fonts/ruby, permissions and claimed Japanese audio features have named-device evidence.
- [ ] No unapproved remote traffic/backup, provider/model download, destructive progress action or publication occurs.
- [ ] Exact APK signing/identity/hash/size, licenses, reviewed/published inventory, known limitations and device support are recorded.

The complete A–B Android release also requires the shared qualified-content and release safety gates. An Android shell/spike, sideloaded debug build or fewer verified features is recorded as a prototype/preview, not full completion. Public distribution is conditional on explicit artifact/size/channel approval.

## Suggested future execution batches

Start with A0 and a focused A1 feasibility deliverable. Then A2+A3 contracts/persistence, A4 core UI, A5 actual integrations, A6 transfer, and A7+A8 release. Reuse the desktop reference tests; expand only for new platform behavior or real failures. Honor any time/check bounds in the current implementation instruction and stop when spent; do not inherit past limits, invent a deadline or require a numeric allowance when none is set. The initial port need not wait for GitHub/social launch or C–F authoring, but it cannot bypass beginner publication/data-safety gates. Update this plan and the handoff with actual decisions and evidence after each batch.

Official text documentation was read on2026-10-25. No SDK, plugin, wheel, APK, model, dependency or source repository was downloaded; no Android commands, builds, device actions, application tests or uploads were run to create this plan. Recheck volatile requirements before implementation.
