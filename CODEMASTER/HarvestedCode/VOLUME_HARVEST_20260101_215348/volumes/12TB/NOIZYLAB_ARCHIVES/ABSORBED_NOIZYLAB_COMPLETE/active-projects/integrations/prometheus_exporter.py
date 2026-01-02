#!/usr/bin/env python3
"""
Prometheus Metrics Exporter for NoizyLab
=========================================
Export custom metrics to Prometheus
"""

from prometheus_client import start_http_server, Gauge, Counter, Histogram, Info
import time
import psutil
import sqlite3
from pathlib import Path
from datetime import datetime
import requests


# System metrics
CPU_USAGE = Gauge('noizylab_cpu_usage_percent', 'CPU usage percentage')
MEMORY_USAGE = Gauge('noizylab_memory_usage_percent', 'Memory usage percentage')
DISK_USAGE = Gauge('noizylab_disk_usage_percent', 'Disk usage percentage')
LOAD_AVG_1 = Gauge('noizylab_load_average_1min', '1-minute load average')
LOAD_AVG_5 = Gauge('noizylab_load_average_5min', '5-minute load average')

# Slack metrics
SLACK_NOTIFICATIONS_TOTAL = Counter('noizylab_slack_notifications_total', 'Total Slack notifications sent')
SLACK_NOTIFICATIONS_FAILED = Counter('noizylab_slack_notifications_failed', 'Failed Slack notifications')
SLACK_NOTIFICATION_DURATION = Histogram('noizylab_slack_notification_duration_seconds', 'Slack notification duration')

# Network metrics
NETWORK_DEVICES_CONNECTED = Gauge('noizylab_network_devices_connected', 'Number of connected devices')
NETWORK_HANDSHAKES_TOTAL = Counter('noizylab_network_handshakes_total', 'Total handshakes performed')
NETWORK_HANDSHAKES_SUCCESS = Counter('noizylab_network_handshakes_success', 'Successful handshakes')
NETWORK_HANDSHAKE_DURATION = Histogram('noizylab_network_handshake_duration_seconds', 'Handshake duration')
PORT_STATUS = Gauge('noizylab_port_status', 'Port link status (1=up, 0=down)', ['port'])

# Service health
SERVICE_UP = Gauge('noizylab_service_up', 'Service health status (1=up, 0=down)', ['service'])
SERVICE_RESPONSE_TIME = Histogram('noizylab_service_response_time_seconds', 'Service response time', ['service'])

# AI metrics
AI_QUERIES_TOTAL = Counter('noizylab_ai_queries_total', 'Total AI queries')
AI_QUERY_DURATION = Histogram('noizylab_ai_query_duration_seconds', 'AI query duration')

# System info
SYSTEM_INFO = Info('noizylab_system', 'System information')


