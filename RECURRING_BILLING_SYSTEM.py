#!/usr/bin/env python3
"""
💰 RECURRING BILLING & SUBSCRIPTION SYSTEM
Monthly support plans, auto-billing, subscription management
PREDICTABLE REVENUE - PASSIVE INCOME!!
"""

from flask import Flask, render_template_string, request, jsonify
import stripe
import json
import os
from datetime import datetime, timedelta
import sys

sys.path.append('../FishMusic_Email_System')
from MAIL_APP_COMPLETE_SYSTEM import MailAppMailer

app = Flask(__name__)
mailer = MailAppMailer()

SUBSCRIPTION_PLANS = {
    "basic": {
        "name": "Basic Support",
        "price": 49,
        "interval": "month",
        "features": [
            "Email support (24hr response)",
            "1 remote session per month",
            "Software troubleshooting",
            "Priority queue"
        ]
    },
    "pro": {
        "name": "Pro Support",
        "price": 99,
        "interval": "month",
        "features": [
            "Email support (4hr response)",
            "3 remote sessions per month",
            "Software + performance optimization",
            "Monthly health check",
            "Priority queue",
            "Phone support"
        ]
    },
    "premium": {
        "name": "Premium Care",
        "price": 199,
        "interval": "month",
        "features": [
            "Email support (1hr response)",
            "Unlimited remote sessions",
            "Complete Mac management",
            "Weekly health checks",
            "Priority queue",
            "Phone support",
            "Data backup management",
            "Software updates handled"
        ]
    }
}

