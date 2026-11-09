# Windows Japanese input verification

Documentation checked 2026-10-23 against [Microsoft Learn's Japanese IME guide](https://learn.microsoft.com/en-us/globalization/input/japanese-ime) and [Microsoft Support's IME reference](https://support.microsoft.com/en-us/windows/hardware/input-devices/microsoft-japanese-ime). The in-app guide under Writing contains the setup steps and an unsaved input tester. It does not install language support or change Windows settings.

Observed host: Windows NT 10.0.26200.0. The documentation describes Windows 11; this run did not exercise its actual settings or a physical Japanese keyboard/IME. The guide's source verification and automated input checks cannot prove physical conversion behavior.

Pending physical checks (Plan 9.2 D4):

- Choose the installed IME and enter kana, select a kanji candidate and confirm it.
- During conversion, confirm Enter changes the candidate without submitting an exercise.
- Compose a sentence and a paragraph; check paste, focus, autosave and refresh.
- With two tabs and a failed save, retain both texts and avoid duplicate submission XP.

No physical device, screen reader, touch/stylus or Japanese-language review gate is closed by documentation verification.
