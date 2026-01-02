#!/usr/bin/env python3
"""
flush_rogers.py
Flushes DNS cache, restarts network interfaces, and checks internet connectivity.
Designed for Mac systems using Rogers internet.
"""

import subprocess
import sys
import time

def run_cmd(cmd, sudo=False):
    if sudo:
        cmd = ["sudo"] + cmd
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"$ {' '.join(cmd)}\n{result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {' '.join(cmd)}:\n{e.stderr.strip()}", file=sys.stderr)

def flush_dns():
    print("Flushing DNS cache...")
    run_cmd(["dscacheutil", "-flushcache"], sudo=True)
    run_cmd(["killall", "-HUP", "mDNSResponder"], sudo=True)

def restart_network(interface="en0"):
    print(f"Restarting network interface {interface}...")
    run_cmd(["ifconfig", interface, "down"], sudo=True)
    sleep_duration = 2  # seconds
    time.sleep(sleep_duration)
    run_cmd(["ifconfig", interface, "up"], sudo=True)

def check_connectivity():
    print("Checking internet connectivity...")
    run_cmd(["networkQuality"])
    run_cmd(["ping", "-c", "4", "google.com"])

def main():
    flush_dns()
    restart_network()
    check_connectivity()
    print("✅ Rogers pipeline flushed and checked.")

if __name__ == "__main__":
    main()