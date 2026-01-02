from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/trigger-guest', methods=['GET', 'POST'])
def trigger_guest():
    # Trigger guest logic here (e.g., run a capsule, log event)
    print("Guest triggered!")
    return jsonify({"status": "Guest triggered"})

@app.route('/log-mood', methods=['POST'])
def log_mood():
    data = request.get_json()
    mood = data.get('mood', 'Unknown')
    # Log mood to a file
    log_entry = {"mood": mood}
    log_path = os.path.expanduser('~/WORK_OF_TODAY/utilities/mood_log.json')
    try:
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                logs = json.load(f)
        else:
            logs = []
        logs.append(log_entry)
        with open(log_path, 'w') as f:
            json.dump(logs, f, indent=2)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    print(f"Mood logged: {mood}")
    return jsonify({"status": "Mood logged", "mood": mood})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
