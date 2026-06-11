# cron

Scheduled automations for the gateway and CLI.

- `jobs.py` — CRUD for `~/.quill/cron/jobs.json` (schema v2: optional `model` / `provider` per job)
- `scheduler.py` — `tick()` executor; gateway calls on a background interval
- `tools/cronjob_tools.py` — agent-facing cron management tool
