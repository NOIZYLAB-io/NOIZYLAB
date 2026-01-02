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
