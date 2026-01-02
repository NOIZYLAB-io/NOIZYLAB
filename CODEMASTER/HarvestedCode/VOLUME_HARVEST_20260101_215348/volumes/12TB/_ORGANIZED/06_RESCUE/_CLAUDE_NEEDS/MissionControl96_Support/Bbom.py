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
        import sys, os, logging
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
        from flask import Flask
        from flask_jwt_extended import JWTManager
        from flask_limiter import Limiter
        from flask_limiter.util import get_remote_address
        from flask_sock import Sock
        from dotenv import load_dotenv
        load_dotenv()
        def create_app():
            app = Flask(__name__, static_folder="static", template_folder="templates")
            app.config.from_object("dlink_dashboard.config.Config")
            logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
            app.logger.info("Starting D-LINK Dashboard BIW")
            @app.after_request
            def headers(resp):
                resp.headers["X-Content-Type-Options"] = "nosniff"
                resp.headers["X-Frame-Options"] = "DENY"
                resp.headers["X-XSS-Protection"] = "1; mode=block"
                resp.headers["Content-Security-Policy"] = "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'"
                return resp
            JWTManager(app)
            Limiter(get_remote_address, app=app, default_limits=["200/hour", "50/minute"])
            sock = Sock(app)
            # Register blueprints
            from dlink_dashboard.routes.topology import bp as topo_bp
            from dlink_dashboard.routes.devices import bp as devices_bp
            from dlink_dashboard.health.sentinel import Sentinel
            from dlink_dashboard.routes.metrics import bp as metrics_bp
            from dlink_dashboard.routes.auth import bp as auth_bp
            from dlink_dashboard.routes.scheduler import bp as scheduler_bp
            app.register_blueprint(topo_bp)
            app.register_blueprint(devices_bp)
            app.register_blueprint(metrics_bp)
            app.register_blueprint(auth_bp)
            app.register_blueprint(scheduler_bp)
            sentinel = Sentinel(interval=15)
            sentinel.start(app)
            @app.route("/")
            def index():
                from dlink_dashboard.utils.audit import story_mode
                return f"<h1>D-LINK Dashboard is running!</h1><pre>{story_mode()}</pre>"
            return app
        app = create_app()
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
