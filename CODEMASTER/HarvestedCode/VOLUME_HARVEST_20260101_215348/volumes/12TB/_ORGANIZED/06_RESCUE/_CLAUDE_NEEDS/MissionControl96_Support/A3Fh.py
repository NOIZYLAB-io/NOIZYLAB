
from fastapi import FastAPI
from pydantic import BaseModel


import logging
import os
from datetime import datetime

class MCPClient:
    def __init__(self):
        self.log_file = "./mcp_events.log"
        logging.basicConfig(filename=self.log_file, level=logging.INFO)

    def send_event(self, event_type, data):
        msg = f"[{datetime.now()}] Event: {event_type} | Data: {data}"
        print(msg)
        logging.info(msg)
        # Sarah TTS stub (replace with ElevenLabs API call)
        if event_type == "speak":
            print(f"Sarah says: {data.get('text')}")

    def diagnostics(self):
        # Basic healthcheck
        checks = {
            "python": True,
            "api_key": bool(os.environ.get("ELEVENLABS_API_KEY")),
            "voice_sarah": True,  # Stub: Assume Sarah is available
            "icloud_sync": os.path.isdir(os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/SleepLearning")),
        }
        return checks

    def generate_playlist(self):
        # Stub for playlist generation
        playlist_path = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/SleepLearning/playlist.m3u")
        with open(playlist_path, "w") as f:
            f.write("#EXTM3U\n")
            # Add all mp3 files
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
    uvicorn.run("mcp_server:app", host="127.0.0.1", port=8777, reload=True)
