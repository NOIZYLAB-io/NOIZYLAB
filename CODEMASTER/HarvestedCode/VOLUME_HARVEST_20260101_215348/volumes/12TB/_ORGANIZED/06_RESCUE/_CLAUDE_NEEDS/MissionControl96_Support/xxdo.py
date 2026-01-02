#!/usr/bin/env python3
"""
fb_recover_helper.py
Opens Facebook recovery/login-identify links for a list of emails/phones,
logs the attempts to recover_log.txt, and spaces openings so you don't blast
Facebook with requests.
"""

import webbrowser
import time
import csv
from datetime import datetime
from pathlib import Path
import sys

# === CONFIG ===
# Add all emails / phone numbers you want to test below.
LOGINS = [
    "rp@fishmusicinc.com",
    "rsplowman@icloud.com",
    "rsp@noizyfish.com",
    "info@fishmusicinc.com",
]

# Where to save the log
LOG_FILE = Path.home() / "fb_recovery_attempts.csv"

# Delay between opening tabs (seconds). Increase to be gentler.
DELAY_BETWEEN = 3.0

# Facebook endpoints to open for each login
ENDPOINTS = {
    "identify": "https://www.facebook.com/login/identify?ctx=recover&email={q}",
    "two_factor": "https://www.facebook.com/two_step_verification/two_factor/?flow=two_factor_login&next",
    "messenger": "https://www.facebook.com/messages/t/"
}

# === END CONFIG ===

def log_attempt(login, endpoint_name, url):
    first_time = not LOG_FILE.exists()
    with LOG_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if first_time:
            writer.writerow(["timestamp_iso", "login", "endpoint", "url"])
        writer.writerow([datetime.utcnow().isoformat(), login, endpoint_name, url])

def open_for_login(login):
    for name, template in ENDPOINTS.items():
        # Only fill endpoint if it takes a query param
        if "{q}" in template:
            url = template.format(q=login)
        else:
            url = template
        try:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Opening {name} for {login}: {url}")
            webbrowser.open_new_tab(url)
            log_attempt(login, name, url)
        except Exception as e:
            print(f"Error opening {url} for {login}: {e}", file=sys.stderr)
        time.sleep(DELAY_BETWEEN)

def main():
    print("FB Recovery Helper — launching tabs and logging attempts.")
    for login in LOGINS:
        open_for_login(login)
    print(f"Done. Log written to: {LOG_FILE}")
    print("All recovery searches completed.")

if __name__ == "__main__":
    main()
