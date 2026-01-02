#!/usr/bin/env python3


import subprocess
import datetime
import os
import threading
import time
import smtplib
from email.message import EmailMessage
from flask import Flask
import audioread
import ffmpeg
import shutil

import importlib.util

# --- CONFIG LOADING ---
CONFIG_PATH = os.path.expanduser("~/NoizyFish/Triggers/genie_config.py")
def load_config():
    spec = importlib.util.spec_from_file_location("genie_config", CONFIG_PATH)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config

config = load_config()

# --- CONFIG ---
SLAB_NAME = "Mac Pro"
SLAB_IPS = ["192.168.2.2", "192.168.3.2", "macpro.local"]
SLAB_USERS = ["RSP"]
RITUAL_COMMAND = "bash ~/NoizyFish/CreativeMode/activate.sh"
LOG_PATH = "/Users/rsp_ms/NoizyFish/Logs/slablink.log"
SYNC_PATHS = ["~/Documents/Important"]
VOICE_FEEDBACK = True
ALERT_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASS = "your_password"

SAMPLE_DIR = "/Users/rob/Samples"
SYNC_DIRS = ["/Users/rob/NoizyFish/Shared"]
SAMPLE_COMMAND = "afplay"  # macOS audio player, replace with your sampler app if needed
SAMPLE_FILES = ["kick.wav", "snare.wav", "ambient.mp3"]  # Add your sample files here
SCHEDULE_INTERVAL = 1800  # Sample every 30 minutes

# --- UTILS ---
def ensure_log_dir():
    os.makedirs(os.path.dirname(config.LOG_PATH), exist_ok=True)

def log_event(message):
    ensure_log_dir()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as log:
        log.write(f"{timestamp} {message}\n")

def speak(message, voice=None, volume=None):
    if VOICE_FEEDBACK:
        cmd = ["say"]
        if voice:
            cmd += ["-v", voice]
        if volume:
            subprocess.run(["osascript", "-e", f"set volume output volume {volume}"])
        cmd += [message]
        subprocess.run(cmd)

def send_email_alert(subject, body):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = ALERT_EMAIL
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
    except Exception as e:
        log_event(f"Email alert failed: {e}")

def ping(ip):
    try:
        subprocess.run(["ping", "-c", "1", "-W", "1", ip], check=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def ssh_trigger(ip, user):
    try:
        subprocess.run(["ssh", f"{user}@{ip}", RITUAL_COMMAND], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def sync_files(ip, user):
    for path in SYNC_PATHS:
        subprocess.run(["rsync", "-avz", path, f"{user}@{ip}:~/sync/"], check=False)

def remote_screen_share(ip):
    subprocess.run(["open", f"vnc://{ip}"])

def av_control(command):
    subprocess.run(["echo", command, "|", "/opt/homebrew/bin/cec-client", "-s", "-d", "1"], shell=True)

def homekit_control(device, action):
    # Placeholder for HomeKit integration
    log_event(f"HomeKit: {device} -> {action}")

def sync_files():
    for sync_dir in SYNC_DIRS:
        subprocess.run(["rsync", "-avz", sync_dir, SAMPLE_DIR], check=False)
        log_event(f"Synced {sync_dir} to {SAMPLE_DIR}")

def play_sample(sample_file):
    sample_path = os.path.join(SAMPLE_DIR, sample_file)
    if os.path.exists(sample_path):
        subprocess.run([SAMPLE_COMMAND, sample_path])
        log_event(f"Played sample: {sample_file}")
        speak(f"Sample {sample_file} played.")
    else:
        log_event(f"Sample not found: {sample_file}")
        speak(f"Sample {sample_file} not found.", voice="Victoria", volume=30)

def scheduled_sampler():
    while True:
        for sample in SAMPLE_FILES:
            play_sample(sample)
            time.sleep(2)  # Short pause between samples
        sync_files()
        speak("Sampler cycle complete. Waiting for next schedule.")
        time.sleep(SCHEDULE_INTERVAL)

def remote_trigger(sample_file):
    play_sample(sample_file)
    speak(f"Remote trigger: {sample_file} played.")

def start_sampler():
    threading.Thread(target=scheduled_sampler, daemon=True).start()
    log_event("Sampler started.")
    speak("Mac Pro sound sampler and workhorse is running.")

# --- SCHEDULER ---
def schedule_ritual(interval_sec, func, *args):
    def wrapper():
        while True:
            func(*args)
            time.sleep(interval_sec)
    t = threading.Thread(target=wrapper, daemon=True)
    t.start()

# --- MAIN RITUAL ---
def genie_mode():
    print("🧞‍♂️ Genie Mode Activated — Seeking SlabLink...")
    for ip in config.SLAB_IPS:
        for user in config.SLAB_USERS:
            print(f"🔍 Probing {config.SLAB_NAME} at {ip} for user {user}...")
            if ping(ip):
                print(f"✅ Link detected at {ip}. Initiating ritual...")
                if ssh_trigger(ip, user):
                    msg = f"✅ Ritual executed on {config.SLAB_NAME} via {ip}."
                    print(msg)
                    log_event(msg)
                    speak(f"{config.SLAB_NAME} link active. Ritual complete.", voice="Samantha", volume=50)
                    sync_files(ip, user)
                    remote_screen_share(ip)
                    for av_cmd in getattr(config, "AV_COMMANDS", []):
                        av_control(av_cmd)
                    for device in getattr(config, "HOMEKIT_DEVICES", []):
                        homekit_control(device, "on")
                    send_email_alert("Genie Ritual Success", msg)
                    return
                else:
                    print(f"⚠️ SSH failed for {ip}.")
            else:
                print(f"❌ No response from {ip}.")
    else:
        msg = f"❌ All slab links failed. Fallback mode engaged."
        print(msg)
        log_event(msg)
        speak(f"{config.SLAB_NAME} unreachable. Fallback mode engaged.", voice="Victoria", volume=25)
        send_email_alert("Genie Ritual Failure", msg)

app = Flask(__name__)

@app.route('/genie_mode', methods=['POST'])
def trigger_genie_mode():
    threading.Thread(target=genie_mode).start()
    return "Genie mode ritual has been triggered.", 202

if __name__ == "__main__":
    interactive_setup()
    genie_mode()
    start_sampler()
    # Example: schedule_ritual(getattr(config, "SCHEDULE_INTERVAL", 3600), genie_mode)  # Run every hour

# (Already provided above, just ensure Flask is installed and run the script)

# To batch normalize WAV files, run this in your terminal:
# for f in /Users/rsp_ms/Samples/*.wav; do sox "$f" "normalized_$f" norm; done

tell application "Logic Pro"
    open "Macintosh HD:Users:rob:Music:Logic:MyProject.logicx"
    play
end tell

import shutil, subprocess
total, used, free = shutil.disk_usage("/")
if free < 100*1024*1024*1024:  # Less than 100GB
    subprocess.run(["say", "Warning: Low disk space!"])
pip install Flask
