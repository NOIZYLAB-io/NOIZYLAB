#!/usr/bin/env python3
"""
Ultimate Status Dashboard

Real-time status dashboard that combines all automation systems:
- DNS nameserver health monitoring
- Token automation status
- System health metrics
- Cloudflare integration status
- VS Code integration status
- Comprehensive reporting

This is the master dashboard for all NoizyLab automation systems.
"""

import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


class UltimateStatusDashboard:
    """Master status dashboard for all automation systems."""

    def __init__(self):
        """Initialize the ultimate status dashboard."""
        self.domains = [
            "fishmusicinc.com",
            "mc96.ca",
            "noizyfish.ca",
            "noizylab.ca"]
        self.cloudflare_ns = [
            "renan.ns.cloudflare.com",
            "naomi.ns.cloudflare.com"]

        # Environment check
        self.env_status = self.check_environment()

        # System components
        self.components = {
            "dns_monitoring": "dns_monitoring_dashboard.py",
            "token_automation": "token_automation.py",
            "unified_automation": "unified_automation.py",
            "dns_fixer": "cloudflare_nameserver_fixer.py",
        }

    def check_environment(self) -> Dict[str, Any]:
        """Check environment configuration status."""
        env_vars = {
            "TELEGRAM_BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN"),
            "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID"),
            "CLOUDFLARE_API_TOKEN": os.getenv("CLOUDFLARE_API_TOKEN"),
            "DNS_MONITORING_INTERVAL": os.getenv("DNS_MONITORING_INTERVAL"),
            "AUTOMATION_MODE": os.getenv("AUTOMATION_MODE"),
        }

        status = {"configured": 0, "missing": 0, "details": {}}

        for var, value in env_vars.items():
            if (
                value
                and value != "your_bot_token_here"
                and value != "your_chat_id_here"
            ):
                status["configured"] += 1
                status["details"][var] = "✅ Configured"
            else:
                status["missing"] += 1
                status["details"][var] = "❌ Not configured"

        return status

    def check_dns_status(self) -> Dict[str, Any]:
        """Check current DNS status for all domains."""
        dns_status = {
            "total_domains": len(self.domains),
            "healthy": 0,
            "issues": 0,
            "domains": {},
        }

        for domain in self.domains:
            try:
                # Check nameservers
                cmd = ["dig", "NS", domain, "+short"]
                process = subprocess.run(
                    cmd, capture_output=True, text=True, timeout=5)

                if process.returncode == 0 and process.stdout.strip():
                    nameservers = [
                        ns.strip().rstrip(".")
                        for ns in process.stdout.strip().split("\n")
                        if ns.strip()
                    ]

                    # Check if using Cloudflare
                    using_cloudflare = any(
                        any(
                            cf_ns in ns
                            for cf_ns in [
                                "renan.ns.cloudflare.com",
                                "naomi.ns.cloudflare.com",
                            ]
                        )
                        for ns in nameservers
                    )

                    dns_status["domains"][domain] = {
                        "status": "✅ Healthy" if using_cloudflare else "❌ Wrong NS",
                        "nameservers": nameservers,
                        "healthy": using_cloudflare,
                    }

                    if using_cloudflare:
                        dns_status["healthy"] += 1
                    else:
                        dns_status["issues"] += 1

                else:
                    dns_status["domains"][domain] = {
                        "status": "❌ NXDOMAIN",
                        "nameservers": [],
                        "healthy": False,
                    }
                    dns_status["issues"] += 1

            except Exception as e:
                dns_status["domains"][domain] = {
                    "status": f"❌ Error: {str(e)[:30]}...",
                    "nameservers": [],
                    "healthy": False,
                }
                dns_status["issues"] += 1

        return dns_status

    def check_file_status(self) -> Dict[str, Any]:
        """Check status of automation files and scripts."""
        files_to_check = [
            "token_automation.py",
            "dns_nameserver_fix.py",
            "cloudflare_nameserver_fixer.py",
            "dns_monitoring_dashboard.py",
            "unified_automation.py",
            "verify_dns.sh",
            "cloudflare_fix_checklist.md",
            ".env",
            "requirements.txt",
        ]

        file_status = {
            "total": len(files_to_check),
            "present": 0,
            "missing": 0,
            "details": {},
        }

        for file_path in files_to_check:
            if Path(file_path).exists():
                size = Path(file_path).stat().st_size
                file_status["present"] += 1
                file_status["details"][file_path] = f"✅ Present ({size} bytes)"
            else:
                file_status["missing"] += 1
                file_status["details"][file_path] = "❌ Missing"

        return file_status

    def check_vscode_integration(self) -> Dict[str, Any]:
        """Check VS Code integration status."""
        vscode_files = [".vscode/launch.json", ".vscode/tasks.json"]

        vscode_status = {"configured": True, "details": {}}

        for file_path in vscode_files:
            if Path(file_path).exists():
                vscode_status["details"][file_path] = "✅ Configured"
            else:
                vscode_status["configured"] = False
                vscode_status["details"][file_path] = "❌ Missing"

        return vscode_status

    def check_system_health(self) -> Dict[str, Any]:
        """Check overall system health."""
        health = {
            "python_version": sys.version.split()[0],
            "working_directory": os.getcwd(),
            "virtual_env": (
                "✅ Active"
                if hasattr(sys, "real_prefix")
                or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
                else "❌ Not active"
            ),
        }

        # Check disk space
        try:
            import shutil

            total, used, free = shutil.disk_usage(os.getcwd())
            health["disk_space"] = {
                "free_gb": round(free / (1024**3), 2),
                "usage_percent": round((used / total) * 100, 1),
            }
        except Exception:
            health["disk_space"] = "❌ Error checking"

        return health

    def check_network_connectivity(self) -> Dict[str, Any]:
        """Check network connectivity to key services."""
        test_urls = {
            "Telegram API": "https://api.telegram.org",
            "Cloudflare API": "https://api.cloudflare.com/client/v4",
            "Google DNS": "https://8.8.8.8",
        }

        connectivity = {}

        for service, url in test_urls.items():
            try:
                response = requests.get(url, timeout=5)
                connectivity[service] = (
                    f"✅ OK ({response.elapsed.total_seconds():.2f}s)"
                )
            except Exception as e:
                connectivity[service] = f"❌ Failed: {str(e)[:30]}..."

        return connectivity

    def get_recent_logs(self) -> Dict[str, Any]:
        """Get recent log entries from automation systems."""
        log_files = [
            "token_automation.log",
            "dns_monitoring.log",
            "unified_automation.log",
        ]

        logs = {}

        for log_file in log_files:
            if Path(log_file).exists():
                try:
                    # Get last 5 lines
                    result = subprocess.run(
                        ["tail", "-5", log_file], capture_output=True, text=True
                    )
                    logs[log_file] = (
                        result.stdout.strip().split("\n")
                        if result.stdout.strip()
                        else ["No recent entries"]
                    )
                except Exception:
                    logs[log_file] = ["Error reading log"]
            else:
                logs[log_file] = ["Log file not found"]

        return logs

    def generate_comprehensive_report(self) -> str:
        """Generate the ultimate status report."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Gather all status information
        env_status = self.env_status
        dns_status = self.check_dns_status()
        file_status = self.check_file_status()
        vscode_status = self.check_vscode_integration()
        system_health = self.check_system_health()
        connectivity = self.check_network_connectivity()
        recent_logs = self.get_recent_logs()

        # Generate report
        report = f"""
