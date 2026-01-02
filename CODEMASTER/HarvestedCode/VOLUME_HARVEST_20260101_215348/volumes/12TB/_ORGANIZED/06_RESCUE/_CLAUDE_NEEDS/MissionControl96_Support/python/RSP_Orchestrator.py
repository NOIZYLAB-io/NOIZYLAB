#!/usr/bin/env python3
"""
RSP Orchestrator Core — Everything Always
Author: RSP
Purpose: Hand of God Sweep + Mission Control status updates
"""

import os, json, hashlib, datetime
from pathlib import Path

AUTHOR = "RSP"
VAULT_ROOT = str(Path.home() / "FishMusicVault")
LOG_DIR = str(Path.home() / "RSP/Logs")
STATUS_JSON = str(Path.home() / "RSP/NW_MissionControl/dashboard/status.json")

def ts(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def update_status(section, state, message):
    Path(STATUS_JSON).parent.mkdir(parents=True, exist_ok=True)
    try:
        data = json.load(open(STATUS_JSON))
    except: data = {"author": AUTHOR}
    data["author"] = AUTHOR; data["timestamp"] = ts()
    data[section] = {"state": state, "message": message}
    json.dump(data, open(STATUS_JSON,"w"), indent=2)

def sha256_file(path):
    h = hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def sweep_vault(root):
    update_status("vault","WORKING","Hand of God Sweep running…")
    seen, dupes, empties = {}, [], []
    for dirpath, dirs, files in os.walk(root):
        if not dirs and not files:
            empties.append(dirpath)
        for f in files:
            path = os.path.join(dirpath,f)
            try:
                digest = sha256_file(path)
                if digest in seen:
                    os.remove(path)
                    dupes.append(path)
                else:
                    seen[digest] = path
            except Exception as e:
                pass
    for folder in sorted(empties, key=lambda p: len(p), reverse=True):
        try: os.rmdir(folder)
        except: pass
    report = {
        "author": AUTHOR,
        "timestamp": ts(),
        "dupes_removed": len(dupes),
        "empties_removed": len(empties)
    }
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    json.dump(report, open(Path(LOG_DIR)/f"sweep_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json","w"), indent=2)
    update_status("vault","OK",f"Sweep complete — {len(dupes)} dupes, {len(empties)} empties removed")

def capsule_log(event, details=None):
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    log = {"author": AUTHOR,"timestamp": ts(),"event": event,"details": details or {}}
    json.dump(log, open(Path(LOG_DIR)/f"capsule_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json","w"), indent=2)

def main():
    update_status("nw","WORKING","NOIZYWIND orchestrator starting")
    capsule_log("orchestrator_start")
    sweep_vault(VAULT_ROOT)
    # Hooks for Planar, mastering, sync
    update_status("nw","OK","NOIZYWIND orchestration complete")
    capsule_log("orchestrator_complete")

if __name__=="__main__":
    main()
