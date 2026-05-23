# Third-Party Notices

## hermes-agent (NousResearch)

Quill-Agent is derived from hermes-agent by Nous Research.
Source: https://github.com/NousResearch/hermes-agent
License: MIT

The following files in this repository are derived from hermes-agent
with identifier and filename renames from "hermes" to "quill":

Python files:
  hermes_constants.py     → quill_constants.py
  hermes_state.py         → quill_state.py
  hermes_logging.py       → quill_logging.py
  hermes_time.py          → quill_time.py
  hermes_bootstrap.py     → quill_bootstrap.py

Directories:
  hermes_cli/             → quill_cli/
  ui-tui/packages/hermes-ink/ → ui-tui/packages/quill-ink/

TypeScript files (ui-tui/packages/quill-ink/src/ink/):
  render-border.ts        → quill-border.ts
  parse-keypress.ts       → quill-keypress.ts
  render-to-screen.ts     → quill-screen-render.ts
  log-update.ts           → quill-terminal-diff.ts
  useComposerState.ts     → useQuillComposer.ts (in ui-tui/src/app/)

Original additions in Quill-Agent not present in hermes-agent:
  - Multi-agent Kanban board collaboration system
  - Delegation snapshot ledger (delegationSnapshotLedger)
  - agentsOverlay React component
  - quillGatewayRouter
