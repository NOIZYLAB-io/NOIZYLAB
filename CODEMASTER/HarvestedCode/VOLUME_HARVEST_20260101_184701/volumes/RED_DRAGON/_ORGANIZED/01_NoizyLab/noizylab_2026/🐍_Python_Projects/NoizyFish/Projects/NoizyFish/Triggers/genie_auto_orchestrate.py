import subprocess
import sys
import re
import time

# Genie Mode: Check, Alert, and Auto-Orchestrate

def check_interface(interface, expected_ip):
    result = subprocess.getoutput(f"ifconfig {interface}")
    ip_match = re.search(r"inet (\d+\.\d+\.\d+\.\d+)", result)
    if ip_match and ip_match.group(1) == expected_ip:
        print(f"✅ {interface} has IP {expected_ip}")
        return True
    else:
        print(f"❌ {interface} does not have IP {expected_ip}. Current config:\n{result}")
        return False

def ping_test(target_ip):
    print(f"Pinging {target_ip}...")
    result = subprocess.run(["ping", "-c", "2", target_ip])
    if result.returncode == 0:
        print(f"✅ Ping to {target_ip} successful.")
        return True
    else:
        print(f"❌ Ping to {target_ip} failed.")
        return False

def auto_orchestrate():
    interfaces = ["bridge0", "en4", "en5", "Thunderbolt Bridge"]
    expected_ip = "192.168.2.1"
    found = False
    for iface in interfaces:
        try:
            if check_interface(iface, expected_ip):
                found = True
                break
        except Exception:
            continue
    if not found:
        print("\nACTION REQUIRED: Set Thunderbolt Bridge/Ethernet to IP 192.168.2.1 in System Settings > Network, then rerun this script.")
        sys.exit(1)
    # Test ping to Mac Pro
    while True:
        if ping_test("192.168.2.2"):
            print("✅ Connectivity restored! Running Genie Mode orchestration...")
            break
        else:
            print("Waiting for connectivity... Retrying in 30 seconds.")
            time.sleep(30)
    # Auto-run Genie Mode orchestration scripts
    scripts = [
        "~/NoizyFish/Triggers/genie_suite.py",
        "~/NoizyFish/Triggers/genie_super_duper_control.py",
        "~/NoizyFish/Triggers/slablink_scanner.py",
        "~/NoizyFish/Triggers/Noizy_Genie_SlabLink.py"
    ]
    for script in scripts:
        path = subprocess.os.path.expanduser(script)
        print(f"Launching {path}...")
        subprocess.Popen(["python3", path])
    print("🧞‍♂️ Genie Mode: All automations and rituals have been launched.")

if __name__ == "__main__":
    auto_orchestrate()
