#!/usr/bin/env python3
import os, sys, subprocess, venv, json, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV = ROOT/".venv"
PY = VENV/("Scripts/python.exe" if os.name=="nt" else "bin/python")
ENV = ROOT/".env"
REQ = ROOT/"requirements.txt"

def env_dict():
    d={}
    if ENV.exists():
        for line in ENV.read_text().splitlines():
            if not line.strip() or line.strip().startswith("#"): continue
            k,v = line.split("=",1)
            d[k.strip()] = v.strip()
    return d

def ensure_venv():
    if not VENV.exists():
        print("🧩 creating venv…")
        venv.create(VENV, with_pip=True)
    subprocess.run([str(PY), "-m", "pip", "install", "-U", "pip", "setuptools", "wheel"], check=False)
    if REQ.exists():
        subprocess.run([str(PY), "-m", "pip", "install", "-r", str(REQ)], check=False)

def start_services():
    # Start the core API (only on control if desired) and heartbeat everywhere
    e = env_dict()
    role = e.get("ROLE","worker").lower()
    if role == "control":
        subprocess.Popen([str(PY), "services/core.py"], cwd=str(ROOT))
        time.sleep(0.5)
    subprocess.Popen([str(PY), "services/heartbeat.py"], cwd=str(ROOT))
    print("✅ services started")

if __name__=="__main__":
    ensure_venv()
    start_services()
