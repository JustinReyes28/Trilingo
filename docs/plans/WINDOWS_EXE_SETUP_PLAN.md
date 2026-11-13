# Trilingo Windows EXE setup plan

Status: **planning only; no packaged application or installer exists or is verified by this document.** Created 2026-10-25. This file owns the Windows setup track. Start with [the short routing guide](../AGENT_CONTINUATION_GUIDE.md), current [handoff](../../HANDOFF.md) and EXE-0 below. Open [Phase10](PHASE_10_RELEASE.md) when its backup/release contract is needed; Android and public-launch implementation stay in their own files. This is a delivery supplement, not a twelfth phase.

## Outcome and release boundary

Deliver `trilingo-setup-<version>-windows-x64.exe`: an offline-capable, per-user installer that supplies the application runtime, installs Start menu shortcuts and an uninstaller, and launches the existing original Trilingo learning experience. The learner should not need Node, npm, Python, PowerShell commands, Docker or an internet connection for authored core study and bundled MP3 audio playback after installation. Trilingo runs 100% locally with zero external or local AI, STT, microphone capture, or runtime TTS engines or model downloads.

A packaging prototype may use the honestly labeled published starter slice while Plan 9.2 is incomplete. It cannot be described as the full A-B release, satisfy content/provider gates, or bypass the Phase 10 completion gate. Public distribution also needs the licenses, release evidence and explicit publication authorization in [Phase 11](PHASE_11_OPEN_SOURCE_LAUNCH.md). Windows packaging does not establish an Android port or cross-device synchronization; see the [Android port plan](ANDROID_PORT_PLAN.md).

Initial target recommendation: Windows x64 on the user's actual supported Windows edition, then a separately recorded clean standard-user test machine. Record the exact OS version/build before claiming support. Windows ARM64 and additional OS versions need their own builds and verification; do not advertise them from one x64 result.

## Current repository facts to preserve

These are inspected source facts, not completed packaging work:

- [`scripts/start.ps1`](../../scripts/start.ps1) checks existing `.venv`/frontend dependencies, runs Alembic and the idempotent content importer, starts Uvicorn plus the Vite development server, and opens port 5173. It owns its child processes and logs to repository `.data`. It is a development launcher, not an installer build input to execute unchanged on an end-user machine.
- [`backend/app/config.py`](../../backend/app/config.py) derives `ROOT` from source layout, reads `ROOT/.env`, defaults the learner database and backups below `ROOT/.data`, and defaults `audio_pack_dir` to `ROOT/content/audio` (there is no runtime `AUDIO_CACHE_DIR`). Resource roots and writable learner data must be separated before freezing.
- [`frontend/src/api.ts`](../../frontend/src/api.ts) uses a Vite build-time API URL with a fixed port-8000 default. A packaged same-origin API/runtime bootstrap needs a validated implementation; changing a runtime environment variable after a build does not rewrite its compiled frontend.
- [`backend/app/main.py`](../../backend/app/main.py) creates the API, installs local CORS and request-size middleware, checks migration head through Alembic resources, and disposes its engine during shutdown. It does not currently serve the built frontend or implement launcher capability authentication.
- [`backend/app/cli.py`](../../backend/app/cli.py) validates/imports immutable course versions without resetting progress. [`backend/migrations/env.py`](../../backend/migrations/env.py) uses the central config and versioned migrations. Bundle those resources deliberately rather than relying on the working directory.
- The existing runtime default is `.data/trilingo.db`, schema head `0015` (`0015_remove_ai_stt_settings` strips `"ai"`, `"stt"`, and legacy `"tts"` preferences; updated 2026-11-13), source `ja-starter` 0.1.21. Re-read the current handoff and actual versions before a future build. No source-controlled learner DB, `.env`, logs, recordings, provider models, test databases, `.tools`, review packets, `node_modules`, or script-only `mutagen` (`GPL-2.0-or-later`) belong in the runtime installer.
- Phase 10 backup/restore, installer lifecycle, signing and packaged security/clean-install gates remain open. Existing frontend/backend checks do not prove a frozen build works.

## Proposed architecture and decisions

