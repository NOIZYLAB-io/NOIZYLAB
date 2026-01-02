import speech_recognition as sr

import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import os
import threading
import sys
import json

BOBBY_IMAGE = os.path.join(os.path.dirname(__file__), "bobby_fish.jpg")
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "bobby_actions.json")

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
    def listen_for_command(self):
        self.status.config(text="Listening for command...")
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            self.status.config(text=f"Heard: {text}")
            self.handle_voice_command(text)
        except sr.UnknownValueError:
            self.status.config(text="Sorry, I didn't catch that.")
        except sr.RequestError as e:
            self.status.config(text=f"Speech error: {e}")

    def handle_voice_command(self, text):
        # Map recognized text to actions
        cmd = text.strip().lower()
        for item in self.actions.get("right_menu", []):
            if item.get("label", "").lower() in cmd:
                self.run_action(item.get("command", ""), item.get("label", ""))
                return
        # Fallback: speak the command
        self.status.config(text=f"Bobby: {text}")
        threading.Thread(target=self._speak_bobby, args=(text,), daemon=True).start()
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)  # Remove window border/title bar
        self.attributes("-topmost", True)  # Always on top
        self.geometry("180x180+50+50")
        self.resizable(False, False)
        self.configure(bg="#222")
        self.icon = None
        self._load_image()
        self.label = tk.Label(self, image=self.icon, bg="#222")
        self.label.pack(padx=10, pady=10)
        self.label.bind("<Button-1>", self.on_click)
        self.label.bind("<Button-3>", self.on_right_click_menu)
        self.label.bind("<B1-Motion>", self.on_drag)
        self.status = tk.Label(self, text="Click Bobby!", fg="#fff", bg="#222", font=("Arial", 12))
        self.status.pack(pady=(0,10))
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        if not self.api_key:
            self.after(500, self.prompt_api_key)
        # Hide from dock/taskbar on macOS
        if sys.platform == "darwin":
            try:
                import ctypes
                NSApplication = ctypes.cdll.LoadLibrary("/System/Library/Frameworks/AppKit.framework/AppKit").NSApplication
                NSApplication.sharedApplication().setActivationPolicy_(1)  # NSApplicationActivationPolicyAccessory
            except Exception:
                pass
        self._drag_data = {"x": 0, "y": 0}
        self.actions = self.load_actions()

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

    def load_actions(self):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Bobby] Could not load actions config: {e}")
            return {}

    def on_click(self, event=None):
        self._drag_data["x"] = event.x_root - self.winfo_rootx()
        self._drag_data["y"] = event.y_root - self.winfo_rooty()
        # Run left-click action if defined
        action = self.actions.get("left_click")
        if action:
            self.status.config(text=f"Bobby: {action.get('label','Running...')}")
            threading.Thread(target=self.run_action, args=(action["command"],), daemon=True).start()
        else:
            self.status.config(text="Bobby: Got It!")
            threading.Thread(target=self._speak_bobby, args=("Got it.",), daemon=True).start()

    def on_right_click_menu(self, event=None):
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Listen (Voice Command)", command=lambda: threading.Thread(target=self.listen_for_command, daemon=True).start())
        for item in self.actions.get("right_menu", []):
            label = item.get("label", "Action")
            cmd = item.get("command", "")
            if cmd == "close":
                menu.add_command(label=label, command=self.destroy)
            else:
                menu.add_command(label=label, command=lambda c=cmd, l=label: self.run_action(c, l))
        menu.add_separator()
        menu.add_command(label="Quit", command=self.destroy)
        menu.tk_popup(event.x_root, event.y_root)

    def run_action(self, command, label=None):
        import subprocess
        if command == "close":
            self.destroy()
            return
        try:
            if command.startswith("python3") or command.startswith("sh"):
                subprocess.Popen(command, shell=True, cwd=os.path.dirname(__file__))
            else:
                subprocess.Popen(command, shell=True)
            if label:
                self.status.config(text=f"Bobby: {label}")
        except Exception as e:
            self.status.config(text=f"Error: {e}")

    def on_drag(self, event):
        x = self.winfo_pointerx() - self._drag_data["x"]
        y = self.winfo_pointery() - self._drag_data["y"]
        self.geometry(f"+{x}+{y}")

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
