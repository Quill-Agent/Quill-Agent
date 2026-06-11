"""Groq provider — fast cloud inference with a generous free tier."""

from providers import register_provider
from providers.base import ProviderProfile

groq = ProviderProfile(
    name="groq",
    aliases=(),
    display_name="Groq",
    description="Ultra-fast Llama, Mixtral, and Gemma models — free tier available",
    signup_url="https://console.groq.com/keys",
    env_vars=("GROQ_API_KEY", "GROQ_BASE_URL"),
    base_url="https://api.groq.com/openai/v1",
    default_aux_model="llama-3.3-70b-versatile",
    fallback_models=(
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
    ),
)

register_provider(groq)
