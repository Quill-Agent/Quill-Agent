"""ACP (Agent Client Protocol) adapter for Quill Agent.

Exposes Quill as an ACP backend for VS Code, Zed, and JetBrains. Model lists
are sourced from ``quill_cli.models.curated_models_for_provider`` (Groq, HF,
OpenRouter free tier, etc.) with the same fallbacks as the CLI picker.
"""
