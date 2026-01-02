from __future__ import annotations
import os, json, socket
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT/".env", override=True)

def env(k, default=None): return os.getenv(k, default)
def node_name(): return env("NODE_NAME") or socket.gethostname()
def node_priority(): return int(env("NODE_PRIORITY","999"))

def role():
    r=(env("ROLE","worker") or "worker").lower()
    return "control" if r=="control" else "worker"

def mission_api():
    return env("MISSION_API","http://127.0.0.1:8010")

def read_json(p: Path, default):
    try: return json.loads(p.read_text())
    except: return default
