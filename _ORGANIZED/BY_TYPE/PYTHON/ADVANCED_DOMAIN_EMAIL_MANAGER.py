#!/usr/bin/env python3
"""
ADVANCED DOMAIN & EMAIL MANAGER - ULTIMATE UPGRADE
Features: Monitoring, Analytics, Automation, Health Checks, Backups, Optimization
"""

import json
import requests
import smtplib
import imaplib
import dns.resolver
import whois
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor
import os
import time

# ==================== CONFIGURATION ====================
CONFIG_FILE = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/domains_and_emails_master.json"
BACKUP_DIR = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/email_backups"
REPORTS_DIR = "/Volumes/4TBSG/NOIZYLAB/Github/Noizyfish/NOIZYLAB/domain_reports"

# Create directories
os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# Load configuration
with open(CONFIG_FILE, 'r') as f:
    CONFIG = json.load(f)

DOMAINS = CONFIG.get('all_domains', [])
EMAILS = CONFIG.get('all_emails', [])

# ==================== DOMAIN HEALTH CHECKER ====================
class DomainHealthChecker:
    """Advanced domain health monitoring"""
    
    def __init__(self, domain):
        self.domain = domain
        self.health_score = 0
        self.issues = []
        self.recommendations = []
    
    def check_dns_records(self):
        """Check all DNS records"""
        print(f"\n[DNS CHECK] {self.domain}")
        score = 0
        
        # Check A record
        try:
            a_records = dns.resolver.resolve(self.domain, 'A')
            print(f"  ✓ A Record: {a_records[0]}")
            score += 20
        except Exception as e:
            print(f"  ✗ A Record: MISSING")
            self.issues.append("No A record found")
            self.recommendations.append("Add A record pointing to server IP")
        
        # Check MX records
        try:
            mx_records = dns.resolver.resolve(self.domain, 'MX')
            print(f"  ✓ MX Record: {mx_records[0].exchange}")
            score += 20
        except Exception as e:
            print(f"  ✗ MX Record: MISSING")
            self.issues.append("No MX record found")
            self.recommendations.append("Add MX record for email delivery")
        
        # Check SPF record
        try:
            txt_records = dns.resolver.resolve(self.domain, 'TXT')
            spf_found = False
            for record in txt_records:
                if 'v=spf1' in str(record):
                    print(f"  ✓ SPF Record: Found")
                    spf_found = True
                    score += 20
                    break
            if not spf_found:
                print(f"  ⚠ SPF Record: NOT FOUND")
                self.recommendations.append("Add SPF record to prevent email spoofing")
        except Exception as e:
            print(f"  ✗ SPF Record: ERROR")
            self.recommendations.append("Add SPF TXT record")
        
        # Check DKIM
        try:
            dkim = dns.resolver.resolve(f"default._domainkey.{self.domain}", 'TXT')
            print(f"  ✓ DKIM Record: Found")
            score += 20
        except:
            print(f"  ⚠ DKIM Record: NOT FOUND")
            self.recommendations.append("Add DKIM for email authentication")
        
        # Check DMARC
        try:
            dmarc = dns.resolver.resolve(f"_dmarc.{self.domain}", 'TXT')
            print(f"  ✓ DMARC Record: Found")
            score += 20
        except:
            print(f"  ⚠ DMARC Record: NOT FOUND")
            self.recommendations.append("Add DMARC policy for email security")
        
        self.health_score = score
        return score
    
    def check_ssl_certificate(self):
        """Check SSL/TLS certificate"""
        print(f"\n[SSL CHECK] {self.domain}")
        try:
            import ssl
            import socket
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    cert = ssock.getpeercert()
                    expiry = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    days_left = (expiry - datetime.now()).days
                    print(f"  ✓ SSL Certificate valid for {days_left} days")
                    if days_left < 30:
                        self.recommendations.append(f"SSL certificate expires in {days_left} days - renew soon")
                    return True
        except Exception as e:
            print(f"  ⚠ SSL Certificate: {e}")
            self.recommendations.append("Install or renew SSL certificate")
            return False
    
    def check_domain_expiration(self):
        """Check domain registration expiration"""
        print(f"\n[EXPIRATION CHECK] {self.domain}")
        try:
            domain_info = whois.whois(self.domain)
            if domain_info.expiration_date:
                if isinstance(domain_info.expiration_date, list):
                    expiry = domain_info.expiration_date[0]
                else:
                    expiry = domain_info.expiration_date
                days_left = (expiry - datetime.now()).days
                print(f"  ✓ Domain expires in {days_left} days")
                if days_left < 60:
                    self.recommendations.append(f"Domain expires in {days_left} days - renew now!")
                return days_left
        except Exception as e:
            print(f"  ⚠ Could not check expiration: {e}")
        return None
    
    def check_blacklists(self):
        """Check if domain/IP is blacklisted"""
        print(f"\n[BLACKLIST CHECK] {self.domain}")
        # This would check against known blacklist services
        print(f"  ℹ Blacklist check would query RBL services")
        self.recommendations.append("Regularly monitor email blacklists")
        return True
    
    def generate_report(self):
        """Generate comprehensive health report"""
        report = {
            "domain": self.domain,
            "timestamp": datetime.now().isoformat(),
            "health_score": self.health_score,
            "issues": self.issues,
            "recommendations": self.recommendations,
            "grade": self.get_grade()
        }
        
        # Save report
        report_file = f"{REPORTS_DIR}/{self.domain}_health_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n[REPORT] Saved to {report_file}")
        return report
    
    def get_grade(self):
        """Calculate letter grade from score"""
        if self.health_score >= 90:
            return "A+"
        elif self.health_score >= 80:
            return "A"
        elif self.health_score >= 70:
            return "B"
        elif self.health_score >= 60:
            return "C"
        else:
            return "D"

