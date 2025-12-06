# NLR_01 - NOIZYLAB Voice Assistant

Voice-powered AI assistant with Speech-to-Text input, Talon integration, and flexible LLM backends.

## Features

- **Speech-to-Text**: Local Whisper for accurate transcription
- **Talon Integration**: Works with existing voice command setup
- **Multi-LLM Support**: Claude, OpenAI, Ollama (local models)
- **Accessibility First**: Designed for voice-only operation

## Architecture

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────┐
│   Microphone    │────▶│  Whisper STT │────▶│ LLM Router  │
└─────────────────┘     └──────────────┘     └─────────────┘
                                                    │
                              ┌─────────────────────┼─────────────────────┐
                              ▼                     ▼                     ▼
                        ┌──────────┐          ┌──────────┐          ┌──────────┐
                        │  Claude  │          │  OpenAI  │          │  Ollama  │
                        └──────────┘          └──────────┘          └──────────┘
```

## Requirements

- Python 3.11+
- macOS (M2 Ultra optimized)
- Talon Voice (optional, for integration)
- Whisper.cpp or faster-whisper

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp config/config.example.yaml config/config.yaml
# Edit config.yaml with your API keys

# Run the assistant
python -m nlr_01
```

## Configuration

Edit `config/config.yaml`:

```yaml
stt:
  engine: whisper
  model: base.en  # tiny, base, small, medium, large

llm:
  default: claude
  providers:
    claude:
      model: claude-sonnet-4-20250514
    openai:
      model: gpt-4
    ollama:
      model: llama3.2
      host: http://localhost:11434
```

## Talon Integration

Copy the Talon commands to your Talon user directory:

```bash
cp scripts/nlr_commands.talon ~/.talon/user/
```

## Author

Rob Plowman - NOIZYLAB / Fish Music Inc.
