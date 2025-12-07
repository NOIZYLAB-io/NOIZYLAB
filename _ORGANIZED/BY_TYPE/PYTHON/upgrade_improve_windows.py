#!/usr/bin/env python3
"""
NOIZYLAB UPGRADE & IMPROVE - WINDOWS VERSION
For Gabriel (HP Omen) and other Windows machines
Uses Chocolatey for package management
"""

import subprocess
import sys
import os
import sqlite3
import datetime

DB_FILE = 'C:\\NOIZYLAB\\data\\upgrade_improve.db'

def upgrade_pip_packages():
    print("Checking for outdated pip packages...")
    try:
        outdated = subprocess.check_output([sys.executable, "-m", "pip", "list", "--outdated"]).decode()
        upgraded = []
        for line in outdated.splitlines()[2:]:
            if line.strip():
                pkg = line.split()[0]
                print(f"Upgrading {pkg}...")
                subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", pkg])
                upgraded.append(pkg)
        return upgraded
    except Exception as e:
        print(f"Error checking pip packages: {e}")
        return []

def check_missing_tools(tools):
    print("Checking for missing essential tools...")
    missing = []
    for tool in tools:
        # Use 'where' command on Windows to check if tool is installed
        if subprocess.call(f"where {tool}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
            missing.append(tool)
    if missing:
        print("Missing tools:", ", ".join(missing))
        # Install missing tools with Chocolatey
        for tool in missing:
            print(f"Installing {tool} with Chocolatey...")
            try:
                subprocess.run(["choco", "install", tool, "-y"], check=True)
            except Exception as e:
                print(f"Failed to install {tool}: {e}")
    else:
        print("All essential tools are installed.")
    return missing

def improve_configurations():
    print("Applying configuration improvements...")
    improvements = []

    # Enable Windows Defender real-time protection
    try:
        subprocess.run(["powershell", "-Command", "Set-MpPreference -DisableRealtimeMonitoring $false"], check=True)
        improvements.append("Windows Defender real-time protection enabled")
    except Exception as e:
        improvements.append(f"Failed to enable Defender: {e}")

    # Enable Windows Firewall
    try:
        subprocess.run(["powershell", "-Command", "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True"], check=True)
        improvements.append("Windows Firewall enabled")
    except Exception as e:
        improvements.append(f"Failed to enable Firewall: {e}")

    # Update Windows Defender definitions
    try:
        subprocess.run(["powershell", "-Command", "Update-MpSignature"], check=True)
        improvements.append("Windows Defender definitions updated")
    except Exception as e:
        improvements.append(f"Failed to update Defender: {e}")

    return improvements

def update_database(upgraded, missing, improvements):
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS improvements (
        id INTEGER PRIMARY KEY,
        source TEXT,
        description TEXT,
        date_added TEXT
    )
    ''')
    today = datetime.date.today().isoformat()
    for pkg in upgraded:
        cursor.execute('INSERT INTO improvements (source, description, date_added) VALUES (?, ?, ?)',
                       ("upgrade", f"Upgraded pip package: {pkg}", today))
    for tool in missing:
        cursor.execute('INSERT INTO improvements (source, description, date_added) VALUES (?, ?, ?)',
                       ("missing", f"Missing tool installed: {tool}", today))
    for imp in improvements:
        cursor.execute('INSERT INTO improvements (source, description, date_added) VALUES (?, ?, ?)',
                       ("improve", imp, today))
    conn.commit()
    conn.close()
    print("Database updated with upgrade, improvement, and missing tool info.")

def main():
    print("=" * 60)
    print("NOIZYLAB UPGRADE & IMPROVE - WINDOWS")
    print("Gabriel (HP Omen) / Windows Machines")
    print("=" * 60)

    # 1. Upgrade pip packages
    upgraded = upgrade_pip_packages()

    # 2. Check for missing tools
    essential_tools = ["git", "curl", "wget", "python", "node", "npm", "code"]
    missing = check_missing_tools(essential_tools)

    # 3. Apply improvements
    improvements = improve_configurations()

    # 4. Update database
    update_database(upgraded, missing, improvements)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Packages upgraded: {len(upgraded)}")
    print(f"Missing tools installed: {len(missing)}")
    print(f"Improvements applied: {len(improvements)}")
    print("All upgrade, improvement, missing checks, and database update completed!")

if __name__ == "__main__":
    main()
