#!/usr/bin/env python3
"""
🔥 FIX EMAILS NOW - SHOW ROB WORKING EMAILS!!
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

print("🔥 FIXING EMAILS NOW!!")
print("=" * 60)
print()

# Use Gmail SMTP directly - THIS WORKS!
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

print("📧 EMAIL CONFIGURATION:")
print(f"  Server: {SMTP_SERVER}")
print(f"  Port: {SMTP_PORT}")
print()

# Test with rsp@noizyfish.com
FROM_EMAIL = "rsp@noizyfish.com"

print("🔑 SETUP REQUIRED:")
print()
print("1. Go to: https://myaccount.google.com/security")
print("2. Enable 2-Step Verification")
print("3. Create App Password:")
print("   - Search 'App Passwords'")
print("   - Select 'Mail'")
print("   - Generate password")
print("4. Copy that password")
print()

app_password = input("Paste your Gmail App Password here: ").strip()

if not app_password:
    print("❌ No password provided!")
    exit(1)

print()
print("🚀 SENDING TEST EMAIL TO SHOW IT WORKS...")
print()

# Send to ROB's email
TO_EMAIL = input("Your email to receive test (press Enter for rsp@noizyfish.com): ").strip()
if not TO_EMAIL:
    TO_EMAIL = "rsp@noizyfish.com"

try:
    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "🔥 EMAIL SYSTEM WORKING!! - Test from CB_01"
    msg['From'] = f"NoizyLab <{FROM_EMAIL}>"
    msg['To'] = TO_EMAIL
    
    text = f"""
EMAIL SYSTEM IS WORKING!!

This is a test email from your fixed email system.

If you're reading this - EMAILS ARE FIXED! ✅

Sent: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
From: {FROM_EMAIL}
System: ULTIMATE_FISH_MAILER

GORUNFREE! 🚀

CB_01
"""
    
    html = f"""
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; padding: 20px; background: #f0f0f0;">
    <div style="max-width: 600px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h1 style="color: #00ff88; margin-bottom: 20px;">🔥 EMAIL SYSTEM WORKING!!</h1>
        
        <div style="background: #00ff88; color: #0f0f23; padding: 20px; border-radius: 5px; margin: 20px 0;">
            <h2 style="margin: 0;">✅ EMAILS ARE FIXED!</h2>
        </div>
        
        <p>If you're reading this - <strong>YOUR EMAIL SYSTEM IS WORKING PERFECTLY!</strong></p>
        
        <p><strong>Sent:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
        <strong>From:</strong> {FROM_EMAIL}<br>
        <strong>System:</strong> ULTIMATE_FISH_MAILER</p>
        
        <p style="color: #00ff88; font-size: 1.5rem; font-weight: bold; margin-top: 30px;">GORUNFREE! 🚀</p>
        
        <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
        
        <p style="font-size: 12px; color: #666;">
            CB_01 - Your LIFELUV ENGR<br>
            NoizyLab Portal | noizylab.ca
        </p>
    </div>
</body>
</html>
"""
    
    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))
    
    # SEND IT!
    print(f"📤 Connecting to {SMTP_SERVER}...")
    
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
    server.starttls()
    
    print(f"🔐 Logging in as {FROM_EMAIL}...")
    server.login(FROM_EMAIL, app_password)
    
    print(f"📧 Sending to {TO_EMAIL}...")
    server.send_message(msg)
    server.quit()
    
    print()
    print("=" * 60)
    print("🎉 EMAIL SENT SUCCESSFULLY!!")
    print("=" * 60)
    print()
    print(f"✅ Check your inbox: {TO_EMAIL}")
    print("✅ Email system is WORKING!")
    print("✅ You should see it within seconds!")
    print()
    
    # Save working config
    config = {
        "smtp_server": SMTP_SERVER,
        "smtp_port": SMTP_PORT,
        "from_email": FROM_EMAIL,
        "username": FROM_EMAIL,
        "password": app_password,
        "working": True,
        "tested": datetime.now().isoformat()
    }
    
    with open('working_email_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("💾 Configuration saved to working_email_config.json")
    print()
    print("GORUNFREE! 🚀")
    
except smtplib.SMTPAuthenticationError as e:
    print()
    print("❌ AUTHENTICATION FAILED!")
    print()
    print("The app password is wrong or 2FA isn't enabled.")
    print()
    print("STEPS TO FIX:")
    print("1. Go to: https://myaccount.google.com/security")
    print("2. Make sure 2-Step Verification is ON")
    print("3. Search for 'App Passwords'")
    print("4. Create new app password for 'Mail'")
    print("5. Run this script again with that password")
    print()
    
except Exception as e:
    print()
    print(f"❌ ERROR: {e}")
    print()
    print("Something went wrong. Check your internet connection.")
    print()

