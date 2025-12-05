#!/usr/bin/env node
// CLAUDE-CURSOR BRIDGE SERVER
// Run on GOD, access from anywhere in MC96
// GORUNFREE X1000 - One command = unified workflow

const http = require('http');
const fs = require('fs');
const { exec } = require('child_process');

const PORT = 9999;

// Store conversations
let conversations = [];

const server = http.createServer((req, res) => {
    // CORS
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }
    
    const url = new URL(req.url, `http://localhost:${PORT}`);
    
    // ENDPOINT: Send code to Claude
    if (url.pathname === '/to-claude' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => { body += chunk; });
        req.on('end', () => {
            const { code, prompt } = JSON.parse(body);
            
            // Save to clipboard
            exec(`echo "${code}" | pbcopy`);
            
            // Open Claude.ai
            exec('open -a Safari https://claude.ai');
            
            // Wait then paste
            setTimeout(() => {
                exec(`osascript -e 'tell application "System Events" to keystroke "v" using command down'`);
                setTimeout(() => {
                    exec(`osascript -e 'tell application "System Events" to keystroke return'`);
                }, 500);
            }, 2000);
            
            conversations.push({ type: 'to-claude', code, prompt, timestamp: Date.now() });
            
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true, message: 'Sent to Claude' }));
        });
        return;
    }
    
    // ENDPOINT: Get Claude response back to Cursor
    if (url.pathname === '/from-claude' && req.method === 'POST') {
        // Copy from Claude
        exec(`osascript -e 'tell application "Safari" to activate'`);
        setTimeout(() => {
            exec(`osascript -e 'tell application "System Events" to keystroke "a" using command down'`);
            setTimeout(() => {
                exec(`osascript -e 'tell application "System Events" to keystroke "c" using command down'`);
                
                // Switch to Cursor
                setTimeout(() => {
                    exec(`osascript -e 'tell application "Cursor" to activate'`);
                    setTimeout(() => {
                        exec(`osascript -e 'tell application "System Events" to keystroke "v" using command down'`);
                    }, 500);
                }, 500);
            }, 200);
        }, 1000);
        
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, message: 'Retrieved from Claude' }));
        return;
    }
    
    // ENDPOINT: Voice command
    if (url.pathname === '/voice' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => { body += chunk; });
        req.on('end', () => {
            const { command } = JSON.parse(body);
            
            if (command.includes('claude review') || command.includes('ask claude')) {
                // Send to Claude
                exec('open -a Safari https://claude.ai');
                exec(`osascript -e 'tell application "System Events" to keystroke "v" using command down'`);
                exec(`osascript -e 'tell application "System Events" to keystroke return'`);
                
                // Speak confirmation
                exec(`say "Sent to Claude"`);
            }
            
            if (command.includes('get response') || command.includes('claude done')) {
                // Get from Claude
                exec(`osascript -e 'tell application "Safari" to activate'`);
                exec(`osascript -e 'tell application "System Events" to keystroke "a" using command down'`);
                exec(`osascript -e 'tell application "System Events" to keystroke "c" using command down'`);
                exec(`osascript -e 'tell application "Cursor" to activate'`);
                exec(`osascript -e 'tell application "System Events" to keystroke "v" using command down'`);
                
                exec(`say "Got response from Claude"`);
            }
            
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true }));
        });
        return;
    }
    
    // ENDPOINT: Web UI
    if (url.pathname === '/') {
        const html = `<!DOCTYPE html>
<html>
<head>
    <title>Claude-Cursor Bridge</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0e27; color: white; padding: 40px;
        }
        h1 { 
            font-size: 48px; 
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 40px;
        }
        .controls { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; max-width: 800px; }
        button {
            padding: 60px 40px; font-size: 24px; font-weight: 700;
            border: none; border-radius: 16px; cursor: pointer;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white; transition: transform 0.2s;
        }
        button:hover { transform: translateY(-2px); }
        button:active { transform: translateY(0); }
        textarea {
            width: 100%; max-width: 800px; height: 200px;
            padding: 20px; margin: 20px 0;
            background: #1a1f3a; color: white; border: 2px solid #667eea;
            border-radius: 12px; font-size: 16px; font-family: monospace;
        }
        .status { 
            margin-top: 20px; padding: 20px; background: #1a1f3a; 
            border-radius: 12px; max-width: 800px;
        }
    </style>
</head>
<body>
    <h1>🔗 Claude ↔ Cursor Bridge</h1>
    
    <div class="controls">
        <button onclick="sendToClaude()">📤 Send to Claude</button>
        <button onclick="getFromClaude()">📥 Get from Claude</button>
        <button onclick="voiceCommand('claude review')">🎤 Voice: Ask Claude</button>
        <button onclick="voiceCommand('get response')">🎤 Voice: Get Response</button>
    </div>
    
    <textarea id="codeInput" placeholder="Paste code here or use clipboard..."></textarea>
    
    <div class="status" id="status">Ready</div>
    
    <script>
        async function sendToClaude() {
            const code = document.getElementById('codeInput').value || await navigator.clipboard.readText();
            const res = await fetch('/to-claude', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code, prompt: 'Review this code' })
            });
            const data = await res.json();
            document.getElementById('status').textContent = '✅ ' + data.message;
        }
        
        async function getFromClaude() {
            const res = await fetch('/from-claude', { method: 'POST' });
            const data = await res.json();
            document.getElementById('status').textContent = '✅ ' + data.message;
        }
        
        async function voiceCommand(cmd) {
            const res = await fetch('/voice', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: cmd })
            });
            document.getElementById('status').textContent = '🎤 Voice command: ' + cmd;
        }
        
        // Auto-refresh status
        setInterval(() => {
            document.getElementById('status').textContent = 'Ready • ' + new Date().toLocaleTimeString();
        }, 1000);
    </script>
</body>
</html>`;
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(html);
        return;
    }
    
    res.writeHead(404);
    res.end('Not found');
});

server.listen(PORT, '0.0.0.0', () => {
    console.log('🔗 Claude-Cursor Bridge Server');
    console.log('================================');
    console.log('');
    console.log(`✅ Running on: http://GOD.local:${PORT}`);
    console.log(`✅ From iPad: http://10.90.90.x:${PORT}`);
    console.log('');
    console.log('Endpoints:');
    console.log('  POST /to-claude     - Send code to Claude');
    console.log('  POST /from-claude   - Get response back');
    console.log('  POST /voice         - Voice commands');
    console.log('  GET  /              - Web UI');
    console.log('');
    console.log('Usage:');
    console.log('  curl -X POST http://localhost:9999/to-claude \\');
    console.log('    -H "Content-Type: application/json" \\');
    console.log('    -d \'{"code":"console.log(123)"}\'');
    console.log('');
    console.log('Voice commands:');
    console.log('  - "claude review" → Send to Claude');
    console.log('  - "get response" → Retrieve from Claude');
});

// Auto-start on boot (create launchd plist)
const plist = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noizylab.claude-cursor-bridge</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/node</string>
        <string>${__filename}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>`;

console.log('');
console.log('To auto-start on boot, save this to:');
console.log('  ~/Library/LaunchAgents/com.noizylab.claude-cursor-bridge.plist');
console.log('');
console.log('Then run:');
console.log('  launchctl load ~/Library/LaunchAgents/com.noizylab.claude-cursor-bridge.plist');
