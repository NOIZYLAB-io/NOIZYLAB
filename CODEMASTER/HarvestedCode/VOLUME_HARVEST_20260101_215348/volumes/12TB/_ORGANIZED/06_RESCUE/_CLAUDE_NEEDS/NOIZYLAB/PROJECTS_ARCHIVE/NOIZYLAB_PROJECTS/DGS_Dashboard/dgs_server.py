#!/usr/bin/env python3
"""
DGS Server - Simple Local Dashboard Database Service
A lightweight Flask-based service for tracking events and activities
across all NoizyLab automation systems.
"""

import json
import logging
import os
import sqlite3
from datetime import datetime, timedelta
from typing import Any, Dict, List

from flask import Flask, jsonify, render_template_string, request

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PATH = "dgs.db"
app = Flask(__name__)


def init_db():
    """Initialize the DGS database with all required tables."""
    if not os.path.exists(DB_PATH):
        logger.info("Creating new DGS database...")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Events table for general activity tracking
    c.execute(
        """CREATE TABLE IF NOT EXISTS events(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    agent TEXT NOT NULL,
                    action TEXT NOT NULL,
                    payload TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    severity TEXT DEFAULT 'info',
                    category TEXT DEFAULT 'general'
                )"""
    )

    # System metrics table for performance tracking
    c.execute(
        """CREATE TABLE IF NOT EXISTS system_metrics(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    metric_name TEXT NOT NULL,
                    metric_value REAL NOT NULL,
                    unit TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
    )

    # DNS health table for domain monitoring
    c.execute(
        """CREATE TABLE IF NOT EXISTS dns_health(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    domain TEXT NOT NULL,
                    status TEXT NOT NULL,
                    response_time REAL,
                    nameservers TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
    )

    # Progress tracking table for task management
    c.execute(
        """CREATE TABLE IF NOT EXISTS progress_tracking(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    completion_percentage INTEGER DEFAULT 0,
                    status TEXT DEFAULT 'pending',
                    details TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
    )

    conn.commit()
    conn.close()
    logger.info("DGS database initialized successfully")


@app.route("/")
def dashboard():
    """Serve the main dashboard interface."""
    dashboard_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 DGS Dashboard - NoizyLab Control Center</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            min-height: 100vh;
        }
        .header {
            background: rgba(0,0,0,0.3);
            padding: 1rem;
            text-align: center;
            border-bottom: 2px solid rgba(255,255,255,0.1);
        }
        .header h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
        .header p { opacity: 0.8; font-size: 1.1rem; }
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }
        .widget {
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 1.5rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            transition: transform 0.3s ease;
        }
        .widget:hover { transform: translateY(-5px); }
        .widget h3 {
            font-size: 1.4rem;
            margin-bottom: 1rem;
            color: #ffd700;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .status-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin-top: 1rem;
        }
        .status-item {
            background: rgba(0,0,0,0.2);
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
        }
        .status-value {
            font-size: 1.8rem;
            font-weight: bold;
            color: #00ff88;
        }
        .activity-list {
            max-height: 300px;
            overflow-y: auto;
            background: rgba(0,0,0,0.2);
            border-radius: 8px;
            padding: 1rem;
        }
        .activity-item {
            padding: 0.8rem;
            margin: 0.5rem 0;
            background: rgba(255,255,255,0.05);
            border-radius: 6px;
            border-left: 4px solid #00ff88;
        }
        .activity-time { color: #ccc; font-size: 0.9rem; }
        .refresh-btn {
            background: linear-gradient(45deg, #00ff88, #00cc70);
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 25px;
            color: white;
            font-weight: bold;
            cursor: pointer;
            margin: 1rem 0;
            transition: all 0.3s ease;
        }
        .refresh-btn:hover { transform: scale(1.05); }
        .metric-bar {
            background: rgba(0,0,0,0.3);
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 0.5rem;
        }
        .metric-fill {
            background: linear-gradient(90deg, #00ff88, #00cc70);
            height: 100%;
            transition: width 0.3s ease;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 DGS Dashboard</h1>
        <p>NoizyLab Unified Automation Control Center</p>
    </div>

    <div class="dashboard-grid">
        <div class="widget">
            <h3>📊 System Status</h3>
            <div class="status-grid">
                <div class="status-item">
                    <div class="status-value" id="total-events">0</div>
                    <div>Total Events</div>
                </div>
                <div class="status-item">
                    <div class="status-value" id="active-agents">0</div>
                    <div>Active Agents</div>
                </div>
                <div class="status-item">
                    <div class="status-value" id="dns-health">0%</div>
                    <div>DNS Health</div>
                </div>
                <div class="status-item">
                    <div class="status-value" id="system-load">0%</div>
                    <div>System Load</div>
                </div>
            </div>
        </div>

        <div class="widget">
            <h3>🔄 Recent Activity</h3>
            <button class="refresh-btn" onclick="loadData()">🔄 Refresh Data</button>
            <div class="activity-list" id="activity-list">
                <div class="activity-item">
                    <div><strong>System Starting...</strong></div>
                    <div class="activity-time">Loading data...</div>
                </div>
            </div>
        </div>

        <div class="widget">
            <h3>🌐 DNS Monitoring</h3>
            <div id="dns-status">
                <div class="status-item">
                    <div>Loading DNS data...</div>
                </div>
            </div>
        </div>

        <div class="widget">
            <h3>📈 Progress Tracking</h3>
            <div id="progress-tracking">
                <div class="activity-item">
                    <div>System Initialization</div>
                    <div class="metric-bar">
                        <div class="metric-fill" style="width: 100%"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        async function loadData() {
            try {
                // Load recent events
                const events = await fetch('/api/events').then(r => r.json());
                const activityList = document.getElementById('activity-list');
                activityList.innerHTML = events.slice(0, 10).map(event => `
                    <div class="activity-item">
                        <div><strong>${event.agent}</strong>: ${event.action}</div>
                        <div class="activity-time">${new Date(event.time).toLocaleString()}</div>
                        ${event.payload ? `<div style="font-size: 0.9rem; margin-top: 0.3rem;">${event.payload}</div>` : ''}
                    </div>
                `).join('');

                // Update counters
                document.getElementById('total-events').textContent = events.length;
                const uniqueAgents = [...new Set(events.map(e => e.agent))];
                document.getElementById('active-agents').textContent = uniqueAgents.length;

                // Load DNS health
                const dnsHealth = await fetch('/api/dns/health').then(r => r.json());
                document.getElementById('dns-health').textContent = `${dnsHealth.health_percentage}%`;

                // Load system metrics
                const metrics = await fetch('/api/metrics').then(r => r.json());
                const cpuMetric = metrics.find(m => m.metric_name === 'cpu_usage');
                document.getElementById('system-load').textContent =
                    cpuMetric ? `${cpuMetric.metric_value}%` : '0%';

            } catch (error) {
                console.error('Error loading data:', error);
            }
        }

        // Load data on page load and refresh every 30 seconds
        loadData();
        setInterval(loadData, 30000);
    </script>
</body>
</html>
    """
    return render_template_string(dashboard_html)


@app.route("/api/events", methods=["POST"])
def add_event():
    """Add a new event to the database."""
    try:
        data = request.json
        if not data or "agent" not in data or "action" not in data:
            return jsonify(
                {"error": "Missing required fields: agent, action"}), 400

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            """INSERT INTO events(agent, action, payload, severity, category)
                     VALUES(?, ?, ?, ?, ?)""",
            (
                data["agent"],
                data["action"],
                data.get("payload", ""),
                data.get("severity", "info"),
                data.get("category", "general"),
            ),
        )
        conn.commit()
        conn.close()

        logger.info(f"Event added: {data['agent']} - {data['action']}")
        return jsonify(
            {"status": "ok", "message": "Event added successfully"}), 201

    except Exception as e:
        logger.error(f"Error adding event: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/events", methods=["GET"])
def get_events():
    """Get recent events from the database."""
    try:
        limit = request.args.get("limit", 50, type=int)
        agent_filter = request.args.get("agent")

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        query = "SELECT * FROM events"
        params = []

        if agent_filter:
            query += " WHERE agent = ?"
            params.append(agent_filter)

        query += " ORDER BY id DESC LIMIT ?"
        params.append(limit)

        c.execute(query, params)
        rows = [
            dict(
                id=r[0],
                agent=r[1],
                action=r[2],
                payload=r[3],
                time=r[4],
                severity=r[5],
                category=r[6],
            )
            for r in c.fetchall()
        ]
        conn.close()

        return jsonify(rows)

    except Exception as e:
        logger.error(f"Error getting events: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/metrics", methods=["POST"])
def add_metric():
    """Add a system metric."""
    try:
        data = request.json
        if not data or "metric_name" not in data or "metric_value" not in data:
            return (
                jsonify(
                    {"error": "Missing required fields: metric_name, metric_value"}
                ),
                400,
            )

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            """INSERT INTO system_metrics(metric_name, metric_value, unit)
                     VALUES(?, ?, ?)""",
            (data["metric_name"], data["metric_value"], data.get("unit", "")),
        )
        conn.commit()
        conn.close()

        return jsonify({"status": "ok"}), 201

    except Exception as e:
        logger.error(f"Error adding metric: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/metrics", methods=["GET"])
