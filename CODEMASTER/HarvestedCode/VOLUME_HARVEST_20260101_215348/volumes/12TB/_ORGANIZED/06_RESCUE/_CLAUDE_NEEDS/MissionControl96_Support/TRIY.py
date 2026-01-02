#!/usr/bin/env python3
import sys
import sounddevice as sd
import numpy as np
from elevenlabs import ElevenLabs

# Get text from command line
text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello from Bobby"

# Initialize client with your API key
client = ElevenLabs(api_key="YOUR_11LABS_API_KEY_HERE")

# Generate audio
audio = client.text_to_speech.convert(
    voice_id="Rachel",                 # Change to your preferred voice ID
    model_id="eleven_multilingual_v2", # Best for smooth natural performance
    text=text
)

# Play audio
sd.play(np.frombuffer(audio, dtype=np.int16), samplerate=44100)
sd.wait()
