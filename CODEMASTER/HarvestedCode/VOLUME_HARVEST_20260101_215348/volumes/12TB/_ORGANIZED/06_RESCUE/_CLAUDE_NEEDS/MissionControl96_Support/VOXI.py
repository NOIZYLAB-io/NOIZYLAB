"""
setup_dlink_dashboard.py
Sets up a Flask-based D-Link Dashboard web app.
"""
import os
import sys
import subprocess
# Files to create
FILES = {
		# Backend engine (placeholder; replace with your real logic later)
		PROJECT_ROOT / "DLink_Control.py": textwrap.dedent(r"""
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
		"""),

		# Requirements
		REQ_FILE: textwrap.dedent(r"""
				Flask==3.0.0
				requests==2.32.3
				cachetools==5.3.3
				pyyaml==6.0.2
		"""),

		"""
		# Files to create
		# All imports and variables are defined at the top for clarity and maintainability
		"""
		FILES = {
			# Backend engine (placeholder; replace with your real logic later)
			PROJECT_ROOT / "DLink_Control.py": textwrap.dedent(r"""
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
			"""),
			# ...rest of FILES dictionary remains unchanged...
		}
				bp = Blueprint("devices", __name__)

				@bp.route("/")
				def index():
						devices = service.list_devices()
						return render_template("index.html", devices=devices)

				@bp.route("/device/<device_id>")
				def device(device_id):
						dev = service.device_detail(device_id)
						if not dev:
								abort(404)
						status = service.device_status(device_id)
						clients = service.device_clients(device_id)
						return render_template("device.html", device=dev, status=status, clients=clients)

				@bp.route("/clients/<device_id>")
				def clients(device_id):
						dev = service.device_detail(device_id)
						if not dev:
								abort(404)
						clients = service.device_clients(device_id)
						return render_template("clients.html", device=dev, clients=clients)
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "routes" / "actions.py": textwrap.dedent(r"""
				from flask import Blueprint, request, jsonify
				from ..dlink import service

				bp = Blueprint("actions", __name__, url_prefix="/api")

				@bp.post("/reboot/<device_id>")
				def reboot(device_id):
						result = service.reboot(device_id)
						return jsonify(result), (200 if result.get("ok") else 400)

				@bp.post("/config/<device_id>")
				def config(device_id):
						changes = request.get_json(force=True, silent=True) or {}
						result = service.apply_config(device_id, changes)
						return jsonify(result), (200 if result.get("ok") else 400)

				@bp.get("/status/<device_id>")
				def status(device_id):
						status = service.device_status(device_id)
						return jsonify(status.__dict__)

				@bp.get("/clients/<device_id>")
				def clients(device_id):
						clients = service.device_clients(device_id)
						return jsonify([c.__dict__ for c in clients])
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "dlink" / "__init__.py": "",
		PROJECT_ROOT / "dlink_dashboard" / "dlink" / "models.py": textwrap.dedent(r"""
				from dataclasses import dataclass
				from typing import Dict, List

				@dataclass
				class Device:
						id: str
						ip: str
						model: str
						name: str

				@dataclass
				class DeviceStatus:
						online: bool
						uptime: str
						cpu: int
						mem: int
						firmware: str
						wan: str

				@dataclass
				class Client:
						mac: str
						hostname: str
						ip: str
						signal: int

				def to_device(raw: Dict) -> Device:
						return Device(**raw)

				def to_status(raw: Dict) -> DeviceStatus:
						return DeviceStatus(**raw)

				def to_clients(raw_list: List[Dict]) -> List[Client]:
						return [Client(**c) for c in raw_list]
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "dlink" / "adapters.py": textwrap.dedent(r"""
				import DLink_Control
				from .models import to_device, to_status, to_clients

				def discover_devices():
						return [to_device(d) for d in DLink_Control.discover_devices()]

				def get_device(device_id: str):
						raw = DLink_Control.get_device(device_id)
						return to_device(raw) if raw else None

				def get_status(device_id: str):
						return to_status(DLink_Control.get_device_status(device_id))

				def get_clients(device_id: str):
						return to_clients(DLink_Control.list_clients(device_id))

				def reboot(device_id: str):
						return DLink_Control.reboot_device(device_id)

				def apply_config(device_id: str, changes: dict):
						return DLink_Control.set_config(device_id, changes)
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "dlink" / "service.py": textwrap.dedent(r"""
				from cachetools import TTLCache
				from . import adapters

				_device_cache = TTLCache(maxsize=64, ttl=10)
				_status_cache = TTLCache(maxsize=256, ttl=5)
				_clients_cache = TTLCache(maxsize=256, ttl=5)

				def list_devices():
						if "devices" in _device_cache:
								return _device_cache["devices"]
						devices = adapters.discover_devices()
						_device_cache["devices"] = devices
						return devices

				def device_detail(device_id: str):
						return adapters.get_device(device_id)

				def device_status(device_id: str):
						if device_id in _status_cache:
								return _status_cache[device_id]
						status = adapters.get_status(device_id)
						_status_cache[device_id] = status
						return status

				def device_clients(device_id: str):
						if device_id in _clients_cache:
								return _clients_cache[device_id]
						clients = adapters.get_clients(device_id)
						_clients_cache[device_id] = clients
						return clients

				def reboot(device_id: str):
						return adapters.reboot(device_id)

				def apply_config(device_id: str, changes: dict):
						return adapters.apply_config(device_id, changes)
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "templates" / "base.html": textwrap.dedent(r"""
				<!doctype html>
				<html lang="en">
				<head>
					<meta charset="utf-8">
					<title>D-LINK Dashboard</title>
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">
				</head>
				<body>
					<nav class="navbar">
						<a href="{{ url_for('devices.index') }}" class="brand">D-LINK Dashboard</a>
						<div class="spacer"></div>
						<span class="env">ENV: {{ config.get('ENV', 'dev') }}</span>
					</nav>
					<main class="container">
						{% include 'partials/flash.html' %}
						{% block content %}{% endblock %}
					</main>
					<script src="{{ url_for('static', filename='js/api.js') }}"></script>
					<script src="{{ url_for('static', filename='js/main.js') }}"></script>
				</body>
				</html>
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "templates" / "index.html": textwrap.dedent(r"""
				{% extends "base.html" %}
				{% block content %}
				<h1>Discovered devices</h1>
				<div class="grid">
					{% for d in devices %}
					<div class="card">
						<h2>{{ d.name }}</h2>
						<p><strong>Model:</strong> {{ d.model }}</p>
						<p><strong>IP:</strong> {{ d.ip }}</p>
						<div class="actions">
							<a class="btn" href="{{ url_for('devices.device', device_id=d.id) }}">View</a>
							<button class="btn danger" data-reboot="{{ d.id }}">Reboot</button>
						</div>
					</div>
					{% endfor %}
				</div>
				{% endblock %}
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "templates" / "device.html": textwrap.dedent(r"""
				{% extends "base.html" %}
				{% block content %}
				<h1>{{ device.name }} ({{ device.model }})</h1>

				<section class="status">
					<h2>Status</h2>
					<ul>
						<li><strong>Online:</strong> {{ 'Yes' if status.online else 'No' }}</li>
						<li><strong>Uptime:</strong> {{ status.uptime }}</li>
						<li><strong>CPU:</strong> {{ status.cpu }}%</li>
						<li><strong>Memory:</strong> {{ status.mem }}%</li>
						<li><strong>Firmware:</strong> {{ status.firmware }}</li>
						<li><strong>WAN:</strong> {{ status.wan }}</li>
					</ul>
				</section>

				<section class="clients">
					<h2>Connected clients</h2>
					<table>
						<thead>
							<tr><th>MAC</th><th>Hostname</th><th>IP</th><th>Signal</th></tr>
						</thead>
						<tbody>
							{% for c in clients %}
							<tr>
								<td>{{ c.mac }}</td>
								<td>{{ c.hostname }}</td>
								<td>{{ c.ip }}</td>
								<td>{{ c.signal }} dBm</td>
							</tr>
							{% endfor %}
						</tbody>
					</table>
				</section>

				<section class="config">
					<h2>Quick config</h2>
					<form id="config-form" data-device="{{ device.id }}">
						<label>
							<span>SSID</span>
							<input type="text" name="ssid" placeholder="New SSID">
						</label>
						<label>
							<span>Channel</span>
							<input type="number" name="channel" min="1" max="165">
						</label>
						<button type="submit" class="btn">Apply</button>
					</form>
				</section>

				<div class="row">
					<button class="btn danger" data-reboot="{{ device.id }}">Reboot device</button>
				</div>
				{% endblock %}
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "templates" / "clients.html": textwrap.dedent(r"""
				{% extends "base.html" %}
				{% block content %}
				<h1>Clients on {{ device.name }}</h1>
				<table>
					<thead>
						<tr><th>MAC</th><th>Hostname</th><th>IP</th><th>Signal</th></tr>
					</thead>
					<tbody>
						{% for c in clients %}
						<tr>
							<td>{{ c.mac }}</td>
							<td>{{ c.hostname }}</td>
							<td>{{ c.ip }}</td>
							<td>{{ c.signal }} dBm</td>
						</tr>
						{% endfor %}
					</tbody>
				</table>
				{% endblock %}
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "templates" / "partials" / "flash.html": textwrap.dedent(r"""
				{% with messages = get_flashed_messages() %}
					{% if messages %}
					<div class="flash">
						{% for m in messages %}<div class="flash-item">{{ m }}</div>{% endfor %}
					</div>
					{% endif %}
				{% endwith %}
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "static" / "css" / "styles.css": textwrap.dedent(r"""
				:root { --bg:#0b0f14; --fg:#eaeef2; --muted:#9ba7b2; --card:#141a21; --accent:#3aa3ff; --danger:#ff4d4f; }
				* { box-sizing: border-box; }
				body { margin:0; background:var(--bg); color:var(--fg); font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }
				.navbar { display:flex; align-items:center; padding:12px 16px; background:#0e1319; border-bottom:1px solid #1e2530; }
				.navbar .brand { color:var(--fg); text-decoration:none; font-weight:700; }
				.navbar .spacer { flex:1; }
				.container { padding:16px; }
				.grid { display:grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap:16px; }
				.card { background:var(--card); padding:16px; border-radius:10px; border:1px solid #1f2732; }
				.btn { background:var(--accent); color:#fff; border:none; padding:8px 12px; border-radius:6px; cursor:pointer; }
				.btn.danger { background:var(--danger); }
				.row { margin-top:16px; }
				table { width:100%; border-collapse: collapse; margin-top:8px; }
				th, td { padding:8px; border-bottom:1px solid #1e2530; text-align:left; }
				.status ul { list-style:none; padding:0; }
				.status li { margin:4px 0; color: var(--muted); }
				.flash { margin-bottom:12px; }
				.flash-item { background:#13304a; padding:8px; border-left:4px solid var(--accent); border-radius:6px; }
				label { display:block; margin:8px 0; }
				input[type="text"], input[type="number"] { width:100%; padding:8px; border-radius:6px; border:1px solid #2a3442; background:#0f141a; color:var(--fg); }
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "static" / "js" / "api.js": textwrap.dedent(r"""
				async function apiReboot(deviceId) {
					const res = await fetch(`/api/reboot/${deviceId}`, { method: 'POST' });
					return res.json();
				}

				async function apiApplyConfig(deviceId, payload) {
					const res = await fetch(`/api/config/${deviceId}`, {
						method: 'POST',
						headers: { 'Content-Type': 'application/json' },
						body: JSON.stringify(payload)
					});
					return res.json();
				}

				async function apiStatus(deviceId) {
					const res = await fetch(`/api/status/${deviceId}`);
					return res.json();
				}

				async function apiClients(deviceId) {
					const res = await fetch(`/api/clients/${deviceId}`);
					return res.json();
				}
		"""),

		PROJECT_ROOT / "dlink_dashboard" / "static" / "js" / "main.js": textwrap.dedent(r"""
				document.addEventListener('click', async (ev) => {
					const rebootId = ev.target.getAttribute('data-reboot');
					if (rebootId) {
						ev.preventDefault();
						const result = await apiReboot(rebootId);
						alert(result.message || (result.ok ? 'Reboot initiated' : 'Reboot failed'));
					}
				});

				document.addEventListener('submit', async (ev) => {
					const form = ev.target;
					if (form.id === 'config-form') {
						ev.preventDefault();
						const deviceId = form.getAttribute('data-device');
						const payload = Object.fromEntries(new FormData(form));
						const result = await apiApplyConfig(deviceId, payload);
						alert(result.ok ? 'Config applied' : `Failed: ${result.message || 'Unknown error'}`);
					}
				});
		"""),
}
REQUIRED_PACKAGES = ["flask"]