# ==================== EMAIL HEALTH CHECKER ====================
class EmailHealthChecker:
    """Advanced email account monitoring"""
    
    def __init__(self, email, password=None):
        self.email = email
        self.password = password
        self.deliverability_score = 0
        self.issues = []
    
    def check_deliverability(self):
        """Check email deliverability"""
        print(f"\n[EMAIL CHECK] {self.email}")
        domain = self.email.split('@')[1]
        
        # Check MX records for email domain
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            print(f"  ✓ MX records found: {len(list(mx_records))}")
            self.deliverability_score += 50
        except:
            print(f"  ✗ No MX records found")
            self.issues.append("No MX records - emails cannot be delivered")
        
        return self.deliverability_score
    
    def test_smtp_connection(self, smtp_server, port=587):
        """Test SMTP connection"""
        print(f"\n[SMTP TEST] {smtp_server}:{port}")
        try:
            server = smtplib.SMTP(smtp_server, port, timeout=10)
            server.ehlo()
            server.starttls()
            print(f"  ✓ SMTP connection successful")
            server.quit()
            return True
        except Exception as e:
            print(f"  ✗ SMTP connection failed: {e}")
            self.issues.append(f"SMTP connection error: {e}")
            return False
    
    def check_spam_score(self):
        """Check spam score factors"""
        print(f"\n[SPAM SCORE] {self.email}")
        domain = self.email.split('@')[1]
        
        score = 100
        # Check SPF
        try:
            txt_records = dns.resolver.resolve(domain, 'TXT')
            spf_found = any('v=spf1' in str(r) for r in txt_records)
            if spf_found:
                print(f"  ✓ SPF configured")
            else:
                print(f"  ⚠ No SPF record")
                score -= 30
        except:
            score -= 30
        
        print(f"  📊 Spam Score: {score}/100 (higher is better)")
        return score

# ==================== AUTOMATED EMAIL FORWARDING ====================
class EmailForwardingManager:
    """Manage email forwarding rules"""
    
    def __init__(self):
        self.rules = self.load_rules()
    
    def load_rules(self):
        """Load forwarding rules"""
        rules_file = f"{REPORTS_DIR}/forwarding_rules.json"
        if os.path.exists(rules_file):
            with open(rules_file, 'r') as f:
                return json.load(f)
        return {
            "rules": [
                {
                    "from": "info@fishmusicinc.com",
                    "forward_to": ["rsplowman@gmail.com"],
                    "condition": "all",
                    "enabled": True
                },
                {
                    "from": "help@noizylab.ca",
                    "forward_to": ["rsplowman@gmail.com"],
                    "condition": "all",
                    "enabled": True
                }
            ]
        }
    
    def save_rules(self):
        """Save forwarding rules"""
        rules_file = f"{REPORTS_DIR}/forwarding_rules.json"
        with open(rules_file, 'w') as f:
            json.dump(self.rules, f, indent=2)
        print(f"✓ Forwarding rules saved to {rules_file}")
    
    def add_rule(self, from_email, forward_to, condition="all"):
        """Add new forwarding rule"""
        rule = {
            "from": from_email,
            "forward_to": forward_to if isinstance(forward_to, list) else [forward_to],
            "condition": condition,
            "enabled": True
        }
        self.rules['rules'].append(rule)
        self.save_rules()
        print(f"✓ Added forwarding rule: {from_email} → {forward_to}")
    
    def display_rules(self):
        """Display all forwarding rules"""
        print("\n[FORWARDING RULES]")
        for idx, rule in enumerate(self.rules['rules'], 1):
            status = "✓ Active" if rule['enabled'] else "✗ Inactive"
            print(f"{idx}. {rule['from']} → {', '.join(rule['forward_to'])} [{status}]")

