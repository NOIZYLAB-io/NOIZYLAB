#!/usr/bin/env python3
"""
DNS Monitoring Dashboard

A comprehensive real-time monitoring system for DNS nameservers and domain health.
Features:
- Real-time DNS status monitoring
- Cloudflare integration
- Telegram alerts
- Web dashboard
- Historical tracking
- Automated health checks
"""

import json
import logging
import os
import sqlite3
import subprocess
import sys
import threading
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("dns_monitoring.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


@dataclass
class DNSHealth:
    """DNS health status data structure."""

    domain: str
    timestamp: datetime
    nameservers: List[str]
    cloudflare_status: str
    response_time: float
    is_healthy: bool
    issues: List[str]
    cloudflare_zone_id: Optional[str] = None


class DNSMonitoringDashboard:
    """Main DNS monitoring and dashboard system."""

    def __init__(self):
        """Initialize the DNS monitoring dashboard."""
        self.domains = [
            "fishmusicinc.com",
            "mc96.ca",
            "noizyfish.ca",
            "noizylab.ca"]

        self.cloudflare_ns = [
            "renan.ns.cloudflare.com",
            "naomi.ns.cloudflare.com"]

        # Configuration from environment
        self.telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.cloudflare_token = os.getenv("CLOUDFLARE_API_TOKEN")
        self.monitoring_interval = int(
            os.getenv("DNS_MONITORING_INTERVAL", "300")
        )  # 5 minutes

        # Initialize database
        self.init_database()

        # Monitoring state
        self.monitoring_active = False
        self.last_alerts = {}

    def init_database(self):
        """Initialize SQLite database for historical tracking."""
        self.db_path = Path("dns_monitoring.db")

        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS dns_health (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    domain TEXT NOT NULL,
                    timestamp DATETIME NOT NULL,
                    nameservers TEXT,
                    cloudflare_status TEXT,
                    response_time REAL,
                    is_healthy BOOLEAN,
                    issues TEXT,
                    cloudflare_zone_id TEXT
                )
            """
            )

            conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_domain_timestamp
                ON dns_health(domain, timestamp)
            """
            )

        logger.info("DNS monitoring database initialized")

    def check_dns_health(self, domain: str) -> DNSHealth:
        """
        Perform comprehensive DNS health check for a domain.

        Args:
            domain (str): Domain to check

        Returns:
            DNSHealth: Complete health status
        """
        start_time = time.time()
        issues = []
        nameservers = []
        cloudflare_status = "unknown"

        try:
            # Check nameservers
            cmd = ["dig", "NS", domain, "+short"]
            process = subprocess.run(
                cmd, capture_output=True, text=True, timeout=10)

            if process.returncode == 0 and process.stdout.strip():
                nameservers = [
                    ns.strip().rstrip(".")
                    for ns in process.stdout.strip().split("\n")
                    if ns.strip()
                ]

                # Validate nameservers
                cloudflare_ns_clean = [
                    ns.rstrip(".") for ns in self.cloudflare_ns]
                using_cloudflare = any(
                    any(cf_ns in ns for cf_ns in cloudflare_ns_clean)
                    for ns in nameservers
                )

                if not using_cloudflare:
                    issues.append(
                        f"Not using Cloudflare nameservers: {nameservers}")
                    cloudflare_status = "wrong_nameservers"
                else:
                    cloudflare_status = "correct"

            else:
                # Check if domain exists
                cmd = ["nslookup", "-type=NS", domain]
                process = subprocess.run(
                    cmd, capture_output=True, text=True, timeout=10
                )

                if "NXDOMAIN" in process.stdout or "can't find" in process.stdout:
                    issues.append("Domain does not exist (NXDOMAIN)")
                    cloudflare_status = "nxdomain"
                else:
                    issues.append("No DNS response")
                    cloudflare_status = "no_response"

        except subprocess.TimeoutExpired:
            issues.append("DNS query timeout")
            cloudflare_status = "timeout"
        except Exception as e:
            issues.append(f"DNS check error: {str(e)}")
            cloudflare_status = "error"

        response_time = time.time() - start_time
        is_healthy = cloudflare_status == "correct"

        return DNSHealth(
            domain=domain,
            timestamp=datetime.now(),
            nameservers=nameservers,
            cloudflare_status=cloudflare_status,
            response_time=response_time,
            is_healthy=is_healthy,
            issues=issues,
        )

    def check_cloudflare_zone(self, domain: str) -> Dict:
        """
        Check domain status in Cloudflare via API.

        Args:
            domain (str): Domain to check

        Returns:
            Dict: Cloudflare zone information
        """
        if not self.cloudflare_token:
            return {"status": "no_api_token", "zone_id": None}

        try:
            headers = {
                "Authorization": f"Bearer {self.cloudflare_token}",
                "Content-Type": "application/json",
            }

            # List zones to find domain
            url = "https://api.cloudflare.com/client/v4/zones"
            params = {"name": domain}

            response = requests.get(
                url, headers=headers, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data.get("success") and data.get("result"):
                zone = data["result"][0]
                return {
                    "status": "active" if zone["status"] == "active" else "inactive",
                    "zone_id": zone["id"],
                    "name_servers": zone.get(
                        "name_servers",
                        []),
                    "plan": zone.get(
                        "plan",
                        {}).get(
                        "name",
                        "unknown"),
                }
            else:
                return {"status": "not_found", "zone_id": None}

        except requests.exceptions.RequestException as e:
            logger.error(f"Cloudflare API error for {domain}: {e}")
            return {"status": "api_error", "zone_id": None, "error": str(e)}
        except Exception as e:
            logger.error(
                f"Unexpected error checking Cloudflare for {domain}: {e}")
            return {"status": "error", "zone_id": None, "error": str(e)}

    def save_health_check(self, health: DNSHealth):
        """Save health check result to database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO dns_health
                (domain, timestamp, nameservers, cloudflare_status, response_time,
                 is_healthy, issues, cloudflare_zone_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    health.domain,
                    health.timestamp,
                    json.dumps(health.nameservers),
                    health.cloudflare_status,
                    health.response_time,
                    health.is_healthy,
                    json.dumps(health.issues),
                    health.cloudflare_zone_id,
                ),
            )

    def send_alert(self, domain: str, issues: List[str]):
        """
        Send Telegram alert for DNS issues.

        Args:
            domain (str): Affected domain
            issues (List[str]): List of issues found
        """
        if not self.telegram_token or not self.telegram_chat_id:
            logger.warning(
                "Telegram credentials not configured, skipping alert")
            return

        # Rate limiting - don't spam alerts
        alert_key = f"{domain}:{hash(str(sorted(issues)))}"
        now = datetime.now()

        if alert_key in self.last_alerts:
            if now - self.last_alerts[alert_key] < timedelta(hours=1):
                return  # Skip duplicate alert within 1 hour

        self.last_alerts[alert_key] = now

        message = f"""
🚨 <b>DNS ALERT</b> 🚨

🌐 <b>Domain:</b> {domain}
⏰ <b>Time:</b> {now.strftime('%Y-%m-%d %H:%M:%S')}

❌ <b>Issues Detected:</b>
"""
        for issue in issues:
            message += f"• {issue}\n"

        message += f"""
🔧 <b>Recommended Action:</b>
Check DNS configuration for {domain}

Run: <code>./verify_dns.sh</code>
"""

        try:
            url = f"https://api.telegram.org/bot{
                self.telegram_token}/sendMessage"
            payload = {
                "chat_id": self.telegram_chat_id,
                "text": message.strip(),
                "parse_mode": "HTML",
            }

            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()

            logger.info(f"DNS alert sent for {domain}")

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send DNS alert: {e}")

    def generate_dashboard_report(self) -> str:
        """Generate a comprehensive dashboard report."""
        report_lines = []
        report_lines.append("📊 DNS MONITORING DASHBOARD")
        report_lines.append("=" * 50)
        report_lines.append(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        report_lines.append("")

        total_domains = len(self.domains)
        healthy_count = 0

        # Current status
        report_lines.append("🔍 CURRENT STATUS:")
        report_lines.append("")

        for domain in self.domains:
            health = self.check_dns_health(domain)

            # Get Cloudflare status
            cf_info = self.check_cloudflare_zone(domain)
            health.cloudflare_zone_id = cf_info.get("zone_id")

            # Save to database
            self.save_health_check(health)

            # Status emoji
            status_emoji = "✅" if health.is_healthy else "❌"

            report_lines.append(f"{status_emoji} {domain.upper()}")
            report_lines.append(f"   Status: {health.cloudflare_status}")
            report_lines.append(
                f"   Response Time: {
                    health.response_time:.3f}s"
            )

            if health.nameservers:
                report_lines.append(
                    f"   Nameservers: {
                        ', '.join(
                            health.nameservers)}"
                )

            if cf_info.get("status") != "no_api_token":
                report_lines.append(
                    f"   Cloudflare: {cf_info.get('status', 'unknown')}"
                )

            if health.issues:
                report_lines.append(f"   Issues: {'; '.join(health.issues)}")
                # Send alert for unhealthy domains
                self.send_alert(domain, health.issues)
            else:
                healthy_count += 1

            report_lines.append("")

        # Summary
        report_lines.append("📈 SUMMARY:")
        report_lines.append(f"   Total Domains: {total_domains}")
        report_lines.append(f"   Healthy: {healthy_count}")
        report_lines.append(f"   Issues: {total_domains - healthy_count}")
        report_lines.append(
            f"   Health Rate: {(healthy_count / total_domains) * 100:.1f}%"
        )
        report_lines.append("")

        # Historical trends (last 24 hours)
        report_lines.append("📊 24-HOUR TRENDS:")
        report_lines.append(self.get_historical_summary())

        return "\n".join(report_lines)

    def get_historical_summary(self) -> str:
        """Get historical summary from database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    """
                    SELECT domain, AVG(is_healthy) as health_rate, COUNT(*) as checks
                    FROM dns_health
                    WHERE timestamp > datetime('now', '-24 hours')
                    GROUP BY domain
                    ORDER BY domain
                """
                )

                results = cursor.fetchall()

            if not results:
                return "   No historical data available"

            lines = []
            for domain, health_rate, checks in results:
                lines.append(
                    f"   {domain}: {
                        health_rate *
                        100:.1f}% uptime ({checks} checks)"
                )

            return "\n".join(lines)

        except Exception as e:
            logger.error(f"Error getting historical summary: {e}")
            return f"   Error retrieving historical data: {e}"

    def start_monitoring(self):
        """Start continuous DNS monitoring."""
        self.monitoring_active = True
        logger.info(
            f"Starting DNS monitoring (interval: {
                self.monitoring_interval}s)"
        )

        while self.monitoring_active:
            try:
                report = self.generate_dashboard_report()

                # Save report
                with open("dns_monitoring_report.txt", "w") as f:
                    f.write(report)

                logger.info("DNS monitoring cycle completed")

                # Wait for next cycle
                for _ in range(self.monitoring_interval):
                    if not self.monitoring_active:
                        break
                    time.sleep(1)

            except KeyboardInterrupt:
                logger.info("DNS monitoring stopped by user")
                break
            except Exception as e:
                logger.error(f"Error in monitoring cycle: {e}")
                time.sleep(60)  # Wait 1 minute before retry

        self.monitoring_active = False

    def stop_monitoring(self):
        """Stop continuous monitoring."""
        self.monitoring_active = False
        logger.info("DNS monitoring stopped")

    def run_single_check(self):
        """Run a single monitoring check and display results."""
        logger.info("Running single DNS health check...")

        report = self.generate_dashboard_report()
        print("\n" + report)

        # Save report
        with open("dns_monitoring_report.txt", "w") as f:
            f.write(report)

        logger.info(
            "Single check completed - report saved to dns_monitoring_report.txt"
        )

    def run(self):
        """Execute the DNS monitoring system."""
        try:
            mode = os.getenv("DASHBOARD_MODE", "single")

            if mode == "continuous":
                self.start_monitoring()
            else:
                self.run_single_check()

        except KeyboardInterrupt:
            logger.info("DNS monitoring interrupted by user")
            self.stop_monitoring()
        except Exception as e:
            logger.error(f"Error in DNS monitoring: {e}")
            raise


def main():
    """Main entry point for DNS monitoring dashboard."""
    try:
        dashboard = DNSMonitoringDashboard()

        if len(sys.argv) > 1:
            if sys.argv[1] == "--continuous":
                os.environ["DASHBOARD_MODE"] = "continuous"
            elif sys.argv[1] == "--single":
                os.environ["DASHBOARD_MODE"] = "single"

        dashboard.run()

    except KeyboardInterrupt:
        logger.info("DNS monitoring interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
