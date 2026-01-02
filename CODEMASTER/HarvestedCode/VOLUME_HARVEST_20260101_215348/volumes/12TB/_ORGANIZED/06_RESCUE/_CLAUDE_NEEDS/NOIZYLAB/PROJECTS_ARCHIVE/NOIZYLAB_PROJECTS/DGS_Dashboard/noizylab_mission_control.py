#!/usr/bin/env python3
# ===============================================================
#  NOIZYLAB  |  Mission Control Dashboard
#  Local Flask dashboard that merges Mac, OMEN, and DGS metrics
# ===============================================================

import json
import os
import socket
import subprocess
import threading
import time

import paramiko
import psutil
from flask import Flask, render_template_string
from pysnmp.hlapi import *

# ---------- MISSIONCONTROL96 HOT-ROD CONFIG ----------
# Enhanced configuration for tighter Dell Inspiron 17 7779 & MacPro integration via Planar2495
OMEN_IP = "10.0.0.121"
OMEN_USER = "YourWindowsUser"
OMEN_PASS = "YourPassword"

# Dell Inspiron 17 7779 Gaming Rig - Connected to Planar2495 DisplayPort 1
DELL_IP = "10.0.0.122"
DELL_USER = os.getenv("DELL_HOTROD_USER", "gamer")
DELL_PASS = os.getenv("DELL_HOTROD_PASS", "YourPassword")
DELL_MODEL = "Dell Inspiron 17 7779"
DELL_SPECS = {
    "cpu": "Intel Core i7-7700HQ (4C/8T @ 2.8-3.8GHz)",
    "gpu": "NVIDIA GeForce GTX 1050 Ti 4GB GDDR5",
    "ram": "16GB DDR4-2400 (2x8GB)",
    "storage": "256GB NVMe SSD + 1TB 5400RPM HDD",
    "display_out": "USB-C to DisplayPort (Planar2495)",
    "kvm_priority": 1,
    "performance_mode": "gaming_hotrod",
}

# MacPro Development Beast - Connected to Planar2495 DisplayPort 2
MACPRO_IP = "10.0.0.123"
MACPRO_USER = os.getenv("MACPRO_HOTROD_USER", "developer")
MACPRO_PASS = os.getenv("MACPRO_HOTROD_PASS", "YourPassword")
MACPRO_MODEL = "Mac Pro (2019)"
MACPRO_SPECS = {
    "cpu": "Intel Xeon W (8-28 cores)",
    "gpu": "AMD Radeon Pro 580X/Vega II",
    "ram": "32GB+ DDR4 ECC (up to 1.5TB)",
    "storage": "NVMe SSD Array (up to 8TB)",
    "display_out": "Thunderbolt 3 to DisplayPort (Planar2495)",
    "kvm_priority": 2,
    "performance_mode": "development_hotrod",
}

# Planar PXL2495MW - Hot-Rodded Display & KVM Hub
PLANAR2495_CONFIG = {
    "model": "Planar PXL2495MW",
    "resolution": "2560x1440",
    "refresh_rate": "144Hz (hot-rodded from 75Hz)",
    "panel_type": "IPS with LED backlight",
    "response_time": "1ms (overdrive) / 5ms (standard)",
    "connectivity": ["2x DisplayPort 1.4", "1x HDMI 2.0", "4x USB 3.0 Hub"],
    "kvm_switching": "Hardware KVM with hotkeys",
    "audio_routing": "Follows video input",
    "vesa_mount": "100x100mm",
    "power_consumption": "65W (hot-rod optimized)",
}

DGS_IP = "10.0.0.1"
SNMP_COMM = "public"
REFRESH_SECS = 5  # Faster refresh for hot-rod responsiveness

# Hot-Rod Performance Tracking
ACTIVE_SYSTEM = "dell"  # 'dell' or 'macpro' - tracks which system is active via KVM
PERFORMANCE_MODE = "hotrod"  # 'hotrod', 'balanced', or 'eco'
KVM_LAST_SWITCH = None
# -----------------------------------------------------

app = Flask(__name__)

data = {
    "mac": {},
    "omen": {},
    "dell": {},
    "macpro": {},
    "dgs": {},
    "network_devices": {},
    "log": [],
}


# ---------- MAC METRICS ----------
def get_mac_metrics():
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }


# ---------- OMEN METRICS ----------
def get_omen_metrics():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(OMEN_IP, username=OMEN_USER, password=OMEN_PASS, timeout=5)
        cmds = {
            "cpu": "wmic cpu get loadpercentage | findstr [0-9]",
            "ram": "powershell -command \"(Get-Counter '\\\\Memory\\\\Available MBytes').CounterSamples.CookedValue\"",
            "disk": 'powershell -command "(Get-PSDrive C).Used / (Get-PSDrive C).Free * 100"',
        }
        result = {}
        for k, c in cmds.items():
            stdin, stdout, stderr = ssh.exec_command(c)
            out = stdout.read().decode().strip().splitlines()
            if out:
                result[k] = float(out[0])
        ssh.close()
        return result
    except Exception as e:
        return {"error": str(e)}


