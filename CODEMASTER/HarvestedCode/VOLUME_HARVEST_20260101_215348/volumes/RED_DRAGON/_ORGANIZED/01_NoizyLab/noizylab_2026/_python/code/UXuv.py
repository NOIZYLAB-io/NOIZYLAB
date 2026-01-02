import tkinter as tk
from tkinter import ttk
import subprocess
import threading

def set_system_volume(val):
    # macOS system volume (0-100 mapped to 0-10)
    volume = int(float(val) / 10)
    subprocess.run(['osascript', '-e', f'set volume output volume {int(val)}'])

def auto_close(window, delay=10):
    def close():
        window.after(delay * 1000, window.destroy)
    threading.Thread(target=close).start()

def main():
    root = tk.Tk()
    root.title("Ernest Volume Slider")

    slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=set_system_volume)
    slider.set(50)
    slider.pack(fill='x', padx=20, pady=20)

    label = ttk.Label(root, text="Move the slider to set volume")
    label.pack(pady=10)

    auto_close(root, delay=15)  # Auto-close after 15 seconds

    root.mainloop()

if __name__ == "__main__":
    main() where is my slider what's that that's not is that the slider that can't be the slider