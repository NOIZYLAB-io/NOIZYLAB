import requests
import subprocess
import time
import keyboard
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
            # Convert mono to stereo and play
            audio = AudioSegment.from_file("sarah_output.mp3")
            if audio.channels == 1:
                stereo_audio = AudioSegment.from_mono_audiosegments(audio, audio)
                play(stereo_audio)
            else:
                play(audio)
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

for point in important_points:
    sarah_11labs_speak(point)
    time.sleep(1.5)


