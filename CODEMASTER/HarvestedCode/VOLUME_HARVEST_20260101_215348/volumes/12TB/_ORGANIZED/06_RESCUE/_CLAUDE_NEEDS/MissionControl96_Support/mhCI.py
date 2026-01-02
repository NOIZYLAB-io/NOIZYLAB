#!/usr/bin/env python3
"""
setup_dlink_dashboard_best.py
Sets up a world-class Flask-based D-Link Dashboard web app.
"""
import os
import sys
import subprocess
import textwrap
from pathlib import Path

PROJECT_ROOT = Path.cwd()
VENV_DIR = PROJECT_ROOT / ".venv"
REQ_FILE = PROJECT_ROOT / "requirements.txt"

FILES = {
    PROJECT_ROOT / "DLink_Control.py": textwrap.dedent(r'''
from typing import List, Dict, Optional

_DEVICES = [
    {"id": "DL-001", "ip": "192.168.0.1", "model": "DIR-882", "name": "Main Router"},
    {"id": "DL-002", "ip": "192.168.0.2", "model": "DAP-1610", "name": "Living Room AP"},
]

_CLIENTS = {
    "DL-001": [
        {"mac": "AA:BB:CC:DD:EE:01", "hostname": "MacStudio", "ip": "192.168.0.101", "signal": -45},
        {"mac": "AA:BB:CC:DD:EE:02", "hostname": "HP-OMEN", "ip": "192.168.0.102", "signal": -60},
    ],
    "DL-002": [
        {"mac": "AA:BB:CC:DD:EE:03", "hostname": "iPhone", "ip": "192.168.0.150", "signal": -55},
    ],
}

def discover_devices() -> List[Dict]:
    return _DEVICES

def get_device(device_id: str) -> Optional[Dict]:
    return next((d for d in _DEVICES if d["id"] == device_id), None)

def get_device_status(device_id: str) -> Dict:
    return {"online": True, "uptime": "3d 12h", "cpu": 22, "mem": 48, "firmware": "1.20", "wan": "up"}

def list_clients(device_id: str) -> List[Dict]:
    return _CLIENTS.get(device_id, [])

def reboot_device(device_id: str) -> Dict:
    return {"ok": True, "message": f"Reboot initiated for {device_id}"}

def set_config(device_id: str, changes: Dict) -> Dict:
    return {"ok": True, "applied": changes}
'''),
    REQ_FILE: textwrap.dedent(r'''
Flask==3.0.0
requests==2.32.3
cachetools==5.3.3
pyyaml==6.0.2
'''),
    # ...rest of dashboard files as in previous scaffold...
}

def ensure_dirs():
    for path in FILES.keys():
        if path.suffix:
            path.parent.mkdir(parents=True, exist_ok=True)

def write_files():
    for path, content in FILES.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def run(cmd, env=None):
    print(f"[RUN] {' '.join(cmd)}")
    subprocess.check_call(cmd, env=env)

def create_venv():
    if VENV_DIR.exists():
        print(f"[SKIP] venv already exists at {VENV_DIR}")
        return
    run([sys.executable, "-m", "venv", str(VENV_DIR)])
    print(f"[OK] venv created: {VENV_DIR}")

def install_requirements():
    pip = VENV_DIR / "bin" / "pip"
    run([str(pip), "install", "-r", str(REQ_FILE)])
    print("[OK] dependencies installed")

def set_flask_env():
    print("\n[ENV] To run the app:")
    print(f"source {VENV_DIR}/bin/activate")
    print("export FLASK_APP=dlink_dashboard/app.py")
    print("export FLASK_ENV=development")
    print("flask run\n")