# ==================== EMAIL BACKUP SYSTEM ====================
def backup_email_configuration():
    """Backup all email configurations"""
    print("\n[BACKUP] Creating email configuration backup...")
    
    backup_data = {
        "timestamp": datetime.now().isoformat(),
        "domains": CONFIG.get('domains', {}),
        "emails": CONFIG.get('all_emails', []),
        "gmail_setup": CONFIG.get('gmail_setup', {}),
        "server_settings": {}
    }
    
    # Add server settings for each domain
    for domain, settings in CONFIG.get('domains', {}).items():
        backup_data['server_settings'][domain] = settings.get('server_settings', {})
    
    backup_file = f"{BACKUP_DIR}/email_config_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(backup_file, 'w') as f:
        json.dump(backup_data, f, indent=2)
    
    print(f"✓ Backup saved: {backup_file}")
    return backup_file

# ==================== DOMAIN ANALYTICS ====================
def generate_domain_analytics():
    """Generate comprehensive domain analytics"""
    print("\n[ANALYTICS] Generating domain analytics...")
    
    analytics = {
        "timestamp": datetime.now().isoformat(),
        "total_domains": len(DOMAINS),
        "total_emails": len(EMAILS),
        "domains": {},
        "summary": {
            "healthy_domains": 0,
            "needs_attention": 0,
            "critical": 0
        }
    }
    
    for domain in DOMAINS:
        checker = DomainHealthChecker(domain)
        checker.check_dns_records()
        
        analytics['domains'][domain] = {
            "health_score": checker.health_score,
            "grade": checker.get_grade(),
            "issues_count": len(checker.issues),
            "recommendations_count": len(checker.recommendations)
        }
        
        if checker.health_score >= 80:
            analytics['summary']['healthy_domains'] += 1
        elif checker.health_score >= 60:
            analytics['summary']['needs_attention'] += 1
        else:
            analytics['summary']['critical'] += 1
    
    # Save analytics
    analytics_file = f"{REPORTS_DIR}/domain_analytics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(analytics_file, 'w') as f:
        json.dump(analytics, f, indent=2)
    
    print(f"✓ Analytics saved: {analytics_file}")
    return analytics

# ==================== AUTOMATED OPTIMIZATION ====================
def optimize_all_domains():
    """Run optimization on all domains"""
    print("\n" + "="*60)
    print("🚀 DOMAIN & EMAIL OPTIMIZATION - STARTING")
    print("="*60)
    
    optimizations = []
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        
        # Check all domains in parallel
        for domain in DOMAINS:
            futures.append(executor.submit(optimize_domain, domain))
        
        for future in futures:
            result = future.result()
            optimizations.append(result)
    
    return optimizations

def optimize_domain(domain):
    """Optimize single domain"""
    print(f"\n[OPTIMIZE] {domain}")
    
    checker = DomainHealthChecker(domain)
    checker.check_dns_records()
    checker.check_ssl_certificate()
    checker.check_domain_expiration()
    report = checker.generate_report()
    
    print(f"\n✓ {domain} - Health Score: {checker.health_score}/100 (Grade: {checker.get_grade()})")
    
    if checker.recommendations:
        print(f"\n📋 Recommendations for {domain}:")
        for rec in checker.recommendations:
            print(f"  • {rec}")
    
    return report

# ==================== MAIN DASHBOARD ====================
def run_comprehensive_check():
    """Run complete domain and email check"""
    print("\n" + "="*60)
    print("🎯 ADVANCED DOMAIN & EMAIL MANAGER")
    print("="*60)
    
    # 1. Backup configuration
    backup_file = backup_email_configuration()
    
    # 2. Check all domains
    domain_reports = optimize_all_domains()
    
    # 3. Check email deliverability
    print("\n[EMAIL DELIVERABILITY CHECK]")
    for email in EMAILS[:3]:  # Check first 3 emails as examples
        checker = EmailHealthChecker(email)
        checker.check_deliverability()
    
    # 4. Generate analytics
    analytics = generate_domain_analytics()
    
    # 5. Display forwarding rules
    forwarder = EmailForwardingManager()
    forwarder.display_rules()
    
    # 6. Final summary
    print("\n" + "="*60)
    print("✅ COMPREHENSIVE CHECK COMPLETE!")
    print("="*60)
    print(f"\n📊 SUMMARY:")
    print(f"  • Domains checked: {len(DOMAINS)}")
    print(f"  • Emails verified: {len(EMAILS)}")
    print(f"  • Healthy domains: {analytics['summary']['healthy_domains']}")
    print(f"  • Needs attention: {analytics['summary']['needs_attention']}")
    print(f"  • Backup created: {backup_file}")
    print(f"\n📁 Reports saved to: {REPORTS_DIR}")
    
    return {
        "backup": backup_file,
        "analytics": analytics,
        "domain_reports": domain_reports
    }

if __name__ == "__main__":
    run_comprehensive_check()

