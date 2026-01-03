// Email Setup AI Worker - Cloudflare AI Assistant for iOS Email Setup
// ===================================================================
// Uses Cloudflare AI to guide email setup on iPad and iPhone

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // CORS headers for iOS access
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };
    
    // Handle preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }
    
    // Email setup assistant endpoint
    if (url.pathname === '/setup' && request.method === 'POST') {
      const { email, device, step } = await request.json();
      
      // Use Cloudflare AI to generate setup instructions
      const prompt = `You are an email setup assistant. Help set up ${email} on ${device}. 
Current step: ${step || 'initial'}. 
Provide clear, step-by-step instructions for iOS Mail app setup.
Include: IMAP server (imap.gmail.com:993), SMTP server (smtp.gmail.com:587), 
and remind user to use App Password from Google Account.`;
      
      try {
        const aiResponse = await env.AI.run('@cf/meta/llama-2-7b-chat-int8', {
          messages: [
            { role: 'system', content: 'You are a helpful email setup assistant for iOS devices.' },
            { role: 'user', content: prompt }
          ]
        });
        
        return new Response(JSON.stringify({
          success: true,
          instructions: aiResponse.response || aiResponse,
          email: email,
          device: device,
          step: step
        }), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      } catch (error) {
        // Fallback instructions if AI fails
        return new Response(JSON.stringify({
          success: true,
          instructions: generateFallbackInstructions(email, device, step),
          email: email,
          device: device
        }), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }
    }
    
    // Get email configurations
    if (url.pathname === '/configs' && request.method === 'GET') {
      const configs = [
        {
          email: 'rspplowman@gmail.com',
          type: 'Gmail',
          imap: 'imap.gmail.com:993',
          smtp: 'smtp.gmail.com:587',
          notes: 'Use App Password from Google Account'
        },
        {
          email: 'rsp@noizylab.ca',
          type: 'NoizyLab',
          imap: 'imap.gmail.com:993',
          smtp: 'smtp.gmail.com:587',
          notes: 'Google Workspace - Use App Password'
        },
        {
          email: 'help@noizylab.ca',
          type: 'NoizyLab',
          imap: 'imap.gmail.com:993',
          smtp: 'smtp.gmail.com:587',
          notes: 'Google Workspace - Use App Password'
        },
        {
          email: 'hello@noizylab.ca',
          type: 'NoizyLab',
          imap: 'imap.gmail.com:993',
          smtp: 'smtp.gmail.com:587',
          notes: 'Google Workspace - Use App Password'
        },
        {
          email: 'rp@fishmusicinc.com',
          type: 'Fish Music',
          imap: 'imap.gmail.com:993',
          smtp: 'smtp.gmail.com:587',
          notes: 'Google Workspace - Use App Password'
        },
        {
          email: 'info@fishmusicinc.com',
          type: 'Fish Music',
          imap: 'imap.gmail.com:993',
          smtp: 'smtp.gmail.com:587',
          notes: 'Google Workspace - Use App Password'
        }
      ];
      
      return new Response(JSON.stringify({ configs }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }
    
    // Serve web interface
    if (url.pathname === '/' || url.pathname === '/index.html') {
      const html = generateWebInterface();
      return new Response(html, {
        headers: { ...corsHeaders, 'Content-Type': 'text/html' }
      });
    }
    
    return new Response('NoizyLab Email Setup AI', {
      headers: corsHeaders
    });
  }
};

function generateFallbackInstructions(email, device, step) {
  return {
    step1: `Open Settings on your ${device}`,
    step2: 'Tap "Mail" → "Accounts" → "Add Account"',
    step3: email.includes('gmail.com') 
      ? 'Select "Google" and sign in'
      : 'Select "Other" → "Add Mail Account"',
    step4: `Enter your email: ${email}`,
    step5: 'Enter your App Password (get from myaccount.google.com/apppasswords)',
    step6: email.includes('gmail.com')
      ? 'Enable Mail, Contacts, Calendars'
      : 'Enter IMAP: imap.gmail.com:993 (SSL), SMTP: smtp.gmail.com:587 (TLS)',
    step7: 'Tap "Save" and wait for verification'
  };
}

function generateWebInterface() {
  return `<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NoizyLab Email Setup - Cloudflare AI</title>
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
    .email-item:hover {
      background: #e8e8e8;
      transform: translateX(5px);
    }
    .email-item.active {
      background: #667eea;
      color: white;
    }
    .device-select {
      margin: 20px 0;
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
      padding: 10px;
      background: white;
      border-left: 4px solid #667eea;
      border-radius: 5px;
    }
    .loading {
      text-align: center;
      padding: 20px;
      color: #667eea;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>📧 Email Setup AI</h1>
    <p class="subtitle">Cloudflare AI-powered email setup for iOS</p>
    
    <div class="device-select">
      <label>Select Device:</label>
      <select id="device">
        <option value="iPhone">iPhone</option>
        <option value="iPad">iPad</option>
      </select>
    </div>
    
    <div class="email-list" id="emailList">
      <div class="loading">Loading emails...</div>
    </div>
    
    <button onclick="setupEmail()">🤖 Get AI Setup Instructions</button>
    
    <div class="instructions" id="instructions">
      <h3>Setup Instructions:</h3>
      <div id="steps"></div>
    </div>
  </div>
  
  <script>
    let selectedEmail = '';
    let device = 'iPhone';
    
    // Load email configs
    fetch('/configs')
      .then(r => r.json())
      .then(data => {
        const list = document.getElementById('emailList');
        list.innerHTML = '';
        data.configs.forEach(config => {
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
      });
    
    document.getElementById('device').onchange = (e) => {
      device = e.target.value;
    };
    
    async function setupEmail() {
      if (!selectedEmail) {
        alert('Please select an email address');
        return;
      }
      
      const instructionsDiv = document.getElementById('instructions');
      const stepsDiv = document.getElementById('steps');
      instructionsDiv.classList.add('show');
      stepsDiv.innerHTML = '<div class="loading">🤖 AI is generating instructions...</div>';
      
      try {
        const response = await fetch('/setup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: selectedEmail,
            device: device,
            step: 'initial'
          })
        });
        
        const data = await response.json();
        
        if (data.instructions) {
          if (typeof data.instructions === 'object') {
            // Fallback instructions
            stepsDiv.innerHTML = Object.entries(data.instructions)
              .map(([key, value]) => `<div class="step"><strong>${key}:</strong> ${value}</div>`)
              .join('');
          } else {
            // AI-generated instructions
            stepsDiv.innerHTML = `<div class="step">${data.instructions}</div>`;
          }
        }
      } catch (error) {
        stepsDiv.innerHTML = '<div class="step">Error: ' + error.message + '</div>';
      }
    }
  </script>
</body>
</html>`;
}

