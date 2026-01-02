import requests
import subprocess
import threading
import time
import sys
import termios
import tty

# --- 11 Labs Sarah TTS ---
def sarah_11labs_speak(text, api_key, voice_id):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key}
    data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.ok:
            with open("sarah_output.mp3", "wb") as f:
                f.write(response.content)
            subprocess.run(["afplay", "sarah_output.mp3"])
        else:
            print("Error with 11 Labs TTS:", response.text)
    except Exception as e:
        print("TTS execution failed:", e)

# --- Interactive Yes/No Prompt ---
def sarah_yes_no_prompt(question, api_key, voice_id):
    sarah_11labs_speak(question + " Please answer yes or no.", api_key, voice_id)
    print(question + " (y/n): ", end='', flush=True)
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1).lower()
            if ch == 'y':
                sarah_11labs_speak("You answered yes.", api_key, voice_id)
                return True
            elif ch == 'n':
                sarah_11labs_speak("You answered no.", api_key, voice_id)
                return False
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# --- Example Navigation Assistant ---
def navigation_assistant(api_key, voice_id):
    sarah_11labs_speak("Welcome to NoizyFish navigation assistant. Would you like to search for NoizyFish items outside your main folder?", api_key, voice_id)
    if sarah_yes_no_prompt("Search for NoizyFish items outside Desktop/NoizyFish?", api_key, voice_id):
        sarah_11labs_speak("Searching now.", api_key, voice_id)
        # Insert your search logic here
        time.sleep(2)
        sarah_11labs_speak("Search complete. Would you like to move found items into your main folder?", api_key, voice_id)
        if sarah_yes_no_prompt("Move found items into Desktop/NoizyFish?", api_key, voice_id):
            sarah_11labs_speak("Moving items now.", api_key, voice_id)
            # Insert your move logic here
            time.sleep(2)
            sarah_11labs_speak("All items have been moved.", api_key, voice_id)
        else:
            sarah_11labs_speak("No items were moved.", api_key, voice_id)
    else:
        sarah_11labs_speak("Navigation cancelled.", api_key, voice_id)

if __name__ == "__main__":
    api_key = "b2e4a5aeb966fbd4aff9e46e7bc73d77073b34f042d6ecb0dbeb75b32d961536"
    voice_id = "YOUR_SARAH_VOICE_ID"
    navigation_assistant(api_key, voice_id)
