---
title: "Windows (Native) Guide — Early Beta"
description: "Early BETA: run Quill Agent natively on Windows 10 / 11 — install, feature matrix, UTF-8 console, Git Bash, gateway as a Scheduled Task, editor handling, PATH, uninstall, and common pitfalls"
sidebar_label: "Windows (Native) — Beta"
sidebar_position: 3
---

# Windows (Native) Guide — Early Beta

:::warning Early BETA
Native Windows support is **early beta**. It installs, runs, and passes our Windows-footgun lint, but it hasn't been road-tested at the scale our Linux/macOS/WSL2 paths have. Expect rough edges — especially around subprocess handling, path quirks, and non-ASCII console output. Please [file issues](https://github.com/YOUR_USERNAME/quill-agent/issues) with repro steps when you hit something. If you want a battle-tested setup today, use the [Linux/macOS installer under WSL2](./windows-wsl-quickstart.md) instead.
:::

Quill runs natively on Windows 10 and Windows 11 — no WSL, no Cygwin, no Docker. This page is the deep dive: what works natively, what's WSL-only, what the installer actually does, and the Windows-specific knobs you might need to touch.

If you just want to install, the one-liner on the [landing page](/) or [Installation page](../getting-started/installation#windows-native-powershell--early-beta) is all you need. Come back here when something surprises you.

:::tip Want WSL instead?
If you prefer a real POSIX environment (for the dashboard's embedded terminal, `fork` semantics, Linux-style file watchers, etc.), see the **[Windows (WSL2) Guide](./windows-wsl-quickstart.md)**. Both coexist cleanly: native data lives under `%LOCALAPPDATA%\quill`, WSL data lives under `~/.quill`.
:::

## Quick install

Open **PowerShell** (or Windows Terminal) and run:

```powershell
iex (irm https://raw.githubusercontent.com/YOUR_USERNAME/quill-agent/main/scripts/install.ps1)
```

No admin rights required. The installer goes to `%LOCALAPPDATA%\quill\` and adds `quill` to your **User PATH** — open a new terminal after it finishes.

**Installer options** (requires the scriptblock form to pass parameters):

```powershell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/YOUR_USERNAME/quill-agent/main/scripts/install.ps1))) -NoVenv -SkipSetup -Branch main
```

| Parameter | Default | Purpose |
|---|---|---|
| `-Branch` | `main` | Clone a specific branch (useful for testing PRs) |
| `-Commit` | unset | Pin install to a specific commit SHA (overrides `-Branch`) |
| `-Tag` | unset | Pin install to a specific git tag (e.g. `v0.14.0`) |
| `-NoVenv` | off | Skip venv creation (advanced — you manage Python yourself) |
| `-SkipSetup` | off | Skip the post-install `quill setup` wizard |
| `-QuillHome` | `%LOCALAPPDATA%\quill` | Override data directory |
| `-InstallDir` | `%LOCALAPPDATA%\quill\quill-agent` | Override code location |

The installer auto-retries flaky git fetches and strips BOM from any downloaded `install.ps1` payload, so a UTF-8 BOM picked up during HTTP transit no longer breaks the `[scriptblock]::Create((irm ...))` form.

### Desktop installer (alternative)

A thin GUI installer is also available — useful if you'd rather double-click an `.exe` than open PowerShell. Download Quill Desktop, run the installer, and on first launch the GUI calls `install.ps1` under the hood to provision Python (via `uv`), Node, PortableGit, and the rest of the dependency bootstrap described below. After the first run, the desktop app and the PowerShell-installed `quill` CLI share the same `%LOCALAPPDATA%\quill\quill-agent` install and `%USERPROFILE%\.quill` data directory — switch between the GUI and the CLI freely.

Use the desktop installer when you want a familiar Windows install experience or you're handing Quill to a non-developer; use the PowerShell one-liner when you're already in a terminal.

### Dependency bootstrap (`dep_ensure`)

On first launch (and on demand when a missing tool is detected), Quill runs a small Python bootstrapper — `quill_cli/dep_ensure.py` — that checks for and lazily installs the non-Python dependencies it needs. On Windows, the relevant ones are:

| Dependency | Why Quill needs it |
|---|---|
| **PortableGit** | Provides `bash.exe` for the terminal tool and `git` for in-session clones. Provisioned at install time, not by `dep_ensure`. |
| **Node.js 22** | Required for the browser tool (`agent-browser`), the TUI's web bridge, and the WhatsApp bridge. |
| **ffmpeg** | Audio format conversion for TTS / voice messages. |
| **ripgrep** | Fast file search — falls back to `grep` if unavailable. |
| **npm packages** | `agent-browser`, Playwright Chromium, and any per-toolset Node deps are installed once at first browser-tool use. |

Each dep has a `shutil.which(...)`-style check; if a binary is missing and the run is interactive, `dep_ensure` offers to install it (deferring to `scripts\install.ps1 -ensure <dep>` for the actual install logic). Non-interactive runs (gateway, cron, headless desktop launches) skip the prompt and surface a clear `this feature needs <dep>` error instead.

## What the installer actually does

Top-to-bottom, in order:

1. **Bootstraps `uv`** — Astral's fast Python manager. Installed to `%USERPROFILE%\.local\bin`.
2. **Installs Python 3.11** via `uv`. No existing Python needed.
3. **Installs Node.js 22** (winget if available, else a portable Node tarball unpacked under `%LOCALAPPDATA%\quill\node`). Used for the browser tool and the WhatsApp bridge.
4. **Installs portable Git** — if `git` is already on PATH the installer uses it; otherwise it downloads a trimmed, self-contained **PortableGit** (~45 MB, from the official `git-for-windows` release) to `%LOCALAPPDATA%\quill\git`. No admin, no Windows installer registry, no interference with anything else on the box.
5. **Clones the repo** to `%LOCALAPPDATA%\quill\quill-agent` and creates a virtualenv inside it.
6. **Tiered `uv pip install`** — tries `.[all]` first, falls back to progressively smaller sets (`[messaging,dashboard,ext]` → `[messaging]` → `.`) if a `git+https` dep flakes on rate-limited GitHub. Prevents "single flake drops you to a bare install" failure mode.
7. **Auto-installs messaging SDKs** keyed off `.env` — if `TELEGRAM_BOT_TOKEN` / `DISCORD_BOT_TOKEN` / `SLACK_BOT_TOKEN` / `SLACK_APP_TOKEN` / `WHATSAPP_ENABLED` are present, runs `python -m ensurepip --upgrade` and targeted `pip install` calls so each platform's SDK is actually importable.
8. **Sets `QUILL_GIT_BASH_PATH`** to the resolved `bash.exe` so Quill finds it deterministically in fresh shells.
9. **Adds `%LOCALAPPDATA%\quill\bin` to User PATH** — exposes the `quill` command after you open a new terminal.
10. **Runs `quill setup`** — the normal first-run wizard (model, provider, toolsets). Skip with `-SkipSetup`.

## Feature matrix

Everything except the dashboard's embedded terminal pane runs natively on Windows.

| Feature | Native Windows | WSL2 |
|---|---|---|
| CLI (`quill chat`, `quill setup`, `quill gateway`, …) | ✓ | ✓ |
| Interactive TUI (`quill --tui`) | ✓ | ✓ |
| Messaging gateway (Telegram, Discord, Slack, WhatsApp, 15+ platforms) | ✓ | ✓ |
| Cron scheduler | ✓ | ✓ |
| Browser tool (Chromium via Node) | ✓ | ✓ |
| MCP servers (stdio and HTTP) | ✓ | ✓ |
| Local Ollama / LM Studio / llama-server | ✓ | ✓ (via WSL networking) |
| Web dashboard (sessions, jobs, metrics, config) | ✓ | ✓ |
| Dashboard `/chat` embedded terminal pane | ✗ (needs POSIX PTY) | ✓ |
| Auto-start at login | ✓ (schtasks) | ✓ (systemd) |

The dashboard's `/chat` tab embeds a real terminal via a POSIX PTY (`ptyprocess`). Native Windows has no equivalent primitive; Python's `pywinpty` / Windows ConPTY would work but is a separate implementation — treat as future work. **The rest of the dashboard works natively** — only that one tab shows a "use WSL2 for this" banner.

## How Quill runs shell commands on Windows

Quill's terminal tool runs commands through **Git Bash**, same strategy Claude Code uses. This sidesteps the POSIX-vs-Windows gap without rewriting every tool.

Resolution order for `bash.exe`:

1. `QUILL_GIT_BASH_PATH` environment variable if set.
2. `%LOCALAPPDATA%\quill\git\usr\bin\bash.exe` (installer-managed PortableGit).
3. `%LOCALAPPDATA%\quill\git\bin\bash.exe` (older Git-for-Windows layout).
4. System Git-for-Windows install (`%ProgramFiles%\Git\bin\bash.exe`, etc.).
5. MSYS2, Cygwin, or any `bash.exe` on PATH as a last resort.

The installer sets `QUILL_GIT_BASH_PATH` explicitly so fresh PowerShell sessions don't have to re-discover. Override it if you want Quill to use a specific bash — for example, your system Git Bash or a WSL-hosted bash via a symlink.

**Pitfall:** MinGit's layout is different from the full Git-for-Windows installer — bash lives under `usr\bin\bash.exe`, not `bin\bash.exe`. Quill checks both. If you're manually unpacking a MinGit zip, make sure you pick the **non-busybox** variant (`MinGit-*-64-bit.zip`, not `MinGit-*-busybox*.zip`) — busybox builds ship `ash` instead of `bash` and most coreutils are missing.

## UTF-8 console on Windows

Python's default stdio on Windows uses the console's active code page (usually cp1252 or cp437). Quill's banner, slash-command list, tool feed, Rich panels, and skill descriptions all contain Unicode. Without intervention, any of that crashes with `UnicodeEncodeError: 'charmap' codec can't encode character…`.

