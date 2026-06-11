"""Tests for Quill-exclusive Claude Fable 5 efficiency prompt injection."""

from unittest.mock import MagicMock, patch

from agent.prompt_builder import QUILL_FABLE_EFFICIENCY_GUIDANCE
from agent.system_prompt import build_system_prompt_parts


def _make_agent(*, model: str, provider: str = "anthropic") -> MagicMock:
    agent = MagicMock()
    agent.model = model
    agent.provider = provider
    agent.valid_tool_names = set()
    agent._tool_use_enforcement = False
    agent.load_soul_identity = False
    agent.skip_context_files = True
    agent._kanban_worker_guidance = None
    agent.platform = None
    agent._memory_store = None
    agent._memory_enabled = False
    agent._user_profile_enabled = False
    agent._memory_manager = None
    return agent


@patch("agent.system_prompt._ra")
def test_fable_efficiency_guidance_in_system_prompt(mock_ra):
    mock_ra.return_value.load_soul_md.return_value = None
    mock_ra.return_value.build_environment_hints.return_value = ""
    mock_ra.return_value.build_nous_subscription_prompt.return_value = ""
    mock_ra.return_value.build_context_files_prompt.return_value = ""
    mock_ra.return_value.build_skills_system_prompt.return_value = ""

    parts = build_system_prompt_parts(_make_agent(model="claude-fable-5"))
    assert QUILL_FABLE_EFFICIENCY_GUIDANCE in parts["stable"]
    assert "Quill-Agent exclusive" in parts["stable"]


@patch("agent.system_prompt._ra")
def test_fable_efficiency_guidance_openrouter_id(mock_ra):
    mock_ra.return_value.load_soul_md.return_value = None
    mock_ra.return_value.build_environment_hints.return_value = ""
    mock_ra.return_value.build_nous_subscription_prompt.return_value = ""
    mock_ra.return_value.build_context_files_prompt.return_value = ""
    mock_ra.return_value.build_skills_system_prompt.return_value = ""

    parts = build_system_prompt_parts(
        _make_agent(model="anthropic/claude-fable-5", provider="openrouter")
    )
    assert QUILL_FABLE_EFFICIENCY_GUIDANCE in parts["stable"]


@patch("agent.system_prompt._ra")
def test_non_fable_model_omits_efficiency_layer(mock_ra):
    mock_ra.return_value.load_soul_md.return_value = None
    mock_ra.return_value.build_environment_hints.return_value = ""
    mock_ra.return_value.build_nous_subscription_prompt.return_value = ""
    mock_ra.return_value.build_context_files_prompt.return_value = ""
    mock_ra.return_value.build_skills_system_prompt.return_value = ""

    parts = build_system_prompt_parts(_make_agent(model="claude-sonnet-4-6"))
    assert QUILL_FABLE_EFFICIENCY_GUIDANCE not in parts["stable"]
