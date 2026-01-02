#!/usr/bin/env python3
"""
Unified Automation Platform

Combines DNS nameserver monitoring with token automation into a single,
comprehensive automation system. Features include:

- Integrated DNS health monitoring
- Token operations automation
- Unified Telegram reporting
- Scheduled execution coordination
- Cross-system alert correlation
- Comprehensive status dashboard
"""

import asyncio
import json
import logging
import os
import subprocess
import sys
import threading
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
from dotenv import load_dotenv

# Import our existing automation modules
try:
    from dns_monitoring_dashboard import DNSHealth, DNSMonitoringDashboard
    from token_automation import AutoGoTokenAutomation
except ImportError as e:
    logger.warning(f"Could not import automation modules: {e}")

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("unified_automation.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


@dataclass
class AutomationResult:
    """Result from any automation operation."""

    component: str
    timestamp: datetime
    success: bool
    data: Dict[str, Any]
    errors: List[str]
    execution_time: float


class UnifiedAutomationPlatform:
    """Main unified automation platform."""

    def __init__(self):
        """Initialize the unified automation platform."""
        self.telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.automation_mode = os.getenv("AUTOMATION_MODE", "full")

        # Initialize component systems
        self.token_automation = None
        self.dns_monitoring = None

        try:
            self.token_automation = AutoGoTokenAutomation()
            logger.info("Token automation system initialized")
        except Exception as e:
            logger.error(f"Failed to initialize token automation: {e}")

        try:
            self.dns_monitoring = DNSMonitoringDashboard()
            logger.info("DNS monitoring system initialized")
        except Exception as e:
            logger.error(f"Failed to initialize DNS monitoring: {e}")

        # Results tracking
        self.results_history = []
        self.last_execution = {}

    def execute_token_automation(self) -> AutomationResult:
        """
        Execute token automation operations.

        Returns:
            AutomationResult: Results from token operations
        """
        start_time = time.time()

        result = AutomationResult(
            component="token_automation",
            timestamp=datetime.now(),
            success=False,
            data={},
            errors=[],
            execution_time=0.0,
        )

        try:
            if not self.token_automation:
                result.errors.append("Token automation not initialized")
                return result

            logger.info("Executing token automation...")

            # Perform token operations
            token_results = self.token_automation.perform_token_operations()

            result.data = token_results
            result.success = len(token_results.get("errors", [])) == 0

            if result.success:
                logger.info("Token automation completed successfully")
            else:
                result.errors.extend(token_results.get("errors", []))
                logger.warning("Token automation completed with errors")

        except Exception as e:
            error_msg = f"Token automation failed: {str(e)}"
            logger.error(error_msg)
            result.errors.append(error_msg)

        finally:
            result.execution_time = time.time() - start_time

        return result

    def execute_dns_monitoring(self) -> AutomationResult:
        """
        Execute DNS monitoring operations.

        Returns:
            AutomationResult: Results from DNS monitoring
        """
        start_time = time.time()

        result = AutomationResult(
            component="dns_monitoring",
            timestamp=datetime.now(),
            success=False,
            data={},
            errors=[],
            execution_time=0.0,
        )

        try:
            if not self.dns_monitoring:
                result.errors.append("DNS monitoring not initialized")
                return result

            logger.info("Executing DNS health monitoring...")

            # Check all domains
            domain_results = {}
            total_healthy = 0

            for domain in self.dns_monitoring.domains:
                health = self.dns_monitoring.check_dns_health(domain)
                domain_results[domain] = asdict(health)

                if health.is_healthy:
                    total_healthy += 1
                else:
                    result.errors.extend(health.issues)

                # Save health check
                self.dns_monitoring.save_health_check(health)

            result.data = {
                "domains": domain_results,
                "summary": {
                    "total_domains": len(self.dns_monitoring.domains),
                    "healthy_domains": total_healthy,
                    "health_rate": (total_healthy / len(self.dns_monitoring.domains))
                    * 100,
                },
            }

            result.success = len(result.errors) == 0

            if result.success:
                logger.info("DNS monitoring completed successfully")
            else:
                logger.warning(
                    f"DNS monitoring found {len(result.errors)} issues")

        except Exception as e:
            error_msg = f"DNS monitoring failed: {str(e)}"
            logger.error(error_msg)
            result.errors.append(error_msg)

        finally:
            result.execution_time = time.time() - start_time

        return result

    def execute_system_health_check(self) -> AutomationResult:
        """
        Execute overall system health check.

        Returns:
            AutomationResult: System health status
        """
        start_time = time.time()

        result = AutomationResult(
            component="system_health",
            timestamp=datetime.now(),
            success=True,
            data={},
            errors=[],
            execution_time=0.0,
        )

        try:
            logger.info("Executing system health check...")

            health_data = {
                "python_version": sys.version,
                "working_directory": os.getcwd(),
                "environment_variables": {
                    "TELEGRAM_BOT_TOKEN": (
                        "configured" if self.telegram_token else "missing"),
                    "TELEGRAM_CHAT_ID": (
                        "configured" if self.telegram_chat_id else "missing"),
                    "CLOUDFLARE_API_TOKEN": (
                        "configured" if os.getenv("CLOUDFLARE_API_TOKEN") else "missing"),
                },
                "disk_space": self.get_disk_usage(),
                "network_connectivity": self.check_network_connectivity(),
                "dependencies": self.check_dependencies(),
            }

            result.data = health_data

            # Check for critical issues
            if not self.telegram_token:
                result.errors.append("Telegram bot token not configured")

            if health_data["network_connectivity"]["status"] != "ok":
                result.errors.append("Network connectivity issues detected")

            result.success = len(result.errors) == 0

            logger.info("System health check completed")

        except Exception as e:
            error_msg = f"System health check failed: {str(e)}"
            logger.error(error_msg)
            result.errors.append(error_msg)

        finally:
            result.execution_time = time.time() - start_time

        return result

    def get_disk_usage(self) -> Dict[str, Any]:
        """Get current disk usage information."""
        try:
            import shutil

            total, used, free = shutil.disk_usage(os.getcwd())

            return {
                "total_gb": round(total / (1024**3), 2),
                "used_gb": round(used / (1024**3), 2),
                "free_gb": round(free / (1024**3), 2),
                "usage_percent": round((used / total) * 100, 1),
            }
        except Exception as e:
            return {"error": str(e)}

    def check_network_connectivity(self) -> Dict[str, Any]:
        """Check network connectivity to key services."""
        connectivity = {"status": "ok", "services": {}}

        test_urls = {
            "telegram": "https://api.telegram.org",
            "cloudflare": "https://api.cloudflare.com/client/v4",
            "google_dns": "https://8.8.8.8",
            "internet": "https://httpbin.org/ip",
        }

        for service, url in test_urls.items():
            try:
                response = requests.get(url, timeout=5)
                connectivity["services"][service] = {
                    "status": "ok",
                    "response_time": response.elapsed.total_seconds(),
                }
            except Exception as e:
                connectivity["services"][service] = {
                    "status": "error", "error": str(e)}
                connectivity["status"] = "degraded"

        return connectivity

    def check_dependencies(self) -> Dict[str, Any]:
        """Check status of required dependencies."""
        dependencies = {}

        required_packages = ["requests", "python-dotenv"]

        for package in required_packages:
            try:
                __import__(package.replace("-", "_"))
                dependencies[package] = {"status": "installed"}
            except ImportError:
                dependencies[package] = {"status": "missing"}

        # Check system tools
        system_tools = ["dig", "nslookup", "whois"]

        for tool in system_tools:
            try:
                subprocess.run([tool, "--version"],
                               capture_output=True, timeout=5)
                dependencies[tool] = {"status": "available"}
            except (subprocess.SubprocessError, FileNotFoundError):
                dependencies[tool] = {"status": "missing"}

        return dependencies

    def send_unified_report(self, results: List[AutomationResult]):
        """
        Send a comprehensive unified report via Telegram.

        Args:
            results (List[AutomationResult]): All automation results
        """
        if not self.telegram_token or not self.telegram_chat_id:
            logger.warning(
                "Telegram credentials not configured, skipping report")
            return

        try:
            # Generate comprehensive report
            report = self.generate_unified_report(results)

            # Send via Telegram
            url = f"https://api.telegram.org/bot{
                self.telegram_token}/sendMessage"
            payload = {
                "chat_id": self.telegram_chat_id,
                "text": report,
                "parse_mode": "HTML",
            }

            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()

            logger.info("Unified automation report sent successfully")

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send unified report: {e}")

    def generate_unified_report(self, results: List[AutomationResult]) -> str:
        """
        Generate a comprehensive unified report.

        Args:
            results (List[AutomationResult]): All automation results

        Returns:
            str: Formatted report message
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report = f"""
🤖 <b>UNIFIED AUTOMATION REPORT</b>
📅 <b>Timestamp:</b> {timestamp}

