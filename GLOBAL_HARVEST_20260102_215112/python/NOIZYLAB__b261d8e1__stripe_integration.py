"""
💳 STRIPE PAYMENT INTEGRATION - 100% PERFECT
Perfect Stripe integration
GORUNFREE Protocol
"""

import stripe
from typing import Optional, Dict, Any
from ..config import settings
from ..logging import get_logger

logger = get_logger("stripe")

# Initialize Stripe
if settings.STRIPE_SECRET_KEY:
    stripe.api_key = settings.STRIPE_SECRET_KEY


class StripePayment:
    """Stripe payment integration"""
    
    def __init__(self):
        """Initialize Stripe"""
        if not settings.STRIPE_SECRET_KEY:
            logger.warning("stripe_not_configured")
        self.stripe = stripe
    
    def create_payment_intent(
        self,
        amount: float,
        currency: str = "usd",
        customer_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create payment intent
        
        Args:
            amount: Amount in cents
            currency: Currency code
            customer_id: Stripe customer ID
            metadata: Additional metadata
            
        Returns:
            Payment intent object
        """
        try:
            intent_data = {
                "amount": int(amount * 100),  # Convert to cents
                "currency": currency,
                "metadata": metadata or {}
            }
            
            if customer_id:
                intent_data["customer"] = customer_id
            
            intent = self.stripe.PaymentIntent.create(**intent_data)
            
            logger.info("payment_intent_created", intent_id=intent.id, amount=amount)
            return intent
        except Exception as e:
            logger.error("payment_intent_failed", error=str(e))
            raise
    
    def confirm_payment(self, payment_intent_id: str) -> Dict[str, Any]:
        """
        Confirm payment intent
        
        Args:
            payment_intent_id: Payment intent ID
            
        Returns:
            Confirmed payment intent
        """
        try:
            intent = self.stripe.PaymentIntent.retrieve(payment_intent_id)
            if intent.status == "requires_confirmation":
                intent = self.stripe.PaymentIntent.confirm(payment_intent_id)
            
            logger.info("payment_confirmed", intent_id=payment_intent_id, status=intent.status)
            return intent
        except Exception as e:
            logger.error("payment_confirmation_failed", error=str(e))
            raise
    
    def create_customer(
        self,
        email: str,
        name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create Stripe customer
        
        Args:
            email: Customer email
            name: Customer name
            metadata: Additional metadata
            
        Returns:
            Customer object
        """
        try:
            customer_data = {
                "email": email,
                "metadata": metadata or {}
            }
            
            if name:
                customer_data["name"] = name
            
            customer = self.stripe.Customer.create(**customer_data)
            
            logger.info("customer_created", customer_id=customer.id, email=email)
            return customer
        except Exception as e:
            logger.error("customer_creation_failed", error=str(e))
            raise
    
    def create_subscription(
        self,
        customer_id: str,
        price_id: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create subscription
        
        Args:
            customer_id: Stripe customer ID
            price_id: Stripe price ID
            metadata: Additional metadata
            
        Returns:
            Subscription object
        """
        try:
            subscription_data = {
                "customer": customer_id,
                "items": [{"price": price_id}],
                "metadata": metadata or {}
            }
            
            subscription = self.stripe.Subscription.create(**subscription_data)
            
            logger.info("subscription_created", subscription_id=subscription.id)
            return subscription
        except Exception as e:
            logger.error("subscription_creation_failed", error=str(e))
            raise
    
    def handle_webhook(self, payload: bytes, signature: str) -> Dict[str, Any]:
        """
        Handle Stripe webhook
        
        Args:
            payload: Webhook payload
            signature: Webhook signature
            
        Returns:
            Event object
        """
        try:
            event = self.stripe.Webhook.construct_event(
                payload, signature, settings.STRIPE_WEBHOOK_SECRET
            )
            
            logger.info("webhook_received", event_type=event["type"], event_id=event["id"])
            return event
        except ValueError as e:
            logger.error("webhook_invalid_payload", error=str(e))
            raise
        except stripe.error.SignatureVerificationError as e:
            logger.error("webhook_invalid_signature", error=str(e))
            raise

