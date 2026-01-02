from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

SLABS = {
    "StudioSlab": "192.168.2.10",
    "PowerSlab": "192.168.2.20",
    "NOIZYWIND": "192.168.2.30",
    "VisionSlab": "192.168.2.40"
}

@app.route("/status")
def status():
    statuses = {}
    for slab, ip in SLABS.items():
        result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
        statuses[slab] = "Online" if result.returncode == 0 else "Offline"
    return jsonify(statuses)

@app.route("/link", methods=["POST"])
def link():
    slab = request.json.get("slab")
    ip = SLABS.get(slab)
    if not ip:
        return jsonify({"error": "Unknown slab"}), 404
    # Placeholder for actual link logic
    return jsonify({"message": f"Link established with {slab} ({ip})"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5151)
