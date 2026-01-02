#!/usr/bin/env python3
import os, sys, subprocess, textwrap
from pathlib import Path

PROJECT_ROOT = Path.cwd()
VENV_DIR = PROJECT_ROOT / ".venv"

# Minimal Flask app setup and run
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

# Create requirements.txt
(PROJECT_ROOT / "requirements.txt").write_text("Flask==3.0.0\n")

# Create venv if not exists
if not VENV_DIR.exists():
    subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])

# Install requirements
pip = VENV_DIR / "bin" / "pip"
subprocess.check_call([str(pip), "install", "-r", "requirements.txt"])

# Run the app
python = VENV_DIR / "bin" / "python"
subprocess.check_call([str(python), "dlink_dashboard/app.py"])
