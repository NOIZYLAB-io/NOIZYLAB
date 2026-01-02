#!/usr/bin/env python3

import sys
import os
import subprocess
try:
    import sounddevice as sd
    import numpy as np
    from elevenlabs import ElevenLabs
except ImportError:
    print("[ERROR] Required packages not found. Please activate your virtual environment and install dependencies.")
    sys.exit(1)

def speak_with_elevenlabs(text, api_key, voice_id="Rachel", model_id="eleven_multilingual_v2"):
    try:
        client = ElevenLabs(api_key=api_key)
        audio_gen = client.text_to_speech.convert(
            voice_id=voice_id,
            model_id=model_id,
            text=text
        )
        audio_bytes = b"".join(audio_gen)
        sd.play(np.frombuffer(audio_bytes, dtype=np.int16), samplerate=44100)
        sd.wait()
        return True
    except Exception as e:
        print(f"[ERROR] ElevenLabs TTS failed: {e}")
        return False

def speak_with_say(text):
    try:
        subprocess.run(["say", text], check=True)
        return True
    except Exception as e:
        print(f"[ERROR] macOS 'say' failed: {e}")
        return False

def main():
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello from Bobby in VS Code"
    api_key = os.getenv("ELEVENLABS_API_KEY")

    if api_key:
        success = speak_with_elevenlabs(text, api_key)
        if success:
            return
        print("[INFO] Falling back to macOS 'say' command.")
        speak_with_say(text)
    else:
        print("[WARN] ELEVENLABS_API_KEY not set. Using macOS 'say' command.")
        speak_with_say(text)

if __name__ == "__main__":
    main()
