"""
Mac Task Management System for Mission Control 96
Proxy system for ARD commands, task scheduling, and diagnostic collection
"""

import json
import subprocess
import threading
import time
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running" 
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class TaskType(Enum):
    APPLESCRIPT = "applescript"
    SHELL_COMMAND = "shell_command"
    SYSTEM_INFO = "system_info"
    MAINTENANCE = "maintenance"
    FILE_TRANSFER = "file_transfer"
    PACKAGE_INSTALL = "package_install"
    RESTART = "restart"

@dataclass
class MacTask:
    """Represents a Mac management task"""
    id: str
    type: TaskType
    target_client: str
    command: Dict[str, Any]
    status: TaskStatus
    created_at: datetime
    scheduled_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    retries: int = 0
    max_retries: int = 3

class MacTaskManager:
    """Manages Mac tasks and ARD proxy operations"""
    
    def __init__(self):
        self.tasks: Dict[str, MacTask] = {}
        self.running_tasks: Dict[str, threading.Thread] = {}
        self.task_queue: List[str] = []
        self.clients: Dict[str, Dict[str, Any]] = {}
        self.lock = threading.Lock()
        
        # Start task processor
        self.processor_thread = threading.Thread(target=self._process_tasks, daemon=True)
        self.processor_thread.start()
    
    def register_client(self, client_id: str, client_info: Dict[str, Any]) -> Dict[str, Any]:
        """Register a new Mac client"""
        with self.lock:
            self.clients[client_id] = {
                **client_info,
                "registered_at": datetime.now().isoformat(),
                "last_seen": datetime.now().isoformat(),
                "status": "online"
            }
        
        return {
            "status": "success",
            "client_id": client_id,
            "message": "Client registered successfully"
        }
    
    def get_clients(self) -> Dict[str, Any]:
        """Get list of registered clients"""
        with self.lock:
            return {
                "clients": dict(self.clients),
                "total_count": len(self.clients),
                "online_count": len([c for c in self.clients.values() if c.get("status") == "online"])
            }
    
    def create_task(self, task_type: TaskType, target_client: str, command: Dict[str, Any], 
                   scheduled_at: Optional[datetime] = None) -> str:
        """Create a new Mac task"""
        task_id = str(uuid.uuid4())
        
        task = MacTask(
            id=task_id,
            type=task_type,
            target_client=target_client,
            command=command,
            status=TaskStatus.PENDING,
            created_at=datetime.now(),
            scheduled_at=scheduled_at
        )
        
        with self.lock:
            self.tasks[task_id] = task
            if scheduled_at is None or scheduled_at <= datetime.now():
                self.task_queue.append(task_id)
        
        return task_id
    
    def get_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Get task details"""
        with self.lock:
            task = self.tasks.get(task_id)
            if task:
                return asdict(task)
        return None
    
    def get_tasks(self, client_id: Optional[str] = None, status: Optional[TaskStatus] = None) -> List[Dict[str, Any]]:
        """Get list of tasks with optional filtering"""
        with self.lock:
            tasks = list(self.tasks.values())
            
            if client_id:
                tasks = [t for t in tasks if t.target_client == client_id]
            
            if status:
                tasks = [t for t in tasks if t.status == status]
            
            return [asdict(t) for t in tasks]
    
    def cancel_task(self, task_id: str) -> Dict[str, Any]:
        """Cancel a pending or running task"""
        with self.lock:
            task = self.tasks.get(task_id)
            if not task:
                return {"status": "error", "error": "Task not found"}
            
            if task.status in [TaskStatus.COMPLETED, TaskStatus.FAILED, TaskStatus.CANCELLED]:
                return {"status": "error", "error": f"Cannot cancel task in {task.status.value} state"}
            
            task.status = TaskStatus.CANCELLED
            task.completed_at = datetime.now()
            
            # Remove from queue if pending
            if task_id in self.task_queue:
                self.task_queue.remove(task_id)
            
            return {"status": "success", "message": "Task cancelled"}
    
    def _process_tasks(self):
        """Background task processor"""
        while True:
            try:
                # Process scheduled tasks
                self._check_scheduled_tasks()
                
                # Process pending tasks
                if self.task_queue:
                    with self.lock:
                        if self.task_queue:
                            task_id = self.task_queue.pop(0)
                            task = self.tasks.get(task_id)
                            
                            if task and task.status == TaskStatus.PENDING:
                                # Start task in separate thread
                                thread = threading.Thread(target=self._execute_task, args=(task,))
                                self.running_tasks[task_id] = thread
                                thread.start()
                
                time.sleep(1)  # Check every second
                
            except Exception as e:
                print(f"Error in task processor: {e}")
                time.sleep(5)
    
    def _check_scheduled_tasks(self):
        """Check for scheduled tasks that are ready to run"""
        now = datetime.now()
        
        with self.lock:
            for task in self.tasks.values():
                if (task.status == TaskStatus.PENDING and 
                    task.scheduled_at and 
                    task.scheduled_at <= now and 
                    task.id not in self.task_queue):
                    self.task_queue.append(task.id)
    
    def _execute_task(self, task: MacTask):
        """Execute a single task"""
        try:
            with self.lock:
                task.status = TaskStatus.RUNNING
                task.started_at = datetime.now()
            
            # Execute based on task type
            if task.type == TaskType.APPLESCRIPT:
                result = self._execute_applescript_task(task)
            elif task.type == TaskType.SHELL_COMMAND:
                result = self._execute_shell_task(task)
            elif task.type == TaskType.SYSTEM_INFO:
                result = self._execute_system_info_task(task)
            elif task.type == TaskType.MAINTENANCE:
                result = self._execute_maintenance_task(task)
            elif task.type == TaskType.RESTART:
                result = self._execute_restart_task(task)
            else:
                result = {"success": False, "error": f"Unsupported task type: {task.type.value}"}
            
            with self.lock:
                task.result = result
                task.status = TaskStatus.COMPLETED if result.get("success") else TaskStatus.FAILED
                task.completed_at = datetime.now()
                
                # Remove from running tasks
                if task.id in self.running_tasks:
                    del self.running_tasks[task.id]
            
        except Exception as e:
            with self.lock:
                task.error = str(e)
                task.status = TaskStatus.FAILED
                task.completed_at = datetime.now()
                
                if task.id in self.running_tasks:
                    del self.running_tasks[task.id]
    
    def _execute_applescript_task(self, task: MacTask) -> Dict[str, Any]:
        """Execute AppleScript task"""
        try:
            script = task.command.get("script", "")
            if not script:
                return {"success": False, "error": "No script provided"}
            
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                text=True,
                timeout=task.command.get("timeout", 30)
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "error": result.stderr.strip(),
                "return_code": result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "AppleScript execution timed out"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _execute_shell_task(self, task: MacTask) -> Dict[str, Any]:
        """Execute shell command task"""
        try:
            command = task.command.get("command", "")
            if not command:
                return {"success": False, "error": "No command provided"}
            
            # Security check
            allowed_commands = [
                "dscl", "scutil", "system_profiler", "sw_vers", "diskutil",
                "pmset", "networksetup", "security", "launchctl", "ps",
                "top", "vm_stat", "iotop", "netstat", "lsof", "df", "du"
            ]
            
            cmd_parts = command.split()
            if not cmd_parts or cmd_parts[0] not in allowed_commands:
                return {"success": False, "error": f"Command not allowed: {cmd_parts[0] if cmd_parts else 'empty'}"}
            
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=task.command.get("timeout", 30)
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "error": result.stderr.strip(),
                "return_code": result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "Command execution timed out"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _execute_system_info_task(self, task: MacTask) -> Dict[str, Any]:
        """Execute system information collection task"""
        try:
            info_type = task.command.get("info_type", "basic")
            
            if info_type == "basic":
                return self._get_basic_system_info()
            elif info_type == "hardware":
                return self._get_hardware_info()
            elif info_type == "network":
                return self._get_network_info()
            elif info_type == "security":
                return self._get_security_info()
            else:
                return {"success": False, "error": f"Unknown info type: {info_type}"}
                
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _execute_maintenance_task(self, task: MacTask) -> Dict[str, Any]:
        """Execute maintenance task"""
        try:
            maintenance_type = task.command.get("maintenance_type", "")
            
            maintenance_scripts = {
                "cleanup": [
                    "sudo periodic daily",
                    "sudo dscacheutil -flushcache"
                ],
                "permissions": [
                    "sudo diskutil repairPermissions /"
                ],
                "cache_clear": [
                    "sudo dscacheutil -flushcache",
                    "sudo killall -HUP mDNSResponder"
                ]
            }
            
            scripts = maintenance_scripts.get(maintenance_type, [])
            if not scripts:
                return {"success": False, "error": f"Unknown maintenance type: {maintenance_type}"}
            
            results = []
            for script in scripts:
                result = subprocess.run(
                    script,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=120
                )
                results.append({
                    "script": script,
                    "success": result.returncode == 0,
                    "output": result.stdout.strip(),
                    "error": result.stderr.strip()
                })
            
            success_count = sum(1 for r in results if r["success"])
            
            return {
                "success": success_count == len(results),
                "results": results,
                "success_count": success_count,
                "total_count": len(results)
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _execute_restart_task(self, task: MacTask) -> Dict[str, Any]:
        """Execute restart task"""
        try:
            delay = task.command.get("delay", 60)
            
            result = subprocess.run(
                f"sudo shutdown -r +{delay//60}",
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "error": result.stderr.strip(),
                "message": f"Restart scheduled in {delay} seconds"
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _get_basic_system_info(self) -> Dict[str, Any]:
        """Get basic system information"""
        try:
            # Get macOS version
            sw_vers = subprocess.run(["sw_vers"], capture_output=True, text=True, timeout=10)
            
            # Get hostname
            hostname = subprocess.run(["hostname"], capture_output=True, text=True, timeout=10)
            
            # Get uptime
            uptime = subprocess.run(["uptime"], capture_output=True, text=True, timeout=10)
            
            return {
                "success": True,
                "system_version": sw_vers.stdout.strip() if sw_vers.returncode == 0 else "Unknown",
                "hostname": hostname.stdout.strip() if hostname.returncode == 0 else "Unknown",
                "uptime": uptime.stdout.strip() if uptime.returncode == 0 else "Unknown",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _get_hardware_info(self) -> Dict[str, Any]:
        """Get hardware information"""
        try:
            result = subprocess.run(
                ["system_profiler", "SPHardwareDataType"],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            return {
                "success": result.returncode == 0,
                "hardware_info": result.stdout.strip(),
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _get_network_info(self) -> Dict[str, Any]:
        """Get network information"""
        try:
            # Get network interfaces
            ifconfig = subprocess.run(["ifconfig"], capture_output=True, text=True, timeout=10)
            
            # Get routing table
            netstat = subprocess.run(["netstat", "-rn"], capture_output=True, text=True, timeout=10)
            
            return {
                "success": True,
                "interfaces": ifconfig.stdout.strip() if ifconfig.returncode == 0 else "Unknown",
                "routing_table": netstat.stdout.strip() if netstat.returncode == 0 else "Unknown",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _get_security_info(self) -> Dict[str, Any]:
        """Get security information"""
        try:
            # Check SIP status
            csrutil = subprocess.run(["csrutil", "status"], capture_output=True, text=True, timeout=10)
            
            # Check Gatekeeper status
            gatekeeper = subprocess.run(["spctl", "--status"], capture_output=True, text=True, timeout=10)
            
            return {
                "success": True,
                "sip_status": csrutil.stdout.strip() if csrutil.returncode == 0 else "Unknown",
                "gatekeeper_status": gatekeeper.stdout.strip() if gatekeeper.returncode == 0 else "Unknown",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get task management statistics"""
        with self.lock:
            total_tasks = len(self.tasks)
            status_counts = {}
            
            for status in TaskStatus:
                status_counts[status.value] = len([t for t in self.tasks.values() if t.status == status])
            
            return {
                "total_tasks": total_tasks,
                "status_counts": status_counts,
                "running_tasks": len(self.running_tasks),
                "queued_tasks": len(self.task_queue),
                "registered_clients": len(self.clients),
                "online_clients": len([c for c in self.clients.values() if c.get("status") == "online"])
            }

# Global task manager instance
mac_task_manager = MacTaskManager()