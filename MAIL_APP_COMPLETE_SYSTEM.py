#!/usr/bin/env python3
"""
🍎 MAIL.APP COMPLETE EMAIL SYSTEM - NO PASSWORDS EVER!!
Uses your Mac's native Mail.app - if it's configured, this JUST WORKS!!
"""

import subprocess
import os
from datetime import datetime
import json

class MailAppMailer:
    """Complete email system using Apple Mail.app - NO PASSWORDS!"""
    
    def __init__(self):
        self.from_name = "Rob @ NoizyLab"
        print("🍎 Mail.app Email System Initialized")
        print("   Using your configured Mail.app accounts!")
    
    def send_email(self, to_email, subject, body_text, body_html=None):
        """Send email via Mail.app"""
        
        # Use text body (Mail.app doesn't handle HTML well via AppleScript)
        content = body_text
        
        # Escape quotes for AppleScript
        content = content.replace('"', '\\"')
        subject = subject.replace('"', '\\"')
        
        script = f'''
tell application "Mail"
    set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{content}", visible:false}}
    
    tell newMessage
        make new to recipient at end of to recipients with properties {{address:"{to_email}"}}
        send
    end tell
end tell
'''
        
        try:
            result = subprocess.run(
                ['osascript', '-e', script],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"✅ Email sent to {to_email}")
                self.log_email(to_email, subject, 'success')
                return True
            else:
                print(f"❌ Mail.app error: {result.stderr}")
                self.log_email(to_email, subject, 'failed', result.stderr)
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            self.log_email(to_email, subject, 'error', str(e))
            return False
    
    def send_receipt(self, customer_email, customer_name, track_name, price, order_id):
        """Send purchase receipt"""
        subject = f"🐟 Thank you for your purchase! Order #{order_id}"
        
        body = f"""
Hi {customer_name}!

Thank you for supporting Fish Music Inc!

ORDER DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━
Order #: {order_id}
Track: {track_name}
Price: ${price:.2f}

Your download link will arrive shortly.

We create music with passion, love, and FLOW.

GORUNFREE! 🚀

Best,
Rob @ Fish Music Inc
rsplowman@icloud.com
fishmusicinc.com
"""
        
        return self.send_email(customer_email, subject, body)
    
    def send_download_link(self, customer_email, customer_name, track_name, download_url):
        """Send download link"""
        subject = f"🎵 Your track is ready: {track_name}"
        
        body = f"""
Hi {customer_name}!

Your track is ready to download!

Track: {track_name}
Download: {download_url}

This link expires in 7 days.

Enjoy your music! 🎵

Rob @ Fish Music Inc
rsplowman@icloud.com
"""
        
        return self.send_email(customer_email, subject, body)
    
    def send_invoice(self, client_email, client_name, invoice_number, amount, description, due_date):
        """Send invoice"""
        subject = f"🧾 Invoice {invoice_number} from NoizyLab"
        
        body = f"""
Hi {client_name},

Your invoice is ready!

INVOICE {invoice_number}
━━━━━━━━━━━━━━━━━━━━━━━━━━
Amount: ${amount:.2f}
Due Date: {due_date}

Description:
{description}

PAYMENT METHODS:
• PayPal: rsp@noizyfish.com
• e-Transfer: rsp@noizylab.ca
• Stripe: [payment link]

Thank you for your business!

Rob @ NoizyLab
noizylab.ca
rsplowman@icloud.com
"""
        
        return self.send_email(client_email, subject, body)
    
    def send_checkin_notification(self, project_name, status, hours, notes):
        """Send check-in notification to yourself"""
        subject = f"📝 Check-in: {project_name}"
        
        body = f"""
PROJECT CHECK-IN LOGGED

Project: {project_name}
Status: {status}
Hours Worked: {hours}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

NOTES:
{notes}

---
NoizyLab Portal
noizylab.ca
"""
        
        return self.send_email("rsplowman@icloud.com", subject, body)
    
    def log_email(self, to, subject, status, error=None):
        """Log email sends"""
        log_file = 'mail_app_log.json'
        
        log = []
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                log = json.load(f)
        
        log.append({
            'timestamp': datetime.now().isoformat(),
            'to': to,
            'subject': subject,
            'status': status,
            'error': error,
            'method': 'Mail.app'
        })
        
        with open(log_file, 'w') as f:
            json.dump(log, f, indent=2)

# CLI INTERFACE
if __name__ == "__main__":
    import sys
    
    print("🍎 MAIL.APP EMAIL SYSTEM")
    print("=" * 60)
    print()
    
    mailer = MailAppMailer()
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  Send test email:
    python3 MAIL_APP_COMPLETE_SYSTEM.py test your@email.com
  
  Send receipt:
    python3 MAIL_APP_COMPLETE_SYSTEM.py receipt \\
      customer@email.com "John Smith" "Track Name" 9.99 "ORD123"
  
  Send download link:
    python3 MAIL_APP_COMPLETE_SYSTEM.py download \\
      customer@email.com "John Smith" "Track Name" "https://download.link"
  
  Send invoice:
    python3 MAIL_APP_COMPLETE_SYSTEM.py invoice \\
      client@email.com "Client Name" "INV001" 1500.00 "Services" "2025-12-31"
  
  Send check-in:
    python3 MAIL_APP_COMPLETE_SYSTEM.py checkin \\
      "Project Name" "in_progress" 4.5 "Worked on mixing today"

FEATURES:
  ✅ Uses your Mac's Mail.app (no passwords!)
  ✅ All email templates included
  ✅ Logs all sends
  ✅ Works with ANY email configured in Mail.app
        """)
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "test":
        email = sys.argv[2] if len(sys.argv) > 2 else "rsplowman@icloud.com"
        mailer.send_email(
            email,
            "🍎 Test from Mail.app System",
            f"This works!! No passwords needed!!\n\nSent: {datetime.now()}\n\nGORUNFREE! 🚀"
        )
    
    elif command == "receipt":
        mailer.send_receipt(
            sys.argv[2], sys.argv[3], sys.argv[4],
            float(sys.argv[5]), sys.argv[6]
        )
    
    elif command == "download":
        mailer.send_download_link(
            sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        )
    
    elif command == "invoice":
        mailer.send_invoice(
            sys.argv[2], sys.argv[3], sys.argv[4],
            float(sys.argv[5]), sys.argv[6], sys.argv[7]
        )
    
    elif command == "checkin":
        mailer.send_checkin_notification(
            sys.argv[2], sys.argv[3], float(sys.argv[4]), sys.argv[5]
        )
    
    else:
        print(f"❌ Unknown command: {command}")

