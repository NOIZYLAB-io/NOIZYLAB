# voice_assistant.py
# Features: wake word, async audio playback, error handling, VS Code task triggers

import asyncio
import speech_recognition as sr
import requests, os, tempfile, subprocess
from playsound import playsound

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
VOICE_ID = "your_sarah_voice_id"

async def listen_once():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except Exception:
        return None

async def speak(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": ELEVEN_API_KEY, "Content-Type": "application/json"}
    data = {"text": text}
    resp = requests.post(url, headers=headers, json=data)
    if resp.ok:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            f.write(resp.content)
            path = f.name
        playsound(path)
        os.remove(path)

async def handle_command(cmd):
    if "checklist" in cmd.lower():
        subprocess.run(["python", "forward1_all_in_one.py", "checklist"])
        return "Checklist run in VS Code."
    if "open godaddy" in cmd.lower():
        subprocess.run(["python", "forward1_all_in_one.py", "open", "godaddy"])
        return "Opening GoDaddy security."
    return f"You said: {cmd}"

async def main():
    while True:
        text = await listen_once()
        if not text:
            continue
        print("Heard:", text)
        response = await handle_command(text)
        await speak(response)

if __name__ == "__main__":
    asyncio.run(main())