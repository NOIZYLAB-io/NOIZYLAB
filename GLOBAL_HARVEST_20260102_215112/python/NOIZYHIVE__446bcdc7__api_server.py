#!/usr/bin/env python3
"""
NOIZYDIGGER High-Performance API Server
Fast, responsive, integrated with THE CIRCLE OF 8
"""

import http.server
import json
import os
import subprocess
import socket
import time
from datetime import datetime
from urllib.parse import parse_qs, urlparse
from http import HTTPStatus

PORT = int(os.environ.get('API_PORT', 8080))
VERSION = "2.0.0"

class NoizyAPIHandler(http.server.BaseHTTPRequestHandler):
    """Ultra-fast API handler for NOIZYDIGGER"""

    def log_message(self, format, *args):
        """Suppress default logging for speed"""
        pass

    def send_json(self, data, status=200):
        """Fast JSON response"""
        response = json.dumps(data).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(response))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('X-Powered-By', 'NOIZYDIGGER/2.0')
        self.end_headers()
        self.wfile.write(response)

    def send_html(self, html, status=200):
        """Fast HTML response"""
        response = html.encode()
        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(response))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        path = urlparse(self.path).path

        if path == '/':
            self.serve_dashboard()
        elif path == '/status':
            self.serve_status()
        elif path == '/health':
            self.serve_health()
        elif path == '/metrics':
            self.serve_metrics()
        elif path == '/api/circle8':
            self.serve_circle8()
        elif path == '/api/ollama':
            self.serve_ollama()
        elif path == '/api/tunnel':
            self.serve_tunnel_status()
        else:
            self.send_json({'error': 'Not found'}, 404)

    def do_POST(self):
        path = urlparse(self.path).path

        if path == '/api/command':
            self.handle_command()
        elif path == '/api/ai':
            self.handle_ai_request()
        else:
            self.send_json({'error': 'Not found'}, 404)

    def serve_dashboard(self):
        """Serve real-time dashboard"""
        html = '''<!DOCTYPE html>
<html>
<head>
    <title>NOIZYDIGGER - THE CIRCLE OF 8</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 100%);
            color: #fff;
            font-family: 'SF Mono', Monaco, monospace;
            min-height: 100vh;
            padding: 20px;
        }
        .header {
            text-align: center;
            padding: 30px 0;
            border-bottom: 1px solid #333;
            margin-bottom: 30px;
        }
        h1 {
            color: #00d4ff;
            font-size: 2.5em;
            text-shadow: 0 0 30px #00d4ff;
            letter-spacing: 3px;
        }
        .subtitle { color: #888; margin-top: 10px; }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }
        .card {
            background: rgba(20, 20, 30, 0.8);
            border: 1px solid #333;
            border-radius: 15px;
            padding: 25px;
            backdrop-filter: blur(10px);
        }
        .card h2 {
            color: #00ff88;
            font-size: 1.2em;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .status-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #222;
        }
        .status-item:last-child { border-bottom: none; }
        .online { color: #00ff88; }
        .offline { color: #ff4444; }
        .warning { color: #ffaa00; }
        .metric-value {
            font-size: 2em;
            color: #00d4ff;
            font-weight: bold;
        }
        .api-endpoint {
            background: #1a1a2e;
            padding: 8px 12px;
            border-radius: 5px;
            margin: 5px 0;
            font-size: 0.9em;
        }
        .method { color: #00ff88; font-weight: bold; }
        .pulse {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .refresh-btn {
            background: #00d4ff;
            color: #000;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-family: inherit;
            font-weight: bold;
        }
        .refresh-btn:hover { background: #00ff88; }
    </style>
</head>
<body>
    <div class="header">
        <h1>NOIZYDIGGER</h1>
        <p class="subtitle">THE CIRCLE OF 8 Control Node | <span class="online pulse">ONLINE</span></p>
    </div>

    <div class="grid">
        <div class="card">
            <h2>THE CIRCLE OF 8</h2>
            <div id="circle8">Loading...</div>
        </div>

        <div class="card">
            <h2>Tunnel Status</h2>
            <div id="tunnel">Loading...</div>
        </div>

        <div class="card">
            <h2>Ollama Models</h2>
            <div id="ollama">Loading...</div>
        </div>

        <div class="card">
            <h2>API Endpoints</h2>
            <div class="api-endpoint"><span class="method">GET</span> /status</div>
            <div class="api-endpoint"><span class="method">GET</span> /health</div>
            <div class="api-endpoint"><span class="method">GET</span> /metrics</div>
            <div class="api-endpoint"><span class="method">GET</span> /api/circle8</div>
            <div class="api-endpoint"><span class="method">GET</span> /api/ollama</div>
            <div class="api-endpoint"><span class="method">POST</span> /api/command</div>
            <div class="api-endpoint"><span class="method">POST</span> /api/ai</div>
        </div>

        <div class="card">
            <h2>System Metrics</h2>
            <div id="metrics">Loading...</div>
        </div>

        <div class="card">
            <h2>Quick Actions</h2>
            <button class="refresh-btn" onclick="refreshAll()">Refresh All</button>
        </div>
    </div>

    <script>
        async function fetchJSON(url) {
            try {
                const res = await fetch(url);
                return await res.json();
            } catch(e) {
                return {error: e.message};
            }
        }

        async function loadCircle8() {
            const data = await fetchJSON('/api/circle8');
            const el = document.getElementById('circle8');
            if (data.nodes) {
                el.innerHTML = data.nodes.map(n =>
                    `<div class="status-item">
                        <span>${n.icon} ${n.name}</span>
                        <span class="${n.status === 'HEALTHY' ? 'online' : 'offline'}">${n.status}</span>
                    </div>`
                ).join('');
            }
        }

        async function loadTunnel() {
            const data = await fetchJSON('/api/tunnel');
            const el = document.getElementById('tunnel');
            el.innerHTML = `
                <div class="status-item">
                    <span>Cloudflare Tunnel</span>
                    <span class="${data.tunnel ? 'online' : 'offline'}">${data.tunnel ? 'CONNECTED' : 'DISCONNECTED'}</span>
                </div>
                <div class="status-item">
                    <span>Local Server</span>
                    <span class="${data.server ? 'online' : 'offline'}">${data.server ? 'RUNNING' : 'STOPPED'}</span>
                </div>
                <div class="status-item">
                    <span>Domain</span>
                    <span>${data.domain}</span>
                </div>
            `;
        }

        async function loadOllama() {
            const data = await fetchJSON('/api/ollama');
            const el = document.getElementById('ollama');
            if (data.models) {
                el.innerHTML = data.models.map(m =>
                    `<div class="status-item">
                        <span>${m.name}</span>
                        <span>${m.size}</span>
                    </div>`
                ).join('');
            } else {
                el.innerHTML = '<span class="offline">Ollama not available</span>';
            }
        }

        async function loadMetrics() {
            const data = await fetchJSON('/metrics');
            const el = document.getElementById('metrics');
            el.innerHTML = `
                <div class="status-item">
                    <span>Uptime</span>
                    <span class="metric-value">${data.uptime || 'N/A'}</span>
                </div>
                <div class="status-item">
                    <span>Requests</span>
                    <span>${data.requests || 0}</span>
                </div>
            `;
        }

        function refreshAll() {
            loadCircle8();
            loadTunnel();
            loadOllama();
            loadMetrics();
        }

        refreshAll();
        setInterval(refreshAll, 10000);
    </script>
</body>
</html>'''
        self.send_html(html)

    def serve_status(self):
        """Quick status check"""
        self.send_json({
            'status': 'online',
            'node': 'GOD',
            'version': VERSION,
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        })

    def serve_health(self):
        """Health check endpoint"""
        tunnel_ok = self.check_process('cloudflared')
        ollama_ok = self.check_port(11434)

        status = 'healthy' if tunnel_ok and ollama_ok else 'degraded'

        self.send_json({
            'status': status,
            'checks': {
                'tunnel': tunnel_ok,
                'ollama': ollama_ok,
                'api': True
            },
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        })

    def serve_metrics(self):
        """Metrics endpoint"""
        self.send_json({
            'uptime': self.get_uptime(),
            'requests': 0,
            'version': VERSION
        })

    def serve_circle8(self):
        """THE CIRCLE OF 8 status"""
        nodes = [
            {'icon': '①', 'name': 'CLAUDE', 'status': 'HEALTHY'},
            {'icon': '②', 'name': 'M2G', 'status': 'HEALTHY' if os.path.exists(os.path.expanduser('~/m2g')) else 'STOPPED'},
            {'icon': '③', 'name': 'GABRIEL', 'status': 'HEALTHY'},
            {'icon': '④', 'name': 'ANTIGRAVITY', 'status': 'HEALTHY' if os.path.exists(os.path.expanduser('~/.antigravity')) else 'STOPPED'},
            {'icon': '⑤', 'name': 'SYNC', 'status': 'HEALTHY'},
            {'icon': '⑥', 'name': 'AUDIO', 'status': 'HEALTHY'},
            {'icon': '⑦', 'name': 'TUNNEL', 'status': 'HEALTHY' if self.check_process('cloudflared') else 'STOPPED'},
            {'icon': '⑧', 'name': 'VOICE', 'status': 'HEALTHY'},
        ]
        self.send_json({'nodes': nodes, 'power_level': sum(1 for n in nodes if n['status'] == 'HEALTHY')})

    def serve_ollama(self):
        """Ollama models endpoint"""
        try:
            result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, timeout=5)
            lines = result.stdout.strip().split('\n')[1:]
            models = []
            for line in lines:
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 3:
                        models.append({
                            'name': parts[0],
                            'id': parts[1] if len(parts) > 1 else '',
                            'size': parts[2] if len(parts) > 2 else ''
                        })
            self.send_json({'models': models, 'count': len(models)})
        except Exception as e:
            self.send_json({'error': str(e), 'models': []})

    def serve_tunnel_status(self):
        """Tunnel status endpoint"""
        self.send_json({
            'tunnel': self.check_process('cloudflared'),
            'server': self.check_port(PORT),
            'domain': os.environ.get('DOMAIN', 'god.noizy.ai'),
            'port': PORT
        })

    def handle_command(self):
        """Handle command execution"""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode()
        try:
            data = json.loads(body)
            cmd = data.get('command', '')
            if cmd in ['status', 'health', 'restart']:
                result = subprocess.run(
                    ['bash', os.path.expanduser('~/noizyhive/god/noizydigger.sh'), cmd],
                    capture_output=True, text=True, timeout=10
                )
                self.send_json({'output': result.stdout, 'error': result.stderr})
            else:
                self.send_json({'error': 'Command not allowed'}, 403)
        except Exception as e:
            self.send_json({'error': str(e)}, 500)

    def handle_ai_request(self):
        """Route AI request through ai-router"""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode()
        try:
            data = json.loads(body)
            prompt = data.get('prompt', '')
            result = subprocess.run(
                [os.path.expanduser('~/.local/bin/ai-router'), 'route', prompt],
                capture_output=True, text=True, timeout=60
            )
            self.send_json({'response': result.stdout, 'error': result.stderr})
        except Exception as e:
            self.send_json({'error': str(e)}, 500)

    def check_process(self, name):
        """Check if process is running"""
        try:
            result = subprocess.run(['pgrep', '-f', name], capture_output=True)
            return result.returncode == 0
        except:
            return False

    def check_port(self, port):
        """Check if port is listening"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('127.0.0.1', port))
            sock.close()
            return result == 0
        except:
            return False

    def get_uptime(self):
        """Get system uptime"""
        try:
            result = subprocess.run(['uptime'], capture_output=True, text=True)
            return result.stdout.strip().split('up ')[1].split(',')[0] if 'up' in result.stdout else 'N/A'
        except:
            return 'N/A'


def run_server():
    """Start the API server"""
    server = http.server.HTTPServer(('0.0.0.0', PORT), NoizyAPIHandler)
    print(f"NOIZYDIGGER API Server v{VERSION}")
    print(f"Listening on http://0.0.0.0:{PORT}")
    print(f"Dashboard: http://localhost:{PORT}")
    server.serve_forever()


if __name__ == '__main__':
    run_server()
