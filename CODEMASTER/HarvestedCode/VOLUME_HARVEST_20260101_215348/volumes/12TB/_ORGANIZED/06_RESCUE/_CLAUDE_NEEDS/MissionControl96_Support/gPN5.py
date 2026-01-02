import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import os
import threading
import sys

BOBBY_IMAGE = os.path.join(os.path.dirname(__file__), "bobby_fish.jpg")

def speak_with_elevenlabs(text, api_key):
    try:
        from elevenlabs import ElevenLabs
        from elevenlabs.types.voice_settings import VoiceSettings
        from elevenlabs.play import play
        client = ElevenLabs(api_key=api_key)
        settings = VoiceSettings(
            stability=float(os.getenv("BOBBY_STABILITY", 0.5)),
            similarity_boost=float(os.getenv("BOBBY_SIMILARITY_BOOST", 0.75)),
            style=float(os.getenv("BOBBY_STYLE", 0.0)),
            use_speaker_boost=bool(int(os.getenv("BOBBY_SPEAKER_BOOST", 1))),
            speed=float(os.getenv("BOBBY_SPEED", 1.0)),
        )
        audio_gen = client.text_to_speech.convert(
            voice_id=os.getenv("BOBBY_VOICE_ID", "Rachel"),
            text=text,
            model_id=os.getenv("BOBBY_MODEL_ID", "eleven_multilingual_v2"),
            voice_settings=settings,
            output_format="mp3_44100_128",
        )
        audio_bytes = b"".join(audio_gen)
        play(audio_bytes)
        return True
    except Exception as e:
        print(f"[ERROR] ElevenLabs TTS failed: {e}")
        return False

class BobbyWidget(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bobby Widget")
        self.geometry("180x180+50+50")
        self.resizable(False, False)
        self.configure(bg="#222")
        self.icon = None
        self._load_image()
        self.label = tk.Label(self, image=self.icon, bg="#222")
        self.label.pack(padx=10, pady=10)
        self.label.bind("<Button-1>", self.on_click)
        self.status = tk.Label(self, text="Click Bobby!", fg="#fff", bg="#222", font=("Arial", 12))
        self.status.pack(pady=(0,10))
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        if not self.api_key:
            self.after(500, self.prompt_api_key)

    def _load_image(self):
        img = Image.open(BOBBY_IMAGE)
        img = img.resize((128,128), Image.LANCZOS)
        self.icon = ImageTk.PhotoImage(img)

    def prompt_api_key(self):
        self.api_key = simpledialog.askstring("ElevenLabs API Key", "Enter your ElevenLabs API Key:", show='*')
        if self.api_key:
            os.environ["ELEVENLABS_API_KEY"] = self.api_key
        else:
            self.status.config(text="API key required for voice.")

    def on_click(self, event=None):
        self.status.config(text="Bobby: Got It!")
        threading.Thread(target=self._speak_bobby, args=("Got it.",), daemon=True).start()

    def _speak_bobby(self, text):
        if not self.api_key:
            self.status.config(text="No API key for ElevenLabs.")
            return
        ok = speak_with_elevenlabs(text, self.api_key)
        if not ok:
            self.status.config(text="TTS failed. Check API key.")

if __name__ == "__main__":
    app = BobbyWidget()
    app.mainloop()
