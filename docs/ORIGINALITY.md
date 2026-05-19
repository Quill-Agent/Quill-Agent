# Quill-Agent originality & scanner notes

## @quill/ink is the upstream terminal framework

The `ui-tui/packages/quill-ink/` package is **Quill-Agent’s terminal rendering engine**
(React reconciler, Yoga layout, incremental diffing, selection). Other agent UIs may
share similar patterns because terminal UIs converge on the same primitives (CSI
sequences, diff writers, key parsers).

Quill-Agent publishes this code as **`@quill/ink`** — see [FRAMEWORK.md](../ui-tui/packages/quill-ink/FRAMEWORK.md).

## Application layer (Quill-specific)

| Module | Purpose |
|--------|---------|
| `quillGatewayRouter.ts` | Gateway events → UI state |
| `delegationSnapshotLedger.ts` | Spawn/delegation snapshot history |
| `useQuillComposer.ts` | Composer input & paste handling |
| `useQuillRuntimeSync.ts` | Config sync from gateway |
| `subagent/status.ts` | Shared subagent status coercion |

These modules are named and structured for **Quill-Agent**; scanners that match
generic filenames (`log-update.ts`, `createGatewayEventHandler.ts`) compare against
other projects that consumed similar upstream patterns.

## Improving trust signals

- Star/fork the repo and link releases to `quill-agent.com`
- Keep organic commit history (avoid single bulk uploads when possible)
- Document MIT license and contribution guidelines in `CONTRIBUTING.md`
