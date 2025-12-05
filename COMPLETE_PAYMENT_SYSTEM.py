#!/usr/bin/env python3
"""
💳 COMPLETE PAYMENT SYSTEM - STRIPE + APPLE PAY + PAYPAL
Accept payments through ALL methods - MAXIMUM CONVERSION!!
AUTOALLOW - NO STOPPING UNTIL COMPLETE!!
"""

from flask import Flask, render_template_string, request, jsonify
import stripe
import json
import os
from datetime import datetime
import requests

class CompletePaymentSystem:
    """All payment methods in one system"""
    
    def __init__(self):
        self.load_config()
        
        if self.config.get('stripe_key'):
            stripe.api_key = self.config['stripe_key']
            print("💳 Stripe: READY")
        
        if self.config.get('paypal_client_id'):
            print("💙 PayPal: READY")
        
        print("🍎 Apple Pay: READY (via Stripe)")
    
    def load_config(self):
        """Load payment configuration"""
        if os.path.exists('payment_config.json'):
            with open('payment_config.json', 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                'stripe_key': None,
                'stripe_publishable_key': None,
                'paypal_client_id': None,
                'paypal_secret': None,
                'paypal_email': 'rsp@noizyfish.com'
            }
            self.save_config()
    
    def save_config(self):
        """Save configuration"""
        with open('payment_config.json', 'w') as f:
            json.dump(self.config, f, indent=2)
    
    # STRIPE CHECKOUT (INCLUDES APPLE PAY!)
    
    def create_stripe_checkout(self, amount, description, success_url, cancel_url, customer_email=None):
        """
        Create Stripe checkout session
        INCLUDES Apple Pay automatically if on Safari/iOS!
        """
        try:
            params = {
                'payment_method_types': ['card'],  # Apple Pay auto-enabled on Safari!
                'line_items': [{
                    'price_data': {
                        'currency': 'cad',
                        'product_data': {
                            'name': description,
                            'description': 'NoizyLab Services'
                        },
                        'unit_amount': int(amount * 100)
                    },
                    'quantity': 1
                }],
                'mode': 'payment',
                'success_url': success_url,
                'cancel_url': cancel_url,
                'billing_address_collection': 'auto'
            }
            
            if customer_email:
                params['customer_email'] = customer_email
            
            session = stripe.checkout.Session.create(**params)
            
            print(f"✅ Stripe checkout created: {session.id}")
            print(f"   Apple Pay: Auto-enabled on Safari!")
            
            return {
                'success': True,
                'session_id': session.id,
                'url': session.url
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    # STRIPE PAYMENT INTENT (CUSTOM CHECKOUT WITH APPLE PAY)
    
    def create_payment_intent(self, amount, currency='cad', description=None):
        """
        Create payment intent - use with Stripe.js for Apple Pay button
        """
        try:
            params = {
                'amount': int(amount * 100),
                'currency': currency,
                'payment_method_types': ['card'],  # Stripe auto-enables Apple Pay!
                'statement_descriptor_suffix': 'NOIZYLAB'
            }
            
            if description:
                params['description'] = description
            
            intent = stripe.PaymentIntent.create(**params)
            
            return {
                'success': True,
                'client_secret': intent.client_secret,
                'intent_id': intent.id
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    # PAYPAL INTEGRATION
    
    def create_paypal_order(self, amount, description, return_url, cancel_url):
        """Create PayPal order"""
        if not self.config.get('paypal_client_id'):
            return {'success': False, 'error': 'PayPal not configured'}
        
        try:
            # Get PayPal access token
            token_url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"  # Use api-m.paypal.com for production
            
            auth = (self.config['paypal_client_id'], self.config['paypal_secret'])
            headers = {'Accept': 'application/json', 'Accept-Language': 'en_US'}
            data = {'grant_type': 'client_credentials'}
            
            token_response = requests.post(token_url, headers=headers, data=data, auth=auth)
            access_token = token_response.json()['access_token']
            
            # Create order
            order_url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
            
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }
            
            order_data = {
                'intent': 'CAPTURE',
                'purchase_units': [{
                    'amount': {
                        'currency_code': 'CAD',
                        'value': f'{amount:.2f}'
                    },
                    'description': description
                }],
                'application_context': {
                    'return_url': return_url,
                    'cancel_url': cancel_url,
                    'brand_name': 'NoizyLab',
                    'user_action': 'PAY_NOW'
                }
            }
            
            order_response = requests.post(order_url, headers=headers, json=order_data)
            order = order_response.json()
            
            # Get approval URL
            approval_url = next(
                (link['href'] for link in order['links'] if link['rel'] == 'approve'),
                None
            )
            
            print(f"✅ PayPal order created: {order['id']}")
            
            return {
                'success': True,
                'order_id': order['id'],
                'approval_url': approval_url
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    # SIMPLE PAYPAL EMAIL LINK
    
    def get_paypal_payment_link(self, amount, description):
        """Generate PayPal.me link (EASIEST!)"""
        paypal_email = self.config.get('paypal_email', 'rsp@noizyfish.com')
        
        # PayPal.me link (if you have it setup)
        # Format: https://paypal.me/yourusername/amount
        
        # For now, return standard PayPal link
        link = f"https://www.paypal.com/paypalme/noizyfish/{amount:.2f}CAD"
        
        print(f"💙 PayPal link: {link}")
        
        return {
            'success': True,
            'url': link,
            'email': paypal_email,
            'method': 'PayPal'
        }
    
    # APPLE PAY PAYMENT REQUEST
    
    def get_apple_pay_config(self, amount, label):
        """Get Apple Pay configuration for frontend"""
        return {
            'country': 'CA',
            'currency': 'cad',
            'total': {
                'label': label,
                'amount': amount
            },
            'requestPayerName': True,
            'requestPayerEmail': True
        }

# COMPLETE CHECKOUT PAGE WITH ALL PAYMENT METHODS
COMPLETE_CHECKOUT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💳 Payment - NoizyLab</title>
    <script src="https://js.stripe.com/v3/"></script>
    <script src="https://www.paypal.com/sdk/js?client-id=YOUR_PAYPAL_CLIENT_ID&currency=CAD"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .checkout-container {
            max-width: 600px;
            width: 100%;
        }
        
        .checkout-box {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 20px;
            padding: 40px;
        }
        
        h1 {
            color: #00ff88;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5rem;
        }
        
        .amount-display {
            text-align: center;
            font-size: 4rem;
            font-weight: bold;
            color: #fff;
            margin: 20px 0;
        }
        
        .description {
            text-align: center;
            color: #888;
            margin-bottom: 40px;
            font-size: 1.1rem;
        }
        
        .payment-methods {
            margin: 30px 0;
        }
        
        .payment-methods h2 {
            color: #00ff88;
            margin-bottom: 20px;
            font-size: 1.3rem;
        }
        
        .payment-button {
            width: 100%;
            padding: 20px;
            margin: 12px 0;
            border: none;
            border-radius: 12px;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .btn-apple-pay {
            background: #000;
            color: #fff;
            border: 1px solid #fff;
        }
        
        .btn-apple-pay:hover {
            background: #1a1a1a;
            transform: scale(1.02);
        }
        
        .btn-stripe {
            background: #635bff;
            color: #fff;
        }
        
        .btn-stripe:hover {
            background: #5348e8;
            transform: scale(1.02);
        }
        
        .btn-paypal {
            background: #0070ba;
            color: #fff;
        }
        
        .btn-paypal:hover {
            background: #005ea6;
            transform: scale(1.02);
        }
        
        .divider {
            text-align: center;
            margin: 25px 0;
            color: #666;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="checkout-container">
        <div class="checkout-box">
            <h1>💳 Payment</h1>
            
            <div class="amount-display">
                ${{ amount }}
            </div>
            
            <div class="description">
                {{ description }}
            </div>
            
            <div class="payment-methods">
                <h2>Choose Payment Method:</h2>
                
                <!-- APPLE PAY -->
                <button class="payment-button btn-apple-pay" id="applePay Button" onclick="payWithApplePay()">
                    🍎 Pay with Apple Pay
                </button>
                
                <div class="divider">OR</div>
                
                <!-- STRIPE (CREDIT CARD) -->
                <button class="payment-button btn-stripe" onclick="payWithStripe()">
                    💳 Pay with Card (Stripe)
                </button>
                
                <div class="divider">OR</div>
                
                <!-- PAYPAL -->
                <div id="paypal-button-container"></div>
                <button class="payment-button btn-paypal" onclick="payWithPayPal()">
                    💙 Pay with PayPal
                </button>
            </div>
            
            <div style="text-align: center; margin-top: 30px; color: #888; font-size: 0.9rem;">
                <p>🔒 Secure payment processing</p>
                <p style="margin-top: 5px;">All methods are safe and encrypted</p>
            </div>
        </div>
    </div>
    
    <script>
        const stripe = Stripe('{{ stripe_publishable_key }}');
        
        // APPLE PAY
        async function payWithApplePay() {
            if (!window.ApplePaySession || !ApplePaySession.canMakePayments()) {
                alert('Apple Pay is not available on this device. Use Card or PayPal instead.');
                return;
            }
            
            try {
                // Create payment intent
                const response = await fetch('/api/create-payment-intent', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        amount: {{ amount }},
                        method: 'apple_pay'
                    })
                });
                
                const { clientSecret } = await response.json();
                
                // Use Stripe's Apple Pay
                const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        type: 'card',
                        // Apple Pay automatically appears on Safari
                    }
                });
                
                if (error) {
                    alert('Payment failed: ' + error.message);
                } else {
                    window.location.href = '/payment-success?id=' + paymentIntent.id;
                }
                
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }
        
        // STRIPE CREDIT CARD
        async function payWithStripe() {
            try {
                const response = await fetch('/api/create-checkout-session', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        amount: {{ amount }},
                        description: '{{ description }}'
                    })
                });
                
                const { sessionId } = await response.json();
                
                // Redirect to Stripe Checkout
                const result = await stripe.redirectToCheckout({ sessionId });
                
                if (result.error) {
                    alert(result.error.message);
                }
                
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }
        
        // PAYPAL
        function payWithPayPal() {
            // Redirect to PayPal.me or use PayPal button
            window.location.href = 'https://www.paypal.com/paypalme/noizyfish/{{ amount }}CAD';
        }
        
        // Initialize PayPal button
        if (typeof paypal !== 'undefined') {
            paypal.Buttons({
                createOrder: function(data, actions) {
                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: '{{ amount }}',
                                currency_code: 'CAD'
                            },
                            description: '{{ description }}'
                        }]
                    });
                },
                onApprove: function(data, actions) {
                    return actions.order.capture().then(function(details) {
                        window.location.href = '/payment-success?paypal_order=' + data.orderID;
                    });
                },
                onError: function(err) {
                    alert('PayPal error: ' + err);
                }
            }).render('#paypal-button-container');
        }
    </script>
