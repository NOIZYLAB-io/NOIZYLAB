#!/usr/bin/env python3
"""
🤖 NOIZYLAB AGENT MASTER CONTROL
Complete orchestration and management system for all agents
"""
import os
import sys
import asyncio
import time
from pathlib import Path
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='🎯 [%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("MasterControl")

# Import agent modules
from agent_core import AgentCoordinator, Task, TaskPriority, coordinator
from specialized_agents import create_all_agents
from advanced_agents import create_advanced_agents
from task_scheduler import scheduler, setup_default_schedules
from agent_communication import global_message_bus, MessageType

class MasterControl:
    """Master control system for all NoizyLab agents"""
    
    def __init__(self):
        self.coordinator = coordinator
        self.scheduler = scheduler
        self.message_bus = global_message_bus
        self.all_agents = []
        self.start_time = None
        self.logger = logging.getLogger("MasterControl")
    
    def initialize(self):
        """Initialize the complete agent system"""
        print("\n" + "=" * 70)
        print("🤖 NOIZYLAB AGENT MASTER CONTROL SYSTEM")
        print("=" * 70)
        print(f"📅 Initialization started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70 + "\n")
        
        self.logger.info("🔧 Initializing master control system...")
        
        # Create all agents
        self.logger.info("📦 Loading agent modules...")
        basic_agents = create_all_agents()
        advanced_agents = create_advanced_agents()
        self.all_agents = basic_agents + advanced_agents
        
        # Register all agents
        self.logger.info("📝 Registering agents with coordinator...")
        for agent in self.all_agents:
            self.coordinator.register_agent(agent)
            self.logger.info(f"   ✓ {agent.name} ({len(agent.capabilities)} capabilities)")
        
        # Setup scheduled tasks
        self.logger.info("📅 Configuring task scheduler...")
        setup_default_schedules()
        self.logger.info(f"   ✓ {len(self.scheduler.scheduled_tasks)} recurring tasks configured")
        
        print("\n" + "=" * 70)
        print(f"✅ SYSTEM INITIALIZED")
        print(f"   • Total Agents: {len(self.all_agents)}")
        print(f"   • Total Capabilities: {sum(len(a.capabilities) for a in self.all_agents)}")
        print(f"   • Scheduled Tasks: {len(self.scheduler.scheduled_tasks)}")
        print("=" * 70 + "\n")
    
    def start_all_systems(self):
        """Start all agent systems"""
        self.start_time = time.time()
        
        self.logger.info("🚀 Starting all systems...")
        
        # Start all agents
        self.logger.info("   Starting agent fleet...")
        self.coordinator.start_all()
        
        # Start scheduler
        self.logger.info("   Starting task scheduler...")
        asyncio.create_task(self.scheduler.run())
        
        print("\n" + "=" * 70)
        print("✅ ALL SYSTEMS OPERATIONAL")
        print("=" * 70)
        
        self._print_status()
    
    def stop_all_systems(self):
        """Stop all systems gracefully"""
        self.logger.info("🛑 Shutting down all systems...")
        
        # Stop scheduler
        self.scheduler.stop()
        
        # Stop all agents
        self.coordinator.stop_all()
        
        # Calculate uptime
        if self.start_time:
            uptime = time.time() - self.start_time
            uptime_str = f"{int(uptime // 3600)}h {int((uptime % 3600) // 60)}m {int(uptime % 60)}s"
            self.logger.info(f"⏱️  Total uptime: {uptime_str}")
        
        print("\n" + "=" * 70)
        print("🏁 ALL SYSTEMS STOPPED")
        print("=" * 70 + "\n")
    
    def _print_status(self):
        """Print current system status"""
        status = self.coordinator.get_fleet_status()
        
        print("\n📊 SYSTEM STATUS")
        print("-" * 70)
        print(f"Active Agents:     {status['total_agents']}")
        print(f"Total Tasks:       {status['coordinator_metrics']['total_tasks']}")
        print(f"Completed Tasks:   {status['coordinator_metrics']['completed_tasks']}")
        print(f"Failed Tasks:      {status['coordinator_metrics']['failed_tasks']}")
        print(f"Scheduler Status:  {'Running' if self.scheduler.running else 'Stopped'}")
        print("-" * 70)
    
    def submit_comprehensive_scan(self):
        """Submit comprehensive system scan tasks"""
        self.logger.info("🔍 Submitting comprehensive scan tasks...")
        
        scan_tasks = [
            # File system scans
            Task(
                id="scan_noizylab",
                name="Scan NoizyLab Main Directory",
                action="scan_directory",
                params={"path": "/Volumes/RED DRAGON/noizylab_2026", "depth": 2},
                priority=TaskPriority.HIGH
            ),
            Task(
                id="scan_audio_sfx",
                name="Scan Audio SFX Library",
                action="scan_audio_library",
                params={"path": "/Volumes/4TBSG/2026_SFX"},
                priority=TaskPriority.HIGH
            ),
            Task(
                id="scan_projects",
                name="Scan All Projects",
                action="scan_projects",
                params={"path": "/Volumes/RED DRAGON/noizylab_2026"},
                priority=TaskPriority.NORMAL
            ),
            
            # Code analysis
            Task(
                id="find_todos",
                name="Find All TODOs",
                action="find_todos",
                params={"path": "/Volumes/RED DRAGON/noizylab_2026"},
                priority=TaskPriority.NORMAL
            ),
            Task(
                id="analyze_agents",
                name="Analyze Agent Code",
                action="analyze_code",
                params={"file_path": "/Volumes/RED DRAGON/noizylab_2026/agents/agent_core.py"},
                priority=TaskPriority.LOW
            ),
            
            # System monitoring
            Task(
                id="health_check",
                name="System Health Check",
                action="check_health",
                params={},
                priority=TaskPriority.CRITICAL
            ),
            Task(
                id="resource_monitor",
                name="Monitor System Resources",
                action="monitor_resources",
                params={},
                priority=TaskPriority.HIGH
            ),
            
            # Audio library maintenance
            Task(
                id="find_duplicates",
                name="Find Duplicate Audio Files",
                action="find_duplicates",
                params={"path": "/Volumes/4TBSG/2026_SFX"},
                priority=TaskPriority.NORMAL
            ),
            Task(
                id="verify_audio",
                name="Verify Audio File Integrity",
                action="verify_integrity",
                params={"path": "/Volumes/4TBSG/2026_SFX"},
                priority=TaskPriority.LOW
            )
        ]
        
        submitted = 0
        for task in scan_tasks:
            if self.coordinator.assign_task(task):
                submitted += 1
                self.logger.info(f"   ✓ {task.name}")
        
        self.logger.info(f"📋 Submitted {submitted}/{len(scan_tasks)} tasks")
        return submitted
    
    async def run_monitoring_loop(self):
        """Run continuous monitoring loop"""
        self.logger.info("🔄 Starting monitoring loop...")
        
        while True:
            await asyncio.sleep(30)
            
            # Print status update
            self._print_status()
            
            # Check for any issues
            status = self.coordinator.get_fleet_status()
            for agent_id, agent_status in status['agents'].items():
                if agent_status['status'] == 'error':
                    self.logger.warning(f"⚠️  Agent {agent_id} in error state!")
    
    def interactive_mode(self):
        """Run in interactive mode with menu"""
        while True:
            print("\n" + "=" * 70)
            print("🎮 MASTER CONTROL MENU")
            print("=" * 70)
            print("1. 📊 View Status")
            print("2. 🔍 Run Comprehensive Scan")
            print("3. 📋 Submit Custom Task")
            print("4. 📅 View Scheduled Tasks")
            print("5. 🤖 List All Agents")
            print("6. ⏸️  Pause/Resume Scheduler")
            print("7. 🛑 Stop All Systems and Exit")
            print("=" * 70)
            
            choice = input("\nEnter choice [1-7]: ").strip()
            
            if choice == "1":
                self._print_status()
            elif choice == "2":
                self.submit_comprehensive_scan()
            elif choice == "3":
                self._submit_custom_task()
            elif choice == "4":
                self._view_scheduled_tasks()
            elif choice == "5":
                self._list_agents()
            elif choice == "6":
                self._toggle_scheduler()
            elif choice == "7":
                self.stop_all_systems()
                break
            else:
                print("❌ Invalid choice")
            
            input("\nPress Enter to continue...")
    
    def _submit_custom_task(self):
        """Interactive task submission"""
        print("\n📋 CUSTOM TASK SUBMISSION")
        print("-" * 70)
        
        # List available actions
        all_actions = set()
        for agent in self.all_agents:
            all_actions.update(agent.capabilities.keys())
        
        print("Available actions:")
        for i, action in enumerate(sorted(all_actions), 1):
            print(f"  {i}. {action}")
        
        # This would be expanded for full interactive task creation
        print("\n(Full implementation would allow custom task creation)")
    
    def _view_scheduled_tasks(self):
        """View scheduled tasks"""
        print("\n📅 SCHEDULED TASKS")
        print("-" * 70)
        
        status = self.scheduler.get_status()
        for task in status['tasks']:
            enabled_str = "✓" if task['enabled'] else "✗"
            print(f"{enabled_str} {task['name']}")
            print(f"   Action: {task['action']}")
            print(f"   Interval: {task['interval']}s")
            print(f"   Run Count: {task['run_count']}")
            print(f"   Last Run: {task['last_run'] or 'Never'}")
            print()
    
    def _list_agents(self):
        """List all agents and their capabilities"""
        print("\n🤖 REGISTERED AGENTS")
        print("-" * 70)
        
        for agent in self.all_agents:
            status = agent.get_status()
            print(f"\n{agent.name} ({agent.agent_id})")
            print(f"   Status: {status['status']}")
            print(f"   Queue: {status['queue_size']} tasks")
            print(f"   Completed: {status['metrics']['tasks_completed']}")
            print(f"   Failed: {status['metrics']['tasks_failed']}")
            print(f"   Capabilities:")
            for cap in agent.capabilities.keys():
                print(f"      • {cap}")
    
    def _toggle_scheduler(self):
        """Toggle scheduler on/off"""
        if self.scheduler.running:
            self.scheduler.stop()
            print("⏸️  Scheduler paused")
        else:
            asyncio.create_task(self.scheduler.run())
            print("▶️  Scheduler resumed")

async def main():
    """Main entry point"""
    # Create master control
    mc = MasterControl()
    
    # Initialize
    mc.initialize()
    
    # Start all systems
    mc.start_all_systems()
    
    # Give agents a moment to start
    await asyncio.sleep(2)
    
    # Submit initial comprehensive scan
    mc.submit_comprehensive_scan()
    
    # Run in interactive mode
    try:
        mc.interactive_mode()
    except KeyboardInterrupt:
        print("\n\n⚠️  Keyboard interrupt received")
        mc.stop_all_systems()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
    
    print("\n" + "=" * 70)
    print("🏁 MASTER CONTROL SHUTDOWN COMPLETE")
    print("=" * 70 + "\n")