🎯 NOIZYLAB ULTIMATE STATUS DASHBOARD
{'=' * 60}
Generated: {timestamp}

📊 SYSTEM OVERVIEW:
   Environment: {env_status['configured']}/{env_status['configured'] + env_status['missing']} configured
   DNS Health: {dns_status['healthy']}/{dns_status['total_domains']} domains healthy
   Files: {file_status['present']}/{file_status['total']} files present
   VS Code: {'✅ Configured' if vscode_status['configured'] else '❌ Needs setup'}
   Network: {'✅ Connected' if all('✅' in status for status in connectivity.values()) else '⚠️ Issues detected'}

🌐 DNS STATUS DETAILS:
"""

        for domain, info in dns_status["domains"].items():
            report += f"   {domain}: {info['status']}\n"
            if info["nameservers"]:
                for ns in info["nameservers"]:
                    report += f"      └─ {ns}\n"

        report += f"""
⚙️  ENVIRONMENT CONFIGURATION:
"""
        for var, status in env_status["details"].items():
            report += f"   {var}: {status}\n"

        report += f"""
📁 FILE STATUS:
"""
        for file_path, status in file_status["details"].items():
            report += f"   {file_path}: {status}\n"

        report += f"""
🔧 SYSTEM HEALTH:
   Python: {system_health['python_version']}
   Virtual Env: {system_health['virtual_env']}
   Directory: {Path(system_health['working_directory']).name}
