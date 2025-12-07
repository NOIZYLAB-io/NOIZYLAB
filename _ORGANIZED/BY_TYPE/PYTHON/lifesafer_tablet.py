# VS Code Bridge integration routes
@APP.route("/cockpit/vsc/run-task/<path:label>")
def vsc_run_task(label):
    try:
        vsc_call("/run-task", {"label": label})
    except Exception as e:
        print(f"[VSC] run-task error: {e}")
    return redirect(url_for("dashboard"))

@APP.route("/cockpit/vsc/run-command/<path:cmd_id>")
def vsc_run_command(cmd_id):
    try:
        vsc_call("/run-command", {"id": cmd_id})
    except Exception as e:
        print(f"[VSC] run-command error: {e}")
    return redirect(url_for("dashboard"))

@APP.route("/cockpit/vsc/open")
def vsc_open():
    p = request.args.get("path", "")
    try:
        vsc_call("/open", {"path": p})
    except Exception as e:
        print(f"[VSC] open error: {e}")
    return redirect(url_for("dashboard"))

@APP.route("/cockpit/vsc/workspace")
def vsc_workspace():
    p = request.args.get("path", "")
    try:
        vsc_call("/workspace", {"path": p})
    except Exception as e:
        print(f"[VSC] workspace error: {e}")
    return redirect(url_for("dashboard"))

@APP.route("/cockpit/vsc/terminal")
def vsc_terminal():
    cmd = request.args.get("cmd", "")
    cwd = request.args.get("cwd", "")
    try:
        vsc_call("/terminal", {"cmd": cmd, "cwd": cwd})
    except Exception as e:
        print(f"[VSC] terminal error: {e}")
    return redirect(url_for("dashboard"))

@APP.route("/cockpit/vsc/paste")
def vsc_paste():
    text = request.args.get("text", "")
    try:
        vsc_call("/paste", {"text": text})
    except Exception as e:
        print(f"[VSC] paste error: {e}")
    return redirect(url_for("dashboard"))

@APP.route("/cockpit/vsc/save")
def vsc_save():
    try:
        vsc_call("/save")
    except Exception as e:
        print(f"[VSC] save error: {e}")
    return redirect(url_for("dashboard"))
#!/usr/bin/env python3
# lifesafer_tablet.py
# LifeSaver Tablet kiosk: big-button rituals for Noizy_Genie_Mode + Emotional Tech Player.


import os
import sys
import subprocess
import threading
import time
import json
import math
import io
import platform
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, jsonify, send_file, request

APP = Flask(__name__, template_folder="templates", static_folder="static")

ROOT = Path(__file__).resolve().parent
GENIE = ROOT / "noizy_genie_all.py"
PLAYLISTS_DIR = ROOT / "playlists"         # JSON playlists
AUDIO_DIR = ROOT / "static" / "audio"      # Local audio files

STATUS = {
    "last_align": None,
    "align_running": False,
    "last_archive": None,
    "power": {"battery_pct": None, "solar_input_w": None, "grid": False},
    "mode": "idle"  # idle | emergency | emotech | creative
}

# -----------------------------
# Genie orchestration helpers
# -----------------------------

def run_genie_command(args_list):
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
    t = run_genie_command(["align"])
    def _watch():
        t.join()
        mark_align()
    threading.Thread(target=_watch, daemon=True).start()

def archive_now():
    run_genie_command(["archive-assets"])
    STATUS["last_archive"] = datetime.now().strftime("%Y-%m-%d %H:%M")

def refresh_power():
    # TODO: replace with real sensors or UPS API
    STATUS["power"]["battery_pct"] = 87
    STATUS["power"]["solar_input_w"] = 42
    STATUS["power"]["grid"] = True

# -----------------------------
# Emotional Tech: playlists API
# -----------------------------

def list_playlists():
    PLAYLISTS_DIR.mkdir(parents=True, exist_ok=True)
    return [p.name for p in PLAYLISTS_DIR.glob("*.json")]

