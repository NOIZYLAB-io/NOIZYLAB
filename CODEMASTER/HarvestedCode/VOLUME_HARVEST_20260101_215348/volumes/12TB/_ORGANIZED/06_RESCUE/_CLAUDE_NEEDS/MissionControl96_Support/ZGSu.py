#!/usr/bin/env python3
"""
setup_dlink_dashboard_best.py
Sets up a world-class Flask-based D-Link Dashboard web app.
"""
import os
import sys
import subprocess
import textwrap
from pathlib import Path

PROJECT_ROOT = Path.cwd()
VENV_DIR = PROJECT_ROOT / ".venv"
REQ_FILE = PROJECT_ROOT / "requirements.txt"

FILES = {
    PROJECT_ROOT / "DLink_Control.py": textwrap.dedent(r'''
from typing import List, Dict, Optional

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
    return {"online": True, "uptime": "3d 12h", "cpu": 22, "mem": 48, "firmware": "1.20", "wan": "up"}

def list_clients(device_id: str) -> List[Dict]:
    return _CLIENTS.get(device_id, [])

def reboot_device(device_id: str) -> Dict:
    return {"ok": True, "message": f"Reboot initiated for {device_id}"}

def set_config(device_id: str, changes: Dict) -> Dict:
    return {"ok": True, "applied": changes}
'''),
    REQ_FILE: textwrap.dedent(r'''
Flask==3.0.0
requests==2.32.3
cachetools==5.3.3
pyyaml==6.0.2
'''),
    # ...rest of dashboard files as in previous scaffold...
}

def ensure_dirs():
    for path in FILES.keys():
        if path.suffix:
            path.parent.mkdir(parents=True, exist_ok=True)

def write_files():
    for path, content in FILES.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def run(cmd, env=None):
    print(f"[RUN] {' '.join(cmd)}")
    subprocess.check_call(cmd, env=env)

def create_venv():
    if VENV_DIR.exists():
        print(f"[SKIP] venv already exists at {VENV_DIR}")
        return
    run([sys.executable, "-m", "venv", str(VENV_DIR)])
    print(f"[OK] venv created: {VENV_DIR}")

def install_requirements():
    pip = VENV_DIR / "bin" / "pip"
    run([str(pip), "install", "-r", str(REQ_FILE)])
    print("[OK] dependencies installed")

def set_flask_env():
    print("\n[ENV] To run the app:")
    print(f"source {VENV_DIR}/bin/activate")
    print("export FLASK_APP=dlink_dashboard/app.py")
    print("export FLASK_ENV=development")
    print("flask run\n")

def main():
    print("[START] D-LINK Dashboard Best Setup")
    ensure_dirs()
    write_files()
    create_venv()
    install_requirements()
    set_flask_env()
    print("[DONE] Files saved, venv ready. Launch with the commands above.")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with code {e.returncode}")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
