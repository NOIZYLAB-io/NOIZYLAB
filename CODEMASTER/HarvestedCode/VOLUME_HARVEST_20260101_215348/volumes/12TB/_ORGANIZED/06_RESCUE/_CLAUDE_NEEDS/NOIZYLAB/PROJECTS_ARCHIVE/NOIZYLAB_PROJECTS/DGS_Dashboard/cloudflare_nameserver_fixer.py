#!/usr/bin/env python3
"""
Automated DNS Nameserver Fix Script

This script provides step-by-step solutions for fixing the nameserver issues
identified in your Cloudflare dashboard.

ISSUES IDENTIFIED:
1. fishmusicinc.com - Wrong nameservers (using OpenProvider)
2. mc96.ca - Domain not registered
3. noizyfish.ca - Domain not registered
4. noizylab.ca - Correct Cloudflare configuration ✅

SOLUTIONS PROVIDED:
- Detailed fix instructions for each domain
- Automated verification commands
- Progress tracking
"""

import json
import logging
import os
import subprocess
import sys
from datetime import datetime
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


class CloudflareNameserverFixer:
    """Automated fixer for Cloudflare nameserver issues."""

    def __init__(self):
        self.cloudflare_ns = [
            "renan.ns.cloudflare.com",
            "naomi.ns.cloudflare.com"]

        self.domain_issues = {
            "fishmusicinc.com": {
                "issue": "wrong_nameservers",
                "current_ns": [
                    "ns1.openprovider.nl",
                    "ns2.openprovider.be",
                    "ns3.openprovider.eu",
                ],
                "action_required": "update_nameservers",
                "registrar": "likely_openprovider_or_reseller",
            },
            "mc96.ca": {
                "issue": "not_registered",
                "action_required": "register_domain",
                "tld": ".ca",
                "registrar_options": ["CIRA approved registrars"],
            },
            "noizyfish.ca": {
                "issue": "not_registered",
                "action_required": "register_domain",
                "tld": ".ca",
                "registrar_options": ["CIRA approved registrars"],
            },
            "noizylab.ca": {
                "issue": "none",
                "status": "correct",
                "current_ns": [
                    "renan.ns.cloudflare.com",
                    "naomi.ns.cloudflare.com"],
            },
        }

    def print_header(self):
        """Print script header."""
        print("🔧 CLOUDFLARE NAMESERVER FIX AUTOMATION")
        print("=" * 50)
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

    def fix_fishmusicinc_com(self):
        """Provide step-by-step fix for fishmusicinc.com."""
        print("🔧 FIXING: fishmusicinc.com")
        print("-" * 30)
        print("ISSUE: Using OpenProvider nameservers instead of Cloudflare")
        print()

        print("STEP-BY-STEP FIX:")
        print("1. Log into your domain registrar account")
        print("   (Likely OpenProvider or a reseller)")
        print()
        print("2. Navigate to DNS/Nameserver settings for fishmusicinc.com")
        print()
        print("3. REPLACE current nameservers:")
        print("   ❌ ns1.openprovider.nl")
        print("   ❌ ns2.openprovider.be")
        print("   ❌ ns3.openprovider.eu")
        print()
        print("4. WITH Cloudflare nameservers:")
        print("   ✅ renan.ns.cloudflare.com")
        print("   ✅ naomi.ns.cloudflare.com")
        print()
        print("5. Save changes and wait 24-48 hours for propagation")
        print()

        # Generate verification command
        print("🔍 VERIFICATION COMMAND:")
        print("dig NS fishmusicinc.com +short")
        print()
        print("Expected result after fix:")
        for ns in self.cloudflare_ns:
            print(f"  {ns}.")
        print()

    def fix_canadian_domains(self):
        """Provide fix for Canadian domains that need registration."""
        domains = ["mc96.ca", "noizyfish.ca"]

        print("🇨🇦 FIXING CANADIAN DOMAINS: mc96.ca & noizyfish.ca")
        print("-" * 50)
        print("ISSUE: Domains are not registered")
        print()

        print("STEP-BY-STEP FIX:")
        print("1. Choose a CIRA-approved registrar:")
        print("   • Namecheap.com")
        print("   • GoDaddy.ca")
        print("   • Hover.com")
        print("   • Register.ca")
        print("   • Tucows.com")
        print()

        for domain in domains:
            print(f"2. Register {domain}:")
            print(f"   • Search for {domain} availability")
            print(f"   • Complete registration process")
            print(f"   • During setup, use these nameservers:")
            for ns in self.cloudflare_ns:
                print(f"     - {ns}")
            print()

        print("3. Add domains to Cloudflare:")
        print("   • Go to Cloudflare dashboard")
        print("   • Click 'Add a Site'")
        print("   • Enter domain name")
        print("   • Follow setup wizard")
        print("   • Confirm nameservers match registration")
        print()

        print("🔍 VERIFICATION COMMANDS:")
        for domain in domains:
            print(f"# Check {domain} registration:")
            print(f"whois {domain}")
            print(f"dig NS {domain} +short")
            print()

    def show_noizylab_status(self):
        """Show status for correctly configured domain."""
        print("✅ CORRECTLY CONFIGURED: noizylab.ca")
        print("-" * 35)
        print("STATUS: Perfect! Using correct Cloudflare nameservers")
        print("CURRENT NAMESERVERS:")
        for ns in self.cloudflare_ns:
            print(f"  ✅ {ns}")
        print()
        print("NO ACTION REQUIRED for this domain.")
        print()

    def generate_automation_script(self):
        """Generate a verification script."""
        script_content = """#!/bin/bash
# DNS Verification Script
# Run this after making nameserver changes

echo "🔍 Verifying DNS nameserver changes..."
echo

domains=("fishmusicinc.com" "mc96.ca" "noizyfish.ca" "noizylab.ca")
cloudflare_ns=("renan.ns.cloudflare.com" "naomi.ns.cloudflare.com")

for domain in "${domains[@]}"; do
    echo "Checking $domain..."
    result=$(dig NS $domain +short 2>/dev/null)

    if [ -z "$result" ]; then
        echo "  ❌ No DNS response (domain may not be registered)"
    else
        echo "  Current nameservers:"
        while IFS= read -r ns; do
            if [[ "$ns" == *"cloudflare.com"* ]]; then
                echo "    ✅ $ns"
            else
                echo "    ❌ $ns"
            fi
        done <<< "$result"
    fi
    echo
done

echo "✅ Verification complete!"
echo "Note: DNS propagation can take 24-48 hours"
"""

        with open("verify_dns.sh", "w") as f:
            f.write(script_content)

        # Make executable
        subprocess.run(["chmod", "+x", "verify_dns.sh"], check=False)

        print("📝 AUTOMATION SCRIPT CREATED: verify_dns.sh")
        print("   Run './verify_dns.sh' to check progress")
        print()

    def create_cloudflare_checklist(self):
        """Create a checklist file for tracking progress."""
        checklist = """# Cloudflare Nameserver Fix Checklist

## ❌ fishmusicinc.com
- [ ] Log into domain registrar
- [ ] Update nameservers to Cloudflare
- [ ] Wait for propagation (24-48 hours)
- [ ] Verify with: dig NS fishmusicinc.com +short

## ❌ mc96.ca
- [ ] Register domain with CIRA-approved registrar
- [ ] Set nameservers to Cloudflare during registration
- [ ] Add domain to Cloudflare dashboard
- [ ] Verify with: dig NS mc96.ca +short

## ❌ noizyfish.ca
- [ ] Register domain with CIRA-approved registrar
- [ ] Set nameservers to Cloudflare during registration
- [ ] Add domain to Cloudflare dashboard
- [ ] Verify with: dig NS noizyfish.ca +short

## ✅ noizylab.ca
- [x] Already correctly configured
- [x] Using proper Cloudflare nameservers

## Cloudflare Nameservers
- renan.ns.cloudflare.com
- naomi.ns.cloudflare.com

## Progress Tracking
Date started: {date}
Expected completion: {date_plus_48h}
""".format(
            date=datetime.now().strftime("%Y-%m-%d"),
            date_plus_48h=(datetime.now()).strftime("%Y-%m-%d (+ 48 hours)"),
        )

        with open("cloudflare_fix_checklist.md", "w") as f:
            f.write(checklist)

        print("📋 CHECKLIST CREATED: cloudflare_fix_checklist.md")
        print("   Track your progress with this file")
        print()

    def run(self):
        """Execute the complete fix workflow."""
        self.print_header()

        print("🎯 SUMMARY OF ISSUES:")
        print("• fishmusicinc.com: Wrong nameservers (OpenProvider → Cloudflare)")
        print("• mc96.ca: Domain not registered")
        print("• noizyfish.ca: Domain not registered")
        print("• noizylab.ca: ✅ Already correct")
        print()

        print("=" * 50)
        print()

        # Fix each domain
        self.fix_fishmusicinc_com()
        print("=" * 50)
        print()

        self.fix_canadian_domains()
        print("=" * 50)
        print()

        self.show_noizylab_status()
        print("=" * 50)
        print()

        # Generate helper files
        self.generate_automation_script()
        self.create_cloudflare_checklist()

        print("🎉 FIX GUIDE COMPLETE!")
        print()
        print("NEXT STEPS:")
        print("1. Follow the domain-specific instructions above")
        print("2. Use 'cloudflare_fix_checklist.md' to track progress")
        print("3. Run './verify_dns.sh' to check your changes")
        print("4. Wait 24-48 hours for full DNS propagation")
        print()
        print("💡 TIP: Start with fishmusicinc.com (easiest fix)")
        print("    then register the Canadian domains")


if __name__ == "__main__":
    fixer = CloudflareNameserverFixer()
    fixer.run()
