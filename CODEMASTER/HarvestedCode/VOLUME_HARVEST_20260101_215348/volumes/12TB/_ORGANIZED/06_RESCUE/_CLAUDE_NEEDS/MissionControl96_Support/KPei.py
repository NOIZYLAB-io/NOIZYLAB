#!/usr/bin/env python3
"""
ENGR Diagnostic Script
Run this in VS Code or terminal to check that ENGR + Sarah setup is correct.
"""

import sys
import os
import importlib
import json

print("🔎 ENGR Diagnostic Check\n")

# 1. Python version
print(f"Python version: {sys.version}")
if sys.version_info < (3, 9):
    print("❌ Python 3.9+ recommended")
else:
    print("✅ Python version is good")

# 2. Virtual environment
venv = os.environ.get("VIRTUAL_ENV")
if venv:
    print(f"✅ Running inside venv: {venv}")
else:
    print("⚠️ Not inside a virtual environment")

# 3. Check packages
required = ["openai", "sounddevice", "soundfile", "requests", "numpy", "pynput"]
for pkg in required:
    try:
        importlib.import_module(pkg)
        print(f"✅ Package installed: {pkg}")
    except ImportError:
        print(f"❌ Missing package: {pkg}")

# 4. API keys
openai_key = os.environ.get("OPENAI_API_KEY")
eleven_key = os.environ.get("ELEVENLABS_API_KEY")
if openai_key:
    print("✅ OPENAI_API_KEY found")
else:
    print("❌ OPENAI_API_KEY missing")

if eleven_key:
    print("✅ ELEVENLABS_API_KEY found")
else:
    print("❌ ELEVENLABS_API_KEY missing")

# 5. Config file
config_path = os.path.expanduser("~/.engr/config.json")
if os.path.exists(config_path):
    try:
        with open(config_path) as f:
            config = json.load(f)
        print(f"✅ Config loaded: {config}")
    except Exception as e:
        print(f"❌ Config error: {e}")
else:
    print("⚠️ No config.json found at ~/.engr/config.json")

# 6. Audio device check
try:
    import sounddevice as sd
    devices = sd.query_devices()
    print(f"✅ Audio devices detected: {len(devices)} found")
    for i, d in enumerate(devices):
        print(f"  [{i}] {d['name']} (in:{d['max_input_channels']} out:{d['max_output_channels']})")
except Exception as e:
    print(f"❌ Audio check failed: {e}")

print("\n🔎 Diagnostic complete.")

# Requirements: pip install sounddevice soundfile requests openai

import os
import sys
import tempfile
import sounddevice as sd
import soundfile as sf
import requests
from openai import OpenAI
import numpy as np

# === Setup ===
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")  # Sarah’s default

# === Recording ===
def record_audio():
    print("Recording... Press Enter again to stop.")
    samplerate = 44100
    channels = 1
    audio_data = []

    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        audio_data.append(indata.copy())

    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
        input()  # wait for Enter to stop
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    with sf.SoundFile(tmpfile.name, mode='x', samplerate=samplerate, channels=channels, subtype='PCM_16') as f:
        for frame in audio_data:
            f.write(frame)
    print(f"💾 Saved recording to {tmpfile.name}")
    return tmpfile.name

# === Transcription (Whisper) ===
def transcribe(path):
    with open(path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return transcript.text

# === Chat (GPT) ===
def chat(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# === TTS (ElevenLabs Sarah) ===
def speak(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code != 200:
        print("❌ ElevenLabs error:", resp.text)
        return
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    with open(tmpfile.name, "wb") as f:
        f.write(resp.content)
    os.system(f"afplay {tmpfile.name}")

# === Main Loop ===
def main():
    print("ENGR Voice Beta (Sarah)")
    print("Press Enter to record. Type q + Enter to quit.")
    while 
True:
        cmd = input("> ")
        if cmd.lower() == "q":
            break
        path = record_audio()
        text = transcribe(path)
        print("🗣️ You said:", text)
        reply = chat(text)
        print("🤖 Sarah:", reply)
        speak(reply)

if __name__ == "__main__":
    if not os.getenv("1234567890abcdef1234567890abcdef") or not ELEVENLABS_API_KEY:
        print("❌ Missing API keys. Please set OPENAI_API_KEY and ELEVENLABS_API_KEY in your environment.")
        sys.exit(1)
    main()

# Create a dedicated ENGR venv
# python3 -m venv ~/ENGR-venv

# Activate it
# source ~/ENGR-venv/bin/activate

# Install everything Sarah needs
# pip install requests sounddevice soundfile openai numpy

# Navigate to project directory
# cd ~/Documents/ENGR

import sounddevice as sd

print("Input Devices:")
for idx, dev in enumerate(sd.query_devices()):
    if dev['max_input_channels'] > 0:
        print(f"{idx}: {dev['name']}")

print("\nOutput Devices:")
for idx, dev in enumerate(sd.query_devices()):
    if dev['max_output_channels'] > 0:
        print(f"{idx}: {dev['name']}")

nano ~/.engr/config.json

chmod +x ~/Downloads/ENGR_All_in_One_Installer.sh

source ~/ENGR-venv/bin/activate
python3 ~/Documents/ENGR/bin/engr_diagnostic.py