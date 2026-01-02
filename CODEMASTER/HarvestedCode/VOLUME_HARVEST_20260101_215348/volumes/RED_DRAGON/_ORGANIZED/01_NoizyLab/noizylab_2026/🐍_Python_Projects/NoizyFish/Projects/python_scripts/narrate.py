import os
import sys
import subprocess
import requests
from elevenlabs import ElevenLabs

# Step 1: Load API key
# Prefer environment variable, else fallback to ~/.elevenlabs_api file
api_key = os.environ.get("ELEVENLABS_API_KEY")
if not api_key:
    config_path = os.path.expanduser("~/.elevenlabs_api")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            api_key = f.read().strip()

if not api_key:
    sys.exit("❌ No API key found. Please set ELEVENLABS_API_KEY or put it in ~/.elevenlabs_api")

# Step 2: Initialize client
client = ElevenLabs(api_key=api_key)

# Step 3: Choose voice + text
voice = "Rachel"  # Replace with any ElevenLabs stock or custom voice ID

if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
else:
    text = "Hello Rob, Lucy here. Fresh, casual, and ready to tell your story."

# Step 4: Convert text to speech
print(f"🔊 Generating narration with voice: {voice}")
audio = client.text_to_speech.convert(
    voice_id=voice,
    model_id="eleven_multilingual_v2",
    text=text
)

# Step 5: Save to file
output_file = os.path.expanduser("~/narration.wav")
with open(output_file, "wb") as f:
    for chunk in audio:
        f.write(chunk)

print(f"✅ Narration saved to {output_file}")

# Step 6: Auto-play result
try:
    subprocess.run(["afplay", output_file])  # macOS built-in audio player
except Exception as e:
    print(f"⚠️ Could not auto-play file: {e}")

response = requests.post(
    "http://127.0.0.1:8765/tts",
    json={"text": "This is a test from the MCP server."}
)
with open("test_narration.wav", "wb") as f:
    f.write(response.content)

print("* Running on http://127.0.0.1:8765")
