import tkinter as tk
import threading
import time
import os

STATUS_FILE = "/Volumes/6TB/noisy fish/noisyfish_status.txt"

class NoisyFishWidget(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Noisy Fish TV")
        self.geometry("220x120")
        self.resizable(True, True)
        self.configure(bg="#222222")
        self.attributes('-topmost', True)
        self.iconify = False
        self.label = tk.Label(self, text="Noisy Fish\nTransfer Monitor", font=("Arial", 12, "bold"), fg="#00ffcc", bg="#222222")
        self.label.pack(pady=5)
        self.status = tk.Label(self, text="Waiting for data...", font=("Arial", 10), fg="#ffffff", bg="#222222")
        self.status.pack(pady=5)
        self.speed = tk.Label(self, text="Speed: -- MB/s", font=("Arial", 10), fg="#ffcc00", bg="#222222")
        self.speed.pack(pady=5)
        self.after(1000, self.update_status)

    def update_status(self):
        if os.path.exists(STATUS_FILE):
            try:
                with open(STATUS_FILE, "r") as f:
                    lines = f.readlines()
                if lines:
                    self.status.config(text=lines[0].strip())
                if len(lines) > 1:
                    self.speed.config(text=lines[1].strip())
            except Exception as e:
                self.status.config(text=f"Error: {e}")
        else:
            self.status.config(text="Waiting for data...")
            self.speed.config(text="Speed: -- MB/s")
        self.after(1000, self.update_status)

def run_widget():
    app = NoisyFishWidget()
    app.mainloop()

if __name__ == "__main__":
    run_widget()