class NoizyLabMetricsExporter:
    """Export NoizyLab metrics to Prometheus"""
    
    def __init__(self):
        self.slack_db = Path("/Users/m2ultra/NOIZYLAB/integrations/slack/slack_data.db")
        self.network_db = Path("/Users/m2ultra/NOIZYLAB/network/network_devices.db")
        self.ai_db = Path("/Users/m2ultra/NOIZYLAB/ai/ai_operations.db")
        
        # Set system info
        import platform
        SYSTEM_INFO.info({
            'version': '1.0.0',
            'python_version': platform.python_version(),
            'platform': platform.system(),
            'hostname': platform.node()
        })
    
    def collect_metrics(self):
        """Collect all metrics"""
        self._collect_system_metrics()
        self._collect_slack_metrics()
        self._collect_network_metrics()
        self._collect_service_metrics()
        self._collect_ai_metrics()
    
    def _collect_system_metrics(self):
        """Collect system metrics"""
        # CPU
        CPU_USAGE.set(psutil.cpu_percent(interval=1))
        
        # Memory
        memory = psutil.virtual_memory()
        MEMORY_USAGE.set(memory.percent)
        
        # Disk
        disk = psutil.disk_usage('/')
        DISK_USAGE.set(disk.percent)
        
        # Load average
        if hasattr(psutil, 'getloadavg'):
            load = psutil.getloadavg()
            LOAD_AVG_1.set(load[0])
            LOAD_AVG_5.set(load[1])
    
    def _collect_slack_metrics(self):
        """Collect Slack metrics"""
        if not self.slack_db.exists():
            return
        
        try:
            conn = sqlite3.connect(str(self.slack_db))
            cursor = conn.cursor()
            
            # Total notifications
            cursor.execute("SELECT COUNT(*) FROM slack_notifications")
            total = cursor.fetchone()[0]
            SLACK_NOTIFICATIONS_TOTAL._value._value = total
            
            # Failed notifications
            cursor.execute("SELECT COUNT(*) FROM slack_notifications WHERE status = 'failed'")
            failed = cursor.fetchone()[0]
            SLACK_NOTIFICATIONS_FAILED._value._value = failed
            
            conn.close()
        except:
            pass
    
    def _collect_network_metrics(self):
        """Collect network metrics"""
        if not self.network_db.exists():
            return
        
        try:
            conn = sqlite3.connect(str(self.network_db))
            cursor = conn.cursor()
            
            # Connected devices
            cursor.execute("SELECT COUNT(*) FROM network_devices WHERE status = 'active'")
            devices = cursor.fetchone()[0]
            NETWORK_DEVICES_CONNECTED.set(devices)
            
            # Total handshakes
            cursor.execute("SELECT COUNT(*) FROM handshake_log")
            total = cursor.fetchone()[0]
            NETWORK_HANDSHAKES_TOTAL._value._value = total
            
            # Successful handshakes
            cursor.execute("SELECT COUNT(*) FROM handshake_log WHERE success = 1")
            success = cursor.fetchone()[0]
            NETWORK_HANDSHAKES_SUCCESS._value._value = success
            
            conn.close()
        except:
            pass
        
        # Try to get port status from API
        try:
            response = requests.get("http://localhost:8005/ports", timeout=2)
            if response.status_code == 200:
                ports = response.json().get("ports", {})
                for port_num, port_data in ports.items():
                    status = 1 if port_data.get("link_status") == "up" else 0
                    PORT_STATUS.labels(port=port_num).set(status)
        except:
            pass
    
    def _collect_service_metrics(self):
        """Collect service health metrics"""
        services = {
            "slack-api": 8003,
            "network-agent": 8005,
            "master-dashboard": 8501
        }
        
        for service_name, port in services.items():
            try:
                start = time.time()
                response = requests.get(f"http://localhost:{port}/health", timeout=2)
                duration = time.time() - start
                
                if response.status_code == 200:
                    SERVICE_UP.labels(service=service_name).set(1)
                else:
                    SERVICE_UP.labels(service=service_name).set(0)
                
                SERVICE_RESPONSE_TIME.labels(service=service_name).observe(duration)
            except:
                SERVICE_UP.labels(service=service_name).set(0)
    
    def _collect_ai_metrics(self):
        """Collect AI metrics"""
        if not self.ai_db.exists():
            return
        
        try:
            conn = sqlite3.connect(str(self.ai_db))
            cursor = conn.cursor()
            
            # Total queries
            cursor.execute("SELECT COUNT(*) FROM ai_analyses")
            total = cursor.fetchone()[0]
            AI_QUERIES_TOTAL._value._value = total
            
            conn.close()
        except:
            pass
    
    def run(self, port: int = 9091, interval: int = 15):
        """Run metrics exporter"""
        print(f"📊 Starting Prometheus exporter on port {port}")
        print(f"⏱️  Collection interval: {interval}s")
        
        # Start HTTP server
        start_http_server(port)
        
        print(f"✅ Metrics available at: http://localhost:{port}/metrics")
        
        # Collection loop
        while True:
            try:
                self.collect_metrics()
                time.sleep(interval)
            except KeyboardInterrupt:
                print("\n🛑 Exporter stopped")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(interval)


if __name__ == "__main__":
    exporter = NoizyLabMetricsExporter()
    exporter.run()

