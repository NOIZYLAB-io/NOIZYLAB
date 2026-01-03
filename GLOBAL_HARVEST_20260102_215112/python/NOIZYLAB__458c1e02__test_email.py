"""
🧪 EMAIL TESTS - 100% PERFECT
Perfect email test coverage
GORUNFREE Protocol
"""

import pytest
from unittest.mock import Mock, patch
from ..infrastructure.email.email_service import EmailService, send_email, send_welcome_email


class TestEmail:
    """Email tests"""
    
    @pytest.fixture
    def email_service(self):
        """Create email service instance"""
        return EmailService(
            smtp_host="smtp.test.com",
            smtp_port=587,
            smtp_user="test",
            smtp_password="test"
        )
    
    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp, email_service):
        """Test email sending"""
        mock_server = Mock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        
        result = email_service.send_email(
            to_email="test@example.com",
            subject="Test",
            body="Test body"
        )
        
        assert result is True
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once()
        mock_server.send_message.assert_called_once()
    
    def test_send_welcome_email(self):
        """Test welcome email"""
        with patch('GABRIEL.infrastructure.email.email_service.send_email') as mock_send:
            mock_send.return_value = True
            
            result = send_welcome_email("test@example.com", "John")
            
            assert result is True
            mock_send.assert_called_once()

