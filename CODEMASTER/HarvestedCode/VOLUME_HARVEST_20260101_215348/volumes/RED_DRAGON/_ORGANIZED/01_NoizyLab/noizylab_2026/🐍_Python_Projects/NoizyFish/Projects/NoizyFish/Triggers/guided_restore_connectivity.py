import subprocess
import sys
import re
import time

def prompt(msg):
    input(f"\n{msg} Press Enter to continue...")

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

def guided_fix():
    print("Step 1: Physical Connection")
    print("Ensure Thunderbolt/Ethernet cable is securely connected on both Macs.")
    prompt("Check cables and ports.")

    print("Step 2: Network Configuration")
    print("On BOTH Macs, go to System Settings > Network.")
    print("Set Thunderbolt Bridge (or Ethernet) to static IPs:")
    print("  Mac Studio: 192.168.2.1")
    print("  Mac Pro:    192.168.2.2")
    print("Subnet mask: 255.255.255.0")
    prompt("Set IPs and subnet mask.")

    print("Step 3: Interface Verification")
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
    prompt("If you changed settings, reboot both Macs now.")

    print("Step 4: Firewall & Sharing")
    print("On BOTH Macs, temporarily disable firewalls for testing.")
    print("On Mac Pro, enable 'Remote Login' (SSH) in System Settings > Sharing.")
    prompt("Adjust firewall and sharing settings.")

    print("Step 5: Test Connectivity")
    print("Testing ping to Mac Pro (192.168.2.2)...")
    if ping_test("192.168.2.2"):
        print("✅ Ping successful! Network is up.")
        print("Testing SSH to Mac Pro...")
        ssh_result = subprocess.run(["ssh", "RSP@192.168.2.2", "hostname"])
        if ssh_result.returncode == 0:
            print("✅ SSH successful! Full connectivity restored.")
        else:
            print("❌ SSH failed. Check SSH settings and user permissions on Mac Pro.")
    else:
        print("❌ Ping failed. Double-check all previous steps.")
    print("If you still have issues, try different cables, ports, or reboot both Macs again.")

if __name__ == "__main__":
    guided_fix()
