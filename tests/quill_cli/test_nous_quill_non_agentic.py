"""Tests for the Nous-Quill-3/4 non-agentic warning detector.

Prior to this check, the warning fired on any model whose name contained
``"quill"`` anywhere (case-insensitive). That false-positived on unrelated
local Modelfiles such as ``quill-brain:qwen3-14b-ctx16k`` — a tool-capable
Qwen3 wrapper that happens to live under the "quill" tag namespace.

``is_nous_quill_non_agentic`` should only match the actual Quill Agent
Quill-3 / Quill-4 chat family.
"""

from __future__ import annotations

import pytest

from quill_cli.model_switch import (
    _QUILL_MODEL_WARNING,
    _check_quill_model_warning,
    is_nous_quill_non_agentic,
)


@pytest.mark.parametrize(
    "model_name",
    [
        "YOUR_USERNAME/Quill-3-Llama-3.1-70B",
        "YOUR_USERNAME/Quill-3-Llama-3.1-405B",
        "quill-3",
        "Quill-3",
        "quill-4",
        "quill-4-405b",
        "quill_4_70b",
        "openrouter/quill3:70b",
        "openrouter/quill-agent/quill-4-405b",
        "YOUR_USERNAME/Quill3",
        "quill-3.1",
    ],
)
def test_matches_real_nous_quill_chat_models(model_name: str) -> None:
    assert is_nous_quill_non_agentic(model_name), (
        f"expected {model_name!r} to be flagged as Nous Quill 3/4"
    )
    assert _check_quill_model_warning(model_name) == _QUILL_MODEL_WARNING


@pytest.mark.parametrize(
    "model_name",
    [
        # Kyle's local Modelfile — qwen3:14b under a custom tag
        "quill-brain:qwen3-14b-ctx16k",
        "quill-brain:qwen3-14b-ctx32k",
        "quill-honcho:qwen3-8b-ctx8k",
        # Plain unrelated models
        "qwen3:14b",
        "qwen3-coder:30b",
        "qwen2.5:14b",
        "claude-opus-4-6",
        "anthropic/claude-sonnet-4.5",
        "gpt-5",
        "openai/gpt-4o",
        "google/gemini-2.5-flash",
        "deepseek-chat",
        # Non-chat Quill models we don't warn about
        "quill-llm-2",
        "quill2-pro",
        "nous-quill-2-mistral",
        # Edge cases
        "",
        "quill",  # bare "quill" isn't the 3/4 family
        "quill-brain",
        "brain-quill-3-impostor",  # "3" not preceded by /: boundary
    ],
)
def test_does_not_match_unrelated_models(model_name: str) -> None:
    assert not is_nous_quill_non_agentic(model_name), (
        f"expected {model_name!r} NOT to be flagged as Nous Quill 3/4"
    )
    assert _check_quill_model_warning(model_name) == ""


def test_none_like_inputs_are_safe() -> None:
    assert is_nous_quill_non_agentic("") is False
    # Defensive: the helper shouldn't crash on None-ish falsy input either.
    assert _check_quill_model_warning("") == ""
# quill: tests
