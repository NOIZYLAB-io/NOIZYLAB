#!/usr/bin/env python3
import os, socket, time, requests

NODE = socket.gethostname()
API = os.getenv("FLEET_URL", "http://127.0.0.1:8010/api/fleet/heartbeat")

def public_ip():
    try:
        return requests.get("https://api.ipify.org").text.strip()
    except Exception:
        return "127.0.0.1"

def heartbeat():
    payload = {"node": NODE, "ip": public_ip()}
    try:
        requests.post(API, json=payload, timeout=1.5)
    except Exception:
        pass

if __name__ == "__main__":
    while True:
        heartbeat()
        time.sleep(30)
