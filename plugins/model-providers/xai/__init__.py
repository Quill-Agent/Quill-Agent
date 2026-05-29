"""xAI (Grok) provider profile."""

from providers import register_provider
from providers.base import ProviderProfile

xai = ProviderProfile(
    name="xai",
    aliases=("grok", "x-ai", "x.ai", "grok-build", "build"),
    api_mode="codex_responses",
    env_vars=("XAI_API_KEY",),
    display_name="xAI Grok",
    description="Grok models via xAI Responses API — including Grok Build 0.1 for agentic coding",
    signup_url="https://console.x.ai/",
    base_url="https://api.x.ai/v1",
    auth_type="api_key",
    fallback_models=(
        "grok-build-0.1",
        "grok-4.3",
        "grok-4.20-0309-reasoning",
        "grok-4.20-multi-agent-0309",
    ),
    default_aux_model="grok-build-0.1",
)

register_provider(xai)
# quill: plugins
