#!/usr/bin/env python3
"""
Agent Fleet Controller - Main orchestration system
Run this to start the entire agent fleet
"""
import asyncio
import signal
import sys
from datetime import datetime
from agent_core import AgentCoordinator, Task, TaskPriority
from specialized_agents import create_all_agents
import logging

# Setup enhanced logging
logging.basicConfig(
    level=logging.INFO,
    format='🚀 [%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("FleetController")

class FleetController:
    """Main controller for the agent fleet"""
    
    def __init__(self):
        self.coordinator = AgentCoordinator()
        self.agents = []
        self.running = False
        
    def initialize(self):
        """Initialize all agents and register them"""
        logger.info("🌟 Initializing NoizyLab Agent Fleet")
        logger.info("=" * 60)
        
        # Create and register all specialized agents
        self.agents = create_all_agents()
        
        for agent in self.agents:
            self.coordinator.register_agent(agent)
            logger.info(f"✓ {agent.name} ready with {len(agent.capabilities)} capabilities")
        
        logger.info("=" * 60)
        logger.info(f"✅ Fleet initialized with {len(self.agents)} agents")
    
    def start(self):
        """Start the agent fleet"""
        logger.info("🚀 Starting agent fleet...")
        self.coordinator.start_all()
        self.running = True
        logger.info("✅ All agents are now active and ready for tasks")
    
    def stop(self):
        """Stop the agent fleet"""
        logger.info("🛑 Stopping agent fleet...")
        self.coordinator.stop_all()
        self.running = False
        logger.info("✅ All agents stopped")
    
    def submit_task(self, task: Task) -> bool:
        """Submit a task to the fleet"""
        return self.coordinator.assign_task(task)
    
    def get_status(self):
        """Get fleet status"""
        return self.coordinator.get_fleet_status()
    
    def demo_tasks(self):
        """Submit demo tasks to show capabilities"""
        logger.info("📋 Submitting demo tasks...")
        
        demo_tasks = [
            Task(
                id="demo_001",
                name="Scan noizylab_2026 directory",
                action="scan_directory",
                params={"path": "/Volumes/RED DRAGON/noizylab_2026", "depth": 2},
                priority=TaskPriority.HIGH
            ),
            Task(
                id="demo_002",
                name="System health check",
                action="check_health",
                params={},
                priority=TaskPriority.CRITICAL
            ),
            Task(
                id="demo_003",
                name="Find TODO comments",
                action="find_todos",
                params={"path": "/Volumes/RED DRAGON/noizylab_2026/agents"},
                priority=TaskPriority.NORMAL
            ),
            Task(
                id="demo_004",
                name="Monitor system resources",
                action="monitor_resources",
                params={},
                priority=TaskPriority.LOW
            ),
            Task(
                id="demo_005",
                name="Search Python files",
                action="search_files",
                params={"path": "/Volumes/RED DRAGON/noizylab_2026", "pattern": "*.py"},
                priority=TaskPriority.NORMAL
            )
        ]
        
        for task in demo_tasks:
            if self.submit_task(task):
                logger.info(f"✓ Submitted: {task.name}")
            else:
                logger.warning(f"✗ Failed to submit: {task.name}")
        
        logger.info(f"📊 {len(demo_tasks)} demo tasks submitted")

def signal_handler(signum, frame):
    """Handle shutdown signals gracefully"""
    logger.info("\n🛑 Shutdown signal received")
    sys.exit(0)

async def status_monitor(controller: FleetController):
    """Monitor and display fleet status periodically"""
    while controller.running:
        await asyncio.sleep(10)
        status = controller.get_status()
        logger.info("📊 Fleet Status Update:")
        logger.info(f"   Active Agents: {status['total_agents']}")
        logger.info(f"   Total Tasks: {status['coordinator_metrics']['total_tasks']}")
        logger.info(f"   Completed: {status['coordinator_metrics']['completed_tasks']}")

def main():
    """Main entry point"""
    # Setup signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    print("\n" + "=" * 60)
    print("🤖 NOIZYLAB AGENT FLEET CONTROL SYSTEM")
    print("=" * 60)
    print(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60 + "\n")
    
    # Create and initialize fleet controller
    controller = FleetController()
    controller.initialize()
    
    # Start the fleet
    controller.start()
    
    # Run demo tasks
    import time
    time.sleep(1)  # Let agents start up
    controller.demo_tasks()
    
    # Keep running and monitoring
    try:
        logger.info("🔄 Fleet is operational. Press Ctrl+C to stop.")
        logger.info("=" * 60)
        
        # Run status monitor
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Keep the main thread alive
        while True:
            time.sleep(5)
            
            # Print occasional status
            status = controller.get_status()
            if status['coordinator_metrics']['total_tasks'] > 0:
                completed = sum(
                    a['metrics']['tasks_completed'] 
                    for a in status['agents'].values()
                )
                logger.info(f"📈 Progress: {completed} tasks completed")
    
    except KeyboardInterrupt:
        logger.info("\n🛑 Keyboard interrupt received")
    finally:
        controller.stop()
        logger.info("👋 Fleet controller shutdown complete")
        print("\n" + "=" * 60)
        print("🏁 NOIZYLAB AGENT FLEET STOPPED")
        print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
