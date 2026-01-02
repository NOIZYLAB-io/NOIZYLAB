#!/usr/bin/env python3
"""
Webador → GoDaddy migration helper.

Steps:
1. Log into Webador and fetch domain transfer (EPP) code.
2. Save EPP code locally.
3. (Optional) Scrape site content for reference.
4. Guide user to GoDaddy transfer portal with EPP code prepped.
"""

import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "~/Documents/NoizyFish/Webador_migrate/output")).expanduser()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
EPP_FILE = OUTPUT_DIR / "transfer_codes.txt"

WEBADOR_EMAIL = os.getenv("WEBADOR_EMAIL")
WEBADOR_PASS = os.getenv("WEBADOR_PASS")

def main():
    if not WEBADOR_EMAIL or not WEBADOR_PASS:
        print("⚠️ Please set WEBADOR_EMAIL and WEBADOR_PASS environment variables.")
        return

    print("🚀 Launching Chrome…")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.webador.com/v2/dashboard")

    # --- Login ---
    print("🔑 Logging into Webador…")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys(WEBADOR_EMAIL)
    driver.find_element(By.NAME, "password").send_keys(WEBADOR_PASS)
    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    time.sleep(5)

    # --- Navigate to Domain Settings ---
    print("🌐 Searching for EPP/Auth code… (you may need to click manually if captcha/2FA shows)")
    try:
        # This selector will likely need tweaking depending on your dashboard layout
        epp_element = driver.find_element(By.XPATH, "//code[contains(@class,'auth-code')]")
        epp_code = epp_element.text.strip()
    except Exception:
        epp_code = None

    if epp_code:
        with open(EPP_FILE, "w") as f:
            f.write(epp_code + "\n")
        print(f"✅ EPP code saved to {EPP_FILE}")
    else:
        print("⚠️ Could not auto-detect code. Check Webador Domain Settings manually.")

    print("👉 Next: Go to https://ca.godaddy.com/domains/transfer and paste your EPP code.")
    driver.quit()

if __name__ == "__main__":
    main()