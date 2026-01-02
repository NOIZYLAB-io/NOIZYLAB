import os
import subprocess
import time
import json
from pathlib import Path
import speech_recognition as sr

# --- CONFIGURATION ---
CAPSULE_CHAIN = [
    "validate_code",
    "auto_save",
    "execute",
    "fallback_if_error",
    "git_sync",
    "log_emotion",
    "pulse_overlay"
]
SLABS = {
    "NOIZYWIND": {"status": "online", "overlay": "blue"},
    "MacPro": {"status": "listening", "overlay": "green"},
    "Planar": {"status": "awaiting", "overlay": "blue"}
}
STATUS_JSON = str(Path.home() / "RSP/NW_MissionControl/dashboard/status.json")
CAPSULE_LOG = str(Path.home() / "RSP/Logs/capsule_chain_log.jsonl")
VOICE_SESSION_LOG = str(Path.home() / "RSP/Logs/noizylab_voice_session.jsonl")
FILE_PATH = "/Users/rsp_ms/Documents/rituals/my_script.py"
RUNTIME = "python3"
GIT_ENABLED = True
GIT_COMMIT_MSG = "🔁 Ritual Executed: Capsule Clean — Synced to NOIZYLAB Grid"

# --- UTILITY FUNCTIONS ---
def speak(message, voice="Kate Premium"):
    os.system(f'say -v "{voice}" "{message}"')

def log_capsule(capsule, mood, slab, status):
    entry = {
        "capsule": capsule,
        "mood": mood,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "slab": slab,
        "status": status
    }
    os.makedirs(os.path.dirname(CAPSULE_LOG), exist_ok=True)
    with open(CAPSULE_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
    update_dashboard(entry)
    speak(f"Capsule {capsule} status: {status}, mood: {mood}", "Kate Premium")

def update_dashboard(entry):
    try:
        if os.path.exists(STATUS_JSON):
            with open(STATUS_JSON) as f:
                status = json.load(f)
        else:
            status = {}
        status[entry["slab"]] = {"state": entry["status"], "message": f"Capsule: {entry['capsule']}, Mood: {entry['mood']}"}
        status["timestamp"] = entry["timestamp"]
        with open(STATUS_JSON, "w") as f:
            json.dump(status, f, indent=2)
    except Exception as e:
        speak(f"Dashboard update error: {e}", "Kate Premium")

def validate_code():
    try:
        subprocess.check_output([RUNTIME, "-m", "py_compile", FILE_PATH])
        return True
    except subprocess.CalledProcessError:
        return False

def auto_save():
    return True

def execute():
    try:
        subprocess.run([RUNTIME, FILE_PATH])
        return True
    except Exception:
        return False

def fallback_if_error():
    speak("Error detected. Launching fallback overlay.", "Kate Premium")
    subprocess.run(["code", FILE_PATH])
    return True

def git_sync():
    try:
        subprocess.run(["git", "add", FILE_PATH])
        subprocess.run(["git", "commit", "-m", GIT_COMMIT_MSG])
        subprocess.run(["git", "push"])
        return True
    except Exception:
        return False

def log_emotion(mood):
    speak(f"Logging mood: {mood}", "Kate Premium")
    return True

def pulse_overlay(slab):
    speak(f"Pulsing overlay for {slab}", "Kate Premium")
    return True

def run_capsule_chain(capsule_name, mood, slab):
    status = "success"
    for step in CAPSULE_CHAIN:
        if step == "validate_code":
            if not validate_code():
                status = "error"
                fallback_if_error()
                break
        elif step == "auto_save":
            auto_save()
        elif step == "execute":
            if not execute():
                status = "error"
                fallback_if_error()
                break
        elif step == "git_sync":
            git_sync()
        elif step == "log_emotion":
            log_emotion(mood)
        elif step == "pulse_overlay":
            pulse_overlay(slab)
    log_capsule(capsule_name, mood, slab, status)

# --- VOICE CONTROL (optional) ---
def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎙️ Listening for capsule command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"🧠 Heard: {command}")
        with open(VOICE_SESSION_LOG, "a") as f:
            f.write(json.dumps({"timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"), "command": command}) + "\n")
        return command
    except sr.UnknownValueError:
        speak("I didn't catch that. Try again.", "Kate Premium")
        return None

def main():
    speak("NOIZYLAB Orchestrator online. Awaiting capsule command.", "Kate Premium")
    while True:
        command = listen_for_command()
        if command:
            if "run capsule" in command:
                run_capsule_chain("NoizyAutoRun", "energized", "NOIZYWIND")
            elif "shutdown" in command:
                speak("Shutting down NOIZYLAB Orchestrator. Ritual complete.", "Kate Premium")
                break
            else:
                speak("Unknown command. Try again.", "Kate Premium")

if __name__ == "__main__":
    main()
