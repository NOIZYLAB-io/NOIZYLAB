#!/usr/bin/env python3
import os, sys, subprocess, textwrap, secrets, time, json
from pathlib import Path

PROJECT_ROOT = Path.cwd()
VENV = PROJECT_ROOT / ".venv"

# --- Autosave Always: All modules, templates, configs, assets ---
MODULES = {
    PROJECT_ROOT/"requirements.txt": """
Flask==3.0.0
Flask-JWT-Extended==4.6.0
Flask-Limiter==3.7.0
Flask-Sock==0.7.0
python-dotenv==1.0.1
cachetools==5.3.3
pyyaml==6.0.2
itsdangerous==2.2.0
requests==2.32.3
gunicorn==22.0.0
qrcode==7.4.2
pyotp==2.9.0
scikit-learn==1.5.2
numpy==2.1.1
pandas==2.2.2
APScheduler==3.10.4
""",
    PROJECT_ROOT/"dlink_dashboard/app.py": textwrap.dedent(f"""
import os, logging
from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "{secrets.token_urlsafe(32)}"
@app.route("/")
def index():
    return "<h1>BITW×500 ignition online</h1>"
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
"""),
    # ... Add all other modules, templates, configs, assets here as strings ...
}

# --- Autosave function ---
def autosave(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"[AUTOSAVE] {path.relative_to(PROJECT_ROOT)}")

# --- Git autosave ---
def git_autosave():
    if (PROJECT_ROOT/".git").exists():
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            subprocess.check_call(["git","add","."])
            subprocess.check_call(["git","commit","-m",f"Autosave BITW×500 at {ts}"])
        except Exception as e:
            print("[WARN] Git autosave skipped:", e)

# --- Run shell commands ---
def run(cmd):
    print("[RUN]", " ".join(cmd)); subprocess.check_call(cmd)

# --- Main sequence ---
def main():
    print("[START] BITW×500 Autosetup Sequence")
    # 1) Autosave all modules/assets
    for path, content in MODULES.items():
        autosave(path, content)
    # 2) venv + deps
    if not VENV.exists(): run([sys.executable, "-m", "venv", str(VENV)])
    run([str(VENV/"bin/pip"), "install", "-r", "requirements.txt"])
    # 3) git autosave
    git_autosave()
    # 4) run app
    run([str(VENV/"bin/python"), "dlink_dashboard/app.py"])
    print("[DONE] Legendary grid ignition complete.")

if __name__ == "__main__":
    main()
