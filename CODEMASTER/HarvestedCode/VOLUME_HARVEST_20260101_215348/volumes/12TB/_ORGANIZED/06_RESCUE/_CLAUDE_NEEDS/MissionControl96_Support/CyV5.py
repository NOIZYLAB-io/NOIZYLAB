import requests
import subprocess
import time
import keyboard
import threading
import speech_recognition as sr
import pyaudio
from pydub import AudioSegment
from pydub.playback import play
import os

# Define your ElevenLabs API key here
# Define your ElevenLabs API key here
api_key = "PASTE_YOUR_ACTUAL_ELEVENLABS_API_KEY_HERE"
def sarah_11labs_speak(text, volume=70):
    # Set macOS system volume (0-100)
    try:
        subprocess.run(["osascript", "-e", f"set volume output volume {volume}"], check=True)
    except Exception:
        pass
    voice_id = "b2e4a5aeb966fbd4aff9e46e7bc73d77073b34f042d6ecb0dbeb75b32d961536"  # Replace with your actual Sarah voice ID
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key}
    # Advanced voice settings for expressiveness
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.3,  # More expressive
            "similarity_boost": 0.85,
            "style": "conversational",
            "use_speaker_boost": True
        }
    }
    try:
        # Caching for repeated phrases
        cache_file = f"sarah_cache_{abs(hash(text))}.mp3"
        if os.path.exists(cache_file):
            audio = AudioSegment.from_file(cache_file)
        else:
            response = requests.post(url, json=data, headers=headers)
            if response.ok:
                with open(cache_file, "wb") as f:
                    f.write(response.content)
                audio = AudioSegment.from_file(cache_file)
            else:
                print("Error with 11 Labs TTS:", response.text)
                return
        # Stereo, normalize, and add gentle background effect
        stereo_audio = audio.set_channels(2)
        normalized_audio = stereo_audio.apply_gain(-stereo_audio.max_dBFS)
        final_audio = add_background_effect(normalized_audio)
        play(final_audio)
    except Exception as e:
        print("TTS execution failed:", e)

# Add gentle background effect for immersion
def add_background_effect(audio_segment):
    try:
        # Optional: add a soft ambient background (e.g., gentle synth pad)
        bg_path = "sarah_bg_soft.mp3"
        if os.path.exists(bg_path):
            bg = AudioSegment.from_file(bg_path).set_channels(2).apply_gain(-30)
            # Loop background to match length
            bg = bg * (len(audio_segment) // len(bg) + 1)
            combined = audio_segment.overlay(bg[:len(audio_segment)])
            return combined
    except Exception:
        pass
    return audio_segment


important_points = [
    "You have 158 settings configured in your VS Code profile.",
    "Your terminal font is set to SL Mono, size 14 for legibility.",
    "The terminal and chat backgrounds use a sandy cream color for comfort.",
    "Accessibility and AI features are enabled for your workspace.",
    "Auto-save and code formatting are active for all files.",
    "Cloud sync and collaboration features are available.",
    "Security and audit logging are enabled for your projects."
]

# Display important points in a Tkinter window at font size 12
def display_points(points):
    import tkinter as tk
    root = tk.Tk()
    root.title("VS Code Bullet Points")
    text = tk.Text(root, font=("SL Mono", 12), bg="#f5ecd7", fg="#222", wrap="word")
    text.pack(expand=True, fill="both")
    for point in points:
        text.insert(tk.END, f"• {point}\n\n")
    text.config(state="disabled")
    root.mainloop()


def control_key_listener():
    while True:
        if keyboard.is_pressed('ctrl'):
            start = time.time()
            while keyboard.is_pressed('ctrl'):
                time.sleep(0.05)
                if time.time() - start > 1:
                    # Read all bullet points
                    for point in important_points:
                        sarah_11labs_speak(point)
                        time.sleep(1.5)
                    # Wait until key is released to avoid repeat
                    while keyboard.is_pressed('ctrl'):
                        time.sleep(0.1)
                    break
        time.sleep(0.1)

def voice_command_listener():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    while True:
        print("🎤 Say a command (e.g., 'Sarah, read my bullet points')...")
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Heard: {command}")
            if "sarah" in command:
                if "read my bullet points" in command:
                    for point in important_points:
                        sarah_11labs_speak(point)
                        time.sleep(1.2)
                elif "greet me" in command:
                    sarah_11labs_speak(f"Hello {os.getlogin()}, welcome back! It's {time.strftime('%A, %B %d, %I:%M %p')}")
                elif "volume up" in command:
                    sarah_11labs_speak("Turning volume up.", volume=100)
                elif "volume down" in command:
                    sarah_11labs_speak("Turning volume down.", volume=30)
                elif "read selected text" in command:
                    # Placeholder: integrate with VS Code API for selected text
                    sarah_11labs_speak("Selected text reading is not yet implemented.")
                else:
                    sarah_11labs_speak("Command not recognized. Try again.")
        except Exception as e:
            print(f"Voice command error: {e}")
        time.sleep(0.5)

def idle_reminder():
    idle_time = 0
    while True:
        if keyboard.is_pressed('ctrl') or keyboard.is_pressed('alt') or keyboard.is_pressed('cmd'):
            idle_time = 0
        else:
            idle_time += 1
        if idle_time > 60:  # 1 minute idle
            sarah_11labs_speak("You've been idle for a minute. Would you like a productivity tip?")
            idle_time = 0
        time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=control_key_listener, daemon=True).start()
    threading.Thread(target=voice_command_listener, daemon=True).start()
    threading.Thread(target=idle_reminder, daemon=True).start()
    display_points(important_points)

# To install pyaudio and set environment variables, run these commands in your terminal:
# export CPATH=$(brew --prefix)/include
# export LIBRARY_PATH=$(brew --prefix)/lib
# pip install pyaudio


