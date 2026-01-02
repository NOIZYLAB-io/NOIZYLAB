#!/usr/bin/env python3
"""
autoregister.py
Sequential Command #9 – NoizyBrain Auto-Thread Registration
Links new or existing devices into the active Fleet Mesh
so each node (Mac Studio, OMEN, DGS, etc.) is aware of others.
"""

import os
import json
import time
import uuid
import socket
import platform
import requests
import datetime

# === CONFIG ===
FLEET_HUB_URL = "https://fleet.noizy.ai/status"
THREAD_API_URL = "https://fleet.noizy.ai/thread"
THREADS_FILE = "/Volumes/NOIZYWIN/NoizyBrain/fleet_threads.json"
LINK_LOG = "/Volumes/NOIZYWIN/NoizyBrain/autoregister.log"

def log(text):
    """Append to log file"""
    entry = f"[{datetime.datetime.utcnow().isoformat()}] {text}\n"
    with open(LINK_LOG, "a") as f:
        f.write(entry)
    print(entry.strip())

def load_fleet():
    """Get current Fleet data from the Hub"""
    try:
        r = requests.get(FLEET_HUB_URL, timeout=10)
        return r.json()
    except Exception as e:
        log(f"⚠️ Failed to fetch Fleet status: {e}")
        return {}

def link_nodes(a, b):
    """Send link info to the Fleet Hub"""
    payload = {
        "thread_id": str(uuid.uuid4()),
        "source": a,
        "target": b,
        "created": datetime.datetime.utcnow().isoformat(),
        "status": "active"
    }
    try:
        r = requests.post(THREAD_API_URL, json=payload, timeout=10)
        if r.status_code == 200:
            log(f"🔗 Linked {a} ⇄ {b}")
        else:
            log(f"❌ Failed linking {a} to {b}: {r.status_code}")
    except Exception as e:
        log(f"❌ Error linking {a} to {b}: {e}")

def thread_all_nodes():
    """Auto-thread all Fleet nodes logically"""
    fleet = load_fleet()
    hosts = list(fleet.keys())
    if not hosts:
        log("⚠️ No fleet nodes found.")
        return

    log(f"🧠 Threading {len(hosts)} Fleet nodes...")
    connections = []

    for i, src in enumerate(hosts):
        for dst in hosts[i + 1:]:
            link_nodes(src, dst)
            connections.append((src, dst))
            time.sleep(1)  # gentle pacing for Cloudflare

    with open(THREADS_FILE, "w") as f:
        json.dump({"threads": connections}, f, indent=2)

    log(f"✅ Auto-threading complete: {len(connections)} connections built.")

def main():
    log("🚀 AutoRegister System initializing...")
    thread_all_nodes()

if __name__ == "__main__":
    main()

