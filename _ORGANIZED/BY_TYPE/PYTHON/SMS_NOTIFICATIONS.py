#!/usr/bin/env python3
"""
📱 SMS NOTIFICATIONS - TWILIO INTEGRATION
Send SMS for urgent RESCUE requests, confirmations, reminders
Faster than email for time-sensitive issues!
FREE trial: $15 credit (100+ SMS), then pay-as-you-go
"""

from twilio.rest import Client
import os
import json
from datetime import datetime

class SMSNotifications:
    """Complete SMS notification system via Twilio"""
    
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.from_number = os.getenv('TWILIO_PHONE_NUMBER')  # e.g., +15551234567
        
        if self.account_sid and self.auth_token:
            self.client = Client(self.account_sid, self.auth_token)
            print("📱 Twilio SMS: CONNECTED")
        else:
            self.client = None
            print("⚠️  Twilio not configured")
    
    def send_sms(self, to_number, message):
        """Send SMS via Twilio"""
        
        if not self.client:
            print("⚠️  SMS not configured - would send:")
            print(f"   To: {to_number}")
            print(f"   Message: {message}")
            return False
        
        try:
            msg = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            
            print(f"✅ SMS sent to {to_number}")
            print(f"   SID: {msg.sid}")
            
            self.log_sms(to_number, message, 'sent', msg.sid)
            
            return True
            
        except Exception as e:
            print(f"❌ SMS failed: {e}")
            self.log_sms(to_number, message, 'failed', None, str(e))
            return False
    
    # ========== RESCUE NOTIFICATIONS ==========
    
    def notify_rescue_received(self, client_name, client_phone, rescue_id):
        """Notify client their rescue request was received"""
        
        message = f"NoizyLab RESCUE: Request {rescue_id} received! I'll contact you within 1-2 hours. -Rob"
        
        return self.send_sms(client_phone, message)
    
    def notify_rescue_ready_for_teamviewer(self, client_phone):
        """Notify client you're ready to connect"""
        
        message = "NoizyLab: Ready to connect! Please have TeamViewer open. I'll connect in 5 minutes. -Rob"
        
        return self.send_sms(client_phone, message)
    
    def notify_rescue_complete(self, client_phone, outcome, amount=None):
        """Notify client of session outcome"""
        
        if outcome == 'fixed':
            message = f"NoizyLab: Issue FIXED! ✅ Payment link sent to email. Min $89, pay more if you want! -Rob"
        elif outcome == 'partially_fixed':
            message = "NoizyLab: Issue partially resolved. Payment optional based on your satisfaction. Details emailed. -Rob"
        elif outcome == 'hardware_needed':
            message = "NoizyLab: Hardware repair needed. NO CHARGE for diagnosis. Apple Store recommended. Details emailed. -Rob"
        else:
            message = "NoizyLab: Unfortunately couldn't fix remotely. NO CHARGE. Details emailed. -Rob"
        
        return self.send_sms(client_phone, message)
    
    # ========== PAYMENT REMINDERS ==========
    
    def send_payment_reminder(self, client_phone, invoice_number, amount):
        """Send gentle payment reminder"""
        
        message = f"NoizyLab: Friendly reminder - Invoice {invoice_number} for ${amount:.2f} is due. Payment link in email. Thanks! -Rob"
        
        return self.send_sms(client_phone, message)
    
    # ========== YOU (ROB) NOTIFICATIONS ==========
    
    def notify_you_new_rescue(self, client_name, issue, rescue_id):
        """Notify YOU of new rescue request"""
        
        your_phone = os.getenv('ROB_PHONE_NUMBER')  # Your phone number
        
        if your_phone:
            message = f"🚨 NEW RESCUE: {client_name} - {issue} - ID: {rescue_id}"
            return self.send_sms(your_phone, message)
    
    def notify_you_payment_received(self, amount, client_name):
        """Notify YOU of payment"""
        
        your_phone = os.getenv('ROB_PHONE_NUMBER')
        
        if your_phone:
            message = f"💰 PAYMENT RECEIVED: ${amount:.2f} from {client_name}!"
            return self.send_sms(your_phone, message)
    
    # ========== LOGGING ==========
    
    def log_sms(self, to_number, message, status, sid=None, error=None):
        """Log SMS sends"""
        
        log_file = 'sms_log.json'
        
        log = []
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                log = json.load(f)
        
        log.append({
            'timestamp': datetime.now().isoformat(),
            'to': to_number,
            'message': message,
            'status': status,
            'sid': sid,
            'error': error
        })
        
        with open(log_file, 'w') as f:
            json.dump(log, f, indent=2)

if __name__ == "__main__":
    print("📱 SMS NOTIFICATIONS SYSTEM")
    print("=" * 60)
    print()
    print("TWILIO SMS INTEGRATION:")
    print()
    print("SETUP:")
    print("  1. Sign up: https://www.twilio.com/try-twilio")
    print("  2. Get FREE $15 credit (100+ SMS!)")
    print("  3. Get phone number ($1/month)")
    print("  4. Get Account SID & Auth Token")
    print("  5. Configure:")
    print("     export TWILIO_ACCOUNT_SID='your_sid'")
    print("     export TWILIO_AUTH_TOKEN='your_token'")
    print("     export TWILIO_PHONE_NUMBER='+15551234567'")
    print("     export ROB_PHONE_NUMBER='+15559999999'")
    print()
    print("FEATURES:")
    print("  ✅ Instant RESCUE notifications")
    print("  ✅ TeamViewer ready alerts")
    print("  ✅ Session complete notifications")
    print("  ✅ Payment reminders")
    print("  ✅ Alerts to YOU for new rescues")
    print("  ✅ Payment confirmations to YOU")
    print()
    print("USE CASES:")
    print("  • Client submits rescue → SMS: 'Received! Will contact soon'")
    print("  • You're ready to connect → SMS: 'Ready! Open TeamViewer'")
    print("  • Session done → SMS: 'Fixed! Payment link sent'")
    print("  • New rescue → SMS to YOU: 'New client waiting!'")
    print()
    print("COST:")
    print("  • FREE $15 credit (100+ SMS)")
    print("  • Then: $0.0075 per SMS (less than 1 cent!)")
    print("  • Phone number: $1/month")
    print()
    print("GORUNFREE!! 🚀")

