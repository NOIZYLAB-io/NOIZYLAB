#!/usr/bin/env python3
import os, sys, subprocess, textwrap, secrets
from pathlib import Path

PROJECT_ROOT = Path.cwd()
VENV_DIR = PROJECT_ROOT / ".venv"
REQ_FILE = PROJECT_ROOT / "requirements.txt"
ENV_FILE = PROJECT_ROOT / ".env"

# --- Generate secrets ---
def gen_secret(): return secrets.token_urlsafe(32)

# --- Full dashboard code scaffold ---
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
            # ...register blueprints here (devices, actions, auth, topology, metrics, etc.)...
            @app.route("/")
            def index():
                return "<h1>D-LINK Dashboard is running!</h1>"
            return app
        app = create_app()
        # ...sentinel, scheduler, etc. bootstrap...
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

# --- Write .env ---
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

# --- Write files ---
def write_files():
    for path, content in FILES.items():
        if content is None:
            continue
        print(f"{'[WRITE]' if not path.exists() else '[UPDATE]'} {path.relative_to(PROJECT_ROOT)}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

# --- Run shell commands ---
def run(cmd, env=None):
    print(f"[RUN] {' '.join(cmd)}")
    subprocess.check_call(cmd, env=env)

# --- Create venv ---
def create_venv():
    if VENV_DIR.exists():
        print(f"[SKIP] venv already exists at {VENV_DIR}")
        return
    run([sys.executable, "-m", "venv", str(VENV_DIR)])
    print(f"[OK] venv created: {VENV_DIR}")

# --- Install requirements ---
def install_requirements():
    pip = VENV_DIR / "bin" / "pip"
    run([str(pip), "install", "-r", str(REQ_FILE)])
    print("[OK] dependencies installed")

# --- Show next steps ---
def show_next():
    print("\n[ENV] To run the app:")
    print(f"source {VENV_DIR}/bin/activate")
    print("export FLASK_APP=dlink_dashboard/app.py")
    print("export FLASK_ENV=development")
    print("flask run")
    print("\n[PROD] Gunicorn example:")
    print(f"source {VENV_DIR}/bin/activate && gunicorn -w 2 -b 0.0.0.0:5000 'dlink_dashboard.app:app'")

# --- Main ---
def main():
    print("[START] MissionControl96 One-Touch Ignition")
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
