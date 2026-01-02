import os
import sys
import requests
import tempfile
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
SARAH_VOICE_ID = os.getenv('ELEVENLABS_SARAH_VOICE_ID', 'EXAVITQu4vr4xnSDxMaL')
API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{SARAH_VOICE_ID}"

HEADERS = {
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}

def sarah_speak(text):
    data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        print(f"[DEBUG] ElevenLabs API status: {response.status_code}")
        if response.status_code == 200:
            # Save audio for inspection
            audio_path = os.path.expanduser("~/Desktop/sarah_output.mp3")
            with open(audio_path, "wb") as f:
                f.write(response.content)
            print(f"[DEBUG] Audio saved to {audio_path}")
            # Play audio
            result = subprocess.run(["afplay", audio_path])
            if result.returncode != 0:
                print(f"[ERROR] afplay failed with code {result.returncode}")
        else:
            print(f"[ERROR] ElevenLabs API: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[EXCEPTION] {e}")

if __name__ == "__main__":
    # Accept text from stdin, argument, or prompt
    if not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    elif len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("Sarah says: ")
    if text:
        print(f"[DEBUG] Input text: {text}")
        sarah_speak(text)
    else:
        print("[ERROR] No text provided.")
