#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   📊 NOIZYLAB CLOUD AGENT ANALYTICS                                      ║
║                                                                           ║
║   Enterprise-grade analytics engine for comprehensive performance        ║
║   monitoring, pattern analysis, and cost optimization                    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import json
import sqlite3
import csv
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
import statistics
import logging

try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    logging.warning("matplotlib not available - chart generation disabled")

# ═══════════════════════════════════════════════════════════════════════════
# DATA MODELS
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class TaskExecution:
    """Single task execution record"""
    task_id: str
    task_type: str
    status: str
    duration_ms: float
    timestamp: datetime
    priority: str = "normal"
    error: Optional[str] = None
    result_size: int = 0

@dataclass
class AnalyticsSummary:
    """Analytics summary report"""
    period_start: datetime
    period_end: datetime
    total_tasks: int
    successful_tasks: int
    failed_tasks: int
    avg_duration_ms: float
    median_duration_ms: float
    p95_duration_ms: float
    p99_duration_ms: float
    tasks_per_hour: float
    most_common_task_types: List[Tuple[str, int]]
    most_common_errors: List[Tuple[str, int]]
    hourly_distribution: Dict[int, int]
    daily_distribution: Dict[str, int]

# ═══════════════════════════════════════════════════════════════════════════
# ANALYTICS ENGINE
# ═══════════════════════════════════════════════════════════════════════════

