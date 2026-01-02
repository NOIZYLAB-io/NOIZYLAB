#!/usr/bin/env python3
"""
macOS Client Agent for Mission Control 96
Client-side daemon for secure command execution and system management
"""

import subprocess
import json
import socket
import ssl
import time
import threading
import logging
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
import argparse

# Client configuration
CLIENT_CONFIG = {
    "server_host": "127.0.0.1",
    "server_port": 8766,  # Different port for agent communication
    "client_id": "mac_client_001",
    "api_key": "your_client_api_key_here",
    "log_file": "/tmp/mc96_client.log",
    "pid_file": "/tmp/mc96_client.pid",
    "check_interval": 30,  # seconds
    "max_retries": 5
}

class MacOSClientAgent:
    """macOS Client Agent for Mission Control 96"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.running = False
        self.logger = self._setup_logging()
        self.socket = None
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger('MC96Client')
        logger.setLevel(logging.INFO)
        
        # File handler
        handler = logging.FileHandler(self.config["log_file"])
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Console handler for debugging
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        return logger
    
    def _execute_applescript(self, script: str) -> Dict[str, Any]:
        """Execute AppleScript commands"""
        try:
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "error": result.stderr.strip(),
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "AppleScript execution timed out",
                "return_code": -1
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"AppleScript execution failed: {str(e)}",
                "return_code": -1
            }
    
    def _execute_shell_command(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """Execute shell commands safely"""
        try:
            # Security check - only allow specific commands
            allowed_commands = [
                "dscl", "scutil", "system_profiler", "sw_vers", "diskutil",
                "pmset", "networksetup", "security", "launchctl", "ps",
                "top", "vm_stat", "iotop", "netstat", "lsof", "df", "du"
            ]
            
            cmd_parts = command.split()
            if not cmd_parts or cmd_parts[0] not in allowed_commands:
                return {
                    "success": False,
                    "error": f"Command '{cmd_parts[0] if cmd_parts else 'empty'}' not allowed",
                    "return_code": -1
                }
            
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "error": result.stderr.strip(),
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": f"Command timed out after {timeout} seconds",
                "return_code": -1
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Command execution failed: {str(e)}",
                "return_code": -1
            }
    
    def _get_system_info(self) -> Dict[str, Any]:
        """Collect comprehensive system information"""
        info = {
            "timestamp": datetime.now().isoformat(),
            "client_id": self.config["client_id"],
            "hostname": socket.gethostname(),
            "system": {},
            "network": {},
            "security": {},
            "performance": {}
        }
        
        try:
            # System version
            sw_vers = self._execute_shell_command("sw_vers")
            if sw_vers["success"]:
                info["system"]["version"] = sw_vers["output"]
            
            # Hardware info
            hw_info = self._execute_shell_command("system_profiler SPHardwareDataType")
            if hw_info["success"]:
                info["system"]["hardware"] = hw_info["output"]
            
            # Disk usage
            disk_info = self._execute_shell_command("df -h")
            if disk_info["success"]:
                info["system"]["disk_usage"] = disk_info["output"]
            
            # Memory info
            vm_stat = self._execute_shell_command("vm_stat")
            if vm_stat["success"]:
                info["performance"]["memory"] = vm_stat["output"]
            
            # Network configuration
            net_config = self._execute_shell_command("scutil --nwi")
            if net_config["success"]:
                info["network"]["config"] = net_config["output"]
            
            # Security status
            sec_status = self._execute_shell_command("security authorizationdb read system.preferences")
            if sec_status["success"]:
                info["security"]["authorization"] = "configured"
            
        except Exception as e:
            self.logger.error(f"Error collecting system info: {e}")
            info["error"] = str(e)
        
        return info
    
    def _execute_ard_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        """Execute Apple Remote Desktop style commands"""
        cmd_type = command.get("type", "")
        
        if cmd_type == "get_info":
            return self._get_system_info()
        
        elif cmd_type == "applescript":
            script = command.get("script", "")
            return self._execute_applescript(script)
        
        elif cmd_type == "shell":
            shell_cmd = command.get("command", "")
            timeout = command.get("timeout", 30)
            return self._execute_shell_command(shell_cmd, timeout)
        
        elif cmd_type == "install_package":
            # Secure package installation
            package_path = command.get("package_path", "")
            return self._install_package(package_path)
        
        elif cmd_type == "restart":
            # Scheduled restart
            delay = command.get("delay", 60)
            return self._schedule_restart(delay)
        
        elif cmd_type == "maintenance":
            # Run maintenance scripts
            script_type = command.get("script_type", "")
            return self._run_maintenance(script_type)
        
        else:
            return {
                "success": False,
                "error": f"Unknown command type: {cmd_type}"
            }
    
    def _install_package(self, package_path: str) -> Dict[str, Any]:
        """Safely install packages"""
        try:
            # Verify package exists and is signed
            if not os.path.exists(package_path):
                return {
                    "success": False,
                    "error": "Package file does not exist"
                }
            
            # Check package signature
            verify_cmd = f"pkgutil --check-signature '{package_path}'"
            verify_result = self._execute_shell_command(verify_cmd)
            
            if not verify_result["success"]:
                return {
                    "success": False,
                    "error": "Package signature verification failed"
                }
            
            # Install package
            install_cmd = f"sudo installer -pkg '{package_path}' -target /"
            install_result = self._execute_shell_command(install_cmd, timeout=300)
            
            return install_result
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Package installation failed: {str(e)}"
            }
    
    def _schedule_restart(self, delay: int) -> Dict[str, Any]:
        """Schedule system restart"""
        try:
            restart_cmd = f"sudo shutdown -r +{delay//60}"
            result = self._execute_shell_command(restart_cmd)
            
            if result["success"]:
                self.logger.info(f"System restart scheduled in {delay} seconds")
            
            return result
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to schedule restart: {str(e)}"
            }
    
    def _run_maintenance(self, script_type: str) -> Dict[str, Any]:
        """Run system maintenance scripts"""
        maintenance_scripts = {
            "cleanup": [
                "sudo periodic daily",
                "sudo dscacheutil -flushcache",
                "sudo rm -rf /private/var/log/asl/*.asl"
            ],
            "permissions": [
                "sudo diskutil repairPermissions /",
                "sudo chmod -R 755 /Applications"
            ],
            "cache_clear": [
                "sudo dscacheutil -flushcache",
                "sudo killall -HUP mDNSResponder"
            ]
        }
        
        scripts = maintenance_scripts.get(script_type, [])
        if not scripts:
            return {
                "success": False,
                "error": f"Unknown maintenance script type: {script_type}"
            }
        
        results = []
        for script in scripts:
            result = self._execute_shell_command(script, timeout=120)
            results.append({
                "script": script,
                "result": result
            })
        
        success_count = sum(1 for r in results if r["result"]["success"])
        
        return {
            "success": success_count == len(results),
            "results": results,
            "success_count": success_count,
            "total_count": len(results)
        }
    
    def _send_heartbeat(self) -> bool:
        """Send heartbeat to Mission Control server"""
        try:
            heartbeat_data = {
                "type": "heartbeat",
                "client_id": self.config["client_id"],
                "timestamp": datetime.now().isoformat(),
                "status": "online",
                "system_info": self._get_system_info()
            }
            
            # In a real implementation, this would send to the server
            self.logger.info("Heartbeat sent successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to send heartbeat: {e}")
            return False
    
    def _check_for_commands(self) -> Optional[Dict[str, Any]]:
        """Check for pending commands from Mission Control"""
        try:
            # In a real implementation, this would check with the server
            # For now, return None (no commands)
            return None
            
        except Exception as e:
            self.logger.error(f"Failed to check for commands: {e}")
            return None
    
    def _process_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        """Process a command from Mission Control"""
        try:
            self.logger.info(f"Processing command: {command.get('type', 'unknown')}")
            
            # Execute the command
            result = self._execute_ard_command(command)
            
            # Log the result
            if result.get("success"):
                self.logger.info(f"Command executed successfully")
            else:
                self.logger.error(f"Command failed: {result.get('error', 'Unknown error')}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Command processing failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def start(self):
        """Start the client agent daemon"""
        try:
            self.running = True
            self.logger.info(f"Starting Mission Control Client Agent")
            self.logger.info(f"Client ID: {self.config['client_id']}")
            
            # Write PID file
            with open(self.config["pid_file"], "w") as f:
                f.write(str(os.getpid()))
            
            # Main loop
            while self.running:
                try:
                    # Send heartbeat
                    self._send_heartbeat()
                    
                    # Check for commands
                    command = self._check_for_commands()
                    if command:
                        result = self._process_command(command)
                        # In a real implementation, send result back to server
                    
                    # Wait for next check
                    time.sleep(self.config["check_interval"])
                    
                except KeyboardInterrupt:
                    self.logger.info("Received interrupt signal")
                    break
                except Exception as e:
                    self.logger.error(f"Error in main loop: {e}")
                    time.sleep(5)  # Brief pause before retry
            
        except Exception as e:
            self.logger.error(f"Failed to start agent: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the client agent daemon"""
        self.running = False
        self.logger.info("Mission Control Client Agent stopped")
        
        # Clean up PID file
        try:
            if os.path.exists(self.config["pid_file"]):
                os.remove(self.config["pid_file"])
        except Exception as e:
            self.logger.error(f"Failed to remove PID file: {e}")
    
    def status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            "running": self.running,
            "pid": os.getpid(),
            "config": self.config,
            "system_info": self._get_system_info()
        }

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Mission Control 96 macOS Client Agent")
    parser.add_argument("--start", action="store_true", help="Start the agent daemon")
    parser.add_argument("--stop", action="store_true", help="Stop the agent daemon")
    parser.add_argument("--status", action="store_true", help="Show agent status")
    parser.add_argument("--test", action="store_true", help="Test agent functionality")
    parser.add_argument("--config", type=str, help="Path to configuration file")
    
    args = parser.parse_args()
    
    # Load configuration
    config = CLIENT_CONFIG.copy()
    if args.config and os.path.exists(args.config):
        with open(args.config, 'r') as f:
            config.update(json.load(f))
    
    agent = MacOSClientAgent(config)
    
    if args.start:
        print("Starting Mission Control Client Agent...")
        agent.start()
    elif args.stop:
        print("Stopping Mission Control Client Agent...")
        agent.stop()
    elif args.status:
        status = agent.status()
        print(json.dumps(status, indent=2))
    elif args.test:
        print("Testing agent functionality...")
        # Test system info collection
        info = agent._get_system_info()
        print("System Info Test:")
        print(json.dumps(info, indent=2))
        
        # Test AppleScript
        script_result = agent._execute_applescript('tell application "System Events" to get name of processes')
        print("\nAppleScript Test:")
        print(json.dumps(script_result, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()