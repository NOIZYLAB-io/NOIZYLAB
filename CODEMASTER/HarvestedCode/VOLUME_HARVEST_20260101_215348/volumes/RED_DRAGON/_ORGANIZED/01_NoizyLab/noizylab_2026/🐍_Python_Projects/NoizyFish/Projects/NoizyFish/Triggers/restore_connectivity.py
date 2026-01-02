import subprocess
import sys
import re

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

def main():
    # Check Thunderbolt Bridge or Ethernet
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
        print("Please set your Thunderbolt Bridge or Ethernet to IP 192.168.2.1 in System Settings > Network.")
        sys.exit(1)
    # Test ping to Mac Pro
    ping_test("192.168.2.2")
    print("If ping fails, check cables, IP settings, and reboot both Macs.")

if __name__ == "__main__":
    main()
