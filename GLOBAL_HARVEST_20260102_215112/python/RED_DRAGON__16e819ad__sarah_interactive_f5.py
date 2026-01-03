import os
import sys
import threading
import time
import requests
import subprocess
import keyboard  # pip install keyboard
import speech_recognition as sr  # pip install SpeechRecognition pyaudio

def sarah_11labs_speak(text, volume=65):
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
        subprocess.run(['osascript', '-e', f'set volume output volume {volume}'])
        player = threading.Thread(target=lambda: os.system("afplay sarah_tts.mp3"))
        player.start()
        return player
    else:
        print("Error with 11 Labs TTS:", response.text)
        return None

def listen_for_question():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening for your question...")
        audio = recognizer.listen(source)
    try:
        question = recognizer.recognize_google(audio)
        print(f"You asked: {question}")
        return question
    except Exception as e:
        print("Could not understand audio:", e)
        return "Sorry, I didn't catch that."

def main():
    print("Hold down F5 to ask Sarah a question.")
    while True:
        keyboard.wait('f5')
        question = listen_for_question()
        sarah_11labs_speak(f"You asked: {question}")
        time.sleep(1)

if __name__ == "__main__":
    main()
