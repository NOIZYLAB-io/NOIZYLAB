from flask import Flask, render_template, jsonify
import platform
import subprocess

app = Flask(__name__)

# Helper functions to get system info
def get_python_version():
    return platform.python_version()

def get_node_version():
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception:
        return 'Not installed'

def get_vscode_version():
    try:
        result = subprocess.run(['code', '--version'], capture_output=True, text=True)
        return result.stdout.splitlines()[0]
    except Exception:
        return 'Not installed'

@app.route('/')
def dashboard():
    python_version = get_python_version()
    node_version = get_node_version()
    vscode_version = get_vscode_version()
    # Example: AI tools status (static for now)
    ai_tools = [
        {'name': 'Continue', 'status': 'Installed'},
        {'name': 'GitHub Copilot', 'status': 'Installed'},
        {'name': 'Codeium', 'status': 'Installed'},
        {'name': 'TabNine', 'status': 'Installed'},
        {'name': 'AWS Toolkit', 'status': 'Installed'},
        {'name': 'SonarLint', 'status': 'Installed'},
        {'name': 'Mintlify Doc Writer', 'status': 'Installed'}
    ]
    return render_template('dashboard.html',
                           python_version=python_version,
                           node_version=node_version,
                           vscode_version=vscode_version,
                           ai_tools=ai_tools)

if __name__ == '__main__':
    app.run(debug=True)

# --- Custom Agent Endpoints ---
@app.route('/super_brain', methods=['POST'])
def super_brain():
    data = request.get_json()
    task = data.get('task', '')
    result = f"Super Brain processed: {task}"
    add_log(f"Super Brain received task: {task}")
    add_log(f"Super Brain result: {result}")
    return jsonify({"result": result})

@app.route('/noisy_brain', methods=['POST'])
def noisy_brain():
    data = request.get_json()
    task = data.get('task', '')
    result = f"Noisy Brain automated: {task}"
    add_log(f"Noisy Brain received task: {task}")
    add_log(f"Noisy Brain result: {result}")
    return jsonify({"result": result})

# --- Real-Time Status/Log Backend ---
import threading

STATUS_LOG = ["System started."]

def add_log(message):
    STATUS_LOG.append(message)
    if len(STATUS_LOG) > 100:
        STATUS_LOG.pop(0)

@app.route('/get_status_log')
def get_status_log():
    return jsonify({"log": STATUS_LOG})

# Example: Add log when agent assignment/priority changes
@app.route('/set_agent_project', methods=['POST'])
def set_agent_project():
    data = request.get_json()
    agent_id = int(data.get('agent_id'))
    project = data.get('project', 'Unassigned')
    if agent_id in AGENTS:
        AGENTS[agent_id]["project"] = project
        add_log(f"Agent {agent_id} assigned to {project}")
        return jsonify({"success": True, "project": project})
    return jsonify({"success": False}), 400

@app.route('/set_agent_priority', methods=['POST'])
def set_agent_priority():
    data = request.get_json()
    agent_id = int(data.get('agent_id'))
    priority = data.get('priority', 'Normal')
    if agent_id in AGENTS:
        AGENTS[agent_id]["priority"] = priority
        add_log(f"Agent {agent_id} priority set to {priority}")
        return jsonify({"success": True, "priority": priority})
    return jsonify({"success": False}), 400

# --- Agent Management Backend ---
from flask import request

# In-memory agent state: {agent_id: {project: str, priority: str}}
AGENTS = {i: {"project": "Unassigned", "priority": "Normal"} for i in range(1, 97)}

@app.route('/set_agent_project', methods=['POST'])
def set_agent_project():
    data = request.get_json()
    agent_id = int(data.get('agent_id'))
    project = data.get('project', 'Unassigned')
    if agent_id in AGENTS:
        AGENTS[agent_id]["project"] = project
        return jsonify({"success": True, "project": project})
    return jsonify({"success": False}), 400

@app.route('/set_agent_priority', methods=['POST'])
def set_agent_priority():
    data = request.get_json()
    agent_id = int(data.get('agent_id'))
    priority = data.get('priority', 'Normal')
    if agent_id in AGENTS:
        AGENTS[agent_id]["priority"] = priority
        return jsonify({"success": True, "priority": priority})
    return jsonify({"success": False}), 400

@app.route('/get_agents')
def get_agents():
    return jsonify(AGENTS)

# --- Drum Core Integrity Scan Endpoint ---
import os
from pathlib import Path

DRUM_CORE_FOLDERS = [
    "/Library/Application Support/EZDrummer",
    "/Library/Application Support/Superior Drummer",
    "/Library/Application Support/Toontrack",
    "/Library/Application Support/XLN Audio",
    "/Library/Application Support/FXpansion",
    "/Library/Application Support/Logic"
]

def check_file_integrity(file_path: Path):
    problems = []
    if not file_path.exists():
        problems.append("Missing")
    elif not file_path.is_file():
        problems.append("Not a file")
    elif file_path.stat().st_size == 0:
        problems.append("Zero-byte file")
    else:
        try:
            with open(file_path, "rb") as f:
                f.read(1)
        except Exception as e:
            problems.append(f"Unreadable: {e}")
    return problems

@app.route('/scan_drum_core')
def scan_drum_core():
    total_files = 0
    problem_files = []
    for folder in DRUM_CORE_FOLDERS:
        for root, _, files in os.walk(folder):
            for f in files:
                file_path = Path(root) / f
                total_files += 1
                problems = check_file_integrity(file_path)
                if problems:
                    problem_files.append((str(file_path), problems))
    return jsonify({
        "total_files": total_files,
        "problem_files": problem_files
    })