# ---------- DELL INSPIRON 17 7779 HOT-ROD METRICS ----------
def get_dell_metrics():
    """Enhanced Dell Inspiron 17 7779 metrics for hot-rod gaming setup"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(DELL_IP, username=DELL_USER, password=DELL_PASS, timeout=5)

        # Enhanced gaming-focused monitoring commands
        cmds = {
            "cpu_usage": "wmic cpu get loadpercentage /value | findstr LoadPercentage",
            "cpu_freq": "wmic cpu get CurrentClockSpeed /value | findstr CurrentClockSpeed",
            "gpu_usage": "nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits 2>nul || echo 0",
            "gpu_temp": "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits 2>nul || echo 0",
            "gpu_power": "nvidia-smi --query-gpu=power.draw --format=csv,noheader,nounits 2>nul || echo 0",
            "gpu_memory": "nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits 2>nul || echo 0,0",
            "ram_usage": "wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /value",
            "disk_c_usage": 'powershell -command "Get-PSDrive C | ForEach-Object {[math]::Round(($_.Used/($_.Used+$_.Free))*100,1)}"',
            "cpu_temp": "wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value | findstr CurrentTemperature",
            "power_plan": "powercfg /getactivescheme | findstr GUID",
            "display_info": "wmic desktopmonitor get ScreenHeight,ScreenWidth /value",
            "network_adapter": "wmic path win32_networkadapter where NetEnabled=true get Speed /value | findstr Speed",
            "usb_devices": 'wmic path Win32_USBControllerDevice get Dependent /value | find "USB" | find /c /v ""',
            "planar_connection": "powershell -command \"Get-PnpDevice | Where-Object {$_.FriendlyName -like '*Display*' -or $_.FriendlyName -like '*Monitor*'} | Select-Object FriendlyName,Status\"",
        }

        result = {
            "system": DELL_MODEL,
            "specs": DELL_SPECS,
            "kvm_active": ACTIVE_SYSTEM == "dell",
            "performance_mode": PERFORMANCE_MODE,
            "planar_input": "DisplayPort 1" if ACTIVE_SYSTEM == "dell" else "Standby",
        }

        for k, c in cmds.items():
            try:
                _, stdout, _ = ssh.exec_command(c)
                out = stdout.read().decode().strip()

                if k == "cpu_usage":
                    if "LoadPercentage=" in out:
                        result["cpu_percent"] = float(out.split("=")[1])
                elif k == "cpu_freq":
                    if "CurrentClockSpeed=" in out:
                        result["cpu_freq_mhz"] = float(out.split("=")[1])
                elif k == "gpu_usage":
                    result["gpu_percent"] = float(out) if out.isdigit() else 0
                elif k == "gpu_temp":
                    result["gpu_temp"] = float(out) if out.isdigit() else 0
                elif k == "gpu_power":
                    result["gpu_power_watts"] = (
                        float(out.replace(" W", "")) if "W" in out else 0
                    )
                elif k == "gpu_memory":
                    if "," in out:
                        used, total = out.split(",")
                        result["gpu_memory_used_mb"] = (
                            float(used) if used.isdigit() else 0
                        )
                        result["gpu_memory_total_mb"] = (
                            float(total) if total.isdigit() else 0
                        )
                        if float(total) > 0:
                            result["gpu_memory_percent"] = round(
                                (float(used) / float(total)) * 100, 1
                            )
                elif k == "ram_usage":
                    lines = out.split("\n")
                    total = free = 0
                    for line in lines:
                        if "TotalVisibleMemorySize=" in line:
                            total = float(line.split("=")[1])
                        elif "FreePhysicalMemory=" in line:
                            free = float(line.split("=")[1])
                    if total > 0:
                        result["ram_percent"] = round(((total - free) / total) * 100, 1)
                        result["ram_used_gb"] = round((total - free) / 1024 / 1024, 1)
                        result["ram_total_gb"] = round(total / 1024 / 1024, 1)
                elif k == "disk_c_usage":
                    result["disk_c_percent"] = (
                        float(out) if out.replace(".", "").isdigit() else 0
                    )
                elif k == "cpu_temp":
                    if "CurrentTemperature=" in out:
                        temp_raw = float(out.split("=")[1])
                        result["cpu_temp"] = round((temp_raw / 10) - 273.15, 1)
                elif k == "power_plan":
                    if "High performance" in out:
                        result["power_plan"] = "High Performance"
                    elif "Balanced" in out:
                        result["power_plan"] = "Balanced"
                    else:
                        result["power_plan"] = "Power Saver"
                elif k == "usb_devices":
                    result["usb_devices_connected"] = int(out) if out.isdigit() else 0
            except Exception as e:
                result[f"{k}_error"] = str(e)

        # Gaming readiness assessment
        result["gaming_ready"] = (
            result.get("gpu_temp", 100) < 80
            and result.get("cpu_percent", 100) < 85
            and result.get("ram_percent", 100) < 90
            and result.get("power_plan", "") == "High Performance"
        )

        # Hot-rod status indicators
        result["hotrod_optimized"] = (
            result.get("gpu_power_watts", 0) > 50  # GPU drawing good power
            and result.get("cpu_freq_mhz", 0) > 2500  # CPU running at good speed
            and result["gaming_ready"]
        )

        ssh.close()
        return result

    except Exception as e:
        return {
            "error": str(e),
            "system": DELL_MODEL,
            "kvm_active": False,
            "status": "offline",
        }


# ---------- MACPRO HOT-ROD DEVELOPMENT METRICS ----------
def get_macpro_metrics():
    """🚀 HOT-ROD MacPro Development Workstation - XCode & VS22 Optimized"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(MACPRO_IP, username=MACPRO_USER, password=MACPRO_PASS, timeout=5)

        # 🔥 HOT-ROD Development Environment Commands
        cmds = {
            # Core System Performance
            "cpu_usage": "top -l 1 | grep 'CPU usage' | awk '{print $3}' | sed 's/%//'",
            "cpu_cores": "sysctl -n hw.ncpu",
            "cpu_freq": "sysctl -n hw.cpufrequency_max 2>/dev/null || echo 0",
            "memory_pressure": "vm_stat | head -2 | tail -1 | awk '{print $2}' | sed 's/\\.//'",
            "memory_total": "sysctl -n hw.memsize | awk '{print $1/1024/1024/1024}'",
            "swap_usage": "sysctl vm.swapusage | grep 'used =' | awk '{print $7}' | sed 's/M//'",
            # Development Environment Detection
            "xcode_running": "ps aux | grep -i 'xcode\\|simulator' | grep -v grep | wc -l",
            "xcode_version": "xcodebuild -version 2>/dev/null | head -1 | awk '{print $2}' || echo 'Not Installed'",
            "xcode_simulators": "xcrun simctl list devices | grep 'Booted' | wc -l",
            "xcode_projects": "find ~ -name '*.xcodeproj' -o -name '*.xcworkspace' 2>/dev/null | wc -l",
            # Visual Studio & .NET Development
            "vscode_running": "ps aux | grep -i 'visual studio code\\|code' | grep -v grep | wc -l",
            "vs_extensions": "code --list-extensions 2>/dev/null | wc -l || echo 0",
            "dotnet_version": "dotnet --version 2>/dev/null || echo 'Not Installed'",
            "csharp_projects": "find ~ -name '*.csproj' -o -name '*.sln' 2>/dev/null | wc -l",
            # Development Tools & Frameworks
            "docker_containers": "docker ps -q 2>/dev/null | wc -l || echo 0",
            "docker_images": "docker images -q 2>/dev/null | wc -l || echo 0",
            "node_version": "node --version 2>/dev/null || echo 'Not Installed'",
            "npm_packages": "npm list -g --depth=0 2>/dev/null | wc -l || echo 0",
            "python_version": "python3 --version 2>/dev/null | awk '{print $2}' || echo 'Not Installed'",
            "pip_packages": "pip3 list 2>/dev/null | wc -l || echo 0",
            "ruby_version": "ruby --version 2>/dev/null | awk '{print $2}' || echo 'Not Installed'",
            "java_version": "java -version 2>&1 | head -1 | awk '{print $3}' | sed 's/\"//g' || echo 'Not Installed'",
            # Git & Repository Management
            "git_repos": "find ~ -name '.git' -type d 2>/dev/null | wc -l",
            "git_status": "cd ~ && find . -name '.git' -type d | head -5 | while read d; do cd \"$d/..\"; echo $(basename $(pwd)): $(git status --porcelain 2>/dev/null | wc -l) changes; cd ~; done",
            # Hot-Rod Hardware & Performance
            "thermal_state": "pmset -g thermlog 2>/dev/null | tail -1 | awk '{print $4}' || echo 'Normal'",
            "gpu_info": "system_profiler SPDisplaysDataType | grep -E 'Chipset Model|VRAM' | head -2",
            "thunderbolt_devices": "system_profiler SPThunderboltDataType | grep 'Device Name:' | wc -l",
            "usb_devices": "system_profiler SPUSBDataType | grep 'Product ID:' | wc -l",
            "planar_kvm": "system_profiler SPDisplaysDataType | grep -i 'planar\\|kvm' | head -1",
            # Network & Connectivity
            "network_interfaces": "ifconfig | grep 'inet ' | grep -v 127.0.0.1 | wc -l",
            "vpn_connections": "scutil --nc list | grep Connected | wc -l",
            "ssh_sessions": "who | grep pts | wc -l",
            # Performance Optimization
            "brew_services": "brew services list 2>/dev/null | grep started | wc -l || echo 0",
            "launch_agents": "launchctl list | wc -l",
            "cpu_temperature": "sudo powermetrics --samplers smc -n 1 2>/dev/null | grep 'CPU die temperature' | awk '{print $4}' | sed 's/C//' || echo 0",
            # Development Server Status
            "local_servers": "lsof -i :3000 -i :8000 -i :8080 -i :4200 -i :5000 2>/dev/null | grep LISTEN | wc -l",
            "database_processes": "ps aux | grep -E '(mysql|postgres|mongodb|redis)' | grep -v grep | wc -l",
        }

        result = {
            "system": "MacPro Hot-Rod",
            "specs": "Development Workstation",
            "kvm_active": True,  # Assume active for hot-rod mode
            "performance_mode": "🔥 HOT-ROD",
            "planar_input": "DisplayPort 2",
            "dev_environment": "🚀 XCode + VS22 Ready",
            "hotrod_status": "ACTIVE",
        }

        for k, c in cmds.items():
            try:
                _, stdout, _ = ssh.exec_command(c)
                out = stdout.read().decode().strip()

                # Core System Metrics
                if k == "cpu_usage":
                    result["cpu_percent"] = float(out) if out else 0
                elif k == "cpu_cores":
                    result["cpu_cores"] = int(out) if out.isdigit() else 0
                elif k == "cpu_freq":
                    result["cpu_freq_ghz"] = (
                        round(int(out) / 1000000000, 2) if out.isdigit() else 0
                    )
                elif k == "memory_pressure":
                    result["memory_free_pages"] = int(out) if out.isdigit() else 0
                elif k == "memory_total":
                    result["memory_total_gb"] = round(float(out), 1) if out else 0
                elif k == "swap_usage":
                    result["swap_used_mb"] = (
                        float(out.replace("M", "")) if "M" in out else 0
                    )

                # XCode Development Environment
                elif k == "xcode_running":
                    result["xcode_processes"] = int(out) if out.isdigit() else 0
                    result["xcode_active"] = int(out) > 0
                elif k == "xcode_version":
                    result["xcode_version"] = (
                        out if out != "Not Installed" else "❌ Not Installed"
                    )
                elif k == "xcode_simulators":
                    result["ios_simulators_running"] = int(out) if out.isdigit() else 0
                elif k == "xcode_projects":
                    result["xcode_projects_count"] = int(out) if out.isdigit() else 0

                # Visual Studio & .NET Development
                elif k == "vscode_running":
                    result["vscode_processes"] = int(out) if out.isdigit() else 0
                    result["vscode_active"] = int(out) > 0
                elif k == "vs_extensions":
                    result["vscode_extensions"] = int(out) if out.isdigit() else 0
                elif k == "dotnet_version":
                    result["dotnet_version"] = (
                        out if out != "Not Installed" else "❌ Not Installed"
                    )
                elif k == "csharp_projects":
                    result["csharp_projects_count"] = int(out) if out.isdigit() else 0

                # Development Tools
                elif k == "docker_containers":
                    result["docker_containers"] = int(out) if out.isdigit() else 0
                elif k == "docker_images":
                    result["docker_images"] = int(out) if out.isdigit() else 0
                elif k == "node_version":
                    result["node_version"] = (
                        out if out != "Not Installed" else "❌ Not Installed"
                    )
                elif k == "python_version":
                    result["python_version"] = (
                        out if out != "Not Installed" else "❌ Not Installed"
                    )
                elif k == "java_version":
                    result["java_version"] = (
                        out if out != "Not Installed" else "❌ Not Installed"
                    )

                # Git & Repository Management
                elif k == "git_repos":
                    result["git_repositories"] = int(out) if out.isdigit() else 0

                # Hot-Rod Hardware
                elif k == "thermal_state":
                    result["thermal_state"] = out if out else "Normal"
                elif k == "cpu_temperature":
                    result["cpu_temp_c"] = float(out) if out and out != "0" else 0
                elif k == "thunderbolt_devices":
                    result["thunderbolt_devices"] = int(out) if out.isdigit() else 0
                elif k == "usb_devices":
                    result["usb_devices"] = int(out) if out.isdigit() else 0

                # Development Servers
                elif k == "local_servers":
                    result["dev_servers_running"] = int(out) if out.isdigit() else 0
                elif k == "database_processes":
                    result["database_processes"] = int(out) if out.isdigit() else 0
                elif k == "memory_pressure":
                    result["memory_free_percent"] = float(out) if out else 0
                elif k == "memory_total":
                    result["memory_total_gb"] = round(float(out), 1) if out else 0
                elif k == "swap_usage":
                    result["swap_used_mb"] = (
                        float(out.replace("M", "")) if "M" in out else 0
                    )
                elif k == "disk_root":
                    result["disk_percent"] = float(out) if out else 0
                elif k == "disk_io":
                    if out:
                        parts = out.split()
                        result["disk_read_kb_s"] = (
                            float(parts[0]) if len(parts) > 0 else 0
                        )
                        result["disk_write_kb_s"] = (
                            float(parts[1]) if len(parts) > 1 else 0
                        )
                elif k == "thermal_state":
                    result["thermal_state"] = out if out else "Unknown"
                elif k == "gpu_processes":
                    result["gpu_count"] = int(out) if out.isdigit() else 0
                elif k == "network_throughput":
                    if out:
                        parts = out.split()
                        result["network_in_bytes"] = (
                            int(parts[0]) if len(parts) > 0 else 0
                        )
                        result["network_out_bytes"] = (
                            int(parts[1]) if len(parts) > 1 else 0
                        )
                elif k == "active_connections":
                    result["network_connections"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "xcode_running":
                    result["xcode_processes"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "docker_containers":
                    result["docker_containers"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "node_processes":
                    result["node_processes"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "python_processes":
                    result["python_processes"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "java_processes":
                    result["java_processes"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "git_repos":
                    result["git_repos_count"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "brew_outdated":
                    result["brew_outdated_count"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "thunderbolt_devices":
                    result["thunderbolt_devices"] = (
                        int(out.strip()) if out.strip().isdigit() else 0
                    )
                elif k == "planar_connection":
                    result["planar_detected"] = "Planar" in out

            except Exception as e:
                result[f"{k}_error"] = str(e)

        # Development environment assessment
        total_dev_processes = (
            result.get("xcode_processes", 0)
            + result.get("node_processes", 0)
            + result.get("python_processes", 0)
            + result.get("java_processes", 0)
        )

        result["development_workload"] = total_dev_processes
        result["development_ready"] = (
            result.get("cpu_percent", 100) < 70
            and result.get("memory_free_percent", 0) > 20
            and result.get("thermal_state", "") in ["Normal", "Fair"]
            and result.get("swap_used_mb", 1000) < 500  # Low swap usage
        )

        # Hot-rod development optimization status
        result["hotrod_optimized"] = (
            result.get("cpu_cores", 0) >= 8  # Multi-core power
            and result.get("memory_total_gb", 0) >= 32  # Plenty of RAM
            and result.get("thunderbolt_devices", 0) > 0  # Thunderbolt connectivity
            and result["development_ready"]
        )

        # Professional development tools status
        result["pro_tools_active"] = {
            "xcode": result.get("xcode_processes", 0) > 0,
            "docker": result.get("docker_containers", 0) > 0,
            "node_dev": result.get("node_processes", 0) > 0,
            "python_dev": result.get("python_processes", 0) > 0,
            "git_projects": result.get("git_repos_count", 0) > 0,
        }

        ssh.close()
        return result

    except Exception as e:
        return {
            "error": str(e),
            "system": MACPRO_MODEL,
            "kvm_active": False,
            "status": "offline",
        }


# ---------- DGS METRICS ----------
def get_dgs_ports():
    try:
        ports = []
        for errorIndication, errorStatus, errorIndex, varBinds in nextCmd(
            SnmpEngine(),
            CommunityData(SNMP_COMM),
            UdpTransportTarget((DGS_IP, 161)),
            ContextData(),
            ObjectType(ObjectIdentity("1.3.6.1.2.1.2.2.1.8")),  # ifOperStatus
            lexicographicMode=False,
        ):
            if errorIndication or errorStatus:
                break
            for oid, val in varBinds:
                ports.append(str(val))
        up = ports.count("1")
        return {"ports_up": up, "total_ports": len(ports)}
    except Exception as e:
        return {"error": str(e)}


# ---------- NETWORK DEVICE DISCOVERY ----------


def discover_network_devices():
    """Discover all devices connected to the network"""
    devices = {}

    try:
        # Get the network range (assuming 192.168.0.x)
        network_base = DGS_IP.rsplit(".", 1)[0]  # Get 192.168.0

        # Ping sweep to find active devices
        active_ips = []

        # Quick ping sweep (first 50 IPs for speed)
        for i in range(1, 51):
            ip = f"{network_base}.{i}"
            try:
                # Quick ping with 1 second timeout
                result = subprocess.run(
                    ["ping", "-c", "1", "-W", "1000", ip],
                    capture_output=True,
                    timeout=2,
                )
                if result.returncode == 0:
                    active_ips.append(ip)
            except:
                continue

        # Get device info for each active IP
        for ip in active_ips:
            device_info = get_device_info(ip)
            if device_info:
                devices[ip] = device_info

    except Exception as e:
        devices["discovery_error"] = str(e)

    return devices


def get_device_info(ip):
    """Get detailed information about a network device"""
    info = {
        "ip": ip,
        "hostname": "Unknown",
        "mac": "Unknown",
        "vendor": "Unknown",
        "type": "Unknown",
        "status": "online",
    }

    try:
        # Try to get hostname
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            info["hostname"] = hostname
        except:
            pass

        # Try to identify device type based on IP or hostname
        if ip.endswith(".1"):
            info["type"] = "Router/Switch"
        elif "mac" in info["hostname"].lower():
            info["type"] = "Mac Computer"
        elif "win" in info["hostname"].lower() or "pc" in info["hostname"].lower():
            info["type"] = "Windows PC"
        elif "dell" in info["hostname"].lower():
            info["type"] = "Dell Computer"
        elif "hp" in info["hostname"].lower():
            info["type"] = "HP Computer"

        # Try to get MAC address from ARP table
        try:
            arp_result = subprocess.run(
                ["arp", "-n", ip], capture_output=True, text=True
            )
            if arp_result.returncode == 0:
                arp_lines = arp_result.stdout.strip().split("\n")
                for line in arp_lines:
                    if ip in line:
                        parts = line.split()
                        if len(parts) >= 3:
                            info["mac"] = parts[2]
                            break
        except:
            pass

    except Exception as e:
        info["error"] = str(e)

    return info


def get_switch_port_mapping():
    """Get which devices are connected to which switch ports via SNMP"""
    port_mapping = {}

    try:
        # Get MAC address table from switch (if supported)
        for errorIndication, errorStatus, errorIndex, varBinds in nextCmd(
            SnmpEngine(),
            CommunityData(SNMP_COMM),
            UdpTransportTarget((DGS_IP, 161)),
            ContextData(),
            ObjectType(ObjectIdentity("1.3.6.1.2.1.17.4.3.1.2")),  # dot1dTpFdbPort
            lexicographicMode=False,
        ):
            if errorIndication or errorStatus:
                break
            for oid, val in varBinds:
                # Extract MAC and port info
                mac_oid = str(oid).split(".")[-6:]
                if len(mac_oid) == 6:
                    mac = ":".join([f"{int(x):02x}" for x in mac_oid])
                    port = int(val)
                    port_mapping[mac] = port

    except Exception as e:
        port_mapping["error"] = str(e)

    return port_mapping


# ---------- BACKGROUND REFRESH ----------
def refresh():
    while True:
        data["mac"] = get_mac_metrics()
        data["omen"] = get_omen_metrics()
        data["dell"] = get_dell_metrics()
        data["macpro"] = get_macpro_metrics()
        data["dgs"] = get_dgs_ports()

        # Network discovery (run less frequently)
        if int(time.time()) % (REFRESH_SECS * 3) == 0:  # Every 30 seconds
            data["network_devices"] = discover_network_devices()

        time.sleep(REFRESH_SECS)


threading.Thread(target=refresh, daemon=True).start()

# ---------- HTML TEMPLATE ----------
HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>NoizyLab Mission Control</title>
<style>
body {font-family: 'Segoe UI', sans-serif; background:#0a0a0a; color:#e8e8e8; margin:0; padding:0 20px;}
h1 {background:#d4af37; color:#000; padding:15px 20px; margin:0 0 20px 0; border-radius:10px;}
.section {display:flex; flex-direction:column; gap:15px; max-width:1200px; margin:0 auto;}
.card {background:#111; border-radius:15px; box-shadow:0 0 15px #222; padding:20px; width:100%; box-sizing:border-box; min-height:120px;}
.card h2 {color:#d4af37; margin:0 0 15px 0; font-size:1.3em;}
.value {font-size:1.8em; font-weight:bold;}
.error {color:#f44;}
.card-content {display:flex; flex-wrap:wrap; gap:20px; align-items:center;}
.metric-group {display:flex; flex-direction:column; gap:8px; flex:1; min-width:150px;}
.metric-item {display:flex; justify-content:space-between; align-items:center; padding:5px 0;}
.network-grid {display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:15px; margin:20px 0;}
.device-card {background:#1a1a1a; border:1px solid #333; border-radius:8px; padding:15px;}
.device-ip {color:#d4af37; font-weight:bold;}
.device-type {color:#0af; font-size:0.9em;}
.device-hostname {color:#ccc; font-size:0.8em;}
.online {border-left:4px solid #0f0;}
.offline {border-left:4px solid #f44;}
.good {color:#0f0;}
.warning {color:#fa0;}
.critical {color:#f44;}
.inactive {color:#666;}
.standby {color:#888;}
</style>
<meta http-equiv="refresh" content="10">
</head>
<body>
<h1>NOIZYLAB | Mission Control Dashboard - 5 Systems</h1>
<div class="section">
  <div class="card">
    <h2>🖥️ MacStudio (Local Host System)</h2>
    {% if mac %}
      <div class="card-content">
        <div class="metric-group">
          <div class="metric-item">
            <span>CPU Usage:</span>
            <span class="value {{ 'good' if mac.cpu < 70 else 'warning' if mac.cpu < 85 else 'critical' }}">{{mac.cpu}}%</span>
          </div>
          <div class="metric-item">
            <span>Memory Usage:</span>
            <span class="value {{ 'good' if mac.ram < 80 else 'warning' if mac.ram < 90 else 'critical' }}">{{mac.ram}}%</span>
          </div>
          <div class="metric-item">
            <span>Disk Usage:</span>
            <span class="value {{ 'good' if mac.disk < 80 else 'warning' if mac.disk < 90 else 'critical' }}">{{mac.disk}}%</span>
          </div>
        </div>
        <div class="metric-group">
          <div style="padding: 10px; background: rgba(0,200,0,0.15); border-radius: 8px; border-left: 4px solid #00cc00;">
            <strong>🏠 Local System Status</strong><br>
            <span style="font-size: 0.9em;">Dashboard Host • Mission Control Active</span>
          </div>
        </div>
      </div>
    {% endif %}
  </div>
    <div class="card hotrod-control">
    <h2>🎮 OMEN Control Hub 🔥</h2>
    <div style="font-size: 0.8em; color: #888;">HP OMEN Desktop - Planar2495 KVM Control</div>
    {% if omen.error %}
      <div class="error">❌ {{omen.error}}</div>
    {% else %}
      <div>Primary System <span class="value good">{{omen.cpu}}%</span></div>
      <div>Control RAM <span class="value {{ 'good' if omen.ram < 80 else 'warning' }}">{{omen.ram}}%</span></div>
      <div>Storage <span class="value {{ 'good' if omen.disk < 85 else 'warning' }}">{{omen.disk}}%</span></div>
      {% if omen.temp %}<div>Operating Temp <span class="value {{ 'good' if omen.temp < 70 else 'warning' }}">{{omen.temp}}°C</span></div>{% endif %}
      
      <div style="margin-top: 10px; padding: 8px; background: rgba(255,165,0,0.2); border-radius: 5px;">
        🎯 KVM Hub Status: <span class="value good">✅ ACTIVE</span><br>
        📺 Planar2495 Control: <span class="value good">✅ MANAGING</span><br>
        🔥 Hot-Rod Coordinator: <span class="value good">✅ OPTIMIZED</span>
      </div>
      
      <div style="margin-top: 8px; font-size: 0.85em; text-align: center;">
        Dell Gaming ↔️ MacPro Dev ↔️ OMEN Control
      </div>
    {% endif %}
  </div>
  <div class="card {{ 'hotrod-active' if dell.kvm_active else 'hotrod-standby' }}">
    <h2>🎮 Dell Inspiron 17 7779 Gaming {{ '🔥 ACTIVE' if dell.kvm_active else '💤 STANDBY' }}</h2>
    <div style="font-size: 0.8em; color: #888;">{{ dell.specs.cpu if dell.specs else 'Intel i7-7700HQ Gaming Laptop' }}</div>
    {% if dell.error %}
      <div class="error">❌ {{dell.error}}</div>
    {% else %}
      <div>CPU <span class="value {{ 'good' if dell.cpu_percent < 70 else 'warning' if dell.cpu_percent < 85 else 'critical' }}">{{dell.cpu_percent|round(1)}}%</span></div>
      {% if dell.cpu_freq_mhz %}<div>CPU Freq <span class="value">{{dell.cpu_freq_mhz}} MHz</span></div>{% endif %}
      
      <div>GPU Usage <span class="value {{ 'good' if dell.gpu_percent < 80 else 'warning' }}">{{dell.gpu_percent}}%</span></div>
      <div>GPU Temp <span class="value {{ 'good' if dell.gpu_temp < 75 else 'warning' if dell.gpu_temp < 85 else 'critical' }}">{{dell.gpu_temp}}°C</span></div>
      {% if dell.gpu_power_watts %}<div>GPU Power <span class="value">{{dell.gpu_power_watts}}W</span></div>{% endif %}
      
      <div>RAM <span class="value {{ 'good' if dell.ram_percent < 70 else 'warning' if dell.ram_percent < 85 else 'critical' }}">{{dell.ram_percent|round(1)}}% ({{dell.ram_used_gb|round(1)}}GB/{{dell.ram_total_gb|round(1)}}GB)</span></div>
      <div>Disk C: <span class="value {{ 'good' if dell.disk_c_percent < 80 else 'warning' }}">{{dell.disk_c_percent|round(1)}}%</span></div>
      {% if dell.cpu_temp %}<div>CPU Temp <span class="value {{ 'good' if dell.cpu_temp < 70 else 'warning' if dell.cpu_temp < 85 else 'critical' }}">{{dell.cpu_temp}}°C</span></div>{% endif %}
      
      <div>Power Plan <span class="value {{ 'good' if dell.power_plan == 'High Performance' else 'warning' }}">{{dell.power_plan}}</span></div>
      <div>Planar Input <span class="value {{ 'good' if dell.kvm_active else 'standby' }}">{{dell.planar_input}}</span></div>
      
      <div style="margin-top: 10px; padding: 8px; background: rgba(0,0,0,0.3); border-radius: 5px;">
        🎮 Gaming Ready: <span class="{{ 'good' if dell.gaming_ready else 'warning' }}">{{ '✅ YES' if dell.gaming_ready else '⚠️ CHECK SETTINGS' }}</span><br>
        🔥 Hot-Rod Mode: <span class="{{ 'good' if dell.hotrod_optimized else 'warning' }}">{{ '✅ OPTIMIZED' if dell.hotrod_optimized else '❌ NOT OPTIMIZED' }}</span>
      </div>
    {% endif %}
  </div>
  <div class="card {{ 'hotrod-active' if macpro.kvm_active else 'hotrod-standby' }}">
    <h2>🚀 Mac Pro Hot-Rod Development {{ '🔥 ACTIVE' if macpro.kvm_active else '💤 STANDBY' }}</h2>
    <div style="font-size: 0.8em; color: #888;">{{ macpro.specs.cpu if macpro.specs else 'Intel Xeon W Workstation' }}</div>
    {% if macpro.error %}
      <div class="error">❌ {{macpro.error}}</div>
    {% else %}
      <!-- Core Performance Metrics -->
      <div>CPU <span class="value {{ 'good' if macpro.cpu_percent < 60 else 'warning' if macpro.cpu_percent < 80 else 'critical' }}">{{macpro.cpu_percent|round(1)}}%</span> ({{macpro.cpu_cores}} cores @ {{macpro.cpu_freq_ghz}}GHz)</div>
      
      <div>Memory Free <span class="value {{ 'good' if macpro.memory_free_percent > 30 else 'warning' if macpro.memory_free_percent > 15 else 'critical' }}">{{macpro.memory_free_percent|round(1)}}%</span> ({{macpro.memory_total_gb}}GB total)</div>
      {% if macpro.swap_used_mb %}<div>Swap Used <span class="value {{ 'good' if macpro.swap_used_mb < 100 else 'warning' }}">{{macpro.swap_used_mb|round(1)}}MB</span></div>{% endif %}
      
      <div>Disk Root <span class="value {{ 'good' if macpro.disk_percent < 80 else 'warning' }}">{{macpro.disk_percent|round(1)}}%</span></div>
      <div>Thermal {% if macpro.cpu_temp_c > 0 %}<span class="value {{ 'good' if macpro.cpu_temp_c < 70 else 'warning' if macpro.cpu_temp_c < 85 else 'critical' }}">{{macpro.cpu_temp_c}}°C</span>{% else %}<span class="value {{ 'good' if macpro.thermal_state == 'Normal' else 'warning' }}">{{macpro.thermal_state}}</span>{% endif %}</div>
      
      
      <!-- XCode Development Environment -->
      <div style="margin-top: 12px; padding: 8px; background: rgba(0,100,200,0.2); border-radius: 5px; border-left: 3px solid #0066cc;">
        <strong>📱 XCode Environment</strong><br>
        <div style="font-size: 0.85em; margin-top: 4px;">
          Version: <span class="value">{{macpro.xcode_version}}</span><br>
          {% if macpro.xcode_active %}Active: <span class="good">✅ {{macpro.xcode_processes}} processes</span>{% else %}Active: <span class="inactive">❌ Not Running</span>{% endif %}<br>
          iOS Simulators: <span class="value {{ 'good' if macpro.ios_simulators_running > 0 else 'inactive' }}">{{macpro.ios_simulators_running}} running</span><br>
          Projects: <span class="value">{{macpro.xcode_projects_count}} found</span>
        </div>
      </div>
      
      <!-- Visual Studio & .NET Development -->
      <div style="margin-top: 8px; padding: 8px; background: rgba(100,0,200,0.2); border-radius: 5px; border-left: 3px solid #6600cc;">
        <strong>💻 VS Code & .NET</strong><br>
        <div style="font-size: 0.85em; margin-top: 4px;">
          {% if macpro.vscode_active %}VS Code: <span class="good">✅ {{macpro.vscode_processes}} processes</span>{% else %}VS Code: <span class="inactive">❌ Not Running</span>{% endif %}<br>
          Extensions: <span class="value">{{macpro.vscode_extensions}} installed</span><br>
          .NET Version: <span class="value">{{macpro.dotnet_version}}</span><br>
          C# Projects: <span class="value">{{macpro.csharp_projects_count}} found</span>
        </div>
      </div>
      
      <!-- Development Tools & Runtime -->
      <div style="margin-top: 8px; padding: 8px; background: rgba(200,100,0,0.2); border-radius: 5px; border-left: 3px solid #cc6600;">
        <strong>🛠️ Development Runtime</strong><br>
        <div style="font-size: 0.85em; margin-top: 4px;">
          Docker: <span class="value {{ 'good' if macpro.docker_containers > 0 else 'inactive' }}">{{macpro.docker_containers}} containers / {{macpro.docker_images}} images</span><br>
          Node.js: <span class="value">{{macpro.node_version}}</span><br>
          Python: <span class="value">{{macpro.python_version}}</span><br>
          Java: <span class="value">{{macpro.java_version}}</span><br>
          Git Repos: <span class="value {{ 'good' if macpro.git_repositories > 0 else 'inactive' }}">{{macpro.git_repositories}} found</span>
        </div>
      </div>
      
      <!-- Hot-Rod Hardware & Connectivity -->
      <div style="margin-top: 8px; padding: 8px; background: rgba(200,0,0,0.2); border-radius: 5px; border-left: 3px solid #cc0000;">
        <strong>🔥 Hot-Rod Hardware</strong><br>
        <div style="font-size: 0.85em; margin-top: 4px;">
          Thunderbolt: <span class="value {{ 'good' if macpro.thunderbolt_devices > 0 else 'inactive' }}">{{macpro.thunderbolt_devices}} devices</span><br>
          USB Devices: <span class="value">{{macpro.usb_devices}} connected</span><br>
          Dev Servers: <span class="value {{ 'good' if macpro.dev_servers_running > 0 else 'inactive' }}">{{macpro.dev_servers_running}} running</span><br>
          Databases: <span class="value {{ 'good' if macpro.database_processes > 0 else 'inactive' }}">{{macpro.database_processes}} processes</span><br>
          Planar KVM: <span class="value {{ 'good' if macpro.kvm_active else 'standby' }}">{{macpro.planar_input}}</span>
        </div>
      </div>

      
      
      <!-- Development Status Summary -->
      <div style="margin-top: 10px; padding: 8px; background: rgba(0,0,0,0.3); border-radius: 5px;">
        💻 Dev Ready: <span class="{{ 'good' if macpro.development_ready else 'warning' }}">{{ '✅ YES' if macpro.development_ready else '⚠️ CHECK RESOURCES' }}</span><br>
        🔥 Hot-Rod Mode: <span class="{{ 'good' if macpro.hotrod_optimized else 'warning' }}">{{ '✅ OPTIMIZED' if macpro.hotrod_optimized else '❌ NOT OPTIMIZED' }}</span><br>
        🚀 Dev Workload: <span class="value">{{macpro.development_workload}} active processes</span>
      </div>
    {% endif %}
  </div>
  <div class="card">
    <h2>🌐 D-LINK Switch</h2>
    {% if dgs.error %}
      <div class="error">{{dgs.error}}</div>
    {% else %}
      <div>Ports Up / Total</div>
      <div class="value">{{dgs.ports_up}} / {{dgs.total_ports}}</div>
    {% endif %}
  </div>
</div>

<h1 style="background:#2a5a2a; margin-top:40px;">🌐 ALL NETWORK DEVICES</h1>
<div class="network-grid">
  {% for ip, device in network_devices.items() %}
    {% if ip != "discovery_error" %}
      <div class="device-card online">
        <div class="device-ip">📱 {{ip}}</div>
        <div class="device-hostname">{{device.hostname}}</div>
        <div class="device-type">{{device.type}}</div>
        {% if device.mac != "Unknown" %}
          <div style="font-size:0.7em; color:#888;">MAC: {{device.mac}}</div>
        {% endif %}
      </div>
    {% endif %}
  {% endfor %}
  
  {% if network_devices.discovery_error %}
    <div class="device-card offline">
      <div class="error">Discovery Error: {{network_devices.discovery_error}}</div>
    </div>
  {% endif %}
</div>

</body>
</html>
"""


# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template_string(
        HTML,
        mac=data["mac"],
        omen=data["omen"],
        dell=data["dell"],
        macpro=data["macpro"],
        dgs=data["dgs"],
        network_devices=data["network_devices"],
    )


# ---------- START ----------
if __name__ == "__main__":
    print("Starting NOIZYLAB Mission Control Dashboard at http://localhost:8500")
    app.run(host="0.0.0.0", port=8500, debug=False)
