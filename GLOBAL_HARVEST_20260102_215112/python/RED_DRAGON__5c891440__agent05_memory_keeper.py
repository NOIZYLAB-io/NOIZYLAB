from __future__ import annotations
import time, random
from statistics import mean
from .registry import register
from .base import BaseAgent

@register("agent05_memory_keeper")
class AgentMemoryKeeper(BaseAgent):
    """Memory management and historical data agent."""
    
    def setup(self):
        self.memory_samples = []
        
    def step(self):
        # Store memory usage samples
        import psutil
        mem = psutil.virtual_memory()
        self.memory_samples.append(mem.percent)
        
        # Keep only last 100 samples
        self.memory_samples = self.memory_samples[-100:]
        
        memory_data = {
            "current_percent": mem.percent,
            "average_percent": round(mean(self.memory_samples), 2) if self.memory_samples else 0,
            "samples_count": len(self.memory_samples),
            "trend": "stable"
        }
        
        self.bus.publish("memory_keeper", memory_data)