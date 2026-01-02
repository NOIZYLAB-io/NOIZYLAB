#!/usr/bin/env python3
"""
🔥🚀 MissionControl96 Hot-Rod Configuration System
Ultra-tight integration for DELL Inspiron 17 7779 & MacPro via Planar2495
"""

import json
import os
import socket
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path

import paramiko
import psutil
from flask import Flask, jsonify, render_template_string, request
from pysnmp.hlapi import *


# ---------- MISSIONCONTROL96 HOT-ROD CONFIG ----------
class MissionControl96Config:
    """Hot-Rod configuration for ultimate performance"""

    def __init__(self):
        # Core hardware configuration
        self.hardware_config = {
            "planar2495": {
                "display_name": "Planar PXL2495MW",
                "resolution": "2560x1440",
                "refresh_rate": "144Hz",  # Hot-rodded refresh rate
                "connection_type": "DisplayPort 1.4",
                "kvm_enabled": True,
                "hotkey_switch": "Scroll Lock x2",
                "usb_hub_ports": 4,
                "audio_passthrough": True,
            },
            "dell_inspiron_17_7779": {
                "display_name": "Dell Inspiron 17 7779 Gaming",
                "cpu": "Intel Core i7-7700HQ",
                "gpu": "NVIDIA GTX 1050 Ti 4GB",
                "ram": "16GB DDR4-2400",
                "storage": "256GB SSD + 1TB HDD",
                "ip_address": "192.168.0.122",
                "connection_priority": 1,  # Primary gaming workstation
                "performance_profile": "gaming_optimized",
                "display_port": "USB-C to DisplayPort",
                "power_profile": "high_performance",
            },
            "macpro": {
                "display_name": "Mac Pro (2019)",
                "cpu": "Intel Xeon W",
                "gpu": "AMD Radeon Pro",
                "ram": "32GB+ DDR4 ECC",
                "storage": "NVMe SSD Array",
                "ip_address": "192.168.0.123",
                "connection_priority": 2,  # Development powerhouse
                "performance_profile": "development_optimized",
                "display_port": "Thunderbolt 3 to DisplayPort",
                "power_profile": "balanced_performance",
            },
            "dgs_switch": {
                "model": "D-Link DGS-1024D",
                "ports": 24,
                "ip_address": "192.168.0.1",
                "role": "network_backbone",
                "priority_ports": [1, 2, 3],  # Hot-rod priority ports
            },
        }

        # Hot-rod performance settings
        self.performance_profiles = {
            "gaming_optimized": {
                "cpu_governor": "performance",
                "gpu_power_limit": 100,
                "memory_timing": "aggressive",
                "cooling_curve": "performance_quiet",
                "network_priority": "gaming",
            },
            "development_optimized": {
                "cpu_governor": "ondemand",
                "gpu_compute_mode": "enabled",
                "memory_management": "development",
                "io_scheduler": "deadline",
                "network_priority": "low_latency",
            },
        }

        # KVM switching configuration
        self.kvm_config = {
            "auto_switch_enabled": True,
            "switch_detection": "usb_activity",
            "fallback_timeout": 30,  # seconds
            "hotkey_combinations": {
                "dell_to_mac": "Scroll Lock + 1",
                "mac_to_dell": "Scroll Lock + 2",
                "toggle": "Scroll Lock x2",
            },
            "display_sync": True,
            "audio_follow_video": True,
            "usb_switching": "intelligent",  # Follow active session
        }


