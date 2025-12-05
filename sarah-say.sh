#!/bin/zsh
# ElevenLabs "Sarah" voice universal say replacement
# Reads API key from env var ELEVENLABS_API_KEY or ~/.elevenlabs file

API_KEY="${ELEVENLABS_API_KEY:-$(cat ~/.elevenlabs 2>/dev/null)}"
VOICE_ID="PUT-SARAH-VOICE-ID-HERE"   # Replace this with Sarah's actual ElevenLabs voice ID

if [ -z "$API_KEY" ]; then
  echo "❌ No ElevenLabs API key found."
  echo "Set ELEVENLABS_API_KEY in your shell or save key to ~/.elevenlabs"
  exit 1
fi

if [ $# -eq 0 ]; then
  echo "Usage: say \"text to speak\""
  exit 1
fi

TEXT="$*"
OUTPUT="/tmp/sarah_output.mp3"

curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/$VOICE_ID" \
  -H "xi-api-key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"text\": \"$TEXT\",
    \"voice_settings\": { \"stability\": 0.5, \"similarity_boost\": 0.75 }
  }" \
  --output "$OUTPUT"

if [ -s "$OUTPUT" ]; then
  afplay "$OUTPUT"
  rm -f "$OUTPUT"
else
  echo "❌ Sarah voice request failed"
fi
