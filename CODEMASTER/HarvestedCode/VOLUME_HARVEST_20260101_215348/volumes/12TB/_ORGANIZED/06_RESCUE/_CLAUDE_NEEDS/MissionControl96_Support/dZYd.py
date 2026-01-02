import yaml
import datetime

LOG_PATH = "/Users/rsp_ms/NoizyFish_Aquarium/Cosmic_Airline/cockpit_fallback_log.yaml"

# Utility to log each step with timestamp and error

def log_step(step, device, status, error=None):
    with open(LOG_PATH, "r") as f:
        data = yaml.safe_load(f)
    for entry in data["steps"]:
        if entry["step"] == step and entry["device"] == device:
            entry["status"] = status
            entry["timestamp"] = datetime.datetime.now().isoformat()
            entry["error"] = error or ""
    with open(LOG_PATH, "w") as f:
        yaml.safe_dump(data, f)

# Example usage:
# log_step("Prep Install Media", "OMEN", "completed")
# log_step("BIOS/UEFI Rituals", "Inspiron", "error", error="TPM not found")
