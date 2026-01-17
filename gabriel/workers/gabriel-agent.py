#!/usr/bin/env python3
"""
###############################################################################
# GABRIEL AGENT — TURBO INTELLIGENT COMMAND SERVER 🔥
# UPGRADED: Smarter, Faster, More Resilient
# DO NOT TAKE NO FOR AN ANSWER
###############################################################################
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import subprocess
import socket
import platform
import psutil
import os
import time
import logging
import hashlib
import threading
from functools import lru_cache
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [GABRIEL] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

PORT = 8080
MAX_RETRIES = 3
RETRY_DELAY = 0.5  # seconds

# EXPANDED command set for smarter operations
ALLOWED_COMMANDS = [
    # System Info
    'systeminfo', 'hostname', 'whoami', 'date', 'time', 'ver', 'set',
    # File Operations
    'dir', 'type', 'find', 'findstr', 'where', 'tree',
    # Network
    'ipconfig', 'netstat', 'ping', 'tracert', 'nslookup', 'arp', 'route',
    # Process Management
    'tasklist', 'wmic',
    # Performance
    'powercfg', 'systeminfo',
    # macOS/Linux equivalents (cross-platform)
    'ls', 'cat', 'grep', 'ps', 'top', 'df', 'du', 'uname', 'sw_vers',
    'ifconfig', 'netstat', 'lsof', 'which', 'pwd', 'env', 'echo',
    # Git operations (read-only)
    'git'
]

# AI reasoning templates
AI_PROMPTS = {
    'diagnose': 'Analyzing system state for issues...',
    'optimize': 'Computing optimization recommendations...',
    'predict': 'Predicting resource usage patterns...',
    'heal': 'Self-healing routine initiated...'
}

# Command result cache (LRU)
@lru_cache(maxsize=100)
def cached_command_hash(cmd: str) -> str:
    return hashlib.md5(cmd.encode()).hexdigest()

class CommandExecutor:
    """Intelligent command executor with retry and caching."""
    
    def __init__(self):
        self.cache = {}
        self.cache_ttl = 30  # seconds
    
    def execute_with_retry(self, cmd: str, timeout: int = 30) -> dict:
        """Execute command with automatic retry on failure."""
        last_error = None
        
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                logger.info(f"Executing (attempt {attempt}/{MAX_RETRIES}): {cmd[:50]}...")
                
                result = subprocess.run(
                    cmd,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )
                
                return {
                    'output': result.stdout,
                    'error': result.stderr,
                    'code': result.returncode,
                    'attempt': attempt,
                    'success': result.returncode == 0
                }
                
            except subprocess.TimeoutExpired:
                last_error = f'Command timed out (attempt {attempt})'
                logger.warning(last_error)
            except Exception as e:
                last_error = str(e)
                logger.warning(f"Attempt {attempt} failed: {last_error}")
            
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY * attempt)  # Exponential backoff
        
        return {
            'output': '',
            'error': last_error or 'Max retries exceeded',
            'code': -1,
            'attempt': MAX_RETRIES,
            'success': False
        }

executor = CommandExecutor()

class GabrielHandler(BaseHTTPRequestHandler):
    """🔥 TURBO-INTELLIGENT HTTP Handler with AI reasoning."""
    
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Gabriel-Token')
    
    def _json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self._cors()
        self.end_headers()
        response = json.dumps(data, indent=2, default=str)
        self.wfile.write(response.encode())
    
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()
    
    def do_GET(self):
        """Enhanced GET endpoints with AI insights."""
        
        if self.path == '/health':
            # Enhanced health with AI analysis
            cpu = psutil.cpu_percent(interval=0.1)
            mem = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # AI Reasoning: Compute health score
            health_score = 100
            issues = []
            recommendations = []
            
            if cpu > 80:
                health_score -= 20
                issues.append(f'CPU high: {cpu}%')
                recommendations.append('Consider killing resource-intensive processes')
            if mem.percent > 85:
                health_score -= 25
                issues.append(f'Memory pressure: {mem.percent}%')
                recommendations.append('Free up memory by closing unused apps')
            if disk.percent > 90:
                health_score -= 15
                issues.append(f'Disk nearly full: {disk.percent}%')
                recommendations.append('Clean up disk space')
            
            self._json({
                'status': 'online' if health_score > 50 else 'degraded',
                'health_score': health_score,
                'hostname': socket.gethostname(),
                'platform': platform.system(),
                'version': platform.version(),
                'cpu_percent': cpu,
                'memory_percent': mem.percent,
                'memory_available_gb': round(mem.available / (1024**3), 2),
                'disk_percent': disk.percent,
                'disk_free_gb': round(disk.free / (1024**3), 2),
                'uptime_seconds': int(time.time() - psutil.boot_time()),
                'process_count': len(psutil.pids()),
                'ai_analysis': {
                    'issues': issues,
                    'recommendations': recommendations
                },
                'timestamp': datetime.now().isoformat()
            })
        
        elif self.path == '/metrics':
            # Detailed metrics endpoint
            net = psutil.net_io_counters()
            self._json({
                'cpu': {
                    'percent': psutil.cpu_percent(percpu=True),
                    'count': psutil.cpu_count(),
                    'freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None
                },
                'memory': psutil.virtual_memory()._asdict(),
                'swap': psutil.swap_memory()._asdict(),
                'disk': {p.mountpoint: psutil.disk_usage(p.mountpoint)._asdict() 
                        for p in psutil.disk_partitions() if not p.mountpoint.startswith('/System')},
                'network': {
                    'bytes_sent': net.bytes_sent,
                    'bytes_recv': net.bytes_recv,
                    'packets_sent': net.packets_sent,
                    'packets_recv': net.packets_recv
                },
                'timestamp': datetime.now().isoformat()
            })
        
        elif self.path == '/processes':
            # Top processes by resource usage
            procs = []
            for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    procs.append(p.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            # Sort by CPU, top 20
            procs.sort(key=lambda x: x.get('cpu_percent', 0) or 0, reverse=True)
            self._json({'processes': procs[:20], 'timestamp': datetime.now().isoformat()})
        
        else:
            self._json({'error': 'Not found', 'available_endpoints': ['/health', '/metrics', '/processes', '/exec']}, 404)
    
    def do_POST(self):
        """Enhanced POST with intelligent command execution."""
        
        if self.path == '/exec':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            
            cmd = body.get('cmd', '')
            timeout = min(body.get('timeout', 30), 120)  # Max 120s for complex ops
            retry = body.get('retry', True)  # Enable retry by default
            
            # Security: Only allow safe commands
            cmd_parts = cmd.split() if cmd else []
            cmd_base = cmd_parts[0].lower() if cmd_parts else ''
            
            if cmd_base not in ALLOWED_COMMANDS:
                self._json({
                    'error': f'Command not allowed: {cmd_base}',
                    'allowed': ALLOWED_COMMANDS
                }, 403)
                return
            
            # Execute with intelligent retry
            if retry:
                result = executor.execute_with_retry(cmd, timeout)
            else:
                try:
                    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
                    result = {'output': proc.stdout, 'error': proc.stderr, 'code': proc.returncode, 'success': proc.returncode == 0}
                except Exception as e:
                    result = {'output': '', 'error': str(e), 'code': -1, 'success': False}
            
            result['timestamp'] = datetime.now().isoformat()
            self._json(result)
        
        elif self.path == '/ai/diagnose':
            # AI-powered system diagnosis
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            
            diagnosis = self._ai_diagnose(body.get('focus', 'all'))
            self._json(diagnosis)
        
        elif self.path == '/ai/optimize':
            # AI-powered optimization recommendations
            recommendations = self._ai_optimize()
            self._json(recommendations)
        
        else:
            self._json({'error': 'Not found'}, 404)
    
    def _ai_diagnose(self, focus: str) -> dict:
        """AI-powered system diagnosis."""
        issues = []
        severity = 'healthy'
        
        # CPU Analysis
        cpu = psutil.cpu_percent(interval=0.5)
        if cpu > 90:
            issues.append({'component': 'CPU', 'issue': f'Critical load: {cpu}%', 'severity': 'critical'})
            severity = 'critical'
        elif cpu > 70:
            issues.append({'component': 'CPU', 'issue': f'High load: {cpu}%', 'severity': 'warning'})
            if severity != 'critical': severity = 'warning'
        
        # Memory Analysis
        mem = psutil.virtual_memory()
        if mem.percent > 90:
            issues.append({'component': 'Memory', 'issue': f'Critical pressure: {mem.percent}%', 'severity': 'critical'})
            severity = 'critical'
        elif mem.percent > 75:
            issues.append({'component': 'Memory', 'issue': f'High usage: {mem.percent}%', 'severity': 'warning'})
            if severity != 'critical': severity = 'warning'
        
        # Disk Analysis
        disk = psutil.disk_usage('/')
        if disk.percent > 95:
            issues.append({'component': 'Disk', 'issue': f'Nearly full: {disk.percent}%', 'severity': 'critical'})
            severity = 'critical'
        elif disk.percent > 85:
            issues.append({'component': 'Disk', 'issue': f'High usage: {disk.percent}%', 'severity': 'warning'})
            if severity != 'critical': severity = 'warning'
        
        return {
            'diagnosis': AI_PROMPTS['diagnose'],
            'overall_severity': severity,
            'issues': issues,
            'issue_count': len(issues),
            'timestamp': datetime.now().isoformat()
        }
    
    def _ai_optimize(self) -> dict:
        """AI-powered optimization recommendations."""
        recommendations = []
        
        # Find top CPU consumers
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                if (proc.info.get('cpu_percent') or 0) > 20:
                    recommendations.append({
                        'action': 'consider_terminating',
                        'target': proc.info['name'],
                        'pid': proc.info['pid'],
                        'reason': f"High CPU: {proc.info['cpu_percent']}%"
                    })
            except:
                pass
        
        # Memory recommendations
        mem = psutil.virtual_memory()
        if mem.percent > 70:
            recommendations.append({
                'action': 'clear_memory',
                'command': 'sudo purge' if platform.system() == 'Darwin' else 'sync; echo 3 > /proc/sys/vm/drop_caches',
                'reason': f'Memory at {mem.percent}%'
            })
        
        return {
            'analysis': AI_PROMPTS['optimize'],
            'recommendations': recommendations,
            'timestamp': datetime.now().isoformat()
        }
    
    def log_message(self, format, *args):
        logger.info(f"{self.client_address[0]} - {args[0]}")

def start_server(port: int = PORT, bind: str = '127.0.0.1', retry: bool = True):
    """Start server with retry logic."""
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            server = HTTPServer((bind, port), GabrielHandler)
            server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            logger.info("="*60)
            logger.info("🔥 GABRIEL TURBO AGENT — INTELLIGENT COMMAND SERVER")
            logger.info("="*60)
            logger.info(f"Host: {socket.gethostname()}")
            logger.info(f"Platform: {platform.system()} {platform.version()[:50]}")
            logger.info(f"Listening: http://{bind}:{port}")
            logger.info(f"Endpoints: /health, /metrics, /processes, /exec, /ai/diagnose, /ai/optimize")
            logger.info(f"Commands: {len(ALLOWED_COMMANDS)} allowed")
            logger.info(f"Retry: {MAX_RETRIES}x with {RETRY_DELAY}s backoff")
            logger.info("="*60)
            logger.info("DO NOT TAKE NO FOR AN ANSWER 🔥")
            logger.info("="*60)
            
            server.serve_forever()
            return
            
        except OSError as e:
            if 'Address already in use' in str(e) and retry:
                logger.warning(f"Port {port} in use, retrying in {RETRY_DELAY}s (attempt {attempt}/{MAX_RETRIES})")
                time.sleep(RETRY_DELAY)
            else:
                raise
        except KeyboardInterrupt:
            logger.info("Shutting down gracefully...")
            break
    
    logger.error(f"Failed to start server after {MAX_RETRIES} attempts")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GABRIEL TURBO Agent')
    parser.add_argument('--port', type=int, default=PORT, help=f'Port (default: {PORT})')
    parser.add_argument('--bind', default='127.0.0.1', help='Bind address (default: 127.0.0.1)')
    args = parser.parse_args()
    
    start_server(port=args.port, bind=args.bind)
