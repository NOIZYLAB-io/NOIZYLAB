import os
import json
from pathlib import Path
import subprocess

def log_capsule(entry):
    CAPSULE_LOG = str(Path.home() / "RSP/Logs/capsule_chain_log.jsonl")
    os.makedirs(os.path.dirname(CAPSULE_LOG), exist_ok=True)
    with open(CAPSULE_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
    # Show notification on macOS
    os.system(f"osascript -e 'display notification \"Capsule {entry['capsule']} logged: {entry['status']}\" with title \"NOIZYLAB\"'")
    print(f"Capsule {entry['capsule']} logged: {entry['status']}")
    # Trigger overlay pulse (HTML file)
    overlay_html = str(Path.home() / "RSP/Overlays/planar_pulse.html")
    os.makedirs(os.path.dirname(overlay_html), exist_ok=True)
    with open(overlay_html, "w") as f:
        f.write("""
        <body style='background-color: #00FF00; animation: pulse 1s infinite;'>
          <style>
            @keyframes pulse {
              0% { background-color: #00FF00; }
              50% { background-color: #33FF33; }
              100% { background-color: #00FF00; }
            }
          </style>
        </body>
        """)
    # Optionally open overlay in browser
    subprocess.run(["open", overlay_html])

# Example usage:
entry = {
  "slab": "Planar",
  "capsule": "OverlayPulse",
  "mood": "resonant",
  "timestamp": "2025-09-30T01:39:00",
  "status": "success"
}
log_capsule(entry)
