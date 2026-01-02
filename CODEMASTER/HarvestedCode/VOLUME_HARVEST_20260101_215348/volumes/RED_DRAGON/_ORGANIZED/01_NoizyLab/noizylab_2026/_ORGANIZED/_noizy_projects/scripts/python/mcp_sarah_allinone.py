import os
from flask import Flask, request, send_file, jsonify
import requests
import threading
import time
import sys
import termios
import tty

app = Flask(__name__)

# Set your ElevenLabs API key and Sarah voice ID as environment variables
ELEVENLABS_API_KEY = "b2e4a5aeb966fbd4aff9e46e7bc73d77073b34f042d6ecb0dbeb75b32d961536"
SARAH_VOICE_ID = os.getenv("SARAH_VOICE_ID", "EXAMPLE_SARAH_VOICE_ID")  # Replace with actual Sarah demo voice ID

# --- Sarah TTS via ElevenLabs API ---
def sarah_11labs_speak(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{SARAH_VOICE_ID}"
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        with open("sarah_tts.mp3", "wb") as f:
            f.write(response.content)
        # Play audio in a separate thread
        player = threading.Thread(target=lambda: os.system("afplay sarah_tts.mp3"))
        player.start()
        return player
    else:
        print("Error with 11 Labs TTS:", response.text)
        return None

# --- Interactive Yes/No Prompt ---
def sarah_yes_no_prompt(question):
    sarah_11labs_speak(question + " Please answer yes or no.")
    print(question + " (y/n): ", end='', flush=True)
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1).lower()
            if ch == 'y':
                sarah_11labs_speak("You answered yes.")
                return True
            elif ch == 'n':
                sarah_11labs_speak("You answered no.")
                return False
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# --- MCP Server Endpoints ---
@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{SARAH_VOICE_ID}"
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        with open("sarah_tts.mp3", "wb") as f:
            f.write(response.content)
        return send_file("sarah_tts.mp3", mimetype="audio/mpeg")
    else:
        return jsonify({"error": response.text}), 500

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "MCP server running", "voice": "Sarah (ElevenLabs demo)"})

# --- Main Interactive Navigation ---
def navigation_assistant():
    sarah_11labs_speak("Welcome to NoizyFish navigation assistant. Would you like to search for NoizyFish items outside your main folder?")
    if sarah_yes_no_prompt("Search for NoizyFish items outside Desktop/NoizyFish?"):
        sarah_11labs_speak("Searching now.")
        # Insert your search logic here
        time.sleep(2)
        sarah_11labs_speak("Search complete. Would you like to move found items into your main folder?")
        if sarah_yes_no_prompt("Move found items into Desktop/NoizyFish?"):
            sarah_11labs_speak("Moving items now.")
            # Insert your move logic here
            time.sleep(2)
            sarah_11labs_speak("All items have been moved.")
        else:
            sarah_11labs_speak("No items were moved.")
    else:
        sarah_11labs_speak("Navigation cancelled.")

if __name__ == '__main__':
    # Start MCP server in a thread
    server_thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000))
    server_thread.daemon = True
    server_thread.start()
    # Start interactive assistant
    navigation_assistant()
