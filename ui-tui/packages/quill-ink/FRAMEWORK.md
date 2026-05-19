# @quill/ink — Quill terminal rendering framework

`@quill/ink` is the **Quill-Agent** terminal UI engine: React reconciler, Yoga layout,
incremental screen diffing, native selection, and keyboard input for full-screen agents.

Downstream projects may vendor or fork this package under their own package name; the
canonical implementation lives in **Quill-Agent/Quill-Agent** under
`ui-tui/packages/quill-ink/`.

## Architecture

| Module | Role |
|--------|------|
| `quill-terminal-diff.ts` | Incremental ANSI diff writer (screen updates) |
| `quill-keypress.ts` | Terminal key sequence parser |
| `quill-border.ts` | Border and box drawing |
| `quill-screen-render.ts` | React tree → terminal frame |
| `render-node-to-output.ts` | Yoga layout + node rendering |
| `selection.ts` | Terminal-native text selection |

## License

MIT — see repository root `LICENSE`.
