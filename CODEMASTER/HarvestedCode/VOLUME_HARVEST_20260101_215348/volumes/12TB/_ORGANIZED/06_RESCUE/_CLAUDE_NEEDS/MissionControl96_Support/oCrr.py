#!/usr/bin/env python3
"""
Predictive Monitor - AI-powered system monitoring
Learns patterns and predicts failures before they happen.
"""
import asyncio
import json
import time
from collections import defaultdict, deque
from uap_core import uap, UapEvent

class PredictiveMonitor:
    def __init__(self):
        self.metrics = defaultdict(lambda: deque(maxlen=100))
        self.patterns = {}
        self.alerts = []
    
    def record_metric(self, name: str, value: float):
        """Record a metric value"""
        self.metrics[name].append({
            'value': value,
            'timestamp': time.time()
        })
        self._analyze_pattern(name)
    
    def _analyze_pattern(self, metric_name: str):
        """Simple pattern analysis - can be enhanced with ML"""
        values = [m['value'] for m in self.metrics[metric_name]]
        if len(values) < 10:
            return
        
        # Calculate trend
        recent = values[-5:]
        older = values[-10:-5]
        recent_avg = sum(recent) / len(recent)
        older_avg = sum(older) / len(older)
        
        # Predict potential issues
        if recent_avg > older_avg * 1.5:
            self._raise_alert(f"Rising trend detected in {metric_name}")
    
    def _raise_alert(self, message: str):
        """Raise a predictive alert"""
        alert = {
            'message': message,
            'timestamp': time.time(),
            'type': 'predictive'
        }
        self.alerts.append(alert)
        uap.publish(UapEvent(
            topic='system_alert',
            payload=alert,
            source='predictive_monitor'
        ))
    
    def get_health_score(self) -> float:
        """Calculate overall system health (0-100)"""
        if not self.metrics:
            return 100.0
        
        # Simple health calculation
        alert_penalty = len([a for a in self.alerts if time.time() - a['timestamp'] < 300]) * 10
        return max(0, 100 - alert_penalty)

# Initialize predictive monitor
monitor = PredictiveMonitor()

def monitor_agent():
    """Agent that collects system metrics"""
    import psutil
    
    # Collect CPU, memory, disk usage
    monitor.record_metric('cpu_percent', psutil.cpu_percent())
    monitor.record_metric('memory_percent', psutil.virtual_memory().percent)
    monitor.record_metric('disk_percent', psutil.disk_usage('/').percent)
    
    # Publish health score
    uap.publish(UapEvent(
        topic='system_health',
        payload={'score': monitor.get_health_score()},
        source='predictive_monitor'
    ))

# Register the monitoring agent
uap.register_agent('predictive_monitor', monitor_agent)

if __name__ == "__main__":
    print("🔮 Predictive Monitor - Seeing the future of your systems!")