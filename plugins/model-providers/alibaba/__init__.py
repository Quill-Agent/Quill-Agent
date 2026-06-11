"""Alibaba Cloud DashScope provider profile."""

from providers import register_provider
from providers.base import ProviderProfile

alibaba = ProviderProfile(
    name="alibaba",
    aliases=("dashscope", "alibaba-cloud", "qwen-dashscope"),
    display_name="Alibaba Qwen",
    description="Qwen and DashScope models — international endpoint",
    signup_url="https://dashscope.console.aliyun.com/",
    env_vars=("DASHSCOPE_API_KEY",),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
    default_aux_model="qwen-plus",
    fallback_models=(
        "qwen3.6-plus",
        "qwen-plus",
        "qwen-turbo",
    ),
)

register_provider(alibaba)