class CloudAgentAnalytics:
    """
    Comprehensive analytics engine for cloud agent performance monitoring
    and optimization recommendations.
    """
    
    def __init__(self, db_path: str = "cloud_agent_analytics.db"):
        """
        Initialize analytics engine.
        
        Args:
            db_path: Path to SQLite database for persistent storage
        """
        self.db_path = db_path
        self.logger = logging.getLogger("CloudAgentAnalytics")
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database schema"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS task_executions (
                task_id TEXT PRIMARY KEY,
                task_type TEXT NOT NULL,
                status TEXT NOT NULL,
                duration_ms REAL NOT NULL,
                timestamp TEXT NOT NULL,
                priority TEXT DEFAULT 'normal',
                error TEXT,
                result_size INTEGER DEFAULT 0
            )
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_timestamp 
            ON task_executions(timestamp)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_task_type 
            ON task_executions(task_type)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_status 
            ON task_executions(status)
        """)
        
        conn.commit()
        conn.close()
        
        self.logger.info(f"📊 Analytics database initialized: {self.db_path}")
    
    def record_task(self, task: TaskExecution):
        """
        Record a task execution.
        
        Args:
            task: TaskExecution object to record
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO task_executions
                (task_id, task_type, status, duration_ms, timestamp, priority, error, result_size)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                task.task_id,
                task.task_type,
                task.status,
                task.duration_ms,
                task.timestamp.isoformat(),
                task.priority,
                task.error,
                task.result_size
            ))
            
            conn.commit()
        except Exception as e:
            self.logger.error(f"Failed to record task: {e}")
        finally:
            conn.close()
    
    def get_summary(
        self,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None
    ) -> AnalyticsSummary:
        """
        Get comprehensive analytics summary for time period.
        
        Args:
            start_time: Start of analysis period (default: 24 hours ago)
            end_time: End of analysis period (default: now)
        
        Returns:
            AnalyticsSummary object with comprehensive metrics
        """
        if end_time is None:
            end_time = datetime.now()
        if start_time is None:
            start_time = end_time - timedelta(hours=24)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get all tasks in period
        cursor.execute("""
            SELECT task_type, status, duration_ms, timestamp, error
            FROM task_executions
            WHERE timestamp >= ? AND timestamp <= ?
        """, (start_time.isoformat(), end_time.isoformat()))
        
        tasks = cursor.fetchall()
        conn.close()
        
        if not tasks:
            return AnalyticsSummary(
                period_start=start_time,
                period_end=end_time,
                total_tasks=0,
                successful_tasks=0,
                failed_tasks=0,
                avg_duration_ms=0,
                median_duration_ms=0,
                p95_duration_ms=0,
                p99_duration_ms=0,
                tasks_per_hour=0,
                most_common_task_types=[],
                most_common_errors=[],
                hourly_distribution={},
                daily_distribution={}
            )
        
        # Calculate metrics
        total_tasks = len(tasks)
        successful_tasks = sum(1 for t in tasks if t[1] == "completed")
        failed_tasks = total_tasks - successful_tasks
        
        durations = [t[2] for t in tasks]
        avg_duration = statistics.mean(durations)
        median_duration = statistics.median(durations)
        
        sorted_durations = sorted(durations)
        p95_index = int(len(sorted_durations) * 0.95)
        p99_index = int(len(sorted_durations) * 0.99)
        p95_duration = sorted_durations[p95_index] if p95_index < len(sorted_durations) else sorted_durations[-1]
        p99_duration = sorted_durations[p99_index] if p99_index < len(sorted_durations) else sorted_durations[-1]
        
        # Calculate tasks per hour
        period_hours = (end_time - start_time).total_seconds() / 3600
        tasks_per_hour = total_tasks / period_hours if period_hours > 0 else 0
        
        # Task type distribution
        task_types = Counter(t[0] for t in tasks)
        most_common_types = task_types.most_common(5)
        
        # Error distribution
        errors = [t[4] for t in tasks if t[4]]
        error_counter = Counter(errors)
        most_common_errors = error_counter.most_common(5)
        
        # Hourly distribution
        hourly_dist: Dict[int, int] = defaultdict(int)
        for task in tasks:
            hour = datetime.fromisoformat(task[3]).hour
            hourly_dist[hour] += 1
        
        # Daily distribution
        daily_dist: Dict[str, int] = defaultdict(int)
        for task in tasks:
            day = datetime.fromisoformat(task[3]).strftime("%Y-%m-%d")
            daily_dist[day] += 1
        
        return AnalyticsSummary(
            period_start=start_time,
            period_end=end_time,
            total_tasks=total_tasks,
            successful_tasks=successful_tasks,
            failed_tasks=failed_tasks,
            avg_duration_ms=round(avg_duration, 2),
            median_duration_ms=round(median_duration, 2),
            p95_duration_ms=round(p95_duration, 2),
            p99_duration_ms=round(p99_duration, 2),
            tasks_per_hour=round(tasks_per_hour, 2),
            most_common_task_types=most_common_types,
            most_common_errors=most_common_errors,
            hourly_distribution=dict(hourly_dist),
            daily_distribution=dict(daily_dist)
        )
    
    def detect_anomalies(
        self,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        threshold_std_dev: float = 2.0
    ) -> List[Dict[str, Any]]:
        """
        Detect anomalous task execution patterns.
        
        Args:
            start_time: Start of analysis period
            end_time: End of analysis period
            threshold_std_dev: Number of standard deviations for anomaly threshold
        
        Returns:
            List of detected anomalies with details
        """
        if end_time is None:
            end_time = datetime.now()
        if start_time is None:
            start_time = end_time - timedelta(hours=24)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT task_type, duration_ms, timestamp
            FROM task_executions
            WHERE timestamp >= ? AND timestamp <= ? AND status = 'completed'
        """, (start_time.isoformat(), end_time.isoformat()))
        
        tasks = cursor.fetchall()
        conn.close()
        
        if len(tasks) < 10:
            return []
        
        # Group by task type
        by_type: Dict[str, List[float]] = defaultdict(list)
        task_details: Dict[str, List[Tuple[float, str]]] = defaultdict(list)
        
        for task_type, duration, timestamp in tasks:
            by_type[task_type].append(duration)
            task_details[task_type].append((duration, timestamp))
        
        anomalies: List[Dict[str, Any]] = []
        
        # Detect anomalies per task type
        for task_type, durations in by_type.items():
            if len(durations) < 5:
                continue
            
            mean = statistics.mean(durations)
            try:
                std_dev = statistics.stdev(durations)
            except statistics.StatisticsError:
                continue
            
            if std_dev == 0:
                continue
            
            # Find outliers
            for duration, timestamp in task_details[task_type]:
                z_score = (duration - mean) / std_dev
                
                if abs(z_score) > threshold_std_dev:
                    anomalies.append({
                        "task_type": task_type,
                        "timestamp": timestamp,
                        "duration_ms": duration,
                        "expected_duration_ms": round(mean, 2),
                        "z_score": round(z_score, 2),
                        "severity": "high" if abs(z_score) > 3 else "medium",
                        "description": f"Task duration {duration}ms is {abs(z_score):.1f} std devs from mean {mean:.0f}ms"
                    })
        
        # Sort by severity and z-score
        anomalies.sort(key=lambda x: (x["severity"] == "high", abs(x["z_score"])), reverse=True)
        
        return anomalies[:20]  # Return top 20 anomalies
    
    def get_cost_estimation(
        self,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        cost_per_million_requests: float = 0.50
    ) -> Dict[str, Any]:
        """
        Estimate costs based on usage patterns.
        
        Args:
            start_time: Start of analysis period
            end_time: End of analysis period
            cost_per_million_requests: Cost per million requests (Cloudflare Workers default)
        
        Returns:
            Cost estimation report with optimization suggestions
        """
        summary = self.get_summary(start_time, end_time)
        
        period_days = (summary.period_end - summary.period_start).days or 1
        monthly_tasks = (summary.total_tasks / period_days) * 30
        monthly_cost = (monthly_tasks / 1_000_000) * cost_per_million_requests
        
        # Calculate potential savings
        failed_task_ratio = summary.failed_tasks / summary.total_tasks if summary.total_tasks > 0 else 0
        potential_savings = monthly_cost * failed_task_ratio
        
        recommendations = []
        
        if failed_task_ratio > 0.05:
            recommendations.append(
                f"High failure rate ({failed_task_ratio*100:.1f}%). "
                "Investigate and fix errors to save ${potential_savings:.2f}/month"
            )
        
        if summary.avg_duration_ms > 1000:
            recommendations.append(
                "Average duration >1s. Optimize slow task handlers to reduce compute costs"
            )
        
        # Check for batch optimization opportunities
        if summary.tasks_per_hour < 60:
            recommendations.append(
                "Low task rate. Consider batching requests to reduce overhead"
            )
        
        return {
            "period_days": period_days,
            "total_tasks": summary.total_tasks,
            "monthly_projection": round(monthly_tasks),
            "monthly_cost_usd": round(monthly_cost, 2),
            "failed_tasks": summary.failed_tasks,
            "failed_task_cost_usd": round(potential_savings, 2),
            "cost_per_task_usd": round(monthly_cost / monthly_tasks * 1000, 6) if monthly_tasks > 0 else 0,
            "recommendations": recommendations
        }
    
    def export_to_json(
        self,
        filepath: str,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None
    ):
        """Export analytics data to JSON file"""
        summary = self.get_summary(start_time, end_time)
        anomalies = self.detect_anomalies(start_time, end_time)
        costs = self.get_cost_estimation(start_time, end_time)
        
        data = {
            "generated_at": datetime.now().isoformat(),
            "summary": asdict(summary),
            "anomalies": anomalies,
            "cost_estimation": costs
        }
        
        # Convert datetime objects to strings
        data["summary"]["period_start"] = data["summary"]["period_start"].isoformat()
        data["summary"]["period_end"] = data["summary"]["period_end"].isoformat()
        
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        
        self.logger.info(f"📄 Analytics exported to {filepath}")
    
    def export_to_csv(
        self,
        filepath: str,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None
    ):
        """Export raw task data to CSV file"""
        if end_time is None:
            end_time = datetime.now()
        if start_time is None:
            start_time = end_time - timedelta(hours=24)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM task_executions
            WHERE timestamp >= ? AND timestamp <= ?
            ORDER BY timestamp DESC
        """, (start_time.isoformat(), end_time.isoformat()))
        
        tasks = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()
        
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(tasks)
        
        self.logger.info(f"📄 Raw data exported to {filepath}")
    
    def generate_html_report(
        self,
        filepath: str,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None
    ):
        """
        Generate comprehensive HTML report with charts (if matplotlib available)
        """
        summary = self.get_summary(start_time, end_time)
        anomalies = self.detect_anomalies(start_time, end_time)
        costs = self.get_cost_estimation(start_time, end_time)
        
        # Generate charts if matplotlib available
        chart_paths = []
        if MATPLOTLIB_AVAILABLE:
            chart_paths = self._generate_charts(summary, filepath)
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>NOIZYLAB Cloud Agent Analytics Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #34495e; margin-top: 30px; }}
        .metric {{ display: inline-block; margin: 15px; padding: 20px; background: #ecf0f1; border-radius: 5px; min-width: 150px; }}
        .metric-value {{ font-size: 32px; font-weight: bold; color: #3498db; }}
        .metric-label {{ font-size: 14px; color: #7f8c8d; margin-top: 5px; }}
        .success {{ color: #27ae60; }}
        .warning {{ color: #f39c12; }}
        .danger {{ color: #e74c3c; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #3498db; color: white; }}
        tr:hover {{ background: #f5f5f5; }}
        .chart {{ margin: 20px 0; text-align: center; }}
        .chart img {{ max-width: 100%; border: 1px solid #ddd; border-radius: 5px; }}
        .recommendation {{ background: #fff3cd; padding: 15px; margin: 10px 0; border-left: 4px solid #ffc107; border-radius: 3px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 NOIZYLAB Cloud Agent Analytics Report</h1>
        <p><strong>Period:</strong> {summary.period_start.strftime("%Y-%m-%d %H:%M")} to {summary.period_end.strftime("%Y-%m-%d %H:%M")}</p>
        <p><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <h2>📈 Key Metrics</h2>
        <div class="metric">
            <div class="metric-value">{summary.total_tasks}</div>
            <div class="metric-label">Total Tasks</div>
        </div>
        <div class="metric">
            <div class="metric-value success">{summary.successful_tasks}</div>
            <div class="metric-label">Successful</div>
        </div>
        <div class="metric">
            <div class="metric-value danger">{summary.failed_tasks}</div>
            <div class="metric-label">Failed</div>
        </div>
        <div class="metric">
            <div class="metric-value">{summary.avg_duration_ms}ms</div>
            <div class="metric-label">Avg Duration</div>
        </div>
        <div class="metric">
            <div class="metric-value">{summary.tasks_per_hour:.1f}</div>
            <div class="metric-label">Tasks/Hour</div>
        </div>
        
        <h2>⚡ Performance Metrics</h2>
        <table>
            <tr>
                <th>Metric</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Median Duration</td>
                <td>{summary.median_duration_ms}ms</td>
            </tr>
            <tr>
                <td>95th Percentile</td>
                <td>{summary.p95_duration_ms}ms</td>
            </tr>
            <tr>
                <td>99th Percentile</td>
                <td>{summary.p99_duration_ms}ms</td>
            </tr>
            <tr>
                <td>Success Rate</td>
                <td>{(summary.successful_tasks/summary.total_tasks*100 if summary.total_tasks > 0 else 0):.1f}%</td>
            </tr>
        </table>
        
        <h2>🎯 Most Common Task Types</h2>
        <table>
            <tr>
                <th>Task Type</th>
                <th>Count</th>
                <th>Percentage</th>
            </tr>
            {"".join(f'<tr><td>{task_type}</td><td>{count}</td><td>{(count/summary.total_tasks*100 if summary.total_tasks > 0 else 0):.1f}%</td></tr>' 
                     for task_type, count in summary.most_common_task_types)}
        </table>
        
        <h2>💰 Cost Estimation</h2>
        <div class="metric">
            <div class="metric-value">${costs['monthly_cost_usd']}</div>
            <div class="metric-label">Monthly Cost (Projected)</div>
        </div>
        <div class="metric">
            <div class="metric-value">${costs['cost_per_task_usd']:.6f}</div>
            <div class="metric-label">Cost per Task</div>
        </div>
        <div class="metric">
            <div class="metric-value danger">${costs['failed_task_cost_usd']}</div>
            <div class="metric-label">Wasted on Failures</div>
        </div>
        
        <h2>💡 Optimization Recommendations</h2>
        {"".join(f'<div class="recommendation">🔔 {rec}</div>' for rec in costs['recommendations'])}
        
        <h2>🚨 Detected Anomalies</h2>
        <p>Found {len(anomalies)} anomalies (tasks with unusual execution patterns)</p>
        <table>
            <tr>
                <th>Task Type</th>
                <th>Timestamp</th>
                <th>Duration</th>
                <th>Expected</th>
                <th>Severity</th>
            </tr>
            {"".join(f'''<tr>
                <td>{a['task_type']}</td>
                <td>{a['timestamp']}</td>
                <td>{a['duration_ms']}ms</td>
                <td>{a['expected_duration_ms']}ms</td>
                <td class="{'danger' if a['severity'] == 'high' else 'warning'}">{a['severity'].upper()}</td>
            </tr>''' for a in anomalies[:10])}
        </table>
        
        {"".join(f'<div class="chart"><h3>{title}</h3><img src="{path}" /></div>' for title, path in chart_paths)}
        
    </div>
</body>
</html>
"""
        
        with open(filepath, "w") as f:
            f.write(html)
        
        self.logger.info(f"📊 HTML report generated: {filepath}")
    
    def _generate_charts(self, summary: AnalyticsSummary, base_filepath: str) -> List[Tuple[str, str]]:
        """Generate visualization charts"""
        import os
        chart_dir = os.path.dirname(base_filepath) or "."
        charts = []
        
        try:
            # Hourly distribution chart
            fig, ax = plt.subplots(figsize=(10, 5))
            hours = sorted(summary.hourly_distribution.keys())
            counts = [summary.hourly_distribution[h] for h in hours]
            ax.bar(hours, counts, color='#3498db')
            ax.set_xlabel('Hour of Day')
            ax.set_ylabel('Number of Tasks')
            ax.set_title('Task Distribution by Hour')
            ax.grid(axis='y', alpha=0.3)
            
            chart_path = os.path.join(chart_dir, "hourly_distribution.png")
            plt.savefig(chart_path, bbox_inches='tight', dpi=100)
            plt.close()
            charts.append(("Hourly Distribution", os.path.basename(chart_path)))
            
            # Task type distribution pie chart
            if summary.most_common_task_types:
                fig, ax = plt.subplots(figsize=(8, 8))
                types, counts = zip(*summary.most_common_task_types)
                ax.pie(counts, labels=types, autopct='%1.1f%%', startangle=90)
                ax.set_title('Task Type Distribution')
                
                chart_path = os.path.join(chart_dir, "task_types.png")
                plt.savefig(chart_path, bbox_inches='tight', dpi=100)
                plt.close()
                charts.append(("Task Types", os.path.basename(chart_path)))
        
        except Exception as e:
            self.logger.warning(f"Chart generation failed: {e}")
        
        return charts


# ═══════════════════════════════════════════════════════════════════════════
# COMMAND-LINE INTERFACE
# ═══════════════════════════════════════════════════════════════════════════

async def main():
    """Demo analytics usage"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
    analytics = CloudAgentAnalytics()
    
    # Simulate some task executions
    print("📊 Simulating task executions...")
    for i in range(100):
        task = TaskExecution(
            task_id=f"task-{i}",
            task_type=["echo", "inference", "monitoring", "file-processing"][i % 4],
            status="completed" if i % 10 != 0 else "failed",
            duration_ms=50 + (i % 100) * 10,
            timestamp=datetime.now() - timedelta(hours=24-i/4),
            priority="high" if i % 5 == 0 else "normal",
            error="Timeout error" if i % 10 == 0 else None,
            result_size=1024 * (i % 10)
        )
        analytics.record_task(task)
    
    # Get summary
    print("\n" + "="*70)
    print("ANALYTICS SUMMARY (Last 24 Hours)")
    print("="*70)
    
    summary = analytics.get_summary()
    print(f"Total Tasks: {summary.total_tasks}")
    print(f"Successful: {summary.successful_tasks} ({summary.successful_tasks/summary.total_tasks*100:.1f}%)")
    print(f"Failed: {summary.failed_tasks} ({summary.failed_tasks/summary.total_tasks*100:.1f}%)")
    print(f"Avg Duration: {summary.avg_duration_ms}ms")
    print(f"Median Duration: {summary.median_duration_ms}ms")
    print(f"P95 Duration: {summary.p95_duration_ms}ms")
    print(f"P99 Duration: {summary.p99_duration_ms}ms")
    print(f"Tasks/Hour: {summary.tasks_per_hour:.1f}")
    
    print(f"\nMost Common Task Types:")
    for task_type, count in summary.most_common_task_types:
        print(f"  - {task_type}: {count} ({count/summary.total_tasks*100:.1f}%)")
    
    # Detect anomalies
    print("\n" + "="*70)
    print("ANOMALY DETECTION")
    print("="*70)
    
    anomalies = analytics.detect_anomalies()
    print(f"Found {len(anomalies)} anomalies")
    for anomaly in anomalies[:5]:
        print(f"  🚨 {anomaly['severity'].upper()}: {anomaly['description']}")
    
    # Cost estimation
    print("\n" + "="*70)
    print("COST ESTIMATION")
    print("="*70)
    
    costs = analytics.get_cost_estimation()
    print(f"Monthly Tasks (Projected): {costs['monthly_projection']:,}")
    print(f"Monthly Cost: ${costs['monthly_cost_usd']:.2f}")
    print(f"Cost per Task: ${costs['cost_per_task_usd']:.6f}")
    print(f"Wasted on Failures: ${costs['failed_task_cost_usd']:.2f}")
    
    print(f"\nRecommendations:")
    for rec in costs['recommendations']:
        print(f"  💡 {rec}")
    
    # Export reports
    print("\n" + "="*70)
    print("EXPORTING REPORTS")
    print("="*70)
    
    analytics.export_to_json("analytics_report.json")
    analytics.export_to_csv("analytics_data.csv")
    analytics.generate_html_report("analytics_report.html")
    
    print("\n✅ Analytics demo complete!")
    print("📄 Check the generated files:")
    print("   - analytics_report.json")
    print("   - analytics_data.csv")
    print("   - analytics_report.html")


if __name__ == "__main__":
    asyncio.run(main())
