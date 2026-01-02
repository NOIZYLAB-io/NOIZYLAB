#!/usr/bin/env python3
"""
cha_cha_listener_bridge.py
Continuously listens for Cha-Cha trigger, sends commands to Bubba (VS Buddy core), and speaks responses.
"""
import speech_recognition as sr
import subprocess
from pathlib import Path

TRIGGER = "hey cha cha"
WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
BRIDGE = WORKSPACE / "cha_cha_to_bubba.py"
VOICE = "Siri Voice 3"

def speak(msg):
    subprocess.run(["say", "-v", VOICE, msg], check=False)

def send_to_bubba(command: str):
    if not BRIDGE.exists():
        speak("Bridge script not found.")
        return "Bridge script missing."
    try:
        result = subprocess.check_output([
            "python3", str(BRIDGE), command
        ], text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Bubba error: {e.output}"

def listen_loop():
    r = sr.Recognizer()
    mic = sr.Microphone()
    speak("Cha-Cha is listening for you, my dear.")
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        try:
            text = r.recognize_google(audio).lower().strip()
            print("Heard:", text)
            if TRIGGER in text:
                command = text.replace(TRIGGER, "").strip()
                if not command:
                    speak("Yes, my dear?")
                else:
                    response = send_to_bubba(command)
                    print("Bubba says:", response)
                    speak(response)
        except sr.UnknownValueError:
            continue
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I didn't catch that.")

if __name__ == "__main__":
    listen_loop()