The fix is in `quill_cli/stdio.py::configure_windows_stdio()`, called early in every entry point (`cli.py::main`, `quill_cli/main.py::main`, `gateway/run.py::main`). It:

1. Flips the console code page to CP_UTF8 (65001) via `kernel32.SetConsoleCP` / `SetConsoleOutputCP`.
2. Reconfigures `sys.stdout` / `sys.stderr` / `sys.stdin` to UTF-8 with `errors='replace'`.
3. Sets `PYTHONIOENCODING=utf-8` and `PYTHONUTF8=1` (via `setdefault`, so explicit user values win) so child Python subprocesses inherit UTF-8.
4. Sets `EDITOR=notepad` if neither `EDITOR` nor `VISUAL` is set (see the Editor section below).

Idempotent. No-op on non-Windows.

**Opt out:** `QUILL_DISABLE_WINDOWS_UTF8=1` in the environment falls back to the legacy cp1252 stdio path. Useful for bisecting an encoding bug; unlikely to be the right setting in normal operation.

## The editor (`Ctrl-X Ctrl-E`, `/edit`)

Pre-#21561, pressing `Ctrl-X Ctrl-E` or typing `/edit` silently did nothing on Windows. prompt_toolkit has a hardcoded POSIX-absolute fallback list (`/usr/bin/nano`, `/usr/bin/pico`, `/usr/bin/vi`, …) that never resolves on Windows — even with full Git for Windows installed.

