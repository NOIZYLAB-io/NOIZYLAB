#!/usr/bin/env python3
"""
🔥 EMAIL TEST DASHBOARD - SEE YOUR EMAILS WORKING NOW!!
Web interface to configure, test, and SEE emails working!
"""

from flask import Flask, render_template_string, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os
from datetime import datetime

app = Flask(__name__)

EMAIL_TEST_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🔥 EMAIL TEST DASHBOARD - FIX & SEE EMAILS NOW!</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        .header {
            background: linear-gradient(135deg, #ff0000 0%, #ff6600 100%);
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }
        .header h1 { font-size: 2.5rem; margin-bottom: 10px; }
        .status-box {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 30px;
        }
        .status-box.error { border-color: #ff0000; }
        .status-box.success { border-color: #00ff88; }
        .big-status {
            font-size: 4rem;
            text-align: center;
            margin: 20px 0;
        }
        .setup-section {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(0,255,136,0.2);
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 20px;
        }
        .setup-section h2 { color: #00ff88; margin-bottom: 20px; }
        .form-group { margin-bottom: 20px; }
        label {
            display: block;
            margin-bottom: 8px;
            color: #00ff88;
            font-weight: 600;
        }
        input, textarea {
            width: 100%;
            padding: 15px;
            background: rgba(255,255,255,0.05);
            border: 2px solid rgba(0,255,136,0.3);
            border-radius: 5px;
            color: #fff;
            font-size: 1.1rem;
        }
        input:focus, textarea:focus {
            outline: none;
            border-color: #00ff88;
            background: rgba(255,255,255,0.08);
        }
        .btn {
            padding: 15px 40px;
            background: #00ff88;
            color: #0f0f23;
            border: none;
            border-radius: 5px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        .btn:hover {
            background: #00cc6a;
            transform: translateY(-2px);
        }
        .btn-danger {
            background: #ff0000;
            color: #fff;
        }
        .btn-danger:hover {
            background: #cc0000;
        }
        .test-result {
            background: rgba(255,255,255,0.08);
            border-left: 4px solid #00ff88;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .test-result.error {
            border-left-color: #ff0000;
        }
        .instructions {
            background: rgba(255,165,0,0.1);
            border-left: 4px solid #ffa500;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .email-log {
            max-height: 400px;
            overflow-y: auto;
            background: rgba(0,0,0,0.3);
            padding: 20px;
            border-radius: 5px;
            font-family: monospace;
        }
        .email-entry {
            padding: 10px;
            border-bottom: 1px solid rgba(0,255,136,0.1);
            margin-bottom: 10px;
        }
        .email-entry.success { color: #00ff88; }
        .email-entry.error { color: #ff0000; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔥 EMAIL TEST DASHBOARD</h1>
            <p>FIX & SEE YOUR EMAILS WORKING NOW!!</p>
        </div>
        
        <div class="status-box {{ 'success' if config_exists else 'error' }}">
            <div class="big-status">
                {{ '✅' if config_exists else '⚠️' }}
            </div>
            <h2 style="text-align: center; margin-bottom: 10px;">
                {{ 'EMAIL CONFIGURED!' if config_exists else 'EMAIL NOT CONFIGURED YET' }}
            </h2>
            <p style="text-align: center;">
                {{ 'Ready to send emails!' if config_exists else 'Configure below to start sending' }}
            </p>
        </div>
        
        <!-- SETUP FORM -->
        <div class="setup-section">
            <h2>⚙️ EMAIL CONFIGURATION</h2>
            
            <div class="instructions">
                <strong>🔑 HOW TO GET APP PASSWORD (2 MINUTES):</strong>
                <ol style="margin: 10px 0 10px 20px; line-height: 2;">
                    <li>Go to: <a href="https://myaccount.google.com/security" target="_blank" style="color: #00ff88;">Google Account Security</a></li>
                    <li>Turn on <strong>2-Step Verification</strong> (if not already on)</li>
                    <li>Search for "App Passwords"</li>
                    <li>Select app: <strong>Mail</strong></li>
                    <li>Click <strong>Generate</strong></li>
                    <li>Copy the 16-character password</li>
                    <li>Paste it below!</li>
                </ol>
            </div>
            
            <form id="configForm">
                <div class="form-group">
                    <label>Your Gmail Address</label>
                    <input type="email" id="email" value="rsp@noizyfish.com" required>
                </div>
                
                <div class="form-group">
                    <label>Gmail App Password (16 characters, no spaces)</label>
                    <input type="text" id="password" placeholder="xxxx xxxx xxxx xxxx" required>
                </div>
                
                <button type="submit" class="btn">💾 Save Configuration</button>
            </form>
        </div>
        
        <!-- SEND TEST EMAIL -->
        <div class="setup-section">
            <h2>📧 SEND TEST EMAIL</h2>
            <p style="margin-bottom: 20px;">Send yourself an email to SEE it working!</p>
            
            <form id="testForm">
                <div class="form-group">
                    <label>Send Test Email To:</label>
                    <input type="email" id="test_email" value="rsp@noizyfish.com" required>
                </div>
                
                <button type="submit" class="btn btn-danger">🔥 SEND TEST EMAIL NOW!!</button>
            </form>
            
            <div id="testResult"></div>
        </div>
        
        <!-- EMAIL LOG -->
        <div class="setup-section">
            <h2>📊 EMAIL LOG (LIVE)</h2>
            <div class="email-log" id="emailLog">
                <div class="email-entry">Waiting for emails...</div>
            </div>
            <button onclick="loadLog()" class="btn btn-secondary" style="margin-top: 10px; background: rgba(0,255,136,0.2); color: #00ff88;">
                🔄 Refresh Log
            </button>
        </div>
    </div>
    
    <script>
        // Save configuration
        document.getElementById('configForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            const response = await fetch('/save-config', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            
            const result = await response.json();
            
            if (result.success) {
                alert('✅ Configuration saved! Now send a test email!');
                location.reload();
            } else {
                alert('❌ Error: ' + result.error);
            }
        });
        
        // Send test email
        document.getElementById('testForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const testEmail = document.getElementById('test_email').value;
            const resultDiv = document.getElementById('testResult');
            
            resultDiv.innerHTML = '<div class="test-result"><strong>⏳ SENDING EMAIL...</strong><br>Please wait...</div>';
            
            try {
                const response = await fetch('/send-test', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: testEmail })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    resultDiv.innerHTML = `
                        <div class="test-result success">
                            <h3 style="color: #00ff88; margin-bottom: 10px;">🎉 EMAIL SENT SUCCESSFULLY!!</h3>
                            <p><strong>Sent to:</strong> ${testEmail}</p>
                            <p><strong>Time:</strong> ${result.timestamp}</p>
                            <p style="margin-top: 15px; font-size: 1.2rem;">
                                ✅ <strong>CHECK YOUR INBOX NOW!</strong>
                            </p>
                            <p style="margin-top: 10px; color: #888;">
                                (Check spam folder if you don't see it)
                            </p>
                        </div>
                    `;
                    loadLog();
                } else {
                    resultDiv.innerHTML = `
                        <div class="test-result error">
                            <h3 style="color: #ff0000; margin-bottom: 10px;">❌ EMAIL FAILED!</h3>
                            <p><strong>Error:</strong> ${result.error}</p>
                            <p style="margin-top: 15px;">
                                Check your app password and try again.
                            </p>
                        </div>
                    `;
                }
            } catch (error) {
                resultDiv.innerHTML = `
                    <div class="test-result error">
                        <h3 style="color: #ff0000;">❌ ERROR!</h3>
                        <p>${error.message}</p>
                    </div>
                `;
            }
        });
        
        // Load email log
        async function loadLog() {
            const response = await fetch('/api/email-log');
            const log = await response.json();
            
            const logDiv = document.getElementById('emailLog');
            
            if (log.length === 0) {
                logDiv.innerHTML = '<div class="email-entry">No emails sent yet</div>';
                return;
            }
            
            logDiv.innerHTML = '';
            
            log.reverse().slice(0, 20).forEach(entry => {
                const entryDiv = document.createElement('div');
                entryDiv.className = `email-entry ${entry.status}`;
                entryDiv.innerHTML = `
                    <strong>${entry.timestamp}</strong><br>
                    To: ${entry.to}<br>
                    Subject: ${entry.subject}<br>
                    Status: <strong>${entry.status.toUpperCase()}</strong>
                `;
                logDiv.appendChild(entryDiv);
            });
        }
        
        // Auto-refresh log every 5 seconds
        setInterval(loadLog, 5000);
        
        // Load on start
        loadLog();
    </script>
</body>
</html>
"""

CONFIG_FILE = "working_email_config.json"
LOG_FILE = "email_test_log.json"

def load_config():
    """Load email configuration"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return None

def save_config(config):
    """Save email configuration"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def log_email(to, subject, status, error=None):
    """Log email send attempt"""
    log = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            log = json.load(f)
    
    log.append({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'to': to,
        'subject': subject,
        'status': status,
        'error': error
    })
    
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)

@app.route('/')
def home():
    """Dashboard home"""
    config = load_config()
    return render_template_string(EMAIL_TEST_HTML, config_exists=(config is not None))

@app.route('/save-config', methods=['POST'])
def save_email_config():
    """Save email configuration"""
    try:
        data = request.json
        
        config = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'from_email': data['email'],
            'username': data['email'],
            'password': data['password'],
            'configured': datetime.now().isoformat()
        }
        
        save_config(config)
        
        return jsonify({'success': True})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/send-test', methods=['POST'])
def send_test_email():
    """Send test email"""
    try:
        data = request.json
        to_email = data['email']
        
        # Load config
        config = load_config()
        
        if not config:
            return jsonify({'success': False, 'error': 'Email not configured yet!'})
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "🔥 YOUR EMAIL SYSTEM IS WORKING!!"
        msg['From'] = f"NoizyLab <{config['from_email']}>"
        msg['To'] = to_email
        
        text = f"""
🔥 EMAIL SYSTEM IS WORKING!!

If you're reading this - YOUR EMAILS ARE FIXED! ✅

This email was sent from your NoizyLab email system.

Sent: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
From: {config['from_email']}

YOU CAN NOW:
✅ Send customer receipts
✅ Send download links
✅ Send invoices
✅ Automate everything!

GORUNFREE! 🚀

CB_01 - Your LIFELUV ENGR
"""
        
        html = f"""
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; padding: 20px; background: #f0f0f0;">
    <div style="max-width: 600px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px;">
        <div style="background: linear-gradient(135deg, #ff0000 0%, #ff6600 100%); color: white; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px;">
            <h1 style="margin: 0; font-size: 2.5rem;">🔥</h1>
            <h2 style="margin: 10px 0 0 0;">EMAIL SYSTEM WORKING!!</h2>
        </div>
        
        <div style="background: #00ff88; color: #0f0f23; padding: 20px; border-radius: 5px; text-align: center; margin: 20px 0;">
            <h2 style="margin: 0;">✅ YOUR EMAILS ARE FIXED!</h2>
        </div>
        
        <p style="font-size: 1.1rem; line-height: 1.8;">
            If you're reading this email - <strong>YOUR EMAIL SYSTEM IS WORKING PERFECTLY!</strong>
        </p>
        
        <div style="background: #f4f4f4; padding: 20px; border-radius: 5px; margin: 20px 0;">
            <strong>Sent:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
            <strong>From:</strong> {config['from_email']}<br>
            <strong>System:</strong> NoizyLab Email Platform
        </div>
        
        <h3>You Can Now:</h3>
        <ul style="line-height: 2;">
            <li>✅ Send customer receipts automatically</li>
            <li>✅ Send download links</li>
            <li>✅ Send invoices</li>
            <li>✅ Automate ALL email tasks</li>
        </ul>
        
        <p style="color: #00ff88; font-size: 1.5rem; font-weight: bold; text-align: center; margin-top: 30px;">
            GORUNFREE! 🚀
        </p>
        
        <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
        
        <p style="font-size: 12px; color: #666; text-align: center;">
            <strong>CB_01 - Your LIFELUV ENGR</strong><br>
            NoizyLab Portal | noizylab.ca
        </p>
    </div>
</body>
</html>
"""
        
        msg.attach(MIMEText(text, 'plain'))
        msg.attach(MIMEText(html, 'html'))
        
        # SEND IT!!
        server = smtplib.SMTP(config['smtp_server'], config['smtp_port'], timeout=10)
        server.starttls()
        server.login(config['username'], config['password'])
        server.send_message(msg)
        server.quit()
        
        # Log success
        log_email(to_email, msg['Subject'], 'success')
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'to': to_email
        })
    
    except smtplib.SMTPAuthenticationError:
        error = "Authentication failed! Check your app password."
        log_email(to_email if 'to_email' in locals() else 'unknown', 'Test Email', 'error', error)
        return jsonify({'success': False, 'error': error})
    
    except Exception as e:
        error = str(e)
        log_email(to_email if 'to_email' in locals() else 'unknown', 'Test Email', 'error', error)
        return jsonify({'success': False, 'error': error})

@app.route('/api/email-log')
def get_email_log():
    """Get email log"""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return jsonify(json.load(f))
    return jsonify([])

if __name__ == '__main__':
    print("🔥 EMAIL TEST DASHBOARD - STARTING...")
    print("=" * 60)
    print("🌐 OPEN THIS IN YOUR BROWSER:")
    print()
    print("   http://localhost:6000")
    print()
    print("=" * 60)
    print("1. Enter your Gmail app password")
    print("2. Click 'Send Test Email'")
    print("3. CHECK YOUR INBOX - SEE IT WORKING!!")
    print("=" * 60)
    print()
    print("EMAILS WILL BE FIXED IN 2 MINUTES!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=6000, debug=True)