# ---------- HOT-ROD SYSTEM MANAGER ----------
class HotRodSystemManager:
    """Manages the hot-rodded MissionControl96 setup"""

    def __init__(self):
        self.config = MissionControl96Config()
        self.app = Flask(__name__)
        self.active_system = "dell_inspiron_17_7779"  # Default primary
        self.performance_mode = "hot_rod"
        self.data = {
            "dell": {},
            "macpro": {},
            "planar2495": {},
            "dgs": {},
            "kvm_status": {},
            "performance_stats": {},
            "hot_rod_metrics": {},
        }

        # Setup routes
        self.setup_routes()

        # Start monitoring threads
        self.start_monitoring()

    def setup_routes(self):
        """Setup Flask routes for hot-rod control"""

        @self.app.route("/")
        def dashboard():
            return render_template_string(self.get_hotrod_template())

        @self.app.route("/api/switch_system")
        def switch_system():
            """Switch between Dell and MacPro via KVM"""
            target = request.args.get("target", "dell")
            success = self.switch_kvm_system(target)
            return jsonify({"success": success, "active_system": self.active_system})

        @self.app.route("/api/performance_mode")
        def set_performance_mode():
            """Set performance mode for active system"""
            mode = request.args.get("mode", "balanced")
            success = self.set_performance_profile(mode)
            return jsonify({"success": success, "mode": mode})

        @self.app.route("/api/hot_rod_status")
        def hot_rod_status():
            """Get comprehensive hot-rod system status"""
            return jsonify(
                {
                    "active_system": self.active_system,
                    "performance_mode": self.performance_mode,
                    "data": self.data,
                    "planar_status": self.get_planar_status(),
                    "system_health": self.get_system_health(),
                }
            )

        @self.app.route("/api/optimize_display")
        def optimize_display():
            """Optimize Planar2495 settings for active system"""
            success = self.optimize_planar_display()
            return jsonify({"success": success, "optimized_for": self.active_system})

    def get_dell_metrics_hotrod(self):
        """Enhanced Dell Inspiron metrics for hot-rod setup"""
        try:
            config = self.config.hardware_config["dell_inspiron_17_7779"]

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                config["ip_address"],
                username=os.getenv("DELL_USER", "admin"),
                password=os.getenv("DELL_PASS", "password"),
                timeout=5,
            )

            # Enhanced monitoring commands for gaming performance
            cmds = {
                "cpu_usage": "wmic cpu get loadpercentage /value | findstr LoadPercentage",
                "gpu_usage": "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits",
                "gpu_temp": "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits",
                "ram_usage": "wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /value",
                "disk_performance": "wmic logicaldisk get size,freespace /value | findstr C:",
                "cpu_temp": "wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value",
                "power_profile": "powercfg /getactivescheme",
                "display_refresh": "wmic desktopmonitor get ScreenHeight,ScreenWidth /value",
            }

            result = {
                "system": "Dell Inspiron 17 7779",
                "status": (
                    "active"
                    if self.active_system == "dell_inspiron_17_7779"
                    else "standby"
                ),
                "performance_profile": config["performance_profile"],
                "connection_priority": config["connection_priority"],
            }

            for key, cmd in cmds.items():
                try:
                    _, stdout, _ = ssh.exec_command(cmd)
                    output = stdout.read().decode().strip()

                    if key == "cpu_usage":
                        result["cpu_percent"] = (
                            float(output.split("=")[1]) if "=" in output else 0
                        )
                    elif key == "gpu_usage":
                        result["gpu_percent"] = float(output) if output.isdigit() else 0
                    elif key == "gpu_temp":
                        result["gpu_temp"] = float(output) if output.isdigit() else 0
                    elif key == "ram_usage":
                        lines = output.split("\n")
                        total = free = 0
                        for line in lines:
                            if "TotalVisibleMemorySize=" in line:
                                total = float(line.split("=")[1])
                            elif "FreePhysicalMemory=" in line:
                                free = float(line.split("=")[1])
                        result["ram_percent"] = (
                            ((total - free) / total * 100) if total > 0 else 0
                        )
                    elif key == "cpu_temp":
                        if "CurrentTemperature=" in output:
                            temp_raw = float(output.split("=")[1])
                            result["cpu_temp"] = round(
                                (temp_raw / 10) - 273.15, 1
                            )  # Kelvin to Celsius
                    elif key == "power_profile":
                        result["power_scheme"] = (
                            "High Performance"
                            if "High performance" in output
                            else "Balanced"
                        )

                except Exception as e:
                    result[f"{key}_error"] = str(e)

            # Gaming performance metrics
            result["gaming_ready"] = (
                result.get("gpu_temp", 100) < 80
                and result.get("cpu_percent", 100) < 80
                and result.get("ram_percent", 100) < 85
            )

            ssh.close()
            return result

        except Exception as e:
            return {
                "error": str(e),
                "system": "Dell Inspiron 17 7779",
                "status": "offline",
            }

    def get_macpro_metrics_hotrod(self):
        """Enhanced MacPro metrics for hot-rod development setup"""
        try:
            config = self.config.hardware_config["macpro"]

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                config["ip_address"],
                username=os.getenv("MACPRO_USER", "admin"),
                password=os.getenv("MACPRO_PASS", "password"),
                timeout=5,
            )

            # Enhanced macOS monitoring for development workloads
            cmds = {
                "cpu_usage": "top -l 1 | grep 'CPU usage' | awk '{print $3}' | sed 's/%//'",
                "memory_pressure": "memory_pressure | grep 'System-wide memory free percentage'",
                "thermal_state": "pmset -g thermlog | tail -1",
                "gpu_activity": "system_profiler SPDisplaysDataType | grep 'Metal Support'",
                "disk_io": "iostat -d 1 2 | tail -1",
                "network_throughput": "netstat -bi | grep en0",
                "xcode_processes": "ps aux | grep -i xcode | grep -v grep | wc -l",
                "docker_containers": "docker ps -q | wc -l 2>/dev/null || echo 0",
                "development_load": "ps aux | grep -E '(node|python|java|swift)' | grep -v grep | wc -l",
            }

            result = {
                "system": "Mac Pro",
                "status": "active" if self.active_system == "macpro" else "standby",
                "performance_profile": config["performance_profile"],
                "connection_priority": config["connection_priority"],
            }

            for key, cmd in cmds.items():
                try:
                    _, stdout, _ = ssh.exec_command(cmd)
                    output = stdout.read().decode().strip()

                    if key == "cpu_usage":
                        result["cpu_percent"] = float(output) if output else 0
                    elif key == "memory_pressure":
                        if "%" in output:
                            result["memory_free_percent"] = float(
                                output.split(":")[1].strip().replace("%", "")
                            )
                    elif key == "thermal_state":
                        result["thermal_state"] = (
                            "Normal" if "Normal" in output else "Elevated"
                        )
                    elif key == "development_load":
                        result["dev_processes"] = int(output) if output.isdigit() else 0
                    elif key == "docker_containers":
                        result["docker_containers"] = (
                            int(output) if output.isdigit() else 0
                        )
                    elif key == "xcode_processes":
                        result["xcode_active"] = int(output) > 0

                except Exception as e:
                    result[f"{key}_error"] = str(e)

            # Development readiness score
            result["development_ready"] = (
                result.get("cpu_percent", 100) < 70
                and result.get("memory_free_percent", 0) > 20
                and result.get("thermal_state", "") == "Normal"
            )

            ssh.close()
            return result

        except Exception as e:
            return {"error": str(e), "system": "Mac Pro", "status": "offline"}

    def get_planar_status(self):
        """Get Planar2495 monitor status and KVM state"""
        config = self.config.hardware_config["planar2495"]
        kvm_config = self.config.kvm_config

        # Simulate Planar2495 status (would use DDC/CI commands in real implementation)
        planar_status = {
            "model": config["display_name"],
            "resolution": config["resolution"],
            "refresh_rate": config["refresh_rate"],
            "active_input": (
                "DisplayPort 1"
                if self.active_system == "dell_inspiron_17_7779"
                else "DisplayPort 2"
            ),
            "kvm_enabled": config["kvm_enabled"],
            "usb_hub_active": True,
            "audio_routing": self.active_system,
            "brightness": 85,  # Would read from DDC/CI
            "contrast": 75,
            "color_profile": (
                "Gaming" if self.active_system == "dell_inspiron_17_7779" else "sRGB"
            ),
            "response_time": (
                "1ms" if self.active_system == "dell_inspiron_17_7779" else "5ms"
            ),
            "overdrive": (
                "Strong" if self.active_system == "dell_inspiron_17_7779" else "Normal"
            ),
        }

        return planar_status

    def switch_kvm_system(self, target_system):
        """Switch KVM to target system"""
        try:
            if target_system in ["dell", "dell_inspiron_17_7779"]:
                self.active_system = "dell_inspiron_17_7779"
            elif target_system in ["mac", "macpro"]:
                self.active_system = "macpro"
            else:
                return False

            # In real implementation, would send DDC/CI commands to Planar2495
            # For now, just update internal state

            # Optimize display settings for new active system
            self.optimize_planar_display()

            return True

        except Exception as e:
            print(f"KVM switch failed: {e}")
            return False

    def optimize_planar_display(self):
        """Optimize Planar2495 settings for active system"""
        try:
            planar_config = self.config.hardware_config["planar2495"]

            if self.active_system == "dell_inspiron_17_7779":
                # Gaming optimization
                display_settings = {
                    "refresh_rate": "144Hz",
                    "response_time": "1ms",
                    "overdrive": "Strong",
                    "color_profile": "Gaming",
                    "brightness": 90,
                    "contrast": 80,
                    "gamma": 2.2,
                }
            else:  # macpro
                # Development/color accuracy optimization
                display_settings = {
                    "refresh_rate": "60Hz",
                    "response_time": "5ms",
                    "overdrive": "Normal",
                    "color_profile": "sRGB",
                    "brightness": 85,
                    "contrast": 75,
                    "gamma": 2.4,
                }

            # In real implementation, would use DDC/CI commands
            print(f"Optimizing Planar2495 for {self.active_system}: {display_settings}")

            return True

        except Exception as e:
            print(f"Display optimization failed: {e}")
            return False

    def set_performance_profile(self, mode):
        """Set performance profile for active system"""
        try:
            self.performance_mode = mode

            if self.active_system == "dell_inspiron_17_7779":
                # Dell gaming optimizations
                if mode == "hot_rod":
                    # Maximum gaming performance
                    commands = [
                        "powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c",  # High performance
                        "nvidia-smi -pl 100",  # Max GPU power
                        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f',
                    ]
                elif mode == "balanced":
                    commands = [
                        "powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e",  # Balanced
                        "nvidia-smi -pl 80",  # 80% GPU power
                    ]

            elif self.active_system == "macpro":
                # MacPro development optimizations
                if mode == "hot_rod":
                    commands = [
                        "sudo pmset -a perfbias 0",  # Maximum performance
                        "sudo sysctl -w kern.timer.coalescing_enabled=0",  # Reduce timer coalescing
                    ]
                elif mode == "balanced":
                    commands = [
                        "sudo pmset -a perfbias 5",  # Balanced performance
                        "sudo sysctl -w kern.timer.coalescing_enabled=1",
                    ]

            # Execute commands (would need proper SSH execution in real implementation)
            print(f"Setting {mode} performance profile for {self.active_system}")

            return True

        except Exception as e:
            print(f"Performance profile setting failed: {e}")
            return False

    def get_system_health(self):
        """Get overall system health metrics"""
        dell_data = self.data.get("dell", {})
        macpro_data = self.data.get("macpro", {})

        health = {
            "overall_status": "healthy",
            "dell_health": (
                "good" if dell_data.get("gaming_ready", False) else "warning"
            ),
            "macpro_health": (
                "good" if macpro_data.get("development_ready", False) else "warning"
            ),
            "planar_health": "excellent",  # Monitor is typically stable
            "network_health": "good",
            "kvm_health": "excellent",
            "recommendations": [],
        }

        # Generate health recommendations
        if dell_data.get("gpu_temp", 0) > 80:
            health["recommendations"].append("Dell GPU running hot - check cooling")

        if macpro_data.get("memory_free_percent", 100) < 15:
            health["recommendations"].append("MacPro low on memory - close unused apps")

        if not health["recommendations"]:
            health["recommendations"].append(
                "All systems operating within normal parameters"
            )

        return health

    def start_monitoring(self):
        """Start background monitoring threads"""

        def monitor_loop():
            while True:
                self.data["dell"] = self.get_dell_metrics_hotrod()
                self.data["macpro"] = self.get_macpro_metrics_hotrod()
                self.data["planar2495"] = self.get_planar_status()
                self.data["performance_stats"] = {
                    "active_system": self.active_system,
                    "performance_mode": self.performance_mode,
                    "uptime": time.time(),
                }
                time.sleep(5)  # Update every 5 seconds for hot-rod responsiveness

        monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitor_thread.start()

    def get_hotrod_template(self):
        """Enhanced HTML template for hot-rod dashboard"""
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>🔥 MissionControl96 Hot-Rod Dashboard 🔥</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a0a0a 100%);
            color: #e8e8e8;
            margin: 0;
            padding: 0;
        }
        
        .header {
            background: linear-gradient(90deg, #d4af37 0%, #f4d03f 50%, #d4af37 100%);
            color: #000;
            padding: 15px 30px;
            text-align: center;
            font-size: 1.5em;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        
        .hot-rod-controls {
            display: flex;
            justify-content: center;
            gap: 20px;
            padding: 20px;
            background: rgba(20, 20, 20, 0.8);
            border-bottom: 2px solid #d4af37;
        }
        
        .control-button {
            background: linear-gradient(145deg, #d4af37, #b8941f);
            border: none;
            color: #000;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            font-size: 14px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .control-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(212, 175, 55, 0.3);
        }
        
        .control-button.active {
            background: linear-gradient(145deg, #ff6b35, #f7931e);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 107, 53, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(255, 107, 53, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 107, 53, 0); }
        }
        
        .systems-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            padding: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .system-card {
            background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            border: 2px solid transparent;
            transition: all 0.3s ease;
        }
        
        .system-card.active {
            border-color: #d4af37;
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
        }
        
        .system-card.standby {
            opacity: 0.7;
            border-color: #555;
        }
        
        .system-title {
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 15px;
            color: #d4af37;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .status-badge {
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.8em;
            font-weight: bold;
        }
        
        .status-active {
            background: #28a745;
            color: white;
        }
        
        .status-standby {
            background: #6c757d;
            color: white;
        }
        
        .metric-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .metric-value {
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .metric-good { color: #28a745; }
        .metric-warning { color: #ffc107; }
        .metric-critical { color: #dc3545; }
        
        .planar-monitor {
            grid-column: 1 / -1;
            background: linear-gradient(145deg, #2a2a2a, #3a3a3a);
            border: 3px solid #d4af37;
        }
        
        .kvm-controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }
        
        .kvm-button {
            background: linear-gradient(145deg, #17a2b8, #138496);
            border: none;
            color: white;
            padding: 10px 20px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .performance-indicator {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 10px;
            padding: 10px;
            background: rgba(0,0,0,0.3);
            border-radius: 8px;
        }
        
        .performance-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            animation: blink 1.5s infinite;
        }
        
        .performance-dot.ready { background: #28a745; }
        .performance-dot.warning { background: #ffc107; }
        .performance-dot.critical { background: #dc3545; }
        
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0.3; }
        }
    </style>
    <meta http-equiv="refresh" content="5">
</head>
<body>
    <div class="header">
        🔥 MissionControl96 Hot-Rod Dashboard - Planar2495 KVM Command Center 🔥
    </div>
    
    <div class="hot-rod-controls">
        <button class="control-button" onclick="switchSystem('dell')">
            🎮 Activate Dell Gaming
        </button>
        <button class="control-button" onclick="switchSystem('mac')">
            💻 Activate MacPro Dev
        </button>
        <button class="control-button" onclick="setPerformance('hot_rod')">
            🔥 Hot-Rod Mode
        </button>
        <button class="control-button" onclick="setPerformance('balanced')">
            ⚖️ Balanced Mode
        </button>
        <button class="control-button" onclick="optimizeDisplay()">
            📺 Optimize Display
        </button>
    </div>
    
    <div class="systems-grid">
        <div class="system-card {{ 'active' if dell.status == 'active' else 'standby' }}">
            <div class="system-title">
                🎮 Dell Inspiron 17 7779 Gaming Rig
                <span class="status-badge {{ 'status-active' if dell.status == 'active' else 'status-standby' }}">
                    {{ dell.status|upper }}
                </span>
            </div>
            
            {% if dell.error %}
                <div style="color: #dc3545;">❌ {{ dell.error }}</div>
            {% else %}
                <div class="metric-row">
                    <span>CPU Usage:</span>
                    <span class="metric-value {{ 'metric-good' if dell.cpu_percent < 70 else 'metric-warning' if dell.cpu_percent < 85 else 'metric-critical' }}">
                        {{ "%.1f"|format(dell.cpu_percent) }}%
                    </span>
                </div>
                
                <div class="metric-row">
                    <span>GPU Usage:</span>
                    <span class="metric-value {{ 'metric-good' if dell.gpu_percent < 80 else 'metric-warning' if dell.gpu_percent < 95 else 'metric-critical' }}">
                        {{ dell.gpu_percent }}%
                    </span>
                </div>
                
                <div class="metric-row">
                    <span>GPU Temp:</span>
                    <span class="metric-value {{ 'metric-good' if dell.gpu_temp < 75 else 'metric-warning' if dell.gpu_temp < 85 else 'metric-critical' }}">
                        {{ dell.gpu_temp }}°C
                    </span>
                </div>
                
                <div class="metric-row">
                    <span>RAM Usage:</span>
                    <span class="metric-value {{ 'metric-good' if dell.ram_percent < 70 else 'metric-warning' if dell.ram_percent < 85 else 'metric-critical' }}">
                        {{ "%.1f"|format(dell.ram_percent) }}%
                    </span>
                </div>
                
                <div class="metric-row">
                    <span>Power Profile:</span>
                    <span class="metric-value">{{ dell.power_scheme|default('Unknown') }}</span>
                </div>
                
                <div class="performance-indicator">
                    <div class="performance-dot {{ 'ready' if dell.gaming_ready else 'warning' }}"></div>
                    <span>Gaming Ready: {{ '✅ YES' if dell.gaming_ready else '⚠️ CHECK TEMPS' }}</span>
                </div>
            {% endif %}
        </div>
        
        <div class="system-card {{ 'active' if macpro.status == 'active' else 'standby' }}">
            <div class="system-title">
                💻 Mac Pro Development Powerhouse
                <span class="status-badge {{ 'status-active' if macpro.status == 'active' else 'status-standby' }}">
                    {{ macpro.status|upper }}
                </span>
            </div>
            
            {% if macpro.error %}
                <div style="color: #dc3545;">❌ {{ macpro.error }}</div>
            {% else %}
                <div class="metric-row">
                    <span>CPU Usage:</span>
                    <span class="metric-value {{ 'metric-good' if macpro.cpu_percent < 60 else 'metric-warning' if macpro.cpu_percent < 80 else 'metric-critical' }}">
                        {{ "%.1f"|format(macpro.cpu_percent) }}%
                    </span>
                </div>
                
                <div class="metric-row">
                    <span>Memory Free:</span>
                    <span class="metric-value {{ 'metric-good' if macpro.memory_free_percent > 30 else 'metric-warning' if macpro.memory_free_percent > 15 else 'metric-critical' }}">
                        {{ "%.1f"|format(macpro.memory_free_percent|default(0)) }}%
                    </span>
                </div>
                
                <div class="metric-row">
                    <span>Thermal State:</span>
                    <span class="metric-value {{ 'metric-good' if macpro.thermal_state == 'Normal' else 'metric-warning' }}">
                        {{ macpro.thermal_state|default('Unknown') }}
                    </span>
                </div>
                
                <div class="metric-row">
                    <span>Dev Processes:</span>
                    <span class="metric-value">{{ macpro.dev_processes|default(0) }}</span>
                </div>
                
                <div class="metric-row">
                    <span>Xcode Active:</span>
                    <span class="metric-value">{{ '✅ YES' if macpro.xcode_active else '❌ NO' }}</span>
                </div>
                
                <div class="performance-indicator">
                    <div class="performance-dot {{ 'ready' if macpro.development_ready else 'warning' }}"></div>
                    <span>Dev Ready: {{ '✅ YES' if macpro.development_ready else '⚠️ CHECK RESOURCES' }}</span>
                </div>
            {% endif %}
        </div>
        
        <div class="system-card planar-monitor">
            <div class="system-title">
                📺 Planar PXL2495MW Hot-Rod Display & KVM Hub
                <span class="status-badge status-active">ACTIVE</span>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div>
                    <div class="metric-row">
                        <span>Resolution:</span>
                        <span class="metric-value metric-good">{{ planar.resolution }}</span>
                    </div>
                    
                    <div class="metric-row">
                        <span>Refresh Rate:</span>
                        <span class="metric-value metric-good">{{ planar.refresh_rate }}</span>
                    </div>
                    
                    <div class="metric-row">
                        <span>Active Input:</span>
                        <span class="metric-value metric-good">{{ planar.active_input }}</span>
                    </div>
                    
                    <div class="metric-row">
                        <span>Color Profile:</span>
                        <span class="metric-value">{{ planar.color_profile }}</span>
                    </div>
                </div>
                
                <div>
                    <div class="metric-row">
                        <span>Response Time:</span>
                        <span class="metric-value metric-good">{{ planar.response_time }}</span>
                    </div>
                    
                    <div class="metric-row">
                        <span>Overdrive:</span>
                        <span class="metric-value">{{ planar.overdrive }}</span>
                    </div>
                    
                    <div class="metric-row">
                        <span>Audio Routing:</span>
                        <span class="metric-value metric-good">{{ planar.audio_routing|title }}</span>
                    </div>
                    
                    <div class="metric-row">
                        <span>USB Hub:</span>
                        <span class="metric-value metric-good">{{ '✅ ACTIVE' if planar.usb_hub_active else '❌ INACTIVE' }}</span>
                    </div>
                </div>
            </div>
            
            <div class="kvm-controls">
                <button class="kvm-button" onclick="switchSystem('dell')">
                    🎮 Switch to Dell Gaming
                </button>
                <button class="kvm-button" onclick="switchSystem('mac')">
                    💻 Switch to MacPro Dev
                </button>
            </div>
        </div>
    </div>
    
    <script>
        function switchSystem(target) {
            fetch('/api/switch_system?target=' + target)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        setTimeout(() => location.reload(), 1000);
                    }
                });
        }
        
        function setPerformance(mode) {
            fetch('/api/performance_mode?mode=' + mode)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        setTimeout(() => location.reload(), 1000);
                    }
                });
        }
        
        function optimizeDisplay() {
            fetch('/api/optimize_display')
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Display optimized for ' + data.optimized_for);
                        setTimeout(() => location.reload(), 1000);
                    }
                });
        }
        
        // Update active system indicator
        setInterval(() => {
            fetch('/api/hot_rod_status')
                .then(response => response.json())
                .then(data => {
                    // Update UI elements based on status
                    console.log('Hot-rod status:', data);
                });
        }, 5000);
    </script>
</body>
</html>
        """

    def run(self, host="0.0.0.0", port=8500, debug=False):
        """Run the hot-rod dashboard"""
        print("🔥 Starting MissionControl96 Hot-Rod Dashboard")
        print(f"🚀 Access at http://localhost:{port}")
        print("💎 Planar2495 KVM integration active")
        print("🎮 Dell Inspiron 17 7779 gaming optimization ready")
        print("💻 Mac Pro development environment ready")

        self.app.run(host=host, port=port, debug=debug)


def main():
    """Main entry point"""
    # Load environment variables for credentials
    from dotenv import load_dotenv

    load_dotenv()

    # Create and run hot-rod system
    hot_rod = HotRodSystemManager()
    hot_rod.run()


if __name__ == "__main__":
    main()
