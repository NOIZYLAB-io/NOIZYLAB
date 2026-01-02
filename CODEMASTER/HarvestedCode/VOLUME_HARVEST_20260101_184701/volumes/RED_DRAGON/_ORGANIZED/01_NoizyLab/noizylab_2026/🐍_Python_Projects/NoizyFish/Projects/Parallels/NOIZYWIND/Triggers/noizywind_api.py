from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

LOG_PATH = "/Users/rsp_ms/NoizyFish/Logs/noizywind_status.log"

@app.route("/noizywind/status", methods=["GET"])
def noizywind_status():
    try:
        with open(LOG_PATH) as f:
            status = f.read()
    except FileNotFoundError:
        status = "No status log found."
    return jsonify({"status": status})

@app.route("/noizywind/trigger", methods=["POST"])
def noizywind_trigger():
    ritual = request.args.get("ritual")
    if ritual == "activate_overlay":
        # Example: Launch overlay ritual
        subprocess.run(["python3", "/Users/rsp_ms/Parallels/NOIZYWIND/Triggers/OverlayLauncher.py"])
        return jsonify({"result": "Overlay activated!"})
    return jsonify({"error": "Unknown ritual"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051, debug=True)
