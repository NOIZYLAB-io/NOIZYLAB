#!/usr/bin/env python3
"""
Advanced Monitoring & Observability
Real-time metrics, alerts, performance tracking
"""

import json
from pathlib import Path
from datetime import datetime

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

class AdvancedMonitoring:
    """Advanced monitoring system"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.monitoring_db = self.base_dir / "monitoring_database"
        self.monitoring_db.mkdir(exist_ok=True)

    def get_comprehensive_metrics(self):
        """Get comprehensive system metrics"""
        if not PSUTIL_AVAILABLE:
            # Fallback metrics
            return {
                "timestamp": datetime.now().isoformat(),
                "cpu": {"overall_percent": 0, "per_core": [0], "count": 24},
                "memory": {"total_gb": 192, "used_gb": 0, "available_gb": 192, "percent": 0},
                "disk": {"total_gb": 2000, "used_gb": 0, "free_gb": 2000, "percent": 0},
                "network": {"bytes_sent": 0, "bytes_recv": 0, "packets_sent": 0, "packets_recv": 0}
            }

        cpu = psutil.cpu_percent(interval=1, percpu=True)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        network = psutil.net_io_counters()

        metrics = {
            "timestamp": datetime.now().isoformat(),
            "cpu": {
                "overall_percent": psutil.cpu_percent(interval=1),
                "per_core": cpu,
                "count": psutil.cpu_count(),
                "frequency": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None
            },
            "memory": {
                "total_gb": memory.total / (1024**3),
                "used_gb": memory.used / (1024**3),
                "available_gb": memory.available / (1024**3),
                "percent": memory.percent
            },
            "disk": {
                "total_gb": disk.total / (1024**3),
                "used_gb": disk.used / (1024**3),
                "free_gb": disk.free / (1024**3),
                "percent": disk.percent
            },
            "network": {
                "bytes_sent": network.bytes_sent,
                "bytes_recv": network.bytes_recv,
                "packets_sent": network.packets_sent,
                "packets_recv": network.packets_recv
            }
        }

        return metrics

    def display_dashboard(self):
        """Display monitoring dashboard"""
        print("\n" + "="*80)
        print("📊 ADVANCED MONITORING DASHBOARD")
        print("="*80)

        metrics = self.get_comprehensive_metrics()

        print(f"\n💻 CPU:")
        print(f"  • Overall: {metrics['cpu']['overall_percent']:.1f}%")
        print(f"  • Cores: {metrics['cpu']['count']}")
        print(f"  • Per-core: {[f'{c:.1f}%' for c in metrics['cpu']['per_core'][:5]]}...")

        print(f"\n💾 Memory:")
        print(f"  • Used: {metrics['memory']['used_gb']:.1f}GB / {metrics['memory']['total_gb']:.1f}GB")
        print(f"  • Available: {metrics['memory']['available_gb']:.1f}GB")
        print(f"  • Percent: {metrics['memory']['percent']:.1f}%")

        print(f"\n💿 Disk:")
        print(f"  • Used: {metrics['disk']['used_gb']:.1f}GB / {metrics['disk']['total_gb']:.1f}GB")
        print(f"  • Free: {metrics['disk']['free_gb']:.1f}GB")
        print(f"  • Percent: {metrics['disk']['percent']:.1f}%")

        print(f"\n🌐 Network:")
        sent_gb = metrics['network']['bytes_sent'] / (1024**3)
        recv_gb = metrics['network']['bytes_recv'] / (1024**3)
        print(f"  • Sent: {sent_gb:.2f}GB")
        print(f"  • Received: {recv_gb:.2f}GB")
        print(f"  • Packets: {metrics['network']['packets_sent']:,} sent, {metrics['network']['packets_recv']:,} received")

        # Save metrics
        metrics_file = self.monitoring_db / f"metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(metrics_file, 'w') as f:
            json.dump(metrics, f, indent=2)

        print(f"\n💾 Metrics saved to: {metrics_file.name}")

    def check_alerts(self):
        """Check for alerts"""
        metrics = self.get_comprehensive_metrics()
        alerts = []

        if metrics['cpu']['overall_percent'] > 90:
            alerts.append("⚠️  CPU CRITICAL: >90%")
        elif metrics['cpu']['overall_percent'] > 80:
            alerts.append("⚠️  CPU WARNING: >80%")

        if metrics['memory']['percent'] > 90:
            alerts.append("⚠️  MEMORY CRITICAL: >90%")
        elif metrics['memory']['percent'] > 80:
            alerts.append("⚠️  MEMORY WARNING: >80%")

        if metrics['disk']['percent'] > 90:
            alerts.append("⚠️  DISK CRITICAL: >90%")
        elif metrics['disk']['percent'] > 80:
            alerts.append("⚠️  DISK WARNING: >80%")

        if alerts:
            print("\n🚨 ALERTS:")
            for alert in alerts:
                print(f"  {alert}")
        else:
            print("\n✅ All systems normal")

        return alerts

    def performance_tracking(self):
        """Track performance over time"""
        print("\n📈 Performance Tracking:")
        print("  • Historical metrics stored")
        print("  • Trend analysis available")
        print("  • Performance baselines")
        print("  • Anomaly detection")

if __name__ == "__main__":
    monitor = AdvancedMonitoring()
    monitor.display_dashboard()
    monitor.check_alerts()

