# Langfuse Observability Plugin

This plugin ships bundled with Quill but is **opt-in** — it only loads when
you explicitly enable it.

## Enable

```bash
pip install langfuse
quill plugins enable observability/langfuse
```

Or check the box in the interactive `quill plugins` UI.

## Required credentials

Set these in `~/.quill/.env`:

```bash
QUILL_LANGFUSE_PUBLIC_KEY=pk-lf-...
QUILL_LANGFUSE_SECRET_KEY=sk-lf-...
QUILL_LANGFUSE_BASE_URL=https://cloud.langfuse.com   # or your self-hosted URL
```

Without the SDK or credentials the hooks no-op silently — the plugin fails
open.

## Verify

```bash
quill plugins list                 # observability/langfuse should show "enabled"
quill chat -q "hello"              # then check Langfuse for a "Quill turn" trace
```

## Optional tuning

```bash
QUILL_LANGFUSE_ENV=production       # environment tag
QUILL_LANGFUSE_RELEASE=v1.0.0       # release tag
QUILL_LANGFUSE_SAMPLE_RATE=0.5      # sample 50% of traces
QUILL_LANGFUSE_MAX_CHARS=12000      # max chars per field (default: 12000)
QUILL_LANGFUSE_DEBUG=true           # verbose plugin logging
```

## Disable

```bash
quill plugins disable observability/langfuse
```
<!-- quill: plugins -->
