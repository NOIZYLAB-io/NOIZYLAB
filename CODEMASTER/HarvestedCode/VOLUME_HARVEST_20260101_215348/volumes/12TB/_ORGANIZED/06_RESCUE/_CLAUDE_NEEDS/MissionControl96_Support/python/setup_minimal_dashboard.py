#!/usr/bin/env python3
import os, sys, subprocess, textwrap, secrets
from pathlib import Path

PROJECT_ROOT = Path.cwd()
VENV_DIR = PROJECT_ROOT / ".venv"

def run(cmd, **kwargs):
    print("[RUN]", " ".join(cmd))
    subprocess.check_call(cmd, **kwargs)

def main():
    # 1. Write a minimal app file (expand with full dashboard code as needed)
    app_dir = PROJECT_ROOT / "dlink_dashboard"
    app_dir.mkdir(exist_ok=True)
    (app_dir / "app.py").write_text(textwrap.dedent("""
        from flask import Flask
        app = Flask(__name__)

        @app.route("/")
        def index():
            return "<h1>D-LINK Dashboard is running!</h1>"

        if __name__ == "__main__":
            app.run(debug=True)
    """))

    # 2. Create requirements.txt
    (PROJECT_ROOT / "requirements.txt").write_text("Flask==3.0.0\n")

    # 3. Create venv if not exists
    if not VENV_DIR.exists():
        run([sys.executable, "-m", "venv", str(VENV_DIR)])

    # 4. Install requirements
    pip = VENV_DIR / "bin" / "pip"
    run([str(pip), "install", "-r", "requirements.txt"])

    # 5. Run the app
    python = VENV_DIR / "bin" / "python"
    run([str(python), "dlink_dashboard/app.py"])

if __name__ == "__main__":
    main()