def get_metrics():
    """Get recent system metrics."""
    try:
        hours = request.args.get("hours", 24, type=int)

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            """SELECT metric_name, AVG(metric_value) as avg_value,
                            MAX(metric_value) as max_value, unit,
                            COUNT(*) as sample_count
                     FROM system_metrics
                     WHERE timestamp > datetime('now', '-{} hours')
                     GROUP BY metric_name
                     ORDER BY metric_name""".format(
                hours
            )
        )

        rows = [
            dict(
                metric_name=r[0],
                avg_value=r[1],
                max_value=r[2],
                unit=r[3],
                sample_count=r[4],
            )
            for r in c.fetchall()
        ]
        conn.close()

        return jsonify(rows)

    except Exception as e:
        logger.error(f"Error getting metrics: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/dns/health", methods=["GET"])
def get_dns_health():
    """Get DNS health summary."""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Get recent DNS health data
        c.execute(
            """SELECT domain, status, response_time, nameservers
                     FROM dns_health
                     WHERE timestamp > datetime('now', '-1 hour')
                     ORDER BY timestamp DESC"""
        )

        recent_checks = c.fetchall()
        total_domains = len(set(row[0] for row in recent_checks))
        healthy_domains = len(
            [
                row
                for row in recent_checks
                if "healthy" in row[1].lower() or "ok" in row[1].lower()
            ]
        )

        health_percentage = (
            int((healthy_domains / total_domains * 100)) if total_domains > 0 else 0
        )

        conn.close()

        return jsonify(
            {
                "health_percentage": health_percentage,
                "total_domains": total_domains,
                "healthy_domains": healthy_domains,
                "recent_checks": len(recent_checks),
            }
        )

    except Exception as e:
        logger.error(f"Error getting DNS health: {str(e)}")
        return jsonify({"error": str(e), "health_percentage": 0}), 500


