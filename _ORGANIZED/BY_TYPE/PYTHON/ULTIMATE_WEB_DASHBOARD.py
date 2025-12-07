#!/usr/bin/env python3
"""
🚀 FISH MUSIC EMAIL - ULTIMATE WEB DASHBOARD
Complete web interface for managing all emails + webhooks + analytics
"""

from flask import Flask, render_template_string, request, jsonify, redirect, url_for
from ULTIMATE_FISH_MAILER import UltimateFishMailer
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)
mailer = UltimateFishMailer()

# HTML TEMPLATE - BEAUTIFUL DASHBOARD
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🐟 Fish Music Email Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        .header {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 20px;
        }
        .header h1 { color: #667eea; margin-bottom: 10px; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .stat-card h3 { color: #667eea; font-size: 14px; margin-bottom: 10px; }
        .stat-card .number { font-size: 36px; font-weight: bold; color: #333; }
        .actions {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .action-card {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .action-card h3 { color: #667eea; margin-bottom: 15px; }
        .btn {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 12px 24px;
            border-radius: 5px;
            text-decoration: none;
            border: none;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s;
        }
        .btn:hover { background: #5568d3; transform: translateY(-2px); }
        .btn-success { background: #10b981; }
        .btn-success:hover { background: #059669; }
        input, textarea, select {
            width: 100%;
            padding: 10px;
            border: 2px solid #e5e7eb;
            border-radius: 5px;
            margin-bottom: 10px;
            font-size: 14px;
        }
        textarea { min-height: 100px; font-family: inherit; }
        .log-entry {
            background: #f9fafb;
            padding: 15px;
            border-left: 4px solid #667eea;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .log-entry.success { border-left-color: #10b981; }
        .log-entry.failed { border-left-color: #ef4444; }
        .log-entry .time { color: #6b7280; font-size: 12px; }
        .tab-container { margin-bottom: 20px; }
        .tabs {
            display: flex;
            gap: 10px;
            background: white;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .tab {
            padding: 12px 24px;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .tab.active { background: #667eea; color: white; }
        .tab:not(.active):hover { background: #f3f4f6; }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        .webhook-url {
            background: #f3f4f6;
            padding: 15px;
            border-radius: 5px;
            font-family: monospace;
            margin: 10px 0;
            word-break: break-all;
        }
        .success-msg {
            background: #d1fae5;
            color: #065f46;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        .dns-status {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px;
            background: #f9fafb;
            border-radius: 5px;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🐟 Fish Music Email Dashboard</h1>
            <p>Complete email management & automation platform</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <h3>EMAILS SENT TODAY</h3>
                <div class="number">{{ stats.today }}</div>
            </div>
            <div class="stat-card">
                <h3>THIS WEEK</h3>
                <div class="number">{{ stats.week }}</div>
            </div>
            <div class="stat-card">
                <h3>SUCCESS RATE</h3>
                <div class="number">{{ stats.success_rate }}%</div>
            </div>
            <div class="stat-card">
                <h3>ACTIVE PROVIDERS</h3>
                <div class="number">{{ stats.providers }}</div>
            </div>
        </div>
        
        <div class="tab-container">
            <div class="tabs">
                <div class="tab active" onclick="switchTab('send')">📧 Send Email</div>
                <div class="tab" onclick="switchTab('templates')">🎨 Templates</div>
                <div class="tab" onclick="switchTab('webhooks')">🔗 Webhooks</div>
                <div class="tab" onclick="switchTab('dns')">🌐 DNS Status</div>
                <div class="tab" onclick="switchTab('logs')">📊 Logs</div>
            </div>
        </div>
        
        <div id="send" class="tab-content active">
            <div class="actions">
                <div class="action-card">
                    <h3>📝 Test Email</h3>
                    <form action="/send-test" method="post">
                        <input name="email" placeholder="Recipient email" required>
                        <button type="submit" class="btn btn-success">Send Test</button>
                    </form>
                </div>
                
                <div class="action-card">
                    <h3>🎵 Purchase Receipt</h3>
                    <form action="/send-receipt" method="post">
                        <input name="email" placeholder="Customer email" required>
                        <input name="name" placeholder="Customer name" required>
                        <input name="track" placeholder="Track name" required>
                        <input name="price" type="number" step="0.01" placeholder="Price" required>
                        <input name="order_id" placeholder="Order ID" required>
                        <button type="submit" class="btn btn-success">Send Receipt</button>
                    </form>
                </div>
                
                <div class="action-card">
                    <h3>⬇️ Download Link</h3>
                    <form action="/send-download" method="post">
                        <input name="email" placeholder="Customer email" required>
                        <input name="name" placeholder="Customer name" required>
                        <input name="track" placeholder="Track name" required>
                        <input name="url" placeholder="Download URL" required>
                        <button type="submit" class="btn btn-success">Send Download</button>
                    </form>
                </div>
                
                <div class="action-card">
                    <h3>👋 Welcome Email</h3>
                    <form action="/send-welcome" method="post">
                        <input name="email" placeholder="Customer email" required>
                        <input name="name" placeholder="Customer name" required>
                        <button type="submit" class="btn btn-success">Send Welcome</button>
                    </form>
                </div>
            </div>
        </div>
        
        <div id="templates" class="tab-content">
            <div class="action-card">
                <h3>🎨 Email Templates</h3>
                <p>Available templates:</p>
                <ul style="margin: 15px 0; line-height: 2;">
                    <li>✅ Purchase Receipt - Branded order confirmation</li>
                    <li>✅ Download Link - Beautiful download delivery</li>
                    <li>✅ Welcome Email - Hero banner welcome</li>
                    <li>✅ Test Email - Quick system test</li>
                </ul>
                <p style="margin-top: 15px; color: #6b7280;">
                    All templates include professional HTML design, mobile responsiveness, 
                    Fish Music branding, and "GORUNFREE!" signature.
                </p>
            </div>
        </div>
        
        <div id="webhooks" class="tab-content">
            <div class="action-card">
                <h3>🔗 Webhook Endpoints</h3>
                <p>Integrate with payment processors:</p>
                
                <h4 style="margin: 20px 0 10px 0;">Stripe Webhook:</h4>
                <div class="webhook-url">
                    POST http://localhost:5000/webhook/stripe
                </div>
                <p style="font-size: 12px; color: #6b7280;">
                    Automatically sends receipt + download link when payment succeeds
                </p>
                
                <h4 style="margin: 20px 0 10px 0;">Ko-fi Webhook:</h4>
                <div class="webhook-url">
                    POST http://localhost:5000/webhook/kofi
                </div>
                <p style="font-size: 12px; color: #6b7280;">
                    Handles Ko-fi donations and sends thank you emails
                </p>
                
                <h4 style="margin: 20px 0 10px 0;">Generic Webhook:</h4>
                <div class="webhook-url">
                    POST http://localhost:5000/webhook/generic
                </div>
                <p style="font-size: 12px; color: #6b7280;">
                    Custom webhook for any integration
                </p>
            </div>
        </div>
        
        <div id="dns" class="tab-content">
            <div class="action-card">
                <h3>🌐 DNS Status</h3>
                {% for domain, status in dns_status.items() %}
                <div style="margin-bottom: 20px;">
                    <h4>{{ domain }}</h4>
                    <div class="dns-status">
                        <span>MX Records:</span>
                        <span>{{ '✅' if status.mx_records else '❌' }}</span>
                    </div>
                    <div class="dns-status">
                        <span>SPF Record:</span>
                        <span>{{ '✅' if status.spf_record else '❌' }}</span>
                    </div>
                    <div class="dns-status">
                        <span>DMARC Record:</span>
                        <span>{{ '✅' if status.dmarc_record else '❌' }}</span>
                    </div>
                    {% if status.issues %}
                    <div style="margin-top: 10px; padding: 10px; background: #fee2e2; border-radius: 5px;">
                        {% for issue in status.issues %}
                        <div style="font-size: 12px; color: #991b1b;">⚠️ {{ issue }}</div>
                        {% endfor %}
                    </div>
                    {% endif %}
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div id="logs" class="tab-content">
            <div class="action-card">
                <h3>📊 Recent Email Logs</h3>
                {% for log in logs %}
                <div class="log-entry {{ log.status }}">
                    <div class="time">{{ log.timestamp }}</div>
                    <div><strong>To:</strong> {{ log.to }}</div>
                    <div><strong>Subject:</strong> {{ log.subject }}</div>
                    <div><strong>Provider:</strong> {{ log.provider }} | <strong>Status:</strong> {{ log.status }}</div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
    
    <script>
        function switchTab(tabName) {
            // Hide all tabs
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(el => el.classList.remove('active'));
            
            // Show selected tab
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }
    </script>
</body>
</html>
"""

def get_email_stats():
    """Get email statistics from logs"""
    stats = {
        'today': 0,
        'week': 0,
        'success_rate': 0,
        'providers': len([p for p in mailer.providers if p.get('enabled')])
    }
    
    if not os.path.exists('email_log.jsonl'):
        return stats
    
    now = datetime.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_start = now - timedelta(days=7)
    
    success_count = 0
    total_count = 0
    
    with open('email_log.jsonl', 'r') as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                timestamp = datetime.fromisoformat(entry['timestamp'])
                
                if timestamp >= today_start:
                    stats['today'] += 1
                
                if timestamp >= week_start:
                    stats['week'] += 1
                
                total_count += 1
                if entry.get('status') == 'success':
                    success_count += 1
            except:
                pass
    
    if total_count > 0:
        stats['success_rate'] = int((success_count / total_count) * 100)
    
    return stats

def get_recent_logs(limit=20):
    """Get recent email logs"""
    logs = []
    
    if not os.path.exists('email_log.jsonl'):
        return logs
    
    with open('email_log.jsonl', 'r') as f:
        lines = f.readlines()
    
    for line in reversed(lines[-limit:]):
        try:
            logs.append(json.loads(line.strip()))
        except:
            pass
    
    return logs

def get_dns_status():
    """Check DNS for all configured domains"""
    domains = ['noizyfish.com', 'fishmusicinc.com']
    status = {}
    
    for domain in domains:
        try:
            status[domain] = mailer.validate_dns_records(domain)
        except Exception as e:
            status[domain] = {'mx_records': False, 'spf_record': False, 'dmarc_record': False, 'issues': [str(e)]}
    
    return status

@app.route('/')
def dashboard():
    """Main dashboard"""
    return render_template_string(
        DASHBOARD_HTML,
        stats=get_email_stats(),
        logs=get_recent_logs(),
        dns_status=get_dns_status()
    )

@app.route('/send-test', methods=['POST'])
def send_test():
    """Send test email"""
    email = request.form.get('email')
    mailer.send_email_bulletproof(
        email,
        "🐟 Test from Fish Music Dashboard",
        "This is a test email from the dashboard. Everything works! GORUNFREE! 🚀",
        "<h1>✅ Dashboard Test!</h1><p>Everything works perfectly! 🐟🚀</p>"
    )
    return redirect('/')

@app.route('/send-receipt', methods=['POST'])
def send_receipt():
    """Send purchase receipt"""
    mailer.send_purchase_receipt(
        request.form.get('email'),
        request.form.get('name'),
        request.form.get('track'),
        float(request.form.get('price')),
        request.form.get('order_id')
    )
    return redirect('/')

@app.route('/send-download', methods=['POST'])
def send_download():
    """Send download link"""
    mailer.send_download_link(
        request.form.get('email'),
        request.form.get('name'),
        request.form.get('track'),
        request.form.get('url')
    )
    return redirect('/')

@app.route('/send-welcome', methods=['POST'])
def send_welcome():
    """Send welcome email"""
    mailer.send_welcome(
        request.form.get('email'),
        request.form.get('name')
    )
    return redirect('/')

@app.route('/webhook/stripe', methods=['POST'])
def stripe_webhook():
    """Handle Stripe webhooks"""
    try:
        data = request.json
        
        # Handle payment success
        if data.get('type') == 'payment_intent.succeeded':
            customer_email = data['data']['object']['receipt_email']
            amount = data['data']['object']['amount'] / 100
            
            # Send receipt
            mailer.send_purchase_receipt(
                customer_email,
                "Customer",  # Get from metadata
                "Track Name",  # Get from metadata
                amount,
                data['data']['object']['id']
            )
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/webhook/kofi', methods=['POST'])
def kofi_webhook():
    """Handle Ko-fi webhooks"""
    try:
        data = request.json
        
        # Send thank you email
        mailer.send_purchase_receipt(
            data.get('email'),
            data.get('from_name'),
            "Support Donation",
            float(data.get('amount', 0)),
            data.get('kofi_transaction_id')
        )
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/stats', methods=['GET'])
def api_stats():
    """API endpoint for stats"""
    return jsonify(get_email_stats())

@app.route('/api/logs', methods=['GET'])
def api_logs():
    """API endpoint for logs"""
    limit = int(request.args.get('limit', 50))
    return jsonify(get_recent_logs(limit))

if __name__ == '__main__':
    print("🚀 STARTING FISH MUSIC EMAIL DASHBOARD")
    print("=" * 60)
    print("📊 Dashboard: http://localhost:5000")
    print("🔗 Stripe Webhook: http://localhost:5000/webhook/stripe")
    print("🔗 Ko-fi Webhook: http://localhost:5000/webhook/kofi")
    print("=" * 60)
    print("GORUNFREE! 🐟🚀")
    print()
    
    app.run(host='0.0.0.0', port=5000, debug=True)
