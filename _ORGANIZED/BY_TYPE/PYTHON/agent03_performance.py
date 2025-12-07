from __future__ import annotations
import time, psutil
from .registry import register
from .base import BaseAgent

@register("agent03_performance")
class AgentPerformance(BaseAgent):
    """Performance monitoring and optimization agent."""
    
    def setup(self):
        self.start_time = time.time()
        
    def step(self):
        runtime = time.time() - self.start_time
        load_avg = psutil.getloadavg() if hasattr(psutil, 'getloadavg') else [0, 0, 0]
        
        perf = {
            "runtime_seconds": round(runtime, 2),
            "load_average": load_avg[0] if load_avg else 0,
            "cpu_count": psutil.cpu_count(),
            "status": "optimal" if load_avg[0] < 2 else "loaded"
        }
        
        self.bus.publish("perf", perf)