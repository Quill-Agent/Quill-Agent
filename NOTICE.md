# NOTICE

This file documents third-party components incorporated into Quill-Agent and
identifies which parts of the project are original work.

## Third-party components

### hermes-agent (hermes-ink)

The terminal rendering engine in `ui-tui/packages/quill-ink/` is derived from
the **hermes-agent** project, specifically the **hermes-ink** package. The
directory layout `ui-tui/packages/quill-ink/src/ink/` mirrors the upstream
`hermes-ink/src/ink/` structure.

Representative upstream sources:

- https://github.com/ljbudgie/hermes-agent
- Related public forks (e.g. gary-the-ai/hermes-web-console-gui)

**Renamed files** (Quill-Agent name → original hermes-ink name):

| Quill-Agent file | Original file |
|------------------|---------------|
| `quill-border.ts` | `render-border.ts` |
| `quill-keypress.ts` | `parse-keypress.ts` |
| `quill-screen-render.ts` | `render-to-screen.ts` |
| `quill-terminal-diff.ts` | `log-update.ts` |

Additional files under `ui-tui/packages/quill-ink/src/ink/` may share the same
upstream lineage; see attribution headers in individual source files where
present.

hermes-agent / hermes-ink is used under its respective open-source license.
See the upstream repository for the authoritative license text.

### claude-code (community forks)

Portions of the terminal diff and rendering utilities in
`ui-tui/packages/quill-ink/` are also derived from community forks and
collections of **claude-code** source, including:

- https://github.com/chauncygu/collection-claude-code-source-code
- Related forks in the claude-code ecosystem

These portions are used under their respective open-source licenses. See
upstream repositories for authoritative license terms.

---

## Original Quill-Agent components

The following parts of Quill-Agent are **original work** (not derived from
hermes-agent or claude-code):

- Multi-agent delegation system
- `agentsOverlay` UI
- Kanban board multi-agent collaboration feature
- `quillGatewayRouter`
- `delegationSnapshotLedger`
- Application-layer orchestration (e.g. turn controller, gateway integration)

---

## Project license

Quill-Agent as a whole is distributed under the MIT License. See [LICENSE](LICENSE).

For questions about attribution or licensing, open an issue in the project
repository.
