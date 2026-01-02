#!/usr/bin/env python3
# MissionControl96: Everything Setup Script
import os, sys, subprocess, textwrap, secrets
from pathlib import Path

PROJECT_ROOT = Path.cwd()
VENV_DIR = PROJECT_ROOT / ".venv"
REQ_FILE = PROJECT_ROOT / "requirements.txt"
ENV_FILE = PROJECT_ROOT / ".env"

# ... (reuse FILES dict and logic from previous setup scripts) ...
# For brevity, this script can be extended to include all features: MFA/TOTP, HMAC config, topology, scheduler, etc.

def gen_secret():
    return secrets.token_urlsafe(32)

FILES = {
    # Add all files and content from previous setup scripts here
    # (DLink_Control.py, requirements.txt, .env, dashboard files, etc.)
}

def ensure_dirs():
    for path in FILES.keys():
        if path.suffix:
            path.parent.mkdir(parents=True, exist_ok=True)

def write_env():
    if ENV_FILE.exists():
        print("[KEEP] .env exists")
        return
    env = [
        f"DASHBOARD_SECRET={gen_secret()}",
        f"JWT_SECRET={gen_secret()}",
        "ADMIN_USER=admin",
        "ADMIN_PASS=change-me",
        "API_TOKEN=",
        "DEVICE_CACHE_TTL=10",
        "STATUS_CACHE_TTL=2",
        f"AUDIT_LOG_PATH={(PROJECT_ROOT / 'audit.log').as_posix()}",
    ]
    ENV_FILE.write_text("\n".join(env) + "\n", encoding="utf-8")
    print("[WRITE] .env")

def write_files():
    for path, content in FILES.items():
        if content is None:
            continue
        print(f"{'[WRITE]' if not path.exists() else '[UPDATE]'} {path.relative_to(PROJECT_ROOT)}")
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

def show_next():
    print("\n[ENV] To run the app:")
    print(f"source {VENV_DIR}/bin/activate")
    print("export FLASK_APP=dlink_dashboard/app.py")
    print("export FLASK_ENV=development")
    print("flask run")
    print("\n[PROD] Gunicorn example:")
    print(f"source {VENV_DIR}/bin/activate && gunicorn -w 2 -b 0.0.0.0:5000 'dlink_dashboard.app:app'")

def main():
    print("[START] Everything Setup for MissionControl96 Dashboard")
    ensure_dirs()
    write_files()
    write_env()
    create_venv()
    install_requirements()
    show_next()
    print("[DONE] Ready. Change ADMIN_PASS in .env before production use.")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with code {e.returncode}")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
