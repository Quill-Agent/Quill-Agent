# Quill-Agent — Full Project Recreation Prompt

Use this prompt with any capable AI coding assistant (Claude, GPT-4, Gemini, etc.) or autonomous coding agent to recreate, fork, and rebrand the Quill-Agent project from scratch.

---

## PROMPT

You are an expert full-stack AI engineer. Your task is to create a complete, production-ready, open-source AI agent project called **Quill-Agent**. This is a fork and complete rebrand of the open-source project at https://github.com/YOUR_USERNAME/quill-agent — rebuilt with a new identity, a new name, and configured to run exclusively on free and open-source AI models.

Follow every instruction below with extreme precision. Do not skip any step. Do not leave any placeholder text unfilled. The output must be a real, runnable project.

---

## PART 1: PROJECT IDENTITY & BRANDING

### Name & Identity
- Project name: **Quill-Agent** (stylized as `quill-agent` in code, `Quill` in conversation)
- CLI command: `quill` (replaces `quill`)
- Tagline: *"The self-improving AI agent that writes its own future"*
- Logo concept: A feather quill pen with a subtle circuit-board pattern — representing the fusion of writing, intelligence, and technology
- Color scheme: Deep navy (#0D1B2A) + warm amber (#F4A261) + clean white (#FFFFFF)
- GitHub repo: `YOUR_USERNAME/quill-agent`

### What Must Be Renamed
Perform a **complete, exhaustive find-and-replace** across all files in the project (Python, TypeScript, Shell, YAML, TOML, JSON, Markdown, Dockerfile, etc.) for every occurrence of the following terms. Replace with the Quill equivalents listed:

| Find | Replace With |
|---|---|
| `quill` (lowercase) | `quill` |
| `Quill` (capitalized) | `Quill` |
| `QUILL` (uppercase) | `QUILL` |
| `quill-agent` | `quill-agent` |
| `quill_agent` | `quill_agent` |
| `quill_cli` | `quill_cli` |
| `quill_bootstrap` | `quill_bootstrap` |
| `quill_constants` | `quill_constants` |
| `quill_logging` | `quill_logging` |
| `quill_state` | `quill_state` |
| `quill_time` | `quill_time` |
| `setup-quill.sh` | `setup-quill.sh` |
| `YOUR_USERNAME` | `YOUR_USERNAME` |
| `Quill Agent` | *(remove or replace with your own org name)* |
| `quill-agent.example.com` | *(your own docs URL or remove)* |
| `example.com` | *(your own website or remove)* |
| `✒️` (caduceus symbol) | `✒️` (quill pen emoji) |
| Any reference to "Nous Portal" | "Open Models Hub" |
| Discord invite link for YOUR_USERNAME | *(your own Discord or remove)* |

**Important:** Also rename these files and directories on disk:
- `quill_cli/` → `quill_cli/`
- `quill_bootstrap.py` → `quill_bootstrap.py`
- `quill_constants.py` → `quill_constants.py`
- `quill_logging.py` → `quill_logging.py`
- `quill_state.py` → `quill_state.py`
- `quill_time.py` → `quill_time.py`
- `setup-quill.sh` → `setup-quill.sh`
- `quill` (the CLI launcher shell script) → `quill`
- `quill-already-has-routines.md` → `quill-already-has-routines.md`
- `quill_constants.py` → `quill_constants.py`

After renaming, update all `import` statements, `from X import Y` lines, and any string references that still mention the old filenames.

---

## PART 2: MODEL PROVIDER CONFIGURATION

The original project supports many providers. For Quill-Agent, the **primary focus** is on free and open-source AI models. Reconfigure the providers list as follows:

### Priority Providers (configure as defaults and document prominently)

1. **Ollama** (local, free, recommended default)
   - Default model: `llama3.2` or `qwen2.5:7b`
   - Connection: `http://localhost:11434`
   - No API key required
   - Setup instructions: `ollama pull llama3.2`

2. **LM Studio** (local, free)
   - Default model: any GGUF loaded in LM Studio
   - Connection: `http://localhost:1234/v1` (OpenAI-compatible)
   - No API key required

3. **OpenRouter** (free tier available, 50+ free models)
   - Free models include: `meta-llama/llama-3.3-70b-instruct:free`, `mistralai/mistral-7b-instruct:free`, `qwen/qwen-2.5-72b-instruct:free`, `deepseek/deepseek-r1:free`
   - API key from: https://openrouter.ai (free signup)
   - Env var: `OPENROUTER_API_KEY`

4. **Hugging Face Inference API** (free tier)
   - Supports hundreds of open-source models
   - API token from: https://huggingface.co (free signup)
   - Env var: `HF_TOKEN`

5. **Groq** (free tier, ultra-fast)
   - Free models: Llama 3.3 70B, Mixtral 8x7B, Gemma 2 9B
   - API key from: https://console.groq.com (free signup)
   - Env var: `GROQ_API_KEY`

6. **Together AI** (free credits)
   - Models: Llama 3, Mistral, Qwen, DeepSeek
   - API key from: https://together.ai
   - Env var: `TOGETHER_API_KEY`

7. **Novita AI** (free credits, open-source GPU cloud)
   - API key from: https://novita.ai
   - Env var: `NOVITA_API_KEY`

8. **Custom OpenAI-compatible endpoint** (any self-hosted server: vLLM, llama.cpp, text-generation-webui, koboldcpp, etc.)
   - Env var: `CUSTOM_API_BASE`, `CUSTOM_API_KEY` (optional), `CUSTOM_MODEL_NAME`

### Provider File Changes
In the `providers/` directory:
- Keep all existing provider adapter files but rename any `quill`-specific references
- Add a new file `providers/ollama.py` if it doesn't exist, implementing full Ollama support with streaming
- Add a new file `providers/lm_studio.py` if it doesn't exist, using the OpenAI-compatible endpoint
- Add a new file `providers/groq.py` if it doesn't exist
- Add a new file `providers/together.py` if it doesn't exist
- In `providers/__init__.py`, add all new providers to the registry

### Default Config
In `quill_constants.py` (renamed from `quill_constants.py`), set:
```python
DEFAULT_PROVIDER = "ollama"
DEFAULT_MODEL = "llama3.2"
DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"
QUILL_VERSION = "1.0.0"
QUILL_DIR = os.path.expanduser("~/.quill")
```

---

## PART 3: COMPLETE FILE STRUCTURE

The project must have this exact directory structure (based on the source repo, fully renamed):

```
quill-agent/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
├── .plans/
├── acp_adapter/
├── acp_registry/
├── agent/
│   ├── __init__.py
│   ├── loop.py           # Main agent loop
│   ├── context.py        # Context management
│   ├── planner.py        # Task planning
│   └── memory.py         # Memory integration
├── assets/
│   └── banner.png        # Quill-Agent banner (create or placeholder)
├── cron/
│   ├── __init__.py
│   └── scheduler.py
├── datagen-config-examples/
├── docker/
├── docs/
├── gateway/
│   ├── __init__.py
│   ├── telegram.py
│   ├── discord.py
│   ├── slack.py
│   ├── whatsapp.py
│   └── signal.py
├── quill_cli/             # renamed from quill_cli
│   ├── __init__.py
│   └── commands.py
├── locales/
├── nix/
├── optional-skills/
├── packaging/
│   └── homebrew/
├── plans/
├── plugins/
├── providers/
│   ├── __init__.py
│   ├── ollama.py         # NEW - primary provider
│   ├── lm_studio.py      # NEW
│   ├── openrouter.py
│   ├── huggingface.py
│   ├── groq.py           # NEW
│   ├── together.py       # NEW
│   ├── novita.py
│   ├── openai_compat.py  # Generic OpenAI-compatible
│   └── base.py           # Abstract base class
├── scripts/
│   ├── install.sh
│   ├── install.ps1
│   └── run_tests.sh
├── skills/
├── tests/
├── tools/
│   ├── __init__.py
│   ├── filesystem.py
│   ├── shell.py
│   ├── browser.py
│   ├── code.py
│   ├── memory_tools.py
│   ├── media.py
│   └── subagent.py
├── tui_gateway/
├── ui-tui/
├── web/
├── website/
├── .dockerignore
├── .env.example
├── .envrc
├── .gitattributes
├── .gitignore
├── AGENTS.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── MANIFEST.in
├── README.md             # The full README from Part 5 below
├── SECURITY.md
├── batch_runner.py
├── cli-config.yaml.example
├── cli.py
├── constraints-termux.txt
├── docker-compose.yml
├── flake.lock
├── flake.nix
├── mcp_serve.py
├── mini_swe_runner.py
├── model_tools.py
├── package.json
├── pyproject.toml
├── quill                 # CLI launcher (renamed from quill)
├── quill-already-has-routines.md
├── quill_bootstrap.py    # renamed
├── quill_constants.py    # renamed
├── quill_logging.py      # renamed
├── quill_state.py        # renamed
├── quill_time.py         # renamed
├── run_agent.py
├── setup-quill.sh        # renamed
├── toolset_distributions.py
├── toolsets.py
├── trajectory_compressor.py
├── utils.py
└── uv.lock
```

---

## PART 4: KEY FILE CONTENTS

### `pyproject.toml`
Update the project metadata:
```toml
[project]
name = "quill-agent"
version = "1.0.0"
description = "The self-improving AI agent that writes its own future"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.11"
keywords = ["ai", "agent", "llm", "open-source", "ollama", "automation"]

[project.scripts]
quill = "quill_cli:main"

[project.urls]
Homepage = "https://github.com/YOUR_USERNAME/quill-agent"
Repository = "https://github.com/YOUR_USERNAME/quill-agent"
Issues = "https://github.com/YOUR_USERNAME/quill-agent/issues"
```

### `.env.example`
```env
# =============================================
# Quill-Agent Environment Configuration
# =============================================

# --- LOCAL MODELS (no API key needed) ---
# Ollama (recommended - completely free)
OLLAMA_BASE_URL=http://localhost:11434
QUILL_DEFAULT_PROVIDER=ollama
QUILL_DEFAULT_MODEL=llama3.2

# LM Studio (OpenAI-compatible local server)
# QUILL_DEFAULT_PROVIDER=lm_studio
# LM_STUDIO_BASE_URL=http://localhost:1234/v1

# --- FREE CLOUD PROVIDERS (free tier) ---

# OpenRouter (50+ free models available)
# Get key at: https://openrouter.ai
OPENROUTER_API_KEY=

# Hugging Face (hundreds of open models)
# Get token at: https://huggingface.co/settings/tokens
HF_TOKEN=

# Groq (ultra-fast inference, generous free tier)
# Get key at: https://console.groq.com
GROQ_API_KEY=

# Together AI (free credits on signup)
# Get key at: https://together.ai
TOGETHER_API_KEY=

# Novita AI (free credits, GPU cloud)
# Get key at: https://novita.ai
NOVITA_API_KEY=

# --- CUSTOM ENDPOINT (self-hosted vLLM, llama.cpp, etc.) ---
# QUILL_DEFAULT_PROVIDER=custom
# CUSTOM_API_BASE=http://localhost:8000/v1
# CUSTOM_API_KEY=
# CUSTOM_MODEL_NAME=my-model

# --- MESSAGING GATEWAY ---
TELEGRAM_BOT_TOKEN=
DISCORD_BOT_TOKEN=
SLACK_BOT_TOKEN=
SLACK_APP_TOKEN=

# --- OPTIONAL FEATURES ---
# ElevenLabs TTS
ELEVENLABS_API_KEY=

# Honcho user modeling
HONCHO_API_KEY=
```

### `setup-quill.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🪶 Setting up Quill-Agent..."

# Install uv if not present
if ! command -v uv &>/dev/null; then
  echo "Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.cargo/bin:$PATH"
fi

# Create virtualenv and install
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all]"

