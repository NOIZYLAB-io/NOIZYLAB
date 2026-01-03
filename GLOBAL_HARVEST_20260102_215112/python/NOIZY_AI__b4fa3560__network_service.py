#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════╗
║  GABRIEL Network Service HYPER - Backend API v2.0                      ║
║  Enhanced network monitoring and backup orchestration                  ║
║  DGS-1210-10 Smart Switch Integration                                  ║
╚════════════════════════════════════════════════════════════════════════╝
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import json
from pathlib import Path
import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for WebAvatar access

# Configuration
BACKUP_SCRIPT = Path(__file__).parent.parent / "network_backup.py"
BACKUP_DIR = Path(__file__).parent / "NetworkBackups"
LOG_FILE = BACKUP_DIR / "backup_log.txt"
SWITCH_IP = os.getenv("SWITCH_IP", "192.168.0.2")

@app.route('/api/network/status', methods=['GET'])
def get_service_status():
    """Enhanced service health check with switch status"""
    try:
        # Check if backup script exists
        script_exists = BACKUP_SCRIPT.exists()
        
        # Check backup directory
        backup_dir_exists = BACKUP_DIR.exists()
        backup_count = len(list(BACKUP_DIR.glob("DGS1210_CFG_*.cfg"))) if backup_dir_exists else 0
        
        # Get last backup time
        last_backup = "Never"
        if backup_dir_exists:
            backups = sorted(BACKUP_DIR.glob("DGS1210_CFG_*.cfg"))
            if backups:
                last_backup = datetime.datetime.fromtimestamp(
                    backups[-1].stat().st_mtime
                ).strftime("%Y-%m-%d %H:%M:%S")
        
        return jsonify({
            'service': 'network_monitor_hyper',
            'version': '2.0',
            'status': 'online',
            'switch_ip': SWITCH_IP,
            'switch_online': True,  # Would ping in production
            'ports_active': 8,
            'backup_script_available': script_exists,
            'backup_directory': str(BACKUP_DIR),
            'backup_count': backup_count,
            'last_backup': last_backup,
            'timestamp': datetime.datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'service': 'network_monitor_hyper',
            'status': 'error',
            'error': str(e)
        }), 500

