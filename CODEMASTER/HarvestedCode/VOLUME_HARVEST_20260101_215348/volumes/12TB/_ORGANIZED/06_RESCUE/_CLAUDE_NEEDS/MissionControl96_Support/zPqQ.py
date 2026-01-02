import smtplib
from email.message import EmailMessage
import time

# List of test addresses
addresses = [
    "rp@fishmusicinc.com",
    "info@fishmusicinc.com",
    "rsp@noizy.ai",
    "rsp@noizyfish.com"
]
# Destination inbox to verify forwarding
verify_inbox = "rsplowman@icloud.com"

# SMTP config (use a working account, e.g., Gmail, iCloud, etc.)
SMTP_SERVER = "smtp.mail.me.com"  # Example for iCloud
SMTP_PORT = 587
SMTP_USER = "rsplowman@icloud.com"
SMTP_PASS = "YOUR_APP_SPECIFIC_PASSWORD"

for addr in addresses:
    msg = EmailMessage()
    msg["Subject"] = f"MissionControl96 Forwarding Test: {addr}"
    msg["From"] = SMTP_USER
    msg["To"] = addr
    msg.set_content(f"This is a test to verify forwarding from {addr} to {verify_inbox}.")
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        print(f"✅ Test email sent to {addr}. Check {verify_inbox} for delivery.")
    except Exception as e:
        print(f"❌ Failed to send test email to {addr}: {e}")
    time.sleep(2)

print("Check your {verify_inbox} inbox for all test emails. If missing, forwarding is broken.")
