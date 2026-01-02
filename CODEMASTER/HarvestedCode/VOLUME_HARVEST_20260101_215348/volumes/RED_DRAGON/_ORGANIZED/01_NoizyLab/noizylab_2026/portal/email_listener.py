#!/usr/bin/env python3
"""
Email Listener for NoizyFish Portal
Monitors info@noizyfish.com for client submissions
"""

import imaplib
import email
import time
import os
import json
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv(Path(__file__).parent.parent / '.env')

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EmailListener:
    """Monitors email inbox for client support requests"""
    
    def __init__(self):
        self.imap_host = os.getenv('IMAP_HOST', 'imap.gmail.com')
        self.imap_user = os.getenv('IMAP_USER', 'info@noizyfish.com')
        self.imap_pass = os.getenv('IMAP_PASS', '')
        self.mc_endpoint = os.getenv('MC_ENDPOINT', 'http://127.0.0.1:8765')
        self.uploads_dir = Path(__file__).parent / 'uploads'
        self.uploads_dir.mkdir(exist_ok=True)
        
        # IMAP connection
        self.imap = None
        self.running = False
        
    def connect(self):
        """Connect to IMAP server"""
        try:
            logger.info(f"Connecting to {self.imap_host} as {self.imap_user}")
            self.imap = imaplib.IMAP4_SSL(self.imap_host)
            self.imap.login(self.imap_user, self.imap_pass)
            self.imap.select('INBOX')
            logger.info("IMAP connection established")
            return True
        except Exception as e:
            logger.error(f"IMAP connection failed: {e}")
            return False
            
    def disconnect(self):
        """Disconnect from IMAP server"""
        if self.imap:
            try:
                self.imap.logout()
                logger.info("IMAP disconnected")
            except:
                pass
                
    def process_email(self, email_msg):
        """Process a single email message"""
        try:
            # Extract basic info
            subject = email_msg.get('Subject', 'No Subject')
            from_addr = email_msg.get('From', 'Unknown')
            date = email_msg.get('Date', '')
            
            logger.info(f"Processing email: {subject} from {from_addr}")
            
            # Extract client name from email
            client_name = from_addr.split('<')[0].strip()
            if not client_name:
                client_name = from_addr.split('@')[0]
                
            # Extract text content
            text_content = ""
            attachments = []
            
            if email_msg.is_multipart():
                for part in email_msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get('Content-Disposition', ''))
                    
                    if content_type == 'text/plain' and 'attachment' not in content_disposition:
                        text_content += part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    elif 'attachment' in content_disposition:
                        # Save attachment
                        filename = part.get_filename()
                        if filename:
                            filepath = self.uploads_dir / f"{int(time.time())}_{filename}"
                            with open(filepath, 'wb') as f:
                                f.write(part.get_payload(decode=True))
                            attachments.append(str(filepath))
                            logger.info(f"Saved attachment: {filename}")
            else:
                text_content = email_msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                
            # Create support request data
            support_data = {
                'client': client_name,
                'email': from_addr,
                'subject': subject,
                'description': text_content.strip(),
                'attachments': attachments,
                'timestamp': time.time(),
                'source': 'email'
            }
            
            # Send to Mission Control
            self.send_to_mission_control(support_data)
            
            # Generate response email
            self.send_auto_response(from_addr, client_name, support_data)
            
        except Exception as e:
            logger.error(f"Error processing email: {e}")
            
    def send_to_mission_control(self, data):
        """Send support data to Mission Control"""
        try:
            response = requests.post(
                f"{self.mc_endpoint}/publish",
                json={
                    "topic": "client_intake",
                    "payload": data
                },
                timeout=5
            )
            if response.status_code == 200:
                logger.info("Support data sent to Mission Control")
            else:
                logger.warning(f"Mission Control responded with {response.status_code}")
        except Exception as e:
            logger.error(f"Failed to send to Mission Control: {e}")
            
    def send_auto_response(self, to_email, client_name, data):
        """Send automated response to client"""
        try:
            # This would integrate with your email sending system
            logger.info(f"Auto-response sent to {to_email}")
            
            # For now, just log what we would send
            response_text = f"""
            Hello {client_name},
            
            Thank you for contacting NoizyFish support. We have received your request:
            
            Subject: {data.get('subject', 'Support Request')}
            Description: {data.get('description', 'No description provided')[:100]}...
            
            Our AI system is analyzing your request and will provide a detailed response shortly.
            
            Best regards,
            NoizyFish Support Team
            """
            
            logger.info(f"Would send response: {response_text[:100]}...")
            
        except Exception as e:
            logger.error(f"Failed to send auto-response: {e}")
            
    def check_new_emails(self):
        """Check for new emails"""
        try:
            # Search for unseen emails
            status, messages = self.imap.search(None, 'UNSEEN')
            
            if status == 'OK' and messages[0]:
                email_ids = messages[0].split()
                logger.info(f"Found {len(email_ids)} new emails")
                
                for email_id in email_ids:
                    # Fetch email
                    status, msg_data = self.imap.fetch(email_id, '(RFC822)')
                    
                    if status == 'OK':
                        email_msg = email.message_from_bytes(msg_data[0][1])
                        self.process_email(email_msg)
                        
                        # Mark as read
                        self.imap.store(email_id, '+FLAGS', '\\Seen')
                        
        except Exception as e:
            logger.error(f"Error checking emails: {e}")
            
    def run(self):
        """Main run loop"""
        logger.info("🐟 Starting NoizyFish Email Listener...")
        
        if not self.connect():
            logger.error("Failed to connect to email server")
            return
            
        self.running = True
        
        try:
            while self.running:
                self.check_new_emails()
                time.sleep(30)  # Check every 30 seconds
                
        except KeyboardInterrupt:
            logger.info("Received interrupt signal")
        finally:
            self.running = False
            self.disconnect()
            logger.info("Email listener stopped")


def main():
    """Main entry point"""
    listener = EmailListener()
    
    try:
        listener.run()
    except Exception as e:
        logger.error(f"Email listener error: {e}")


if __name__ == "__main__":
    main()