@app.route('/api/network/backup', methods=['POST'])
def trigger_backup():
    """Trigger network backup script with enhanced logging"""
    try:
        print(f"🌐 Backup request received at {datetime.datetime.now()}")
        
        # Ensure backup directory exists
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        
        # Run network_backup.py
        result = subprocess.run(
            ['python3', str(BACKUP_SCRIPT)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Parse result
        success = result.returncode == 0
        
        # Find most recent backup file
        backup_files = sorted(BACKUP_DIR.glob("DGS1210_CFG_*.cfg"))
        latest_file = backup_files[-1].name if backup_files else None
        latest_size = backup_files[-1].stat().st_size if backup_files else 0
        
        response_data = {
            'success': success,
            'message': 'Backup completed successfully' if success else 'Backup failed',
            'backup_file': latest_file,
            'backup_size': f"{latest_size / 1024:.2f} KB" if latest_size else "0 KB",
            'output': result.stdout,
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        print(f"✅ Backup {'successful' if success else 'failed'}: {latest_file}")
        
        return jsonify(response_data)
        
    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'message': 'Backup timeout - switch may be unreachable',
            'error': 'Timeout after 30 seconds'
        }), 408
        
    except Exception as e:
        print(f"❌ Backup error: {e}")
        return jsonify({
            'success': False,
            'message': 'Backup failed with error',
            'error': str(e)
        }), 500

@app.route('/api/network/switch/<switch_ip>', methods=['GET'])
def get_switch_status(switch_ip):
    """Get switch status (would query actual switch in production)"""
    # In production, this would query the actual switch
    # For now, return mock data
    return jsonify({
        'ip': switch_ip,
        'model': 'DGS-1210-10',
        'status': 'online',
        'uptime': '15 days, 8 hours',
        'firmware': '6.10.012',
        'temperature': '42°C',
        'ports_active': 8,
        'ports_total': 10,
        'bandwidth_in': '12.5 Mbps',
        'bandwidth_out': '8.2 Mbps'
    })

@app.route('/api/network/switch/<switch_ip>/ports', methods=['GET'])
def get_port_status(switch_ip):
    """Get port status for switch"""
    return jsonify({
        'ports': [
            {'id': 1, 'status': 'up', 'speed': '1000M', 'mode': 'auto', 'device': 'Server'},
            {'id': 2, 'status': 'up', 'speed': '1000M', 'mode': 'auto', 'device': 'NAS'},
            {'id': 3, 'status': 'up', 'speed': '100M', 'mode': 'auto', 'device': 'Camera 1'},
            {'id': 4, 'status': 'up', 'speed': '100M', 'mode': 'auto', 'device': 'Camera 2'},
            {'id': 5, 'status': 'up', 'speed': '1000M', 'mode': 'auto', 'device': 'Desktop'},
            {'id': 6, 'status': 'up', 'speed': '1000M', 'mode': 'auto', 'device': 'Laptop'},
            {'id': 7, 'status': 'up', 'speed': '1000M', 'mode': 'auto', 'device': 'AP'},
            {'id': 8, 'status': 'up', 'speed': '100M', 'mode': 'auto', 'device': 'IoT Hub'},
            {'id': 9, 'status': 'down', 'speed': '-', 'mode': 'auto', 'device': 'Unused'},
            {'id': 10, 'status': 'down', 'speed': '-', 'mode': 'auto', 'device': 'Unused'}
        ]
    })

@app.route('/api/network/history', methods=['GET'])
def get_backup_history():
    """Get backup history from log file and directory"""
    try:
        backups = []
        
        # Get all backup files
        if BACKUP_DIR.exists():
            backup_files = sorted(BACKUP_DIR.glob("DGS1210_CFG_*.cfg"), reverse=True)
            
            for backup_file in backup_files[:20]:  # Last 20 backups
                stat = backup_file.stat()
                backups.append({
                    'filename': backup_file.name,
                    'timestamp': datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                    'size': f"{stat.st_size / 1024:.2f} KB",
                    'size_bytes': stat.st_size
                })
        
        # Get log entries
        logs = []
        if LOG_FILE.exists():
            with open(LOG_FILE, 'r') as f:
                logs = [line.strip() for line in f.readlines()[-50:]]  # Last 50 log entries
        
        return jsonify({
            'backups': backups,
            'logs': logs,
            'total_backups': len(backups),
            'backup_dir': str(BACKUP_DIR)
        })
            
    except Exception as e:
        return jsonify({
            'backups': [],
            'logs': [],
            'error': str(e)
        }), 500

@app.route('/api/network/health', methods=['GET'])
def get_network_health():
    """Get comprehensive network health metrics"""
    try:
        health = {
            'overall_status': 'healthy',
            'checks': []
        }
        
        # Check 1: Backup script exists
        health['checks'].append({
            'name': 'Backup Script',
            'status': 'pass' if BACKUP_SCRIPT.exists() else 'fail',
            'message': 'Backup script is accessible' if BACKUP_SCRIPT.exists() else 'Backup script not found'
        })
        
        # Check 2: Backup directory accessible
        health['checks'].append({
            'name': 'Backup Directory',
            'status': 'pass' if BACKUP_DIR.exists() else 'fail',
            'message': f'Directory accessible: {BACKUP_DIR}' if BACKUP_DIR.exists() else 'Directory not accessible'
        })
        
        # Check 3: Recent backup exists (within 7 days)
        if BACKUP_DIR.exists():
            backups = sorted(BACKUP_DIR.glob("DGS1210_CFG_*.cfg"))
            if backups:
                last_backup_time = datetime.datetime.fromtimestamp(backups[-1].stat().st_mtime)
                age_days = (datetime.datetime.now() - last_backup_time).days
                
                health['checks'].append({
                    'name': 'Recent Backup',
                    'status': 'pass' if age_days <= 7 else 'warn',
                    'message': f'Last backup {age_days} days ago',
                    'last_backup': last_backup_time.strftime("%Y-%m-%d %H:%M:%S")
                })
            else:
                health['checks'].append({
                    'name': 'Recent Backup',
                    'status': 'warn',
                    'message': 'No backups found'
                })
        
        # Set overall status
        if any(c['status'] == 'fail' for c in health['checks']):
            health['overall_status'] = 'unhealthy'
        elif any(c['status'] == 'warn' for c in health['checks']):
            health['overall_status'] = 'warning'
        
        return jsonify(health)
        
    except Exception as e:
        return jsonify({
            'overall_status': 'error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║  🌐 GABRIEL Network Service HYPER v2.0                   ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print(f"\n📍 Starting on http://localhost:5010")
    print(f"🔧 Switch IP: {SWITCH_IP}")
    print(f"💾 Backup Dir: {BACKUP_DIR}")
    print(f"📜 Backup Script: {BACKUP_SCRIPT}")
    print(f"\n✨ API Endpoints:")
    print(f"   GET  /api/network/status   - Service & switch status")
    print(f"   POST /api/network/backup   - Trigger backup")
    print(f"   GET  /api/network/history  - Backup history")
    print(f"   GET  /api/network/health   - Health check")
    print(f"   GET  /api/network/switch/<ip> - Switch details")
    print(f"   GET  /api/network/switch/<ip>/ports - Port status")
    print(f"\n🚀 Ready for requests!\n")
    
    app.run(host='0.0.0.0', port=5010, debug=False)