def load_playlist(name: str):
    path = PLAYLISTS_DIR / f"{name}.json"
    if not path.exists():
        return {"name": name, "tracks": []}
    return json.loads(path.read_text(encoding="utf-8"))

@APP.route("/api/playlists")
def api_playlists():
    return jsonify({"playlists": list_playlists()})

@APP.route("/api/playlist/<name>")
def api_playlist(name):
    return jsonify(load_playlist(name))

# Serve local audio files (static/audio/*)
@APP.route("/audio/<path:fname>")
def audio_file(fname):
    path = AUDIO_DIR / fname
    if not path.exists():
        return jsonify({"error": "not found"}), 404
    return send_file(path)

# -----------------------------
# Emotional Tech: binaural tones
# -----------------------------

def generate_binaural_wav(duration_sec=300, base_freq=220.0, beat_hz=7.0, sample_rate=48000, volume=0.2):
    # Left: base_freq; Right: base_freq + beat_hz
    import wave
    import struct
    frames = int(duration_sec * sample_rate)
    buf = io.BytesIO()
    wf = wave.open(buf, 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(2)  # 16-bit
    wf.setframerate(sample_rate)
    for i in range(frames):
        t = i / sample_rate
        left = volume * math.sin(2 * math.pi * base_freq * t)
        right = volume * math.sin(2 * math.pi * (base_freq + beat_hz) * t)
        # clip and pack
        l_int = int(max(-1.0, min(1.0, left)) * 32767)
        r_int = int(max(-1.0, min(1.0, right)) * 32767)
        wf.writeframes(struct.pack('<hh', l_int, r_int))
    wf.close()
    buf.seek(0)
    return buf

@APP.route("/api/binaural")
def api_binaural():
    # Query params: duration, base, beat, rate, vol
    duration = float(request.args.get("duration", 300))
    base = float(request.args.get("base", 220.0))
    beat = float(request.args.get("beat", 7.0))
    rate = int(request.args.get("rate", 48000))
    vol = float(request.args.get("vol", 0.2))
    buf = generate_binaural_wav(duration, base, beat, rate, vol)
    return send_file(buf, mimetype="audio/wav", as_attachment=False, download_name="binaural.wav")

# Optional: simple TTS using macOS 'say'
@APP.route("/api/say")
def api_say():
    text = request.args.get("text", "Alignment complete")
    if platform.system() == "Darwin":
        subprocess.Popen(["say", text])
        return jsonify({"ok": True})
    return jsonify({"ok": False, "msg": "TTS unavailable on this OS"})

# -----------------------------
# Routes: dashboard + modes
# -----------------------------

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
    return redirect(url_for("emotech"))  # use emergency page if you add one

@APP.route("/mode/emotech")
def mode_emotech():
    set_mode("emotech")
    return redirect(url_for("emotech"))

@APP.route("/mode/creative")
def mode_creative():
    set_mode("creative")
    return redirect(url_for("dashboard"))  # or creative page if you add one

# Emotional Tech UI
@APP.route("/emotech")
def emotech():
    refresh_power()
    # default playlist selection
    playlists = list_playlists()
    default_pl = playlists[0] if playlists else None
    return render_template("emotech.html", status=STATUS, playlists=playlists, default_playlist=default_pl)

# Designer prompt helper
@APP.route("/designer/prompt/<pack>")
def designer_prompt(pack):
    run_genie_command(["add-prompt", "--template", "base", "--pack", pack, "--override", "act=Campaign Poster A1"])
    return redirect(url_for("dashboard"))

def main():
    if not GENIE.exists():
        print("Missing noizy_genie_all.py. Place it in the same directory.")
        sys.exit(1)
    host = os.getenv("LIFESAVER_HOST", "0.0.0.0")
    port = int(os.getenv("LIFESAVER_PORT", "8080"))
    APP.run(host=host, port=port, debug=False)

if __name__ == "__main__":
    main()