# Create symlink
mkdir -p "$HOME/.local/bin"
ln -sf "$(pwd)/quill" "$HOME/.local/bin/quill"

echo ""
echo "✅ Quill-Agent installed successfully!"
echo ""
echo "Run: quill setup   — to configure your model and API keys"
echo "Run: quill         — to start chatting"
```

### `quill_constants.py` (core constants file)
```python
"""
Quill-Agent Constants
"""
import os

# Version
QUILL_VERSION = "1.0.0"

# Directories
QUILL_DIR = os.path.expanduser("~/.quill")
QUILL_SKILLS_DIR = os.path.join(QUILL_DIR, "skills")
QUILL_MEMORY_DIR = os.path.join(QUILL_DIR, "memory")
QUILL_SESSIONS_DIR = os.path.join(QUILL_DIR, "sessions")
QUILL_LOGS_DIR = os.path.join(QUILL_DIR, "logs")
QUILL_CONFIG_FILE = os.path.join(QUILL_DIR, "config.yaml")

# Default model config
DEFAULT_PROVIDER = "ollama"
DEFAULT_MODEL = "llama3.2"
DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_MAX_TOKENS = 4096
DEFAULT_CONTEXT_WINDOW = 32768

# Memory files
MEMORY_FILE = os.path.join(QUILL_MEMORY_DIR, "MEMORY.md")
USER_MODEL_FILE = os.path.join(QUILL_MEMORY_DIR, "USER.md")
SOUL_FILE = os.path.join(QUILL_DIR, "SOUL.md")
AGENTS_FILE = os.path.join(QUILL_DIR, "AGENTS.md")

