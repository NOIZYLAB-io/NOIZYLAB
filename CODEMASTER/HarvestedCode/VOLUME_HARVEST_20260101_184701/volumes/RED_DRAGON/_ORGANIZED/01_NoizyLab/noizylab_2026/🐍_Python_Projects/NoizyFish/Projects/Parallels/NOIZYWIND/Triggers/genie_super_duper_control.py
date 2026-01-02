#!/usr/bin/env python3
"""
Genie Super Duper Control Script
- Switch HDMI inputs (CEC)
- Query device status
- Broadcast rituals
- Log actions
- Voice feedback
"""
import subprocess
import datetime
import sys

# Input mapping for Planar/Slabs
PLANAR_INPUTS = {
    "StudioSlab": "HDMI1",
    "PowerSlab": "HDMI2",
    "VisionSlab": "HDMI3"
}

LOG_PATH = "/Users/rsp_ms/NoizyFish/Logs/genie_control.log"
VOICE_FEEDBACK = True

# --- HDMI-CEC Control ---
def switch_input(slab_name):
    input_port = PLANAR_INPUTS.get(slab_name)
    if not input_port:
        log_event(f"❌ Unknown slab: {slab_name}")
        speak(f"Unknown slab: {slab_name}")
        return
    # Example CEC command mapping
    cec_map = {"HDMI1": "10:00", "HDMI2": "20:00", "HDMI3": "30:00"}
    cec_code = cec_map.get(input_port)
    if not cec_code:
        log_event(f"❌ Unknown input port: {input_port}")
        speak(f"Unknown input port: {input_port}")
        return
    command = f"echo 'tx 10:82:{cec_code}' | cec-client"
    subprocess.run(command, shell=True)
    msg = f"🧞 Planar slab now channeling {slab_name} via {input_port}"
    log_event(msg)
    speak(msg)

# --- Ritual Broadcast ---
def broadcast_ritual(ritual, recipients):
    for recipient in recipients:
        command = f"ssh RSP@{recipient} '~/NoizyFish/Triggers/{ritual}.py'"
        subprocess.run(command, shell=True)
        log_event(f"🔊 Ritual '{ritual}' broadcast to {recipient}")
        speak(f"Ritual {ritual} sent to {recipient}")

# --- Device Status ---
def get_status():
    result = subprocess.getoutput("cec-client -s -d 1")
    log_event("Device status queried.")
    print(result)
    return result

# --- Logging ---
def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as log:
        log.write(f"{timestamp} {message}\n")

# --- Voice Feedback ---
def speak(message):
    if VOICE_FEEDBACK:
        try:
            subprocess.run(["say", message])
        except Exception:
            pass

# --- Main CLI ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: genie_control.py [switch|broadcast|status] ...")
        sys.exit(1)
    action = sys.argv[1]
    if action == "switch" and len(sys.argv) > 2:
        switch_input(sys.argv[2])
    elif action == "broadcast" and len(sys.argv) > 3:
        ritual = sys.argv[2]
        recipients = sys.argv[3:]
        broadcast_ritual(ritual, recipients)
    elif action == "status":
        get_status()
    else:
        print("Unknown command or missing arguments.")
