from flask import Flask, render_template
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
