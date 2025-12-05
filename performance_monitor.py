#!/usr/bin/env python3
"""
Performance Monitor - Real-time system monitoring
"""
import psutil
import time
from pathlib import Path

class PerformanceMonitor:
    """Monitor system performance"""

    def __init__(self):
        self.base_dir = Path(__file__).parent

    def get_stats(self):
        """Get current stats"""
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        return {
            "cpu_percent": cpu,
            "memory_percent": memory.percent,
            "memory_available": memory.available / (1024**3),  # GB
            "disk_percent": disk.percent,
            "disk_free": disk.free / (1024**3)  # GB
        }

    def monitor(self):
        """Monitor continuously"""
        while True:
            stats = self.get_stats()
            print(f"CPU: {stats['cpu_percent']}% | "
                  f"Memory: {stats['memory_percent']}% | "
                  f"Disk: {stats['disk_percent']}%")
            time.sleep(5)

if __name__ == "__main__":
    monitor = PerformanceMonitor()
    monitor.monitor()
