<div align="center">

<img src="assets/banner.png" alt="Quill-Agent — manga-style portrait banner" width="100%" />

<br /><br />

# Quill-Agent

### *Faster. Better. Free. The AI agent that outperforms hermes-agent at zero API cost.*

<br />

[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Open Source Models](https://img.shields.io/badge/Models-100%25%20Open%20Source-orange?style=for-the-badge)](https://openrouter.ai)
[![Platform](https://img.shields.io/badge/Runs%20Anywhere-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Android-purple?style=for-the-badge)](#installation)

**Quill-Agent** is a fully open-source AI agent built on the hermes-agent foundation — with a faster agent loop, smarter context compression, multi-agent Kanban coordination, and full support for 100% free and open-source models. No paid API required. No lock-in. Runs entirely local or on free-tier cloud.

> Built on hermes-agent by Nous Research · Extended with multi-agent Kanban, delegation tracking, and performance upgrades · 100% free models · MIT License

### What's new

- **More free open-source models** — Expanded OpenRouter, Hugging Face, and Groq coverage; easier switching with `quill model` and clearer free-tier defaults in setup.
- **Cloud use upgrade** — Smoother cloud provider setup (OpenRouter, Groq, Together, HF), improved env/key handling, and better remote shell backends (SSH, Modal, Docker).
- **Performance upgrade** — Faster agent loop, leaner context handling, and snappier TUI/gateway responses under load.
- **Multi-agent Kanban** — Coordinate parallel agents on a shared board: assign tasks by profile, auto-decompose triage, and track collaboration in the live dashboard.
- **DeepSeek V4 Pro** — First-class `deepseek-v4-pro` support (1M context, thinking mode, native API + OpenRouter).
- **Grok Build 0.1** — xAI’s fast agentic coding model (`grok-build-0.1`, 256K context, Responses API).

</div>

---

## ⚡ Why Quill over hermes-agent?

Quill-Agent started as a fork of hermes-agent and has grown into a faster, leaner, and more capable alternative:

| | Quill-Agent | hermes-agent |
|---|---|---|
| **API cost** | $0 — works 100% on free/local models | Requires paid API for full features |
| **Multi-agent coordination** | ✅ Built-in Kanban board + delegation ledger | ❌ Not available |
| **Agent loop speed** | Faster — optimized context handling | Baseline |
| **Context compression** | ✅ Smarter leaner compression | Basic |
| **DeepSeek V4 Pro** | ✅ First-class (1M context, thinking mode) | ❌ Not available |
| **Grok Build 0.1** | ✅ Agentic coding model (256K, 100+ tok/s) | ❌ Not available |
| **Privacy** | ✅ Fully local option, no data sent out | Depends on provider |
| **Live delegation UI** | ✅ agentsOverlay — real-time tree view | ❌ Not available |

---

## ✨ What Makes Quill Different

| Feature | Description |
|---|---|
| **Closed Learning Loop** | Quill creates skills from experience, improves them during use, nudges itself to persist knowledge, and searches its own past conversations. It grows smarter with every session. |
| **100% Open-Source Models** | Works with Ollama, LM Studio, OpenRouter (250+ free/open models), Hugging Face Inference, Groq, Together, and any OpenAI-compatible endpoint. No paid API required. |
| **Cloud-ready** | First-class cloud providers with guided setup, key rotation via `.env`, and remote execution on SSH, Modal, or Docker. |
| **Performance** | Faster turns, smarter context compression, and lower latency on gateway and TUI sessions. |
| **Lives Where You Do** | Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription included. |
| **Runs Anywhere** | Local, Docker, SSH, Modal, or a $5 VPS. The agent hibernates when idle; wake it from your phone. |
| **Scheduled Automations** | Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly summaries — all in natural language. |
| **Delegates and Parallelizes** | Spawn isolated subagents for parallel workstreams. Collapse multi-step pipelines into zero-context-cost turns. |
| **Multi-agent Kanban** | Shared SQLite board coordinates multiple Quill profiles: triage → decompose → parallel workers, parent/child task links, live dashboard, and gateway dispatch. Use `quill kanban create` or `/kanban` in chat. |
| **MCP Integration** | Connect any Model Context Protocol server for extended tools and capabilities. |
| **Research-Ready** | Batch trajectory generation and trajectory compression for training next-generation tool-calling models. |

---

## 🆓 Supported Open-Source & Free AI Models

Quill-Agent is designed to work **entirely for free** using open-source and freely available models:

| Provider | Models | Cost |
|---|---|---|
| [Ollama](https://ollama.com) | Llama 3, Mistral, Qwen, Phi, Gemma, DeepSeek, and 100+ more | Free (local) |
| [LM Studio](https://lmstudio.ai) | Any GGUF model from Hugging Face | Free (local) |
| [OpenRouter](https://openrouter.ai) | Llama 3.3 70B, Mistral 7B, Qwen 2.5/3, DeepSeek V4 Pro/Flash, Gemma 3, and 80+ free-tier models | Free tier available |
| [DeepSeek](https://platform.deepseek.com) | **V4 Pro** (1M context), V4 Flash, legacy V3/R1 — direct API | Pay-per-use |
| [xAI Grok](https://x.ai/api) | **Grok Build 0.1** (coding), Grok 4.3 — direct API | Pay-per-use |
| [Hugging Face](https://huggingface.co) | Serverless Inference API (hundreds of open models) | Free tier available |
| [Groq](https://groq.com) | Llama 3, Mixtral, Gemma (ultra-fast inference) | Free tier available |
| [Together AI](https://together.ai) | Llama, Mistral, Qwen | Free credits |
| [Novita AI](https://novita.ai) | Open-source model API + GPU cloud | Free credits |
| Any OpenAI-compatible endpoint | Self-hosted vLLM, llama.cpp server, text-generation-webui | Free (self-hosted) |

Switch models anytime with `quill model` — no code changes, no lock-in.

---

## 🚀 Quick Install

### Linux, macOS, WSL2, Termux

```bash
curl -fsSL https://raw.githubusercontent.com/Quill-Agent/quill-agent/main/scripts/install.sh | bash
```

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/Quill-Agent/quill-agent/main/scripts/install.ps1 | iex
```

The installer handles everything: Python 3.11, Node.js, uv, ripgrep, ffmpeg, and Git. No admin required.

After installation:

```bash
source ~/.bashrc    # reload shell (or: source ~/.zshrc)
quill               # start chatting!
```

---

## 🛠️ Getting Started

```bash
quill               # Interactive CLI — start a conversation
quill model         # Choose your LLM provider and model
quill tools         # Configure which tools are enabled
quill config set    # Set individual config values
quill gateway       # Start the messaging gateway (Telegram, Discord, etc.)
quill setup         # Run the full setup wizard
quill update        # Update to the latest version
quill doctor        # Diagnose any issues
```

### First-Time Setup (2 minutes)

```bash
# 1. Install Quill
curl -fsSL https://raw.githubusercontent.com/Quill-Agent/quill-agent/main/scripts/install.sh | bash

# 2. Run the setup wizard
quill setup

# 3. Pick a free model (e.g. Ollama with Llama 3)
quill model
# → Select: ollama / llama3.2

# 4. Start chatting
quill
```

---

## 🖥️ CLI vs Messaging Quick Reference

Quill has two entry points: the terminal UI (`quill`), or the gateway for Telegram, Discord, Slack, WhatsApp, and Signal.

| Action | CLI | Messaging |
|---|---|---|
| Start chatting | `quill` | `quill gateway start` → message the bot |
| New conversation | `/new` or `/reset` | `/new` or `/reset` |
| Change model | `/model [provider:model]` | `/model [provider:model]` |
| Set a personality | `/personality [name]` | `/personality [name]` |
| Retry last turn | `/retry` | `/retry` |
| Compress context | `/compress` | `/compress` |
| Browse skills | `/skills` | `/skills` |
| Interrupt current work | `Ctrl+C` | `/stop` |

---

## 🧠 The Skills System

Quill learns by doing. After completing complex tasks, it automatically creates **skills** — reusable procedural memories written as markdown files.

- Skills are stored in `~/.quill/skills/`
- They self-improve as Quill uses them and finds better approaches
- You can browse, share, and install community skills
- Skills are compatible with the [agentskills.io](https://agentskills.io) open standard

```bash
# Browse your skills
quill skills

# Use a skill manually
/skill-name

# List all skills
ls ~/.quill/skills/
```

---

## 💾 Memory & User Modeling

Quill builds a persistent model of who you are across sessions:

- **MEMORY.md** — key facts Quill remembers about you
- **USER.md** — your preferences, working style, and goals
- **FTS5 session search** — full-text search across all past conversations with LLM summarization
- **Periodic nudges** — Quill autonomously prompts itself to save important knowledge

---

## 📅 Cron Scheduling

Schedule any task in natural language:

```bash
# Inside a Quill conversation:
"Every morning at 8am, check my project files and send me a summary to Telegram"
"Every Sunday, generate a weekly review of what I worked on"
"At 11pm daily, backup my notes folder and confirm via Discord"
```

Manage schedules:

```bash
quill cron list
quill cron delete [id]
```

---

## 🔌 Tools & Integrations

Quill ships with 40+ built-in tools:

- **File system** — read, write, search, edit files
- **Shell** — run bash commands in configurable backends (local, Docker, SSH, Modal)
- **Browser** — web search, page fetching, screenshot
- **Code** — Python execution, linting, formatting
- **Media** — image analysis, voice transcription
- **Memory** — read/write persistent memory
- **Subagents** — spawn parallel agent instances
- **MCP** — connect any Model Context Protocol server

Configure which tools are active:

```bash
quill tools
```

---

## 🏗️ Architecture

```
quill-agent/
├── agent/              # Core agent loop and reasoning engine
├── providers/          # LLM provider adapters (Ollama, OpenRouter, HuggingFace, etc.)
├── tools/              # 40+ built-in tools
├── skills/             # User and system skills (procedural memory)
├── gateway/            # Messaging platform gateway
├── tui_gateway/        # Terminal UI backend
├── web/                # Web interface
├── cron/               # Scheduled task engine
├── plugins/            # Plugin system
├── quill_cli/          # CLI entry point (renamed from quill_cli)
├── quill_constants.py  # Global constants
├── quill_state.py      # Session state management
├── quill_logging.py    # Logging system
├── quill_time.py       # Time utilities
├── mcp_serve.py        # MCP server
├── cli.py              # CLI launcher
└── run_agent.py        # Agent runner
```

---

## 🔑 API access

Quill supports **local Ollama** (no key), **Groq**, **OpenRouter**, **DeepSeek V4 Pro**, **Hugging Face**, **Together**, and any OpenAI-compatible endpoint. Cloud setup is one command: copy env template, run `quill setup`, pick a model — keys stay in `~/.quill` or `.env`, never in chat logs.

```bash
cp .env.example .env    # add keys for cloud providers (optional)
quill setup             # interactive provider + model picker (free-tier models highlighted)
quill model             # switch provider anytime — no restart required
```

Full reference: **[docs/API_ACCESS.md](docs/API_ACCESS.md)**

---

## 🔧 Configuration

Quill is configured via `~/.quill/config.yaml`. Key settings:

```yaml
# Model provider
provider: ollama          # ollama | deepseek | openrouter | huggingface | groq | together | custom
model: llama3.2           # e.g. deepseek-v4-pro, llama3.2, meta-llama/llama-3.3-70b-instruct:free

# Provider API keys (leave blank for local models)
openrouter_api_key: ""
huggingface_token: ""
groq_api_key: ""

# Shell backend
shell_backend: local      # local | docker | ssh | modal

# Memory
memory_enabled: true
user_modeling: true

# Skills
skills_enabled: true
auto_create_skills: true
```

Set any value from the CLI:

```bash
quill config set provider ollama
quill config set model llama3.2
```

---

## 🐳 Docker

```bash
# Build
docker build -t quill-agent .

# Run
docker run -it \
  -v ~/.quill:/root/.quill \
  -e OPENROUTER_API_KEY=your_key \
  quill-agent
```

Or with docker-compose:

```bash
docker-compose up
```

---

## 🤝 Contributing

Contributions are welcome! To get started:

```bash
# Clone and set up dev environment
git clone https://github.com/Quill-Agent/quill-agent.git
cd quill-agent
./setup-quill.sh

# Run tests
./scripts/run_tests.sh

# Start hacking
./quill
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a PR. Key guidelines:

- Follow existing code style (Python: black + ruff, TypeScript: prettier)
- Add tests for new tools and providers
- Update docs for any user-facing changes
- Keep provider adapters modular and independent

---

## 🔒 Security

Quill prompts for approval before running shell commands by default. Configure the approval policy:

```bash
quill config set command_approval always    # always ask
quill config set command_approval auto      # auto-approve safe commands
quill config set command_approval yolo      # never ask (not recommended)
```

See [SECURITY.md](SECURITY.md) for responsible disclosure policy.

---

## 🙏 Acknowledgements

Quill-Agent is built on top of [hermes-agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com), an open-source self-improving AI agent framework released under the MIT License.

The terminal rendering engine (quill-ink), core agent loop, provider adapters, gateway system, skills architecture, cron scheduler, and CLI tooling originate from hermes-agent, with identifiers and filenames renamed from "hermes" to "quill".

The following features are original additions in Quill-Agent, not present in hermes-agent:
- Multi-agent Kanban board (`quill kanban` / `/kanban`)
- Delegation snapshot ledger (full history of every subagent delegation)
- agentsOverlay live UI (real-time delegation tree with cost, tokens, duration)
- quillGatewayRouter (custom gateway dispatch layer)
- DeepSeek V4 Pro support (1M context, thinking mode)
- Grok Build 0.1 support (xAI agentic coding model)
- Performance and privacy improvements over the upstream baseline

Full credit to the Nous Research team and all hermes-agent contributors. Quill-Agent is an independent project and is not affiliated with Nous Research.

---

## 📄 License

MIT — see [LICENSE](LICENSE). Free to use, fork, and modify. Third-party attributions: [NOTICE.md](NOTICE.md).

---

<div align="center">

**Built for everyone. Powered by open models. Owned by you.**

[Issues](https://github.com/Quill-Agent/quill-agent/issues) · [Discussions](https://github.com/Quill-Agent/quill-agent/discussions) · [agentskills.io](https://agentskills.io)

</div>
<!-- quill: root -->
