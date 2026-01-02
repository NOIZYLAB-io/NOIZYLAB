#!/usr/bin/env python3
# ===============================================================
#  NOIZYLAB  |  Planar PXL2495MW Super-Control Surface
#  Hot-Rod Dashboard for 24" 1920x1200 Display Management
#  Connected via HDMI to OMEN Control Hub
# ===============================================================

import json
import os
import socket
import subprocess
import threading
import time
from datetime import datetime

import paramiko
import psutil
from flask import Flask, jsonify, render_template_string, request
from pysnmp.hlapi import *

# ===============================================================
#  PLANAR2495 SUPER-CONTROL CONFIGURATION
# ===============================================================

# Display Configuration
PLANAR_RESOLUTION = "1920x1200"  # 16:10 aspect ratio
PLANAR_REFRESH_RATE = "60Hz"
PLANAR_CONNECTION = "HDMI-1 (OMEN Control Hub)"

# System Endpoints
OMEN_IP = "10.0.0.121"
DELL_IP = "10.0.0.122"
MACPRO_IP = "10.0.0.123"
DGS_IP = "10.0.0.240"

# Credentials (Environment Variables)
OMEN_USER = os.getenv("OMEN_USER", "admin")
OMEN_PASS = os.getenv("OMEN_PASS", "password")
DELL_USER = os.getenv("DELL_USER", "gamer")
DELL_PASS = os.getenv("DELL_PASS", "password")
MACPRO_USER = os.getenv("MACPRO_USER", "developer")
MACPRO_PASS = os.getenv("MACPRO_PASS", "password")

# Network & SNMP
SNMP_COMM = "public"
REFRESH_SECS = 5

# Flask App
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Global Data Store
data = {
    "planar_status": "ACTIVE",
    "control_host": "OMEN",
    "last_update": datetime.now().isoformat(),
    "systems": {
        "omen": {"status": "unknown", "role": "Control Hub"},
        "dell": {"status": "unknown", "role": "Gaming Powerhouse"},
        "macpro": {"status": "unknown", "role": "Development Beast"},
        "macstudio": {"status": "active", "role": "Local Host"},
        "dgs": {"status": "unknown", "role": "Network Infrastructure"},
    },
    "network_map": {},
    "active_kvm_input": 1,  # 1=OMEN, 2=Dell, 3=MacPro
    "performance_profiles": {
        "gaming": {"active": False, "systems": ["dell", "omen"]},
        "development": {"active": False, "systems": ["macpro", "macstudio"]},
        "mixed": {"active": True, "systems": ["all"]},
    },
}

# ===============================================================
#  SYSTEM MONITORING FUNCTIONS
# ===============================================================


