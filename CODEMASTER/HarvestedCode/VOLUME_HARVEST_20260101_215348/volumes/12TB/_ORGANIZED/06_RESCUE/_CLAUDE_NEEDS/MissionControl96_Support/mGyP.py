#!/usr/bin/env python3


import subprocess
import datetime
import os
import threading
import time
import smtplib
from email.message import EmailMessage

# --- CONFIG ---
SLAB_NAME = "Mac Pro"
SLAB_IPS = ["192.168.2.2", "192.168.3.2", "macpro.local"]
SLAB_USERS = ["rob"]
RITUAL_COMMAND = "bash ~/NoizyFish/CreativeMode/activate.sh"
LOG_PATH = "/Users/rsp_ms/NoizyFish/Logs/slablink.log"
SYNC_PATHS = ["~/Documents/Important"]
VOICE_FEEDBACK = True
ALERT_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASS = "your_password"

# --- UTILS ---
def ensure_log_dir():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

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
    for ip in SLAB_IPS:
        for user in SLAB_USERS:
            print(f"🔍 Probing {SLAB_NAME} at {ip} for user {user}...")
            if ping(ip):
                print(f"✅ Link detected at {ip}. Initiating ritual...")
                if ssh_trigger(ip, user):
                    msg = f"✅ Ritual executed on {SLAB_NAME} via {ip}."
                    print(msg)
                    log_event(msg)
                    speak("Mac Pro link active. Ritual complete.", voice="Samantha", volume=50)
                    sync_files(ip, user)
                    remote_screen_share(ip)
                    av_control("volup")
                    homekit_control("lights", "on")
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
        speak("Mac Pro unreachable. Fallback mode engaged.", voice="Victoria", volume=25)
        send_email_alert("Genie Ritual Failure", msg)

if __name__ == "__main__":
    genie_mode()
    # Example: schedule_ritual(3600, genie_mode)  # Run every hour
