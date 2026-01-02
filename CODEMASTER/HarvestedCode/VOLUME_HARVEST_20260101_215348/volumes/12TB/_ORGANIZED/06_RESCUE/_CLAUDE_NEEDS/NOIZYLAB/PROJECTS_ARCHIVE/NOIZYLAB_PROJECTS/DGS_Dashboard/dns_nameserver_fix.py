#!/usr/bin/env python3
"""
DNS Nameserver Fix Script for NoizyLab Domains

This script diagnoses and helps fix nameserver issues for domains
managed in Cloudflare. It identifies common problems and provides
solutions for fixing invalid nameserver configurations.

Issues Found:
1. fishmusicinc.com - Using OpenProvider nameservers instead of Cloudflare
2. mc96.ca - Domain not resolving (NXDOMAIN)
3. noizyfish.ca - Domain not resolving (NXDOMAIN)
4. noizylab.ca - Correctly using Cloudflare nameservers
"""

import json
import logging
import os
import subprocess
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("dns_fix.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


class DNSNameserverFixer:
    """Main class for diagnosing and fixing DNS nameserver issues."""

    def __init__(self):
        """Initialize the DNS fixer."""
        self.domains = [
            "fishmusicinc.com",
            "mc96.ca",
            "noizyfish.ca",
            "noizylab.ca"]

        # Cloudflare nameservers (these should be used for all domains)
        self.cloudflare_nameservers = [
            "renan.ns.cloudflare.com",
            "naomi.ns.cloudflare.com",
        ]

        self.results = {}

    def check_domain_nameservers(self, domain: str) -> Dict:
        """
        Check current nameservers for a domain.

        Args:
            domain (str): Domain to check

        Returns:
            Dict: Status and nameserver information
        """
        result = {
            "domain": domain,
            "status": "unknown",
            "current_nameservers": [],
            "issue": None,
            "solution": None,
        }

        try:
            # Use dig to check nameservers
            cmd = ["dig", "NS", domain, "+short"]
            process = subprocess.run(
                cmd, capture_output=True, text=True, timeout=10)

            if process.returncode == 0 and process.stdout.strip():
                nameservers = [
                    ns.strip().rstrip(".")
                    for ns in process.stdout.strip().split("\n")
                    if ns.strip()
                ]
                result["current_nameservers"] = nameservers

                # Check if using Cloudflare nameservers
                cloudflare_ns = [ns.rstrip(".")
                                 for ns in self.cloudflare_nameservers]
                if all(
                    ns in cloudflare_ns or any(cf_ns in ns for cf_ns in cloudflare_ns)
                    for ns in nameservers
                ):
                    result["status"] = "correct"
                    result["issue"] = None
                else:
                    result["status"] = "wrong_nameservers"
                    result["issue"] = (
                        f"Using {nameservers} instead of Cloudflare nameservers")
                    result["solution"] = (
                        f"Update nameservers to: {
                            ', '.join(
                                self.cloudflare_nameservers)}"
                    )
            else:
                # Try nslookup as backup
                cmd = ["nslookup", "-type=NS", domain]
                process = subprocess.run(
                    cmd, capture_output=True, text=True, timeout=10
                )

                if "NXDOMAIN" in process.stdout or "can't find" in process.stdout:
                    result["status"] = "nxdomain"
                    result["issue"] = (
                        "Domain does not exist or is not properly configured"
                    )
                    result["solution"] = (
                        "Check domain registration and add to Cloudflare DNS"
                    )
                else:
                    result["status"] = "no_response"
                    result["issue"] = "No DNS response"
                    result["solution"] = "Check domain configuration"

        except subprocess.TimeoutExpired:
            result["status"] = "timeout"
            result["issue"] = "DNS query timeout"
            result["solution"] = "Check network connectivity"
        except Exception as e:
            result["status"] = "error"
            result["issue"] = f"Error checking domain: {str(e)}"
            result["solution"] = "Investigate DNS configuration"

        return result

    def check_cloudflare_zone_status(self, domain: str) -> Dict:
        """
        Check if domain is properly configured in Cloudflare.
        Note: This would require Cloudflare API credentials for full functionality.
        """
        return {
            "domain": domain,
            "cloudflare_status": "api_credentials_required",
            "note": "Add CLOUDFLARE_API_TOKEN to environment for full zone checking",
        }

    def generate_nameserver_fix_commands(
        self, domain: str, issue_type: str
    ) -> List[str]:
        """
        Generate commands to fix nameserver issues.

        Args:
            domain (str): Domain to fix
            issue_type (str): Type of issue found

        Returns:
            List[str]: List of commands or instructions
        """
        commands = []

        if issue_type == "wrong_nameservers":
            commands.extend(
                [
                    f"# Fix nameservers for {domain}",
                    f"# 1. Log into your domain registrar (where {domain} is registered)",
                    f"# 2. Update nameservers to:",
                    f"#    - {self.cloudflare_nameservers[0]}",
                    f"#    - {self.cloudflare_nameservers[1]}",
                    f"# 3. Wait 24-48 hours for propagation",
                    f"",
                    f"# Verify after update:",
                    f"dig NS {domain} +short",
                    "",
                ]
            )

        elif issue_type == "nxdomain":
            commands.extend(
                [
                    f"# Fix NXDOMAIN for {domain}",
                    f"# 1. Verify domain is registered and not expired",
                    f"# 2. Add domain to Cloudflare:",
                    f"#    - Go to Cloudflare dashboard",
                    f"#    - Click 'Add a Site'",
                    f"#    - Enter {domain}",
                    f"#    - Follow setup wizard",
                    f"# 3. Update nameservers at registrar to Cloudflare NS",
                    f"",
                    f"# Check domain registration:",
                    f"whois {domain}",
                    "",
                ]
            )

        return commands

    def run_diagnosis(self) -> Dict:
        """
        Run complete DNS diagnosis for all domains.

        Returns:
            Dict: Complete diagnosis results
        """
        logger.info("Starting DNS nameserver diagnosis...")

        diagnosis = {
            "timestamp": datetime.now().isoformat(),
            "domains": {},
            "summary": {
                "total_domains": len(self.domains),
                "correct": 0,
                "issues": 0,
                "errors": 0,
            },
        }

        for domain in self.domains:
            logger.info(f"Checking {domain}...")

            # Check nameservers
            ns_result = self.check_domain_nameservers(domain)

            # Check Cloudflare status (placeholder)
            cf_result = self.check_cloudflare_zone_status(domain)

            # Combine results
            domain_result = {**ns_result, **cf_result}

            # Generate fix commands if needed
            if ns_result["status"] in ["wrong_nameservers", "nxdomain"]:
                domain_result["fix_commands"] = self.generate_nameserver_fix_commands(
                    domain, ns_result["status"])
                diagnosis["summary"]["issues"] += 1
            elif ns_result["status"] == "correct":
                diagnosis["summary"]["correct"] += 1
            else:
                diagnosis["summary"]["errors"] += 1

            diagnosis["domains"][domain] = domain_result

        return diagnosis

    def generate_fix_report(self, diagnosis: Dict) -> str:
        """
        Generate a detailed fix report.

        Args:
            diagnosis (Dict): Diagnosis results

        Returns:
            str: Formatted report
        """
        report_lines = []
        report_lines.append("🔧 DNS NAMESERVER FIX REPORT")
        report_lines.append("=" * 50)
        report_lines.append(f"Generated: {diagnosis['timestamp']}")
        report_lines.append("")

        # Summary
        summary = diagnosis["summary"]
        report_lines.append("📊 SUMMARY:")
        report_lines.append(f"  Total Domains: {summary['total_domains']}")
        report_lines.append(f"  ✅ Correct: {summary['correct']}")
        report_lines.append(f"  ❌ Issues: {summary['issues']}")
        report_lines.append(f"  ⚠️  Errors: {summary['errors']}")
        report_lines.append("")

        # Domain details
        report_lines.append("🔍 DOMAIN ANALYSIS:")
        report_lines.append("")

        for domain, result in diagnosis["domains"].items():
            status_emoji = {
                "correct": "✅",
                "wrong_nameservers": "❌",
                "nxdomain": "🚫",
                "timeout": "⏱️",
                "error": "⚠️",
                "no_response": "❓",
            }.get(result["status"], "❓")

            report_lines.append(f"{status_emoji} {domain.upper()}")
            report_lines.append(f"   Status: {result['status']}")

            if result.get("current_nameservers"):
                report_lines.append(
                    f"   Current NS: {
                        ', '.join(
                            result['current_nameservers'])}"
                )

            if result.get("issue"):
                report_lines.append(f"   Issue: {result['issue']}")

            if result.get("solution"):
                report_lines.append(f"   Solution: {result['solution']}")

            report_lines.append("")

        # Fix commands
        report_lines.append("🛠️  FIX COMMANDS:")
        report_lines.append("")

        for domain, result in diagnosis["domains"].items():
            if result.get("fix_commands"):
                report_lines.extend(result["fix_commands"])

        # Cloudflare nameservers reference
        report_lines.append("📋 CLOUDFLARE NAMESERVERS:")
        report_lines.append("All domains should use these nameservers:")
        for ns in self.cloudflare_nameservers:
            report_lines.append(f"  - {ns}")
        report_lines.append("")

        return "\n".join(report_lines)

    def save_results(self, diagnosis: Dict, report: str):
        """Save diagnosis results and report to files."""
        # Save JSON results
        with open("dns_diagnosis.json", "w") as f:
            json.dump(diagnosis, f, indent=2)

        # Save text report
        with open("dns_fix_report.txt", "w") as f:
            f.write(report)

        logger.info(
            "Results saved to dns_diagnosis.json and dns_fix_report.txt")

    def run(self):
        """Execute the complete DNS nameserver fix workflow."""
        try:
            # Run diagnosis
            diagnosis = self.run_diagnosis()

            # Generate report
            report = self.generate_fix_report(diagnosis)

            # Display report
            print("\n" + report)

            # Save results
            self.save_results(diagnosis, report)

            logger.info("DNS nameserver diagnosis completed successfully")

        except Exception as e:
            logger.error(f"Error in DNS diagnosis: {str(e)}")
            raise


def main():
    """Main entry point for the DNS fixer script."""
    try:
        fixer = DNSNameserverFixer()
        fixer.run()

    except KeyboardInterrupt:
        logger.info("DNS diagnosis interrupted by user")
        sys.exit(0)

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
