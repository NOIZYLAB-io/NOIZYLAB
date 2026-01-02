from flask import Flask, render_template, jsonify
import threading
import time

app = Flask(__name__)

status_data = {
    "macpro": {
        "cpu": "Apple M2 Ultra",
        "ram": "192 GB",
        "uptime": "0:00",
        "thermal": "Nominal",
        "silence": "Active",
        "grid": "Linked"
    },
    "noizygrid": {
        "nodes": 1,
        "health": "Optimal"
    }
}

@app.route('/')
def dashboard():
    return render_template('dashboard.html', status=status_data)

@app.route('/api/status')
def api_status():
    return jsonify(status_data)

# Background thread to simulate status updates
def update_status():
    while True:
        # Simulate status changes here
        status_data["macpro"]["uptime"] = time.strftime("%H:%M", time.gmtime(time.time()))
        time.sleep(10)

if __name__ == '__main__':
    threading.Thread(target=update_status, daemon=True).start()
    app.run(debug=True, host='0.0.0.0', port=5000)
