#!/usr/bin/env python3
"""
NoizyLab Agent Core System
Advanced multi-agent coordination and execution framework
"""
import os
import json
import time
import asyncio
import logging
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import threading
from queue import Queue, PriorityQueue

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='🤖 [%(asctime)s] %(levelname)s - %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)

class AgentStatus(Enum):
    """Agent operational status"""
    IDLE = "idle"
    ACTIVE = "active"
    BUSY = "busy"
    ERROR = "error"
    OFFLINE = "offline"
    PAUSED = "paused"

class TaskPriority(Enum):
    """Task priority levels"""
    CRITICAL = 0
    HIGH = 1
    NORMAL = 2
    LOW = 3
    BACKGROUND = 4

@dataclass
class Task:
    """Represents a task to be executed by an agent"""
    id: str
    name: str
    action: str
    params: Dict[str, Any]
    priority: TaskPriority = TaskPriority.NORMAL
    created_at: float = field(default_factory=time.time)
    assigned_to: Optional[str] = None
    status: str = "pending"
    result: Optional[Any] = None
    error: Optional[str] = None
    
    def __lt__(self, other):
        return self.priority.value < other.priority.value

@dataclass
class AgentCapability:
    """Defines what an agent can do"""
    name: str
    description: str
    parameters: List[str]
    cost: float = 1.0  # Computational cost estimate

class Agent:
    """Base Agent class with enhanced capabilities"""
    
    def __init__(self, agent_id: str, name: str, capabilities: List[AgentCapability]):
        self.agent_id = agent_id
        self.name = name
        self.capabilities = {cap.name: cap for cap in capabilities}
        self.status = AgentStatus.IDLE
        self.task_queue: PriorityQueue = PriorityQueue()
        self.completed_tasks: List[Task] = []
        self.current_task: Optional[Task] = None
        self.logger = logging.getLogger(f"Agent.{name}")
        self.metrics = {
            "tasks_completed": 0,
            "tasks_failed": 0,
            "total_runtime": 0.0,
            "avg_task_time": 0.0
        }
        self.is_running = False
        self.worker_thread = None
        
    def can_handle(self, action: str) -> bool:
        """Check if agent can handle a specific action"""
        return action in self.capabilities
    
    def add_task(self, task: Task) -> bool:
        """Add a task to the agent's queue"""
        if not self.can_handle(task.action):
            self.logger.warning(f"Cannot handle task action: {task.action}")
            return False
        
        task.assigned_to = self.agent_id
        self.task_queue.put((task.priority.value, task))
        self.logger.info(f"Task {task.id} added to queue (Priority: {task.priority.name})")
        return True
    
    async def execute_task(self, task: Task) -> Any:
        """Execute a specific task - to be overridden by subclasses"""
        self.logger.info(f"Executing task: {task.name}")
        await asyncio.sleep(0.1)  # Simulate work
        return {"status": "success", "message": f"Task {task.name} completed"}
    
    def start(self):
        """Start the agent worker thread"""
        if self.is_running:
            self.logger.warning("Agent already running")
            return
        
        self.is_running = True
        self.worker_thread = threading.Thread(target=self._run_worker, daemon=True)
        self.worker_thread.start()
        self.logger.info(f"🚀 Agent {self.name} started")
    
    def stop(self):
        """Stop the agent worker thread"""
        self.is_running = False
        if self.worker_thread:
            self.worker_thread.join(timeout=5)
        self.logger.info(f"🛑 Agent {self.name} stopped")
    
    def _run_worker(self):
        """Worker thread that processes tasks"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        while self.is_running:
            try:
                if not self.task_queue.empty():
                    priority, task = self.task_queue.get(timeout=1)
                    self._process_task(task, loop)
                else:
                    time.sleep(0.5)
            except Exception as e:
                self.logger.error(f"Worker error: {e}")
                time.sleep(1)
        
        loop.close()
    
    def _process_task(self, task: Task, loop):
        """Process a single task"""
        self.status = AgentStatus.BUSY
        self.current_task = task
        task.status = "running"
        start_time = time.time()
        
        try:
            self.logger.info(f"⚡ Processing task: {task.name}")
            result = loop.run_until_complete(self.execute_task(task))
            
            task.status = "completed"
            task.result = result
            self.completed_tasks.append(task)
            self.metrics["tasks_completed"] += 1
            
            elapsed = time.time() - start_time
            self.metrics["total_runtime"] += elapsed
            self.metrics["avg_task_time"] = (
                self.metrics["total_runtime"] / self.metrics["tasks_completed"]
            )
            
            self.logger.info(f"✅ Task completed in {elapsed:.2f}s")
            
        except Exception as e:
            task.status = "failed"
            task.error = str(e)
            self.metrics["tasks_failed"] += 1
            self.logger.error(f"❌ Task failed: {e}")
        
        finally:
            self.current_task = None
            self.status = AgentStatus.IDLE if self.task_queue.empty() else AgentStatus.ACTIVE
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status and metrics"""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "status": self.status.value,
            "current_task": self.current_task.name if self.current_task else None,
            "queue_size": self.task_queue.qsize(),
            "capabilities": list(self.capabilities.keys()),
            "metrics": self.metrics
        }