</body>
</html>
"""

# PAYMENT BUTTON GENERATOR
PAYMENT_BUTTONS_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>💳 Payment Options</title>
    <script src="https://js.stripe.com/v3/"></script>
    <style>
        .payment-buttons {
            max-width: 400px;
            margin: 0 auto;
        }
        
        .pay-btn {
            width: 100%;
            padding: 18px;
            margin: 10px 0;
            border: none;
            border-radius: 10px;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .apple-pay {
            background: #000;
            color: #fff;
            border: 1px solid #fff;
        }
        
        .stripe-pay {
            background: #635bff;
            color: #fff;
        }
        
        .paypal-pay {
            background: #0070ba;
            color: #fff;
        }
        
        .pay-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body style="background: #0f0f23; color: #fff; padding: 40px; font-family: Arial;">
    <div class="payment-buttons">
        <h2 style="text-align: center; color: #00ff88; margin-bottom: 30px;">
            💳 Choose Payment Method
        </h2>
        
        <button class="pay-btn apple-pay" onclick="payApple()">
            🍎 Apple Pay
        </button>
        
        <button class="pay-btn stripe-pay" onclick="payStripe()">
            💳 Credit Card
        </button>
        
        <button class="pay-btn paypal-pay" onclick="payPayPal()">
            💙 PayPal
        </button>
        
        <p style="text-align: center; margin-top: 30px; color: #888;">
            Amount: <strong style="color: #00ff88; font-size: 1.5rem;">${{ amount }} CAD</strong>
        </p>
    </div>
    
    <script>
        function payApple() {
            alert('Apple Pay: Opens on Safari/iOS automatically via Stripe!');
            payStripe(); // Same checkout, Apple Pay appears on Safari
        }
        
        function payStripe() {
            window.location.href = '/checkout/stripe?amount={{ amount }}&desc={{ description }}';
        }
        
        function payPayPal() {
            window.location.href = 'https://www.paypal.com/paypalme/noizyfish/{{ amount }}';
        }
    </script>
</body>
</html>
"""

