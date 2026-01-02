
from fastapi import FastAPI
from pydantic import BaseModel


import logging
import os
from datetime import datetime
import requests

class MCPClient:
    def __init__(self):
        self.log_file = "./mcp_events.log"
        logging.basicConfig(filename=self.log_file, level=logging.INFO)
        self.api_key = os.environ.get("ELEVENLABS_API_KEY", "")
        self.voice_id = os.environ.get("ELEVEN_VOICE_ID", "")
        self.default_voice = "Sarah"

    def send_event(self, event_type, data):
        msg = f"[{datetime.now()}] Event: {event_type} | Data: {data}"
        print(msg)
        logging.info(msg)
        if event_type == "speak":
            self.speak(data.get('text'), data.get('voice', self.default_voice))

    def speak(self, text, voice_name):
        # Real ElevenLabs TTS integration
        if not self.api_key:
            print("No ElevenLabs API key set. Cannot use Sarah.")
            return
        voice_id = self.voice_id or self.get_voice_id(voice_name)
        if not voice_id:
            print(f"Voice '{voice_name}' not found. Using fallback.")
            return
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {"xi-api-key": self.api_key, "accept": "audio/mpeg", "Content-Type": "application/json"}
        payload = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}}
        try:
            r = requests.post(url, headers=headers, json=payload)
            if r.status_code == 200:
                out_path = f"./Backups/sarah_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
                with open(out_path, "wb") as f:
                    f.write(r.content)
                print(f"✅ Sarah TTS generated: {out_path}")
            else:
                print(f"❌ ElevenLabs TTS error: {r.status_code} {r.text}")
        except Exception as e:
            print(f"❌ ElevenLabs TTS exception: {e}")

    def get_voice_id(self, voice_name):
        # Fetch voice_id for given name
        if not self.api_key:
            return None
        url = "https://api.elevenlabs.io/v1/voices"
        headers = {"xi-api-key": self.api_key, "accept": "application/json"}
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                data = r.json()
                for v in data.get("voices", []):
                    if v.get("name", "").lower() == voice_name.lower():
                        return v.get("voice_id", "")
            return None
        except Exception:
            return None

    def diagnostics(self):
        # Improved healthcheck
        checks = {
            "python": True,
            "api_key": bool(self.api_key),
            "voice_sarah": bool(self.get_voice_id("Sarah")),
            "icloud_sync": os.path.isdir(os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/SleepLearning")),
        }
        return checks

    def generate_playlist(self):
        # Playlist generation
        playlist_path = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/SleepLearning/playlist.m3u")
        with open(playlist_path, "w") as f:
            f.write("#EXTM3U\n")
            audio_dir = os.path.dirname(playlist_path)
            for file in os.listdir(audio_dir):
                if file.endswith(".mp3"):
                    f.write(f"{file}\n")
        print(f"Playlist generated at {playlist_path}")


app = FastAPI()
mcp_client = MCPClient()

class Message(BaseModel):
    text: str


@app.post("/speak")
def speak(message: Message):
    mcp_client.send_event("speak", {"text": message.text})
    return {"response": f"Sarah says: {message.text}"}

@app.get("/diagnostics")
def diagnostics():
    return mcp_client.diagnostics()

@app.post("/generate_playlist")
def generate_playlist():
    mcp_client.generate_playlist()
    return {"status": "Playlist generated"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("mcp_server:app", host="127.0.0.1", port=8788, reload=True)
