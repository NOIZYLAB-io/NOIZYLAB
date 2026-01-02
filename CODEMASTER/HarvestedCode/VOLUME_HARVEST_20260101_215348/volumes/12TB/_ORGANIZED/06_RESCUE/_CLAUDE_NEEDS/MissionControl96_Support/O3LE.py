import os
import sys

def read_paragraph():
    # Function to read a paragraph from a file
    pass

if __name__ == "__main__":
    read_paragraph()

import requests
import subprocess
import threading
import time
import sys
import termios
import tty

# --- 11 Labs Sarah TTS ---
def sarah_11labs_speak(text):
    api_key = "b2e4a5aeb966fbd4aff9e46e7bc73d77073b34f042d6ecb0dbeb75b32d961536"
    voice_id = "YOUR_SARAH_VOICE_ID"  # Replace with your actual Sarah voice ID
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key}
    data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.ok:
            with open("sarah_output.mp3", "wb") as f:
                f.write(response.content)
            # Play audio in a separate thread so it can be stopped
            player = threading.Thread(target=subprocess.run, args=(["afplay", "sarah_output.mp3"],))
            player.start()
            return player
        else:
            print("Error with 11 Labs TTS:", response.text)
    except Exception as e:
        print("TTS execution failed:", e)
    return None

# --- Keyboard listener for spacebar ---
def wait_for_spacebar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == ' ':
                return
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# --- Main logic ---
paragraph = "The ‘158 settings found’ message at the top of the settings folder means that VS Code has detected 158 individual configuration options in your current settings.json file. This count includes all keys and sub-settings you’ve customized for your profile. It’s just an indicator of how many settings are present, not an error or warning."

print("Press SPACE to have Sarah read the paragraph. Press SPACE again to stop playback.")

while True:
    wait_for_spacebar()
    player_thread = sarah_11labs_speak(paragraph)
    wait_for_spacebar()
    # Attempt to stop playback
    subprocess.run(["killall", "afplay"])
    print("Playback stopped. Press SPACE to play again.")

os.system("python3 /Users/rsp_ms/Desktop/NoizyFish/utilities/fb_autorun.py --run")

FB_ACCESS_TOKEN=your-valid-access-token
FB_APP_ID=your-app-id
FB_APP_SECRET=your-app-secret
