#!/usr/bin/env python3
"""
NoizyLab Web Dashboard

A real-time web-based dashboard for monitoring DNS health, token automation,
and system status. Built with Flask and includes:

- Real-time DNS status monitoring
- Interactive charts and graphs
- System health metrics
- Alert management interface
- Mobile-responsive design
- RESTful API endpoints
"""

import json
import logging
import os
import sqlite3
import sys
import threading
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS

# Import our automation modules
try:
    from dns_monitoring_dashboard import DNSMonitoringDashboard
    from ultimate_status_dashboard import UltimateStatusDashboard
    from unified_automation import UnifiedAutomationPlatform
except ImportError as e:
    print(f"Warning: Could not import automation modules: {e}")

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask app setup
app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = os.getenv(
    "FLASK_SECRET_KEY", "noizylab-dashboard-secret-key"
)

# Global instances
dns_monitor = None
status_dashboard = None
automation_platform = None


def init_monitoring_systems():
    """Initialize monitoring systems."""
    global dns_monitor, status_dashboard, automation_platform

    try:
        dns_monitor = DNSMonitoringDashboard()
        status_dashboard = UltimateStatusDashboard()
        automation_platform = UnifiedAutomationPlatform()
        logger.info("Monitoring systems initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize monitoring systems: {e}")


