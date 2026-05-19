<div align="center">

<img src="assets/banner.png" alt="Quill-Agent banner" width="100%" />

<br /><br />

# Quill-Agent ✒️

### *The self-improving AI agent that writes its own future*

[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Open Source Models](https://img.shields.io/badge/Models-100%25%20Open%20Source-orange?style=for-the-badge)](https://openrouter.ai)
[![Platform](https://img.shields.io/badge/Runs%20Anywhere-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Android-purple?style=for-the-badge)](#installation)

**Quill-Agent** is a fully open-source, self-improving AI agent that runs on 100% free and open-source AI models. It learns from every conversation, builds skills over time, runs scheduled automations, delegates tasks to subagents, and lives wherever you do — terminal, Telegram, Discord, Slack, and more.

> Fully open-source AI agent — local models, free-tier APIs, and self-hosted endpoints. See **[API access guide](docs/API_ACCESS.md)** for setup.

</div>

---

## ✨ What Makes Quill Different

| Feature | Description |
|---|---|
| **Closed Learning Loop** | Quill creates skills from experience, improves them during use, nudges itself to persist knowledge, and searches its own past conversations. It grows smarter with every session. |
| **100% Open-Source Models** | Works with Ollama, LM Studio, OpenRouter (200+ free/open models), Hugging Face Inference, and any OpenAI-compatible endpoint. No paid API required. |
| **Lives Where You Do** | Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription included. |
| **Runs Anywhere** | Local, Docker, SSH, Modal, or a $5 VPS. The agent hibernates when idle; wake it from your phone. |
| **Scheduled Automations** | Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly summaries — all in natural language. |
| **Delegates and Parallelizes** | Spawn isolated subagents for parallel workstreams. Collapse multi-step pipelines into zero-context-cost turns. |
| **MCP Integration** | Connect any Model Context Protocol server for extended tools and capabilities. |
| **Research-Ready** | Batch trajectory generation and trajectory compression for training next-generation tool-calling models. |

---

## 🆓 Supported Open-Source & Free AI Models

Quill-Agent is designed to work **entirely for free** using open-source and freely available models:

| Provider | Models | Cost |
|---|---|---|
| [Ollama](https://ollama.com) | Llama 3, Mistral, Qwen, Phi, Gemma, DeepSeek, and 100+ more | Free (local) |
| [LM Studio](https://lmstudio.ai) | Any GGUF model from Hugging Face | Free (local) |
| [OpenRouter](https://openrouter.ai) | Llama 3.3 70B, Mistral 7B, Qwen 2.5, DeepSeek R1, and 50+ free-tier models | Free tier available |
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

Quill supports **local Ollama** (no key), **Groq**, **OpenRouter**, **Hugging Face**, and any OpenAI-compatible endpoint.

```bash
cp .env.example .env    # add keys for cloud providers (optional)
quill setup             # interactive provider + model picker
quill model             # switch provider anytime
```

Full reference: **[docs/API_ACCESS.md](docs/API_ACCESS.md)**

---

## 🔧 Configuration

Quill is configured via `~/.quill/config.yaml`. Key settings:

```yaml
# Model provider
provider: ollama          # ollama | openrouter | huggingface | groq | together | custom
model: llama3.2           # Any model supported by your provider

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

## 📄 License

MIT — see [LICENSE](LICENSE). Free to use, fork, and modify.

---

## 🙏 Acknowledgements

Quill-Agent is a fork and rebrand of the open-source [Quill-Agent/quill-agent](https://github.com/Quill-Agent/quill-agent) project. Full credit to the Quill Agent team and all contributors for building the foundation this project is built on.

---

<div align="center">

**Built for everyone. Powered by open models. Owned by you.**

[Issues](https://github.com/Quill-Agent/quill-agent/issues) · [Discussions](https://github.com/Quill-Agent/quill-agent/discussions) · [agentskills.io](https://agentskills.io)

</div>