def main():
    print("[START] D-LINK Dashboard Best Setup")
    ensure_dirs()
    write_files()
    create_venv()
    install_requirements()
    set_flask_env()
    print("[DONE] Files saved, venv ready. Launch with the commands above.")
    
        # Add dashboard files to FILES
        FILES.update({
            PROJECT_ROOT / "dlink_dashboard/app.py": textwrap.dedent(r'''
    from flask import Flask
    from dlink_dashboard.routes.devices import devices_bp
    from dlink_dashboard.routes.clients import clients_bp
    from dlink_dashboard.routes.status import status_bp

    def create_app():
        app = Flask(__name__)
        app.config.from_pyfile('config.py')
        app.register_blueprint(devices_bp)
        app.register_blueprint(clients_bp)
        app.register_blueprint(status_bp)
        return app
    '''),
            PROJECT_ROOT / "dlink_dashboard/config.py": textwrap.dedent(r'''
    SECRET_KEY = "noizyfish_secret"
    CACHE_TYPE = "simple"
    '''),
            PROJECT_ROOT / "dlink_dashboard/routes/devices.py": textwrap.dedent(r'''
    from flask import Blueprint, render_template, request
    from dlink_dashboard.dlink.adapters import discover_devices, get_device

    devices_bp = Blueprint('devices', __name__)

    @devices_bp.route('/')
    def dashboard():
        devices = discover_devices()
        return render_template('dashboard.html', devices=devices)

    @devices_bp.route('/device/<device_id>')
    def device_detail(device_id):
        device = get_device(device_id)
        return render_template('device_detail.html', device=device)
    '''),
            PROJECT_ROOT / "dlink_dashboard/routes/clients.py": textwrap.dedent(r'''
    from flask import Blueprint, render_template
    from dlink_dashboard.dlink.adapters import list_clients

    clients_bp = Blueprint('clients', __name__)

    @clients_bp.route('/device/<device_id>/clients')
    def clients(device_id):
        clients = list_clients(device_id)
        return render_template('clients.html', clients=clients, device_id=device_id)
    '''),
            PROJECT_ROOT / "dlink_dashboard/routes/status.py": textwrap.dedent(r'''
    from flask import Blueprint, render_template
    from dlink_dashboard.dlink.adapters import get_device_status

    status_bp = Blueprint('status', __name__)

    @status_bp.route('/device/<device_id>/status')
    def status(device_id):
        status = get_device_status(device_id)
        return render_template('status.html', status=status, device_id=device_id)
    '''),
            PROJECT_ROOT / "dlink_dashboard/dlink/adapters.py": textwrap.dedent(r'''
    import sys
    sys.path.append(str(__import__('pathlib').Path(__file__).parent.parent.parent))
    from DLink_Control import discover_devices, get_device, get_device_status, list_clients, reboot_device, set_config
    '''),
            PROJECT_ROOT / "dlink_dashboard/templates/dashboard.html": textwrap.dedent(r'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>D-LINK Dashboard</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>D-LINK Dashboard</h1>
        <ul>
        {% for device in devices %}
            <li><a href="/device/{{ device.id }}">{{ device.name }} ({{ device.model }})</a></li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''),
            PROJECT_ROOT / "dlink_dashboard/templates/device_detail.html": textwrap.dedent(r'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Device Detail</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h2>{{ device.name }} ({{ device.model }})</h2>
        <p>ID: {{ device.id }}</p>
        <a href="/device/{{ device.id }}/status">Status</a> |
        <a href="/device/{{ device.id }}/clients">Clients</a>
    </body>
    </html>
    '''),
            PROJECT_ROOT / "dlink_dashboard/templates/clients.html": textwrap.dedent(r'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Clients</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h2>Clients for Device {{ device_id }}</h2>
        <ul>
        {% for client in clients %}
            <li>{{ client.hostname }} ({{ client.mac }}) - IP: {{ client.ip }}, Signal: {{ client.signal }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''),
            PROJECT_ROOT / "dlink_dashboard/templates/status.html": textwrap.dedent(r'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Status</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h2>Status for Device {{ device_id }}</h2>
        <ul>
        {% for k, v in status.items() %}
            <li>{{ k }}: {{ v }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''),
            PROJECT_ROOT / "dlink_dashboard/static/style.css": textwrap.dedent(r'''
    body { font-family: Arial, sans-serif; background: #f8f8f8; color: #222; }
    h1, h2 { color: #0055a5; }
    a { color: #0077cc; text-decoration: none; }
    a:hover { text-decoration: underline; }
    ul { list-style: none; padding: 0; }
    li { margin: 0.5em 0; }
    '''),
        })

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with code {e.returncode}")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
