import requests
import subprocess
import time
import keyboard
import threading
import speech_recognition as sr
import pyaudio
from pydub import AudioSegment
from pydub.playback import play

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
            # Always convert to mono and play (centered)
            audio = AudioSegment.from_file("sarah_output.mp3")
            mono_audio = audio.set_channels(1)
            play(mono_audio)
        else:
            print("Error with 11 Labs TTS:", response.text)
    except Exception as e:
        print("TTS execution failed:", e)


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

if __name__ == "__main__":
    threading.Thread(target=control_key_listener, daemon=True).start()
    display_points(important_points)
pip install keyboard


