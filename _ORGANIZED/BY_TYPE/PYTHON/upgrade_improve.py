import subprocess
import sys
import os
import sqlite3
import datetime

DB_FILE = '/Users/m2ultra/NOIZYLAB/data/upgrade_improve.db'

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

def check_system_updates():
    print("Checking for system updates...")
    updated = []
    if sys.platform == "darwin":
        # MacOS - use brew
        try:
            subprocess.run(["brew", "update"], capture_output=True)
            result = subprocess.run(["brew", "upgrade"], capture_output=True)
            updated.append("System packages upgraded (brew)")
        except Exception as e:
            print(f"Brew update error: {e}")
    elif sys.platform.startswith("linux"):
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "upgrade", "-y"])
        updated.append("System packages upgraded (apt)")
    return updated

def check_missing_tools(tools):
    print("Checking for missing essential tools...")
    missing = []
    for tool in tools:
        if subprocess.call(f"which {tool}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
            missing.append(tool)
    if missing:
        print("Missing tools:", ", ".join(missing))
    else:
        print("All essential tools are installed.")
    return missing

def improve_configurations():
    print("Applying configuration improvements...")
    improvements = []
    if sys.platform == "darwin":
        # MacOS improvements
        try:
            # Enable firewall
            subprocess.run(["sudo", "/usr/libexec/ApplicationFirewall/socketfilterfw", "--setglobalstate", "on"], capture_output=True)
            improvements.append("Firewall enabled (macOS)")
        except:
            pass
    elif sys.platform.startswith("linux"):
        subprocess.run(["sudo", "ufw", "enable"])
        improvements.append("Firewall enabled (ufw)")
    return improvements

def update_database(upgraded, updated, missing, improvements):
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
    for item in updated:
        cursor.execute('INSERT INTO improvements (source, description, date_added) VALUES (?, ?, ?)',
                       ("upgrade", item, today))
    for tool in missing:
        cursor.execute('INSERT INTO improvements (source, description, date_added) VALUES (?, ?, ?)',
                       ("missing", f"Missing tool: {tool}", today))
    for imp in improvements:
        cursor.execute('INSERT INTO improvements (source, description, date_added) VALUES (?, ?, ?)',
                       ("improve", imp, today))
    conn.commit()
    conn.close()
    print("Database updated with upgrade, improvement, and missing tool info.")

def main():
    print("=" * 60)
    print("NOIZYLAB UPGRADE & IMPROVE SYSTEM")
    print("=" * 60)

    # 1. Upgrade
    upgraded = upgrade_pip_packages()
    updated = check_system_updates()

    # 2. Check for missing upgrades/improvements
    essential_tools = ["git", "curl", "wget", "python3", "node", "npm", "brew", "claude"]
    missing = check_missing_tools(essential_tools)

    # 3. Improve
    improvements = improve_configurations()

    # 4. Update database
    update_database(upgraded, updated, missing, improvements)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Packages upgraded: {len(upgraded)}")
    print(f"System updates: {len(updated)}")
    print(f"Missing tools: {len(missing)}")
    print(f"Improvements applied: {len(improvements)}")
    print("All upgrade, improvement, missing checks, and database update completed!")

if __name__ == "__main__":
    main()
