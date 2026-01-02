#!/usr/bin/env python3

import subprocess
import datetime
import os
import threading
import time
from flask import Flask, render_template_string, request, redirect

# --- CONFIG ---
MUSIC_DIR = "/Users/rob/Music/Libraries"
SAMPLE_DIR = "/Users/rob/Samples"
SYNC_DIRS = ["/Users/rob/NoizyFish/Shared"]
LOG_PATH = "/Users/rob/NoizyFish/Logs/music_server.log"
VOICE_FEEDBACK = True
SCHEDULE_INTERVAL = 1800  # 30 minutes

# --- UTILS ---
def ensure_log_dir():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def log_event(message):
    ensure_log_dir()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as log:
        log.write(f"{timestamp} {message}\n")

def speak(message, voice="Samantha", volume=50):
    if VOICE_FEEDBACK:
        subprocess.run(["osascript", "-e", f"set volume output volume {volume}"])
        subprocess.run(["say", "-v", voice, message])

def sync_files():
    for sync_dir in SYNC_DIRS:
        subprocess.run(["rsync", "-avz", sync_dir, SAMPLE_DIR], check=False)
        log_event(f"Synced {sync_dir} to {SAMPLE_DIR}")

def play_audio(file_path):
    if os.path.exists(file_path):
        subprocess.run(["afplay", file_path])
        log_event(f"Played: {file_path}")
        speak(f"Playing {os.path.basename(file_path)}.")
    else:
        log_event(f"File not found: {file_path}")
        speak(f"File {os.path.basename(file_path)} not found.", voice="Victoria", volume=30)

def scan_music():
    music_files = []
    for root, dirs, files in os.walk(MUSIC_DIR):
        for file in files:
            if file.lower().endswith((".mp3", ".wav", ".aiff", ".flac")):
                music_files.append(os.path.join(root, file))
    return music_files

def scheduled_sync_and_scan():
    while True:
        sync_files()
        log_event("Scheduled sync complete.")
        speak("Music libraries synced.")
        time.sleep(SCHEDULE_INTERVAL)

# --- WEB DASHBOARD ---
app = Flask(__name__)

@app.route("/")
def index():
    music_files = scan_music()
    html = """
    <h1>Mac Pro Music Server</h1>
    <form method='post' action='/play'>
    <select name='file'>
    {% for f in files %}
      <option value='{{f}}'>{{f.split('/')[-1]}}</option>
    {% endfor %}
    </select>
    <button type='submit'>Play</button>
    </form>
    """
    return render_template_string(html, files=music_files)

@app.route("/play", methods=["POST"])
def play():
    file_path = request.form['file']
    threading.Thread(target=play_audio, args=(file_path,)).start()
    return redirect("/")

# --- MAIN ---
if __name__ == "__main__":
    threading.Thread(target=scheduled_sync_and_scan, daemon=True).start()
    speak("Mac Pro music server is online.")
    app.run(host="0.0.0.0", port=5000)
