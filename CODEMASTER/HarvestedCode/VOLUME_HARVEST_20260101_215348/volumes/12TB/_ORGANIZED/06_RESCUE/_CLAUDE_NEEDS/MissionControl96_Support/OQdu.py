from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)
RITUALS = {
    "sequoia": "~/NoizyFish/Triggers/activate_sequoia.py",
    "pcie": "~/NoizyFish/Triggers/pcie_health_check.py",
    "capsule": "~/NoizyFish/Triggers/build_capsule.py"
}

@app.route("/status")
def status(): return jsonify({"status": "Online", "slab": "NOIZYWIND"})

@app.route("/trigger")
def trigger():
    ritual = request.args.get("ritual")
    path = RITUALS.get(ritual)
    if path:
        subprocess.run(["python3", os.path.expanduser(path)])
        return f"{ritual} triggered"
    return "Ritual not found", 404

if __name__ == "__main__": app.run(host="0.0.0.0", port=5050)
