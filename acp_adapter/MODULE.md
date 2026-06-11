# acp_adapter

ACP server exposing Quill Agent to VS Code, Zed, and JetBrains.

- `server.py` — ACP handshake, model picker (`curated_models_for_provider`), streaming
- `session.py` — session fork/resume parity with gateway sessions
- `auth.py` — detects active provider (Groq, OpenRouter, Anthropic, etc.)