class WebDashboardManager:
    """Manages the web dashboard functionality."""

    def __init__(self):
        self.db_path = Path("dns_monitoring.db")
        self.cache = {}
        self.cache_timeout = 60  # 1 minute

    def get_dns_status(self) -> Dict[str, Any]:
        """Get current DNS status for all domains."""
        cache_key = "dns_status"

        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]["data"]

        if not dns_monitor:
            return {"error": "DNS monitor not initialized"}

        try:
            domains = [
                "fishmusicinc.com",
                "mc96.ca",
                "noizyfish.ca",
                "noizylab.ca"]
            status = {
                "timestamp": datetime.now().isoformat(),
                "domains": {},
                "summary": {"healthy": 0, "total": len(domains)},
            }

            for domain in domains:
                health = dns_monitor.check_dns_health(domain)
                status["domains"][domain] = {
                    "status": "healthy" if health.is_healthy else "unhealthy",
                    "nameservers": health.nameservers,
                    "response_time": health.response_time,
                    "issues": health.issues,
                    "cloudflare_status": health.cloudflare_status,
                }

                if health.is_healthy:
                    status["summary"]["healthy"] += 1

            self._cache_data(cache_key, status)
            return status

        except Exception as e:
            logger.error(f"Error getting DNS status: {e}")
            return {"error": str(e)}

    def get_system_health(self) -> Dict[str, Any]:
        """Get comprehensive system health information."""
        cache_key = "system_health"

        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]["data"]

        if not status_dashboard:
            return {"error": "Status dashboard not initialized"}

        try:
            health = {
                "timestamp": datetime.now().isoformat(),
                "environment": status_dashboard.check_environment(),
                "connectivity": status_dashboard.check_network_connectivity(),
                "files": status_dashboard.check_file_status(),
                "vscode": status_dashboard.check_vscode_integration(),
                "system": status_dashboard.check_system_health(),
            }

            # Calculate overall health score
            scores = []

            # Environment score
            env = health["environment"]
            scores.append(
                (env["configured"] / (env["configured"] + env["missing"])) * 100
            )

            # Connectivity score
            conn_healthy = sum(
                1 for status in health["connectivity"].values() if "✅" in status)
            scores.append((conn_healthy / len(health["connectivity"])) * 100)

            # Files score
            files = health["files"]
            scores.append((files["present"] / files["total"]) * 100)

            # VS Code score
            scores.append(100 if health["vscode"]["configured"] else 0)

            health["overall_score"] = sum(scores) / len(scores)

            self._cache_data(cache_key, health)
            return health

        except Exception as e:
            logger.error(f"Error getting system health: {e}")
            return {"error": str(e)}

    def get_historical_data(self, hours: int = 24) -> Dict[str, Any]:
        """Get historical DNS monitoring data."""
        if not self.db_path.exists():
            return {"error": "No historical data available"}

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    """
                    SELECT domain, timestamp, is_healthy, response_time, cloudflare_status
                    FROM dns_health
                    WHERE timestamp > datetime('now', '-{} hours')
                    ORDER BY timestamp DESC
                """.format(
                        hours
                    )
                )

                rows = cursor.fetchall()

            # Process data for charting
            data = {"labels": [], "datasets": {}}

            # Group by domain
            domain_data = {}
            for row in rows:
                domain, timestamp, is_healthy, response_time, status = row
                if domain not in domain_data:
                    domain_data[domain] = {
                        "health": [],
                        "response_times": [],
                        "timestamps": [],
                    }

                domain_data[domain]["timestamps"].append(timestamp)
                domain_data[domain]["health"].append(1 if is_healthy else 0)
                domain_data[domain]["response_times"].append(
                    response_time or 0)

            # Format for frontend
            for domain, values in domain_data.items():
                data["datasets"][domain] = {
                    "health_rate": (
                        sum(values["health"]) / len(values["health"]) * 100
                        if values["health"]
                        else 0
                    ),
                    "avg_response_time": (
                        sum(values["response_times"]) / len(values["response_times"])
                        if values["response_times"]
                        else 0
                    ),
                    "checks": len(values["health"]),
                }

            # Get unique timestamps for labels
            all_timestamps = set()
            for values in domain_data.values():
                all_timestamps.update(values["timestamps"])
            # Last 50 data points
            data["labels"] = sorted(list(all_timestamps))[-50:]

            return data

        except Exception as e:
            logger.error(f"Error getting historical data: {e}")
            return {"error": str(e)}

    def run_automation(
            self, automation_type: str = "unified") -> Dict[str, Any]:
        """Trigger automation run."""
        if not automation_platform:
            return {
                "error": "Automation platform not initialized",
                "success": False}

        try:
            if automation_type == "dns":
                result = automation_platform.execute_dns_monitoring()
            elif automation_type == "token":
                result = automation_platform.execute_token_automation()
            else:
                results = automation_platform.run_full_automation_cycle()
                result = {
                    "success": all(r.success for r in results),
                    "results": len(results),
                    "timestamp": datetime.now().isoformat(),
                }

            return {"success": True, "result": result}

        except Exception as e:
            logger.error(f"Error running automation: {e}")
            return {"error": str(e), "success": False}

    def _is_cache_valid(self, key: str) -> bool:
        """Check if cached data is still valid."""
        if key not in self.cache:
            return False

        cache_age = datetime.now().timestamp() - self.cache[key]["timestamp"]
        return cache_age < self.cache_timeout

    def _cache_data(self, key: str, data: Any):
        """Cache data with timestamp."""
        self.cache[key] = {
            "data": data,
            "timestamp": datetime.now().timestamp()}


# Initialize dashboard manager
dashboard_manager = WebDashboardManager()


# Routes
@app.route("/")
def index():
    """Main dashboard page."""
    return render_template("dashboard.html")


@app.route("/api/dns/status")
def api_dns_status():
    """API endpoint for DNS status."""
    return jsonify(dashboard_manager.get_dns_status())


@app.route("/api/system/health")
def api_system_health():
    """API endpoint for system health."""
    return jsonify(dashboard_manager.get_system_health())


@app.route("/api/historical/<int:hours>")
def api_historical_data(hours):
    """API endpoint for historical data."""
    return jsonify(dashboard_manager.get_historical_data(hours))


@app.route("/api/automation/run", methods=["POST"])
def api_run_automation():
    """API endpoint to trigger automation."""
    data = request.get_json() or {}
    automation_type = data.get("type", "unified")
    return jsonify(dashboard_manager.run_automation(automation_type))


