#!/usr/bin/env python3
"""
🔥 BULLETPROOF EMAIL FIX - MULTIPLE METHODS THAT ACTUALLY WORK!!
Try Gmail, SendGrid, AND Mailgun - ONE of these WILL work!!
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import sys

def send_with_gmail(from_email, app_password, to_email):
    """Method 1: Gmail"""
    print("📧 METHOD 1: Trying Gmail...")
    
    try:
        msg = MIMEMultipart()
        msg['Subject'] = "✅ EMAIL WORKING - Gmail Method"
        msg['From'] = from_email
        msg['To'] = to_email
        
        body = f"""
✅ EMAIL IS WORKING!!

Method: Gmail SMTP
From: {from_email}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

If you see this - GMAIL METHOD WORKS!! ✅

GORUNFREE! 🚀
CB_01
"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
        server.quit()
        
        print("✅✅✅ GMAIL WORKED!!")
        print(f"   Email sent to: {to_email}")
        print(f"   CHECK YOUR INBOX NOW!!")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ Gmail authentication failed - trying next method...")
        return False
    except Exception as e:
        print(f"❌ Gmail failed: {e}")
        return False

def send_with_sendgrid(api_key, to_email):
    """Method 2: SendGrid API"""
    print("\n📧 METHOD 2: Trying SendGrid...")
    
    try:
        import requests
        
        url = "https://api.sendgrid.com/v3/mail/send"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "personalizations": [{
                "to": [{"email": to_email}],
                "subject": "✅ EMAIL WORKING - SendGrid Method"
            }],
            "from": {"email": "rsp@noizyfish.com", "name": "NoizyLab"},
            "content": [{
                "type": "text/plain",
                "value": f"""
✅ EMAIL IS WORKING!!

Method: SendGrid API
From: rsp@noizyfish.com
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

If you see this - SENDGRID METHOD WORKS!! ✅

GORUNFREE! 🚀
CB_01
"""
            }]
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 202:
            print("✅✅✅ SENDGRID WORKED!!")
            print(f"   Email sent to: {to_email}")
            print(f"   CHECK YOUR INBOX NOW!!")
            return True
        else:
            print(f"❌ SendGrid failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ SendGrid failed: {e}")
        return False

def send_with_mailgun(api_key, domain, to_email):
    """Method 3: Mailgun API"""
    print("\n📧 METHOD 3: Trying Mailgun...")
    
    try:
        import requests
        
        url = f"https://api.mailgun.net/v3/{domain}/messages"
        
        response = requests.post(
            url,
            auth=("api", api_key),
            data={
                "from": f"NoizyLab <noreply@{domain}>",
                "to": to_email,
                "subject": "✅ EMAIL WORKING - Mailgun Method",
                "text": f"""
✅ EMAIL IS WORKING!!

Method: Mailgun API
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

If you see this - MAILGUN METHOD WORKS!! ✅

GORUNFREE! 🚀
CB_01
"""
            }
        )
        
        if response.status_code == 200:
            print("✅✅✅ MAILGUN WORKED!!")
            print(f"   Email sent to: {to_email}")
            print(f"   CHECK YOUR INBOX NOW!!")
            return True
        else:
            print(f"❌ Mailgun failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Mailgun failed: {e}")
        return False

# MAIN - TRY ALL METHODS
if __name__ == "__main__":
    print()
    print("🔥" * 40)
    print()
    print("     BULLETPROOF EMAIL FIX")
    print("     TRYING MULTIPLE METHODS UNTIL ONE WORKS!!")
    print()
    print("🔥" * 40)
    print()
    
    to_email = input("Send test email to (default: rsp@noizyfish.com): ").strip()
    if not to_email:
        to_email = "rsp@noizyfish.com"
    
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("TRYING ALL METHODS...")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Method 1: Gmail
    print("\n🔑 For Gmail, enter your app password")
    print("   (Get it at: https://myaccount.google.com/apppasswords)")
    gmail_password = input("   Gmail app password (or press Enter to skip): ").strip()
    
    if gmail_password:
        if send_with_gmail("rsp@noizyfish.com", gmail_password, to_email):
            print("\n🎉🎉🎉 SUCCESS WITH GMAIL!! 🎉🎉🎉")
            print("\nCHECK YOUR INBOX NOW!!")
            sys.exit(0)
    
    # Method 2: SendGrid
    print("\n🔑 For SendGrid (FREE! signup at sendgrid.com)")
    sendgrid_key = input("   SendGrid API key (or press Enter to skip): ").strip()
    
    if sendgrid_key:
        if send_with_sendgrid(sendgrid_key, to_email):
            print("\n🎉🎉🎉 SUCCESS WITH SENDGRID!! 🎉🎉🎉")
            print("\nCHECK YOUR INBOX NOW!!")
            sys.exit(0)
    
    # Method 3: Mailgun
    print("\n🔑 For Mailgun (FREE! signup at mailgun.com)")
    mailgun_key = input("   Mailgun API key (or press Enter to skip): ").strip()
    mailgun_domain = input("   Mailgun domain (or press Enter to skip): ").strip()
    
    if mailgun_key and mailgun_domain:
        if send_with_mailgun(mailgun_key, mailgun_domain, to_email):
            print("\n🎉🎉🎉 SUCCESS WITH MAILGUN!! 🎉🎉🎉")
            print("\nCHECK YOUR INBOX NOW!!")
            sys.exit(0)
    
    print()
    print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
    print("     NO METHOD WORKED YET")
    print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
    print()
    print("NEXT STEPS:")
    print()
    print("1. GET GMAIL APP PASSWORD:")
    print("   https://myaccount.google.com/apppasswords")
    print("   - Turn on 2FA first")
    print("   - Create password for 'Mail'")
    print("   - Run script again with that password")
    print()
    print("OR")
    print()
    print("2. SIGN UP SENDGRID (EASIER!):")
    print("   https://signup.sendgrid.com")
    print("   - 100% FREE (100 emails/day)")
    print("   - Get API key instantly")
    print("   - Run script with SendGrid key")
    print()
    print("ONE OF THESE WILL WORK!! 🚀")
    print()