"""

        # Summary
        successful = sum(1 for r in results if r.success)
        total = len(results)

        report += f"""📊 <b>EXECUTION SUMMARY:</b>
✅ Successful: {successful}/{total}
⚡ Total Execution Time: {sum(r.execution_time for r in results):.2f}s

"""

        # Component results
        for result in results:
            status_emoji = "✅" if result.success else "❌"
            component_name = result.component.replace("_", " ").title()

            report += f"""{status_emoji} <b>{component_name}</b>
⏱️ Execution Time: {result.execution_time:.2f}s
"""

            if result.component == "token_automation" and result.data:
                operations = result.data.get("operations_completed", 0)
                report += f"🔄 Operations: {operations} completed\n"

            elif result.component == "dns_monitoring" and result.data:
                summary = result.data.get("summary", {})
                health_rate = summary.get("health_rate", 0)
                report += f"🌐 DNS Health: {
                    health_rate:.1f}% ({
                    summary.get(
                        'healthy_domains',
                        0)}/{
                    summary.get(
                        'total_domains',
                        0)})\n"

            elif result.component == "system_health" and result.data:
                network = result.data.get("network_connectivity", {})
                report += f"🌍 Network: {
                    network.get(
                        'status',
                        'unknown').upper()}\n"

            if result.errors:
                report += f"⚠️ Issues: {len(result.errors)} found\n"
                for error in result.errors[:3]:  # Limit to first 3 errors
                    report += f"  • {error}\n"
                if len(result.errors) > 3:
                    report += f"  • ... and {len(result.errors) - 3} more\n"

            report += "\n"

        # Overall status
        if successful == total:
            report += "🎉 <b>Status:</b> All systems operational!"
        else:
            report += f"⚠️ <b>Status:</b> {total -
                                           successful} system(s) need attention"

        return report.strip()

    def save_results(self, results: List[AutomationResult]):
        """Save automation results to file."""
        results_data = {
            "timestamp": datetime.now().isoformat(),
            "results": [asdict(result) for result in results],
        }

        # Convert datetime objects to strings for JSON serialization
        for result in results_data["results"]:
            if isinstance(result["timestamp"], datetime):
                result["timestamp"] = result["timestamp"].isoformat()

        # Save to JSON file
        with open("unified_automation_results.json", "w") as f:
            json.dump(results_data, f, indent=2, default=str)

        # Save human-readable report
        report = self.generate_unified_report(results)
        with open("unified_automation_report.txt", "w") as f:
            # Strip HTML tags for text file
            import re

            text_report = re.sub(r"<[^>]+>", "", report)
            f.write(text_report)

        logger.info(
            "Automation results saved to unified_automation_results.json and unified_automation_report.txt"
        )

    def run_full_automation_cycle(self) -> List[AutomationResult]:
        """
        Execute a complete automation cycle.

        Returns:
            List[AutomationResult]: Results from all components
        """
        logger.info("Starting unified automation cycle...")

        results = []

        # Execute system health check
        system_result = self.execute_system_health_check()
        results.append(system_result)

        # Execute DNS monitoring
        dns_result = self.execute_dns_monitoring()
        results.append(dns_result)

        # Execute token automation
        token_result = self.execute_token_automation()
        results.append(token_result)

        # Store results
        self.results_history.append(
            {"timestamp": datetime.now(), "results": results})

        # Keep only last 100 results
        if len(self.results_history) > 100:
            self.results_history = self.results_history[-100:]

        return results

    def run(self):
        """Execute the unified automation platform."""
        try:
            logger.info(
                f"Starting unified automation platform (mode: {
                    self.automation_mode})"
            )

            # Execute full automation cycle
            results = self.run_full_automation_cycle()

            # Generate and send reports
            self.send_unified_report(results)
            self.save_results(results)

            # Display summary
            successful = sum(1 for r in results if r.success)
            total = len(results)

            print(f"\n🎯 AUTOMATION COMPLETE!")
            print(f"   ✅ Successful: {successful}/{total}")
            print(
                f"   ⏱️  Total Time: {sum(r.execution_time for r in results):.2f}s")

            if successful == total:
                print(f"   🎉 All systems operational!")
            else:
                print(f"   ⚠️  {total - successful} system(s) need attention")

            logger.info("Unified automation cycle completed")

        except Exception as e:
            logger.error(f"Error in unified automation: {e}")
            raise


def main():
    """Main entry point for unified automation platform."""
    try:
        platform = UnifiedAutomationPlatform()
        platform.run()

    except KeyboardInterrupt:
        logger.info("Unified automation interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
