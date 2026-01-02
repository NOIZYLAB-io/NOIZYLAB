#!/usr/bin/env python3

import sys
import os
import sounddevice as sd
import numpy as np
from elevenlabs import ElevenLabs

def main():
    # Get text from command line
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello from Bobby in VS Code"

    # Get API key from environment variable for security
    api_key = os.getenv("ELEVENLABS_API_KEY", "YOUR_11LABS_API_KEY_HERE")
    if api_key == "YOUR_11LABS_API_KEY_HERE":
        print("[ERROR] Please set your ElevenLabs API key in the ELEVENLABS_API_KEY environment variable or directly in the script.")
        sys.exit(1)

    # Initialize client
    client = ElevenLabs(api_key=api_key)

    try:
        # Generate audio (returns a generator)
        audio_gen = client.text_to_speech.convert(
            voice_id="Rachel",   # Or whichever 11 Labs voice you like
            model_id="eleven_multilingual_v2",
            text=text
        )
        audio_bytes = b"".join(audio_gen)
        # Play audio
        sd.play(np.frombuffer(audio_bytes, dtype=np.int16), samplerate=44100)
        sd.wait()
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
