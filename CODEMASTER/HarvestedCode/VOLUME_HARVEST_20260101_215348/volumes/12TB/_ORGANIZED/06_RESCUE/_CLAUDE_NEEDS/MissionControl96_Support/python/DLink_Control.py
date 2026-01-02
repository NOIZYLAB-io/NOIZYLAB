
from typing import List, Dict, Optional
import time

_DEVICES = [
    {"id": "DL-001", "ip": "192.168.0.1", "model": "DIR-882", "name": "Main Router"},
    {"id": "DL-002", "ip": "192.168.0.2", "model": "DAP-1610", "name": "Living Room AP"},
]

_CLIENTS = {
    "DL-001": [
        {"mac": "AA:BB:CC:DD:EE:01", "hostname": "MacStudio", "ip": "192.168.0.101", "signal": -45},
        {"mac": "AA:BB:CC:DD:EE:02", "hostname": "HP-OMEN", "ip": "192.168.0.102", "signal": -60},
    ],
    "DL-002": [
        {"mac": "AA:BB:CC:DD:EE:03", "hostname": "iPhone", "ip": "192.168.0.150", "signal": -55},
    ],
}

def discover_devices() -> List[Dict]:
    return _DEVICES

def get_device(device_id: str) -> Optional[Dict]:
    return next((d for d in _DEVICES if d["id"] == device_id), None)

def get_device_status(device_id: str) -> Dict:
    t = int(time.time())
    return {"online": True, "uptime": f"{t//3600}h", "cpu": (t % 20) + 10, "mem": (t % 40) + 30, "firmware": "1.20", "wan": "up"}

def list_clients(device_id: str) -> List[Dict]:
    return _CLIENTS.get(device_id, [])

def reboot_device(device_id: str) -> Dict:
    return {"ok": True, "message": f"Reboot initiated for {device_id}"}

def set_config(device_id: str, changes: Dict, dry_run: bool = False) -> Dict:
    return {"ok": True, "applied": changes, "dry_run": dry_run}
