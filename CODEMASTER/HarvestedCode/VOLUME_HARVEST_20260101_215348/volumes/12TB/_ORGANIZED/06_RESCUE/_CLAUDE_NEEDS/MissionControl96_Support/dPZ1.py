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

def speak_with_sarah(text):
    data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
            tmp.write(response.content)
            tmp.flush()
            # Play through system output (set to Loopback for routing)
            subprocess.run(["afplay", tmp.name])
            os.unlink(tmp.name)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Accept text from stdin or argument
    if not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    elif len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("Enter text for Sarah to speak: ")
    if text:
        speak_with_sarah(text)
    else:
        print("No text provided.")
