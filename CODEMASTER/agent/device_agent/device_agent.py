#!/usr/bin/env python3
"""
🤖 CODEMASTER DEVICE AGENT 🤖
==============================
Outbound agent for endpoint devices.

Features:
- Auto-registration with Fleet service
- Heartbeat (system metrics)
- Command execution (remote jobs)
- Screenshot capture (remote view)
- File transfer (push/pull)
- Session management

Every action creates Evidence!
"""

import os
import sys
import json
import uuid
import socket
import platform
import asyncio
import subprocess
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
from dataclasses import dataclass, asdict

import httpx
import psutil

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

AGENT_ROOT = Path(__file__).parent
CONFIG_FILE = AGENT_ROOT / "agent_config.json"
EVIDENCE_DIR = AGENT_ROOT / "evidence"
SCREENSHOTS_DIR = AGENT_ROOT / "screenshots"

# Default settings
DEFAULT_CONFIG = {
    "fleet_url": os.environ.get("FLEET_URL", "http://localhost:8200"),
    "device_name": socket.gethostname(),
    "device_id": None,  # Set on first registration
    "heartbeat_interval": 30,  # seconds
    "enrollment_key": os.environ.get("ENROLLMENT_KEY", ""),
    "tags": [],
    "labels": {},
}


@dataclass
class AgentConfig:
    """Agent configuration"""
    fleet_url: str
    device_name: str
    device_id: Optional[str]
    heartbeat_interval: int
    enrollment_key: str
    tags: List[str]
    labels: Dict[str, str]
    
    @classmethod
    def load(cls) -> 'AgentConfig':
        """Load config from file or create default"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE) as f:
                data = json.load(f)
                return cls(**{**DEFAULT_CONFIG, **data})
        return cls(**DEFAULT_CONFIG)
    
    def save(self):
        """Save config to file"""
        with open(CONFIG_FILE, 'w') as f:
            json.dump(asdict(self), f, indent=2)


# ═══════════════════════════════════════════════════════════════
# 📊 SYSTEM METRICS
# ═══════════════════════════════════════════════════════════════

def collect_system_info() -> Dict[str, Any]:
    """Collect comprehensive system information"""
    uname = platform.uname()
    
    # CPU info
    cpu_freq = psutil.cpu_freq()
    
    # Memory info
    memory = psutil.virtual_memory()
    
    # Disk info
    disk_usage = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_usage.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype,
                "total_gb": round(usage.total / (1024**3), 2),
                "used_gb": round(usage.used / (1024**3), 2),
                "free_gb": round(usage.free / (1024**3), 2),
                "percent": usage.percent,
            })
        except:
            pass
    
    # Network interfaces
    network_interfaces = []
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                network_interfaces.append({
                    "interface": iface,
                    "ip": addr.address,
                    "netmask": addr.netmask,
                })
    
    return {
        "hostname": socket.gethostname(),
        "platform": {
            "system": uname.system,
            "release": uname.release,
            "version": uname.version,
            "machine": uname.machine,
            "processor": uname.processor,
        },
        "cpu": {
            "count": psutil.cpu_count(logical=False),
            "count_logical": psutil.cpu_count(logical=True),
            "freq_current": cpu_freq.current if cpu_freq else None,
            "freq_max": cpu_freq.max if cpu_freq else None,
            "percent": psutil.cpu_percent(interval=1),
        },
        "memory": {
            "total_gb": round(memory.total / (1024**3), 2),
            "available_gb": round(memory.available / (1024**3), 2),
            "used_gb": round(memory.used / (1024**3), 2),
            "percent": memory.percent,
        },
        "disk": disk_usage,
        "network": network_interfaces,
        "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat(),
    }


def collect_runtime_metrics() -> Dict[str, Any]:
    """Collect current runtime metrics (for heartbeat)"""
    memory = psutil.virtual_memory()
    
    # Top processes by memory
    top_processes = []
    for proc in sorted(psutil.process_iter(['pid', 'name', 'memory_percent']), 
                       key=lambda p: p.info['memory_percent'] or 0, reverse=True)[:5]:
        try:
            top_processes.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "memory_percent": round(proc.info['memory_percent'] or 0, 2),
            })
        except:
            pass
    
    return {
        "timestamp": datetime.now().isoformat(),
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": memory.percent,
        "memory_available_gb": round(memory.available / (1024**3), 2),
        "disk_io": dict(psutil.disk_io_counters()._asdict()) if psutil.disk_io_counters() else {},
        "net_io": dict(psutil.net_io_counters()._asdict()) if psutil.net_io_counters() else {},
        "top_processes": top_processes,
        "uptime_seconds": int(datetime.now().timestamp() - psutil.boot_time()),
    }


# ═══════════════════════════════════════════════════════════════
# 📸 SCREENSHOT CAPTURE
# ═══════════════════════════════════════════════════════════════

def capture_screenshot() -> Optional[Path]:
    """Capture a screenshot of the display"""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = SCREENSHOTS_DIR / f"screen_{timestamp}.png"
    
    system = platform.system()
    
    try:
        if system == "Darwin":  # macOS
            subprocess.run([
                "screencapture", "-x", str(filename)
            ], check=True, capture_output=True)
        elif system == "Linux":
            # Try scrot first, then import from ImageMagick
            try:
                subprocess.run([
                    "scrot", str(filename)
                ], check=True, capture_output=True)
            except FileNotFoundError:
                subprocess.run([
                    "import", "-window", "root", str(filename)
                ], check=True, capture_output=True)
        elif system == "Windows":
            # PowerShell screenshot
            ps_script = f'''
Add-Type -AssemblyName System.Windows.Forms
$screen = [System.Windows.Forms.Screen]::PrimaryScreen
$bitmap = New-Object System.Drawing.Bitmap($screen.Bounds.Width, $screen.Bounds.Height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($screen.Bounds.Location, [System.Drawing.Point]::Empty, $screen.Bounds.Size)
$bitmap.Save("{filename}")
'''
            subprocess.run(["powershell", "-Command", ps_script], 
                         check=True, capture_output=True)
        else:
            print(f"⚠️ Screenshot not supported on {system}")
            return None
        
        if filename.exists():
            print(f"📸 Screenshot saved: {filename}")
            return filename
        return None
        
    except Exception as e:
        print(f"❌ Screenshot failed: {e}")
        return None


# ═══════════════════════════════════════════════════════════════
# 🖥️ COMMAND EXECUTION
# ═══════════════════════════════════════════════════════════════

async def execute_command(command: str, timeout: int = 60, 
                         capture_output: bool = True) -> Dict[str, Any]:
    """Execute a command and return results"""
    start_time = datetime.now()
    evidence_id = str(uuid.uuid4())[:8]
    
    # Create evidence record
    evidence = {
        "id": evidence_id,
        "type": "command_execution",
        "command": command,
        "started_at": start_time.isoformat(),
        "timeout": timeout,
    }
    
    try:
        # Run command
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE if capture_output else None,
            stderr=asyncio.subprocess.PIPE if capture_output else None,
        )
        
        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )
            
            evidence.update({
                "exit_code": process.returncode,
                "stdout": stdout.decode('utf-8', errors='replace') if stdout else "",
                "stderr": stderr.decode('utf-8', errors='replace') if stderr else "",
                "completed_at": datetime.now().isoformat(),
                "duration_seconds": (datetime.now() - start_time).total_seconds(),
                "success": process.returncode == 0,
            })
            
        except asyncio.TimeoutError:
            process.kill()
            evidence.update({
                "error": "Command timed out",
                "exit_code": -1,
                "completed_at": datetime.now().isoformat(),
                "duration_seconds": timeout,
                "success": False,
            })
    
    except Exception as e:
        evidence.update({
            "error": str(e),
            "exit_code": -1,
            "completed_at": datetime.now().isoformat(),
            "duration_seconds": (datetime.now() - start_time).total_seconds(),
            "success": False,
        })
    
    # Save evidence locally
    save_evidence(evidence)
    
    return evidence


def save_evidence(evidence: Dict) -> Path:
    """Save evidence to local file"""
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    
    filename = EVIDENCE_DIR / f"{evidence['type']}_{evidence['id']}.json"
    with open(filename, 'w') as f:
        json.dump(evidence, f, indent=2)
    
    return filename


# ═══════════════════════════════════════════════════════════════
# 🌐 FLEET CLIENT
# ═══════════════════════════════════════════════════════════════

class FleetClient:
    """Client for communicating with Fleet service"""
    
    def __init__(self, config: AgentConfig):
        self.config = config
        self.client = httpx.AsyncClient(timeout=30.0)
        self.registered = False
        
    async def close(self):
        await self.client.aclose()
    
    async def register(self) -> bool:
        """Register this device with Fleet service"""
        system_info = collect_system_info()
        
        payload = {
            "name": self.config.device_name,
            "device_type": "endpoint",
            "enrollment_key": self.config.enrollment_key,
            "system_info": system_info,
            "capabilities": ["shell", "screenshot", "file_transfer", "metrics"],
            "agent_version": "1.0.0",
            "tags": self.config.tags,
            "labels": self.config.labels,
        }
        
        try:
            response = await self.client.post(
                f"{self.config.fleet_url}/devices/register",
                json=payload
            )
            
            if response.status_code == 200:
                data = response.json()
                self.config.device_id = data.get("device_id")
                self.config.save()
                self.registered = True
                print(f"✅ Registered with Fleet: {self.config.device_id}")
                return True
            else:
                print(f"❌ Registration failed: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Registration error: {e}")
            return False
    
    async def heartbeat(self) -> bool:
        """Send heartbeat with current metrics"""
        if not self.config.device_id:
            return False
        
        metrics = collect_runtime_metrics()
        
        try:
            response = await self.client.post(
                f"{self.config.fleet_url}/devices/{self.config.device_id}/heartbeat",
                json={"metrics": metrics}
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Process any pending commands
                commands = data.get("pending_commands", [])
                for cmd in commands:
                    await self.process_command(cmd)
                
                return True
            else:
                print(f"⚠️ Heartbeat failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"⚠️ Heartbeat error: {e}")
            return False
    
    async def process_command(self, command: Dict):
        """Process a command from Fleet"""
        cmd_type = command.get("type")
        cmd_id = command.get("id")
        
        print(f"📥 Processing command: {cmd_type} ({cmd_id})")
        
        result = None
        
        if cmd_type == "shell":
            # Execute shell command
            result = await execute_command(
                command.get("command", ""),
                timeout=command.get("timeout", 60)
            )
        
        elif cmd_type == "screenshot":
            # Capture screenshot
            path = capture_screenshot()
            result = {
                "success": path is not None,
                "path": str(path) if path else None,
            }
        
        elif cmd_type == "system_info":
            # Return system info
            result = {
                "success": True,
                "system_info": collect_system_info(),
            }
        
        elif cmd_type == "metrics":
            # Return current metrics
            result = {
                "success": True,
                "metrics": collect_runtime_metrics(),
            }
        
        else:
            result = {
                "success": False,
                "error": f"Unknown command type: {cmd_type}",
            }
        
        # Report result back to Fleet
        await self.report_command_result(cmd_id, result)
    
    async def report_command_result(self, command_id: str, result: Dict):
        """Report command result back to Fleet"""
        try:
            await self.client.post(
                f"{self.config.fleet_url}/commands/{command_id}/result",
                json=result
            )
        except Exception as e:
            print(f"⚠️ Failed to report command result: {e}")
    
    async def get_pending_commands(self) -> List[Dict]:
        """Get any pending commands for this device"""
        if not self.config.device_id:
            return []
        
        try:
            response = await self.client.get(
                f"{self.config.fleet_url}/devices/{self.config.device_id}/commands"
            )
            
            if response.status_code == 200:
                return response.json().get("commands", [])
            return []
            
        except:
            return []


# ═══════════════════════════════════════════════════════════════
# 🔄 AGENT MAIN LOOP
# ═══════════════════════════════════════════════════════════════

class DeviceAgent:
    """Main agent class"""
    
    def __init__(self, config: AgentConfig):
        self.config = config
        self.fleet = FleetClient(config)
        self.running = False
    
    async def start(self):
        """Start the agent"""
        print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  🤖 CODEMASTER DEVICE AGENT                                   ║
║                                                               ║
║  Device:  {self.config.device_name:<46} ║
║  Fleet:   {self.config.fleet_url:<46} ║
╚═══════════════════════════════════════════════════════════════╝
        """)
        
        # Register if needed
        if not self.config.device_id:
            print("📝 Registering with Fleet...")
            if not await self.fleet.register():
                print("❌ Failed to register - will retry")
        else:
            print(f"🔗 Device ID: {self.config.device_id}")
        
        # Start main loop
        self.running = True
        await self.main_loop()
    
    async def main_loop(self):
        """Main agent loop"""
        heartbeat_count = 0
        
        while self.running:
            try:
                # If not registered, try to register
                if not self.config.device_id:
                    await self.fleet.register()
                    await asyncio.sleep(10)
                    continue
                
                # Send heartbeat
                await self.fleet.heartbeat()
                heartbeat_count += 1
                
                if heartbeat_count % 10 == 0:
                    print(f"💓 Heartbeat #{heartbeat_count}")
                
                # Wait for next interval
                await asyncio.sleep(self.config.heartbeat_interval)
                
            except KeyboardInterrupt:
                print("\n⏹️ Shutting down...")
                self.running = False
            except Exception as e:
                print(f"❌ Error in main loop: {e}")
                await asyncio.sleep(10)
        
        await self.fleet.close()
    
    async def stop(self):
        """Stop the agent"""
        self.running = False


