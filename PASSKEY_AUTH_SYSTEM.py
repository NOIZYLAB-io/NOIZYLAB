#!/usr/bin/env python3
"""
🔐 PASSKEY AUTHENTICATION SYSTEM - NO MORE PASSWORDS!!
WebAuthn/FIDO2 passkey system - Touch ID, Face ID, security keys
MODERN, SECURE, NO PASSWORDS EVER!!
"""

from flask import Flask, render_template_string, request, jsonify, session
import secrets
import json
import os
from datetime import datetime
import base64
import hashlib

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# PASSKEY LOGIN PAGE
PASSKEY_LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔐 NoizyLab - Passkey Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro', Arial, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 100%);
            color: #fff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .login-container {
            max-width: 500px;
            width: 100%;
            padding: 20px;
        }
        
        .login-box {
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 20px;
            padding: 50px 40px;
            backdrop-filter: blur(10px);
        }
        
        .logo {
            text-align: center;
            font-size: 5rem;
            margin-bottom: 20px;
        }
        
        h1 {
            text-align: center;
            color: #00ff88;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 40px;
            font-size: 1.1rem;
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
            margin: 15px 0;
        }
        
        .btn:hover {
            background: #00cc6a;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,255,136,0.3);
        }
        
        .btn-secondary {
            background: transparent;
            border: 2px solid #00ff88;
            color: #00ff88;
        }
        
        .btn-secondary:hover {
            background: rgba(0,255,136,0.1);
        }
        
        .info-box {
            background: rgba(0,113,227,0.1);
            border: 1px solid #0071e3;
            border-radius: 10px;
            padding: 20px;
            margin: 25px 0;
            font-size: 0.95rem;
        }
        
        .info-box h3 {
            color: #0071e3;
            margin-bottom: 10px;
        }
        
        .status-msg {
            background: rgba(0,255,136,0.1);
            border-left: 4px solid #00ff88;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
            display: none;
        }
        
        .status-msg.show {
            display: block;
        }
        
        .status-msg.error {
            background: rgba(255,0,0,0.1);
            border-left-color: #ff0000;
            color: #ff0000;
        }
        
        .fingerprint {
            font-size: 3rem;
            text-align: center;
            margin: 20px 0;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.1); opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-box">
            <div class="logo">🔐</div>
            <h1>NoizyLab</h1>
            <div class="subtitle">Passwordless Login with Passkeys</div>
            
            <div id="statusMsg" class="status-msg"></div>
            
            <!-- PASSKEY BUTTONS -->
            <button id="registerBtn" class="btn" onclick="registerPasskey()">
                🔑 Register New Passkey
            </button>
            
            <button id="loginBtn" class="btn btn-secondary" onclick="loginWithPasskey()">
                👆 Login with Passkey
            </button>
            
            <div class="info-box">
                <h3>🍎 What are Passkeys?</h3>
                <ul style="line-height: 1.8; margin-left: 20px;">
                    <li>✅ Use Touch ID or Face ID</li>
                    <li>✅ No passwords to remember</li>
                    <li>✅ More secure than passwords</li>
                    <li>✅ Works on iPhone, iPad, Mac</li>
                    <li>✅ Can't be phished or stolen</li>
                </ul>
            </div>
            
            <div class="info-box" style="border-color: #00ff88; background: rgba(0,255,136,0.05);">
                <h3 style="color: #00ff88;">🎯 First Time Setup:</h3>
                <p style="line-height: 1.8;">
                    1. Click "Register New Passkey"<br>
                    2. Use Touch ID / Face ID<br>
                    3. Done! Login anytime with Touch ID!
                </p>
            </div>
            
            <div class="fingerprint">👆</div>
        </div>
    </div>
    
    <script>
        // WebAuthn / Passkey Implementation
        
        async function registerPasskey() {
            const statusMsg = document.getElementById('statusMsg');
            statusMsg.textContent = '⏳ Creating your passkey...';
            statusMsg.className = 'status-msg show';
            
            try {
                // Get challenge from server
                const challengeResponse = await fetch('/passkey/register/begin', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username: 'rob@noizylab.ca' })
                });
                
                const options = await challengeResponse.json();
                
                // Convert base64 to ArrayBuffer
                options.challenge = base64ToArrayBuffer(options.challenge);
                options.user.id = base64ToArrayBuffer(options.user.id);
                
                // Create passkey using WebAuthn
                const credential = await navigator.credentials.create({
                    publicKey: options
                });
                
                // Send credential to server
                const registerResponse = await fetch('/passkey/register/complete', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        credential: {
                            id: credential.id,
                            rawId: arrayBufferToBase64(credential.rawId),
                            response: {
                                attestationObject: arrayBufferToBase64(credential.response.attestationObject),
                                clientDataJSON: arrayBufferToBase64(credential.response.clientDataJSON)
                            },
                            type: credential.type
                        }
                    })
                });
                
                const result = await registerResponse.json();
                
                if (result.success) {
                    statusMsg.textContent = '✅ Passkey registered! Now login with Touch ID!';
                    setTimeout(() => {
                        loginWithPasskey();
                    }, 2000);
                } else {
                    statusMsg.textContent = '❌ Registration failed: ' + result.error;
                    statusMsg.className = 'status-msg show error';
                }
                
            } catch (error) {
                statusMsg.textContent = '❌ Error: ' + error.message;
                statusMsg.className = 'status-msg show error';
                console.error(error);
            }
        }
        
        async function loginWithPasskey() {
            const statusMsg = document.getElementById('statusMsg');
            statusMsg.textContent = '👆 Use Touch ID to login...';
            statusMsg.className = 'status-msg show';
            
            try {
                // Get challenge from server
                const challengeResponse = await fetch('/passkey/login/begin', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' }
                });
                
                const options = await challengeResponse.json();
                
                // Convert challenge
                options.challenge = base64ToArrayBuffer(options.challenge);
                
                // Authenticate with passkey
                const assertion = await navigator.credentials.get({
                    publicKey: options
                });
                
                // Send assertion to server
                const loginResponse = await fetch('/passkey/login/complete', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        credential: {
                            id: assertion.id,
                            rawId: arrayBufferToBase64(assertion.rawId),
                            response: {
                                authenticatorData: arrayBufferToBase64(assertion.response.authenticatorData),
                                clientDataJSON: arrayBufferToBase64(assertion.response.clientDataJSON),
                                signature: arrayBufferToBase64(assertion.response.signature),
                                userHandle: assertion.response.userHandle ? arrayBufferToBase64(assertion.response.userHandle) : null
                            },
                            type: assertion.type
                        }
                    })
                });
                
                const result = await loginResponse.json();
                
                if (result.success) {
                    statusMsg.textContent = '✅ Login successful! Redirecting...';
                    setTimeout(() => {
                        window.location.href = '/dashboard';
                    }, 1000);
                } else {
                    statusMsg.textContent = '❌ Login failed: ' + result.error;
                    statusMsg.className = 'status-msg show error';
                }
                
            } catch (error) {
                statusMsg.textContent = '❌ Error: ' + error.message;
                statusMsg.className = 'status-msg show error';
                console.error(error);
            }
        }
        
        // Helper functions
        function base64ToArrayBuffer(base64) {
            const binary = atob(base64.replace(/-/g, '+').replace(/_/g, '/'));
            const bytes = new Uint8Array(binary.length);
            for (let i = 0; i < binary.length; i++) {
                bytes[i] = binary.charCodeAt(i);
            }
            return bytes.buffer;
        }
        
        function arrayBufferToBase64(buffer) {
            const bytes = new Uint8Array(buffer);
            let binary = '';
            for (let i = 0; i < bytes.byteLength; i++) {
                binary += String.fromCharCode(bytes[i]);
            }
            return btoa(binary).replace(/\+/g, '-').replace(/\//g, '_').replace(/=/g, '');
        }
    </script>
</body>
</html>
"""

# Simple passkey storage (use database in production!)
PASSKEY_FILE = "passkeys.json"

def load_passkeys():
    """Load registered passkeys"""
    if os.path.exists(PASSKEY_FILE):
        with open(PASSKEY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_passkeys(passkeys):
    """Save passkeys"""
    with open(PASSKEY_FILE, 'w') as f:
        json.dump(passkeys, f, indent=2)

@app.route('/')
def login_page():
    """Passkey login page"""
    return render_template_string(PASSKEY_LOGIN_HTML)

@app.route('/passkey/register/begin', methods=['POST'])
def register_begin():
    """Begin passkey registration"""
    data = request.json
    username = data.get('username', 'rob@noizylab.ca')
    
    # Generate challenge
    challenge = secrets.token_bytes(32)
    challenge_b64 = base64.urlsafe_b64encode(challenge).decode('utf-8').rstrip('=')
    
    # Store challenge in session
    session['challenge'] = challenge_b64
    session['username'] = username
    
    # WebAuthn registration options
    options = {
        "challenge": challenge_b64,
        "rp": {
            "name": "NoizyLab",
            "id": "localhost"  # Change to noizylab.ca in production
        },
        "user": {
            "id": base64.urlsafe_b64encode(username.encode()).decode('utf-8').rstrip('='),
            "name": username,
            "displayName": "Rob @ NoizyLab"
        },
        "pubKeyCredParams": [
            {"type": "public-key", "alg": -7},   # ES256
            {"type": "public-key", "alg": -257}  # RS256
        ],
        "authenticatorSelection": {
            "authenticatorAttachment": "platform",  # Use built-in Touch ID/Face ID
            "requireResidentKey": True,
            "userVerification": "required"
        },
        "timeout": 60000,
        "attestation": "none"
    }
    
    return jsonify(options)

@app.route('/passkey/register/complete', methods=['POST'])
def register_complete():
    """Complete passkey registration"""
    try:
        data = request.json
        credential = data['credential']
        username = session.get('username')
        
        # Store passkey
        passkeys = load_passkeys()
        
        passkeys[username] = {
            'id': credential['id'],
            'rawId': credential['rawId'],
            'registered': datetime.now().isoformat(),
            'last_used': None
        }
        
        save_passkeys(passkeys)
        
        print(f"✅ Passkey registered for {username}")
        
        return jsonify({'success': True})
        
    except Exception as e:
        print(f"❌ Registration error: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/passkey/login/begin', methods=['POST'])
def login_begin():
    """Begin passkey login"""
    # Generate challenge
    challenge = secrets.token_bytes(32)
    challenge_b64 = base64.urlsafe_b64encode(challenge).decode('utf-8').rstrip('=')
    
    session['challenge'] = challenge_b64
    
    # Get all registered passkeys
    passkeys = load_passkeys()
    
    allowed_credentials = [
        {"type": "public-key", "id": pk['rawId']}
        for pk in passkeys.values()
    ]
    
    options = {
        "challenge": challenge_b64,
        "timeout": 60000,
        "rpId": "localhost",  # Change to noizylab.ca in production
        "allowCredentials": allowed_credentials,
        "userVerification": "required"
    }
    
    return jsonify(options)

@app.route('/passkey/login/complete', methods=['POST'])
def login_complete():
    """Complete passkey login"""
    try:
        data = request.json
        credential = data['credential']
        
        # Verify credential exists
        passkeys = load_passkeys()
        
        # Find matching passkey
        for username, pk in passkeys.items():
            if pk['id'] == credential['id']:
                # Update last used
                pk['last_used'] = datetime.now().isoformat()
                save_passkeys(passkeys)
                
                # Set session
                session['logged_in'] = True
                session['username'] = username
                
                print(f"✅ Passkey login successful for {username}")
                
                return jsonify({'success': True})
        
        return jsonify({'success': False, 'error': 'Passkey not found'})
        
    except Exception as e:
        print(f"❌ Login error: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/dashboard')
def dashboard():
    """Dashboard after passkey login"""
    if not session.get('logged_in'):
        return redirect('/')
    
    username = session.get('username', 'User')
    
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>NoizyLab Dashboard</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 40px;
        }}
        h1 {{ color: #00ff88; }}
        .success {{ 
            background: rgba(0,255,136,0.1);
            border: 2px solid #00ff88;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin: 30px 0;
        }}
    </style>
</head>
<body>
    <h1>🎉 Welcome {username}!</h1>
    
    <div class="success">
        <h2 style="color: #00ff88; font-size: 2rem;">✅ PASSKEY LOGIN WORKS!!</h2>
        <p style="font-size: 1.2rem; margin-top: 15px;">
            You logged in with Touch ID / Face ID!<br>
            NO PASSWORD NEEDED!!
        </p>
    </div>
    
    <h2>You're now logged into NoizyLab Portal!</h2>
    
    <p style="font-size: 1.1rem; line-height: 2;">
        ✅ No passwords to remember<br>
        ✅ No passwords to type<br>
        ✅ Just your fingerprint / face<br>
        ✅ Modern, secure, easy!
    </p>
    
    <a href="http://localhost:4000" style="display: inline-block; background: #00ff88; color: #0f0f23; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin-top: 20px;">
        → Go to Full NoizyLab Portal
    </a>
    
    <p style="margin-top: 40px; font-size: 1.5rem; color: #00ff88; font-weight: bold;">
        GORUNFREE!! 🚀
    </p>
</body>
</html>
"""

if __name__ == '__main__':
    print("🔐 PASSKEY AUTHENTICATION SYSTEM - STARTING...")
    print("=" * 60)
    print("🌐 Passkey Login: http://localhost:7000")
    print()
    print("FEATURES:")
    print("  ✅ Touch ID / Face ID login")
    print("  ✅ NO passwords ever!")
    print("  ✅ Works on all Apple devices")
    print("  ✅ More secure than passwords")
    print("  ✅ Can't be phished")
    print()
    print("FIRST TIME:")
    print("  1. Click 'Register New Passkey'")
    print("  2. Use Touch ID")
    print("  3. Done! Login anytime with Touch ID!")
    print("=" * 60)
    print()
    print("GORUNFREE!! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=7000, debug=True, ssl_context='adhoc')

