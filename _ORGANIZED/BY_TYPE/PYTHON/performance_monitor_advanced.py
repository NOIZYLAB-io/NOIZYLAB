#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Performance Monitor - Track all system performance
"""

import time
import psutil
from pathlib import Path

class PerformanceMonitor:
    """Monitor system performance"""

    def __init__(self):
        self.metrics = {}

    def track_function(self, func):
        """Decorator to track function performance"""
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            self.metrics[func.__name__] = duration
            return result
        return wrapper

    def get_metrics(self):
        """Get performance metrics"""
        return self.metrics

if __name__ == "__main__":
    try:
        monitor = PerformanceMonitor()
            print("✅ Performance Monitor Ready")

    except Exception as e:
        print(f"Error: {e}")
