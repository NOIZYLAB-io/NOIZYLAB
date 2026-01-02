import os
import importlib.util
import threading
from flask import Flask, request, jsonify

# Plugin/Agent Registry
AGENTS = {}
EVENTS = []

# Flask API for cross-device (iPad, etc.)
app = Flask(__name__)

@app.route('/api/message', methods=['POST'])
def api_message():
    data = request.json
    msg = data.get('message', '')
    # Broadcast to all agents
    for agent in AGENTS.values():
        if hasattr(agent, 'on_message'):
            agent.on_message(msg)
    EVENTS.append({'type': 'api_message', 'message': msg})
    return jsonify({'status': 'ok'})

@app.route('/api/events', methods=['GET'])
def api_events():
    return jsonify(EVENTS[-20:])

# Plugin Loader
def load_plugins(plugin_dir='_plugins'):
    if not os.path.isdir(plugin_dir):
        os.makedirs(plugin_dir)
    for fname in os.listdir(plugin_dir):
        if fname.endswith('.py'):
            path = os.path.join(plugin_dir, fname)
            spec = importlib.util.spec_from_file_location(fname[:-3], path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, 'register_agent'):
                agent = mod.register_agent()
                AGENTS[agent.__class__.__name__] = agent

if __name__ == '__main__':
    print('[Orchestrator] Loading plugins...')
    load_plugins()
    print(f'[Orchestrator] Loaded agents: {list(AGENTS.keys())}')
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5005), daemon=True).start()
    print('[Orchestrator] API running on port 5005')
    # Main event loop (placeholder)
    while True:
        pass