SUBSCRIPTION_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>💰 NoizyLab Support Plans</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 40px 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        
        .header {
            text-align: center;
            margin-bottom: 60px;
        }
        .header h1 {
            color: #00ff88;
            font-size: 3.5rem;
            margin-bottom: 15px;
        }
        .header p {
            font-size: 1.3rem;
            color: #888;
        }
        
        .plans-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }
        
        .plan-card {
            background: rgba(255,255,255,0.03);
            border: 2px solid rgba(0,255,136,0.2);
            border-radius: 20px;
            padding: 40px;
            transition: all 0.3s;
            position: relative;
        }
        
        .plan-card:hover {
            border-color: #00ff88;
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,255,136,0.2);
        }
        
        .plan-card.featured {
            border-color: #00ff88;
            background: rgba(0,255,136,0.05);
        }
        
        .plan-card.featured::before {
            content: "MOST POPULAR";
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            background: #00ff88;
            color: #0f0f23;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }
        
        .plan-name {
            font-size: 1.8rem;
            color: #00ff88;
            margin-bottom: 20px;
        }
        
        .plan-price {
            font-size: 3.5rem;
            font-weight: bold;
            margin: 20px 0;
        }
        
        .plan-price .currency {
            font-size: 1.5rem;
            vertical-align: super;
        }
        
        .plan-price .period {
            font-size: 1.2rem;
            color: #888;
        }
        
        .plan-features {
            margin: 30px 0;
            list-style: none;
        }
        
        .plan-features li {
            padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            font-size: 1.05rem;
        }
        
        .plan-features li::before {
            content: "✅";
            margin-right: 10px;
        }
        
        .btn-subscribe {
            width: 100%;
            padding: 18px;
            background: #00ff88;
            color: #0f0f23;
            border: none;
            border-radius: 10px;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn-subscribe:hover {
            background: #00cc6a;
            transform: scale(1.05);
        }
        
        .guarantee {
            background: rgba(0,255,136,0.05);
            border: 2px solid #00ff88;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            margin: 60px 0;
        }
        
        .guarantee h2 {
            color: #00ff88;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💰 NoizyLab Support Plans</h1>
            <p>Ongoing Mac support - Cancel anytime!</p>
        </div>
        
        <div class="plans-grid">
            {% for plan_id, plan in plans.items() %}
            <div class="plan-card {{ 'featured' if plan_id == 'pro' else '' }}">
                <div class="plan-name">{{ plan.name }}</div>
                <div class="plan-price">
                    <span class="currency">$</span>{{ plan.price }}<span class="period">/mo</span>
                </div>
                
                <ul class="plan-features">
                    {% for feature in plan.features %}
                    <li>{{ feature }}</li>
                    {% endfor %}
                </ul>
                
                <button class="btn-subscribe" onclick="subscribe('{{ plan_id }}')">
                    Subscribe Now
                </button>
            </div>
            {% endfor %}
        </div>
        
        <div class="guarantee">
            <h2>✅ Satisfaction Guaranteed</h2>
            <p style="font-size: 1.2rem; line-height: 2;">
                Cancel anytime, no questions asked<br>
                First month satisfaction guaranteed<br>
                If not happy, full refund!
            </p>
        </div>
    </div>
    
    <script>
        async function subscribe(planId) {
            const email = prompt('Your email:');
            if (!email) return;
            
            try {
                const response = await fetch('/api/subscribe', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ plan: planId, email })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    window.location.href = result.checkout_url;
                } else {
                    alert('Error: ' + result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }
    </script>
</body>
</html>
"""

class RecurringBilling:
    """Subscription and recurring billing system"""
    
    def __init__(self):
        self.stripe_key = os.getenv('STRIPE_SECRET_KEY')
        if self.stripe_key:
            stripe.api_key = self.stripe_key
    
    def create_subscription(self, customer_email, plan_id):
        """Create Stripe subscription"""
        
        if not self.stripe_key:
            return {'success': False, 'error': 'Stripe not configured'}
        
        try:
            # Create or get customer
            customers = stripe.Customer.list(email=customer_email, limit=1)
            
            if customers.data:
                customer = customers.data[0]
            else:
                customer = stripe.Customer.create(
                    email=customer_email,
                    metadata={'source': 'noizylab'}
                )
            
            # Get plan details
            plan = SUBSCRIPTION_PLANS[plan_id]
            
            # Create price (if not exists)
            price = stripe.Price.create(
                unit_amount=int(plan['price'] * 100),
                currency='cad',
                recurring={'interval': plan['interval']},
                product_data={'name': plan['name']}
            )
            
            # Create checkout session for subscription
            session = stripe.checkout.Session.create(
                customer=customer.id,
                payment_method_types=['card'],
                line_items=[{
                    'price': price.id,
                    'quantity': 1
                }],
                mode='subscription',
                success_url='http://localhost:4000/subscription-success',
                cancel_url='http://localhost:4000/subscription-cancel'
            )
            
            return {
                'success': True,
                'checkout_url': session.url,
                'customer_id': customer.id
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}

@app.route('/')
def subscription_page():
    """Subscription plans page"""
    return render_template_string(SUBSCRIPTION_PAGE, plans=SUBSCRIPTION_PLANS)

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    """Create subscription"""
    data = request.json
    
    billing = RecurringBilling()
    result = billing.create_subscription(data['email'], data['plan'])
    
    return jsonify(result)

if __name__ == '__main__':
    print("💰 RECURRING BILLING SYSTEM")
    print("=" * 60)
    print()
    print("SUBSCRIPTION PLANS:")
    for plan_id, plan in SUBSCRIPTION_PLANS.items():
        print(f"\n  {plan['name']} - ${plan['price']}/month")
        for feature in plan['features']:
            print(f"    • {feature}")
    print()
    print("FEATURES:")
    print("  ✅ Stripe Subscriptions")
    print("  ✅ Auto-billing monthly")
    print("  ✅ Cancel anytime")
    print("  ✅ Satisfaction guarantee")
    print("  ✅ Multiple plan tiers")
    print()
    print("REVENUE MODEL:")
    print("  • Basic: $49/mo x 10 clients = $490/mo")
    print("  • Pro: $99/mo x 20 clients = $1,980/mo")
    print("  • Premium: $199/mo x 5 clients = $995/mo")
    print("  • TOTAL: $3,465/mo recurring!")
    print()
    print("🌐 Subscription Page: http://localhost:8600")
    print()
    print("GORUNFREE!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=8600, debug=True)

