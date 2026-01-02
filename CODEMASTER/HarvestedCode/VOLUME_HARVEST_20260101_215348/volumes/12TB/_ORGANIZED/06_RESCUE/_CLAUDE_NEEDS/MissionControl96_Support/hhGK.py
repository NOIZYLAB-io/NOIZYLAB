#!/usr/bin/env python3
import os, sys, subprocess, textwrap, secrets, shutil, time, json
from pathlib import Path

PROJECT_ROOT = Path.cwd()
VENV_DIR = PROJECT_ROOT / ".venv"
REQ_FILE = PROJECT_ROOT / "requirements.txt"
ENV_FILE = PROJECT_ROOT / ".env"
AUDIT_LOG = PROJECT_ROOT / "audit.log"
CONFIG_SNAPSHOTS = PROJECT_ROOT / "config_snapshots"

# --- Generate secrets ---
def gen_secret(): return secrets.token_urlsafe(32)

# --- Mythic modules scaffold ---
FILES = {
    PROJECT_ROOT / "dlink_dashboard" / "app.py": textwrap.dedent("""
        ...existing code for app.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "routes" / "topology.py": textwrap.dedent("""
        ...existing code for topology.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "routes" / "devices.py": textwrap.dedent("""
        ...existing code for devices.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "routes" / "metrics.py": textwrap.dedent("""
        ...existing code for metrics.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "routes" / "auth.py": textwrap.dedent("""
        ...existing code for auth.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "routes" / "scheduler.py": textwrap.dedent("""
        ...existing code for scheduler.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "health" / "sentinel.py": textwrap.dedent("""
        ...existing code for sentinel.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "utils" / "audit.py": textwrap.dedent("""
        ...existing code for audit.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "config.py": textwrap.dedent("""
        ...existing code for config.py...
    """),
    PROJECT_ROOT / "dlink_dashboard" / "templates" / "topology.html": textwrap.dedent("""
        ...existing code for topology.html...
    """),
    PROJECT_ROOT / "Dockerfile": textwrap.dedent("""
        ...existing code for Dockerfile...
    """),
    PROJECT_ROOT / "docker-compose.yml": textwrap.dedent("""
        ...existing code for docker-compose.yml...
    """),
    REQ_FILE: textwrap.dedent("""
        Flask==3.0.0
        Flask-JWT-Extended==4.6.0
        Flask-Limiter==3.7.0
        Flask-Sock==0.7.0
        python-dotenv==1.0.1
        requests==2.32.3
        cachetools==5.3.3
        pyyaml==6.0.2
        itsdangerous==2.2.0
        gunicorn==22.0.0
        qrcode==7.4.2
        pyotp==2.9.0
    """),
    ENV_FILE: None,
}

# --- Ensure directories ---
def ensure_dirs():
    for path in FILES.keys():
        if path.suffix:
            path.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_SNAPSHOTS.mkdir(exist_ok=True)

# --- Write .env ---
def write_env():
    env = [
        f"DASHBOARD_SECRET={gen_secret()}",
        f"JWT_SECRET={gen_secret()}",
        "ADMIN_USER=admin",
        "ADMIN_PASS=change-me",
        "API_TOKEN=",
        "DEVICE_CACHE_TTL=10",
        "STATUS_CACHE_TTL=2",
        f"AUDIT_LOG_PATH={AUDIT_LOG.as_posix()}",
    ]
    ENV_FILE.write_text("\n".join(env) + "\n", encoding="utf-8")
    print("[WRITE] .env")

# --- Write files (autosave always) ---
def write_files_always():
    for path, content in FILES.items():
        if content is None:
            continue
        print(f"[WRITE] {path.relative_to(PROJECT_ROOT)}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

# --- Rotate audit log ---
def rotate_audit_log():
    if AUDIT_LOG.exists() and AUDIT_LOG.stat().st_size > 1024 * 1024:
        ts = time.strftime("%Y%m%d-%H%M%S")
        backup = PROJECT_ROOT / f"audit_{ts}.log"
        shutil.move(AUDIT_LOG, backup)
        print(f"[ROTATE] audit.log -> {backup}")

# --- Snapshot config ---
def snapshot_config():
    if ENV_FILE.exists():
        ts = time.strftime("%Y%m%d-%H%M%S")
        snap = CONFIG_SNAPSHOTS / f".env.{ts}.bak"
        shutil.copy(ENV_FILE, snap)
        print(f"[SNAPSHOT] .env -> {snap}")

# --- Git auto-commit ---
def git_commit():
    try:
        subprocess.check_call(["git", "add", "."])
        subprocess.check_call(["git", "commit", "-am", f"autosave: {time.strftime('%Y-%m-%d %H:%M:%S')}"])
        print("[GIT] auto-commit done")
    except Exception as e:
        print(f"[GIT] commit failed: {e}")

# --- Run shell commands ---
def run(cmd, env=None):
    print(f"[RUN] {' '.join(cmd)}")
    subprocess.check_call(cmd, env=env)

# --- Create venv ---
def create_venv():
    if not VENV_DIR.exists():
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
        print(f"[OK] venv created: {VENV_DIR}")

# --- Install requirements ---
def install_requirements():
    pip = VENV_DIR / "bin" / "pip"
    run([str(pip), "install", "-r", str(REQ_FILE)])
    print("[OK] dependencies installed")

# --- Launch dashboard ---
def launch_dashboard(mode="flask"):
    if mode == "docker":
        run(["docker-compose", "up", "--build", "-d"])
        print("[LAUNCH] Dashboard running in Docker")
    else:
        activate = f"source {VENV_DIR}/bin/activate"
        os.system(f"{activate} && export FLASK_APP=dlink_dashboard/app.py && export FLASK_ENV=development && flask run")
        print("[LAUNCH] Dashboard running in Flask dev mode")

# --- Main ---
def main():
    print("[START] Legendary MissionControl96 Ignition")
    ensure_dirs()
    write_files_always()
    write_env()
    rotate_audit_log()
    snapshot_config()
    git_commit()
    create_venv()
    install_requirements()
    launch_dashboard(mode="flask")  # Change to "docker" for Docker Compose
    print("[DONE] Grid reborn. Change ADMIN_PASS in .env before production use.")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with code {e.returncode}")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
