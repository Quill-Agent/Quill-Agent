"""Local Ollama provider — no API key, runs on your machine."""

from providers import register_provider
from providers.base import ProviderProfile

ollama_local = ProviderProfile(
    name="ollama-local",
    aliases=("ollama_local", "local-ollama"),
    display_name="Ollama (local)",
    description="Free local models via Ollama — no API key required",
    signup_url="https://ollama.com/download",
    env_vars=("OLLAMA_BASE_URL",),
    base_url="http://localhost:11434/v1",
    default_aux_model="llama3.2",
)

register_provider(ollama_local)
# quill: plugins