@app.route("/api/status/overview")
def api_status_overview():
    """API endpoint for complete status overview."""
    dns = dashboard_manager.get_dns_status()
    health = dashboard_manager.get_system_health()

    return jsonify(
        {
            "timestamp": datetime.now().isoformat(),
            "dns": dns,
            "system": health,
            "uptime": "Available via system metrics",
            "version": "1.0.0",
        }
    )


# Template creation
def create_dashboard_template():
    """Create the HTML dashboard template."""
    template_dir = Path("templates")
    template_dir.mkdir(exist_ok=True)

    template_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NoizyLab Automation Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255,255,255,0.95);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border-left: 5px solid #28a745;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        .card.warning { border-left-color: #ffc107; }
        .card.error { border-left-color: #dc3545; }
        .card.info { border-left-color: #17a2b8; }
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .status-healthy { background: #28a745; }
        .status-warning { background: #ffc107; }
        .status-error { background: #dc3545; }
        .metric {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 6px;
        }
        .btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.2s ease;
        }
        .btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        .chart-container {
            position: relative;
            height: 300px;
            margin-top: 20px;
        }
        .loading {
            text-align: center;
            color: #666;
            font-style: italic;
        }
        .timestamp {
            color: #6c757d;
            font-size: 0.9em;
            text-align: center;
            margin-top: 30px;
        }
        @media (max-width: 768px) {
            .container { margin: 10px; padding: 20px; }
            .grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 NoizyLab Automation Dashboard</h1>
            <p>Real-time monitoring and control center</p>
        </div>

        <div class="grid">
            <div class="card" id="dns-status-card">
                <h3>🌐 DNS Status</h3>
                <div id="dns-status">
                    <p class="loading">Loading DNS status...</p>
                </div>
            </div>

            <div class="card" id="system-health-card">
                <h3>🏥 System Health</h3>
                <div id="system-health">
                    <p class="loading">Loading system health...</p>
                </div>
            </div>

            <div class="card info">
                <h3>🔄 Automation Controls</h3>
                <button class="btn" onclick="runAutomation('unified')">🚀 Run Full Automation</button>
                <button class="btn" onclick="runAutomation('dns')" style="margin-top: 10px;">🌐 DNS Check Only</button>
                <button class="btn" onclick="runAutomation('token')" style="margin-top: 10px;">💰 Token Operations</button>
            </div>

            <div class="card">
                <h3>📊 Performance Metrics</h3>
                <div class="chart-container">
                    <canvas id="performanceChart"></canvas>
                </div>
            </div>
        </div>

        <div class="card">
            <h3>📈 Historical Overview</h3>
            <div class="chart-container">
                <canvas id="historicalChart"></canvas>
            </div>
        </div>

        <p class="timestamp">Last updated: <span id="last-updated">--</span></p>
    </div>

    <script>
        // Dashboard JavaScript
        let performanceChart, historicalChart;

        async function loadDashboard() {
            try {
                // Load DNS status
                const dnsResponse = await fetch('/api/dns/status');
                const dnsData = await dnsResponse.json();
                updateDNSStatus(dnsData);

                // Load system health
                const healthResponse = await fetch('/api/system/health');
                const healthData = await healthResponse.json();
                updateSystemHealth(healthData);

                // Load historical data
                const histResponse = await fetch('/api/historical/24');
                const histData = await histResponse.json();
                updateCharts(histData);

                document.getElementById('last-updated').textContent = new Date().toLocaleString();
            } catch (error) {
                console.error('Error loading dashboard:', error);
            }
        }

        function updateDNSStatus(data) {
            const container = document.getElementById('dns-status');
            const card = document.getElementById('dns-status-card');

            if (data.error) {
                container.innerHTML = `<p class="error">Error: ${data.error}</p>`;
                card.className = 'card error';
                return;
            }

            let html = '';
            let allHealthy = true;

            for (const [domain, info] of Object.entries(data.domains)) {
                const isHealthy = info.status === 'healthy';
                if (!isHealthy) allHealthy = false;

                const statusClass = isHealthy ? 'status-healthy' : 'status-error';
                html += `
                    <div class="metric">
                        <span><span class="status-indicator ${statusClass}"></span>${domain}</span>
                        <span>${info.status.toUpperCase()}</span>
                    </div>
                `;
            }

            container.innerHTML = html;
            card.className = allHealthy ? 'card' : 'card warning';
        }

        function updateSystemHealth(data) {
            const container = document.getElementById('system-health');
            const card = document.getElementById('system-health-card');

            if (data.error) {
                container.innerHTML = `<p class="error">Error: ${data.error}</p>`;
                card.className = 'card error';
                return;
            }

            const score = data.overall_score || 0;
            const scoreClass = score >= 80 ? 'status-healthy' : score >= 60 ? 'status-warning' : 'status-error';

            let html = `
                <div class="metric">
                    <span><span class="status-indicator ${scoreClass}"></span>Overall Health</span>
                    <span>${score.toFixed(1)}%</span>
                </div>
            `;

            // Add key metrics
            if (data.environment) {
                html += `
                    <div class="metric">
                        <span>Environment Config</span>
                        <span>${data.environment.configured}/${data.environment.configured + data.environment.missing}</span>
                    </div>
                `;
            }

            container.innerHTML = html;
            card.className = score >= 80 ? 'card' : score >= 60 ? 'card warning' : 'card error';
        }

        function updateCharts(data) {
            // Create performance chart
            const perfCtx = document.getElementById('performanceChart').getContext('2d');
            if (performanceChart) performanceChart.destroy();

            performanceChart = new Chart(perfCtx, {
                type: 'doughnut',
                data: {
                    labels: ['Healthy Domains', 'Issues'],
                    datasets: [{
                        data: [3, 1], // Example data
                        backgroundColor: ['#28a745', '#dc3545']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom' }
                    }
                }
            });

            // Create historical chart
            const histCtx = document.getElementById('historicalChart').getContext('2d');
            if (historicalChart) historicalChart.destroy();

            historicalChart = new Chart(histCtx, {
                type: 'line',
                data: {
                    labels: data.labels ? data.labels.slice(-10) : [],
                    datasets: Object.keys(data.datasets || {}).map((domain, index) => ({
                        label: domain,
                        data: Array(10).fill(Math.random() * 100), // Example data
                        borderColor: ['#667eea', '#764ba2', '#28a745', '#ffc107'][index % 4],
                        tension: 0.4,
                        fill: false
                    }))
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom' }
                    },
                    scales: {
                        y: { beginAtZero: true, max: 100 }
                    }
                }
            });
        }

        async function runAutomation(type) {
            try {
                const response = await fetch('/api/automation/run', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ type })
                });

                const result = await response.json();

                if (result.success) {
                    alert(`✅ ${type} automation completed successfully!`);
                    loadDashboard(); // Refresh data
                } else {
                    alert(`❌ Automation failed: ${result.error}`);
                }
            } catch (error) {
                alert(`❌ Error running automation: ${error.message}`);
            }
        }

        // Initialize dashboard
        loadDashboard();

        // Auto-refresh every 5 minutes
        setInterval(loadDashboard, 5 * 60 * 1000);
    </script>
</body>
</html>"""

    with open(template_dir / "dashboard.html", "w") as f:
        f.write(template_content)

    logger.info("Dashboard template created")


def run_web_dashboard(host="0.0.0.0", port=5000, debug=False):
    """Run the web dashboard."""
    try:
        # Initialize monitoring systems
        init_monitoring_systems()

        # Create template
        create_dashboard_template()

        logger.info(f"Starting NoizyLab Web Dashboard on http://{host}:{port}")
        app.run(host=host, port=port, debug=debug, threaded=True)

    except Exception as e:
        logger.error(f"Error running web dashboard: {e}")
        raise


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="NoizyLab Web Dashboard")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="Port to bind to")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode")

    args = parser.parse_args()

    run_web_dashboard(host=args.host, port=args.port, debug=args.debug)
