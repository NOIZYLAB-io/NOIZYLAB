#!/usr/bin/env python3
"""
Genie Mode Orchestration Suite
- Flask API for remote control
- Dashboard integration
- Ritual scheduling
- Networked slab control
- Voice & visual feedback
- Journal & backup automation
"""
import subprocess
import datetime
import schedule
import time
import threading
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

PLANAR_INPUTS = {
    "StudioSlab": "HDMI1",
    "PowerSlab": "HDMI2",
    "VisionSlab": "HDMI3"
}
SLABS = {
    "StudioSlab": "192.168.2.1",
    "PowerSlab": "192.168.2.2",
    "VisionSlab": "192.168.2.3"
}
LOG_PATH = "/Users/rsp_ms/NoizyFish/Logs/genie_suite.log"
JOURNAL_PATH = "/Users/rsp_ms/NoizyFish/Memory/slab_journal.json"
VOICE_FEEDBACK = True

# --- Rituals ---
def switch_input(slab_name):
    input_port = PLANAR_INPUTS.get(slab_name)
    cec_map = {"HDMI1": "10:00", "HDMI2": "20:00", "HDMI3": "30:00"}
    cec_code = cec_map.get(input_port)
    if not cec_code:
        log_event(f"❌ Unknown input for {slab_name}")
        speak(f"Unknown input for {slab_name}")
        return
    command = f"echo 'tx 10:82:{cec_code}' | cec-client"
    subprocess.run(command, shell=True)
    msg = f"🧞 {slab_name} now channeling {input_port}"
    log_event(msg)
    speak(msg)

def broadcast_ritual(ritual, recipients):
    for recipient in recipients:
        command = f"ssh RSP@{recipient} '~/NoizyFish/Triggers/{ritual}.py'"
        subprocess.run(command, shell=True)
        log_event(f"🔊 Ritual '{ritual}' broadcast to {recipient}")
        speak(f"Ritual {ritual} sent to {recipient}")

def capture_memory():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"/Users/rsp_ms/NoizyFish/Legacy/memory_{timestamp}.aiff"
    subprocess.run(["say", "Tell me something you want remembered."])
    subprocess.run(["rec", path])
    log_event(f"🧠 Memory captured: {path}")
    speak("Memory captured.")

def backup_journal():
    subprocess.run(["zip", "-r", "/Users/rsp_ms/NoizyFish/Legacy/Capsule_2025.zip", JOURNAL_PATH])
    log_event("Journal backed up to Capsule_2025.zip")

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as log:
        log.write(f"{timestamp} {message}\n")

def speak(message):
    if VOICE_FEEDBACK:
        try:
            subprocess.run(["say", message])
        except Exception:
            pass

# --- Flask API ---
@app.route("/slablink/status", methods=["GET"])
def slablink_status():
    with open(LOG_PATH) as f:
        status = f.read()
    return jsonify({"status": status})

@app.route("/slablink/trigger", methods=["POST"])
def slablink_trigger():
    ritual = request.args.get("ritual")
    if ritual:
        broadcast_ritual(ritual, SLABS.values())
        return jsonify({"result": f"Ritual {ritual} triggered."})
    return jsonify({"error": "No ritual specified."}), 400

@app.route("/")
def dashboard():
    with open(LOG_PATH) as f:
        status_lines = f.readlines()
    return render_template("dashboard.html", status=status_lines)

# --- Scheduling ---
def run_ambient_overlay():
    broadcast_ritual("ambient_healing", SLABS.values())
    log_event("Ambient overlay ritual scheduled.")
    speak("Ambient overlay ritual running.")

schedule.every().sunday.at("21:00").do(run_ambient_overlay)

def scheduler_thread():
    while True:
        schedule.run_pending()
        time.sleep(30)

# --- Main ---
if __name__ == "__main__":
    threading.Thread(target=scheduler_thread, daemon=True).start()
    app.run(host="0.0.0.0", port=5050, debug=True)