Use the existing React production build with the existing FastAPI/SQLAlchemy/Alembic/SQLite engine. Provisional packaging choice: **PyInstaller one-folder (`onedir`) application, wrapped by an Inno Setup full `.exe` installer**. PyInstaller can include the interpreter/dependencies; its one-folder form is easier to inspect before considering one-file extraction. Build on Windows for the declared architecture. These are supported upstream mechanisms, not a tested dependency compatibility claim for this repository. [PyInstaller operating modes](https://pyinstaller.org/en/stable/operating-mode.html).

The distributed setup file is one `.exe`; the installed application may contain an executable and internal resource files. Do not force the running application into PyInstaller `onefile` merely to satisfy the setup filename. Start without an embedded Chromium/WebView framework: a small owned launcher starts the local service and opens the user's installed default browser. A dedicated desktop app window is an explicit later decision if browser-hosted presentation fails the user's requirements; compare its additional runtime, download size, lifecycle and maintenance before adding Electron, Tauri, WebView2 or another GUI dependency.

Proposed installed layout, to validate in the first spike:

```text
%LOCALAPPDATA%\Programs\Trilingo\       installed executables/read-only app resources
  Trilingo.exe                         owned launcher and packaged backend entry point
  _internal\...                        pinned Python runtime/dependencies/resources
  _internal\content\audio\...          read-only bundled MP3 pack (90.4 MB)
  licenses\...                         notices and component license inventory

%LOCALAPPDATA%\Trilingo\               learner-owned writable app data
  data\trilingo.db                     migration-controlled durable learning records
  backups\...                          verified pre-upgrade/recovery snapshots
  logs\...                             bounded, redacted rotating logs
  config\...                           validated local configuration, if required
```

Resolve Windows known folders rather than assuming a particular username or literal C-drive location. These paths are design defaults; exports go to a user-selected local destination. Keep configuration separate from the packaged resource root and preserve source-mode defaults for developers. [Microsoft known-folder reference](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid).

Use per-user non-elevated installation (`PrivilegesRequired=lowest`) after proving that shortcuts, files and update behavior work under a standard account. Avoid an administrator service, scheduled task, firewall exception, registry-wide runtime modification or automatic startup for the first version. [Inno Setup privileges](https://jrsoftware.org/ishelp/topic_setup_privilegesrequired.htm).

### Local service ownership and browser security

These are required design tasks, not current protections:

1. A named per-user/per-data-directory mutex or equivalent establishes one writer/launcher owner. A second launch verifies the existing instance through a scoped authenticated control channel and opens its UI. A PID file or listening port alone does not prove process ownership; stale metadata cannot authorize killing a process.
2. Bind explicitly to `127.0.0.1`. Have the OS choose an available port and keep the bound socket through server handoff; do not probe, close and race another process for that port. The launcher's private resolved port is passed into validated configuration. No LAN binding or unauthenticated desktop-companion endpoint is added.
3. Serve the bundled frontend and `/api/v1` from that one origin. Add same-origin API configuration with validation and retain an explicit source-development override. Static fallback must not turn unknown API routes into successful HTML responses. Do not ship Vite, dev hot reload or a development proxy as the production server.
4. Create a fresh cryptographically random launch capability. Design and test a one-time browser bootstrap and authenticated API/control requests without placing reusable secrets in query strings, referrers, logs or localStorage. A possible spike is a short-lived single-use fragment bootstrap immediately removed from browser history, exchanged for an ephemeral session; this is a candidate, not an approved security implementation. Cookies are host-scoped across ports, so an HttpOnly/SameSite cookie or unique cookie name alone does not establish port isolation from another local server. Compare an in-memory capability header with a safe reload/rebootstrap mechanism; do not accept a cookie-only design without resolving that exposure. Include exact origin/host validation and capability checks in the final design.
5. Reject untrusted `Host`/`Origin`, null origins and cross-site state-changing requests; use a reviewed CSRF strategy. CORS is not authentication or complete CSRF protection. Verify all personal-data endpoints and control actions, including GET endpoints, cannot leak data to an untrusted website or another unauthenticated local process. Local account compromise is outside the promised protection boundary.
6. Keep capabilities in memory or a tightly permissioned same-user IPC mechanism, expire them on stop, redact diagnostics, and restrict any shutdown endpoint to the owning launcher. No unauthenticated HTTP shutdown route, remotely supplied shell arguments, arbitrary file serving or provider URL proxy.
7. Give the learner an accessible, truthful launcher status/Stop surface. Select the smallest maintainable implementation during the spike; an invisible background server without an understandable exit path is insufficient. Closing a browser tab must not be assumed to prove all tabs are gone. Explain when the app remains running; Stop waits for in-flight transactions within a safe timeout, disposes DB connections and stops only owned processes. Never close the user's browser or unrelated services.
8. On crash or failed startup, preserve data and show the app/version, safe log location and recovery action. Do not silently reinstall, reset progress, repeatedly migrate or report a healthy UI while its API has failed. Recovery can reopen a clean launcher after stale-instance validation; never infer an exited owner solely from an observation timeout.

## Work packages and evidence

Each package is unchecked. On a future implementation instruction, implement one coherent package at a time under any current user time/check bounds; update this document and the handoff with evidence. The spent18-check run is historical. Do not inherit or renew it, invent a deadline, or require a new numeric allowance when the current instruction sets none. Transfer/destructive/public approvals remain separate.

### EXE-0 — Packaging feasibility and declared support

- [ ] Read the current AGENTS/README/master/Phase 10/handoff and relevant source. Record baseline app, schema and content versions/hashes, release scope, supported Windows/Python/architecture and build-tool versions.
- [ ] Inventory installed PyInstaller/Inno/Windows signing tools and caches without installing anything. Decide and pin compatible build-tool versions in a dedicated build dependency manifest/lock; do not add packaging tools to learner runtime dependencies unnecessarily.
- [ ] Make a minimal frozen proof using an isolated QA data directory: imports, Pydantic/SQLAlchemy, FSRS/tzdata, Alembic discovery and a bundled content file. Inventory hooks/native bindings/data files that static import discovery misses.
- [ ] Record an architecture decision: default browser plus owned launcher versus a native host window; include accessibility, Japanese input, shutdown, startup time, measured bundle size and additional dependencies. Retain the default-browser choice unless evidence requires a different host.
- [ ] Produce a file manifest, license inventory, measured installed/build/temp size and toolchain transfer estimate. The authored audio pack measures **90.4 MB** (`4,394` MP3 clips at 128 kbps plus a 2.4 MB manifest) and must be included in the payload estimate; zero TTS engines, Kokoro containers, model weights, or script-only `mutagen` (`GPL-2.0-or-later`) belong in the runtime payload; re-measure the installer itself after packaging.

Evidence: `docs/verification/windows-exe/<version>/feasibility.md`, exact local commands/exit codes, isolated paths, build manifest and decision. Failed hooks or unavailable tools leave the spike partial; they are not a reason to download silently.

### EXE-1 — Paths, packaged resources and lifecycle

- [ ] Introduce focused validated resource/data path helpers that work from source and frozen layouts. Bundle built frontend assets, content (including the versioned `content/audio/<course>/<version>/` MP3 pack), Alembic configuration/revisions and required package data. Respect PyInstaller resource-path behavior rather than treating its temporary/internal resources as durable storage. [PyInstaller runtime paths](https://pyinstaller.org/en/stable/runtime-information.html).
- [ ] Preserve migration-driven persistence; no runtime `create_all`, bundled prepopulated personal DB or manual schema patch. If any new persistent settings change the schema, add the corresponding Alembic migration and forward-upgrade tests.
- [ ] Implement same-origin production frontend serving, launcher entry point, single-instance/port ownership, authentication/origin protection, readiness and graceful shutdown defined above. Add a development/QA data override that cannot silently target the default learner directory.
- [ ] Defer the source application's global creation until explicit packaged config is installed where necessary; never accidentally create or query a DB beside the frozen executable while discovering resources.
- [ ] Implement first-run import through existing validated/idempotent services. Reopening/reinstalling preserves stable IDs, snapshots, saved writing, assistance, FSRS/log history, XP ledger and all settings.
- [ ] Keep sensitive local config out of the frontend and logs, and preserve usable `AUDIO_PACK_ENABLED=false` (`503 audio_unavailable`) text/typed fallbacks (optional AI, STT, and microphone capture were removed in schema `0015`).

Evidence: targeted path/lifecycle/security regressions, clean disposable initialization, second-launch/occupied-port/failed-readiness checks and frozen critical-flow evidence. Any UI additions follow the repository's design/IME/accessibility workflow.

### EXE-2 — Backup-first update and recovery contract

Depends on the Phase 10 backup/restore service contract, which is not implemented by this plan.

- [ ] Version a manifest declaring app/schema/content versions, snapshot timestamp, included files/entities, checksums and exclusions. Preserve immutable content snapshots required by old sessions/cards/writing revisions.
- [ ] Produce a consistent live SQLite snapshot using the SQLite backup API, with integrity/reference checks and bounded lock/retry behavior. Do not copy only `trilingo.db` while ignoring an active WAL. The SQLite backup API is designed for consistent database snapshots. [SQLite backup API](https://sqlite.org/backup.html).
- [ ] Include durable learning/progress, XP/activity, settings, attempts/assistance/skips, writing/revisions, FSRS states/logs, collections, optional personal records and owned content. Exclude credentials and transient recordings by default (no runtime audio cache directory exists); clearly preview optional retained samples.
- [ ] Before migrating an existing installed profile, ensure exclusive app ownership, show upgrade/recovery status, validate available space and create/verify a recoverable pre-upgrade snapshot. If backup/validation fails, stop before migration and leave the old database intact.
- [ ] Prefer a migration/import preflight against a snapshot in staging. Close all live handles before an atomic same-volume switch, preserving the original until the new version passes integrity/readiness validation. Use a crash-recoverable journal/state marker; never leave two writers or silently lose writes recorded after the snapshot.
- [ ] Handle interrupted backup/migration/import/switch, invalid/missing resources, low disk, locked files and antivirus denial with a truthful resumable recovery path. Do not assume all SQLite schema operations can be rolled back by one application transaction.
- [ ] Block an older binary from opening an unsupported newer schema. Restoring an older snapshot is an explicit replacement of newer progress, not a merge or an automatic downgrade. Preview the date, omitted data and rollback effect, offer export and require confirmation before replacement.
- [ ] Support importing an existing developer-profile backup only through explicit selection/preview/confirmation. Do not automatically search for and migrate the learner's current source-checkout `.data/trilingo.db` on launch.

Evidence: valid round trip and upgrade from a populated previous version; corrupt/future/oversized/path-traversal archives; cancelled restore/reset; retained Japanese text; failed/interrupted update recovery; unchanged reward/idempotency and FSRS snapshots. Run every destructive case only on disposable copies.

### EXE-3 — Full installer and safe uninstall

- [ ] Add a reviewed PyInstaller `.spec` and Inno `.iss` under a dedicated `packaging/windows/` directory, plus scoped build scripts/documentation. They do not exist yet. Keep the Inno application identity stable across updates, use a declared app version and x64 compatibility policy, and include original Trilingo icon/version metadata.
- [ ] The installer contains the complete pinned application/runtime/content payload. It must not run pip/npm, download a browser/runtime/model, start Docker, request a firewall rule, or fetch dependencies during setup/first run. Build-time Node is not installed on the learner's system.
- [ ] Install per-user, create Start menu and optional desktop shortcuts, register the uninstaller, and give readable installation/upgrade errors. Installers update application files; learner DB migration happens through the verified launcher recovery contract, not ad hoc installer SQL.
- [ ] Detect an owned running app and request graceful closure before replacing files. Failure to stop cancels/defer the update rather than force-killing unrelated processes. Do not auto-launch as an elevated user or share one writable profile across Windows accounts.
- [ ] Uninstall removes only the installed program/owned shortcuts/registration. **Keep learner data and backups by default**, state their location, and verify reinstall can reopen them. A separate in-app delete/reset action requires explicit confirmation and export; never put recursive deletion of the data root into a silent uninstall hook.
- [ ] Provide manual offline update using a verified complete new setup file first. Automatic update checks, download agents/delta patches and background telemetry are deferred; any later design needs a bounded consent/download/signature/rollback policy.

Evidence: clean standard-user installation, cancel/retry, launch/relaunch, same-version repair, populated forward upgrade, unsupported downgrade rejection, uninstall with retained data, reinstall and separate explicitly confirmed deletion in isolated accounts/paths. Test non-ASCII usernames, spaces, read-only install resources and a working directory outside the install directory.

### EXE-4 — Signing, licensing and release record

- [ ] Inventory code/content/fonts/icons/runtime/package licenses and redistributable notices. Exclude draft material the declared package is not authorized to distribute; retain honest review/publication labels for any included previews.
- [ ] Decide private unsigned prototype versus signed distribution. Clearly label an unsigned prototype; never instruct the user to disable antivirus/SmartScreen or claim signing guarantees reputation or removes all warnings.
- [ ] For distribution, obtain an authorized signing identity; keep certificate/private key outside source control. Sign owned executables and setup/uninstaller as appropriate, use explicit digest algorithms and an approved timestamp endpoint, then verify signatures on final artifacts. Signing and timestamping are supported by Microsoft SignTool; Inno can invoke a configured signer for setup/uninstall. [Microsoft SignTool](https://learn.microsoft.com/en-us/windows/win32/seccrypto/signtool), [Inno signing integration](https://jrsoftware.org/ishelp/topic_setup_signtool.htm).
- [ ] Treat certificate enrollment/cloud signing/timestamp requests, revocation checks and release uploads as separately bounded external traffic where applicable. Ask for exact source/destination, scope and estimated size before invoking them; no signing purchase/publication is implied.
- [ ] Produce release version, source identifier/tree manifest, schema/content versions/hashes, build environment, dependency/license manifest, SHA-256 checksums, artifact sizes, signature status, known limitations and recovery instructions. Do not claim byte-reproducible builds until demonstrated.
- [ ] Store build logs locally after redaction. Publishing installer/checksums/screenshots is a Phase 11 action requiring explicit authorization and a transfer estimate.

### EXE-5 — Packaged release validation

- [ ] Run relevant source gates first, then verify the actual frozen bundle and final installed payload. Source Vite/browser passes cannot substitute for packaged execution.
- [ ] On an isolated Windows account/machine with no Node/Python/project checkout required, install offline, launch, directly open later published material, use hints/reveal/skip/retry/pause/resume, finish and restart. Verify durable progress and unrestricted new genuine-session XP versus idempotent duplicate requests.
- [ ] Verify kana/ruby, Japanese IME composition, guided writing autosave/conflict/revision, unassessed evidence labels, grammar/dialogue recovery, saved-item/collection navigation and same-card early FSRS review. Compare records across restart/upgrade/restore.
- [ ] Inspect 320/390/tablet/desktop, keyboard-only focus/labels, screen reader, zoom/reduced motion and physical input. Record exact browser/OS/device; automated snapshots do not close physical IME/accessibility gates.
- [ ] Confirm expected outbound traffic with external internet blocked: core app still works; no update/telemetry/font/CDN/model/bootstrap request occurs. Separate browser/Windows background traffic from app-origin requests before making a precise claim.
- [ ] Verify bundled `content/audio/` MP3 playback (`0.75x` with `preservesPitch=true` and `503 audio_unavailable` text fallback when disabled). Zero AI, STT, microphone capture, or runtime TTS engine or model weights are bundled or downloaded; qualified human listening review (`F3`) still gates the full speaking/listening release claim.
- [ ] Test malicious origins/hosts, unauthenticated data reads/writes, bootstrap reuse, another local process, static path traversal, invalid backups, bounded media uploads, stale-instance metadata, simultaneous launch, suspend/resume, OS shutdown, crashes and low disk.
- [ ] Measure cold/warm startup, idle memory, final installer/installed size and representative large-history operations with the declared content scope. Record targets before optimizing; do not hide existing bundle warnings or invent performance results.
- [ ] Complete Phase 10's full regression, backup round trip and manual critical flow; reconcile every remaining gate in its owning phase. Only then label the installed application a verified release for its declared scope.

## Future commands and proposed artifacts

**Examples below are future commands, not executed evidence.** Run only after the named scripts/specs and pinned tools exist and their paths/options are checked. They are local operations when all dependencies are already installed. No command here grants permission to install missing tools or test against real learner data.

```powershell
# Existing source build/gates, with the supported installed runtime on PATH:
Set-Location frontend
npm run lint
npm run typecheck
npm test -- --run
npm run build
Set-Location ..

# Future packaging spec: tool installation is a separate approved transfer.
.\.venv\Scripts\python.exe -m PyInstaller --noconfirm packaging\windows\trilingo.spec

# Future installer script; use the verified installed Inno compiler path.
& '<installed-Inno-compiler>\ISCC.exe' packaging\windows\trilingo.iss

# Measure a produced local artifact before requesting permission to transfer it.
Get-Item -LiteralPath '<actual-output>\trilingo-setup-<version>-windows-x64.exe' |
    Select-Object Name, Length
Get-FileHash -Algorithm SHA256 -LiteralPath '<actual-output>\trilingo-setup-<version>-windows-x64.exe'
```

Expected future deliverables: a dedicated pinned build-tool manifest/lock, resource/data-path adapter, production same-origin hosting, authenticated owned launcher, PyInstaller spec/hooks, Inno installer script, upgrade/recovery implementation and tests, local build instructions, user install/update/uninstall/backup guide, and versioned evidence under `docs/verification/windows-exe/<version>/`. Name additional scripts/tests only when implemented; do not report placeholder paths as working commands.

## Historical transfer notes (superseded 2026-11-09 & 2026-11-13)

*(The 2026-10-25 cellular-transfer paragraphs below are historical; the connection has been unmetered since 2026-11-09 per [AGENTS.md](../../AGENTS.md#network-and-external-actions), and as of 2026-11-13 zero runtime TTS engines or TTS models are downloaded or bundled in the Windows installer — only the committed `90.4 MB` `content/audio/` MP3 pack ships.)*

Ordinary focused official documentation reads are allowed. No package/runtime/browser/model/container download, Git transfer, code-signing upload, installer upload or remote publishing is authorized by this plan.

For each future bounded external batch, record the exact official package/release source or upload destination, pinned versions/architecture, transitive dependencies/layers and retry policy. Inventory local caches first. Estimate total network **MB/GB**, explain uncertainty, identify separately any disk space needed for cache/build/unpacked app/staging/database backups, and ask the user to approve that batch before starting. Stop at the approved size/scope; a cache miss or unknown size does not authorize a transfer or automatic retry. Disable package-manager background audit/update downloads while doing approved installs where supported.

There is no measured installer/toolchain size yet. Do not invent a download allowance from a generic PyInstaller estimate: measure the actual built `.exe` and inventory missing tools first. For an upload, the artifact byte length plus protocol overhead gives a bounded request; Git must include actual reachable objects/history rather than only source-file size. Keep optional provider/model packages separate because they can dominate both network and disk use. Signed/timestamped artifacts may change final sizes; measure again before a release transfer request.

## Next-agent handoff checklist

- Read the latest handoff and remaining-work plan; follow the current implementation instruction and any time/check bounds it specifies, preserving all phase gates and current learner data. Do not invent a new numeric approval step solely because a past run had one.
- Start at the first unchecked package whose dependencies are satisfied. EXE-0 can investigate feasibility locally; it cannot close Plan 9.2 or Phase 10.
- Use disposable per-user QA roots and snapshots, never the current learner profile for migration/restore/install tests. Preserve exact source/content/schema IDs and idempotency semantics.
- Record changed files, exact commands/exit codes, environment, database paths, network bytes/approval scope, screenshots/manual evidence, unmet checks and next work. Leave blocked or unverified boxes open.
- Stop owned QA/launcher services, retain readable local evidence, and update this plan plus `HANDOFF.md`. A setup `.exe` file existing is not proof of a safe install, full curriculum, qualified human audio review, or release readiness.
