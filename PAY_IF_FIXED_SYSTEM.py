#!/usr/bin/env python3
"""
💼 "PAY ONLY IF I FIX IT" - RESULTS-BASED PRICING
$89 minimum if fixed, MORE if they want, NOTHING if not fixed
CONFIDENCE IN YOUR WORK - PROFESSIONAL & FAIR!!
"""

from flask import Flask, render_template_string, request, jsonify, redirect, session
import json
import os
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# CLIENT SATISFACTION PAGE
CLIENT_PAYMENT_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💼 NoizyLab - Fair Pricing</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro', Arial, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 100%);
            color: #fff;
            padding: 40px 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 700px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .header h1 {
            color: #00ff88;
            font-size: 3rem;
            margin-bottom: 15px;
        }
        
        .guarantee-box {
            background: linear-gradient(135deg, #00ff88 0%, #00cc6a 100%);
            color: #0f0f23;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 40px;
        }
        
        .guarantee-box h2 {
            font-size: 2rem;
            margin-bottom: 15px;
        }
        
        .guarantee-box p {
            font-size: 1.3rem;
            font-weight: 500;
        }
        
        .pricing-card {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 15px;
            padding: 40px;
            margin-bottom: 30px;
        }
        
        .pricing-card h2 {
            color: #00ff88;
            margin-bottom: 20px;
            font-size: 1.8rem;
        }
        
        .price-options {
            margin: 30px 0;
        }
        
        .price-btn {
            width: 100%;
            padding: 25px;
            margin: 15px 0;
            background: rgba(0,113,227,0.1);
            border: 2px solid #0071e3;
            border-radius: 12px;
            color: #fff;
            font-size: 1.3rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .price-btn:hover {
            background: rgba(0,113,227,0.2);
            border-color: #00ff88;
            transform: scale(1.02);
        }
        
        .price-btn.selected {
            background: rgba(0,255,136,0.1);
            border-color: #00ff88;
        }
        
        .custom-amount {
            margin-top: 20px;
        }
        
        .custom-amount input {
            width: 100%;
            padding: 20px;
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 10px;
            color: #fff;
            font-size: 1.5rem;
            text-align: center;
        }
        
        .payment-methods {
            margin-top: 40px;
        }
        
        .payment-methods h3 {
            color: #00ff88;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .pay-btn {
            width: 100%;
            padding: 22px;
            margin: 12px 0;
            border: none;
            border-radius: 12px;
            font-size: 1.3rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .pay-stripe {
            background: #635bff;
            color: #fff;
        }
        
        .pay-stripe:hover {
            background: #5348e8;
            transform: scale(1.02);
        }
        
        .pay-paypal {
            background: #0070ba;
            color: #fff;
        }
        
        .pay-paypal:hover {
            background: #005ea6;
            transform: scale(1.02);
        }
        
        .pay-etransfer {
            background: transparent;
            border: 2px solid #00ff88;
            color: #00ff88;
        }
        
        .pay-etransfer:hover {
            background: rgba(0,255,136,0.1);
        }
        
        .satisfaction {
            background: rgba(255,165,0,0.1);
            border-left: 4px solid #ffa500;
            padding: 20px;
            border-radius: 8px;
            margin-top: 30px;
        }
        
        .satisfaction h4 {
            color: #ffa500;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔬 NoizyLab</h1>
            <p style="font-size: 1.2rem; color: #888;">Professional IT & Tech Services</p>
        </div>
        
        <div class="guarantee-box">
            <h2>✅ 100% Satisfaction Guarantee</h2>
            <p>If I can't fix it - You pay NOTHING</p>
        </div>
        
        <div class="pricing-card">
            <h2>Your Issue is FIXED! ✅</h2>
            <p style="color: #888; margin-bottom: 30px;">
                Choose what you'd like to pay - minimum $89
            </p>
            
            <div class="price-options">
                <button class="price-btn" onclick="selectAmount(89)">
                    <span>Standard Service</span>
                    <span style="color: #00ff88;">$89</span>
                </button>
                
                <button class="price-btn" onclick="selectAmount(150)">
                    <span>Great Service</span>
                    <span style="color: #00ff88;">$150</span>
                </button>
                
                <button class="price-btn" onclick="selectAmount(250)">
                    <span>Exceptional Service</span>
                    <span style="color: #00ff88;">$250</span>
                </button>
                
                <div class="custom-amount">
                    <label style="display: block; text-align: center; color: #00ff88; margin-bottom: 10px; font-weight: 600;">
                        Or enter custom amount (min $89):
                    </label>
                    <input type="number" id="customAmount" min="89" step="0.01" placeholder="$89.00" onchange="selectCustomAmount()">
                </div>
            </div>
            
            <div class="payment-methods" id="paymentMethods" style="display: none;">
                <h3>💳 Choose Payment Method:</h3>
                
                <button class="pay-btn pay-stripe" onclick="payWithStripe()">
                    💳 Pay with Card (Stripe + Apple Pay)
                </button>
                
                <button class="pay-btn pay-paypal" onclick="payWithPayPal()">
                    💙 Pay with PayPal
                </button>
                
                <button class="pay-btn pay-etransfer" onclick="showEtransfer()">
                    💸 Canadian e-Transfer
                </button>
                
                <div id="selectedAmount" style="text-align: center; margin-top: 25px; padding: 20px; background: rgba(0,255,136,0.1); border-radius: 10px;">
                    <p style="color: #888; font-size: 0.9rem;">Amount selected:</p>
                    <p style="color: #00ff88; font-size: 2.5rem; font-weight: bold; margin-top: 5px;">
                        $<span id="amountDisplay">89.00</span>
                    </p>
                </div>
            </div>
            
            <div class="satisfaction">
                <h4>🤝 Our Promise:</h4>
                <p style="line-height: 1.8;">
                    • If I fix your issue → Pay minimum $89 (or more if you want!)<br>
                    • If I can't fix it → You pay NOTHING<br>
                    • Fair, honest, results-based pricing<br>
                    • No hidden fees, no surprises
                </p>
            </div>
        </div>
    </div>
    
    <script>
        let selectedAmountValue = 0;
        
        function selectAmount(amount) {
            selectedAmountValue = amount;
            document.querySelectorAll('.price-btn').forEach(btn => btn.classList.remove('selected'));
            event.target.closest('.price-btn').classList.add('selected');
            document.getElementById('customAmount').value = '';
            document.getElementById('amountDisplay').textContent = amount.toFixed(2);
            document.getElementById('paymentMethods').style.display = 'block';
        }
        
        function selectCustomAmount() {
            const amount = parseFloat(document.getElementById('customAmount').value);
            if (amount >= 89) {
                selectedAmountValue = amount;
                document.querySelectorAll('.price-btn').forEach(btn => btn.classList.remove('selected'));
                document.getElementById('amountDisplay').textContent = amount.toFixed(2);
                document.getElementById('paymentMethods').style.display = 'block';
            } else {
                alert('Minimum amount is $89');
                document.getElementById('customAmount').value = 89;
            }
        }
        
        async function payWithStripe() {
            if (selectedAmountValue < 89) {
                alert('Please select an amount (minimum $89)');
                return;
            }
            
            try {
                const response = await fetch('/api/create-stripe-checkout', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ amount: selectedAmountValue })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    window.location.href = result.url;
                } else {
                    alert('Error: ' + result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }
        
        function payWithPayPal() {
            if (selectedAmountValue < 89) {
                alert('Please select an amount (minimum $89)');
                return;
            }
            
            window.location.href = 'https://www.paypal.com/paypalme/noizyfish/' + selectedAmountValue.toFixed(2);
        }
        
        function showEtransfer() {
            if (selectedAmountValue < 89) {
                alert('Please select an amount (minimum $89)');
                return;
            }
            
            alert('Canadian e-Transfer:\\n\\nSend $' + selectedAmountValue.toFixed(2) + ' to:\\nrsp@noizylab.ca\\n\\nInclude your name in the message!');
        }
    </script>
</body>
</html>
"""

# ROUTES
@app.route('/')
def payment_page():
    """Client-facing payment page"""
    return render_template_string(CLIENT_PAYMENT_PAGE)

@app.route('/api/create-stripe-checkout', methods=['POST'])
def create_stripe_checkout():
    """Create Stripe checkout for flexible amount"""
    try:
        data = request.json
        amount = float(data['amount'])
        
        if amount < 89:
            return jsonify({'success': False, 'error': 'Minimum $89'}), 400
        
        # Would create actual Stripe checkout here
        # For now, return demo URL
        
        checkout_url = f"https://checkout.stripe.com/demo?amount={amount}"
        
        return jsonify({
            'success': True,
            'url': checkout_url,
            'amount': amount
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/not-fixed')
def not_fixed_page():
    """Page if issue wasn't fixed - NO PAYMENT"""
    return """
<!DOCTYPE html>
<html>
<head>
    <title>NoizyLab - No Charge</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 40px;
            text-align: center;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .box {
            max-width: 600px;
            background: rgba(255,255,255,0.05);
            border: 2px solid #888;
            border-radius: 20px;
            padding: 50px;
        }
        h1 { color: #888; font-size: 2.5rem; margin-bottom: 20px; }
        p { font-size: 1.2rem; line-height: 1.8; color: #aaa; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Issue Not Resolved</h1>
        <p>
            I wasn't able to fix your issue this time.
        </p>
        <p style="margin-top: 30px; font-size: 1.5rem; font-weight: bold;">
            NO CHARGE
        </p>
        <p style="margin-top: 20px; color: #888;">
            You only pay when the problem is solved.<br>
            That's fair business.
        </p>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    print("💼 'PAY ONLY IF FIXED' SYSTEM")
    print("=" * 60)
    print()
    print("PRICING MODEL:")
    print("  ✅ Issue FIXED → Minimum $89 (client can pay more!)")
    print("  ❌ Issue NOT fixed → $0 (NO CHARGE!)")
    print()
    print("PAYMENT METHODS:")
    print("  💳 Stripe (cards + Apple Pay)")
    print("  💙 PayPal (rsp@noizyfish.com)")
    print("  💸 e-Transfer (rsp@noizylab.ca)")
    print()
    print("CLIENT CHOOSES:")
    print("  • $89 (standard)")
    print("  • $150 (great service)")
    print("  • $250 (exceptional)")
    print("  • Custom amount (min $89)")
    print()
    print("🌐 Client Payment Page: http://localhost:5001")
    print()
    print("CONFIDENCE IN YOUR WORK!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=5001, debug=True)

