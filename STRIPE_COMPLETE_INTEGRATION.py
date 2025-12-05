#!/usr/bin/env python3
"""
💳 STRIPE COMPLETE INTEGRATION - FULL PAYMENT SYSTEM
Accept payments, create payment links, manage subscriptions
COMPLETE SYSTEM - NO HALF MEASURES!!
"""

import stripe
import json
import os
from datetime import datetime

class StripePayments:
    """Complete Stripe payment integration"""
    
    def __init__(self, api_key=None):
        self.config_file = "stripe_config.json"
        
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = self.load_api_key()
        
        if self.api_key:
            stripe.api_key = self.api_key
            print("💳 Stripe initialized")
        else:
            print("⚠️  Stripe API key not configured")
    
    def load_api_key(self):
        """Load Stripe API key"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                return config.get('api_key')
        return None
    
    def save_api_key(self, api_key):
        """Save Stripe API key"""
        config = {
            'api_key': api_key,
            'configured': datetime.now().isoformat()
        }
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        self.api_key = api_key
        stripe.api_key = api_key
    
    # PAYMENT LINKS
    
    def create_payment_link(self, amount, description, client_email):
        """Create Stripe payment link"""
        try:
            # Create product
            product = stripe.Product.create(
                name=description[:100],
                description=description
            )
            
            # Create price
            price = stripe.Price.create(
                product=product.id,
                unit_amount=int(amount * 100),  # Convert to cents
                currency='cad'
            )
            
            # Create payment link
            payment_link = stripe.PaymentLink.create(
                line_items=[{
                    'price': price.id,
                    'quantity': 1
                }],
                after_completion={
                    'type': 'redirect',
                    'redirect': {'url': 'https://noizylab.ca/thank-you'}
                },
                customer_creation='always',
                metadata={'client_email': client_email}
            )
            
            print(f"✅ Payment link created: {payment_link.url}")
            
            return {
                'success': True,
                'url': payment_link.url,
                'id': payment_link.id
            }
            
        except Exception as e:
            print(f"❌ Error creating payment link: {e}")
            return {'success': False, 'error': str(e)}
    
    # INVOICES
    
    def create_invoice(self, customer_email, customer_name, amount, description, due_days=30):
        """Create Stripe invoice"""
        try:
            # Create or get customer
            customers = stripe.Customer.list(email=customer_email, limit=1)
            
            if customers.data:
                customer = customers.data[0]
            else:
                customer = stripe.Customer.create(
                    email=customer_email,
                    name=customer_name,
                    metadata={'source': 'noizylab_portal'}
                )
            
            # Create invoice
            invoice = stripe.Invoice.create(
                customer=customer.id,
                description=description,
                collection_method='send_invoice',
                days_until_due=due_days,
                metadata={'portal': 'noizylab'}
            )
            
            # Add line item
            stripe.InvoiceItem.create(
                customer=customer.id,
                invoice=invoice.id,
                amount=int(amount * 100),
                currency='cad',
                description=description
            )
            
            # Finalize and send
            invoice = stripe.Invoice.finalize_invoice(invoice.id)
            stripe.Invoice.send_invoice(invoice.id)
            
            print(f"✅ Invoice created and sent: {invoice.id}")
            
            return {
                'success': True,
                'invoice_id': invoice.id,
                'invoice_url': invoice.hosted_invoice_url,
                'invoice_pdf': invoice.invoice_pdf
            }
            
        except Exception as e:
            print(f"❌ Error creating invoice: {e}")
            return {'success': False, 'error': str(e)}
    
    # CHECKOUT SESSIONS
    
    def create_checkout_session(self, price_amount, success_url, cancel_url, customer_email=None):
        """Create Stripe Checkout session"""
        try:
            params = {
                'payment_method_types': ['card'],
                'line_items': [{
                    'price_data': {
                        'currency': 'cad',
                        'product_data': {
                            'name': 'NoizyLab Services'
                        },
                        'unit_amount': int(price_amount * 100)
                    },
                    'quantity': 1
                }],
                'mode': 'payment',
                'success_url': success_url,
                'cancel_url': cancel_url
            }
            
            if customer_email:
                params['customer_email'] = customer_email
            
            session = stripe.checkout.Session.create(**params)
            
            return {
                'success': True,
                'session_id': session.id,
                'url': session.url
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    # PAYMENT INTENTS (CUSTOM CHECKOUT)
    
    def create_payment_intent(self, amount, currency='cad', customer_email=None):
        """Create payment intent for custom checkout"""
        try:
            params = {
                'amount': int(amount * 100),
                'currency': currency,
                'payment_method_types': ['card']
            }
            
            if customer_email:
                params['receipt_email'] = customer_email
            
            intent = stripe.PaymentIntent.create(**params)
            
            return {
                'success': True,
                'client_secret': intent.client_secret,
                'intent_id': intent.id
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    # WEBHOOK HANDLING
    
    def verify_webhook(self, payload, sig_header, webhook_secret):
        """Verify and process Stripe webhook"""
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
            
            return {'success': True, 'event': event}
            
        except Exception as e:
            return {'success': False, 'error': str(e)}

# CLI INTERFACE
if __name__ == "__main__":
    import sys
    
    print("💳 STRIPE COMPLETE INTEGRATION")
    print("=" * 60)
    print()
    
    sp = StripePayments()
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  Setup Stripe API key:
    python3 STRIPE_COMPLETE_INTEGRATION.py setup sk_test_...
  
  Create payment link:
    python3 STRIPE_COMPLETE_INTEGRATION.py payment-link 150.00 "Services" client@email.com
  
  Create invoice:
    python3 STRIPE_COMPLETE_INTEGRATION.py invoice client@email.com "Client Name" 1500.00 "Description"
  
  Create checkout session:
    python3 STRIPE_COMPLETE_INTEGRATION.py checkout 500.00 https://success https://cancel

GET STRIPE API KEY:
  1. Sign up: https://dashboard.stripe.com/register
  2. Get API keys: https://dashboard.stripe.com/apikeys
  3. Use TEST key (starts with sk_test_) for now
  4. Use LIVE key (starts with sk_live_) in production
        """)
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "setup":
        api_key = sys.argv[2]
        sp.save_api_key(api_key)
        print("✅ Stripe API key saved!")
    
    elif command == "payment-link":
        amount = float(sys.argv[2])
        description = sys.argv[3]
        email = sys.argv[4]
        
        result = sp.create_payment_link(amount, description, email)
        
        if result['success']:
            print(f"✅ Payment link created!")
            print(f"   URL: {result['url']}")
            print(f"   Send this to client!")
        else:
            print(f"❌ Error: {result['error']}")
    
    elif command == "invoice":
        email = sys.argv[2]
        name = sys.argv[3]
        amount = float(sys.argv[4])
        description = sys.argv[5]
        
        result = sp.create_invoice(email, name, amount, description)
        
        if result['success']:
            print(f"✅ Invoice created!")
            print(f"   Invoice URL: {result['invoice_url']}")
            print(f"   PDF: {result['invoice_pdf']}")
        else:
            print(f"❌ Error: {result['error']}")
    
    elif command == "checkout":
        amount = float(sys.argv[2])
        success_url = sys.argv[3]
        cancel_url = sys.argv[4]
        
        result = sp.create_checkout_session(amount, success_url, cancel_url)
        
        if result['success']:
            print(f"✅ Checkout session created!")
            print(f"   URL: {result['url']}")
        else:
            print(f"❌ Error: {result['error']}")
    
    else:
        print(f"❌ Unknown command: {command}")

