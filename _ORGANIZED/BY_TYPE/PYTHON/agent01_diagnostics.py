from __future__ import annotations
import psutil, os, platform, subprocess
from .registry import register
from .base import BaseAgent

@register("agent01_diagnostics")
class AgentDiagnostics(BaseAgent):
    """System diagnostics and health monitoring agent."""
    
    def step(self):
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()
        boot_time = psutil.boot_time()
        
        diagnostics = {
            "cpu_percent": cpu,
            "memory_percent": mem.percent,
            "memory_available_gb": round(mem.available / (1024**3), 2),
            "platform": platform.system(),
            "python_version": platform.python_version(),
            "uptime_hours": round((psutil.time.time() - boot_time) / 3600, 1),
            "status": "ok" if cpu < 80 and mem.percent < 80 else "warning"
        }
        
        self.bus.publish("diagnostics", diagnostics)