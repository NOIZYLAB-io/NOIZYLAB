from flask import Flask, render_template, jsonify
import threading
import time

app = Flask(__name__)

fleet_status = {
    "MacStudio": {"status": "online", "ritual": "commander"},
    "MacPro_Hot-Rod": {"status": "online", "ritual": "hotrod_engine"},
    "INSPIRON_Rebirth": {"status": "online", "ritual": "rebirth_agent"},
    "OMEN_Sentinel": {"status": "online", "ritual": "sentinel_agent"},
    "PLANAR_Oracle": {"status": "online", "ritual": "display_config"},
    "NOIZYGATE": {"status": "online", "ritual": "gateway_config"}
}

@app.route('/')
def dashboard():
    return render_template('sentinel_dashboard.html', fleet=fleet_status)

@app.route('/api/fleet')
def api_fleet():
    return jsonify(fleet_status)

# Background thread to simulate status updates
def update_fleet():
    while True:
        # Simulate status changes here
        for node in fleet_status:
            fleet_status[node]["status"] = "online"  # Placeholder for real status
        time.sleep(10)

if __name__ == '__main__':
    threading.Thread(target=update_fleet, daemon=True).start()
    app.run(debug=True, host='0.0.0.0', port=5050)
