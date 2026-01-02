#!/usr/bin/env python3

import subprocess
import datetime
import os

# 🧞 Ritual Identity
SLAB_NAME = "Mac Pro"
SLAB_IPS = ["192.168.2.2", "192.168.3.2", "macpro.local"]  # TB Bridge, AX88179A, Bonjour fallback
RITUAL_COMMAND = "bash ~/NoizyFish/CreativeMode/activate.sh"
LOG_PATH = "/Users/rsp_ms/NoizyFish/Logs/slablink.log"
VOICE_FEEDBACK = True

# Ensure log directory exists
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# 🕰️ Timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 🧠 Ping Ritual
def ping(ip):
    try:
        subprocess.run(["ping", "-c", "1", "-W", "1", ip], check=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

# 🔗 SSH Ritual
def ssh_trigger(ip):
    try:
        subprocess.run(["ssh", f"rob@{ip}", RITUAL_COMMAND], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# 📜 Ritual Log
def log_event(message):
    with open(LOG_PATH, "a") as log:
        log.write(f"{timestamp} {message}\n")

# 🔊 Voice Ritual
def speak(message):
    if VOICE_FEEDBACK:
        subprocess.run(["say", message])

# 🧞‍♂️ SlabLink Beacon Ritual Begins
print("🧞‍♂️ Genie Mode Activated — Seeking SlabLink...")

for ip in SLAB_IPS:
    print(f"🔍 Probing {SLAB_NAME} at {ip}...")
    if ping(ip):
        print(f"✅ Link detected at {ip}. Initiating ritual...")
        if ssh_trigger(ip):
            msg = f"✅ Ritual executed on {SLAB_NAME} via {ip}."
            print(msg)
            log_event(msg)
            speak("Mac Pro link active. Ritual complete.")
            break
        else:
            print(f"⚠️ SSH failed for {ip}.")
    else:
        print(f"❌ No response from {ip}.")

else:
    msg = f"❌ All slab links failed. Fallback mode engaged."
    print(msg)
    log_event(msg)
    speak("Mac Pro unreachable. Fallback mode engaged.")
