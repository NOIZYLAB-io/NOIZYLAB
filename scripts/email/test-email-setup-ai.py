#!/usr/bin/env python3
"""
Local Email Setup AI - Test Version
===================================
Test the email setup AI locally before deploying to Cloudflare
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Email Setup AI - Local Test")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SetupRequest(BaseModel):
    email: str
    device: str
    step: Optional[str] = "initial"

# Email configurations
EMAIL_CONFIGS = [
    {
        "email": "rspplowman@gmail.com",
        "type": "Gmail",
        "imap": "imap.gmail.com:993",
        "smtp": "smtp.gmail.com:587",
        "notes": "Use App Password from Google Account"
    },
    {
        "email": "rsp@noizylab.ca",
        "type": "NoizyLab",
        "imap": "imap.gmail.com:993",
        "smtp": "smtp.gmail.com:587",
        "notes": "Google Workspace - Use App Password"
    },
    {
        "email": "help@noizylab.ca",
        "type": "NoizyLab",
        "imap": "imap.gmail.com:993",
        "smtp": "smtp.gmail.com:587",
        "notes": "Google Workspace - Use App Password"
    },
    {
        "email": "hello@noizylab.ca",
        "type": "NoizyLab",
        "imap": "imap.gmail.com:993",
        "smtp": "smtp.gmail.com:587",
        "notes": "Google Workspace - Use App Password"
    },
    {
        "email": "rp@fishmusicinc.com",
        "type": "Fish Music",
        "imap": "imap.gmail.com:993",
        "smtp": "smtp.gmail.com:587",
        "notes": "Google Workspace - Use App Password"
    },
    {
        "email": "info@fishmusicinc.com",
        "type": "Fish Music",
        "imap": "imap.gmail.com:993",
        "smtp": "smtp.gmail.com:587",
        "notes": "Google Workspace - Use App Password"
    }
]

def generate_instructions(email: str, device: str) -> dict:
    """Generate setup instructions"""
    config = next((c for c in EMAIL_CONFIGS if c["email"] == email), None)
    
    if not config:
        return {"error": "Email not found"}
    
    is_gmail = "gmail.com" in email
    
    instructions = {
        "step1": f"Open Settings on your {device}",
        "step2": 'Tap "Mail" → "Accounts" → "Add Account"',
        "step3": 'Select "Google"' if is_gmail else 'Select "Other" → "Add Mail Account"',
        "step4": f"Enter your email: {email}",
        "step5": f"Enter your App Password (get from: https://myaccount.google.com/apppasswords)",
        "step6": "Enable Mail, Contacts, Calendars" if is_gmail else f"Enter IMAP: {config['imap']} (SSL), SMTP: {config['smtp']} (TLS)",
        "step7": 'Tap "Save" and wait for verification',
        "step8": f"Note: {config['notes']}"
    }
    
    return instructions

@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve web interface"""
    html = """<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NoizyLab Email Setup - AI Assistant</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      padding: 20px;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      background: white;
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    h1 {
      color: #667eea;
      margin-bottom: 10px;
      font-size: 28px;
    }
    .subtitle {
      color: #666;
      margin-bottom: 30px;
    }
    .email-list {
      margin: 20px 0;
    }
    .email-item {
      background: #f5f5f5;
      padding: 15px;
      margin: 10px 0;
      border-radius: 10px;
      cursor: pointer;
      transition: all 0.3s;
    }
    .email-item:hover, .email-item.active {
      background: #667eea;
      color: white;
    }
    select, button {
      width: 100%;
      padding: 15px;
      border: 2px solid #ddd;
      border-radius: 10px;
      font-size: 16px;
      margin: 10px 0;
    }
    button {
      background: #667eea;
      color: white;
      border: none;
      cursor: pointer;
      font-weight: bold;
    }
    button:hover {
      background: #5568d3;
    }
    .instructions {
      margin-top: 30px;
      padding: 20px;
      background: #f9f9f9;
      border-radius: 10px;
      display: none;
    }
    .instructions.show {
      display: block;
    }
    .step {
      margin: 15px 0;
      padding: 15px;
      background: white;
      border-left: 4px solid #667eea;
      border-radius: 5px;
    }
    .step-number {
      font-weight: bold;
      color: #667eea;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🤖 Email Setup AI</h1>
    <p class="subtitle">AI-powered email setup for your iPad and iPhone</p>
    
    <div>
      <label>Select Device:</label>
      <select id="device">
        <option value="iPhone">iPhone</option>
        <option value="iPad">iPad</option>
      </select>
    </div>
    
    <div class="email-list" id="emailList"></div>
    
    <button onclick="setupEmail()">🤖 Get AI Setup Instructions</button>
    
    <div class="instructions" id="instructions">
      <h3>📋 Setup Instructions:</h3>
      <div id="steps"></div>
    </div>
  </div>
  
  <script>
    let selectedEmail = '';
    const emails = """ + str(EMAIL_CONFIGS).replace("'", '"') + """;
    
    // Render email list
    const list = document.getElementById('emailList');
    emails.forEach(config => {
      const div = document.createElement('div');
      div.className = 'email-item';
      div.textContent = config.email + ' (' + config.type + ')';
      div.onclick = () => {
        document.querySelectorAll('.email-item').forEach(e => e.classList.remove('active'));
        div.classList.add('active');
        selectedEmail = config.email;
      };
      list.appendChild(div);
    });
    
    async function setupEmail() {
      if (!selectedEmail) {
        alert('Please select an email address');
        return;
      }
      
      const device = document.getElementById('device').value;
      const instructionsDiv = document.getElementById('instructions');
      const stepsDiv = document.getElementById('steps');
      instructionsDiv.classList.add('show');
      stepsDiv.innerHTML = '<div class="step">🤖 Generating instructions...</div>';
      
      try {
        const response = await fetch('/setup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: selectedEmail, device: device })
        });
        
        const data = await response.json();
        
        if (data.instructions) {
          stepsDiv.innerHTML = Object.entries(data.instructions)
            .map(([key, value]) => `<div class="step"><span class="step-number">${key.replace('step', 'Step ')}:</span> ${value}</div>`)
            .join('');
        }
      } catch (error) {
        stepsDiv.innerHTML = '<div class="step">Error: ' + error.message + '</div>';
      }
    }
  </script>
</body>
</html>"""
    return html

@app.get("/configs")
async def get_configs():
    """Get email configurations"""
    return {"configs": EMAIL_CONFIGS}

@app.post("/setup")
async def setup_email(request: SetupRequest):
    """Get setup instructions"""
    instructions = generate_instructions(request.email, request.device)
    return {
        "success": True,
        "instructions": instructions,
        "email": request.email,
        "device": request.device
    }

if __name__ == "__main__":
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print("🤖 Email Setup AI - Local Test Server")
    print("=====================================")
    print()
    print(f"📱 Access from iPad/iPhone:")
    print(f"   http://{local_ip}:8788")
    print()
    print("💻 Or from this Mac:")
    print("   http://localhost:8788")
    print()
    
    uvicorn.run(app, host="0.0.0.0", port=8788)

