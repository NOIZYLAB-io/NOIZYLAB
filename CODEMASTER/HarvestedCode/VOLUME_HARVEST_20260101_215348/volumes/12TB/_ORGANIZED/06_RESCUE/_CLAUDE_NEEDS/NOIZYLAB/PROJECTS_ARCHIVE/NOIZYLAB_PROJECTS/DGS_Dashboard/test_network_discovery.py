#!/usr/bin/env python3
"""
Quick Network Discovery Test
Test the network discovery functionality independently
"""

import socket
import subprocess
import sys


def test_network_discovery():
    """Test network discovery functionality"""
    print("🔍 Testing Network Discovery...")
    print("=" * 50)

    # Test basic network connectivity
    network_base = "10.0.0"
    devices_found = []

    print(f"🌐 Scanning network: {network_base}.1-50")
    print("-" * 30)

    for i in range(1, 51):
        ip = f"{network_base}.{i}"
        try:
            # Quick ping test
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1000", ip], capture_output=True, timeout=2
            )
            if result.returncode == 0:
                # Device found, try to get hostname
                hostname = "Unknown"
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except:
                    pass

                device_type = "Unknown Device"
                if ip.endswith(".1"):
                    device_type = "🌐 Router/Switch"
                elif "mac" in hostname.lower():
                    device_type = "🖥️ Mac Computer"
                elif any(x in hostname.lower() for x in ["win", "pc", "desktop"]):
                    device_type = "💻 Windows PC"
                elif "dell" in hostname.lower():
                    device_type = "💻 Dell Computer"
                elif "hp" in hostname.lower():
                    device_type = "🎮 HP Computer"

                devices_found.append(
                    {"ip": ip, "hostname": hostname, "type": device_type}
                )

                print(f"✅ {ip:<15} | {hostname:<25} | {device_type}")

        except Exception as e:
            pass

    print("-" * 30)
    print(f"🎯 Found {len(devices_found)} active devices")
    print("=" * 50)

    if devices_found:
        print("\n📊 DEVICE SUMMARY:")
        for device in devices_found:
            print(f"  • {device['ip']} - {device['type']} ({device['hostname']})")
    else:
        print("⚠️ No devices found. Check network connectivity.")

    return devices_found


if __name__ == "__main__":
    devices = test_network_discovery()

    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        import json

        print("\n" + json.dumps(devices, indent=2))
