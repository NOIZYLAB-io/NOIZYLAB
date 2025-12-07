#!/usr/bin/env python3
"""
🔧 SMART DIAGNOSTIC SYSTEM - HARDWARE vs SOFTWARE TRIAGE
Identifies if problem is fixable remotely or needs Apple Store
SAVES TIME, SETS EXPECTATIONS, PROFESSIONAL!!
"""

from flask import Flask, render_template_string, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DIAGNOSTIC_INTAKE_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔧 NoizyLab - Issue Diagnostic</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro', Arial, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 100%);
            color: #fff;
            padding: 20px;
            min-height: 100vh;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .header h1 {
            color: #00ff88;
            font-size: 3rem;
            margin-bottom: 10px;
        }
        
        .diagnostic-box {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 15px;
            padding: 40px;
        }
        
        .step {
            margin-bottom: 30px;
        }
        
        .step h2 {
            color: #00ff88;
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        
        .form-group {
            margin-bottom: 20px;
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
            min-height: 100px;
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
        
        .result-box {
            display: none;
            margin-top: 30px;
            padding: 30px;
            border-radius: 12px;
        }
        
        .result-box.show {
            display: block;
        }
        
        .can-fix {
            background: rgba(0,255,136,0.1);
            border: 2px solid #00ff88;
        }
        
        .hardware-issue {
            background: rgba(255,165,0,0.1);
            border: 2px solid #ffa500;
        }
        
        .apple-store {
            background: rgba(0,113,227,0.1);
            border: 2px solid #0071e3;
        }
        
        .result-box h3 {
            font-size: 1.8rem;
            margin-bottom: 15px;
        }
        
        .can-fix h3 { color: #00ff88; }
        .hardware-issue h3 { color: #ffa500; }
        .apple-store h3 { color: #0071e3; }
        
        .info-list {
            font-size: 1.1rem;
            line-height: 2;
            margin: 15px 0;
        }
        
        .action-btn {
            display: inline-block;
            padding: 15px 35px;
            background: #00ff88;
            color: #0f0f23;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            margin: 10px 5px;
            transition: all 0.3s;
        }
        
        .action-btn:hover {
            transform: scale(1.05);
        }
        
        .action-btn.apple {
            background: #0071e3;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔧 Issue Diagnostic</h1>
            <p style="font-size: 1.2rem; color: #888;">Let's identify your Mac issue</p>
        </div>
        
        <div class="diagnostic-box">
            <form id="diagnosticForm">
                <div class="step">
                    <h2>📱 Mac Information</h2>
                    
                    <div class="form-group">
                        <label>Mac Model</label>
                        <select name="mac_model" required>
                            <option value="">Select your Mac...</option>
                            <option value="m3">Mac M3 (2023-2024)</option>
                            <option value="m2">Mac M2 (2022-2023)</option>
                            <option value="m1">Mac M1 (2020-2021)</option>
                            <option value="intel_2019">Intel Mac (2019-2020)</option>
                            <option value="intel_2016">Intel Mac (2016-2018)</option>
                            <option value="intel_old">Intel Mac (2015 or older)</option>
                            <option value="unknown">Not sure</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>macOS Version</label>
                        <select name="macos_version" required>
                            <option value="">Select macOS version...</option>
                            <option value="sequoia">Sequoia (15.x)</option>
                            <option value="sonoma">Sonoma (14.x)</option>
                            <option value="ventura">Ventura (13.x)</option>
                            <option value="monterey">Monterey (12.x)</option>
                            <option value="bigsur">Big Sur (11.x)</option>
                            <option value="older">Catalina or older</option>
                            <option value="unknown">Not sure</option>
                        </select>
                    </div>
                </div>
                
                <div class="step">
                    <h2>🔍 Problem Description</h2>
                    
                    <div class="form-group">
                        <label>What's the issue?</label>
                        <select name="issue_type" id="issueType" required onchange="analyzeIssue()">
                            <option value="">Select issue type...</option>
                            
                            <optgroup label="Software Issues (Usually Fixable!)">
                                <option value="software_slow">Mac is running slow</option>
                                <option value="software_app">App won't open/crashes</option>
                                <option value="software_update">Update problems</option>
                                <option value="software_wifi">WiFi/network issues</option>
                                <option value="software_email">Email not working</option>
                                <option value="software_files">Files missing/corrupted</option>
                                <option value="software_password">Password/login issues</option>
                                <option value="software_other">Other software problem</option>
                            </optgroup>
                            
                            <optgroup label="Hardware Concerns">
                                <option value="hardware_screen">Screen issues (flickering, lines, black)</option>
                                <option value="hardware_keyboard">Keyboard not working</option>
                                <option value="hardware_trackpad">Trackpad not working</option>
                                <option value="hardware_battery">Battery draining fast</option>
                                <option value="hardware_ports">Ports not working</option>
                                <option value="hardware_heat">Overheating</option>
                                <option value="hardware_sound">No sound</option>
                                <option value="hardware_power">Won't turn on/boot</option>
                                <option value="hardware_physical">Physical damage</option>
                            </optgroup>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>Detailed Description</label>
                        <textarea name="description" placeholder="What exactly is happening? When did it start?" required></textarea>
                    </div>
                    
                    <div class="form-group">
                        <label>Your Email</label>
                        <input type="email" name="client_email" required placeholder="your@email.com">
                    </div>
                </div>
                
                <button type="submit" class="btn">
                    🔍 Analyze Issue
                </button>
            </form>
            
            <!-- RESULTS -->
            <div id="resultCanFix" class="result-box can-fix">
                <h3>✅ I Can Fix This Remotely!</h3>
                <div class="info-list">
                    <p>This is a <strong>software issue</strong> that can be resolved remotely.</p>
                    <p><strong>What happens next:</strong></p>
                    <ul style="margin: 15px 0 15px 25px; line-height: 2;">
                        <li>I'll connect remotely to your Mac</li>
                        <li>Fix the issue (usually 30-60 minutes)</li>
                        <li>If fixed → Payment of $89+ (you choose!)</li>
                        <li>If NOT fixed → You pay NOTHING</li>
                    </ul>
                </div>
                <a href="/payment" class="action-btn">
                    ✅ Proceed with Remote Fix
                </a>
            </div>
            
            <div id="resultHardware" class="result-box hardware-issue">
                <h3>⚠️ This Might Be Hardware</h3>
                <div class="info-list">
                    <p>This could be a <strong>hardware issue</strong>.</p>
                    <p><strong>Options:</strong></p>
                    <ul style="margin: 15px 0 15px 25px; line-height: 2;">
                        <li><strong>Option 1:</strong> I can diagnose remotely first (FREE diagnosis!)</li>
                        <li><strong>Option 2:</strong> If hardware confirmed → Apple Store needed</li>
                        <li>If I can fix it remotely → $89+ (you choose!)</li>
                        <li>If hardware repair needed → I'll guide you to Apple Store</li>
                    </ul>
                </div>
                <a href="#" onclick="proceedWithDiagnosis()" class="action-btn">
                    🔍 FREE Remote Diagnosis First
                </a>
                <a href="#" onclick="showAppleStore()" class="action-btn apple">
                    🍎 Find Apple Store
                </a>
            </div>
            
            <div id="resultAppleStore" class="result-box apple-store">
                <h3>🍎 Apple Store Recommended</h3>
                <div class="info-list">
                    <p>Based on your description, this likely needs <strong>Apple Store repair</strong>.</p>
                    <p><strong>Why:</strong></p>
                    <ul style="margin: 15px 0 15px 25px; line-height: 2;">
                        <li>Physical damage requires parts replacement</li>
                        <li>Hardware warranty might cover it</li>
                        <li>Apple has genuine parts</li>
                        <li>Professional hardware repair needed</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>I can still help:</strong></p>
                    <ul style="margin: 10px 0 15px 25px; line-height: 2;">
                        <li>Backup your data before repair</li>
                        <li>Prepare your Mac for service</li>
                        <li>Restore after repair</li>
                    </ul>
                </div>
                <a href="https://locate.apple.com" target="_blank" class="action-btn apple">
                    🍎 Find Nearest Apple Store
                </a>
                <a href="#" onclick="needsDataBackup()" class="action-btn">
                    💾 Help Me Backup First ($89)
                </a>
            </div>
        </div>
    </div>
    
    <script>
        function analyzeIssue() {
            // Hide all results
            document.querySelectorAll('.result-box').forEach(box => {
                box.classList.remove('show');
            });
        }
        
        document.getElementById('diagnosticForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/api/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                // Show appropriate result
                if (result.category === 'software') {
                    document.getElementById('resultCanFix').classList.add('show');
                } else if (result.category === 'hardware_maybe') {
                    document.getElementById('resultHardware').classList.add('show');
                } else if (result.category === 'hardware_definite') {
                    document.getElementById('resultAppleStore').classList.add('show');
                }
                
                // Scroll to result
                setTimeout(() => {
                    document.querySelector('.result-box.show').scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'start' 
                    });
                }, 100);
                
            } catch (error) {
                alert('Error analyzing issue: ' + error.message);
            }
        });
        
        function proceedWithDiagnosis() {
            alert('Great! I\\'ll do a FREE remote diagnosis first.\\n\\nIf fixable remotely → $89+\\nIf hardware needed → I\\'ll tell you upfront!');
            window.location.href = '/schedule-diagnosis';
        }
        
        function showAppleStore() {
            window.open('https://locate.apple.com', '_blank');
        }
        
        function needsDataBackup() {
            alert('I can backup your data before Apple Store visit!\\n\\nService: $89\\n\\nEnsures nothing is lost during repair.');
            window.location.href = '/payment?service=backup';
        }
    </script>
</body>
</html>
"""

class IssueDiagnostic:
    """Diagnose if issue is software (fixable) or hardware (Apple Store)"""
    
    def __init__(self):
        self.software_issues = [
            'software_slow', 'software_app', 'software_update',
            'software_wifi', 'software_email', 'software_files',
            'software_password', 'software_other'
        ]
        
        self.hardware_maybe = [
            'hardware_battery', 'hardware_ports', 'hardware_heat', 'hardware_sound'
        ]
        
        self.hardware_definite = [
            'hardware_screen', 'hardware_keyboard', 'hardware_trackpad',
            'hardware_power', 'hardware_physical'
        ]
    
    def analyze(self, issue_type, mac_model, description):
        """Analyze issue and recommend action"""
        
        # Software issues - can fix remotely!
        if issue_type in self.software_issues:
            return {
                'category': 'software',
                'fixable': True,
                'confidence': 0.95,
                'action': 'remote_fix',
                'pricing': 'pay_if_fixed',
                'message': 'This is a software issue I can fix remotely!'
            }
        
        # Definite hardware - needs Apple Store
        if issue_type in self.hardware_definite:
            # Check Mac age
            old_models = ['intel_2016', 'intel_old']
            
            if mac_model in old_models:
                return {
                    'category': 'hardware_definite',
                    'fixable': False,
                    'confidence': 0.9,
                    'action': 'apple_store',
                    'pricing': 'optional_backup',
                    'message': 'This is a hardware issue requiring Apple Store visit. Older Mac = likely needs parts.'
                }
            else:
                return {
                    'category': 'hardware_definite',
                    'fixable': False,
                    'confidence': 0.85,
                    'action': 'apple_store',
                    'pricing': 'optional_backup',
                    'message': 'This is a hardware issue requiring Apple Store. May be under warranty!'
                }
        
        # Maybe hardware - diagnose first
        if issue_type in self.hardware_maybe:
            return {
                'category': 'hardware_maybe',
                'fixable': 'maybe',
                'confidence': 0.6,
                'action': 'free_diagnosis',
                'pricing': 'pay_if_fixed',
                'message': 'Could be software OR hardware. Free diagnosis will determine!'
            }
        
        return {
            'category': 'unknown',
            'fixable': 'unknown',
            'confidence': 0.5,
            'action': 'contact',
            'pricing': 'tbd',
            'message': 'Need more information to diagnose.'
        }

diagnostic_engine = IssueDiagnostic()

@app.route('/')
def diagnostic_page():
    """Diagnostic intake page"""
    return render_template_string(DIAGNOSTIC_INTAKE_PAGE)

@app.route('/api/analyze', methods=['POST'])
def analyze_issue():
    """Analyze the issue"""
    try:
        data = request.json
        
        result = diagnostic_engine.analyze(
            data['issue_type'],
            data['mac_model'],
            data['description']
        )
        
        # Log intake
        intake = {
            'timestamp': datetime.now().isoformat(),
            'client_email': data['client_email'],
            'mac_model': data['mac_model'],
            'macos_version': data['macos_version'],
            'issue_type': data['issue_type'],
            'description': data['description'],
            'diagnosis': result
        }
        
        intakes = []
        if os.path.exists('diagnostic_log.json'):
            with open('diagnostic_log.json', 'r') as f:
                intakes = json.load(f)
        
        intakes.append(intake)
        
        with open('diagnostic_log.json', 'w') as f:
            json.dump(intakes, f, indent=2)
        
        print(f"📋 Diagnostic logged for {data['client_email']}")
        print(f"   Issue: {data['issue_type']}")
        print(f"   Category: {result['category']}")
        print(f"   Action: {result['action']}")
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("🔧 SMART DIAGNOSTIC SYSTEM")
    print("=" * 60)
    print()
    print("TRIAGE SYSTEM:")
    print("  ✅ SOFTWARE → I can fix remotely ($89+ if fixed)")
    print("  ⚠️  HARDWARE (Maybe) → FREE diagnosis first")
    print("  🍎 HARDWARE (Definite) → Apple Store needed")
    print()
    print("PRICING:")
    print("  • Software fix: $89+ (only if fixed!)")
    print("  • Hardware diagnosis: FREE")
    print("  • Data backup before Apple Store: $89")
    print("  • If I can't fix: $0 (NO CHARGE!)")
    print()
    print("🌐 Diagnostic Page: http://localhost:5002")
    print()
    print("HONEST, FAIR, PROFESSIONAL!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=5002, debug=True)

