import subprocess
import os
import json
from datetime import datetime

def trigger_ritual(name):
    script = os.path.expanduser(f"~/GitHub/noizywind-ritual-pack/scripts/{name}.bat")
    if os.path.exists(script):
        subprocess.run([script])
    else:
        print(f"Ritual script {script} not found.")

def overlay_launch(name):
    overlay = os.path.expanduser(f"~/GitHub/noizywind-ritual-pack/overlays/{name}.html")
    if os.path.exists(overlay):
        subprocess.run(["open", overlay])
    else:
        print(f"Overlay {overlay} not found.")

def ambient_play(filename):
    sound = os.path.expanduser(f"~/GitHub/noizywind-ritual-pack/assets/{filename}")
    if os.path.exists(sound):
        subprocess.run(["ffplay", "-nodisp", "-autoexit", sound])
    else:
        print(f"Ambient sound {sound} not found.")

def agent_log(message):
    log = {
        "timestamp": datetime.now().isoformat(),
        "message": message
    }
    log_path = os.path.expanduser(f"~/GitHub/noizywind-ritual-pack/legacy/Ritual_Log_{datetime.now().strftime('%Y%m%d')}.json")
    with open(log_path, "w") as f:
        json.dump(log, f, indent=4)

def capsule_push_to_github(filename):
    capsule = os.path.expanduser(f"~/GitHub/noizywind-ritual-pack/legacy/{filename}")
    if os.path.exists(capsule):
        subprocess.run(["git", "add", capsule])
        subprocess.run(["git", "commit", "-m", f"Add {filename} capsule"])
        subprocess.run(["git", "push"])
    else:
        print(f"Capsule {capsule} not found.")

def voice_say(message):
    subprocess.run(["say", message])

# Example usage
if __name__ == "__main__":
    trigger_ritual("build_capsule")
    overlay_launch("planar_eyelevel")
    ambient_play("charged_loop.wav")
    agent_log("Archivist preserved 3 memories")
    capsule_push_to_github("Capsule_20250929.zip")
    voice_say("Capsule detonated. Legacy preserved. Slab is sovereign.")
