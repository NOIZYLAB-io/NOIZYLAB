
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

# New: /ask endpoint for Bobby Orb and Noizy Brain
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query', '')
    # Route to Noizy Brain router if available, else fallback
    if 'noizy_brain' in AGENTS:
        result = AGENTS['noizy_brain'].handle_event({'query': query, 'agents': AGENTS})
        EVENTS.append({'type': 'ask', 'query': query, 'result': result})
        return jsonify(result)
    else:
        return jsonify({'status': 'error', 'answer': 'Noizy Brain router not loaded.'}), 500

# Plugin Loader: expects each plugin to define register(orchestrator) and register itself with a unique name
def register_agent(name, agent):
    AGENTS[name] = agent

def load_plugins(plugin_dir='_plugins'):
    if not os.path.isdir(plugin_dir):
        os.makedirs(plugin_dir)
    for fname in os.listdir(plugin_dir):
        if fname.endswith('.py'):
            path = os.path.join(plugin_dir, fname)
            spec = importlib.util.spec_from_file_location(fname[:-3], path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, 'register'):
                # Pass orchestrator context for registration
                mod.register(orchestrator=type('Orchestrator', (), {'register_agent': register_agent}))

if __name__ == '__main__':
    print('[Orchestrator] Loading plugins...')
    load_plugins()
    print(f'[Orchestrator] Loaded agents: {list(AGENTS.keys())}')
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000), daemon=True).start()
    print('[Orchestrator] API running on port 5000')
    # Main event loop (placeholder)
    while True:
        pass