# Agent identity
AGENT_NAME = "Quill"
AGENT_EMOJI = "✒️"
AGENT_TAGLINE = "The self-improving AI agent that writes its own future"

# CLI
CLI_HISTORY_FILE = os.path.join(QUILL_DIR, ".cli_history")
CLI_MAX_HISTORY = 1000

# Cron
CRON_FILE = os.path.join(QUILL_DIR, "cron.yaml")

# MCP
MCP_SERVER_FILE = os.path.join(QUILL_DIR, "mcp_servers.yaml")
```

### `cli.py`
```python
#!/usr/bin/env python3
"""
Quill-Agent CLI entry point.
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from quill_cli import main

if __name__ == "__main__":
    main()
```

### `scripts/install.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

QUILL_DIR="$HOME/.quill"
INSTALL_DIR="$HOME/.local/share/quill-agent"
BIN_DIR="$HOME/.local/bin"

echo ""
echo "  ✒️  Quill-Agent Installer"
echo "  ─────────────────────────"
echo ""

# Check OS
OS="$(uname -s)"
ARCH="$(uname -m)"

# Install system dependencies
install_deps() {
  if command -v apt-get &>/dev/null; then
    sudo apt-get update -qq && sudo apt-get install -y -qq curl git ripgrep ffmpeg
  elif command -v brew &>/dev/null; then
    brew install ripgrep ffmpeg
  fi
}

# Install uv
if ! command -v uv &>/dev/null; then
  echo "→ Installing uv (Python package manager)..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"
fi

# Install Node.js if missing
if ! command -v node &>/dev/null; then
  echo "→ Installing Node.js..."
  curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
  sudo apt-get install -y nodejs
fi

# Clone or update repo
if [ -d "$INSTALL_DIR" ]; then
  echo "→ Updating Quill-Agent..."
  cd "$INSTALL_DIR" && git pull
else
  echo "→ Installing Quill-Agent..."
  git clone https://github.com/YOUR_USERNAME/quill-agent.git "$INSTALL_DIR"
  cd "$INSTALL_DIR"
fi

# Set up Python environment
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all]"

# Create CLI launcher
mkdir -p "$BIN_DIR"
cat > "$BIN_DIR/quill" << 'EOF'
#!/usr/bin/env bash
source "$HOME/.local/share/quill-agent/.venv/bin/activate"
python "$HOME/.local/share/quill-agent/cli.py" "$@"
EOF
chmod +x "$BIN_DIR/quill"

# Create quill dir
mkdir -p "$QUILL_DIR"

echo ""
echo "  ✅ Quill-Agent installed successfully!"
echo ""
echo "  Next steps:"
echo "  1. Reload your shell:  source ~/.bashrc (or ~/.zshrc)"
echo "  2. Set up Quill:       quill setup"
echo "  3. Start chatting:     quill"
echo ""
echo "  💡 Tip: For a completely free setup, install Ollama first:"
echo "     curl -fsSL https://ollama.com/install.sh | sh"
echo "     ollama pull llama3.2"
echo ""
```

---

## PART 5: README.md

Write a complete, polished README.md for the project. It must include:

1. A centered header with the project name `Quill-Agent ✒️`, tagline, and 4 badge shields: License (MIT), Python version, Open Source Models, and Platform support
2. A note crediting the original source: "Based on the architecture of [YOUR_USERNAME/quill-agent](https://github.com/YOUR_USERNAME/quill-agent), rebuilt and rebranded as Quill-Agent"
3. A feature table (same structure as original but rebranded)
4. A full table of supported free/open-source AI providers with links and cost notes
5. Quick install section with Linux/macOS/WSL2 and Windows PowerShell one-liners
6. Getting started section with all CLI commands
7. CLI vs Messaging quick reference table
8. Skills system explanation
9. Memory & user modeling section
10. Cron scheduling examples
11. Full tools & integrations list
12. Architecture tree
13. Configuration section with sample YAML
14. Docker instructions
15. Contributing section
16. Security section
17. License section
18. Acknowledgements crediting YOUR_USERNAME/quill-agent

---

## PART 6: ADDITIONAL FILES TO CREATE

### `CONTRIBUTING.md`
Write a complete contributing guide covering:
- Development setup using `setup-quill.sh`
- Code style (Python: black + ruff, TypeScript: prettier + eslint)
- How to add a new tool (with template)
- How to add a new provider (with template)
- How to create a skill
- PR process and review standards
- Running the test suite
- Issue reporting guidelines

### `SECURITY.md`
Write a security policy covering:
- Supported versions
- Reporting vulnerabilities
- Command approval system documentation
- Data privacy (all data stored locally by default)
- API key storage best practices

### `AGENTS.md`
Write an AGENTS.md instruction file for Quill itself, explaining:
- Its name is Quill
- It should refer to itself as Quill
- Its personality: thoughtful, precise, helpful, like a brilliant writing partner
- How to use its skills and memory systems
- How to handle tool use responsibly

### `cli-config.yaml.example`
```yaml
# Quill-Agent Configuration
# Copy to ~/.quill/config.yaml and customize

# Model settings
provider: ollama
model: llama3.2
ollama_base_url: http://localhost:11434
max_tokens: 4096
temperature: 0.7

# Memory
memory_enabled: true
user_modeling: true
session_search: true

# Skills
skills_enabled: true
auto_create_skills: true
skills_hub: true

# Shell
shell_backend: local  # local | docker | ssh | modal
command_approval: auto  # always | auto | yolo

# TUI
theme: dark
multiline: true
streaming: true

# Cron
cron_enabled: true

# Gateway
gateway_port: 8765
```

---

## PART 7: PROVIDER IMPLEMENTATIONS

### `providers/ollama.py`
Implement a complete Ollama provider class with:
- Streaming chat completions using Ollama's `/api/chat` endpoint
- Model listing from `/api/tags`
- Proper error handling and connection testing
- Support for `system` messages
- Tool/function calling support (for models that support it)
- Multimodal support for vision models

```python
"""
Quill-Agent Ollama Provider

