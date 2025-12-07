#!/usr/bin/env python3
"""
🚨 NOIZYLAB RESCUE - COMPLETE SYSTEM
Most Mac/Tech issues can be PARTIALLY or COMPLETELY solved with NoizyLab Rescue!
Professional, comprehensive problem-solving service
$89 minimum - Pay only if we help! MORE if you want!
"""

from flask import Flask, render_template_string, request, jsonify, redirect, session
import json
import os
from datetime import datetime
import secrets
import sys

# Mail.app for communications
sys.path.append('../FishMusic_Email_System')
from MAIL_APP_COMPLETE_SYSTEM import MailAppMailer

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
mailer = MailAppMailer()

DATA_DIR = "rescue_data"
os.makedirs(DATA_DIR, exist_ok=True)

RESCUE_HOMEPAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚨 NoizyLab RESCUE - We Solve Mac Problems!</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro', Arial, sans-serif;
            background: #000;
            color: #fff;
        }
        
        /* HERO SECTION */
        .hero {
            background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
            padding: 80px 20px;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 4rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .hero .tagline {
            font-size: 1.8rem;
            margin-bottom: 15px;
            opacity: 0.95;
        }
        
        .hero .promise {
            font-size: 1.3rem;
            background: rgba(0,0,0,0.3);
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
            margin-top: 20px;
        }
        
        /* CONTAINER */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 60px 20px;
        }
        
        /* WHAT WE DO */
        .section {
            margin-bottom: 60px;
        }
        
        .section h2 {
            color: #00ff88;
            font-size: 2.5rem;
            margin-bottom: 30px;
            text-align: center;
        }
        
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .service-card {
            background: rgba(255,255,255,0.03);
            border: 2px solid rgba(0,255,136,0.2);
            border-radius: 15px;
            padding: 30px;
            transition: all 0.3s;
        }
        
        .service-card:hover {
            background: rgba(255,255,255,0.06);
            border-color: #00ff88;
            transform: translateY(-10px);
        }
        
        .service-card h3 {
            color: #00ff88;
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        
        .service-card ul {
            line-height: 2;
            color: #ccc;
            margin-left: 20px;
        }
        
        /* PRICING */
        .pricing-section {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 100%);
            padding: 60px 20px;
            border-radius: 20px;
            text-align: center;
        }
        
        .pricing-boxes {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .price-box {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 15px;
            padding: 40px 30px;
        }
        
        .price-box h3 {
            color: #00ff88;
            font-size: 1.3rem;
            margin-bottom: 15px;
        }
        
        .price-box .amount {
            font-size: 3rem;
            font-weight: bold;
            color: #fff;
            margin: 20px 0;
        }
        
        .price-box p {
            color: #888;
            line-height: 1.8;
        }
        
        /* CTA */
        .cta-section {
            text-align: center;
            margin-top: 60px;
        }
        
        .btn-cta {
            display: inline-block;
            padding: 25px 60px;
            background: #00ff88;
            color: #0f0f23;
            text-decoration: none;
            border-radius: 50px;
            font-size: 1.5rem;
            font-weight: 600;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
        }
        
        .btn-cta:hover {
            background: #00cc6a;
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(0,255,136,0.3);
        }
        
        /* GUARANTEE */
        .guarantee {
            background: rgba(0,255,136,0.05);
            border: 3px solid #00ff88;
            border-radius: 20px;
            padding: 40px;
            margin: 60px 0;
            text-align: center;
        }
        
        .guarantee h2 {
            color: #00ff88;
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        
        .guarantee p {
            font-size: 1.3rem;
            line-height: 2;
        }
    </style>
</head>
<body>
    <!-- HERO -->
    <div class="hero">
        <h1>🚨 NoizyLab RESCUE</h1>
        <p class="tagline">We Solve Your Mac Problems!</p>
        <p class="promise">
            ✅ Most issues PARTIALLY or COMPLETELY solved<br>
            ✅ Remote service - no travel needed<br>
            ✅ Pay only if we help - GUARANTEED!
        </p>
    </div>
    
    <!-- MAIN CONTENT -->
    <div class="container">
        <!-- WHAT WE RESCUE -->
        <div class="section">
            <h2>🔧 What We Rescue</h2>
            
            <div class="services-grid">
                <div class="service-card">
                    <h3>💻 Performance Rescue</h3>
                    <ul>
                        <li>Slow Mac? We'll speed it up!</li>
                        <li>Apps crashing? We'll stabilize!</li>
                        <li>System freezing? We'll fix it!</li>
                        <li>Update problems? We'll resolve!</li>
                    </ul>
                </div>
                
                <div class="service-card">
                    <h3>📁 Data Rescue</h3>
                    <ul>
                        <li>Files missing? We'll recover!</li>
                        <li>Backup needed? We'll create!</li>
                        <li>Data corrupted? We'll repair!</li>
                        <li>Migration needed? We'll transfer!</li>
                    </ul>
                </div>
                
                <div class="service-card">
                    <h3>🌐 Connectivity Rescue</h3>
                    <ul>
                        <li>WiFi issues? We'll reconnect!</li>
                        <li>Email broken? We'll fix!</li>
                        <li>Network slow? We'll optimize!</li>
                        <li>Printer won't work? We'll connect!</li>
                    </ul>
                </div>
                
                <div class="service-card">
                    <h3>🛡️ Security Rescue</h3>
                    <ul>
                        <li>Password locked out? We'll recover!</li>
                        <li>Virus concerns? We'll scan & remove!</li>
                        <li>Account compromised? We'll secure!</li>
                        <li>Privacy setup? We'll configure!</li>
                    </ul>
                </div>
                
                <div class="service-card">
                    <h3>⚙️ Software Rescue</h3>
                    <ul>
                        <li>App won't install? We'll fix!</li>
                        <li>Settings messed up? We'll restore!</li>
                        <li>Errors appearing? We'll resolve!</li>
                        <li>Need setup help? We'll guide!</li>
                    </ul>
                </div>
                
                <div class="service-card">
                    <h3>🎵 Creative Rescue</h3>
                    <ul>
                        <li>Logic/Pro Tools issues? We'll fix!</li>
                        <li>Audio not working? We'll repair!</li>
                        <li>Plugins broken? We'll restore!</li>
                        <li>Project won't open? We'll recover!</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <!-- PRICING -->
        <div class="pricing-section">
            <h2 style="font-size: 2.5rem; margin-bottom: 20px;">💰 Fair, Honest Pricing</h2>
            <p style="font-size: 1.2rem; color: #888; margin-bottom: 40px;">
                You ONLY pay if we help solve your problem!
            </p>
            
            <div class="pricing-boxes">
                <div class="price-box">
                    <h3>Minimum</h3>
                    <div class="amount">$89</div>
                    <p>If we solve your issue<br>(partially or completely)</p>
                </div>
                
                <div class="price-box" style="border-color: #0071e3; background: rgba(0,113,227,0.05);">
                    <h3>You Choose More</h3>
                    <div class="amount" style="color: #0071e3;">$89+</div>
                    <p>Pay more if you feel<br>the service was exceptional!</p>
                </div>
                
                <div class="price-box" style="border-color: #888;">
                    <h3>Not Fixed</h3>
                    <div class="amount" style="color: #888;">$0</div>
                    <p>If we can't help<br>you pay NOTHING</p>
                </div>
            </div>
        </div>
        
        <!-- GUARANTEE -->
        <div class="guarantee">
            <h2>🤝 Our Guarantee</h2>
            <p>
                <strong>Most Mac issues can be PARTIALLY or COMPLETELY solved</strong><br>
                with a NoizyLab Rescue!
            </p>
            <p style="margin-top: 20px;">
                If we help → Minimum $89 (you can pay more!)<br>
                If we don't help → You pay NOTHING
            </p>
            <p style="margin-top: 30px; font-size: 1.5rem; font-weight: bold; color: #00ff88;">
                Fair. Honest. Results-Based.
            </p>
        </div>
        
        <!-- CTA -->
        <div class="cta-section">
            <h2 style="color: #00ff88; font-size: 2.5rem; margin-bottom: 30px;">
                Ready for a NoizyLab RESCUE?
            </h2>
            
            <button class="btn-cta" onclick="startRescue()">
                🚨 Start Your Rescue Now!
            </button>
            
            <p style="margin-top: 30px; color: #888; font-size: 1.1rem;">
                Remote service • Usually 30-90 minutes • Pay only if helped!
            </p>
        </div>
    </div>
    
    <script>
        function startRescue() {
            window.location.href = '/rescue/intake';
        }
    </script>
</body>
</html>
"""

RESCUE_INTAKE_FORM = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>🚨 NoizyLab RESCUE - Start Your Rescue</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 40px 20px;
        }
        .container { max-width: 700px; margin: 0 auto; }
        
        .header {
            text-align: center;
            background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
            padding: 40px;
            border-radius: 15px;
            margin-bottom: 40px;
        }
        .header h1 { font-size: 3rem; margin-bottom: 10px; }
        
        .rescue-form {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 15px;
            padding: 40px;
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        label {
            display: block;
            color: #00ff88;
            font-weight: 600;
            margin-bottom: 8px;
            font-size: 1.05rem;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 15px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(0,255,136,0.3);
            border-radius: 8px;
            color: #fff;
            font-size: 1.05rem;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #00ff88;
            background: rgba(255,255,255,0.08);
        }
        
        textarea {
            min-height: 150px;
            font-family: inherit;
        }
        
        .btn {
            width: 100%;
            padding: 20px;
            background: #00ff88;
            color: #0f0f23;
            border: none;
            border-radius: 10px;
            font-size: 1.3rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn:hover {
            background: #00cc6a;
            transform: translateY(-2px);
        }
        
        .guarantee-note {
            background: rgba(0,255,136,0.05);
            border-left: 4px solid #00ff88;
            padding: 20px;
            border-radius: 5px;
            margin-top: 30px;
        }
        
        .guarantee-note h3 {
            color: #00ff88;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚨 NoizyLab RESCUE</h1>
            <p style="font-size: 1.3rem;">Tell us what's wrong - we'll solve it!</p>
        </div>
        
        <div class="rescue-form">
            <form id="rescueForm">
                <div class="form-group">
                    <label>Your Name</label>
                    <input type="text" name="name" required placeholder="John Smith">
                </div>
                
                <div class="form-group">
                    <label>Your Email</label>
                    <input type="email" name="email" required placeholder="you@email.com">
                </div>
                
                <div class="form-group">
                    <label>Phone (for TeamViewer/remote access)</label>
                    <input type="tel" name="phone" placeholder="Optional - for quick contact">
                </div>
                
                <div class="form-group">
                    <label>What's Your Mac Issue?</label>
                    <select name="issue_category" required>
                        <option value="">Select category...</option>
                        <option value="slow">Mac is slow/freezing</option>
                        <option value="app">App problems</option>
                        <option value="wifi">WiFi/Internet issues</option>
                        <option value="email">Email not working</option>
                        <option value="data">Files/data problems</option>
                        <option value="update">Update issues</option>
                        <option value="password">Password/login problems</option>
                        <option value="audio">Audio/music software</option>
                        <option value="backup">Backup/storage</option>
                        <option value="virus">Security/virus concerns</option>
                        <option value="other">Other issue</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Describe the Problem in Detail</label>
                    <textarea name="description" required placeholder="What exactly is happening? When did it start? What have you tried?"></textarea>
                </div>
                
                <div class="form-group">
                    <label>Mac Model (if you know)</label>
                    <input type="text" name="mac_model" placeholder="e.g., MacBook Pro M2, iMac 2020">
                </div>
                
                <div class="form-group">
                    <label>macOS Version (if you know)</label>
                    <input type="text" name="macos_version" placeholder="e.g., Sonoma 14.5, Ventura">
                </div>
                
                <button type="submit" class="btn">
                    🚨 Submit RESCUE Request
                </button>
            </form>
            
            <div class="guarantee-note">
                <h3>✅ No-Risk Guarantee</h3>
                <p style="line-height: 1.8; color: #ccc;">
                    • We'll assess your issue remotely (FREE!)<br>
                    • Most issues: Partially or completely solvable!<br>
                    • If we solve it: $89 minimum (you choose to pay more!)<br>
                    • If we can't help: You pay NOTHING<br>
                    • Hardware issues: We'll tell you upfront if Apple Store needed
                </p>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('rescueForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/api/rescue/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert('✅ RESCUE Request Received!\\n\\nI\\'ll contact you at: ' + data.email + '\\n\\nUsually respond within 1-2 hours!');
                    window.location.href = '/rescue/confirmation/' + result.rescue_id;
                } else {
                    alert('Error: ' + result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        });
    </script>
</body>
</html>
"""

# ROUTES
@app.route('/')
def homepage():
    """NoizyLab Rescue homepage"""
    return render_template_string(RESCUE_HOMEPAGE)

@app.route('/rescue/intake')
def rescue_intake():
    """Rescue intake form"""
    return render_template_string(RESCUE_INTAKE_FORM)

@app.route('/api/rescue/submit', methods=['POST'])
def submit_rescue_request():
    """Submit rescue request"""
    try:
        data = request.json
        
        # Generate rescue ID
        rescue_id = f"RESCUE{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        rescue_request = {
            'id': rescue_id,
            'name': data['name'],
            'email': data['email'],
            'phone': data.get('phone', ''),
            'issue_category': data['issue_category'],
            'description': data['description'],
            'mac_model': data.get('mac_model', 'Unknown'),
            'macos_version': data.get('macos_version', 'Unknown'),
            'status': 'new',
            'submitted': datetime.now().isoformat(),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save request
        requests_file = os.path.join(DATA_DIR, 'rescue_requests.json')
        
        requests_list = []
        if os.path.exists(requests_file):
            with open(requests_file, 'r') as f:
                requests_list = json.load(f)
        
        requests_list.append(rescue_request)
        
        with open(requests_file, 'w') as f:
            json.dump(requests_list, f, indent=2)
        
        # Send notification email to YOU
        mailer.send_email(
            "rsplowman@icloud.com",
            f"🚨 NEW RESCUE REQUEST: {rescue_id}",
            f"""
NEW RESCUE REQUEST RECEIVED!

Rescue ID: {rescue_id}
Client: {rescue_request['name']}
Email: {rescue_request['email']}
Phone: {rescue_request['phone']}

ISSUE: {rescue_request['issue_category']}

DESCRIPTION:
{rescue_request['description']}

MAC INFO:
Model: {rescue_request['mac_model']}
macOS: {rescue_request['macos_version']}

Submitted: {rescue_request['timestamp']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NEXT STEPS:
1. Review issue
2. Contact client
3. Assess remotely
4. Solve problem!
5. If helped → Invoice $89+
6. If not helped → No charge

NoizyLab RESCUE System
noizylab.ca
"""
        )
        
        # Send confirmation to CLIENT
        mailer.send_email(
            rescue_request['email'],
            f"✅ NoizyLab RESCUE Request Received - {rescue_id}",
            f"""
Hi {rescue_request['name']}!

Your RESCUE request has been received!

Rescue ID: {rescue_id}
Issue: {rescue_request['issue_category']}

WHAT HAPPENS NEXT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. I'll review your issue (within 1-2 hours)
2. Contact you to schedule remote session
3. Connect remotely to assess/fix
4. Most issues: Partially or completely solvable!

PRICING (100% Fair!):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• If we solve your issue → $89 minimum (you can pay more!)
• If we can't help → You pay NOTHING

That's our guarantee - you only pay for results!

I'll be in touch soon!

Rob @ NoizyLab
noizylab.ca
rsplowman@icloud.com
"""
        )
        
        print(f"🚨 NEW RESCUE REQUEST: {rescue_id}")
        print(f"   Client: {rescue_request['name']}")
        print(f"   Issue: {rescue_request['issue_category']}")
        print(f"   ✅ Emails sent!")
        
        return jsonify({
            'success': True,
            'rescue_id': rescue_id
        })
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/rescue/confirmation/<rescue_id>')
def confirmation(rescue_id):
    """Confirmation page"""
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>✅ RESCUE Request Received</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 40px;
            text-align: center;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .box {{
            max-width: 600px;
            background: rgba(0,255,136,0.05);
            border: 2px solid #00ff88;
            border-radius: 20px;
            padding: 50px;
        }}
        h1 {{ color: #00ff88; font-size: 3rem; margin-bottom: 20px; }}
        p {{ font-size: 1.2rem; line-height: 2; }}
        .rescue-id {{
            background: rgba(0,0,0,0.3);
            padding: 15px;
            border-radius: 8px;
            font-family: monospace;
            font-size: 1.5rem;
            margin: 20px 0;
            color: #00ff88;
        }}
    </style>
</head>
<body>
    <div class="box">
        <h1>✅ RESCUE Request Received!</h1>
        
        <p>Your rescue request has been submitted successfully!</p>
        
        <div class="rescue-id">
            Rescue ID: {rescue_id}
        </div>
        
        <p>
            <strong>I'll contact you within 1-2 hours.</strong>
        </p>
        
        <p style="margin-top: 30px; color: #888;">
            Check your email for confirmation!
        </p>
        
        <p style="margin-top: 30px; font-size: 1.5rem; font-weight: bold; color: #00ff88;">
            RESCUE is on the way! 🚨
        </p>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    print("🚨 NOIZYLAB RESCUE - COMPLETE SYSTEM")
    print("=" * 60)
    print()
    print("SERVICE MODEL:")
    print("  🚨 NoizyLab RESCUE - We solve Mac problems!")
    print("  ✅ Most issues: PARTIALLY or COMPLETELY solvable")
    print("  💰 Pricing: $89 min if helped, $0 if not")
    print("  💪 Client can pay MORE if they want!")
    print()
    print("WHAT WE RESCUE:")
    print("  • Performance issues (slow, freezing)")
    print("  • Software problems (apps, updates)")
    print("  • Network issues (WiFi, email)")
    print("  • Data recovery")
    print("  • Security issues")
    print("  • Creative software (Logic, Pro Tools)")
    print()
    print("HARDWARE TRIAGE:")
    print("  • Software → We fix remotely!")
    print("  • Hardware (maybe) → Diagnose free, fix if possible")
    print("  • Hardware (definite) → Guide to Apple Store")
    print()
    print("EMAIL SYSTEM:")
    print("  ✅ Confirmation to client (via Mail.app!)")
    print("  ✅ Notification to you (via Mail.app!)")
    print("  ✅ All automated!")
    print()
    print("🌐 RESCUE Homepage: http://localhost:8000")
    print()
    print("GORUNFREE!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=8000, debug=True)

