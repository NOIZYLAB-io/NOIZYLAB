#!/bin/bash
# NOIZYLAB VOICE CONTROL INTEGRATION
# Run this on GOD to setup voice control endpoints accessible from iPad

API_URL="https://noizylab-api.fishmusicinc.workers.dev"

# Create simple HTTP endpoints that iPad can call via Shortcuts app

create_shortcut_server() {
    echo "🎤 Setting up voice control HTTP server..."
    
    # Create a simple node.js server for Shortcuts integration
    cat > /tmp/noizylab-voice-server.js << 'EOF'
const http = require('http');
const https = require('https');

const API_URL = 'https://noizylab-api.fishmusicinc.workers.dev';

const server = http.createServer(async (req, res) => {
    // CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }
    
    const url = new URL(req.url, 'http://localhost:8888');
    
    // Status command
    if (url.pathname === '/status') {
        try {
            const response = await fetch(API_URL + '/api/dashboard');
            const data = await response.json();
            
            const message = `Today: ${data.today.completed} of 12 repairs completed. ${data.today.in_progress} in progress. Revenue: $${data.today.revenue}`;
            
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ 
                success: true, 
                message: message,
                data: data.today 
            }));
        } catch (error) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: false, error: error.message }));
        }
        return;
    }
    
    // Start next repair
    if (url.pathname === '/start-next') {
        try {
            const response = await fetch(API_URL + '/api/voice', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: 'start next repair' })
            });
            const data = await response.json();
            
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true, message: data.response }));
        } catch (error) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: false, error: error.message }));
        }
        return;
    }
    
    // Complete repair
    if (url.pathname === '/complete' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => { body += chunk; });
        req.on('end', async () => {
            try {
                const { repair_id } = JSON.parse(body);
                const response = await fetch(API_URL + '/api/voice', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        command: 'complete repair',
                        context: { repair_id }
                    })
                });
                const data = await response.json();
                
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ success: true, message: data.response }));
            } catch (error) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ success: false, error: error.message }));
            }
        });
        return;
    }
    
    // Generic voice command
    if (url.pathname === '/voice' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => { body += chunk; });
        req.on('end', async () => {
            try {
                const { command } = JSON.parse(body);
                const response = await fetch(API_URL + '/api/voice', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ command })
                });
                const data = await response.json();
                
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ success: true, message: data.response }));
            } catch (error) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ success: false, error: error.message }));
            }
        });
        return;
    }
    
    res.writeHead(404, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Not found' }));
});

server.listen(8888, '0.0.0.0', () => {
    console.log('🎤 NOIZYLAB Voice Control Server running on port 8888');
    console.log('   Access from iPad: http://GOD.local:8888');
    console.log('');
    console.log('Available endpoints:');
    console.log('   GET  /status          - Get repair status');
    console.log('   POST /start-next      - Start next repair');
    console.log('   POST /complete        - Complete repair (needs repair_id)');
    console.log('   POST /voice           - Generic voice command');
});
EOF
    
    echo "✅ Voice control server created"
    echo ""
    echo "To start the server on GOD:"
    echo "  node /tmp/noizylab-voice-server.js"
    echo ""
    echo "To run automatically at startup, add to launchd or systemd"
}

create_ios_shortcuts() {
    echo "📱 iOS Shortcuts Configuration"
    echo "=============================="
    echo ""
    echo "On your iPad, create these Shortcuts:"
    echo ""
    
    echo "1. 'Repair Status'"
    echo "   - Get Contents of URL: http://GOD.local:8888/status"
    echo "   - Get Dictionary Value 'message' from response"
    echo "   - Speak Text"
    echo ""
    
    echo "2. 'Start Next Repair'"
    echo "   - Get Contents of URL: http://GOD.local:8888/start-next (POST)"
    echo "   - Get Dictionary Value 'message' from response"
    echo "   - Speak Text"
    echo ""
    
    echo "3. 'Complete Repair'"
    echo "   - Ask for Input (Repair ID)"
    echo "   - Set variable 'repairID'"
    echo "   - Get Contents of URL: http://GOD.local:8888/complete (POST)"
    echo "   - Body: {\"repair_id\": \"[repairID]\"}"
    echo "   - Get Dictionary Value 'message' from response"
    echo "   - Speak Text"
    echo ""
    
    echo "4. 'Voice Command'"
    echo "   - Ask for Input (Voice Command)"
    echo "   - Set variable 'command'"
    echo "   - Get Contents of URL: http://GOD.local:8888/voice (POST)"
    echo "   - Body: {\"command\": \"[command]\"}"
    echo "   - Get Dictionary Value 'message' from response"
    echo "   - Speak Text"
    echo ""
    
    echo "Once created, you can:"
    echo "  - Add to Home Screen"
    echo "  - Trigger with Siri: 'Hey Siri, repair status'"
    echo "  - Add to Back Tap gestures"
    echo "  - Add to Control Center"
}

# Main menu
case "$1" in
    "setup")
        create_shortcut_server
        ;;
    "shortcuts")
        create_ios_shortcuts
        ;;
    *)
        echo "NOIZYLAB Voice Control Integration"
        echo "=================================="
        echo ""
        echo "Usage:"
        echo "  $0 setup       - Create voice control server"
        echo "  $0 shortcuts   - Show iOS Shortcuts configuration"
        echo ""
        echo "Example workflow:"
        echo "  1. Run: $0 setup"
        echo "  2. On GOD: node /tmp/noizylab-voice-server.js"
        echo "  3. Run: $0 shortcuts"
        echo "  4. Create shortcuts on iPad as shown"
        echo "  5. Say: 'Hey Siri, repair status'"
        ;;
esac
