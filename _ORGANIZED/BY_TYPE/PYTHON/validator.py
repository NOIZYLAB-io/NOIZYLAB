#!/usr/bin/env python3
"""
Email Validator - Safety Checks
================================
"""

import re
from typing import Tuple, Optional
from rich.console import Console

console = Console()

class EmailValidator:
    """Email validation and safety checks"""
    
    EMAIL_REGEX = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, Optional[str]]:
        """Validate email format"""
        if not email or not email.strip():
            return False, "Email address is empty"
        
        email = email.strip()
        
        if not EmailValidator.EMAIL_REGEX.match(email):
            return False, "Invalid email format"
        
        return True, None
    
    @staticmethod
    def validate_subject(subject: str) -> Tuple[bool, Optional[str]]:
        """Validate email subject"""
        if not subject or not subject.strip():
            return False, "Subject is empty"
        
        if len(subject.strip()) < 3:
            return False, "Subject is too short (minimum 3 characters)"
        
        return True, None
    
    @staticmethod
    def validate_body(body: str) -> Tuple[bool, Optional[str]]:
        """Validate email body"""
        if not body or not body.strip():
            return False, "Email body is empty"
        
        if len(body.strip()) < 10:
            return False, "Email body is too short (minimum 10 characters)"
        
        return True, None
    
    @staticmethod
    def validate_email_data(to_email: str, subject: str, body: str) -> Tuple[bool, Optional[str]]:
        """Validate complete email data"""
        # Validate email
        valid, error = EmailValidator.validate_email(to_email)
        if not valid:
            return False, f"Recipient: {error}"
        
        # Validate subject
        valid, error = EmailValidator.validate_subject(subject)
        if not valid:
            return False, f"Subject: {error}"
        
        # Validate body
        valid, error = EmailValidator.validate_body(body)
        if not valid:
            return False, f"Body: {error}"
        
        return True, None

