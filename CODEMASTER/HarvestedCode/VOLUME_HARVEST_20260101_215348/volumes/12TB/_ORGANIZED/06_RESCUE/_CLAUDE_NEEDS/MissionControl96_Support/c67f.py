#!/usr/bin/env python3
"""
Mission Control 96 - Main Entry Point
Orchestrates all agents and services
"""

import asyncio
import signal
import sys
import time
from typing import Dict, Any, List
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import our modules
from noizy_agents import list_agents, create_agent
from portal.portal_server import app as portal_app


class EventBus:
    """Simple event bus for inter-agent communication"""
    
    def __init__(self):
        self.events: Dict[str, List[Dict[str, Any]]] = {}
        
    def publish(self, topic: str, payload: Dict[str, Any]):
        """Publish an event to a topic"""
        if topic not in self.events:
            self.events[topic] = []
        
        event = {
            "timestamp": time.time(),
            "payload": payload
        }
        self.events[topic].append(event)
        
        # Keep only last 100 events per topic
        if len(self.events[topic]) > 100:
            self.events[topic] = self.events[topic][-100:]
            
    def fetch(self, topic: str) -> List[Dict[str, Any]]:
        """Fetch events from a topic"""
        return self.events.get(topic, [])
        
    def clear(self, topic: str):
        """Clear events from a topic"""
        if topic in self.events:
            self.events[topic] = []


class MissionControl:
    """Main Mission Control orchestrator"""
    
    def __init__(self):
        self.bus = EventBus()
        self.agents = {}
        self.running = False
        
    def load_agents(self):
        """Load and initialize all agents"""
        logger.info("Loading agents...")
        
        available_agents = list_agents()
        for agent_name, agent_class in available_agents.items():
            try:
                agent = create_agent(agent_name, bus=self.bus)
                self.agents[agent_name] = agent
                logger.info(f"Loaded agent: {agent_name}")
            except Exception as e:
                logger.error(f"Failed to load agent {agent_name}: {e}")
                
    def start(self):
        """Start Mission Control"""
        logger.info("🚀 Starting Mission Control 96...")
        
        self.load_agents()
        self.running = True
        
        logger.info(f"Mission Control started with {len(self.agents)} agents")
        
    def stop(self):
        """Stop Mission Control"""
        logger.info("🛑 Stopping Mission Control 96...")
        self.running = False
        
    def step(self):
        """Execute one step of all active agents"""
        for agent_name, agent in self.agents.items():
            if agent.active:
                try:
                    agent.step()
                except Exception as e:
                    logger.error(f"Agent {agent_name} error: {e}")
                    
    def get_status(self) -> Dict[str, Any]:
        """Get system status"""
        return {
            "running": self.running,
            "agents": {name: agent.get_status() for name, agent in self.agents.items()},
            "event_topics": list(self.bus.events.keys())
        }
        
    async def run_loop(self):
        """Main execution loop"""
        while self.running:
            self.step()
            await asyncio.sleep(1)  # Run agents every second


# Global mission control instance
mission_control = MissionControl()


async def main():
    """Main entry point"""
    
    def signal_handler(signum, frame):
        logger.info("Received shutdown signal")
        mission_control.stop()
        sys.exit(0)
        
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        mission_control.start()
        await mission_control.run_loop()
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
    finally:
        mission_control.stop()


if __name__ == "__main__":
    asyncio.run(main())