def get_local_system_metrics():
    """Get MacStudio (local) system metrics"""
    return {
        "hostname": socket.gethostname(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "cpu_temp": get_cpu_temperature(),
        "network_interfaces": len(psutil.net_if_addrs()),
        "processes": len(psutil.pids()),
        "uptime": get_system_uptime(),
        "load_avg": os.getloadavg() if hasattr(os, "getloadavg") else [0, 0, 0],
    }


def get_cpu_temperature():
    """Get CPU temperature on macOS"""
    try:
        result = subprocess.run(
            ["sysctl", "-n", "machdep.xcpm.cpu_thermal_state"],
            capture_output=True,
            text=True,
            timeout=2,
        )
        return float(result.stdout.strip()) if result.returncode == 0 else 0
    except:
        return 0


def get_system_uptime():
    """Get system uptime in hours"""
    try:
        result = subprocess.run(["uptime"], capture_output=True, text=True, timeout=2)
        if "day" in result.stdout:
            days = int(result.stdout.split("day")[0].split()[-1])
            return days * 24
        elif "hr" in result.stdout or ":" in result.stdout:
            return float(
                result.stdout.split("up")[1].split(",")[0].strip().replace(":", ".")
            )
        return 0
    except:
        return 0


def get_remote_system_metrics(ip, username, password, system_name):
    """Get metrics from remote system via SSH"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=5)

        metrics = {"status": "online", "error": None}

        if system_name in ["omen", "dell"]:  # Windows systems
            commands = {
                "cpu": 'wmic cpu get loadpercentage /value | findstr "="',
                "memory": 'wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /value | findstr "="',
                "disk": 'wmic logicaldisk get size,freespace /value | findstr "="',
                "gpu": "nvidia-smi --query-gpu=utilization.gpu,temperature.gpu --format=csv,noheader,nounits",
                "processes": 'tasklist | find /c /v ""',
            }
        else:  # macOS/Linux systems
            commands = {
                "cpu": "top -l 1 | grep 'CPU usage' | awk '{print $3}' | sed 's/%//'",
                "memory": "vm_stat | head -2 | tail -1 | awk '{print $2}' | sed 's/\\.//'",
                "disk": "df -h / | tail -1 | awk '{print $5}' | sed 's/%//'",
                "processes": "ps aux | wc -l",
            }

        for key, cmd in commands.items():
            try:
                stdin, stdout, stderr = ssh.exec_command(cmd)
                output = stdout.read().decode().strip()
                metrics[key] = parse_system_output(key, output, system_name)
            except Exception as e:
                metrics[f"{key}_error"] = str(e)

        ssh.close()
        return metrics

    except Exception as e:
        return {"status": "offline", "error": str(e)}


def parse_system_output(key, output, system_name):
    """Parse system command output based on key and system type"""
    try:
        if key == "cpu":
            if system_name in ["omen", "dell"]:
                return float(output.split("=")[1]) if "=" in output else 0
            else:
                return float(output) if output.replace(".", "").isdigit() else 0
        elif key == "memory":
            if system_name in ["omen", "dell"]:
                lines = output.split("\n")
                total = free = 0
                for line in lines:
                    if "TotalVisibleMemorySize" in line:
                        total = int(line.split("=")[1])
                    elif "FreePhysicalMemory" in line:
                        free = int(line.split("=")[1])
                return round((1 - free / total) * 100, 1) if total > 0 else 0
            else:
                return float(output) if output.replace(".", "").isdigit() else 0
        elif key == "disk":
            return float(output.replace("%", "")) if output else 0
        elif key == "processes":
            return int(output) if output.isdigit() else 0
        elif key == "gpu":
            parts = output.split(",")
            return {
                "usage": int(parts[0]) if len(parts) > 0 else 0,
                "temp": int(parts[1]) if len(parts) > 1 else 0,
            }
        else:
            return output
    except:
        return 0


def discover_network_devices():
    """Discover devices on the network"""
    devices = {}
    base_ip = "10.0.0."

    for i in [1, 3, 25, 121, 122, 123, 240]:
        ip = f"{base_ip}{i}"
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1000", ip], capture_output=True, timeout=2
            )
            if result.returncode == 0:
                device_info = identify_device(ip)
                devices[ip] = device_info
        except:
            pass

    return devices


def identify_device(ip):
    """Identify device type based on IP"""
    device_map = {
        "10.0.0.1": {"name": "Router/Gateway", "type": "Infrastructure", "priority": 1},
        "10.0.0.3": {"name": "Unknown Device", "type": "Network Device", "priority": 5},
        "10.0.0.25": {"name": "MacStudio Local", "type": "Workstation", "priority": 2},
        "10.0.0.121": {
            "name": "OMEN Control Hub",
            "type": "Control Center",
            "priority": 3,
        },
        "10.0.0.122": {
            "name": "Dell Gaming Rig",
            "type": "Gaming System",
            "priority": 4,
        },
        "10.0.0.123": {
            "name": "MacPro Development",
            "type": "Dev Workstation",
            "priority": 4,
        },
        "10.0.0.240": {
            "name": "D-LINK Switch",
            "type": "Network Switch",
            "priority": 2,
        },
    }

    return device_map.get(
        ip, {"name": f"Device {ip}", "type": "Unknown", "priority": 9}
    )


# ===============================================================
#  BACKGROUND DATA REFRESH
# ===============================================================


def refresh_system_data():
    """Background thread to refresh system data"""
    while True:
        try:
            # Update local system
            data["systems"]["macstudio"].update(get_local_system_metrics())

            # Update remote systems
            data["systems"]["omen"].update(
                get_remote_system_metrics(OMEN_IP, OMEN_USER, OMEN_PASS, "omen")
            )
            data["systems"]["dell"].update(
                get_remote_system_metrics(DELL_IP, DELL_USER, DELL_PASS, "dell")
            )
            data["systems"]["macpro"].update(
                get_remote_system_metrics(MACPRO_IP, MACPRO_USER, MACPRO_PASS, "macpro")
            )

            # Update network map
            data["network_map"] = discover_network_devices()
            data["last_update"] = datetime.now().isoformat()

        except Exception as e:
            print(f"Refresh error: {e}")

        time.sleep(REFRESH_SECS)


# Start background refresh
threading.Thread(target=refresh_system_data, daemon=True).start()

# ===============================================================
#  PLANAR SUPER-CONTROL SURFACE HTML TEMPLATE
# ===============================================================

PLANAR_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planar PXL2495MW - Super Control Surface</title>
    <style>
        * {margin:0; padding:0; box-sizing:border-box;}
        
        body {
            font-family: 'Segoe UI', 'SF Pro Display', system-ui, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
            color: #e0e0e0;
            overflow-x: hidden;
            min-height: 100vh;
        }
        
        /* Header Control Bar */
        .control-header {
            background: linear-gradient(90deg, #d4af37 0%, #f4d03f 50%, #d4af37 100%);
            color: #000;
            padding: 12px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: bold;
            font-size: 18px;
            box-shadow: 0 4px 20px rgba(212,175,55,0.3);
        }
        
        .control-title {
            font-size: 22px;
            font-weight: 900;
        }
        
        .control-status {
            display: flex;
            gap: 20px;
            font-size: 14px;
        }
        
        /* Main Grid Layout - Optimized for 1920x1200 */
        .super-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            grid-template-rows: auto auto auto;
            gap: 15px;
            padding: 20px;
            min-height: calc(100vh - 80px);
        }
        
        /* System Cards */
        .system-card {
            background: linear-gradient(145deg, #1e1e1e, #2a2a2a);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
            border: 2px solid transparent;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .system-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(212,175,55,0.2);
            border-color: #d4af37;
        }
        
        .system-card.online {
            border-left: 6px solid #00ff88;
        }
        
        .system-card.offline {
            border-left: 6px solid #ff4444;
        }
        
        .system-card.active-kvm {
            border: 3px solid #d4af37;
            background: linear-gradient(145deg, #2a2520, #3a3530);
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #444;
        }
        
        .card-title {
            font-size: 18px;
            font-weight: bold;
            color: #d4af37;
        }
        
        .card-role {
            font-size: 12px;
            color: #888;
            background: rgba(255,255,255,0.1);
            padding: 4px 8px;
            border-radius: 12px;
        }
        
        .metrics-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin: 15px 0;
        }
        
        .metric-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 12px;
            background: rgba(255,255,255,0.05);
            border-radius: 8px;
            font-size: 13px;
        }
        
        .metric-value {
            font-weight: bold;
            font-size: 16px;
        }
        
        .metric-value.good { color: #00ff88; }
        .metric-value.warning { color: #ffaa00; }
        .metric-value.critical { color: #ff4444; }
        
        /* Control Buttons */
        .control-buttons {
            display: flex;
            gap: 8px;
            margin-top: 15px;
        }
        
        .control-btn {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 8px;
            font-size: 12px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .control-btn.kvm {
            background: linear-gradient(45deg, #d4af37, #f4d03f);
            color: #000;
        }
        
        .control-btn.power {
            background: linear-gradient(45deg, #ff4444, #ff6666);
            color: #fff;
        }
        
        .control-btn.performance {
            background: linear-gradient(45deg, #00ff88, #44ffaa);
            color: #000;
        }
        
        .control-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        
        /* Network Overview */
        .network-overview {
            grid-column: 1 / -1;
            background: linear-gradient(145deg, #1a1a2e, #16213e);
            border-radius: 15px;
            padding: 20px;
            border: 2px solid #0066cc;
        }
        
        .network-title {
            font-size: 20px;
            color: #66ccff;
            margin-bottom: 15px;
            font-weight: bold;
        }
        
        .network-devices {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 12px;
        }
        
        .network-device {
            background: rgba(102,204,255,0.1);
            padding: 12px;
            border-radius: 8px;
            border-left: 4px solid #66ccff;
        }
        
        .device-ip {
            font-weight: bold;
            color: #66ccff;
        }
        
        .device-name {
            font-size: 12px;
            color: #ccc;
        }
        
        /* Performance Profiles */
        .performance-profiles {
            display: flex;
            gap: 10px;
            margin: 15px 0;
        }
        
        .profile-btn {
            flex: 1;
            padding: 12px;
            border: 2px solid #666;
            background: transparent;
            color: #ccc;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .profile-btn.active {
            border-color: #d4af37;
            background: rgba(212,175,55,0.2);
            color: #d4af37;
        }
        
        /* Status Indicators */
        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }
        
        .status-dot.online { background: #00ff88; }
        .status-dot.offline { background: #ff4444; }
        .status-dot.unknown { background: #666; }
        
        /* Auto-refresh indicator */
        .refresh-indicator {
            position: fixed;
            top: 20px;
            right: 20px;
            width: 10px;
            height: 10px;
            background: #00ff88;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
            100% { opacity: 1; transform: scale(1); }
        }
    </style>
    <meta http-equiv="refresh" content="{{refresh_rate}}">
</head>
<body>
    <!-- Auto-refresh indicator -->
    <div class="refresh-indicator"></div>
    
    <!-- Control Header -->
    <div class="control-header">
        <div class="control-title">
            📺 PLANAR PXL2495MW SUPER-CONTROL SURFACE
        </div>
        <div class="control-status">
            <span>🔌 {{planar_connection}}</span>
            <span>🎮 KVM Input: {{active_kvm_input}}</span>
            <span>⏱️ {{last_update_time}}</span>
        </div>
    </div>
    
    <!-- Main Control Grid -->
    <div class="super-grid">
        
        <!-- OMEN Control Hub -->
        <div class="system-card {{omen.status}} {{'active-kvm' if active_kvm_input == 1 else ''}}">
            <div class="card-header">
                <div class="card-title">⚡ OMEN Control Hub</div>
                <div class="card-role">{{omen.role}}</div>
            </div>
            
            {% if omen.get('error') or omen.get('status') == 'offline' %}
                <div class="metric-item">
                    <span>Status:</span>
                    <span class="metric-value critical">❌ {{omen.get('error', 'OFFLINE')}}</span>
                </div>
            {% else %}
                <div class="metrics-grid">
                    <div class="metric-item">
                        <span>CPU:</span>
                        <span class="metric-value {{'good' if (omen.get('cpu', 0)|int) < 70 else 'warning' if (omen.get('cpu', 0)|int) < 90 else 'critical'}}">{{omen.get('cpu', 0)}}%</span>
                    </div>
                    <div class="metric-item">
                        <span>Memory:</span>
                        <span class="metric-value {{'good' if (omen.get('memory', 0)|int) < 80 else 'warning' if (omen.get('memory', 0)|int) < 95 else 'critical'}}">{{omen.get('memory', 0)}}%</span>
                    </div>
                    <div class="metric-item">
                        <span>Disk:</span>
                        <span class="metric-value {{'good' if (omen.get('disk', 0)|int) < 80 else 'warning'}}">{{omen.get('disk', 0)}}%</span>
                    </div>
                    <div class="metric-item">
                        <span>Processes:</span>
                        <span class="metric-value">{{omen.get('processes', 0)}}</span>
                    </div>
                </div>
            {% endif %}
            
            <div class="control-buttons">
                <button class="control-btn kvm" onclick="switchKVM(1)">🎯 ACTIVATE KVM</button>
                <button class="control-btn performance" onclick="optimizeSystem('omen')">🔥 OPTIMIZE</button>
            </div>
        </div>
        
        <!-- Dell Gaming Rig -->
        <div class="system-card {{dell.status}} {{'active-kvm' if active_kvm_input == 2 else ''}}">
            <div class="card-header">
                <div class="card-title">🎮 Dell Gaming Beast</div>
                <div class="card-role">{{dell.role}}</div>
            </div>
            
            {% if dell.get('error') or dell.get('status') == 'offline' %}
                <div class="metric-item">
                    <span>Status:</span>
                    <span class="metric-value critical">❌ {{dell.get('error', 'OFFLINE')}}</span>
                </div>
            {% else %}
                <div class="metrics-grid">
                    <div class="metric-item">
                        <span>CPU:</span>
                        <span class="metric-value {{'good' if (dell.get('cpu', 0)|int) < 70 else 'warning' if (dell.get('cpu', 0)|int) < 90 else 'critical'}}">{{dell.get('cpu', 0)}}%</span>
                    </div>
                    <div class="metric-item">
                        <span>Memory:</span>
                        <span class="metric-value {{'good' if (dell.get('memory', 0)|int) < 80 else 'warning' if (dell.get('memory', 0)|int) < 95 else 'critical'}}">{{dell.get('memory', 0)}}%</span>
                    </div>
                    {% if dell.get('gpu') %}
                    <div class="metric-item">
                        <span>GPU Usage:</span>
                        <span class="metric-value {{'good' if (dell.gpu.get('usage', 0)|int) < 80 else 'warning'}}">{{dell.gpu.get('usage', 0)}}%</span>
                    </div>
                    <div class="metric-item">
                        <span>GPU Temp:</span>
                        <span class="metric-value {{'good' if (dell.gpu.get('temp', 0)|int) < 75 else 'warning' if (dell.gpu.get('temp', 0)|int) < 85 else 'critical'}}">{{dell.gpu.get('temp', 0)}}°C</span>
                    </div>
                    {% endif %}
                </div>
            {% endif %}
            
            <div class="control-buttons">
                <button class="control-btn kvm" onclick="switchKVM(2)">🎯 SWITCH TO GAMING</button>
                <button class="control-btn performance" onclick="optimizeSystem('dell')">🚀 GAME MODE</button>
            </div>
        </div>
        
        <!-- MacPro Development -->
        <div class="system-card {{macpro.status}} {{'active-kvm' if active_kvm_input == 3 else ''}}">
            <div class="card-header">
                <div class="card-title">💻 MacPro Development</div>
                <div class="card-role">{{macpro.role}}</div>
            </div>
            
            {% if macpro.get('error') or macpro.get('status') == 'offline' %}
                <div class="metric-item">
                    <span>Status:</span>
                    <span class="metric-value critical">❌ {{macpro.get('error', 'OFFLINE')}}</span>
                </div>
            {% else %}
                <div class="metrics-grid">
                    <div class="metric-item">
                        <span>CPU:</span>
                        <span class="metric-value {{'good' if (macpro.get('cpu', 0)|int) < 60 else 'warning' if (macpro.get('cpu', 0)|int) < 80 else 'critical'}}">{{macpro.get('cpu', 0)}}%</span>
                    </div>
                    <div class="metric-item">
                        <span>Memory:</span>
                        <span class="metric-value {{'good' if (macpro.get('memory', 0)|int) < 70 else 'warning' if (macpro.get('memory', 0)|int) < 90 else 'critical'}}">{{macpro.get('memory', 0)}}%</span>
                    </div>
                    <div class="metric-item">
                        <span>Disk:</span>
                        <span class="metric-value {{'good' if (macpro.get('disk', 0)|int) < 80 else 'warning'}}">{{macpro.get('disk', 0)}}%</span>
                    </div>
                    <div class="metric-item">
                        <span>Processes:</span>
                        <span class="metric-value">{{macpro.get('processes', 0)}}</span>
                    </div>
                </div>
            {% endif %}
            
            <div class="control-buttons">
                <button class="control-btn kvm" onclick="switchKVM(3)">🎯 SWITCH TO DEV</button>
                <button class="control-btn performance" onclick="optimizeSystem('macpro')">🔥 DEV MODE</button>
            </div>
        </div>
        
        <!-- Local MacStudio -->
        <div class="system-card online">
            <div class="card-header">
                <div class="card-title">🏠 MacStudio Local</div>
                <div class="card-role">{{macstudio.role}}</div>
            </div>
            
            <div class="metrics-grid">
                <div class="metric-item">
                    <span>CPU:</span>
                    <span class="metric-value {{'good' if macstudio.cpu_percent < 70 else 'warning' if macstudio.cpu_percent < 90 else 'critical'}}">{{macstudio.cpu_percent|round(1)}}%</span>
                </div>
                <div class="metric-item">
                    <span>Memory:</span>
                    <span class="metric-value {{'good' if macstudio.memory_percent < 80 else 'warning' if macstudio.memory_percent < 95 else 'critical'}}">{{macstudio.memory_percent|round(1)}}%</span>
                </div>
                <div class="metric-item">
                    <span>Disk:</span>
                    <span class="metric-value {{'good' if macstudio.disk_percent < 80 else 'warning'}}">{{macstudio.disk_percent|round(1)}}%</span>
                </div>
                <div class="metric-item">
                    <span>Uptime:</span>
                    <span class="metric-value">{{macstudio.uptime|round(1)}}h</span>
                </div>
            </div>
            
            <div class="control-buttons">
                <button class="control-btn performance" onclick="optimizeSystem('local')">⚡ OPTIMIZE LOCAL</button>
                <button class="control-btn kvm" onclick="showDashboard()">📊 MAIN DASHBOARD</button>
            </div>
        </div>
        
        <!-- Performance Profiles -->
        <div class="system-card">
            <div class="card-header">
                <div class="card-title">🎯 Performance Profiles</div>
                <div class="card-role">System Optimization</div>
            </div>
            
            <div class="performance-profiles">
                <button class="profile-btn {{'active' if performance_profiles.gaming.active else ''}}" onclick="setProfile('gaming')">
                    🎮 GAMING
                </button>
                <button class="profile-btn {{'active' if performance_profiles.development.active else ''}}" onclick="setProfile('development')">
                    💻 DEVELOPMENT  
                </button>
                <button class="profile-btn {{'active' if performance_profiles.mixed.active else ''}}" onclick="setProfile('mixed')">
                    🔄 MIXED
                </button>
            </div>
            
            <div class="metrics-grid">
                <div class="metric-item">
                    <span>Active Systems:</span>
                    <span class="metric-value">{{active_systems_count}}</span>
                </div>
                <div class="metric-item">
                    <span>Network Load:</span>
                    <span class="metric-value good">{{network_load}}%</span>
                </div>
                <div class="metric-item">
                    <span>KVM Switch:</span>
                    <span class="metric-value">Input {{active_kvm_input}}</span>
                </div>
                <div class="metric-item">
                    <span>Planar Display:</span>
                    <span class="metric-value good">{{planar_resolution}}</span>
                </div>
            </div>
        </div>
        
        <!-- System Control Panel -->
        <div class="system-card">
            <div class="card-header">
                <div class="card-title">🔧 System Control</div>
                <div class="card-role">Hot-Rod Management</div>
            </div>
            
            <div class="control-buttons">
                <button class="control-btn power" onclick="wakeAllSystems()">🚨 WAKE ALL</button>
                <button class="control-btn performance" onclick="turboMode()">🔥 TURBO MODE</button>
            </div>
            
            <div class="control-buttons">
                <button class="control-btn kvm" onclick="cycleKVM()">🔄 CYCLE KVM</button>
                <button class="control-btn performance" onclick="refreshAll()">🔄 REFRESH ALL</button>
            </div>
            
            <div class="metric-item" style="margin-top: 15px;">
                <span>Last Update:</span>
                <span class="metric-value">{{last_update_short}}</span>
            </div>
        </div>
        
        <!-- Network Overview -->
        <div class="network-overview">
            <div class="network-title">🌐 Network Infrastructure Status</div>
            <div class="network-devices">
                {% for ip, device in network_map.items() %}
                <div class="network-device">
                    <div class="device-ip">{{ip}}</div>
                    <div class="device-name">{{device.name}} - {{device.type}}</div>
                </div>
                {% endfor %}
            </div>
        </div>
        
    </div>
    
    <!-- JavaScript Controls -->
    <script>
        function switchKVM(input) {
            fetch('/api/kvm-switch', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({input: input})
            }).then(response => response.json())
              .then(data => {
                  if (data.success) {
                      location.reload();
                  }
              });
        }
        
        function optimizeSystem(system) {
            fetch('/api/optimize', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({system: system})
            }).then(response => response.json())
              .then(data => alert('Optimization ' + (data.success ? 'Started' : 'Failed')));
        }
        
        function setProfile(profile) {
            fetch('/api/profile', {
                method: 'POST', 
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({profile: profile})
            }).then(response => response.json())
              .then(data => {
                  if (data.success) {
                      location.reload();
                  }
              });
        }
        
        function wakeAllSystems() {
            if (confirm('Wake up all sleeping systems?')) {
                fetch('/api/wake-all', {method: 'POST'})
                    .then(response => response.json())
                    .then(data => alert('Wake command sent to all systems'));
            }
        }
        
        function turboMode() {
            fetch('/api/turbo-mode', {method: 'POST'})
                .then(response => response.json())
                .then(data => alert('Turbo mode ' + (data.success ? 'activated' : 'failed')));
        }
        
        function cycleKVM() {
            fetch('/api/cycle-kvm', {method: 'POST'})
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        location.reload();
                    }
                });
        }
        
        function refreshAll() {
            location.reload();
        }
        
        function showDashboard() {
            window.open('http://localhost:8500', '_blank');
        }
    </script>
</body>
</html>
"""

# ===============================================================
#  FLASK ROUTES
# ===============================================================


@app.route("/")
def index():
    """Main Planar Super-Control Surface"""

    # Calculate derived metrics
    active_systems = sum(
        1 for sys in data["systems"].values() if sys.get("status") == "online"
    )

    template_data = {
        "refresh_rate": REFRESH_SECS,
        "planar_connection": PLANAR_CONNECTION,
        "planar_resolution": PLANAR_RESOLUTION,
        "active_kvm_input": data["active_kvm_input"],
        "last_update_time": datetime.now().strftime("%H:%M:%S"),
        "last_update_short": datetime.now().strftime("%H:%M"),
        "active_systems_count": active_systems,
        "network_load": min(active_systems * 15, 100),  # Estimated
        "omen": data["systems"]["omen"],
        "dell": data["systems"]["dell"],
        "macpro": data["systems"]["macpro"],
        "macstudio": data["systems"]["macstudio"],
        "performance_profiles": data["performance_profiles"],
        "network_map": data["network_map"],
    }

    return render_template_string(PLANAR_HTML, **template_data)


@app.route("/api/kvm-switch", methods=["POST"])
def api_kvm_switch():
    """Switch KVM input"""
    try:
        input_num = request.json.get("input", 1)
        data["active_kvm_input"] = input_num

        # Here you would send actual KVM switch commands
        # For now, just simulate the switch
        print(f"Switching KVM to input {input_num}")

        return jsonify({"success": True, "input": input_num})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/api/optimize", methods=["POST"])
def api_optimize():
    """Optimize specific system"""
    try:
        system = request.json.get("system")
        print(f"Optimizing system: {system}")

        # Here you would run system-specific optimization commands
        # For now, just simulate

        return jsonify({"success": True, "system": system})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/api/profile", methods=["POST"])
def api_set_profile():
    """Set performance profile"""
    try:
        profile = request.json.get("profile")

        # Reset all profiles
        for p in data["performance_profiles"]:
            data["performance_profiles"][p]["active"] = False

        # Activate selected profile
        if profile in data["performance_profiles"]:
            data["performance_profiles"][profile]["active"] = True

        return jsonify({"success": True, "profile": profile})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/api/wake-all", methods=["POST"])
def api_wake_all():
    """Wake all sleeping systems"""
    try:
        # Here you would run wake commands for each system
        print("Sending wake commands to all systems...")
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/api/turbo-mode", methods=["POST"])
def api_turbo_mode():
    """Activate turbo mode across all systems"""
    try:
        print("Activating turbo mode...")
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/api/cycle-kvm", methods=["POST"])
def api_cycle_kvm():
    """Cycle through KVM inputs"""
    try:
        current = data["active_kvm_input"]
        next_input = (current % 3) + 1
        data["active_kvm_input"] = next_input

        return jsonify({"success": True, "input": next_input})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


# ===============================================================
#  MAIN ENTRY POINT
# ===============================================================

if __name__ == "__main__":
    print(
        f"""
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀

    📺 PLANAR PXL2495MW SUPER-CONTROL SURFACE
    🔥 Hot-Rod Dashboard for Maximum System Control
    
    ⚡ Resolution: {PLANAR_RESOLUTION} @ {PLANAR_REFRESH_RATE}
    🔌 Connection: {PLANAR_CONNECTION}
    🎯 Optimized for: Multi-System KVM Management
    
    🌐 Super-Control Interface: http://localhost:8501
    📊 Network Range: 10.0.0.x
    🔄 Auto-Refresh: {REFRESH_SECS} seconds
    
    🎮 Systems Under Control:
    ⚡ OMEN Control Hub (10.0.0.121)
    🎮 Dell Gaming Rig (10.0.0.122) 
    💻 MacPro Development (10.0.0.123)
    🏠 MacStudio Local (Dashboard Host)
    
    🔥 PLANAR2495 HOT-ROD MODE: ACTIVATED!
    
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
    """
    )

    app.run(host="0.0.0.0", port=8501, debug=False)
