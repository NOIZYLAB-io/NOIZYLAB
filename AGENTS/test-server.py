#!/usr/bin/env python3
"""
Local test server to demonstrate cloud agent delegation
Simulates the Cloudflare Worker running locally for testing
"""

import json
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import traceback

# Cloud Agents implementation (matches TypeScript version)
class CloudAgents:
    @staticmethod
    def system_guardian(action, params=None):
        params = params or {}
        if action == 'status':
            return {
                'uptime': 1736976000000,
                'health': 'healthy',
                'services': ['monitoring', 'alerts']
            }
        elif action == 'monitor':
            return {
                'cpu': 'normal',
                'memory': 'normal',
                'disk': 'normal'
            }
        else:
            raise Exception(f'Unknown action: {action}')
    
    @staticmethod
    def mc96(action, params=None):
        params = params or {}
        if action == 'organize':
            return {
                'organized': True,
                'filesProcessed': 0,
                'message': 'Cloud organization completed'
            }
        elif action == 'vault-status':
            return {
                'vaultHealth': 'ok',
                'totalFiles': 0
            }
        else:
            raise Exception(f'Unknown action: {action}')
    
    @staticmethod
    def gabriel(action, params=None):
        params = params or {}
        if action == 'health':
            return {
                'status': 'online',
                'capabilities': ['voice', 'ui', 'automation']
            }
        elif action == 'execute':
            return {
                'executed': True,
                'command': params.get('command', 'none')
            }
        else:
            raise Exception(f'Unknown action: {action}')

# Map agent names to functions
CLOUD_AGENTS = {
    'systemGuardian': CloudAgents.system_guardian,
    'mc96': CloudAgents.mc96,
    'gabriel': CloudAgents.gabriel
}

class WorkerHandler(BaseHTTPRequestHandler):
    def _cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    
    def _json_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self._cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
    
    def _text_response(self, text, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'text/plain')
        self._cors_headers()
        self.end_headers()
        self.wfile.write(text.encode())
    
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors_headers()
        self.end_headers()
    
    def do_GET(self):
        path = urlparse(self.path).path
        
        if path == '/health':
            self._json_response({
                'status': 'ok',
                'env': 'local-test',
                'timestamp': '2026-01-25T07:37:52.000Z'
            })
        elif path == '/agent/list':
            self._json_response({
                'agents': list(CLOUD_AGENTS.keys()),
                'endpoint': '/agent/delegate',
                'timestamp': '2026-01-25T07:37:52.000Z'
            })
        else:
            self._text_response(
                "NOIZYLAB Worker is running 🚀\n\n"
                "Endpoints:\n"
                "- GET  /health\n"
                "- GET  /agent/list\n"
                "- POST /agent/delegate"
            )
    
    def do_POST(self):
        path = urlparse(self.path).path
        
        if path == '/agent/delegate':
            try:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                task = json.loads(body)
                
                agent = task.get('agent')
                action = task.get('action')
                params = task.get('params', {})
                
                if not agent or not action:
                    self._json_response({
                        'success': False,
                        'error': 'Missing required fields: agent, action'
                    }, 400)
                    return
                
                if agent not in CLOUD_AGENTS:
                    self._json_response({
                        'success': False,
                        'error': f'Unknown agent: {agent}. Available: {", ".join(CLOUD_AGENTS.keys())}'
                    }, 404)
                    return
                
                agent_func = CLOUD_AGENTS[agent]
                result = agent_func(action, params)
                
                self._json_response({
                    'success': True,
                    'agent': agent,
                    'action': action,
                    'result': result,
                    'timestamp': '2026-01-25T07:37:52.000Z'
                })
            except Exception as e:
                traceback.print_exc()
                self._json_response({
                    'success': False,
                    'agent': 'unknown',
                    'action': 'unknown',
                    'error': str(e),
                    'timestamp': '2026-01-25T07:37:52.000Z'
                }, 500)
        else:
            self._json_response({
                'error': 'Not found'
            }, 404)
    
    def log_message(self, format, *args):
        # Custom logging
        print(f"[{self.command}] {format % args}")

def main():
    port = 8787  # Default Cloudflare Workers dev port
    server = HTTPServer(('localhost', port), WorkerHandler)
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║   🌐 NOIZYLAB Cloud Worker - Local Test Server               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print(f"\n✅ Server running at http://localhost:{port}")
    print("\nEndpoints:")
    print(f"  - GET  http://localhost:{port}/health")
    print(f"  - GET  http://localhost:{port}/agent/list")
    print(f"  - POST http://localhost:{port}/agent/delegate")
    print("\nPress Ctrl+C to stop\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        sys.exit(0)

if __name__ == '__main__':
    main()
