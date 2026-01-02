#!/usr/bin/env python3
# lifesafer_tablet.py
# LifeSaver Tablet kiosk: big-button rituals for Noizy_Genie_Mode.

import os
import sys
import subprocess
import threading
import time
import json
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, jsonify

APP = Flask(__name__, template_folder="templates", static_folder="static")

ROOT = Path(__file__).resolve().parent
GENIE = ROOT / "noizy_genie_all.py"

# Status memory (simple in-memory store)
STATUS = {
    "last_align": None,
    "align_running": False,
    "last_archive": None,
    "power": {"battery_pct": None, "solar_input_w": None, "grid": False},
    "mode": "idle"  # idle | emergency | emotech | creative
}

def run_genie_command(args_list):
    # Runs genie script in a background thread
    def _runner():
        try:
            subprocess.check_call([sys.executable, str(GENIE)] + args_list)
        except subprocess.CalledProcessError as e:
            print(f"[Genie] Error: {e}")
    t = threading.Thread(target=_runner, daemon=True)
    t.start()
    return t

def set_mode(mode):
    STATUS["mode"] = mode

def mark_align():
    STATUS["last_align"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    STATUS["align_running"] = False

def start_align():
    STATUS["align_running"] = True
    # Full pipeline: build tree, organize files, harvest mail, archive assets
    t = run_genie_command(["align"])
    # Detach and mark completion after a delay (best-effort)
    def _watch():
        t.join()
        mark_align()
    threading.Thread(target=_watch, daemon=True).start()

def archive_now():
    run_genie_command(["archive-assets"])
    STATUS["last_archive"] = datetime.now().strftime("%Y-%m-%d %H:%M")

# Optional: mock power telemetry (replace with your hardware interface later)
def refresh_power():
    # Placeholder values. Replace with real sensors or UPS API.
    STATUS["power"]["battery_pct"] = 87
    STATUS["power"]["solar_input_w"] = 42
    STATUS["power"]["grid"] = True

@APP.route("/")
def dashboard():
    refresh_power()
    return render_template("dashboard.html", status=STATUS)

@APP.route("/api/status")
def api_status():
    refresh_power()
    return jsonify(STATUS)

@APP.route("/ritual/align")
def ritual_align():
    start_align()
    return redirect(url_for("dashboard"))

@APP.route("/ritual/archive")
def ritual_archive():
    archive_now()
    return redirect(url_for("dashboard"))

@APP.route("/mode/emergency")
def mode_emergency():
    set_mode("emergency")
    return redirect(url_for("dashboard"))

@APP.route("/mode/emotech")
def mode_emotech():
    set_mode("emotech")
    return redirect(url_for("dashboard"))

@APP.route("/mode/creative")
def mode_creative():
    set_mode("creative")
    return redirect(url_for("dashboard"))

# Designer prompt helper: quick endpoint to generate a prompt pack
@APP.route("/designer/prompt/<pack>")
def designer_prompt(pack):
    # Generates a prompt from base template with a standard override
    run_genie_command(["add-prompt", "--template", "base", "--pack", pack, "--override", "act=Campaign Poster A1"])
    return redirect(url_for("dashboard"))

def main():
    # Ensure Genie script exists
    if not GENIE.exists():
        print("Missing noizy_genie_all.py. Place it in the same directory.")
        sys.exit(1)

    host = os.getenv("LIFESAVER_HOST", "0.0.0.0")
    port = int(os.getenv("LIFESAVER_PORT", "8080"))
    APP.run(host=host, port=port, debug=False)

if __name__ == "__main__":
    main()
