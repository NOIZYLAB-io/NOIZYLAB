#!/usr/bin/env python3
"""
MS365 ADMIN AGENT - NOIZYLAB
IT Administration, Upgrades, Improvements, AI Add-ons Tracker
"""

import subprocess
import sys
import os
import sqlite3
import datetime
import json

DB_FILE = '/Users/m2ultra/NOIZYLAB/data/ms365_admin.db'

# Your email accounts
EMAIL_ACCOUNTS = [
    "rp@fishmusicinc.com",
    "gofish@fishmusicinc.com"
]

# Domains managed
DOMAINS = [
    "NOIZY.ai",
    "NOIZYFISH.com",
    "fishmusicinc.com"
]

# DNS Provider
DNS_PROVIDER = "Cloudflare"
REGISTRAR = "GoDaddy"

def init_database():
    """Initialize the MS365 Admin database"""
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Admin Tasks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin_tasks (
        id INTEGER PRIMARY KEY,
        area TEXT,
        description TEXT,
        status TEXT DEFAULT 'Open',
        assigned_to TEXT DEFAULT 'IT Agent',
        date_logged TEXT,
        upgrade_needed BOOLEAN,
        improvement_suggestion TEXT,
        ai_addon_idea TEXT,
        priority TEXT DEFAULT 'Medium',
        notes TEXT
    )
    ''')

    # Upgrades table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS upgrades (
        id INTEGER PRIMARY KEY,
        source TEXT,
        description TEXT,
        date_added TEXT,
        status TEXT DEFAULT 'Pending'
    )
    ''')

    # Improvements table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS improvements (
        id INTEGER PRIMARY KEY,
        category TEXT,
        suggestion TEXT,
        date_added TEXT,
        implemented BOOLEAN DEFAULT 0
    )
    ''')

    # AI Add-ons table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ai_addons (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        category TEXT,
        status TEXT DEFAULT 'Researching',
        date_added TEXT
    )
    ''')

    # DNS Records table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dns_records (
        id INTEGER PRIMARY KEY,
        domain TEXT,
        record_type TEXT,
        name TEXT,
        value TEXT,
        status TEXT DEFAULT 'Active',
        last_checked TEXT
    )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized!")

def add_default_tasks():
    """Add default admin tasks"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()

    default_tasks = [
        ("User Account Management", "Add new user onboarding automation", True, "Streamline workflow", "AI onboarding", "High"),
        ("Office App Updates", "Ensure all users on latest Office", True, "Auto-update script", "AI update bot", "Medium"),
        ("Security", "Enable MFA for all users", False, "N/A", "N/A", "High"),
        ("Email Management", "Automate spam filtering", True, "Improve rules", "AI spam filter", "High"),
        ("Missing Feature", "Bulk license assignment", True, "Add PowerShell script", "AI license bot", "Medium"),
        ("DNS Management", "Verify Cloudflare DNS records", True, "Automate checks", "AI DNS monitor", "High"),
        ("Copilot Pro+", "Configure MS365 Copilot for admin", True, "Enable all features", "AI Admin Assistant", "High"),
    ]

    for task in default_tasks:
        cursor.execute('''
        INSERT OR IGNORE INTO admin_tasks
        (area, description, upgrade_needed, improvement_suggestion, ai_addon_idea, priority, date_logged)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (*task, today))

    conn.commit()
    conn.close()
    print("Default tasks added!")

def add_ai_addons():
    """Add recommended AI add-ons"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()

    addons = [
        ("MS365 Copilot Pro+", "AI-powered admin assistant integrated into Admin Center", "Admin"),
        ("OfficeAI", "Specialized AI agents for Excel, Word, PowerPoint, Outlook", "Productivity"),
        ("Power BI", "Advanced analytics and dashboards", "Reporting"),
        ("Asa for Teams", "Conversational AI for task management", "Teams"),
        ("AI Admin Assistant", "Automate repetitive admin tasks", "Automation"),
        ("Smart Workflow Optimizer", "Analyze and improve admin workflows", "Optimization"),
        ("Security Advisor AI", "Monitor security and recommend improvements", "Security"),
        ("License Management Bot", "Track and automate license assignments", "Licensing"),
    ]

    for addon in addons:
        cursor.execute('''
        INSERT OR IGNORE INTO ai_addons (name, description, category, date_added)
        VALUES (?, ?, ?, ?)
        ''', (*addon, today))

    conn.commit()
    conn.close()
    print("AI add-ons added!")

def add_dns_records():
    """Add DNS records for tracking"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()

    # Sample DNS records to track
    records = [
        ("fishmusicinc.com", "MX", "@", "mail.fishmusicinc.com"),
        ("fishmusicinc.com", "TXT", "@", "v=spf1 include:_spf.google.com ~all"),
        ("NOIZY.ai", "A", "@", "CloudflareIP"),
        ("NOIZY.ai", "CNAME", "www", "NOIZY.ai"),
        ("NOIZYFISH.com", "A", "@", "CloudflareIP"),
        ("NOIZYFISH.com", "CNAME", "www", "NOIZYFISH.com"),
    ]

    for record in records:
        cursor.execute('''
        INSERT OR IGNORE INTO dns_records (domain, record_type, name, value, last_checked)
        VALUES (?, ?, ?, ?, ?)
        ''', (*record, today))

    conn.commit()
    conn.close()
    print("DNS records added!")

def get_status_report():
    """Generate status report"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print("\n" + "=" * 60)
    print("MS365 ADMIN AGENT - STATUS REPORT")
    print("=" * 60)

    # Tasks summary
    cursor.execute("SELECT COUNT(*) FROM admin_tasks WHERE status = 'Open'")
    open_tasks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM admin_tasks WHERE status = 'Completed'")
    completed_tasks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ai_addons")
    addon_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM dns_records")
    dns_count = cursor.fetchone()[0]

    print(f"\nOpen Tasks: {open_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"AI Add-ons Tracked: {addon_count}")
    print(f"DNS Records: {dns_count}")

    print(f"\nDomains: {', '.join(DOMAINS)}")
    print(f"DNS Provider: {DNS_PROVIDER}")
    print(f"Registrar: {REGISTRAR}")
    print(f"Email Accounts: {', '.join(EMAIL_ACCOUNTS)}")

    print("\n" + "=" * 60)

    conn.close()

def main():
    print("=" * 60)
    print("MS365 ADMIN AGENT - NOIZYLAB")
    print("Upgrade & Improve | Missing | Suggestions | AI Add-ons")
    print("=" * 60)

    # Initialize
    init_database()
    add_default_tasks()
    add_ai_addons()
    add_dns_records()

    # Report
    get_status_report()

    print("\nMS365 Admin Agent initialized successfully!")
    print(f"Database: {DB_FILE}")

if __name__ == "__main__":
    main()
