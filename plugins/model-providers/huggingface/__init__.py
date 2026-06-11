"""Hugging Face provider profile."""

from providers import register_provider
from providers.base import ProviderProfile

huggingface = ProviderProfile(
    name="huggingface",
    aliases=("hf", "hugging-face", "huggingface-hub"),
    env_vars=("HF_TOKEN",),
    display_name="HuggingFace",
    description="HuggingFace Inference API",
    signup_url="https://huggingface.co/settings/tokens",
    fallback_models=(
        "Qwen/Qwen3.5-72B-Instruct",
        "Qwen/Qwen3.5-35B-A3B",
        "deepseek-ai/DeepSeek-V3.2",
        "moonshotai/Kimi-K2.6",
        "MiniMaxAI/MiniMax-M2.5",
    ),
    default_aux_model="Qwen/Qwen3.5-35B-A3B",
    base_url="https://router.huggingface.co/v1",
)

register_provider(huggingface)