Quill's Windows stdio shim now sets `EDITOR=notepad` as a default. Notepad ships with every Windows install and works as a blocking editor — `subprocess.call(["notepad", file])` blocks until the window closes.

**User overrides still win** (they're checked before the setdefault):

| Editor | PowerShell command |
|---|---|
| VS Code | `$env:EDITOR = "code --wait"` |
| Notepad++ | `$env:EDITOR = "'C:\Program Files\Notepad++\notepad++.exe' -multiInst -nosession"` |
| Neovim | `$env:EDITOR = "nvim"` |
| Helix | `$env:EDITOR = "hx"` |

The `--wait` flag on VS Code is critical — without it the editor returns immediately and Quill gets a blank buffer back.

Set it permanently in your PowerShell profile:

```powershell
# In $PROFILE
$env:EDITOR = "code --wait"
```

Or as a User environment variable in System Settings so every new shell picks it up.

## `Ctrl+Enter` for newline in the CLI

Windows Terminal passes `Ctrl+Enter` through as a dedicated key sequence. Quill binds it to "insert newline" so you can compose multi-line prompts in the CLI without falling back to `Esc`-then-`Enter`. Works in Windows Terminal, VS Code integrated terminal, and any modern Windows console host that honors VT escape sequences.

On legacy `cmd.exe` consoles `Ctrl+Enter` collapses to plain `Enter` — use `Esc Enter` instead, or upgrade to Windows Terminal (it's free and installed by default on Windows 11).

## Running the gateway at Windows login

`quill gateway install` on Windows uses **Scheduled Tasks** with a Startup-folder fallback — no admin required.

### Install

```powershell
quill gateway install
```

What happens under the hood:

1. `schtasks /Create /SC ONLOGON /RL LIMITED /TN QuillGateway` — registers a task that runs at your login with standard (non-elevated) permissions. No UAC prompt.
2. If schtasks is blocked by group policy, falls back to writing a `start /min cmd.exe /d /c <wrapper>` shortcut into `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`. Same effect, slightly cruder.
3. Spawns the gateway **detached via `pythonw.exe`** — not `python.exe`. `pythonw.exe` has no console attached, which immunizes it against `CTRL_C_EVENT` broadcasts from sibling processes (a real issue that used to kill the gateway when you Ctrl+C'd anything in the same process group).

Flags used when spawning: `DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP | CREATE_NO_WINDOW | CREATE_BREAKAWAY_FROM_JOB`.

### Manage

```powershell
quill gateway status      # Merged view: schtasks + Startup folder + running PID
quill gateway start       # Starts the scheduled task now
quill gateway stop        # Graceful SIGTERM equivalent (TerminateProcess via psutil)
quill gateway restart
quill gateway uninstall   # Removes schtasks entry, Startup shortcut, pid file
```

`quill gateway status` is idempotent — call it a thousand times in a row and it will never accidentally kill the gateway. (Pre-PR #21561 it silently did, via `os.kill(pid, 0)` colliding with `CTRL_C_EVENT` at the C level — see "process management internals" below if you care about the story.)

### Why not a Windows Service?

Services require admin rights to install and tie the gateway's lifecycle to machine boot, not user login. The typical Quill user wants: log in → gateway available, log out → gateway gone. Scheduled Tasks do exactly that without elevation. If you genuinely want a service, use `nssm` or `sc create` manually — but you probably don't.

## Data layout

| Path | Contents |
|---|---|
| `%LOCALAPPDATA%\quill\quill-agent\` | Git checkout + venv. Safe to `Remove-Item -Recurse` and reinstall. |
| `%LOCALAPPDATA%\quill\git\` | PortableGit (only if the installer provisioned it). |
| `%LOCALAPPDATA%\quill\node\` | Portable Node.js (only if the installer provisioned it). |
| `%LOCALAPPDATA%\quill\bin\` | `quill.cmd` shim, added to User PATH. |
| `%USERPROFILE%\.quill\` | Your config, auth, skills, sessions, logs. **Survives reinstalls.** |

The split is deliberate: `%LOCALAPPDATA%\quill` is disposable infrastructure (you can blow it away and the one-liner restores it). `%USERPROFILE%\.quill` is your data — config, memory, skills, session history — and is identical in shape to a Linux install. Mirror it between machines and your Quill moves with you.

**Override `QUILL_HOME`:** set the environment variable to point at a different data dir. Works the same as on Linux.

## Browser tool

The browser tool uses `agent-browser` (a Node helper) to drive Chromium. On Windows:

- The installer puts `agent-browser` on PATH via npm.
- `shutil.which("agent-browser", path=...)` picks up the `.cmd` shim automatically — `CreateProcessW` can't execute an extensionless shebang, so Quill always resolves to the `.CMD` wrapper. Don't manually invoke the shebang script; always go through the `.cmd`.
- Playwright Chromium is auto-installed on first run (`npx playwright install chromium`). If installation fails, `quill doctor` surfaces it with a fix-it hint.

## Running Quill on Windows — practical notes

### PATH after install

The installer adds `%LOCALAPPDATA%\quill\bin` to your **User PATH** via `[Environment]::SetEnvironmentVariable`. Existing terminals don't pick this up — open a new PowerShell window (or Windows Terminal tab) after installation. Close-and-reopen, don't `$env:PATH += …` by hand unless you know what you're doing.

Verify:

```powershell
Get-Command quill        # should print C:\Users\<you>\AppData\Local\quill\bin\quill.cmd
quill --version
```

### Environment variables

Quill honors both `$env:X` (process-scope) and User environment variables (permanent, set in System Properties → Environment Variables). Setting API keys in `%USERPROFILE%\.quill\.env` is the normal path — same as Linux:

```
OPENROUTER_API_KEY=sk-or-...
TELEGRAM_BOT_TOKEN=...
```

Don't put secrets in User environment variables unless you specifically want every Windows process to see them (it isn't what you want).

### Windows-specific env vars

These only affect native Windows installs:

| Variable | Effect |
|---|---|
| `QUILL_GIT_BASH_PATH` | Override bash.exe discovery. Point at any bash — full Git-for-Windows, WSL bash via symlink, MSYS2, Cygwin. The installer sets this automatically. |
| `QUILL_DISABLE_WINDOWS_UTF8` | Set to `1` to disable the UTF-8 stdio shim and fall back to the locale code page. Useful for bisecting an encoding bug. |
| `EDITOR` / `VISUAL` | Your editor for `/edit` and `Ctrl-X Ctrl-E`. Quill defaults to `notepad` if both are unset. |

## Uninstall

From PowerShell:

```powershell
quill uninstall
```

That's the clean path — removes the schtasks entry, Startup folder shortcut, `quill.cmd` shim, deletes `%LOCALAPPDATA%\quill\quill-agent\`, and trims the User PATH. It leaves `%USERPROFILE%\.quill\` alone (your config, auth, skills, sessions, logs) in case you're reinstalling.

To nuke everything:

```powershell
quill uninstall
Remove-Item -Recurse -Force "$env:USERPROFILE\.quill"
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\quill"
```

The `quill uninstall` CLI subcommand also handles the case where the schtasks entry was registered under a different task name (older installs) — it searches by install path rather than by hardcoded task name.

## Process management internals

This is background material — skip unless you're debugging an "it's killing itself" weirdness.

On Linux and macOS, the POSIX idiom `os.kill(pid, 0)` is a no-op permission check: "is this PID alive and can I signal it?" On Windows, Python's `os.kill` maps `sig=0` to `CTRL_C_EVENT` — they collide at integer value 0 — and routes it through `GenerateConsoleCtrlEvent(0, pid)`, which broadcasts Ctrl+C to the **entire console process group** containing the target PID. That's [bpo-14484](https://bugs.python.org/issue14484), open since 2012. It won't be fixed because changing it would break scripts that depend on the current behavior.

Consequence: any codepath that said "check if this PID is alive" via `os.kill(pid, 0)` on Windows was silently killing the target. Quill migrated every such site (14 across 11 files) to `gateway.status._pid_exists()`, which uses `psutil.pid_exists()` (which in turn uses `OpenProcess + GetExitCodeProcess` on Windows — no signals). If you're writing a plugin or patch, use `psutil.pid_exists()` directly or `gateway.status._pid_exists()` — never `os.kill(pid, 0)`.

`scripts/check-windows-footguns.py` enforces this in CI: any new `os.kill(pid, 0)` call fails the `Windows footguns (blocking)` check unless the line carries a `# windows-footgun: ok — <reason>` marker.

## Common pitfalls

**`quill: command not found` right after install.**
Open a new PowerShell window. The installer added `%LOCALAPPDATA%\quill\bin` to User PATH, but existing shells need to be restarted to pick it up. In the meantime you can run `& "$env:LOCALAPPDATA\quill\bin\quill.cmd"`.

**`WinError 193: %1 is not a valid Win32 application` when running a tool.**
You hit a shebang-script invocation that bypassed the `.cmd` shim. Quill resolves commands through `shutil.which(cmd, path=local_bin)` so PATHEXT picks up `.CMD` — if you're invoking the tool via a hardcoded path instead, switch to the `.cmd` variant (e.g., `npx.cmd`, not `npx`).

**`[scriptblock]::Create(...)` fails with `The assignment expression is not valid`.**
Your download of `install.ps1` picked up a UTF-8 BOM. The `irm | iex` form strips BOMs automatically; `[scriptblock]::Create((irm ...))` does not. Re-run with the simple `irm | iex` form, or download the script manually and save it without a BOM via `[IO.File]::WriteAllText($path, $text, (New-Object Text.UTF8Encoding $false))`.

**Gateway won't stay running after restart.**
Check `quill gateway status` — it merges the schtasks entry, the Startup-folder shortcut (if used), and the live PID. If schtasks is registered but not running, group policy may be blocking `ONLOGON` triggers. Run `schtasks /Query /TN QuillGateway /V /FO LIST` to see the task's failure reason, or fall back to the Startup-folder path by uninstalling and reinstalling with `QUILL_GATEWAY_FORCE_STARTUP=1`.

**`/edit` still does nothing after setting `$env:EDITOR`.**
You set it in the current process only; close and reopen the shell, or set it at User scope in System Properties → Environment Variables. Verify with `echo $env:EDITOR` in a new PowerShell window.

**Browser tool launches but tools time out.**
Chromium is auto-installed on first run. If the install failed (rate-limited GitHub, Playwright CDN hiccup), run `quill doctor` — it will surface the missing Chromium and print the exact `npx playwright install chromium` command to fix it.

**`agent-browser` fails with a weird Node version error.**
The installer provisions Node 22 at `%LOCALAPPDATA%\quill\node` but your PATH may have an older system Node 18 first. Either move Quill's node dir earlier on PATH, or delete the system install if you don't use Node elsewhere.

**Chinese / Japanese / Arabic characters show as `?` in the CLI.**
The UTF-8 stdio shim didn't activate. Check that `QUILL_DISABLE_WINDOWS_UTF8` is NOT set (`Get-ChildItem env:QUILL_DISABLE_WINDOWS_UTF8`). If it's empty and you still see `?`, the console host (very old `cmd.exe`) may not support UTF-8 at all — switch to Windows Terminal.

**Gateway can't send Telegram photos — "`BadRequest: payload contains invalid characters`".**
This is unrelated to Windows but sometimes surfaces first there. Usually it means your file path contains unescaped backslashes in a JSON body. Telegram should be receiving paths Quill normalizes, not raw Windows paths — if you're seeing this inside a custom plugin, make sure you're passing the Quill-provided path, not `str(Path(...))` from user input.

**"Works on my other machine" encoding weirdness after `git pull`.**
If you edited Quill config or a skill on Windows using a non-UTF-8 editor (Notepad on older Windows versions, some Chinese IMEs), the file may have been saved with a BOM. Quill tolerates `utf-8-sig` on most config reads, but a BOM inside a folded YAML scalar (`description: >`) silently breaks YAML parsing. Re-save the file as plain UTF-8 without BOM.

## Where to go next

- **[Installation](../getting-started/installation.md)** — the full install page, including Linux/macOS/WSL2/Termux.
- **[Windows (WSL2) Guide](./windows-wsl-quickstart.md)** — if you want POSIX semantics or the dashboard terminal pane.
- **[CLI Reference](../reference/cli-commands.md)** — every `quill` subcommand.
- **[FAQ](../reference/faq.md)** — common non-Windows-specific questions.
- **[Messaging Gateway](./messaging/index.md)** — running Telegram/Discord/Slack on Windows.
