"""
📧 EMAIL SERVICE - 100% PERFECT
Perfect email service
GORUNFREE Protocol
"""

from typing import List, Optional, Dict, Any
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..config import settings
from ..logging import get_logger

logger = get_logger("email")


class EmailService:
    """Email service implementation"""
    
    def __init__(
        self,
        smtp_host: Optional[str] = None,
        smtp_port: int = 587,
        smtp_user: Optional[str] = None,
        smtp_password: Optional[str] = None
    ):
        """
        Initialize email service
        
        Args:
            smtp_host: SMTP host
            smtp_port: SMTP port
            smtp_user: SMTP username
            smtp_password: SMTP password
        """
        self.smtp_host = smtp_host or os.getenv("SMTP_HOST", "smtp.gmail.com")
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user or os.getenv("SMTP_USER")
        self.smtp_password = smtp_password or os.getenv("SMTP_PASSWORD")
        self.from_email = os.getenv("FROM_EMAIL", "noreply@gabriel.noizylab.com")
    
    def send_email(
        self,
        to_email: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None,
        attachments: Optional[List[str]] = None
    ) -> bool:
        """
        Send email
        
        Args:
            to_email: Recipient email
            subject: Email subject
            body: Plain text body
            html_body: HTML body (optional)
            attachments: List of file paths (optional)
            
        Returns:
            True if successful
        """
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Add plain text
            msg.attach(MIMEText(body, 'plain'))
            
            # Add HTML if provided
            if html_body:
                msg.attach(MIMEText(html_body, 'html'))
            
            # Send email
            if self.smtp_user and self.smtp_password:
                with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                    server.starttls()
                    server.login(self.smtp_user, self.smtp_password)
                    server.send_message(msg)
            else:
                logger.warning("email_not_configured", to_email=to_email)
                return False
            
            logger.info("email_sent", to_email=to_email, subject=subject)
            return True
        except Exception as e:
            logger.error("email_send_failed", to_email=to_email, error=str(e))
            return False


# Global email service instance
_email_service: Optional[EmailService] = None


def get_email_service() -> EmailService:
    """Get email service instance"""
    global _email_service
    if _email_service is None:
        _email_service = EmailService()
    return _email_service


def send_email(
    to_email: str,
    subject: str,
    body: str,
    html_body: Optional[str] = None
) -> bool:
    """
    Send email (convenience function)
    
    Args:
        to_email: Recipient email
        subject: Email subject
        body: Plain text body
        html_body: HTML body (optional)
        
    Returns:
        True if successful
    """
    service = get_email_service()
    return service.send_email(to_email, subject, body, html_body)


def send_welcome_email(to_email: str, name: str) -> bool:
    """
    Send welcome email
    
    Args:
        to_email: Recipient email
        name: User name
        
    Returns:
        True if successful
    """
    subject = "Welcome to GABRIEL!"
    body = f"Hi {name},\n\nWelcome to GABRIEL! We're excited to have you."
    html_body = f"""
    <html>
      <body>
        <h1>Welcome to GABRIEL, {name}!</h1>
        <p>We're excited to have you on board.</p>
      </body>
    </html>
    """
    return send_email(to_email, subject, body, html_body)


def send_verification_email(to_email: str, verification_code: str) -> bool:
    """
    Send verification email
    
    Args:
        to_email: Recipient email
        verification_code: Verification code
        
    Returns:
        True if successful
    """
    subject = "Verify your GABRIEL account"
    body = f"Your verification code is: {verification_code}"
    html_body = f"""
    <html>
      <body>
        <h1>Verify your account</h1>
        <p>Your verification code is: <strong>{verification_code}</strong></p>
      </body>
    </html>
    """
    return send_email(to_email, subject, body, html_body)