class AgentCoordinator:
    """Coordinates multiple agents and distributes tasks"""
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.task_history: List[Task] = []
        self.logger = logging.getLogger("AgentCoordinator")
        self.metrics = {
            "total_tasks": 0,
            "completed_tasks": 0,
            "failed_tasks": 0,
            "active_agents": 0
        }
    
    def register_agent(self, agent: Agent):
        """Register an agent with the coordinator"""
        self.agents[agent.agent_id] = agent
        self.logger.info(f"📝 Registered agent: {agent.name} (ID: {agent.agent_id})")
    
    def unregister_agent(self, agent_id: str):
        """Unregister an agent"""
        if agent_id in self.agents:
            agent = self.agents[agent_id]
            agent.stop()
            del self.agents[agent_id]
            self.logger.info(f"🗑️ Unregistered agent: {agent_id}")
    
    def assign_task(self, task: Task) -> bool:
        """Intelligently assign a task to the best available agent"""
        eligible_agents = [
            agent for agent in self.agents.values()
            if agent.can_handle(task.action) and agent.status != AgentStatus.OFFLINE
        ]
        
        if not eligible_agents:
            self.logger.error(f"No eligible agents for task: {task.action}")
            return False
        
        # Select agent with smallest queue and best capability match
        best_agent = min(
            eligible_agents,
            key=lambda a: (a.task_queue.qsize(), a.capabilities[task.action].cost)
        )
        
        if best_agent.add_task(task):
            self.task_history.append(task)
            self.metrics["total_tasks"] += 1
            self.logger.info(f"📋 Task {task.id} assigned to {best_agent.name}")
            return True
        
        return False
    
    def start_all(self):
        """Start all registered agents"""
        for agent in self.agents.values():
            agent.start()
        self.metrics["active_agents"] = len(self.agents)
        self.logger.info(f"🚀 Started {len(self.agents)} agents")
    
    def stop_all(self):
        """Stop all agents"""
        for agent in self.agents.values():
            agent.stop()
        self.metrics["active_agents"] = 0
        self.logger.info("🛑 All agents stopped")
    
    def get_fleet_status(self) -> Dict[str, Any]:
        """Get status of all agents"""
        return {
            "total_agents": len(self.agents),
            "agents": {aid: agent.get_status() for aid, agent in self.agents.items()},
            "coordinator_metrics": self.metrics,
            "timestamp": datetime.now().isoformat()
        }
    
    def broadcast_task(self, task: Task) -> int:
        """Broadcast a task to all capable agents"""
        assigned = 0
        for agent in self.agents.values():
            if agent.can_handle(task.action):
                task_copy = Task(
                    id=f"{task.id}_{agent.agent_id}",
                    name=task.name,
                    action=task.action,
                    params=task.params.copy(),
                    priority=task.priority
                )
                if agent.add_task(task_copy):
                    assigned += 1
        
        self.logger.info(f"📢 Broadcast task to {assigned} agents")
        return assigned

# Global coordinator instance
coordinator = AgentCoordinator()

if __name__ == "__main__":
    print("🤖 NoizyLab Agent Core System")
    print("=" * 50)
    print(f"Coordinator initialized at {datetime.now()}")
