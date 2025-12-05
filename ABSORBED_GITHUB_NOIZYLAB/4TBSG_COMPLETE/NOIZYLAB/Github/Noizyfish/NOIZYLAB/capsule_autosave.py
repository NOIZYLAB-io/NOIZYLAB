import os
import datetime
import subprocess
import json

def build_capsule():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    capsule = f"C:\🧞‍♂️NOIZYWIND\Legacy\Capsule_{ts}.zip"
    subprocess.run(["powershell", "Compress-Archive", "-Path", "C:\🧞‍♂️NOIZYWIND\Legacy\*", "-DestinationPath", capsule])
    return capsule

def log_capsule(capsule_path):
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "capsule": os.path.basename(capsule_path),
        "status": "AutoSaved",
        "agent": "Archivist",
        "mood": "Focused"
    }
    with open("C:\🧞‍♂️NOIZYWIND\Legacy\autosave_log.json", "a") as f:
        f.write(json.dumps(log) + "\n")

capsule = build_capsule()
log_capsule(capsule)
