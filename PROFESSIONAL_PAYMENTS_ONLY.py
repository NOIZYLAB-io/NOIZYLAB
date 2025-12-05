#!/usr/bin/env python3
"""
💼 PROFESSIONAL PAYMENTS - NO TIPS, NO DONATIONS
Stripe + PayPal for BUSINESS ONLY - Invoices, sales, professional transactions
CLEAN, PROFESSIONAL, NO BULLSHIT!!
"""

from flask import Flask, render_template_string, request, jsonify, redirect
import json
import os
from datetime import datetime
import sys

# Mail.app for invoices
sys.path.append('../FishMusic_Email_System')
from MAIL_APP_COMPLETE_SYSTEM import MailAppMailer

app = Flask(__name__)
mailer = MailAppMailer()

PROFESSIONAL_INVOICE_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>💼 NoizyLab - Professional Invoicing</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 40px 20px;
        }
        .container { max-width: 800px; margin: 0 auto; }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .header h1 {
            color: #00ff88;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .invoice-form {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 15px;
            padding: 40px;
        }
        
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group.full-width {
            grid-column: 1 / -1;
        }
        
        label {
            display: block;
            color: #00ff88;
            font-weight: 600;
            margin-bottom: 8px;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 14px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(0,255,136,0.3);
            border-radius: 8px;
            color: #fff;
            font-size: 1rem;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #00ff88;
            background: rgba(255,255,255,0.08);
        }
        
        textarea {
            min-height: 120px;
            font-family: inherit;
        }
        
        .btn {
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
        
        .btn:hover {
            background: #00cc6a;
            transform: translateY(-2px);
        }
        
        .payment-methods {
            margin-top: 30px;
            padding-top: 30px;
            border-top: 1px solid rgba(0,255,136,0.2);
        }
        
        .payment-methods h3 {
            color: #00ff88;
            margin-bottom: 15px;
        }
        
        .payment-option {
            background: rgba(0,113,227,0.1);
            border: 1px solid #0071e3;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
        }
        
        .payment-option strong {
            color: #0071e3;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💼 Professional Invoice</h1>
            <p style="color: #888;">NoizyLab - Professional Services</p>
        </div>
        
        <div class="invoice-form">
            <form id="invoiceForm">
                <div class="form-grid">
                    <div class="form-group">
                        <label>Client Name</label>
                        <input type="text" name="client_name" required placeholder="Gavin Lumsden">
                    </div>
                    
                    <div class="form-group">
                        <label>Client Email</label>
                        <input type="email" name="client_email" required placeholder="client@company.com">
                    </div>
                    
                    <div class="form-group">
                        <label>Invoice Amount (CAD)</label>
                        <input type="number" name="amount" step="0.01" required placeholder="1500.00">
                    </div>
                    
                    <div class="form-group">
                        <label>Due Date</label>
                        <input type="date" name="due_date" required>
                    </div>
                </div>
                
                <div class="form-group full-width">
                    <label>Services Provided</label>
                    <textarea name="description" required placeholder="Music production services for DESIGN REUNION project..."></textarea>
                </div>
                
                <button type="submit" class="btn">
                    🧾 Create & Send Invoice
                </button>
            </form>
            
            <div class="payment-methods">
                <h3>Payment Methods Included in Invoice:</h3>
                
                <div class="payment-option">
                    <strong>💳 Stripe:</strong> Credit/Debit cards + Apple Pay
                </div>
                
                <div class="payment-option">
                    <strong>💙 PayPal:</strong> rsp@noizyfish.com
                </div>
                
                <div class="payment-option">
                    <strong>💸 e-Transfer (Canadian):</strong> rsp@noizylab.ca
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('invoiceForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/api/create-invoice', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert('✅ Invoice created and emailed to client!\\n\\nInvoice #: ' + result.invoice_number);
                    this.reset();
                } else {
                    alert('❌ Error: ' + result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def invoice_page():
    """Professional invoice creation page"""
    return render_template_string(PROFESSIONAL_INVOICE_PAGE)

@app.route('/api/create-invoice', methods=['POST'])
def create_professional_invoice():
    """Create professional invoice"""
    try:
        data = request.json
        
        # Generate invoice number
        invoice_number = f"NL{datetime.now().strftime('%Y%m%d')}{datetime.now().hour:02d}{datetime.now().minute:02d}"
        
        invoice = {
            'number': invoice_number,
            'client_name': data['client_name'],
            'client_email': data['client_email'],
            'amount': float(data['amount']),
            'description': data['description'],
            'due_date': data['due_date'],
            'created': datetime.now().isoformat(),
            'status': 'sent'
        }
        
        # Save invoice
        invoices = []
        if os.path.exists('invoices.json'):
            with open('invoices.json', 'r') as f:
                invoices = json.load(f)
        
        invoices.append(invoice)
        
        with open('invoices.json', 'w') as f:
            json.dump(invoices, f, indent=2)
        
        # Send invoice via Mail.app
        mailer.send_invoice(
            invoice['client_email'],
            invoice['client_name'],
            invoice_number,
            invoice['amount'],
            invoice['description'],
            invoice['due_date']
        )
        
        print(f"✅ Invoice {invoice_number} created and sent!")
        
        return jsonify({
            'success': True,
            'invoice_number': invoice_number
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    print("💼 PROFESSIONAL PAYMENTS SYSTEM")
    print("=" * 60)
    print()
    print("NO TIPS. NO DONATIONS. PROFESSIONAL BUSINESS ONLY.")
    print()
    print("PAYMENT METHODS:")
    print("  💳 Stripe - Credit cards + Apple Pay")
    print("  💙 PayPal - rsp@noizyfish.com")
    print("  💸 e-Transfer - rsp@noizylab.ca")
    print()
    print("🌐 Invoice System: http://localhost:5000")
    print()
    print("GORUNFREE!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=5000, debug=True)

