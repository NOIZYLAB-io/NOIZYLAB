# Dashboard Sync Module
# Syncs OMEN_Sentinel status and logs to NOIZYGRID dashboard

import requests
import os
from datetime import datetime

DASHBOARD_URL = "http://localhost:5000/api/status"
LOG_PATH = "C:/OMEN_Sentinel/logs/omen_agent.log"

# === UTILS ===
def sync_logs():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            logs = f.read()
        payload = {"logs": logs, "timestamp": datetime.now().isoformat()}
        try:
            requests.post(DASHBOARD_URL, json=payload)
            print("Logs synced to dashboard.")
        except Exception as e:
            print(f"Dashboard log sync failed: {e}")
    else:
        print("No logs found to sync.")

if __name__ == "__main__":
    sync_logs()
