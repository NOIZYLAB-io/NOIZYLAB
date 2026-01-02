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

# Save as: ~/Desktop/NoizyFish/scripts/shell/flush_audio_env.sh

#!/bin/zsh
echo "🧹 Flushing CoreAudio and UAD..."
sudo launchctl kickstart -k system/com.apple.audio.coreaudiod
killall "UA Mixer Engine" "UAD Meter & Control Panel" "Console" 2>/dev/null
sleep 2
open -a "Console"
echo "✅ Audio environment reset. Apollo DSPs should be clean."

chmod +x ~/Desktop/NoizyFish/scripts/audio_hygiene.sh

{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Flush Audio Environment",
      "type": "shell",
      "command": "${workspaceFolder}/scripts/audio_hygiene.sh",
      "problemMatcher": []
    }
  ]
}

python3 ~/Desktop/NoizyFish/utilities/webador_migrate/webador_extract.py

ln -s ~/Desktop/NoizyFish/scripts ~/Desktop/NoisyScripts

cd ~/Desktop/NoizyFish/utilities/webador_migrate

cd ~/Desktop/NoizyFish/NoizyFish_OnGoing_SetUp

cp current_file_path ~/Desktop/NoizyFish/NoizyFish_OnGoing_SetUp

python3 ~/Desktop/NoizyFish/scripts/python/my_script.py

# Save as: ~/Desktop/NoizyFish/scripts/shell/setup_webador_env.sh

#!/bin/zsh
cd ~/Desktop/NoizyFish/utilities/webador_migrate
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install selenium webdriver-manager requests
echo "✅ Webador migration environment is ready!"

chmod +x ~/Desktop/NoizyFish/scripts/shell/setup_webador_env.sh
