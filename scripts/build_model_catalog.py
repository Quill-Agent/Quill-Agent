#!/usr/bin/env python3
"""Build the Quill Model Catalog — a centralized JSON manifest of curated models.

Reads in-repo curated lists from ``quill_cli.models`` and writes a JSON manifest
the CLI can fetch at runtime. Publishing through the docs site lets maintainers
update model lists without shipping a Quill release.

The runtime fetcher falls back to the same in-repo hardcoded lists if the
manifest is unreachable, so this script keeps the manifest in sync — not a
source of truth.

Usage::

    python scripts/build_model_catalog.py

Output: ``website/static/api/model-catalog.json``

Live URL (after ``deploy-site.yml`` runs on merge to main):
``https://github.com/Quill-Agent/Quill-Agent/blob/main/website/static/api/model-catalog.json``
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

# Ensure QUILL_HOME is set for imports that touch it at module level.
os.environ.setdefault("QUILL_HOME", os.path.join(os.path.expanduser("~"), ".quill"))

from quill_cli.models import OPENROUTER_MODELS, _PROVIDER_MODELS  # noqa: E402

OUTPUT_PATH = os.path.join(REPO_ROOT, "website", "static", "api", "model-catalog.json")
CATALOG_VERSION = 2

# Extra providers exported as simple id lists (no per-model descriptions in-repo).
_STATIC_PROVIDER_BLOCKS: dict[str, dict] = {
    "groq": {
        "display_name": "Groq",
        "note": "Free tier — ultra-fast Llama, Mixtral, Gemma inference",
        "recommended": "llama-3.3-70b-versatile",
    },
    "huggingface": {
        "display_name": "Hugging Face",
        "note": "Inference API — open models",
        "recommended": "moonshotai/Kimi-K2.6",
    },
    "deepseek": {
        "display_name": "DeepSeek",
        "note": "V4 Pro (1M context) and Flash",
        "recommended": "deepseek-v4-pro",
    },
    "xai": {
        "display_name": "xAI",
        "note": "Grok Build 0.1 coding + Grok 4.x",
        "recommended": "grok-build-0.1",
    },
}


def _models_for_provider(provider: str) -> list[dict]:
    """Build model entries for a provider id list."""
    meta = _STATIC_PROVIDER_BLOCKS.get(provider, {})
    recommended = meta.get("recommended", "")
    entries: list[dict] = []
    for mid in _PROVIDER_MODELS.get(provider, []):
        desc = "recommended" if mid == recommended else ""
        entries.append({"id": mid, "description": desc})
    return entries


def build_catalog() -> dict:
    return {
        "version": CATALOG_VERSION,
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "metadata": {
            "source": "quill-agent repo",
            "docs": "https://github.com/Quill-Agent/Quill-Agent/blob/main/website/static/api/model-catalog.json",
        },
        "providers": {
            "openrouter": {
                "metadata": {
                    "display_name": "OpenRouter",
                    "note": (
                        "Descriptions drive picker badges. Live /api/v1/models "
                        "filters curated ids by tool-calling support and free pricing."
                    ),
                },
                "models": [
                    {"id": mid, "description": desc}
                    for mid, desc in OPENROUTER_MODELS
                ],
            },
            "nous": {
                "metadata": {
                    "display_name": "Nous Portal",
                    "note": (
                        "Free-tier gating is determined live via Portal pricing "
                        "(partition_nous_models_by_tier), not this manifest."
                    ),
                },
                "models": [
                    {"id": mid}
                    for mid in _PROVIDER_MODELS.get("nous", [])
                ],
            },
            **{
                provider: {
                    "metadata": {
                        "display_name": block["display_name"],
                        "note": block["note"],
                    },
                    "models": _models_for_provider(provider),
                }
                for provider, block in _STATIC_PROVIDER_BLOCKS.items()
            },
        },
    }


def main() -> int:
    catalog = build_catalog()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(catalog, fh, indent=2)
        fh.write("\n")

    print(f"Wrote {OUTPUT_PATH}")
    for provider, block in catalog["providers"].items():
        print(f"  {provider}: {len(block['models'])} models")
    return 0


if __name__ == "__main__":
    sys.exit(main())
