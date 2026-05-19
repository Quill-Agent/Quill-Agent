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
| `custom` | `ollama`, `vllm`, `local` | Any OpenAI-compatible URL |

User overrides: `$QUILL_HOME/plugins/model-providers/<name>/`

---

## Security

- Never commit `.env` or API keys to Git.
- Rotate keys if they were exposed in chat or logs.
- Use `quill config set command_approval always` for safer shell access.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `Connection refused` on Ollama | Run `ollama serve` or start the Ollama app |
| `401` from cloud provider | Check key in `.env`, run `quill doctor` |
| Model not listed | `quill model` → refresh; verify base URL |
| Wrong provider selected | `quill config set provider groq` (or `ollama-local`) |

More: `quill doctor` and [README](../README.md#configuration).
