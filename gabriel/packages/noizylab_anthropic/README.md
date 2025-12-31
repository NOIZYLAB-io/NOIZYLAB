# NOIZYLAB Anthropic

Multi-model Anthropic client for MC96ECOUNIVERSE.

## Features

- **Multi-Platform**: Anthropic Direct, AWS Bedrock, Google Vertex AI
- **Role-Based Prompts**: GABRIEL, LIFELUV, SHIRL, POPS, ENGR_KEITH + professional roles
- **Async & Sync**: Both patterns supported
- **Streaming**: Real-time token streaming
- **Model Shortcuts**: opus(), sonnet(), haiku()

## Installation

```bash
pip install anthropic httpx

# For AWS Bedrock
pip install boto3

# For Google Vertex
pip install google-cloud-aiplatform
```

## Quick Start

```python
from noizylab_anthropic import claude, gabriel, lifeluv

# Simple call
response = claude("What's the status?")
print(response)

# With role
response = claude("Analyze this data", role="data_scientist")

# Persona helpers
print(gabriel("Status report"))
print(lifeluv("How are you feeling today?"))
```

## Async Usage

```python
from noizylab_anthropic import noizy_claude, NoizyAnthropic
import asyncio

async def main():
    # Simple async call
    response = await noizy_claude("What's up?")
    print(response)
    
    # Streaming
    client = NoizyAnthropic()
    async for chunk in client.stream("Tell me a story"):
        print(chunk, end="", flush=True)

asyncio.run(main())
```

## Models

| Shorthand | Full Name | Platform |
|-----------|-----------|----------|
| `opus` | claude-opus-4-5-20250929 | Anthropic |
| `sonnet` | claude-sonnet-4-5-20250929 | Anthropic |
| `haiku` | claude-haiku-4-5-20250929 | Anthropic |

## Roles

- `noizylab` - NOIZYLAB assistant (default)
- `gabriel` - Warrior AI guardian
- `lifeluv` - Compassionate companion
- `shirl` - Rob's virtual aunt
- `pops` - Rob's virtual dad figure
- `engr_keith` - Engineer persona
- `data_scientist` - Data analysis
- `code_reviewer` - Code review
- `composer` - Music composition

## CLI

```bash
# Simple
python -m noizylab_anthropic "What's the status?"

# With role
python -m noizylab_anthropic -r gabriel "Status report"

# With model
python -m noizylab_anthropic -m opus "Complex analysis"

# Streaming
python -m noizylab_anthropic --stream "Tell me a story"
```

## Environment Variables

```bash
export ANTHROPIC_API_KEY="sk-ant-..."

# For platform selection
export CLAUDE_PLATFORM="anthropic"  # or "bedrock" or "vertex"
```

## License

MIT - NOIZYLAB 2025
