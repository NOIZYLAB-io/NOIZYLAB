#!/usr/bin/env python3
"""
UAP Core - Universal Agent Platform
The foundation for everything.
"""
import asyncio
import json
import time
from typing import Dict, Any, Callable
from dataclasses import dataclass
from pathlib import Path

@dataclass
class UapEvent:
    topic: str
    payload: Dict[str, Any]
    timestamp: float = None
    source: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()
    
    def to_json(self) -> str:
        return json.dumps({
            'topic': self.topic,
            'payload': self.payload,
            'timestamp': self.timestamp,
            'source': self.source
        })

class UapBus:
    """Event bus for the Universal Agent Platform"""
    
    def __init__(self):
        self.subscribers = {}
        self.agents = {}
        self.running = False
    
    def subscribe(self, topic: str, handler: Callable):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(handler)
    
    def publish(self, event: UapEvent):
        """Publish event to all subscribers"""
        if event.topic in self.subscribers:
            for handler in self.subscribers[event.topic]:
                try:
                    handler(event)
                except Exception as e:
                    print(f"Handler error for {event.topic}: {e}")
    
    def register_agent(self, name: str, agent_func: Callable):
        """Register an agent to run periodically"""
        self.agents[name] = agent_func
    
    async def start(self):
        """Start the UAP system"""
        self.running = True
        print("🚀 UAP Core starting...")
        
        # Start all agents
        tasks = []
        for name, agent in self.agents.items():
            task = asyncio.create_task(self._run_agent(name, agent))
            tasks.append(task)
        
        await asyncio.gather(*tasks)
    
    async def _run_agent(self, name: str, agent_func: Callable):
        """Run an agent with error handling"""
        while self.running:
            try:
                agent_func()
                await asyncio.sleep(5)  # Default interval
            except Exception as e:
                print(f"Agent {name} error: {e}")
                await asyncio.sleep(10)  # Backoff on error

# Global UAP instance
uap = UapBus()

if __name__ == "__main__":
    print("UAP Core - Ready to build the future! 🌟")
    asyncio.run(uap.start())