import sys
import requests
import subprocess
import threading
import os

def sarah_11labs_speak(text):
    api_key = "b2e4a5aeb966fbd4aff9e46e7bc73d77073b34f042d6ecb0dbeb75b32d961536"
    voice_id = "YOUR_SARAH_VOICE_ID"  # Replace with your actual Sarah voice ID
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key}
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        with open("sarah_tts.mp3", "wb") as f:
            f.write(response.content)
        # Set system volume to 65% for quieter playback
        subprocess.run(['osascript', '-e', 'set volume output volume 65'])
        player = threading.Thread(target=lambda: os.system("afplay sarah_tts.mp3"))
        player.start()
        return player
    else:
        print("Error with 11 Labs TTS:", response.text)
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        sarah_11labs_speak(text)
    else:
        print("Usage: python3 sarah_system_tts.py 'Text to speak'")
