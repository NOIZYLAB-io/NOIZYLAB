#!/usr/bin/env python3
"""
Agent Task Scheduler - Cron-like scheduling for recurring agent tasks
"""
import asyncio
import time
from datetime import datetime, timedelta
from typing import Dict, Any, List, Callable
from dataclasses import dataclass
import logging
from agent_core import Task, TaskPriority, coordinator

logger = logging.getLogger("TaskScheduler")

@dataclass
class ScheduledTask:
    """Represents a scheduled recurring task"""
    name: str
    action: str
    params: Dict[str, Any]
    interval_seconds: int
    priority: TaskPriority = TaskPriority.NORMAL
    last_run: float = 0
    enabled: bool = True
    run_count: int = 0

class TaskScheduler:
    """Scheduler for recurring agent tasks"""
    
    def __init__(self):
        self.scheduled_tasks: Dict[str, ScheduledTask] = {}
        self.running = False
        self.logger = logging.getLogger("TaskScheduler")
    
    def schedule(
        self,
        name: str,
        action: str,
        params: Dict[str, Any],
        interval_seconds: int,
        priority: TaskPriority = TaskPriority.NORMAL
    ):
        """Schedule a recurring task"""
        scheduled = ScheduledTask(
            name=name,
            action=action,
            params=params,
            interval_seconds=interval_seconds,
            priority=priority
        )
        
        self.scheduled_tasks[name] = scheduled
        self.logger.info(f"📅 Scheduled: {name} (every {interval_seconds}s)")
    
    def unschedule(self, name: str):
        """Remove a scheduled task"""
        if name in self.scheduled_tasks:
            del self.scheduled_tasks[name]
            self.logger.info(f"🗑️  Unscheduled: {name}")
    
    def enable(self, name: str):
        """Enable a scheduled task"""
        if name in self.scheduled_tasks:
            self.scheduled_tasks[name].enabled = True
            self.logger.info(f"✅ Enabled: {name}")
    
    def disable(self, name: str):
        """Disable a scheduled task"""
        if name in self.scheduled_tasks:
            self.scheduled_tasks[name].enabled = False
            self.logger.info(f"🚫 Disabled: {name}")
    
    async def run(self):
        """Run the scheduler loop"""
        self.running = True
        self.logger.info("🚀 Task Scheduler started")
        
        while self.running:
            current_time = time.time()
            
            for name, scheduled in list(self.scheduled_tasks.items()):
                if not scheduled.enabled:
                    continue
                
                # Check if it's time to run
                time_since_last = current_time - scheduled.last_run
                if time_since_last >= scheduled.interval_seconds:
                    # Create and submit task
                    task = Task(
                        id=f"scheduled_{name}_{int(current_time)}",
                        name=f"{scheduled.name} (Scheduled)",
                        action=scheduled.action,
                        params=scheduled.params,
                        priority=scheduled.priority
                    )
                    
                    success = coordinator.assign_task(task)
                    
                    if success:
                        scheduled.last_run = current_time
                        scheduled.run_count += 1
                        self.logger.info(f"⏰ Triggered: {name} (run #{scheduled.run_count})")
                    else:
                        self.logger.warning(f"⚠️  Failed to schedule: {name}")
            
            # Sleep for a short interval
            await asyncio.sleep(5)
    
    def stop(self):
        """Stop the scheduler"""
        self.running = False
        self.logger.info("🛑 Task Scheduler stopped")
    
    def get_status(self) -> Dict[str, Any]:
        """Get scheduler status"""
        return {
            "running": self.running,
            "scheduled_tasks": len(self.scheduled_tasks),
            "tasks": [
                {
                    "name": name,
                    "action": task.action,
                    "interval": task.interval_seconds,
                    "enabled": task.enabled,
                    "run_count": task.run_count,
                    "last_run": datetime.fromtimestamp(task.last_run).isoformat() if task.last_run else None
                }
                for name, task in self.scheduled_tasks.items()
            ]
        }

# Global scheduler instance
scheduler = TaskScheduler()

# Predefined schedules for NoizyLab operations
def setup_default_schedules():
    """Setup default recurring tasks"""
    
    # Health check every 5 minutes
    scheduler.schedule(
        name="system_health_check",
        action="check_health",
        params={},
        interval_seconds=300,
        priority=TaskPriority.LOW
    )
    
    # Audio library scan every hour
    scheduler.schedule(
        name="audio_library_scan",
        action="scan_audio_library",
        params={"path": "/Volumes/4TBSG/2026_SFX"},
        interval_seconds=3600,
        priority=TaskPriority.NORMAL
    )
    
    # Project backup check every 30 minutes
    scheduler.schedule(
        name="project_backup_check",
        action="scan_projects",
        params={"path": "/Volumes/RED DRAGON/noizylab_2026/Projects"},
        interval_seconds=1800,
        priority=TaskPriority.NORMAL
    )
    
    # Monitor resources every 2 minutes
    scheduler.schedule(
        name="resource_monitor",
        action="monitor_resources",
        params={},
        interval_seconds=120,
        priority=TaskPriority.LOW
    )
    
    logger.info("✅ Default schedules configured")

if __name__ == "__main__":
    print("📅 Agent Task Scheduler")
    setup_default_schedules()
    print(f"✓ {len(scheduler.scheduled_tasks)} tasks scheduled")
