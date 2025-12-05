#!/usr/bin/env python3
"""
SIMPLE EMAIL TEST - Just paste your app password and GO!
"""
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

print("\n" + "="*60)
print("  SIMPLE EMAIL TEST - PASTE APP PASSWORD & SEE IT WORK!")
print("="*60 + "\n")

print("1. Get Gmail App Password:")
print("   https://myaccount.google.com/apppasswords")
print()

password = input("Paste app password here: ").strip().replace(" ", "")

if not password:
    print("\n❌ No password entered!")
    exit(1)

print(f"\n🚀 Sending test email...")

try:
    msg = MIMEText(f"✅ IT WORKS!! Email sent at {datetime.now()}\n\nGORUNFREE! 🚀")
    msg['Subject'] = "✅ EMAIL WORKS!!"
    msg['From'] = "rsp@noizyfish.com"
    msg['To'] = "rsp@noizyfish.com"
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("rsp@noizyfish.com", password)
    s.send_message(msg)
    s.quit()
    
    print("\n" + "="*60)
    print("  ✅✅✅ EMAIL SENT!! CHECK YOUR INBOX!! ✅✅✅")
    print("="*60 + "\n")
    
except smtplib.SMTPAuthenticationError:
    print("\n" + "="*60)
    print("  ❌ WRONG PASSWORD or 2FA NOT ENABLED")
    print("="*60)
    print("\nGo to: https://myaccount.google.com/apppasswords")
    print("Make sure 2-Step Verification is ON first!\n")
    
except Exception as e:
    print(f"\n❌ Error: {e}\n")