@app.route("/api/progress", methods=["POST"])
def add_progress():
    """Add progress tracking entry."""
    try:
        data = request.json
        if not data or "task_name" not in data:
            return jsonify({"error": "Missing required field: task_name"}), 400

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            """INSERT INTO progress_tracking(task_name, completion_percentage, status, details)
                     VALUES(?, ?, ?, ?)""", (data["task_name"], data.get(
                "completion_percentage", 0), data.get(
                "status", "pending"), data.get(
                "details", ""), ), )
        conn.commit()
        conn.close()

        return jsonify({"status": "ok"}), 201

    except Exception as e:
        logger.error(f"Error adding progress: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/progress", methods=["GET"])
def get_progress():
    """Get progress tracking data."""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            """SELECT task_name, MAX(completion_percentage) as completion,
                            status, details, timestamp
                     FROM progress_tracking
                     GROUP BY task_name
                     ORDER BY timestamp DESC
                     LIMIT 20"""
        )

        rows = [
            dict(
                task_name=r[0],
                completion_percentage=r[1],
                status=r[2],
                details=r[3],
                timestamp=r[4],
            )
            for r in c.fetchall()
        ]
        conn.close()

        return jsonify(rows)

    except Exception as e:
        logger.error(f"Error getting progress: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Get dashboard statistics."""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Event stats
        c.execute(
            "SELECT COUNT(*) FROM events WHERE timestamp > datetime('now', '-24 hours')"
        )
        events_24h = c.fetchone()[0]

        c.execute(
            "SELECT COUNT(DISTINCT agent) FROM events WHERE timestamp > datetime('now', '-1 hour')"
        )
        active_agents = c.fetchone()[0]

        # System uptime (approximate based on first event)
        c.execute("SELECT MIN(timestamp) FROM events")
        first_event = c.fetchone()[0]

        conn.close()

        stats = {
            "events_24h": events_24h,
            "active_agents": active_agents,
            "system_start": first_event,
            "current_time": datetime.now().isoformat(),
        }

        return jsonify(stats)

    except Exception as e:
        logger.error(f"Error getting stats: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    init_db()

    # Add some sample data for demonstration
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Check if we have any events, if not add samples
    c.execute("SELECT COUNT(*) FROM events")
    if c.fetchone()[0] == 0:
        logger.info("Adding sample data...")
        sample_events = [
            ("dgs_server",
             "System Initialization",
             "DGS server starting up",
             "info",
             "system",
             ),
            ("dns_monitor",
             "Health Check",
             "All domains checked",
             "info",
             "dns"),
            ("token_automation",
             "Operation Complete",
             "3 operations completed successfully",
             "success",
             "automation",
             ),
            ("unified_platform",
             "Monitoring Active",
             "Real-time monitoring enabled",
             "info",
             "monitoring",
             ),
        ]

        for event in sample_events:
            c.execute(
                "INSERT INTO events(agent, action, payload, severity, category) VALUES(?, ?, ?, ?, ?)",
                event,
            )

        # Add sample metrics
        sample_metrics = [
            ("cpu_usage", 45.2, "%"),
            ("memory_usage", 68.1, "%"),
            ("disk_usage", 78.5, "%"),
            ("network_latency", 12.3, "ms"),
        ]

        for metric in sample_metrics:
            c.execute(
                "INSERT INTO system_metrics(metric_name, metric_value, unit) VALUES(?, ?, ?)",
                metric,
            )

        conn.commit()
        logger.info("Sample data added successfully")

    conn.close()

    logger.info("🚀 DGS Server starting on http://localhost:5150")
    print("\n" + "=" * 50)
    print("🚀 DGS DASHBOARD SERVER READY!")
    print("=" * 50)
    print("📊 Dashboard URL: http://localhost:5150")
    print("🔌 API Endpoint: http://localhost:5150/api/events")
    print("📈 Metrics API: http://localhost:5150/api/metrics")
    print("🌐 DNS API: http://localhost:5150/api/dns/health")
    print("=" * 50)

    app.run(host="0.0.0.0", port=5150, debug=True)
