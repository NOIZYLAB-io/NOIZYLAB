# Requirements: pip install sounddevice soundfile requests openai

import os
import sys
import tempfile
import sounddevice as sd
import soundfile as sf
import requests
from openai import OpenAI

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
    while True:
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
    if not os.getenv("OPENAI_API_KEY") or not ELEVENLABS_API_KEY:
        print("❌ Missing API keys. Please set OPENAI_API_KEY and ELEVENLABS_API_KEY in your environment.")
        sys.exit(1)
    main()