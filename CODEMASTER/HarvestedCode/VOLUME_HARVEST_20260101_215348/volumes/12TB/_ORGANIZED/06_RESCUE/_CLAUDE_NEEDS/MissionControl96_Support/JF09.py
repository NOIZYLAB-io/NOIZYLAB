import os
import json
from pathlib import Path

def log_capsule(entry):
    CAPSULE_LOG = str(Path.home() / "RSP/Logs/capsule_chain_log.jsonl")
    os.makedirs(os.path.dirname(CAPSULE_LOG), exist_ok=True)
    with open(CAPSULE_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
    # Show notification on macOS
    os.system(f"osascript -e 'display notification \"Capsule {entry['capsule']} logged: {entry['status']}\" with title \"NOIZYLAB\"'")
    print(f"Capsule {entry['capsule']} logged: {entry['status']}")

# Example usage:
entry = {
  "slab": "Planar",
  "capsule": "OverlayPulse",
  "mood": "resonant",
  "timestamp": "2025-09-30T01:39:00",
  "status": "success"
}
log_capsule(entry)
