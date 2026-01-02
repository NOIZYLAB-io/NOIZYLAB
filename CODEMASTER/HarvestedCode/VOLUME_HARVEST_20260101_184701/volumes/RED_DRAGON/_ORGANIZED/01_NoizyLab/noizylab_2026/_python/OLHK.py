# SuperBrain Hub: Multi-Agent Orchestrator
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Example agent endpoints (update with real URLs if needed)
AGENTS = {
    "chatgpt": "http://127.0.0.1:5000/chatgpt",  # Flask app.py endpoint
    "noisy_brain": "http://127.0.0.1:5000/noisy_brain",  # Flask app.py endpoint
    # Add more agents as needed
}

def query_agent(agent_url, prompt):
    try:
        response = requests.post(agent_url, json={"task": prompt}, timeout=10)
        return response.json().get("result", "No result")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

@app.route('/ask')
def ask():
    prompt = request.args.get('q', '')
    results = {}
    for name, url in AGENTS.items():
        results[name] = query_agent(url, prompt)
    # Fuse results (simple join for now)
    fused = " | ".join([f"{k}: {v}" for k, v in results.items()])
    return jsonify({"final": fused, "agents": results})

if __name__ == '__main__':
    app.run(port=8765)
