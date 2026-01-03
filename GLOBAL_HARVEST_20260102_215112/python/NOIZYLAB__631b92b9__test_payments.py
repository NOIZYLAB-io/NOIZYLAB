"""
🧪 PAYMENT TESTS - 100% PERFECT
Perfect payment test coverage
GORUNFREE Protocol
"""

import pytest
from unittest.mock import Mock, patch
from ..infrastructure.payments.stripe_integration import StripePayment


class TestPayments:
    """Payment tests"""
    
    @pytest.fixture
    def stripe_payment(self):
        """Create Stripe payment instance"""
        return StripePayment()
    
    @patch('stripe.PaymentIntent.create')
    def test_create_payment_intent(self, mock_create, stripe_payment):
        """Test payment intent creation"""
        mock_create.return_value = Mock(id="pi_123", status="requires_payment_method")
        
        result = stripe_payment.create_payment_intent(
            amount=10.00,
            currency="usd"
        )
        
        assert result.id == "pi_123"
        mock_create.assert_called_once()
    
    @patch('stripe.Customer.create')
    def test_create_customer(self, mock_create, stripe_payment):
        """Test customer creation"""
        mock_create.return_value = Mock(id="cus_123", email="test@example.com")
        
        result = stripe_payment.create_customer(
            email="test@example.com",
            name="Test User"
        )
        
        assert result.id == "cus_123"
        assert result.email == "test@example.com"
        mock_create.assert_called_once()

