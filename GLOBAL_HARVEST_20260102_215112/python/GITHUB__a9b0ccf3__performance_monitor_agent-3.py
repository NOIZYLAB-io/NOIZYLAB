#!/usr/bin/env python3
"""
GABRIEL Performance Monitor Agent (PERFMON)
Agent #23 - INTELLIGENCE DIVISION

Real-time system and application performance monitoring.
Provides insights, alerts, and optimization recommendations.

Author: GABRIEL AI FAMILY
Date: November 12, 2025
"""

import psutil
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import deque
from enum import Enum


class AlertLevel(Enum):
    """Alert severity levels"""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class PerformanceAlert:
    """Performance alert"""
    def __init__(self, level: AlertLevel, category: str, message: str, metric: float):
        self.level = level
        self.category = category
        self.message = message
        self.metric = metric
        self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict:
        return {
            'level': self.level.value,
            'category': self.category,
            'message': self.message,
            'metric': self.metric,
            'timestamp': self.timestamp.isoformat()
        }


class PerformanceMonitorAgent:
    """
    PERFMON - Performance Monitor Agent
    
    Monitors system and application performance in real-time.
    """
    
    def __init__(self):
        self.name = "PERFMON"
        self.division = "INTELLIGENCE"
        self.role = "Performance Monitor & System Optimizer"
        
        # Performance thresholds
        self.thresholds = {
            'cpu_warning': 70.0,  # %
            'cpu_critical': 90.0,
            'memory_warning': 80.0,  # %
            'memory_critical': 95.0,
            'disk_warning': 80.0,  # %
            'disk_critical': 90.0,
            'temperature_warning': 80.0,  # °C (if available)
            'temperature_critical': 90.0
        }
        
        # Historical data (last 60 samples = 5 minutes at 5s intervals)
        self.history_size = 60
        self.cpu_history = deque(maxlen=self.history_size)
        self.memory_history = deque(maxlen=self.history_size)
        self.disk_io_history = deque(maxlen=self.history_size)
        self.network_io_history = deque(maxlen=self.history_size)
        
        # Alerts
        self.active_alerts: List[PerformanceAlert] = []
        self.alert_history: List[PerformanceAlert] = []
        
        # Statistics
        self.stats = {
            'monitoring_start': datetime.now(),
            'samples_collected': 0,
            'alerts_triggered': 0,
            'optimizations_suggested': 0
        }
        
        # Process tracking
        self.process_stats = {}
        
        print(f"📊 {self.name} - Performance Monitor Agent initialized")
    
    def collect_system_metrics(self) -> Dict:
        """Collect current system performance metrics"""
        metrics = {}
        
        # CPU metrics
        cpu_percent = psutil.cpu_percent(interval=0.1, percpu=False)
        cpu_per_core = psutil.cpu_percent(interval=0.1, percpu=True)
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        
        metrics['cpu'] = {
            'percent': cpu_percent,
            'per_core': cpu_per_core,
            'count': cpu_count,
            'frequency': {
                'current': cpu_freq.current if cpu_freq else 0,
                'min': cpu_freq.min if cpu_freq else 0,
                'max': cpu_freq.max if cpu_freq else 0
            }
        }
        
        # Memory metrics
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        metrics['memory'] = {
            'total': memory.total / (1024**3),  # GB
            'available': memory.available / (1024**3),
            'used': memory.used / (1024**3),
            'percent': memory.percent,
            'swap_total': swap.total / (1024**3),
            'swap_used': swap.used / (1024**3),
            'swap_percent': swap.percent
        }
        
        # Disk metrics
        disk_usage = psutil.disk_usage('/')
        disk_io = psutil.disk_io_counters()
        
        metrics['disk'] = {
            'total': disk_usage.total / (1024**3),  # GB
            'used': disk_usage.used / (1024**3),
            'free': disk_usage.free / (1024**3),
            'percent': disk_usage.percent,
            'read_bytes': disk_io.read_bytes / (1024**2) if disk_io else 0,  # MB
            'write_bytes': disk_io.write_bytes / (1024**2) if disk_io else 0,
            'read_count': disk_io.read_count if disk_io else 0,
            'write_count': disk_io.write_count if disk_io else 0
        }
        
        # Network metrics
        net_io = psutil.net_io_counters()
        
        metrics['network'] = {
            'bytes_sent': net_io.bytes_sent / (1024**2),  # MB
            'bytes_recv': net_io.bytes_recv / (1024**2),
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv,
            'errors_in': net_io.errin,
            'errors_out': net_io.errout,
            'drops_in': net_io.dropin,
            'drops_out': net_io.dropout
        }
        
        # Battery (if laptop)
        try:
            battery = psutil.sensors_battery()
            if battery:
                metrics['battery'] = {
                    'percent': battery.percent,
                    'secsleft': battery.secsleft,
                    'power_plugged': battery.power_plugged
                }
        except Exception:
            metrics['battery'] = None
        
        # Temperature (if available)
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                metrics['temperature'] = {
                    sensor: [
                        {'label': t.label, 'current': t.current, 'high': t.high, 'critical': t.critical}
                        for t in readings
                    ]
                    for sensor, readings in temps.items()
                }
        except Exception:
            metrics['temperature'] = None
        
        metrics['timestamp'] = datetime.now().isoformat()
        
        # Update history
        self.cpu_history.append(cpu_percent)
        self.memory_history.append(memory.percent)
        if disk_io:
            self.disk_io_history.append({
                'read': disk_io.read_bytes,
                'write': disk_io.write_bytes
            })
        if net_io:
            self.network_io_history.append({
                'sent': net_io.bytes_sent,
                'recv': net_io.bytes_recv
            })
        
        self.stats['samples_collected'] += 1
        
        return metrics
    
    def collect_process_metrics(self) -> List[Dict]:
        """Collect metrics for all running processes"""
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'memory_info', 'status']):
            try:
                proc_info = proc.info
                
                # Skip system processes
                if proc_info['pid'] == 0:
                    continue
                
                processes.append({
                    'pid': proc_info['pid'],
                    'name': proc_info['name'],
                    'username': proc_info['username'],
                    'cpu_percent': proc_info['cpu_percent'] or 0.0,
                    'memory_percent': proc_info['memory_percent'] or 0.0,
                    'memory_mb': (proc_info['memory_info'].rss / (1024**2)) if proc_info['memory_info'] else 0,
                    'status': proc_info['status']
                })
                
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Sort by CPU usage
        processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        
        return processes
    
    def analyze_performance(self, metrics: Dict) -> List[PerformanceAlert]:
        """Analyze metrics and generate alerts"""
        alerts = []
        
        # Check CPU
        cpu_percent = metrics['cpu']['percent']
        if cpu_percent >= self.thresholds['cpu_critical']:
            alerts.append(PerformanceAlert(
                AlertLevel.CRITICAL,
                'CPU',
                f'CPU usage critical: {cpu_percent:.1f}%',
                cpu_percent
            ))
        elif cpu_percent >= self.thresholds['cpu_warning']:
            alerts.append(PerformanceAlert(
                AlertLevel.WARNING,
                'CPU',
                f'CPU usage high: {cpu_percent:.1f}%',
                cpu_percent
            ))
        
        # Check Memory
        memory_percent = metrics['memory']['percent']
        if memory_percent >= self.thresholds['memory_critical']:
            alerts.append(PerformanceAlert(
                AlertLevel.CRITICAL,
                'Memory',
                f'Memory usage critical: {memory_percent:.1f}%',
                memory_percent
            ))
        elif memory_percent >= self.thresholds['memory_warning']:
            alerts.append(PerformanceAlert(
                AlertLevel.WARNING,
                'Memory',
                f'Memory usage high: {memory_percent:.1f}%',
                memory_percent
            ))
        
        # Check Disk
        disk_percent = metrics['disk']['percent']
        if disk_percent >= self.thresholds['disk_critical']:
            alerts.append(PerformanceAlert(
                AlertLevel.CRITICAL,
                'Disk',
                f'Disk usage critical: {disk_percent:.1f}%',
                disk_percent
            ))
        elif disk_percent >= self.thresholds['disk_warning']:
            alerts.append(PerformanceAlert(
                AlertLevel.WARNING,
                'Disk',
                f'Disk usage high: {disk_percent:.1f}%',
                disk_percent
            ))
        
        # Check Swap
        swap_percent = metrics['memory']['swap_percent']
        if swap_percent > 50.0:
            alerts.append(PerformanceAlert(
                AlertLevel.WARNING,
                'Memory',
                f'High swap usage: {swap_percent:.1f}% (indicates memory pressure)',
                swap_percent
            ))
        
        # Check Temperature (if available)
        if metrics.get('temperature'):
            for sensor, readings in metrics['temperature'].items():
                for temp in readings:
                    if temp['critical'] and temp['current'] >= temp['critical']:
                        alerts.append(PerformanceAlert(
                            AlertLevel.CRITICAL,
                            'Temperature',
                            f'{sensor} temperature critical: {temp["current"]:.1f}°C',
                            temp['current']
                        ))
        
        # Check Battery (if available)
        if metrics.get('battery') and not metrics['battery']['power_plugged']:
            battery_percent = metrics['battery']['percent']
            if battery_percent <= 10:
                alerts.append(PerformanceAlert(
                    AlertLevel.CRITICAL,
                    'Battery',
                    f'Battery critically low: {battery_percent}%',
                    battery_percent
                ))
            elif battery_percent <= 20:
                alerts.append(PerformanceAlert(
                    AlertLevel.WARNING,
                    'Battery',
                    f'Battery low: {battery_percent}%',
                    battery_percent
                ))
        
        # Update active alerts
        self.active_alerts = alerts
        self.stats['alerts_triggered'] += len(alerts)
        
        # Add to history
        for alert in alerts:
            self.alert_history.append(alert)
        
        return alerts
    
    def get_optimization_recommendations(self, metrics: Dict, processes: List[Dict]) -> List[str]:
        """Generate optimization recommendations"""
        recommendations = []
        
        # High CPU usage
        if metrics['cpu']['percent'] > 70:
            top_cpu_processes = processes[:5]
            recommendations.append(
                f"🔴 High CPU usage ({metrics['cpu']['percent']:.1f}%). "
                f"Top consumers: {', '.join([p['name'] for p in top_cpu_processes])}"
            )
        
        # High Memory usage
        if metrics['memory']['percent'] > 80:
            top_memory_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]
            recommendations.append(
                f"🔴 High memory usage ({metrics['memory']['percent']:.1f}%). "
                f"Top consumers: {', '.join([p['name'] for p in top_memory_processes])}"
            )
            recommendations.append("💡 Consider closing unused applications or restarting memory-intensive apps")
        
        # High Swap usage
        if metrics['memory']['swap_percent'] > 50:
            recommendations.append(
                f"🔴 High swap usage ({metrics['memory']['swap_percent']:.1f}%). "
                "This indicates insufficient RAM."
            )
            recommendations.append("💡 Consider upgrading RAM or closing applications")
        
        # Disk space low
        if metrics['disk']['percent'] > 80:
            recommendations.append(
                f"🔴 Low disk space ({metrics['disk']['free']:.1f} GB free). "
            )
            recommendations.append("💡 Run disk cleanup or move large files to external storage")
        
        # CPU throttling detection (if frequency drops)
        cpu_freq = metrics['cpu']['frequency']
        if cpu_freq['current'] < cpu_freq['max'] * 0.7:
            recommendations.append(
                "⚠️ CPU may be throttling. Check temperature and power settings."
            )
        
        self.stats['optimizations_suggested'] += len(recommendations)
        
        return recommendations
    
    def get_performance_trends(self) -> Dict:
        """Analyze performance trends from historical data"""
        if not self.cpu_history:
            return {'status': 'insufficient_data'}
        
        trends = {}
        
        # CPU trend
        cpu_avg = sum(self.cpu_history) / len(self.cpu_history)
        cpu_recent = sum(list(self.cpu_history)[-10:]) / min(10, len(self.cpu_history))
        trends['cpu'] = {
            'average': cpu_avg,
            'recent': cpu_recent,
            'trend': 'increasing' if cpu_recent > cpu_avg else 'stable' if abs(cpu_recent - cpu_avg) < 5 else 'decreasing'
        }
        
        # Memory trend
        mem_avg = sum(self.memory_history) / len(self.memory_history)
        mem_recent = sum(list(self.memory_history)[-10:]) / min(10, len(self.memory_history))
        trends['memory'] = {
            'average': mem_avg,
            'recent': mem_recent,
            'trend': 'increasing' if mem_recent > mem_avg else 'stable' if abs(mem_recent - mem_avg) < 5 else 'decreasing'
        }
        
        return trends
    
    def get_system_health_score(self, metrics: Dict) -> int:
        """Calculate overall system health score (0-100)"""
        score = 100
        
        # CPU impact (max -30 points)
        cpu_percent = metrics['cpu']['percent']
        if cpu_percent > 90:
            score -= 30
        elif cpu_percent > 70:
            score -= 20
        elif cpu_percent > 50:
            score -= 10
        
        # Memory impact (max -30 points)
        memory_percent = metrics['memory']['percent']
        if memory_percent > 95:
            score -= 30
        elif memory_percent > 80:
            score -= 20
        elif memory_percent > 60:
            score -= 10
        
        # Disk impact (max -20 points)
        disk_percent = metrics['disk']['percent']
        if disk_percent > 90:
            score -= 20
        elif disk_percent > 80:
            score -= 10
        
        # Swap impact (max -20 points)
        swap_percent = metrics['memory']['swap_percent']
        if swap_percent > 50:
            score -= 20
        elif swap_percent > 25:
            score -= 10
        
        return max(0, score)
    
    def get_status(self) -> Dict:
        """Get agent status"""
        uptime = datetime.now() - self.stats['monitoring_start']
        
        return {
            'agent': self.name,
            'division': self.division,
            'role': self.role,
            'uptime': str(uptime).split('.')[0],
            'statistics': {
                'samples_collected': self.stats['samples_collected'],
                'alerts_triggered': self.stats['alerts_triggered'],
                'active_alerts': len(self.active_alerts),
                'optimizations_suggested': self.stats['optimizations_suggested']
            }
        }
    
    def display_status(self):
        """Display formatted status with current metrics"""
        status = self.get_status()
        metrics = self.collect_system_metrics()
        processes = self.collect_process_metrics()
        
        print("\n" + "="*70)
        print(f"📊 {self.name} - PERFORMANCE MONITOR STATUS")
        print("="*70)
        print(f"Uptime: {status['uptime']}")
        print(f"Samples Collected: {status['statistics']['samples_collected']}")
        
        # System Health Score
        health_score = self.get_system_health_score(metrics)
        health_emoji = "🟢" if health_score >= 80 else "🟡" if health_score >= 60 else "🔴"
        print(f"\n{health_emoji} System Health Score: {health_score}/100")
        
        # Current Metrics
        print(f"\n📈 Current Metrics:")
        print(f"   CPU: {metrics['cpu']['percent']:.1f}% ({metrics['cpu']['count']} cores)")
        print(f"   Memory: {metrics['memory']['used']:.1f}/{metrics['memory']['total']:.1f} GB ({metrics['memory']['percent']:.1f}%)")
        print(f"   Disk: {metrics['disk']['used']:.1f}/{metrics['disk']['total']:.1f} GB ({metrics['disk']['percent']:.1f}%)")
        
        if metrics.get('battery'):
            battery_emoji = "🔌" if metrics['battery']['power_plugged'] else "🔋"
            print(f"   {battery_emoji} Battery: {metrics['battery']['percent']}%")
        
        # Active Alerts
        alerts = self.analyze_performance(metrics)
        if alerts:
            print(f"\n⚠️  Active Alerts ({len(alerts)}):")
            for alert in alerts:
                emoji = "🔴" if alert.level == AlertLevel.CRITICAL else "🟡"
                print(f"   {emoji} {alert.message}")
        
        # Top Processes
        print(f"\n🔝 Top 5 CPU Consumers:")
        for i, proc in enumerate(processes[:5], 1):
            print(f"   {i}. {proc['name']}: {proc['cpu_percent']:.1f}% CPU, {proc['memory_mb']:.0f} MB")
        
        # Recommendations
        recommendations = self.get_optimization_recommendations(metrics, processes)
        if recommendations:
            print(f"\n💡 Optimization Recommendations:")
            for rec in recommendations[:3]:
                print(f"   {rec}")
        
        print("="*70 + "\n")


def main():
    """Main function for testing"""
    print("🌟 GABRIEL Performance Monitor Agent")
    print("=" * 70)
    
    # Initialize agent
    perfmon = PerformanceMonitorAgent()
    
    # Display initial status
    perfmon.display_status()
    
    # Monitor for a short period
    print("\n📊 Monitoring system performance...\n")
    for i in range(3):
        time.sleep(2)
        metrics = perfmon.collect_system_metrics()
        print(f"Sample {i+1}: CPU {metrics['cpu']['percent']:.1f}% | Memory {metrics['memory']['percent']:.1f}% | Health Score {perfmon.get_system_health_score(metrics)}/100")
    
    # Show trends
    trends = perfmon.get_performance_trends()
    if trends.get('cpu'):
        print(f"\n📈 Performance Trends:")
        print(f"   CPU: {trends['cpu']['trend']} (avg: {trends['cpu']['average']:.1f}%)")
        print(f"   Memory: {trends['memory']['trend']} (avg: {trends['memory']['average']:.1f}%)")


if __name__ == "__main__":
    main()
