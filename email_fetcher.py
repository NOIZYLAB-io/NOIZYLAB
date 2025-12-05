#!/usr/bin/env python3
"""
NOIZYLAB Email Fetcher
Fetches emails from fishmusicinc.com accounts
"""

import os
import imaplib
import email
import sqlite3
import datetime
from email.header import decode_header

# Configuration - Set these as environment variables or update directly
EMAIL_ACCOUNTS = [
    {
        "user": "rp@fishmusicinc.com",
        "server": "imap.fishmusicinc.com",
        "port": 993
    },
    {
        "user": "gofish@fishmusicinc.com",
        "server": "imap.fishmusicinc.com",
        "port": 993
    }
]

DB_FILE = '/Users/m2ultra/NOIZYLAB/data/emails.db'

def init_database():
    """Initialize email database"""
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY,
        account TEXT,
        subject TEXT,
        sender TEXT,
        date_received TEXT,
        has_improvement BOOLEAN DEFAULT 0,
        has_upgrade BOOLEAN DEFAULT 0,
        processed BOOLEAN DEFAULT 0,
        date_fetched TEXT
    )
    ''')
    conn.commit()
    conn.close()

def decode_subject(subject):
    """Decode email subject"""
    if subject is None:
        return "No Subject"
    decoded = decode_header(subject)
    result = ""
    for part, charset in decoded:
        if isinstance(part, bytes):
            result += part.decode(charset or 'utf-8', errors='ignore')
        else:
            result += part
    return result

def fetch_emails_from_account(account_config, password):
    """Fetch emails from a single account"""
    emails_fetched = []
    try:
        mail = imaplib.IMAP4_SSL(account_config["server"], account_config["port"])
        mail.login(account_config["user"], password)
        mail.select('inbox')

        # Search for recent emails (last 7 days)
        typ, data = mail.search(None, 'ALL')

        for num in data[0].split()[-50:]:  # Last 50 emails
            typ, msg_data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])

            subject = decode_subject(msg['subject'])
            sender = msg['from']
            date = msg['date']

            # Check for upgrade/improvement keywords
            has_improvement = any(kw in subject.lower() for kw in ['improve', 'suggestion', 'better', 'fix'])
            has_upgrade = any(kw in subject.lower() for kw in ['upgrade', 'update', 'new version', 'patch'])

            emails_fetched.append({
                'account': account_config["user"],
                'subject': subject,
                'sender': sender,
                'date': date,
                'has_improvement': has_improvement,
                'has_upgrade': has_upgrade
            })

        mail.logout()
        print(f"Fetched {len(emails_fetched)} emails from {account_config['user']}")

    except Exception as e:
        print(f"Error fetching from {account_config['user']}: {e}")

    return emails_fetched

def save_to_database(emails):
    """Save fetched emails to database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()

    for em in emails:
        cursor.execute('''
        INSERT INTO emails (account, subject, sender, date_received, has_improvement, has_upgrade, date_fetched)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (em['account'], em['subject'], em['sender'], em['date'],
              em['has_improvement'], em['has_upgrade'], today))

    conn.commit()
    conn.close()
    print(f"Saved {len(emails)} emails to database")

def main():
    print("=" * 60)
    print("NOIZYLAB EMAIL FETCHER")
    print("=" * 60)

    init_database()

    print("\nEmail accounts configured:")
    for acc in EMAIL_ACCOUNTS:
        print(f"  - {acc['user']} @ {acc['server']}:{acc['port']}")

    print("\nTo fetch emails, set EMAIL_PASS environment variable")
    print("or call fetch_emails_from_account() with password")

    print("\nDatabase initialized at:", DB_FILE)

if __name__ == "__main__":
    main()
