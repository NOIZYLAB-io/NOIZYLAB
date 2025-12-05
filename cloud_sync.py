import json
import os
import time

SYNC_FILE = "./noizy_sync.json"


def sync_push(data: dict):
    payload = {
        "updated": time.time(),
        "data": data
    }
    with open(SYNC_FILE, "w") as f:
        json.dump(payload, f, indent=2)
    return {"status": "ok", "written": True}


def sync_pull():
    if not os.path.exists(SYNC_FILE):
        return {"exists": False, "data": {}}

    with open(SYNC_FILE, "r") as f:
        data = json.load(f)
    return {"exists": True, "data": data}

