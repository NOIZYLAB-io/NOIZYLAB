#!/usr/bin/env python3
"""
🖥️ TEAMVIEWER REMOTE REPAIR SYSTEM - COMPLETE INTEGRATION
Remote access for Mac repairs via TeamViewer
Automated session management, client instructions, post-repair follow-up
"""

from flask import Flask, render_template_string, request, jsonify, redirect
import json
import os
from datetime import datetime
import sys

# Mail.app for instructions
sys.path.append('../FishMusic_Email_System')
from MAIL_APP_COMPLETE_SYSTEM import MailAppMailer

app = Flask(__name__)
mailer = MailAppMailer()

DATA_DIR = "teamviewer_sessions"
os.makedirs(DATA_DIR, exist_ok=True)

# CLIENT INSTRUCTIONS PAGE - TEAMVIEWER SETUP
TEAMVIEWER_INSTRUCTIONS = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🖥️ TeamViewer Setup - NoizyLab RESCUE</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro', Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 20px;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .header {
            background: linear-gradient(135deg, #0e4aff 0%, #0038cc 100%);
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 40px;
        }
        
        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
        }
        
        .step-box {
            background: rgba(255,255,255,0.05);
            border: 2px solid #0e4aff;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 25px;
        }
        
        .step-box h2 {
            color: #0e4aff;
            margin-bottom: 20px;
            font-size: 1.8rem;
        }
        
        .step-number {
            display: inline-block;
            background: #0e4aff;
            color: #fff;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            text-align: center;
            line-height: 40px;
            font-weight: bold;
            margin-right: 10px;
        }
        
        .download-btn {
            display: inline-block;
            padding: 20px 40px;
            background: #0e4aff;
            color: #fff;
            text-decoration: none;
            border-radius: 10px;
            font-size: 1.3rem;
            font-weight: 600;
            transition: all 0.3s;
            margin: 15px 0;
        }
        
        .download-btn:hover {
            background: #0038cc;
            transform: scale(1.05);
        }
        
        .id-display {
            background: rgba(0,0,0,0.4);
            border: 2px solid #00ff88;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }
        
        .id-display .label {
            color: #888;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        
        .id-display .id {
            font-size: 2.5rem;
            font-weight: bold;
            color: #00ff88;
            font-family: monospace;
            letter-spacing: 3px;
        }
        
        .note {
            background: rgba(255,165,0,0.1);
            border-left: 4px solid #ffa500;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }
        
        ul {
            line-height: 2;
            margin-left: 25px;
            font-size: 1.1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🖥️ Remote Access Setup</h1>
            <p style="font-size: 1.2rem;">Quick setup for NoizyLab RESCUE</p>
        </div>
        
        <!-- STEP 1: DOWNLOAD -->
        <div class="step-box">
            <h2><span class="step-number">1</span> Download TeamViewer</h2>
            <p style="margin-bottom: 20px; font-size: 1.1rem;">
                Download the FREE TeamViewer QuickSupport app:
            </p>
            <a href="https://www.teamviewer.com/en/download/mac-os/" target="_blank" class="download-btn">
                📥 Download TeamViewer for Mac
            </a>
            <div class="note">
                <strong>💡 Tip:</strong> Download "TeamViewer QuickSupport" - it's the simplest version for receiving help!
            </div>
        </div>
        
        <!-- STEP 2: INSTALL -->
        <div class="step-box">
            <h2><span class="step-number">2</span> Install & Open</h2>
            <ul>
                <li>Open the downloaded file</li>
                <li>Drag TeamViewer to Applications (if asked)</li>
                <li>Double-click to open TeamViewer</li>
                <li>Allow any permissions it asks for</li>
            </ul>
        </div>
        
        <!-- STEP 3: GET ID -->
        <div class="step-box">
            <h2><span class="step-number">3</span> Get Your ID & Password</h2>
            <p style="margin-bottom: 20px; font-size: 1.1rem;">
                TeamViewer will show you two things:
            </p>
            
            <div class="id-display">
                <div class="label">Your ID (looks like this):</div>
                <div class="id">123 456 789</div>
            </div>
            
            <div class="id-display">
                <div class="label">Your Password (looks like this):</div>
                <div class="id">abcd12</div>
            </div>
            
            <p style="margin-top: 20px; font-size: 1.1rem;">
                <strong>Send me these two numbers!</strong>
            </p>
        </div>
        
        <!-- STEP 4: SHARE ID -->
        <div class="step-box">
            <h2><span class="step-number">4</span> Share Your ID & Password</h2>
            
            <form id="idForm">
                <div style="margin-bottom: 15px;">
                    <label style="display: block; color: #0e4aff; margin-bottom: 8px;">TeamViewer ID</label>
                    <input type="text" name="teamviewer_id" placeholder="123 456 789" required
                           style="width: 100%; padding: 15px; background: rgba(255,255,255,0.05); border: 1px solid #0e4aff; border-radius: 8px; color: #fff; font-size: 1.2rem; text-align: center;">
                </div>
                
                <div style="margin-bottom: 20px;">
                    <label style="display: block; color: #0e4aff; margin-bottom: 8px;">TeamViewer Password</label>
                    <input type="text" name="teamviewer_password" placeholder="abcd12" required
                           style="width: 100%; padding: 15px; background: rgba(255,255,255,0.05); border: 1px solid #0e4aff; border-radius: 8px; color: #fff; font-size: 1.2rem; text-align: center;">
                </div>
                
                <button type="submit" style="width: 100%; padding: 18px; background: #00ff88; color: #0f0f23; border: none; border-radius: 10px; font-size: 1.2rem; font-weight: 600; cursor: pointer;">
                    ✅ Submit - Ready for Remote Access
                </button>
            </form>
            
            <div class="note" style="margin-top: 20px;">
                <strong>🔒 Security:</strong> I'll only connect when you're ready. You'll see me connect and can stop anytime!
            </div>
        </div>
        
        <!-- WHAT HAPPENS NEXT -->
        <div class="step-box" style="border-color: #00ff88; background: rgba(0,255,136,0.05);">
            <h2 style="color: #00ff88;"><span class="step-number" style="background: #00ff88; color: #0f0f23;">5</span> What Happens Next</h2>
            <ul style="color: #ccc;">
                <li>I'll connect to your Mac remotely</li>
                <li>You'll see everything I do on screen</li>
                <li>I'll diagnose and fix the issue</li>
                <li>Usually takes 30-90 minutes</li>
                <li>If fixed → Pay $89+ (your choice!)</li>
                <li>If not fixed → Pay NOTHING!</li>
            </ul>
        </div>
    </div>
    
    <script>
        document.getElementById('idForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/api/teamviewer/save', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    alert('✅ Submitted!\\n\\nI have your TeamViewer details and will connect shortly!\\n\\nKeep TeamViewer open!');
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

# TEAMVIEWER SESSION MANAGER
class TeamViewerManager:
    """Manage TeamViewer remote sessions"""
    
    def __init__(self):
        self.sessions_file = os.path.join(DATA_DIR, 'sessions.json')
        self.sessions = self.load_sessions()
    
    def load_sessions(self):
        """Load TeamViewer sessions"""
        if os.path.exists(self.sessions_file):
            with open(self.sessions_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_sessions(self):
        """Save sessions"""
        with open(self.sessions_file, 'w') as f:
            json.dump(self.sessions, f, indent=2)
    
    def create_session(self, rescue_id, client_name, client_email, teamviewer_id, teamviewer_password):
        """Create new TeamViewer session"""
        session = {
            'id': len(self.sessions) + 1,
            'rescue_id': rescue_id,
            'client_name': client_name,
            'client_email': client_email,
            'teamviewer_id': teamviewer_id,
            'teamviewer_password': teamviewer_password,
            'status': 'pending',
            'created': datetime.now().isoformat(),
            'started': None,
            'completed': None,
            'outcome': None,
            'notes': ''
        }
        
        self.sessions.append(session)
        self.save_sessions()
        
        print(f"🖥️  TeamViewer session created!")
        print(f"   Rescue ID: {rescue_id}")
        print(f"   TeamViewer ID: {teamviewer_id}")
        
        return session
    
    def start_session(self, session_id):
        """Mark session as started"""
        for session in self.sessions:
            if session['id'] == session_id:
                session['status'] = 'active'
                session['started'] = datetime.now().isoformat()
                self.save_sessions()
                break
    
    def complete_session(self, session_id, outcome, notes):
        """Complete session"""
        for session in self.sessions:
            if session['id'] == session_id:
                session['status'] = 'completed'
                session['completed'] = datetime.now().isoformat()
                session['outcome'] = outcome  # 'fixed', 'partially_fixed', 'not_fixed', 'hardware_needed'
                session['notes'] = notes
                self.save_sessions()
                
                # Send follow-up email based on outcome
                self.send_completion_email(session)
                break
    
    def send_completion_email(self, session):
        """Send completion email to client"""
        client_email = session['client_email']
        client_name = session['client_name']
        outcome = session['outcome']
        
        if outcome == 'fixed':
            subject = "✅ Your Mac is Fixed! - NoizyLab RESCUE"
            body = f"""
Hi {client_name}!

Great news - your Mac issue is FIXED! ✅

Remote session completed successfully.

WHAT WE FIXED:
{session['notes']}

PAYMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your issue is SOLVED!

Payment: $89 minimum (you can pay more if you felt the service was exceptional!)

Payment Methods:
• Stripe: [link will be sent]
• PayPal: rsp@noizyfish.com
• e-Transfer: rsp@noizylab.ca

Choose what you'd like to pay - minimum $89.

Thank you for trusting NoizyLab RESCUE!

Rob @ NoizyLab
noizylab.ca
rsplowman@icloud.com
"""
            
        elif outcome == 'partially_fixed':
            subject = "⚠️ Partially Resolved - NoizyLab RESCUE"
            body = f"""
Hi {client_name},

I was able to PARTIALLY resolve your issue.

WHAT WAS FIXED:
{session['notes']}

REMAINING ISSUES:
Some aspects may require additional work or hardware repair.

PAYMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Since I helped partially, payment is optional:

• If you feel it helped: $89+ (you choose!)
• If you don't feel it helped enough: $0 (no charge)

Payment Methods (if you'd like to pay):
• PayPal: rsp@noizyfish.com
• e-Transfer: rsp@noizylab.ca

Fair is fair!

Rob @ NoizyLab
"""
            
        elif outcome == 'hardware_needed':
            subject = "🍎 Hardware Repair Needed - NoizyLab RESCUE"
            body = f"""
Hi {client_name},

After remote diagnosis, your issue requires HARDWARE REPAIR.

DIAGNOSIS:
{session['notes']}

RECOMMENDATION:
Visit Apple Store or authorized repair center.

PAYMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NO CHARGE for diagnosis!

I couldn't fix it remotely, so you pay NOTHING.
That's our guarantee!

If you need help:
• Backing up before repair: $89
• Restoring after repair: $89
• Both: $150

Let me know if you want backup help!

Rob @ NoizyLab
"""
            
        else:  # not_fixed
            subject = "Unfortunately Not Fixed - NoizyLab"
            body = f"""
Hi {client_name},

Unfortunately, I wasn't able to resolve your issue remotely.

{session['notes']}

PAYMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NO CHARGE

I couldn't fix it, so you pay NOTHING.
That's our guarantee - you only pay for results!

Sorry I couldn't help this time!

Rob @ NoizyLab
"""
        
        mailer.send_email(client_email, subject, body)

tv_manager = TeamViewerManager()

# ROUTES
@app.route('/')
def instructions_page():
    """TeamViewer setup instructions"""
    return render_template_string(TEAMVIEWER_INSTRUCTIONS)

@app.route('/api/teamviewer/save', methods=['POST'])
def save_teamviewer_info():
    """Save TeamViewer ID & password"""
    try:
        data = request.json
        
        # Create session record
        session = {
            'teamviewer_id': data['teamviewer_id'],
            'teamviewer_password': data['teamviewer_password'],
            'submitted': datetime.now().isoformat(),
            'status': 'ready'
        }
        
        # Save to file
        sessions_file = os.path.join(DATA_DIR, 'pending_sessions.json')
        
        sessions = []
        if os.path.exists(sessions_file):
            with open(sessions_file, 'r') as f:
                sessions = json.load(f)
        
        sessions.append(session)
        
        with open(sessions_file, 'w') as f:
            json.dump(sessions, f, indent=2)
        
        # Email YOU with the TeamViewer details
        mailer.send_email(
            "rsplowman@icloud.com",
            f"🖥️ TeamViewer Access Ready!",
            f"""
CLIENT IS READY FOR REMOTE ACCESS!

TeamViewer ID: {data['teamviewer_id']}
Password: {data['teamviewer_password']}

Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

CONNECT NOW:
1. Open TeamViewer on your Mac
2. Enter their ID: {data['teamviewer_id']}
3. Enter password when prompted: {data['teamviewer_password']}
4. Start the RESCUE!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTER SESSION:
• Mark outcome (fixed/partial/not fixed)
• System will auto-email client
• If fixed → They pay $89+
• If not → No charge

GORUNFREE!! 🚀
"""
        )
        
        print(f"✅ TeamViewer session ready!")
        print(f"   ID: {data['teamviewer_id']}")
        print(f"   Password: {data['teamviewer_password']}")
        print(f"   ✅ Email sent to you with details!")
        
        return jsonify({'success': True})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/session/complete/<session_id>/<outcome>')
def complete_session(session_id, outcome):
    """Mark session as complete"""
    notes = request.args.get('notes', '')
    
    tv_manager.complete_session(int(session_id), outcome, notes)
    
    return f"""
<!DOCTYPE html>
<html>
<head><title>Session Complete</title></head>
<body style="background: #0f0f23; color: #fff; padding: 40px; text-align: center; font-family: Arial;">
    <h1 style="color: #00ff88; font-size: 3rem;">✅ Session Completed!</h1>
    <p style="font-size: 1.3rem; margin: 20px 0;">
        Outcome: <strong>{outcome.replace('_', ' ').title()}</strong>
    </p>
    <p style="color: #888;">
        Client has been notified via email!
    </p>
</body>
</html>
"""

if __name__ == '__main__':
    print("🖥️  TEAMVIEWER REMOTE REPAIR SYSTEM")
    print("=" * 60)
    print()
    print("NOIZYLAB RESCUE - REMOTE ACCESS:")
    print()
    print("  🖥️  TeamViewer for remote Mac access")
    print("  📧 Automated client instructions")
    print("  ✅ Session tracking")
    print("  💰 Payment based on outcome")
    print()
    print("WORKFLOW:")
    print("  1. Client submits RESCUE request")
    print("  2. You send them TeamViewer instructions")
    print("  3. They install & share ID/password")
    print("  4. You connect remotely")
    print("  5. Fix the issue!")
    print("  6. Mark outcome (fixed/partial/not fixed)")
    print("  7. System auto-emails client")
    print("  8. Client pays if helped ($89+)")
    print()
    print("CLIENT INSTRUCTIONS: http://localhost:8001")
    print()
    print("INTEGRATION:")
    print("  ✅ Email system (Mail.app!)")
    print("  ✅ RESCUE request system")
    print("  ✅ Payment system")
    print("  ✅ All automated!")
    print()
    print("GORUNFREE!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=8001, debug=True)

