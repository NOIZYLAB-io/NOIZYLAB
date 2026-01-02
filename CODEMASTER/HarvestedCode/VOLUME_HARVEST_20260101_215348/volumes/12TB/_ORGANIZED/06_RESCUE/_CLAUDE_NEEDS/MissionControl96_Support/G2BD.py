# MissionControl96 Dashboard Backend
from flask import Flask, jsonify, send_file, request
import os, json
app = Flask(__name__)

# Dummy AI health data
@app.route('/ai_health')
def ai_health():
    slabs = ['OMEN_Slab', 'INSPIRON_Slab', 'Legacy_Slab']
    health = { slab: '🟢' for slab in slabs }
    return jsonify(health)

# Dummy alerts
@app.route('/alerts')
def alerts():
    return jsonify(["All systems operational", "No failures detected"])

# Latest logs
@app.route('/logs')
def logs():
    log_path = '/Users/rsp_ms/NOIZYGRID_LOGS/OMEN_Slab.log'
    if os.path.exists(log_path):
        with open(log_path) as f:
            return f.read()[-2000:]
    return "No logs found."

# Fleet map data (optional extension)
@app.route('/fleet')
def fleet():
    slabs = [
        { 'name': 'OMEN_Slab', 'status': '🟢' },
        { 'name': 'INSPIRON_Slab', 'status': '🟢' },
        { 'name': 'Legacy_Slab', 'status': '🟡' }
    ]
    return jsonify(slabs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)