import socket

def find_free_port(start=5003, end=5010):
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:

@app.route('/status')
def status():
    return jsonify({"status": "online", "ai": True, "fleet": True, "alerts": True})
# MissionControl96 Dashboard Backend
from flask import Flask, jsonify, send_file, request
                import socket
                from flask import Flask, jsonify, send_file, request
                import socket
                from flask import Flask, jsonify, send_file, request
                import os, json
                app = Flask(__name__)

                def ai_health():
                    slabs = ['OMEN_Slab', 'INSPIRON_Slab', 'Legacy_Slab']
                    health = dict.fromkeys(slabs, '\ud83d\udfe2')
                    return jsonify(health)
            return f.read()[-2000:]
    return "No logs found."

                @app.route('/status')
                def status():
                    return jsonify({"status": "online", "ai": True, "fleet": True, "alerts": True})

# Fleet map data (optional extension)
@app.route('/fleet')
def fleet():
    slabs = [
        { 'name': 'OMEN_Slab', 'status': '🟢' },
        { 'name': 'INSPIRON_Slab', 'status': '🟢' },
        { 'name': 'Legacy_Slab', 'status': '🟡' }
    ]
    return jsonify(slabs)

# AI Insights endpoint
@app.route('/ai_insights')
def ai_insights():
    # Example: AI-driven recommendation logic
    # In production, use ML models and real logs
    recommendation = "All slabs healthy. No action required. Next check: 5 minutes."
    return jsonify({"recommendation": recommendation})

@app.route('/admin/<cmd>', methods=['POST'])
def admin_cmd(cmd):
    # Example: Execute fleet-wide actions via shell/SSH
    if cmd == 'heal':
        os.system('sh /Users/rsp_ms/Desktop/MissionControl96/daemons/heal_fleet.sh')
        return 'Healing triggered across fleet.'
    elif cmd == 'reboot':
        # Example: Reboot all slabs via SSH
        for ip in ['192.168.0.10', '192.168.0.11', '192.168.0.99']:
            os.system(f"ssh admin@{ip} 'sudo reboot'")
        return 'Reboot triggered across fleet.'
    elif cmd == 'silence':
        os.system('curl -X POST http://macstudio.local:5000/enforce_silence')
        return 'Silence enforced across fleet.'
    else:
        return 'Unknown command.'

if __name__ == '__main__':
    port = find_free_port()
    print(f"MissionControl96 backend running on port {port}")
    app.run(host='0.0.0.0', port=port)
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


@app.route('/admin/<cmd>', methods=['POST'])
def admin_cmd(cmd):
    # Example: Execute fleet-wide actions via shell/SSH
    if cmd == 'heal':
        os.system('sh /Users/rsp_ms/Desktop/MissionControl96/daemons/heal_fleet.sh')
        return 'Healing triggered across fleet.'
    elif cmd == 'reboot':
        # Example: Reboot all slabs via SSH
        for ip in ['192.168.0.10', '192.168.0.11', '192.168.0.99']:
            os.system(f"ssh admin@{ip} 'sudo reboot'")
        return 'Reboot triggered across fleet.'
    elif cmd == 'silence':
        os.system('curl -X POST http://macstudio.local:5000/enforce_silence')
        return 'Silence enforced across fleet.'
    else:
        return 'Unknown command.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)