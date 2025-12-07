import os
import requests
import tempfile
import subprocess
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
SARAH_VOICE_ID = os.getenv('ELEVENLABS_SARAH_VOICE_ID', 'EXAVITQu4vr4xnSDxMaL')  # Replace with your Sarah voice ID if different
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
            subprocess.run(["afplay", tmp.name])  # macOS audio playback
            os.unlink(tmp.name)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("Enter text for Sarah to speak: ")
    speak_with_sarah(text)