# CLI INTERFACE
if __name__ == "__main__":
    import sys
    
    print("💳 COMPLETE PAYMENT SYSTEM")
    print("=" * 60)
    print()
    
    payments = CompletePaymentSystem()
    
    if len(sys.argv) < 2:
        print("""
COMPLETE PAYMENT SYSTEM - ALL METHODS!!

SETUP:
  Configure Stripe:
    python3 COMPLETE_PAYMENT_SYSTEM.py setup-stripe sk_test_... pk_test_...
  
  Configure PayPal:
    python3 COMPLETE_PAYMENT_SYSTEM.py setup-paypal client_id secret

CREATE PAYMENTS:
  Stripe checkout (includes Apple Pay!):
    python3 COMPLETE_PAYMENT_SYSTEM.py stripe-checkout 150.00 "Services"
  
  PayPal link:
    python3 COMPLETE_PAYMENT_SYSTEM.py paypal-link 150.00 "Services"
  
  Payment intent (custom):
    python3 COMPLETE_PAYMENT_SYSTEM.py payment-intent 150.00

FEATURES:
  ✅ Stripe Checkout (credit cards)
  ✅ Apple Pay (auto-enabled via Stripe on Safari!)
  ✅ PayPal (direct integration)
  ✅ All payment methods on one page
  ✅ Maximum conversion rate

GET API KEYS:
  Stripe: https://dashboard.stripe.com/apikeys
  PayPal: https://developer.paypal.com/dashboard/applications
        """)
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "setup-stripe":
        secret_key = sys.argv[2]
        publishable_key = sys.argv[3]
        
        payments.config['stripe_key'] = secret_key
        payments.config['stripe_publishable_key'] = publishable_key
        payments.save_config()
        
        print("✅ Stripe configured!")
        print(f"   Secret key: {secret_key[:20]}...")
        print(f"   Publishable key: {publishable_key[:20]}...")
    
    elif command == "setup-paypal":
        client_id = sys.argv[2]
        secret = sys.argv[3]
        
        payments.config['paypal_client_id'] = client_id
        payments.config['paypal_secret'] = secret
        payments.save_config()
        
        print("✅ PayPal configured!")
    
    elif command == "stripe-checkout":
        amount = float(sys.argv[2])
        description = sys.argv[3]
        
        result = payments.create_stripe_checkout(
            amount, description,
            'http://localhost:4000/success',
            'http://localhost:4000/cancel'
        )
        
        if result['success']:
            print(f"✅ Checkout created!")
            print(f"   URL: {result['url']}")
            print(f"   🍎 Apple Pay auto-enabled on Safari!")
        else:
            print(f"❌ Error: {result['error']}")
    
    elif command == "paypal-link":
        amount = float(sys.argv[2])
        description = sys.argv[3]
        
        result = payments.get_paypal_payment_link(amount, description)
        
        print(f"💙 PayPal link:")
        print(f"   {result['url']}")
        print(f"   Send this to client!")
    
    elif command == "payment-intent":
        amount = float(sys.argv[2])
        
        result = payments.create_payment_intent(amount)
        
        if result['success']:
            print(f"✅ Payment intent created!")
            print(f"   Client secret: {result['client_secret'][:50]}...")
        else:
            print(f"❌ Error: {result['error']}")
    
    else:
        print(f"❌ Unknown command: {command}")

