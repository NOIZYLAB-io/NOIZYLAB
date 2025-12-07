import yaml
import os
from datetime import datetime

LOG_PATH = "/Users/rsp_ms/NoizyFish_Aquarium/Cosmic_Airline/cockpit_fallback_log.yaml"

# Simple dashboard to monitor D-LINK and all device activity

def load_log():
    with open(LOG_PATH) as f:
        return yaml.safe_load(f)

def print_dashboard():
    log = load_log()
    print("\n=== D-LINK Dashboard ===")
    for entry in log["steps"]:
        device = entry["device"]
        step = entry["step"]
        status = entry["status"]
        timestamp = entry["timestamp"]
        error = entry["error"]
        print(f"[{device}] {step}: {status} @ {timestamp} {f'ERROR: {error}' if error else ''}")

if __name__ == "__main__":
    print_dashboard()
