# Playable lesson — Phase 4

Product register, Operate mode. A beginner answers one authored prompt, sees committed feedback, and freely chooses Retry, Hint/Reveal, Skip or Continue.

The layout is a broad question frame inside the existing navigation shell: breadcrumb/pause control, real prompt progress, large Japanese response area, then feedback and actions in natural reading order. A small bottom navigation list permits revisiting any prompt. Mobile collapses to one column with wrapping controls and ordinary page scrolling; there is no timed/sticky overlay.

Use MASTER.md's existing Teal path (#126b62), Ink (#203c3b), Paper (#f8faf9), Mint (#e9f5ef), Plum (#704b77) and semantic error tokens. Segoe UI controls pair with Yu Gothic UI/Meiryo Japanese text. The signature is tactile answer chips that retain stable token identities even when their visible words repeat. Keep the question primary; actual XP appears only after saved completion.

The local ui-ux-pro-max dragging-movements result directly fits ordering: tap to add/remove and labeled move buttons support keyboard/pointer without requiring dragging. Its React controlled-form/submission results fit the implementation; the debounce-search result is unrelated and was not applied. Existing approved layout references are reused; no network/font/image dependencies are introduced.

All feedback includes text. IME composition never submits an answer. Pending network actions retain their receipt ID, input and retry path. Previewed draft assessments remain labeled Draft practice; unreviewed content never becomes reviewed through an engine test. Rendered audit evidence remains open until the real screen is inspected.