Connects to a local Ollama instance for completely free,
offline-capable AI inference.

Setup:
    curl -fsSL https://ollama.com/install.sh | sh
    ollama pull llama3.2
"""

import json
import httpx
from typing import Iterator, AsyncIterator
from .base import BaseProvider, Message, CompletionResponse

class OllamaProvider(BaseProvider):
    name = "ollama"
    display_name = "Ollama (Local)"
    requires_api_key = False
    supports_streaming = True
    supports_tools = True

    FREE_MODELS = [
        "llama3.2",
        "llama3.2:1b",
        "llama3.1:8b",
        "llama3.1:70b",
        "qwen2.5:7b",
        "qwen2.5:14b",
        "mistral",
        "mistral-nemo",
        "phi4",
        "phi3.5",
        "gemma2",
        "gemma2:2b",
        "deepseek-r1:7b",
        "deepseek-r1:14b",
        "codellama",
        "codegemma",
        "nomic-embed-text",
    ]

    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.2", **kwargs):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.client = httpx.Client(timeout=120)

    def complete(self, messages: list[Message], **kwargs) -> CompletionResponse:
        # ... implementation
        pass

    def stream(self, messages: list[Message], **kwargs) -> Iterator[str]:
        # ... implementation
        pass

    def list_models(self) -> list[str]:
        # ... implementation
        pass

    def test_connection(self) -> bool:
        # ... implementation
        pass
```

### `providers/openrouter.py`
Implement OpenRouter provider with:
- Automatic detection and preferencing of `:free` model variants
- A `list_free_models()` method that returns only the zero-cost models
- Proper `HTTP-Referer` and `X-Title` headers as required by OpenRouter
- Rate limit handling

### `providers/base.py`
Define the abstract base class all providers must implement:
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator

@dataclass
class Message:
    role: str  # "system" | "user" | "assistant" | "tool"
    content: str | list
    tool_call_id: str | None = None
    tool_calls: list | None = None

@dataclass
class CompletionResponse:
    content: str
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    tool_calls: list | None = None

class BaseProvider(ABC):
    name: str
    display_name: str
    requires_api_key: bool = True
    supports_streaming: bool = True
    supports_tools: bool = False
    supports_vision: bool = False

    @abstractmethod
    def complete(self, messages: list[Message], **kwargs) -> CompletionResponse: ...

    @abstractmethod
    def stream(self, messages: list[Message], **kwargs) -> Iterator[str]: ...

    def list_models(self) -> list[str]:
        return []

    def test_connection(self) -> bool:
        try:
            self.list_models()
            return True
        except Exception:
            return False
```

---

## PART 8: GITHUB ACTIONS CI

### `.github/workflows/ci.yml`
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Set up Python ${{ matrix.python-version }}
        run: uv venv .venv --python ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          source .venv/bin/activate
          uv pip install -e ".[dev]"

      - name: Run tests
        run: |
          source .venv/bin/activate
          ./scripts/run_tests.sh

      - name: Lint
        run: |
          source .venv/bin/activate
          ruff check .
          black --check .
```

---

## PART 9: DOCKER

### `Dockerfile`
```dockerfile
FROM python:3.11-slim

LABEL maintainer="YOUR_USERNAME"
LABEL description="Quill-Agent - The self-improving AI agent"
LABEL version="1.0.0"

# System dependencies
RUN apt-get update && apt-get install -y \
    curl git ripgrep ffmpeg nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY pyproject.toml ./
COPY . .
RUN uv venv .venv --python 3.11 && \
    . .venv/bin/activate && \
    uv pip install -e ".[all]"

# Create quill directory
RUN mkdir -p /root/.quill

# Entry point
ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT ["python", "cli.py"]
```

### `docker-compose.yml`
```yaml
version: "3.8"

services:
  quill:
    build: .
    image: quill-agent:latest
    container_name: quill-agent
    stdin_open: true
    tty: true
    volumes:
      - quill-data:/root/.quill
      - ./workspace:/workspace
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY:-}
      - GROQ_API_KEY=${GROQ_API_KEY:-}
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN:-}
    depends_on:
      - ollama

  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    volumes:
      - ollama-data:/root/.ollama
    ports:
      - "11434:11434"

volumes:
  quill-data:
  ollama-data:
```

---

## PART 10: FINAL CHECKLIST

Before considering the project complete, verify every item on this list:

- [ ] Zero occurrences of `quill`, `Quill`, or `QUILL` anywhere in the codebase (run: `grep -r -i "quill" . --include="*.py" --include="*.md" --include="*.yaml" --include="*.toml" --include="*.json" --include="*.sh"`)
- [ ] Zero occurrences of `YOUR_USERNAME` or `nousresearch` in any user-facing text
- [ ] All Python files use `quill_*` naming for the renamed modules
- [ ] All imports updated to use new module names
- [ ] `pyproject.toml` has correct project name `quill-agent`
- [ ] CLI command is `quill` (not `quill`)
- [ ] Default provider is `ollama`
- [ ] README.md is complete with all sections
- [ ] `.env.example` is complete with all provider keys documented
- [ ] `setup-quill.sh` is executable and works on Linux/macOS
- [ ] `scripts/install.sh` works end-to-end
- [ ] Docker setup works (`docker-compose up`)
- [ ] All tests pass (`./scripts/run_tests.sh`)
- [ ] GitHub Actions CI passes
- [ ] No broken imports (run: `python -c "import quill_constants; import quill_state"`)
- [ ] `quill --help` runs without errors
- [ ] AGENTS.md refers to agent as "Quill" throughout
- [ ] CONTRIBUTING.md references `quill-agent` and `setup-quill.sh`
- [ ] SECURITY.md is complete
- [ ] LICENSE is MIT and contains correct year
- [ ] README acknowledges YOUR_USERNAME/quill-agent as the original source

---

## SOURCE REFERENCE

The original project this is based on:
**https://github.com/YOUR_USERNAME/quill-agent**

Key technical facts about the source project:
- Language: Python 88.2%, TypeScript 8.7%, Shell 0.6%
- Architecture: modular agent loop with pluggable providers, tools, skills, and gateways
- Memory: FTS5 SQLite full-text search + markdown files
- Skills: markdown-based procedural memory with auto-creation
- Gateway: unified messaging bridge for Telegram, Discord, Slack, WhatsApp, Signal
- Shell backends: local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox
- Scheduling: built-in cron with platform delivery
- MCP: full Model Context Protocol support

Study the source repository carefully before implementing. The goal is a clean, fully functional fork that is identical in capability but completely rebranded as Quill-Agent and configured to prioritize free, open-source AI models.

---

*End of Quill-Agent Recreation Prompt*
