from __future__ import annotations
import time, platform, psutil, requests, socket
from .util import env, mission_api, node_name, node_priority, role

API = mission_api().rstrip("/")
HB = int(env("HEARTBEAT_SECONDS","30"))

def payload():
    return {
        "node": node_name(),
        "priority": node_priority(),
        "role": role(),
        "os": platform.system(),
        "cpu": psutil.cpu_percent(interval=None),
        "mem": psutil.virtual_memory().percent,
        "ip": socket.gethostbyname(socket.gethostname()),
        "ts": time.time()
    }

def send():
    url = f"{API}/api/fleet/heartbeat"
    try:
        requests.post(url, json={"node": payload()["node"], "ip": payload()["ip"]}, timeout=2)
    except Exception:
        pass
    # Optional telemetry push if you exposed such an endpoint
    url2 = f"{API}/telemetry/push"
    try:
        requests.post(url2, json={"topic":"heartbeat","payload":payload()}, timeout=2)
    except Exception:
        pass

if __name__=="__main__":
    print(f"❤️ heartbeat to {API} every {HB}s")
    while True:
        send()
        time.sleep(HB)
