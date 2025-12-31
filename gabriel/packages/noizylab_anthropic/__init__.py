"""
NOIZYLAB Anthropic - Multi-model AI client for MC96ECOUNIVERSE

Quick Start:
    from noizylab_anthropic import claude, gabriel, lifeluv, analyze_data, review_code

    # Simple call
    response = claude("What's the status?")

    # With role
    response = claude("Analyze this", role="data_scientist")

    # Persona helpers
    response = gabriel("Status report")
    response = lifeluv("How are you?")

Async:
    from noizylab_anthropic import noizy_claude, NoizyAnthropic

    response = await noizy_claude("What's up?")

    client = NoizyAnthropic()
    async for chunk in client.stream("Tell me a story"):
        print(chunk, end="")
"""

from .claude_util import (
    claude,
    analyze_data,
    review_code,
    gabriel,
    lifeluv,
    shirl,
    pops,
    engr_keith,
    opus,
    sonnet,
    haiku,
    raw_call,
    git_help,
    client,
    get_client,
    get_model,
    ROLES,
    OPUS,
    SONNET,
    HAIKU,
    OPUS_FULL,
    SONNET_FULL,
    HAIKU_FULL,
    BEDROCK_OPUS,
    BEDROCK_SONNET,
    BEDROCK_HAIKU,
    VERTEX_OPUS,
    VERTEX_SONNET,
    VERTEX_HAIKU,
)

from .noizy_anthropic import (
    NoizyAnthropic,
    NoizyAnthropicSync,
    ClaudeResponse,
    noizy_claude,
    claude_sync,
    ROLE_PROMPTS,
    CLAUDE_OPUS,
    CLAUDE_SONNET,
    CLAUDE_HAIKU,
    DEFAULT_MODEL,
)

__version__ = "1.0.0"
__all__ = [
    # Sync (claude_util)
    "claude",
    "analyze_data",
    "review_code",
    "gabriel",
    "lifeluv",
    "shirl",
    "pops",
    "engr_keith",
    "opus",
    "sonnet",
    "haiku",
    "raw_call",
    "git_help",
    "client",
    "get_client",
    "get_model",
    "ROLES",
    # Async (noizy_anthropic)
    "NoizyAnthropic",
    "NoizyAnthropicSync",
    "ClaudeResponse",
    "noizy_claude",
    "claude_sync",
    "ROLE_PROMPTS",
    # Model constants
    "OPUS",
    "SONNET",
    "HAIKU",
    "OPUS_FULL",
    "SONNET_FULL",
    "HAIKU_FULL",
    "CLAUDE_OPUS",
    "CLAUDE_SONNET",
    "CLAUDE_HAIKU",
    "DEFAULT_MODEL",
    "BEDROCK_OPUS",
    "BEDROCK_SONNET",
    "BEDROCK_HAIKU",
    "VERTEX_OPUS",
    "VERTEX_SONNET",
    "VERTEX_HAIKU",
]
