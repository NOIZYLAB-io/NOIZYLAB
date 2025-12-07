#!/usr/bin/env python3
"""
🐟 FISH MUSIC EMAIL SYSTEM - Complete SMTP/Email Solution
Handles all Fish Music Inc email operations with FLOW
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import json
import os

class FishMailer:
    """Complete email system for Fish Music Inc"""
    
    def __init__(self, config_file="email_config.json"):
        """Initialize with config"""
        self.config = self.load_config(config_file)
        self.from_email = self.config.get('from_email', 'rsp@fishmusicinc.com')
        self.from_name = self.config.get('from_name', 'Fish Music Inc')
        
    def load_config(self, config_file):
        """Load email configuration"""
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
        return self.create_default_config(config_file)
    
    def create_default_config(self, config_file):
        """Create default configuration"""
        config = {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "use_tls": True,
            "from_email": "rsp@fishmusicinc.com",
            "from_name": "Fish Music Inc",
            "username": "",
            "password": "",
            "provider": "gmail"
        }
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"✅ Created default config: {config_file}")
        print("⚠️  Please edit with your SMTP credentials!")
        return config
    
    def send_email(self, to_email, subject, body_text, body_html=None, attachments=None):
        """Send email with optional HTML and attachments"""
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"{self.from_name} <{self.from_email}>"
            msg['To'] = to_email
            msg['Date'] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
            
            # Add text body
            msg.attach(MIMEText(body_text, 'plain'))
            
            # Add HTML body if provided
            if body_html:
                msg.attach(MIMEText(body_html, 'html'))
            
            # Add attachments if provided
            if attachments:
                for filepath in attachments:
                    self.attach_file(msg, filepath)
            
            # Send via SMTP
            self.send_via_smtp(msg, to_email)
            
            print(f"✅ Email sent to {to_email}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False
    
    def send_via_smtp(self, msg, to_email):
        """Send message via SMTP"""
        server = self.config.get('smtp_server')
        port = self.config.get('smtp_port', 587)
        username = self.config.get('username')
        password = self.config.get('password')
        
        if not username or not password:
            raise ValueError("SMTP credentials not configured!")
        
        context = ssl.create_default_context()
        
        with smtplib.SMTP(server, port) as smtp:
            if self.config.get('use_tls', True):
                smtp.starttls(context=context)
            smtp.login(username, password)
            smtp.send_message(msg)
    
    def attach_file(self, msg, filepath):
        """Attach file to email"""
        with open(filepath, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        
        encoders.encode_base64(part)
        filename = os.path.basename(filepath)
        part.add_header('Content-Disposition', f'attachment; filename= {filename}')
        msg.attach(part)
    
    # FISH MUSIC SPECIFIC EMAIL TEMPLATES
    
    def send_purchase_receipt(self, customer_email, customer_name, track_name, price, order_id):
        """Send purchase receipt"""
        subject = f"🐟 Thanks for your Fish Music purchase! Order #{order_id}"
        
        text = f"""
Hi {customer_name}!

Thank you for supporting Fish Music Inc! 

Your Order #{order_id}:
- Track: {track_name}
- Price: ${price}

Your download link will arrive shortly.

GORUNFREE! 🚀

Best,
Rob @ Fish Music Inc
rsp@fishmusicinc.com
"""
        
        html = f"""
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">
    <h2 style="color: #0066cc;">🐟 Fish Music Inc</h2>
    <h3>Thanks for your purchase, {customer_name}!</h3>
    
    <div style="background: #f4f4f4; padding: 20px; border-radius: 5px;">
        <strong>Order #{order_id}</strong><br>
        Track: <strong>{track_name}</strong><br>
        Price: <strong>${price}</strong>
    </div>
    
    <p>Your download link will arrive shortly.</p>
    
    <p style="color: #0066cc; font-weight: bold;">GORUNFREE! 🚀</p>
    
    <hr>
    <p style="font-size: 12px; color: #666;">
        Fish Music Inc<br>
        rsp@fishmusicinc.com<br>
        fishmusicinc.com
    </p>
</body>
</html>
"""
        
        return self.send_email(customer_email, subject, text, html)
    
    def send_download_link(self, customer_email, customer_name, track_name, download_url):
        """Send track download link"""
        subject = f"🎵 Your Fish Music download is ready!"
        
        text = f"""
