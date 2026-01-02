import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import subprocess

BOBBY_IMAGE = os.path.join(os.path.dirname(__file__), "bobby_fish.jpg")

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

    def _load_image(self):
        img = Image.open(BOBBY_IMAGE)
        img = img.resize((128,128), Image.LANCZOS)
        self.icon = ImageTk.PhotoImage(img)

    def on_click(self, event=None):
        self.status.config(text="Bobby: Got It!")
        threading.Thread(target=self._speak_bobby, args=("Got it.",), daemon=True).start()

    def _speak_bobby(self, text):
        try:
            subprocess.run(["python3", os.path.join(os.path.dirname(__file__), "speak_bobby.py"), text], check=True)
        except Exception as e:
            self.status.config(text=f"Error: {e}")

if __name__ == "__main__":
    app = BobbyWidget()
    app.mainloop()