# ═══════════════════════════════════════════════════════════════
# 🎯 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='🤖 CODEMASTER Device Agent')
    parser.add_argument('command', nargs='?', default='run',
                       choices=['run', 'info', 'register', 'screenshot', 'exec'],
                       help='Command to execute')
    parser.add_argument('--fleet-url', help='Fleet service URL')
    parser.add_argument('--name', help='Device name')
    parser.add_argument('--enrollment-key', help='Enrollment key')
    parser.add_argument('--cmd', help='Command to execute (for exec)')
    
    args = parser.parse_args()
    
    # Load config
    config = AgentConfig.load()
    
    # Override from CLI
    if args.fleet_url:
        config.fleet_url = args.fleet_url
    if args.name:
        config.device_name = args.name
    if args.enrollment_key:
        config.enrollment_key = args.enrollment_key
    
    config.save()
    
    if args.command == 'info':
        # Show system info
        info = collect_system_info()
        print(json.dumps(info, indent=2))
    
    elif args.command == 'screenshot':
        # Capture screenshot
        path = capture_screenshot()
        if path:
            print(f"Screenshot saved: {path}")
    
    elif args.command == 'exec':
        # Execute command
        if args.cmd:
            result = asyncio.run(execute_command(args.cmd))
            print(json.dumps(result, indent=2))
        else:
            print("Error: --cmd required for exec")
    
    elif args.command == 'register':
        # Just register
        async def do_register():
            fleet = FleetClient(config)
            await fleet.register()
            await fleet.close()
        asyncio.run(do_register())
    
    else:  # run
        # Start agent
        agent = DeviceAgent(config)
        asyncio.run(agent.start())


if __name__ == "__main__":
    main()
