#!/usr/bin/env python3
"""
NoizyMesh Fleet Handshake + Discovery
Scans all known hosts, verifies ping, logs latency,
and writes a JSON status file used by Mission Control.
"""

import os, platform, json, subprocess
from pathlib import Path
from datetime import datetime

# ---- Configuration ----
FLEET = {
    "MacStudio":     {"ip": "10.0.0.25", "role": "Commander"},   # Current machine (you)
    "MacPro":        {"ip": "10.0.0.130", "role": "AudioCore"},  # Detected on network
    "HP_OMEN":       {"ip": "10.0.0.140", "role": "Compute"},    # Detected on network
    "Dell_7779":     {"ip": "10.0.0.151", "role": "Diagnostics"} # Detected on network
}

REPORT = Path("fleet_status.json")
PING_COUNT = 2
PING_TIMEOUT = 1000  # ms

# ---- Helpers ----
def ping_host(ip):
    """Ping a host once or twice depending on OS, return latency in ms or None."""
    system = platform.system().lower()
    if system.startswith("win"):
        cmd = ["ping", "-n", str(PING_COUNT), "-w", str(PING_TIMEOUT), ip]
    else:
        cmd = ["ping", "-c", str(PING_COUNT), "-W", "1", ip]

    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        for line in out.splitlines():
            if "time=" in line:
                t = line.split("time=")[1].split()[0]
                return float(t.replace("ms", "").strip())
    except subprocess.CalledProcessError:
        return None
    return None


def handshake():
    print("🔭  Starting Fleet Handshake Scan…")
    status = {"timestamp": datetime.now().isoformat(), "nodes": []}

    for name, meta in FLEET.items():
        ip = meta["ip"]
        role = meta["role"]
        print(f"⏳  Checking {name:<10} ({ip}) …", end="")
        latency = ping_host(ip)
        if latency is not None:
            print(f" ✅  {latency:.1f} ms")
            meta.update({"reachable": True, "latency_ms": latency})
        else:
            print(" ❌  unreachable")
            meta.update({"reachable": False, "latency_ms": None})
        status["nodes"].append(meta)

    REPORT.write_text(json.dumps(status, indent=2))
    print(f"\n📄  Wrote report → {REPORT.resolve()}")
    return status


def summary_table(status):
    print("\n🛰  Fleet Summary\n" + "-" * 40)
    for node in status["nodes"]:
        ok = "🟢" if node["reachable"] else "🔴"
        print(f"{ok} {node['role']:<12} {node['ip']:<15} {node['latency_ms'] or '--':>6}")
    print("-" * 40)
    online = [n for n in status["nodes"] if n["reachable"]]
    print(f"{len(online)}/{len(status['nodes'])} nodes online.")


# ---- Main Routine ----
if __name__ == "__main__":
    os.system("cls" if platform.system().lower().startswith("win") else "clear")
    data = handshake()
    summary_table(data)
    print("Complete.  Ready for Fleet Restart.")
    # All audio/voice triggers removed for safety