"""

        if isinstance(system_health.get("disk_space"), dict):
            disk = system_health["disk_space"]
            report += f"   Disk Space: {
                disk['free_gb']} GB free ({
                disk['usage_percent']}% used)\n"
        else:
            report += f"   Disk Space: {
                system_health.get(
                    'disk_space', 'Unknown')}\n"

        report += f"""
🌍 NETWORK CONNECTIVITY:
"""
        for service, status in connectivity.items():
            report += f"   {service}: {status}\n"

        report += f"""
📜 RECENT ACTIVITY:
"""
        for log_file, entries in recent_logs.items():
            report += f"   {log_file}:\n"
            for entry in entries[-3:]:  # Last 3 entries
                if entry:
                    report += f"      {entry}\n"

        # Overall health score
        total_checks = 5  # env, dns, files, vscode, network
        healthy_checks = 0

        if env_status["configured"] > env_status["missing"]:
            healthy_checks += 1
        if dns_status["healthy"] > dns_status["issues"]:
            healthy_checks += 1
        if file_status["present"] > file_status["missing"]:
            healthy_checks += 1
        if vscode_status["configured"]:
            healthy_checks += 1
        if all("✅" in status for status in connectivity.values()):
            healthy_checks += 1

        health_score = (healthy_checks / total_checks) * 100

        report += f"""
🏆 OVERALL HEALTH SCORE: {health_score:.1f}%
   ({healthy_checks}/{total_checks} systems healthy)

🎯 QUICK ACTIONS:
   • Run DNS check: ./verify_dns.sh
   • Full automation: python3 unified_automation.py
   • DNS monitoring: python3 dns_monitoring_dashboard.py
   • VS Code: Press F5 to run configurations

📚 DOCUMENTATION:
   • Setup guide: SETUP_GUIDE.md
   • DNS fixes: DNS_FIX_COMPLETE_GUIDE.md
   • Progress tracker: cloudflare_fix_checklist.md

{'🎉 ALL SYSTEMS OPERATIONAL!' if health_score >= 80 else '⚠️ SOME SYSTEMS NEED ATTENTION'}
"""

        return report.strip()

    def save_dashboard_report(self, report: str):
        """Save the dashboard report to file."""
        with open("ultimate_status_dashboard.txt", "w") as f:
            f.write(report)

        # Also save JSON data for programmatic access
        dashboard_data = {
            "timestamp": datetime.now().isoformat(),
            "environment": self.env_status,
            "dns_status": self.check_dns_status(),
            "file_status": self.check_file_status(),
            "vscode_status": self.check_vscode_integration(),
            "system_health": self.check_system_health(),
            "connectivity": self.check_network_connectivity(),
        }

        with open("ultimate_status_dashboard.json", "w") as f:
            json.dump(dashboard_data, f, indent=2, default=str)

        logger.info(
            "Dashboard report saved to ultimate_status_dashboard.txt and ultimate_status_dashboard.json"
        )

    def run(self):
        """Execute the ultimate status dashboard."""
        try:
            logger.info("Generating ultimate status dashboard...")

            # Generate comprehensive report
            report = self.generate_comprehensive_report()

            # Display report
            print(report)

            # Save report
            self.save_dashboard_report(report)

            logger.info("Ultimate status dashboard completed")

        except Exception as e:
            logger.error(f"Error generating status dashboard: {e}")
            raise


def main():
    """Main entry point for ultimate status dashboard."""
    try:
        dashboard = UltimateStatusDashboard()
        dashboard.run()

    except KeyboardInterrupt:
        logger.info("Status dashboard interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
