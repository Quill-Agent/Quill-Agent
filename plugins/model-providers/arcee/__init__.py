"""Arcee AI provider profile."""

from providers import register_provider
from providers.base import ProviderProfile

arcee = ProviderProfile(
    name="arcee",
    aliases=("arcee-ai", "arceeai"),
    env_vars=("ARCEEAI_API_KEY",),
    base_url="https://api.arcee.ai/api/v1",
    fallback_models=(
        "arcee-spark",
        "arcee-nova",
    ),
)

register_provider(arcee)
