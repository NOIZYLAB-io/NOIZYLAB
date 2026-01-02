import speech_recognition as sr
import requests
import threading
import os
import subprocess
from pathlib import Path

API_KEY = "your-elevenlabs-api-key"
VOICE_ID = "Sarah"
CODE_PATH = str(Path.home() / "Desktop" / "Hand of God" / "create_and_move_volume_aliases.py")
AUDIO_PATH = str(Path.home() / "Desktop" / "Hand of God" / "sarah_output.mp3")
VOLUMES = Path("/Volumes")
SUBFOLDER = Path.home() / "Desktop" / "Hand of God" / "Volume_Aliases"
SUBFOLDER.mkdir(parents=True, exist_ok=True)
SKIP_VOLUMES = {"Macintosh HD", "Recovery", "Preboot"}

def create_volume_aliases():
    for vol in VOLUMES.iterdir():
        if vol.name.startswith('.') or not vol.is_dir() or vol.name in SKIP_VOLUMES:
            continue
        alias_path = SUBFOLDER / vol.name
        if alias_path.exists():
            continue
        try:
            os.symlink(str(vol), str(alias_path))
        except Exception:
            pass

def get_code_text():
    with open(CODE_PATH, "r") as f:
        return f.read()

def speak_with_sarah(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.85
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    with open(AUDIO_PATH, "wb") as f:
        f.write(response.content)

def play_audio():
    global audio_process
    audio_process = subprocess.Popen(["afplay", AUDIO_PATH])

def stop_audio():
    global audio_process
    if audio_process:
        audio_process.terminate()
        audio_process = None

def listen_for_commands():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Say a command: 'create volume aliases', 'read code', 'stop audio', 'exit'")
    while True:
        with mic as source:
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            if "create volume aliases" in command:
                create_volume_aliases()
                speak_with_sarah("Volume aliases created.")
                play_audio()
            elif "read code" in command:
                speak_with_sarah(get_code_text())
                play_audio()
            elif "stop audio" in command:
                stop_audio()
                speak_with_sarah("Audio stopped.")
                play_audio()
            elif "exit" in command:
                speak_with_sarah("Exiting. Goodbye!")
                play_audio()
                break
        except Exception as e:
            print("Could not understand. Try again.")

audio_process = None

if __name__ == "__main__":
    listen_for_commands()
