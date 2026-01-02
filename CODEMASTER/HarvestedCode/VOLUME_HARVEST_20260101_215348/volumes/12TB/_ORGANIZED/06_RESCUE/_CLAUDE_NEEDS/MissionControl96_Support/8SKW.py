#!/usr/bin/env python3
"""
Mission Control 96 - Auto Management System
Implements auto-save, auto-heal, and super agent management
"""

import json
import time
import threading
import subprocess
import logging
from pathlib import Path
from typing import Dict, Any, List
import psutil

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MissionControlManager:
    """Auto-management system for Mission Control 96"""
    
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self.load_config()
        self.running = False
        self.threads: Dict[str, threading.Thread] = {}
        
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Config file {self.config_path} not found, using defaults")
            return self.default_config()
            
    def default_config(self) -> Dict[str, Any]:
        """Default configuration"""
        return {
            "version": "1.0.0",
            "autoSave": True,
            "autoLaunch": True,
            "python_autosave": {"enabled": True, "interval": 60},
            "super_agents": {"enabled": True, "count": 96},
            "autoHeal": {"enabled": True, "check_interval": 30},
            "logging": {"file": "logs/mission_control_autosave.log"}
        }
        
    def setup_logging(self):
        """Setup file logging"""
        log_config = self.config.get("logging", {})
        log_file = log_config.get("file", "logs/mission_control_autosave.log")
        
        # Create logs directory
        Path(log_file).parent.mkdir(exist_ok=True)
        
        # Add file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    def start(self):
        """Start the management system"""
        logger.info("🚀 Starting Mission Control 96 Auto Management System")
        self.running = True
        
        # Setup logging
        self.setup_logging()
        
        # Start auto-save if enabled
        if self.config.get("python_autosave", {}).get("enabled", False):
            self.start_autosave()
            
        # Start auto-heal if enabled  
        if self.config.get("autoHeal", {}).get("enabled", False):
            self.start_autoheal()
            
        # Start super agents if enabled
        if self.config.get("super_agents", {}).get("enabled", False):
            self.start_super_agents()
            
        logger.info("✅ Auto Management System online")
        
    def stop(self):
        """Stop the management system"""
        logger.info("🛑 Stopping Auto Management System")
        self.running = False
        
        # Stop all threads
        for name, thread in self.threads.items():
            logger.info(f"Stopping {name}")
            
    def start_autosave(self):
        """Start auto-save functionality"""
        interval = self.config.get("python_autosave", {}).get("interval", 60)
        
        def autosave_worker():
            logger.info(f"Auto-save worker started (interval: {interval}s)")
            while self.running:
                try:
                    self.perform_autosave()
                    time.sleep(interval)
                except Exception as e:
                    logger.error(f"Auto-save error: {e}")
                    time.sleep(5)
                    
        thread = threading.Thread(target=autosave_worker, daemon=True)
        thread.start()
        self.threads["autosave"] = thread
        
    def perform_autosave(self):
        """Perform auto-save operations"""
        # Save current state
        state = {
            "timestamp": time.time(),
            "running_processes": self.get_running_processes(),
            "system_stats": self.get_system_stats()
        }
        
        # Write to state file
        state_file = Path("state/autosave_state.json")
        state_file.parent.mkdir(exist_ok=True)
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)
            
        logger.debug("Auto-save completed")
        
    def start_autoheal(self):
        """Start auto-heal functionality"""
        check_interval = self.config.get("autoHeal", {}).get("check_interval", 30)
        
        def autoheal_worker():
            logger.info(f"Auto-heal worker started (interval: {check_interval}s)")
            while self.running:
                try:
                    self.perform_autoheal()
                    time.sleep(check_interval)
                except Exception as e:
                    logger.error(f"Auto-heal error: {e}")
                    time.sleep(10)
                    
        thread = threading.Thread(target=autoheal_worker, daemon=True)
        thread.start()
        self.threads["autoheal"] = thread
        
    def perform_autoheal(self):
        """Perform auto-heal checks and repairs"""
        repair_scripts = self.config.get("autoHeal", {}).get("repair_scripts", [])
        
        for script in repair_scripts:
            if not self.is_process_running(script):
                logger.warning(f"Process {script} not running, attempting restart")
                self.restart_process(script)
                
    def start_super_agents(self):
        """Start super agent management"""
        count = self.config.get("super_agents", {}).get("count", 96)
        
        def super_agent_worker():
            logger.info(f"Super agent manager started (target: {count} agents)")
            while self.running:
                try:
                    self.manage_super_agents()
                    time.sleep(10)
                except Exception as e:
                    logger.error(f"Super agent error: {e}")
                    time.sleep(5)
                    
        thread = threading.Thread(target=super_agent_worker, daemon=True)
        thread.start()
        self.threads["super_agents"] = thread
        
    def manage_super_agents(self):
        """Manage super agent lifecycle"""
        # This would integrate with the Mission Control agent system
        # For now, just log status
        logger.debug("Super agents status check completed")
        
    def get_running_processes(self) -> List[Dict[str, Any]]:
        """Get list of running Mission Control processes"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = ' '.join(proc.info['cmdline'] or [])
                if any(script in cmdline for script in ['mission_control.py', 'mcp_server.py', 'rock_mode.py']):
                    processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'cmdline': cmdline
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return processes
        
    def get_system_stats(self) -> Dict[str, Any]:
        """Get system statistics"""
        return {
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'load_average': list(psutil.getloadavg()) if hasattr(psutil, 'getloadavg') else [0, 0, 0]
        }
        
    def is_process_running(self, script_name: str) -> bool:
        """Check if a specific script is running"""
        for proc in psutil.process_iter(['cmdline']):
            try:
                cmdline = ' '.join(proc.info['cmdline'] or [])
                if script_name in cmdline:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return False
        
    def restart_process(self, script_name: str):
        """Restart a process"""
        try:
            # Activate venv and run script
            cmd = f". ./.venv/bin/activate && python {script_name}"
            subprocess.Popen(cmd, shell=True, start_new_session=True)
            logger.info(f"Restarted {script_name}")
        except Exception as e:
            logger.error(f"Failed to restart {script_name}: {e}")
            
    def run_forever(self):
        """Run the manager forever"""
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Received shutdown signal")
            self.stop()

def main():
    """Main entry point"""
    manager = MissionControlManager()
    manager.start()
    
    try:
        manager.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        manager.stop()

if __name__ == "__main__":
    main()