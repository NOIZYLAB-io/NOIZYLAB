#!/usr/bin/env python3
"""
Intelligent System Monitor - AI-Powered Monitoring
==================================================
Self-learning monitoring system with predictive alerts
"""

import psutil
import time
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
from pathlib import Path
from dataclasses import dataclass
import json
import numpy as np
from collections import deque
import requests


@dataclass
class SystemMetrics:
    """System metrics snapshot"""
    timestamp: datetime
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    network_sent: int
    network_recv: int
    load_avg: Tuple[float, float, float]
    process_count: int
    temperature: Optional[float] = None


@dataclass
class Alert:
    """System alert"""
    level: str  # info, warning, critical
    category: str
    message: str
    value: float
    threshold: float
    timestamp: datetime
    auto_resolved: bool = False


class IntelligentMonitor:
    """AI-powered system monitoring with predictive alerts"""
    
    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = Path(__file__).parent / "monitoring.db"
        
        self.db_path = db_path
        self._init_database()
        
        # Sliding windows for trend analysis
        self.cpu_history = deque(maxlen=60)  # Last 60 measurements
        self.memory_history = deque(maxlen=60)
        self.disk_history = deque(maxlen=60)
        
        # Adaptive thresholds
        self.thresholds = {
            "cpu_warning": 70.0,
            "cpu_critical": 90.0,
            "memory_warning": 75.0,
            "memory_critical": 90.0,
            "disk_warning": 80.0,
            "disk_critical": 95.0,
            "temp_warning": 75.0,
            "temp_critical": 85.0
        }
        
        # Learning parameters
        self.baseline_established = False
        self.baseline_cpu = 0.0
        self.baseline_memory = 0.0
        
        # Alert cooldown to prevent spam
        self.alert_cooldown = {}
        
        print("🧠 Intelligent Monitor initialized")
    
    def _init_database(self):
        """Initialize monitoring database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Metrics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS system_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                load_avg_1 REAL,
                load_avg_5 REAL,
                load_avg_15 REAL,
                process_count INTEGER,
                temperature REAL
            )
        """)
        
        # Alerts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                level TEXT,
                category TEXT,
                message TEXT,
                value REAL,
                threshold REAL,
                auto_resolved BOOLEAN DEFAULT 0
            )
        """)
        
        # Predictions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                metric TEXT,
                predicted_value REAL,
                actual_value REAL,
                accuracy REAL
            )
        """)
        
        # Baseline table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS baseline (
                metric TEXT PRIMARY KEY,
                baseline_value REAL,
                std_dev REAL,
                last_updated DATETIME
            )
        """)
        
        conn.commit()
        conn.close()
    
    def collect_metrics(self) -> SystemMetrics:
        """Collect current system metrics"""
        # CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        
        # Memory
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        # Disk
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        
        # Network
        net = psutil.net_io_counters()
        network_sent = net.bytes_sent
        network_recv = net.bytes_recv
        
        # Load average
        load_avg = psutil.getloadavg()
        
        # Process count
        process_count = len(psutil.pids())
        
        # Temperature (if available)
        temperature = None
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                # Get first available temperature
                for name, entries in temps.items():
                    if entries:
                        temperature = entries[0].current
                        break
        except:
            pass
        
        metrics = SystemMetrics(
            timestamp=datetime.now(),
            cpu_percent=cpu_percent,
            memory_percent=memory_percent,
            disk_percent=disk_percent,
            network_sent=network_sent,
            network_recv=network_recv,
            load_avg=load_avg,
            process_count=process_count,
            temperature=temperature
        )
        
        # Store in history
        self.cpu_history.append(cpu_percent)
        self.memory_history.append(memory_percent)
        self.disk_history.append(disk_percent)
        
        return metrics
    
    def save_metrics(self, metrics: SystemMetrics):
        """Save metrics to database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO system_metrics 
            (timestamp, cpu_percent, memory_percent, disk_percent, 
             network_sent, network_recv, load_avg_1, load_avg_5, load_avg_15,
             process_count, temperature)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            metrics.timestamp,
            metrics.cpu_percent,
            metrics.memory_percent,
            metrics.disk_percent,
            metrics.network_sent,
            metrics.network_recv,
            metrics.load_avg[0],
            metrics.load_avg[1],
            metrics.load_avg[2],
            metrics.process_count,
            metrics.temperature
        ))
        
        conn.commit()
        conn.close()
    
    def analyze_metrics(self, metrics: SystemMetrics) -> List[Alert]:
        """Analyze metrics and generate alerts"""
        alerts = []
        
        # CPU analysis
        if metrics.cpu_percent >= self.thresholds["cpu_critical"]:
            alerts.append(Alert(
                level="critical",
                category="cpu",
                message=f"Critical CPU usage: {metrics.cpu_percent:.1f}%",
                value=metrics.cpu_percent,
                threshold=self.thresholds["cpu_critical"],
                timestamp=datetime.now()
            ))
        elif metrics.cpu_percent >= self.thresholds["cpu_warning"]:
            alerts.append(Alert(
                level="warning",
                category="cpu",
                message=f"High CPU usage: {metrics.cpu_percent:.1f}%",
                value=metrics.cpu_percent,
                threshold=self.thresholds["cpu_warning"],
                timestamp=datetime.now()
            ))
        
        # Memory analysis
        if metrics.memory_percent >= self.thresholds["memory_critical"]:
            alerts.append(Alert(
                level="critical",
                category="memory",
                message=f"Critical memory usage: {metrics.memory_percent:.1f}%",
                value=metrics.memory_percent,
                threshold=self.thresholds["memory_critical"],
                timestamp=datetime.now()
            ))
        elif metrics.memory_percent >= self.thresholds["memory_warning"]:
            alerts.append(Alert(
                level="warning",
                category="memory",
                message=f"High memory usage: {metrics.memory_percent:.1f}%",
                value=metrics.memory_percent,
                threshold=self.thresholds["memory_warning"],
                timestamp=datetime.now()
            ))
        
        # Disk analysis
        if metrics.disk_percent >= self.thresholds["disk_critical"]:
            alerts.append(Alert(
                level="critical",
                category="disk",
                message=f"Critical disk usage: {metrics.disk_percent:.1f}%",
                value=metrics.disk_percent,
                threshold=self.thresholds["disk_critical"],
                timestamp=datetime.now()
            ))
        elif metrics.disk_percent >= self.thresholds["disk_warning"]:
            alerts.append(Alert(
                level="warning",
                category="disk",
                message=f"High disk usage: {metrics.disk_percent:.1f}%",
                value=metrics.disk_percent,
                threshold=self.thresholds["disk_warning"],
                timestamp=datetime.now()
            ))
        
        # Temperature analysis
        if metrics.temperature:
            if metrics.temperature >= self.thresholds["temp_critical"]:
                alerts.append(Alert(
                    level="critical",
                    category="temperature",
                    message=f"Critical temperature: {metrics.temperature:.1f}°C",
                    value=metrics.temperature,
                    threshold=self.thresholds["temp_critical"],
                    timestamp=datetime.now()
                ))
            elif metrics.temperature >= self.thresholds["temp_warning"]:
                alerts.append(Alert(
                    level="warning",
                    category="temperature",
                    message=f"High temperature: {metrics.temperature:.1f}°C",
                    value=metrics.temperature,
                    threshold=self.thresholds["temp_warning"],
                    timestamp=datetime.now()
                ))
        
        # Trend-based alerts
        trend_alerts = self._analyze_trends()
        alerts.extend(trend_alerts)
        
        return alerts
    
    def _analyze_trends(self) -> List[Alert]:
        """Analyze trends and predict issues"""
        alerts = []
        
        if len(self.cpu_history) < 10:
            return alerts
        
        # CPU trend
        cpu_trend = self._calculate_trend(list(self.cpu_history))
        if cpu_trend > 2.0:  # Rapid increase
            current = self.cpu_history[-1]
            predicted = current + (cpu_trend * 5)  # 5 minutes ahead
            
            if predicted > self.thresholds["cpu_warning"]:
                alerts.append(Alert(
                    level="warning",
                    category="cpu_trend",
                    message=f"CPU trending up rapidly. Predicted: {predicted:.1f}% in 5 min",
                    value=cpu_trend,
                    threshold=2.0,
                    timestamp=datetime.now()
                ))
        
        # Memory trend
        memory_trend = self._calculate_trend(list(self.memory_history))
        if memory_trend > 1.0:
            current = self.memory_history[-1]
            predicted = current + (memory_trend * 10)  # 10 minutes ahead
            
            if predicted > self.thresholds["memory_warning"]:
                alerts.append(Alert(
                    level="warning",
                    category="memory_trend",
                    message=f"Memory trending up. Predicted: {predicted:.1f}% in 10 min",
                    value=memory_trend,
                    threshold=1.0,
                    timestamp=datetime.now()
                ))
        
        return alerts
    
    def _calculate_trend(self, values: List[float]) -> float:
        """Calculate trend (slope) of values"""
        if len(values) < 2:
            return 0.0
        
        x = np.arange(len(values))
        y = np.array(values)
        
        # Linear regression
        slope, _ = np.polyfit(x, y, 1)
        
        return float(slope)
    
    def predict_next_value(self, metric: str, horizon: int = 5) -> float:
        """Predict future value using simple linear extrapolation"""
        if metric == "cpu":
            history = list(self.cpu_history)
        elif metric == "memory":
            history = list(self.memory_history)
        elif metric == "disk":
            history = list(self.disk_history)
        else:
            return 0.0
        
        if len(history) < 10:
            return history[-1] if history else 0.0
        
        trend = self._calculate_trend(history)
        current = history[-1]
        predicted = current + (trend * horizon)
        
        return max(0.0, min(100.0, predicted))  # Clamp between 0-100
    
    def establish_baseline(self, days: int = 7):
        """Establish baseline from historical data"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(f"""
            SELECT AVG(cpu_percent), AVG(memory_percent), AVG(disk_percent)
            FROM system_metrics
            WHERE timestamp > datetime('now', '-{days} days')
        """)
        
        result = cursor.fetchone()
        
        if result and result[0]:
            self.baseline_cpu = result[0]
            self.baseline_memory = result[1]
            
            # Save to database
            cursor.execute("""
                INSERT OR REPLACE INTO baseline (metric, baseline_value, last_updated)
                VALUES ('cpu', ?, ?), ('memory', ?, ?), ('disk', ?, ?)
            """, (
                self.baseline_cpu, datetime.now(),
                self.baseline_memory, datetime.now(),
                result[2], datetime.now()
            ))
            
            conn.commit()
            self.baseline_established = True
            
            print(f"📊 Baseline established: CPU={self.baseline_cpu:.1f}%, Memory={self.baseline_memory:.1f}%")
        
        conn.close()
    
    def detect_anomalies(self, metrics: SystemMetrics) -> List[Alert]:
        """Detect anomalies based on baseline"""
        if not self.baseline_established:
            return []
        
        alerts = []
        
        # CPU anomaly
        cpu_deviation = abs(metrics.cpu_percent - self.baseline_cpu)
        if cpu_deviation > 30:  # 30% deviation
            alerts.append(Alert(
                level="warning",
                category="anomaly",
                message=f"CPU anomaly detected: {metrics.cpu_percent:.1f}% (baseline: {self.baseline_cpu:.1f}%)",
                value=cpu_deviation,
                threshold=30.0,
                timestamp=datetime.now()
            ))
        
        # Memory anomaly
        memory_deviation = abs(metrics.memory_percent - self.baseline_memory)
        if memory_deviation > 25:  # 25% deviation
            alerts.append(Alert(
                level="warning",
                category="anomaly",
                message=f"Memory anomaly detected: {metrics.memory_percent:.1f}% (baseline: {self.baseline_memory:.1f}%)",
                value=memory_deviation,
                threshold=25.0,
                timestamp=datetime.now()
            ))
        
        return alerts
    
    def save_alert(self, alert: Alert):
        """Save alert to database"""
        # Check cooldown
        cooldown_key = f"{alert.category}_{alert.level}"
        last_alert_time = self.alert_cooldown.get(cooldown_key)
        
        if last_alert_time:
            time_since = (datetime.now() - last_alert_time).seconds
            if time_since < 300:  # 5 minute cooldown
                return
        
        self.alert_cooldown[cooldown_key] = datetime.now()
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO alerts (timestamp, level, category, message, value, threshold, auto_resolved)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            alert.timestamp,
            alert.level,
            alert.category,
            alert.message,
            alert.value,
            alert.threshold,
            alert.auto_resolved
        ))
        
        conn.commit()
        conn.close()
    
    def send_alert_to_slack(self, alert: Alert):
        """Send alert to Slack"""
        try:
            level_emoji = {
                "info": "ℹ️",
                "warning": "⚠️",
                "critical": "🚨"
            }
            
            requests.post(
                "http://localhost:8003/notify/system-alert",
                json={
                    "title": f"{level_emoji.get(alert.level, '📊')} {alert.level.upper()}: {alert.category.title()}",
                    "message": alert.message,
                    "level": alert.level,
                    "details": {
                        "Current Value": f"{alert.value:.1f}",
                        "Threshold": f"{alert.threshold:.1f}",
                        "Time": alert.timestamp.strftime("%H:%M:%S")
                    }
                },
                timeout=2
            )
        except:
            pass  # Slack not available
    
    def get_health_score(self) -> Dict[str, any]:
        """Calculate overall system health score (0-100)"""
        metrics = self.collect_metrics()
        
        # Component scores
        cpu_score = max(0, 100 - metrics.cpu_percent)
        memory_score = max(0, 100 - metrics.memory_percent)
        disk_score = max(0, 100 - metrics.disk_percent)
        
        # Weighted average
        overall_score = (
            cpu_score * 0.4 +
            memory_score * 0.4 +
            disk_score * 0.2
        )
        
        # Health status
        if overall_score >= 80:
            status = "excellent"
        elif overall_score >= 60:
            status = "good"
        elif overall_score >= 40:
            status = "fair"
        else:
            status = "poor"
        
        return {
            "overall_score": overall_score,
            "status": status,
            "components": {
                "cpu": cpu_score,
                "memory": memory_score,
                "disk": disk_score
            },
            "metrics": {
                "cpu_percent": metrics.cpu_percent,
                "memory_percent": metrics.memory_percent,
                "disk_percent": metrics.disk_percent
            }
        }
    
    def monitor_loop(self, interval: int = 60, notify_slack: bool = True):
        """Main monitoring loop"""
        print(f"🔍 Starting monitoring (interval: {interval}s)")
        
        # Establish baseline if enough data
        try:
            self.establish_baseline()
        except:
            print("⚠️ Not enough historical data for baseline")
        
        iteration = 0
        
        while True:
            try:
                # Collect metrics
                metrics = self.collect_metrics()
                
                # Save metrics
                self.save_metrics(metrics)
                
                # Analyze and generate alerts
                alerts = self.analyze_metrics(metrics)
                
                # Detect anomalies
                if self.baseline_established:
                    anomaly_alerts = self.detect_anomalies(metrics)
                    alerts.extend(anomaly_alerts)
                
                # Process alerts
                for alert in alerts:
                    print(f"🚨 {alert.level.upper()}: {alert.message}")
                    self.save_alert(alert)
                    
                    if notify_slack and alert.level in ["warning", "critical"]:
                        self.send_alert_to_slack(alert)
                
                # Periodic health check
                if iteration % 10 == 0:  # Every 10 iterations
                    health = self.get_health_score()
                    print(f"💚 Health Score: {health['overall_score']:.1f} ({health['status']})")
                
                # Re-establish baseline periodically
                if iteration % 100 == 0 and iteration > 0:
                    self.establish_baseline()
                
                iteration += 1
                time.sleep(interval)
                
            except KeyboardInterrupt:
                print("\n🛑 Monitoring stopped")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(interval)


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Intelligent System Monitor")
    parser.add_argument("--interval", type=int, default=60, help="Monitoring interval (seconds)")
    parser.add_argument("--no-slack", action="store_true", help="Disable Slack notifications")
    
    args = parser.parse_args()
    
    monitor = IntelligentMonitor()
    monitor.monitor_loop(interval=args.interval, notify_slack=not args.no_slack)


if __name__ == "__main__":
    main()

