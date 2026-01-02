#!/usr/bin/env python3
"""
SOCIAL_ALIGNMENT.py
Opens Facebook recovery/login-identify links for a list of emails/phones,
logs the attempts to fb_recovery_attempts.csv, and spaces openings so you don't blast
Facebook with requests.
"""

import webbrowser
import time
import csv
from datetime import datetime
from pathlib import Path
import sys


# === CONFIGURATION ===
# List logins in 'fb_logins.txt' (one per line) or use the default list below.
DEFAULT_LOGINS = [
    "rp@fishmusicinc.com",
    "rsplowman@icloud.com",
    "rsp@noizyfish.com",
    "info@fishmusicinc.com",
]

PROJECT_DIR = Path(__file__).parent
LOGINS_FILE = PROJECT_DIR / "fb_logins.txt"
LOG_FILE = PROJECT_DIR / "fb_recovery_attempts.csv"
DELAY_BETWEEN = 3.0  # seconds between tab openings
ENDPOINTS = {
    "identify": "https://www.facebook.com/login/identify?ctx=recover&email={q}",
    "two_factor": "https://www.facebook.com/two_step_verification/two_factor/?flow=two_factor_login&next",
    "messenger": "https://www.facebook.com/messages/t/"
}
# === END CONFIGURATION ===

def log_attempt(login, endpoint_name, url):
    """Log each recovery attempt to the CSV file."""
    first_time = not LOG_FILE.exists()
    try:
        with LOG_FILE.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if first_time:
                writer.writerow(["timestamp_iso", "login", "endpoint", "url"])
            # Use timezone-aware UTC
            writer.writerow([datetime.now().astimezone().isoformat(), login, endpoint_name, url])
    except Exception as e:
        print(f"[ERROR] Could not write to log file: {e}", file=sys.stderr)

def open_for_login(login):
    """Open all recovery endpoints for a single login."""
    for name, template in ENDPOINTS.items():
        url = template.format(q=login) if "{q}" in template else template
        try:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Opening {name} for {login}: {url}")
            webbrowser.open_new_tab(url)
            log_attempt(login, name, url)
        except Exception as e:
            print(f"[ERROR] Could not open {url} for {login}: {e}", file=sys.stderr)
        time.sleep(DELAY_BETWEEN)

def load_logins():
    """Load logins from file or use default list."""
    if LOGINS_FILE.exists():
        try:
            with LOGINS_FILE.open("r", encoding="utf-8") as f:
                logins = [line.strip() for line in f if line.strip()]
            if not logins:
                print(f"[WARNING] 'fb_logins.txt' is empty. Using default logins.")
                return DEFAULT_LOGINS
            return logins
        except Exception as e:
            print(f"[ERROR] Could not read logins file: {e}. Using default logins.", file=sys.stderr)
            return DEFAULT_LOGINS
    return DEFAULT_LOGINS

def validate_login(login):
    """Basic validation for email or phone."""
    if "@" in login or login.startswith("+") or login.isdigit():
        return True
    print(f"[WARNING] Skipping invalid login: {login}", file=sys.stderr)
    return False

def main():
    print("\n=== SOCIAL ALIGNMENT ===\nLaunching tabs and logging attempts.")
    logins = load_logins()
    # Deduplicate and sort logins for alignment
    valid_logins = sorted(set(l for l in logins if validate_login(l)))
    if not valid_logins:
        print("[ERROR] No valid logins to process. Exiting.", file=sys.stderr)
        return
    print(f"Processing {len(valid_logins)} unique accounts:")
    for login in valid_logins:
        print(f" - {login}")
    for login in valid_logins:
        open_for_login(login)
    print(f"\nDone. Log written to: {LOG_FILE}")
    print("All recovery searches completed.\n")

if __name__ == "__main__":
    main()
