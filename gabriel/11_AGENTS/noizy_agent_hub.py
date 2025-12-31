#!/usr/bin/env python3
"""
NoizyFish Agent Hub: Seamless Multi-Agent Orchestrator
- Registers agents (AI, music, file, code, etc.)
- Provides discovery and messaging API
- Enables real-time status and communication
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import time

app = Flask(__name__)
CORS(app)

# In-memory registry of agents
agents = {}

@app.route('/register', methods=['POST'])
def register_agent():
    data = request.get_json()
    name = data.get('name')
    endpoint = data.get('endpoint')
    agent_type = data.get('type', 'generic')
    if not name or not endpoint:
        return jsonify({'error': 'Missing name or endpoint'}), 400
    agents[name] = {
        'endpoint': endpoint,
        'type': agent_type,
        'last_seen': time.time()
    }
    return jsonify({'status': 'registered', 'agents': list(agents.keys())})

@app.route('/agents', methods=['GET'])
def list_agents():
    # Return all registered agents and their status
    now = time.time()
    return jsonify({
        name: {
            **info,
            'online': (now - info['last_seen'] < 60)
        } for name, info in agents.items()
    })

@app.route('/message', methods=['POST'])
def message_agent():
    data = request.get_json()
    target = data.get('target')
    payload = data.get('payload')
    if not target or target not in agents:
        return jsonify({'error': 'Unknown agent'}), 404
    # Forward message to agent endpoint
    import requests
    try:
        resp = requests.post(agents[target]['endpoint'], json=payload, timeout=10)
        return jsonify({'result': resp.json()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Optional: background thread to clean up stale agents

def cleanup_agents():
    while True:
        now = time.time()
        for name in list(agents.keys()):
            if now - agents[name]['last_seen'] > 300:
                del agents[name]
        time.sleep(60)

threading.Thread(target=cleanup_agents, daemon=True).start()

if __name__ == '__main__':
    app.run(port=8787)
