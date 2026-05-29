# API access guide

Quill-Agent can run **without paid APIs** using local models, or connect to free-tier cloud providers in minutes.

## Quick start (recommended)

### Option A — Local Ollama (free, private)

```bash
# Install Ollama: https://ollama.com
ollama pull llama3.2

# Point Quill at your local server (default)
export OLLAMA_BASE_URL=http://localhost:11434/v1

quill setup
# Choose provider: ollama-local (or custom / ollama alias)
# Model: llama3.2
```

No API key required. Data stays on your machine.

### Option B — Groq (free tier, fast cloud)

1. Create a key at [console.groq.com](https://console.groq.com)
2. Add to `.env`:

```bash
GROQ_API_KEY=gsk_your_key_here
```

3. Run `quill model` and select **groq** — models include Llama 3.3 70B, Mixtral, Gemma.

### Option C — OpenRouter (many free models)

1. Sign up at [openrouter.ai](https://openrouter.ai)
2. Add to `.env`:

```bash
OPENROUTER_API_KEY=sk-or-v1-your_key_here
```

3. Use models tagged `:free` in the picker, e.g. `meta-llama/llama-3.3-70b-instruct:free`.

### Option D — DeepSeek V4 Pro (frontier coding, 1M context)

1. Create a key at [platform.deepseek.com](https://platform.deepseek.com/api_keys)
2. Add to `~/.quill/.env` or project `.env`:

```bash
DEEPSEEK_API_KEY=sk-...
```

3. Select provider **deepseek** and model **`deepseek-v4-pro`**:

```bash
quill setup
# or:
quill config set provider deepseek
quill config set model deepseek-v4-pro
quill model
```

**Models:** `deepseek-v4-pro` (frontier, 1M context), `deepseek-v4-flash` (fast default), `deepseek-chat` / `deepseek-reasoner` (legacy aliases, deprecated July 2026).

**Thinking mode:** Enabled by default on V4 models. Disable in config:

```yaml
reasoning:
  enabled: false
```

**Shortcuts:** `quill model deepseek-v4-pro`, `/model deepseek:deepseek-v4-pro`, or aliases `ds-pro` / `v4-pro`.

### Option E — xAI Grok Build 0.1 (fast agentic coding)

1. Create a key at [console.x.ai](https://console.x.ai/)
2. Add to `.env`:

```bash
XAI_API_KEY=xai-...
```

3. Select provider **xai** and model **`grok-build-0.1`**:

```bash
quill config set provider xai
quill config set model grok-build-0.1
```

**Notes:** 256K context, optimized for tool use and multi-step coding. Uses the xAI Responses API (`codex_responses` transport). Shortcuts: `grok-build`, `build`.

---

## Environment variables

Copy the template and uncomment what you need:

```bash
cp .env.example .env
```

| Provider | Key variable | Base URL (optional) |
|----------|--------------|---------------------|
| Ollama (local) | — | `OLLAMA_BASE_URL=http://localhost:11434/v1` |
| Ollama Cloud | `OLLAMA_API_KEY` | `OLLAMA_BASE_URL=https://ollama.com/v1` |
| Groq | `GROQ_API_KEY` | `GROQ_BASE_URL=https://api.groq.com/openai/v1` |
| OpenRouter | `OPENROUTER_API_KEY` | (built-in) |
| DeepSeek | `DEEPSEEK_API_KEY` | `DEEPSEEK_BASE_URL=https://api.deepseek.com/v1` |
| xAI Grok | `XAI_API_KEY` | `XAI_BASE_URL=https://api.x.ai/v1` |
| Hugging Face | `HF_TOKEN` | (built-in) |
| Custom / vLLM / LM Studio | `CUSTOM_API_BASE` | your endpoint `/v1` |

---

## CLI commands

```bash
quill setup              # wizard: provider, model, tools
quill model              # change provider/model
quill config set KEY VAL # set ~/.quill/config.yaml values
quill doctor             # diagnose missing keys / connectivity
```

---

## Provider plugins

Built-in profiles live under `plugins/model-providers/`. Each registers env vars and default URLs used by `quill model` and the agent runtime.

| Plugin | Alias | Notes |
|--------|-------|-------|
| `ollama-local` | `ollama-local` | Local Ollama at `localhost:11434` |
| `ollama-cloud` | `ollama_cloud` | Hosted Ollama models |
| `groq` | `groq` | Fast inference, free tier |
| `openrouter` | `or` | 200+ models, free tier available |
| `deepseek` | `ds-pro`, `v4-pro` | V4 Pro & Flash — 1M context, thinking mode |
| `custom` | `ollama`, `vllm`, `local` | Any OpenAI-compatible URL |

User overrides: `$QUILL_HOME/plugins/model-providers/<name>/`

---

## Security & privacy

- Never commit `.env` or API keys to Git — keep secrets in `~/.quill/.env` only.
- **Log redaction is on by default** — API keys, Bearer/Basic auth, `x-api-key` headers, and JWTs are masked in `agent.log`, `errors.log`, and verbose output. Disable only for debugging: `security.redact_secrets: false` in `config.yaml`.
- **Local-first** — Ollama and self-hosted endpoints keep prompts on your machine; cloud keys are loaded from env and never echoed in chat.
- Rotate keys if they were exposed; run `quill doctor` to verify redaction and provider config.
- Use `quill config set command_approval always` for safer shell access.

---

## Performance tips

- **Local models** — Ollama/LM Studio avoid network latency; best for privacy and steady throughput.
- **Cloud free tier** — Groq and OpenRouter `:free` models trade a small network hop for faster GPUs on weak hardware.
- **Context** — Use `/compress` in long sessions to reduce tokens and speed up replies.
- **Gateway** — Run `quill gateway` once; it reuses agents across messages instead of cold-starting each time.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `Connection refused` on Ollama | Run `ollama serve` or start the Ollama app |
| `401` from cloud provider | Check key in `.env`, run `quill doctor` |
| Model not listed | `quill model` → refresh; verify base URL |
| Wrong provider selected | `quill config set provider groq` (or `ollama-local`) |

More: `quill doctor` and [README](../README.md#configuration).
<!-- quill: docs -->
