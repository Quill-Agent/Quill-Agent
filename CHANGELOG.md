# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Claude Fable 5 (`claude-fable-5`, `anthropic/claude-fable-5`) — 1M-context Anthropic frontier model
- **Quill Fable Efficiency Layer** — exclusive system prompt for Fable models (~25% lower output-token consumption)
- Grok Build 0.1 (`grok-build-0.1`) — first-class xAI coding model via Responses API
- Groq catalog in `quill model` — Llama 3.3, Mixtral, Gemma, DeepSeek R1 distill
- Expanded Hugging Face and OpenRouter free-tier model lists
- Provider plugin manifests bumped to v1.0.1 with `fallback_models` on more profiles
- `scripts/build_model_catalog.py` exports Groq, Hugging Face, DeepSeek, and xAI blocks
- Cron jobs schema v2 — optional `model` / `provider` per scheduled run
- GitHub workflow `model-catalog.yml` for daily catalog rebuilds

### Performance

- Cache xAI and OpenAI Codex model catalog lookups per process (faster `quill model` picker)
- Cache gateway config until `config.yaml` / `gateway.json` changes on disk
- Provider registry: sorted `list_providers()` cached per process; httpx for catalog fetch

## [0.1.0] - 2026-05-19

### Added

- Initial terminal UI framework (`ui-tui/packages/quill-ink/`, derived from hermes-ink)
- Multi-agent collaboration Kanban board
- Delegation snapshot ledger
- `quillGatewayRouter`
- `agentsOverlay` component

### Attribution

- Terminal rendering primitives in `quill-ink` are derived from
  [hermes-agent](https://github.com/ljbudgie/hermes-agent) (hermes-ink package).
  See [NOTICE.md](NOTICE.md) for renamed files and upstream sources.

[0.1.0]: https://github.com/Quill-Agent/Quill-Agent/releases/tag/v0.1.0
