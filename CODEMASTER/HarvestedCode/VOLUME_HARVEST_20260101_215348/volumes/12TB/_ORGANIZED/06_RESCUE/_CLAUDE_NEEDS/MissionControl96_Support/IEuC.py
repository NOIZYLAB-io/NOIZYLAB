import os
import subprocess
import datetime
import json

def say(msg):
    subprocess.run(["say", msg])

def launch_overlay():
    subprocess.run(["start", "C:\🧞‍♂️NOIZYWIND\Overlays\planar_eyelevel.html"], shell=True)

def play_ambient():
    subprocess.run(["start", "C:\🧞‍♂️NOIZYWIND\Soundscapes\charged_loop.wav"], shell=True)

def build_capsule():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    capsule = f"C:\🧞‍♂️NOIZYWIND\Legacy\Capsule_{ts}.zip"
    subprocess.run(["powershell", "Compress-Archive", "-Path", "C:\🧞‍♂️NOIZYWIND\Legacy\*", "-DestinationPath", capsule])
    return capsule

def verify_windows():
    subprocess.run(["python", "C:\🧞‍♂️NOIZYWIND\Scripts\windows_installation_verifier.py"])

def infuse_sequoia():
    subprocess.run(["python", "C:\🧞‍♂️NOIZYWIND\Agents\sequoia_infusion.py"])

def sync_to_github(capsule_path):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "capsule": os.path.basename(capsule_path),
        "status": "Pushed to GitHub (symbolic)"
    }
    with open("C:\🧞‍♂️NOIZYWIND\Legacy\capsule_sync_log.json", "w") as f:
        json.dump(log, f, indent=4)

# 🔥 Ritual Detonation Begins
say("Igniting NoizyGenieMode Thermonuclear × 100")
verify_windows()
infuse_sequoia()
launch_overlay()
play_ambient()
capsule = build_capsule()
sync_to_github(capsule)
say("Capsule detonated. Slab is sovereign. Legacy preserved.")