Hi {customer_name}!

Your track is ready to download:

Track: {track_name}
Download: {download_url}

This link expires in 7 days.

Enjoy! 🎵

Rob @ Fish Music Inc
"""
        
        html = f"""
<html>
<body style="font-family: Arial, sans-serif;">
    <h2 style="color: #0066cc;">🎵 Your track is ready!</h2>
    
    <p>Hi {customer_name},</p>
    
    <div style="background: #f4f4f4; padding: 20px; border-radius: 5px; margin: 20px 0;">
        <strong>{track_name}</strong><br><br>
        <a href="{download_url}" style="background: #0066cc; color: white; padding: 12px 24px; 
           text-decoration: none; border-radius: 5px; display: inline-block;">
            Download Track
        </a>
    </div>
    
    <p style="font-size: 12px; color: #666;">
        This link expires in 7 days.
    </p>
    
    <p>Enjoy! 🎵</p>
    
    <hr>
    <p style="font-size: 12px; color: #666;">
        Fish Music Inc | rsp@fishmusicinc.com
    </p>
</body>
</html>
"""
        
        return self.send_email(customer_email, subject, text, html)
    
    def send_welcome_email(self, customer_email, customer_name):
        """Send welcome email to new customer"""
        subject = "🐟 Welcome to Fish Music Inc!"
        
        text = f"""
Hi {customer_name}!

Welcome to Fish Music Inc!

We create original music with passion, love, and FLOW.

Check out our latest releases:
fishmusicinc.com

GORUNFREE! 🚀

Rob @ Fish Music Inc
"""
        
        html = f"""
<html>
<body style="font-family: Arial, sans-serif;">
    <h1 style="color: #0066cc;">🐟 Welcome to Fish Music Inc!</h1>
    
    <p>Hi {customer_name}!</p>
    
    <p>Thanks for joining the Fish Music family.</p>
    
    <p>We create original music with <strong>passion, love, and FLOW</strong>.</p>
    
    <p>
        <a href="https://fishmusicinc.com" style="color: #0066cc;">
            Check out our latest releases →
        </a>
    </p>
    
    <p style="color: #0066cc; font-weight: bold; font-size: 18px;">GORUNFREE! 🚀</p>
    
    <hr>
    <p style="font-size: 12px; color: #666;">
        Rob @ Fish Music Inc<br>
        rsp@fishmusicinc.com
    </p>
</body>
</html>
"""
        
        return self.send_email(customer_email, subject, text, html)
    
    def send_newsletter(self, subscribers, subject, content_text, content_html):
        """Send newsletter to subscriber list"""
        results = {'sent': 0, 'failed': 0}
        
        for subscriber in subscribers:
            email = subscriber.get('email')
            name = subscriber.get('name', 'Friend')
            
            # Personalize content
            text = content_text.replace('{{name}}', name)
            html = content_html.replace('{{name}}', name)
            
            if self.send_email(email, subject, text, html):
                results['sent'] += 1
            else:
                results['failed'] += 1
        
        print(f"\n📊 Newsletter sent: {results['sent']} success, {results['failed']} failed")
        return results

# CLI Interface
if __name__ == "__main__":
    import sys
    
    print("🐟 FISH MUSIC EMAIL SYSTEM")
    print("=" * 50)
    
    mailer = FishMailer()
    
    if len(sys.argv) < 2:
        print("""
Usage:
  python fish_mail.py test <email>
  python fish_mail.py receipt <email> <name> <track> <price> <order_id>
  python fish_mail.py download <email> <name> <track> <url>
  python fish_mail.py welcome <email> <name>
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "test":
        email = sys.argv[2]
        mailer.send_email(
            email,
            "🐟 Test from Fish Music Email System",
            "This is a test email. If you're seeing this, everything works! GORUNFREE! 🚀",
            "<h1>Test Email</h1><p>Everything works! 🐟</p>"
        )
    
    elif command == "receipt":
        mailer.send_purchase_receipt(
            sys.argv[2], sys.argv[3], sys.argv[4], 
            sys.argv[5], sys.argv[6]
        )
    
    elif command == "download":
        mailer.send_download_link(
            sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        )
    
    elif command == "welcome":
        mailer.send_welcome_email(sys.argv[2], sys.argv[3])
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

