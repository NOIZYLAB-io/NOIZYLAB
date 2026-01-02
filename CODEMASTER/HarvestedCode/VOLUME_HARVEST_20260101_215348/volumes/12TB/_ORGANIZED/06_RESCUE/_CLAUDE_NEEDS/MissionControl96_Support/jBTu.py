#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import threading, subprocess, sys, os

APP_TITLE = "The Perfectionist"
SCRIPT = os.path.join(os.path.dirname(__file__), "../core/cleaner.py")

def run_cleaner(path):
    subprocess.run([sys.executable, SCRIPT], env={**os.environ, "PERFECTIONIST_PATH": path})

def drop(event):
    path = event.data.strip("{}")
    threading.Thread(target=run_cleaner, args=(path,), daemon=True).start()

# Try to use tkinterdnd2 for drag-and-drop
try:
    import tkinterdnd2 as tkdnd
    root = tkdnd.TkinterDnD.Tk()
    dnd_enabled = True
except ImportError:
    root = tk.Tk()
    dnd_enabled = False

root.title(APP_TITLE)
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry("120x120+40+40")
root.configure(bg="#1e1e1e")

canvas = tk.Canvas(root, width=120, height=120, bg="#1e1e1e", highlightthickness=0)
canvas.pack()

canvas.create_oval(10, 10, 110, 110, fill="#2e2e2e", outline="#888", width=2)
canvas.create_text(60, 60, text="🧹", font=("Helvetica", 42), fill="white")

def move(event): root.geometry(f"+{event.x_root-60}+{event.y_root-60}")
canvas.bind("<B1-Motion>", move)
canvas.bind("<Button-3>", lambda e: root.destroy())

if dnd_enabled:
    canvas.drop_target_register(tkdnd.DND_FILES)
    canvas.dnd_bind('<<Drop>>', drop)
else:
    print("Drag-and-drop not available (tkinterdnd2 not installed).")

try:
    import pip
    pip.main(['install', 'tkinterdnd2'])
except Exception as e:
    print(f"Error installing tkinterdnd2: {e}")

root.mainloop()