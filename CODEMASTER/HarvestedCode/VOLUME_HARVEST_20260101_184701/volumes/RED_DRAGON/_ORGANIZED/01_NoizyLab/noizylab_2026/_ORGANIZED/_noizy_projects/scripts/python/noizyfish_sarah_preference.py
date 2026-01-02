import requests
import threading
import tkinter as tk
import os
import subprocess
from pathlib import Path

API_KEY = "your-elevenlabs-api-key"
VOICE_ID = "Sarah"
CODE_PATH = str(Path.home() / "Desktop" / "Hand of God" / "create_and_move_volume_aliases.py")
AUDIO_PATH = str(Path.home() / "Desktop" / "Hand of God" / "sarah_output.mp3")

# --- Volume Alias Creation ---
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
            if alias_path.is_symlink() and os.readlink(str(alias_path)) == str(vol):
                print(f"Alias already exists and is correct: {alias_path}")
            else:
                print(f"Alias already exists but may be incorrect: {alias_path}")
            continue
        try:
            os.symlink(str(vol), str(alias_path))
            print(f"Created alias for {vol} -> {alias_path}")
        except PermissionError:
            print(f"Permission denied: Failed to create alias for {vol}")
        except Exception as e:
            print(f"Failed to create alias for {vol}: {e}")
    print("All volume aliases created in Hand of God's Volume_Aliases subfolder.")

# --- Sarah Reader ---
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

def on_read():
    def task():
        speak_with_sarah(get_code_text())
        play_audio()
    threading.Thread(target=task).start()

def on_stop():
    stop_audio()

audio_process = None

if __name__ == "__main__":
    create_volume_aliases()
    # GUI for Sarah Reader
    root = tk.Tk()
    root.title("NoizyFish Sarah Reader Preference")
    read_btn = tk.Button(root, text="Read with Sarah", command=on_read)
    read_btn.pack(pady=10)
    stop_btn = tk.Button(root, text="Stop Sarah", command=on_stop)
    stop_btn.pack(pady=10)
    root.mainloop()
