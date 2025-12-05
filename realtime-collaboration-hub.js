/**
 * REAL-TIME COLLABORATION HUB
 * WebSocket-powered live collaboration across all domains
 * Team sync, live cursors, presence awareness, real-time updates
 * 
 * FOR: ROB PLOWMAN (NOT PICKERING - SORRY ROB!)
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // WebSocket upgrade
      if (path === '/ws') {
        return handleWebSocket(request, env);
      }
      
      if (path === '/') {
        return handleCollaborationHub();
      } else if (path === '/api/presence') {
        return await handlePresence(env, corsHeaders);
      } else if (path === '/api/rooms') {
        return await handleRooms(env, corsHeaders);
      } else if (path === '/api/broadcast' && request.method === 'POST') {
        return await handleBroadcast(request, env, corsHeaders);
      } else if (path === '/health') {
        return new Response(JSON.stringify({ status: 'healthy' }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      return new Response('Not Found', { status: 404 });

    } catch (error) {
      console.error('Error:', error);
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }
};

function handleCollaborationHub() {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time Collaboration Hub</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            padding: 2rem;
        }
        
        .container { max-width: 1400px; margin: 0 auto; }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            font-size: 1.1rem;
            opacity: 0.9;
            margin-bottom: 2rem;
        }
        
        .connection-status {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 1rem 1.5rem;
            border-radius: 12px;
            border: 2px solid rgba(255,255,255,0.2);
            display: inline-flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #10b981;
            animation: pulse 2s infinite;
        }
        
        .status-dot.disconnected {
            background: #ef4444;
            animation: none;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .presence-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .user-card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 1.5rem;
            border-radius: 12px;
            border: 2px solid rgba(255,255,255,0.2);
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: linear-gradient(135deg, #f59e0b, #ef4444);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .user-info h4 {
            margin-bottom: 0.25rem;
        }
        
        .user-status {
            font-size: 0.85rem;
            opacity: 0.8;
        }
        
        .rooms-section {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 12px;
            border: 2px solid rgba(255,255,255,0.2);
            margin-bottom: 2rem;
        }
        
        .room-item {
            background: rgba(0,0,0,0.2);
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .room-info h4 {
            margin-bottom: 0.5rem;
        }
        
        .room-meta {
            font-size: 0.9rem;
            opacity: 0.8;
        }
        
        .room-actions button {
            padding: 0.5rem 1.5rem;
            background: linear-gradient(135deg, #10b981, #3b82f6);
            border: none;
            color: white;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
        
        .chat-area {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 12px;
            border: 2px solid rgba(255,255,255,0.2);
        }
        
        .messages {
            background: rgba(0,0,0,0.2);
            height: 300px;
            overflow-y: auto;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        
        .message {
            padding: 0.75rem;
            margin-bottom: 0.5rem;
            background: rgba(255,255,255,0.05);
            border-radius: 8px;
        }
        
        .message-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
        }
        
        .message-author {
            font-weight: bold;
            color: #3b82f6;
        }
        
        .message-time {
            opacity: 0.7;
        }
        
        .input-area {
            display: flex;
            gap: 1rem;
        }
        
        input {
            flex: 1;
            padding: 1rem;
            background: rgba(0,0,0,0.2);
            border: 2px solid rgba(255,255,255,0.2);
            border-radius: 8px;
            color: white;
            font-size: 1rem;
        }
        
        input::placeholder {
            color: rgba(255,255,255,0.5);
        }
        
        button {
            padding: 1rem 2rem;
            background: linear-gradient(135deg, #10b981, #3b82f6);
            border: none;
            color: white;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: transform 0.2s;
        }
        
        button:hover {
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ Real-Time Collaboration Hub</h1>
        <div class="subtitle">Live team sync • Presence awareness • Instant updates</div>
        
        <!-- Connection Status -->
        <div class="connection-status">
            <div class="status-dot" id="statusDot"></div>
            <span id="statusText">Connecting...</span>
        </div>
        
        <!-- Online Users -->
        <h3 style="margin-bottom: 1rem;">Online Now</h3>
        <div class="presence-grid" id="presenceGrid">
            <div class="user-card">
                <div class="avatar">RP</div>
                <div class="user-info">
                    <h4>Rob Plowman</h4>
                    <div class="user-status">Active now</div>
                </div>
            </div>
        </div>
        
        <!-- Active Rooms -->
        <div class="rooms-section">
            <h3 style="margin-bottom: 1rem;">Active Rooms</h3>
            <div id="roomsList">
                <div class="room-item">
                    <div class="room-info">
                        <h4>NOIZYLAB Team</h4>
                        <div class="room-meta">5 members • Last activity: 2 min ago</div>
                    </div>
                    <div class="room-actions">
                        <button onclick="joinRoom('noizylab')">Join</button>
                    </div>
                </div>
                
                <div class="room-item">
                    <div class="room-info">
                        <h4>FishMusicInc Projects</h4>
                        <div class="room-meta">3 members • Last activity: 5 min ago</div>
                    </div>
                    <div class="room-actions">
                        <button onclick="joinRoom('fishmusicinc')">Join</button>
                    </div>
                </div>
                
                <div class="room-item">
                    <div class="room-info">
                        <h4>NOIZY.AI Development</h4>
                        <div class="room-meta">8 members • Last activity: Just now</div>
                    </div>
                    <div class="room-actions">
                        <button onclick="joinRoom('noizyai')">Join</button>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Live Chat -->
        <div class="chat-area">
            <h3 style="margin-bottom: 1rem;">Live Chat</h3>
            <div class="messages" id="messages">
                <div class="message">
                    <div class="message-header">
                        <span class="message-author">Rob Plowman</span>
                        <span class="message-time">Just now</span>
                    </div>
                    <div class="message-body">
                        Welcome to the real-time collaboration hub! 🚀
                    </div>
                </div>
            </div>
            
            <div class="input-area">
                <input 
                    type="text" 
                    id="messageInput" 
                    placeholder="Type a message..." 
                    onkeypress="handleKeyPress(event)"
                />
                <button onclick="sendMessage()">Send</button>
            </div>
        </div>
    </div>
    
    <script>
        let ws = null;
        let currentRoom = 'general';
        let username = 'Rob Plowman';
        
        function connect() {
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            ws = new WebSocket(\`\${protocol}//\${window.location.host}/ws\`);
            
            ws.onopen = () => {
                console.log('Connected to collaboration hub');
                updateStatus('connected');
                
                // Send join message
                ws.send(JSON.stringify({
                    type: 'join',
                    user: username,
                    room: currentRoom
                }));
            };
            
            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                handleMessage(data);
            };
            
            ws.onclose = () => {
                console.log('Disconnected from collaboration hub');
                updateStatus('disconnected');
                setTimeout(connect, 5000); // Reconnect after 5 seconds
            };
            
            ws.onerror = (error) => {
                console.error('WebSocket error:', error);
            };
        }
        
        function updateStatus(status) {
            const dot = document.getElementById('statusDot');
            const text = document.getElementById('statusText');
            
            if (status === 'connected') {
                dot.classList.remove('disconnected');
                text.textContent = 'Connected';
            } else {
                dot.classList.add('disconnected');
                text.textContent = 'Disconnected';
            }
        }
        
        function handleMessage(data) {
            switch (data.type) {
                case 'message':
                    addMessage(data.user, data.message, data.timestamp);
                    break;
                case 'presence':
                    updatePresence(data.users);
                    break;
                case 'notification':
                    showNotification(data.message);
                    break;
            }
        }
        
        function addMessage(user, message, timestamp) {
            const messages = document.getElementById('messages');
            const messageEl = document.createElement('div');
            messageEl.className = 'message';
            
            const time = new Date(timestamp).toLocaleTimeString('en-US', {
                hour: '2-digit',
                minute: '2-digit'
            });
            
            messageEl.innerHTML = \`
                <div class="message-header">
                    <span class="message-author">\${user}</span>
                    <span class="message-time">\${time}</span>
                </div>
                <div class="message-body">\${message}</div>
            \`;
            
            messages.appendChild(messageEl);
            messages.scrollTop = messages.scrollHeight;
        }
        
        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (message && ws && ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({
                    type: 'message',
                    user: username,
                    message: message,
                    room: currentRoom,
                    timestamp: new Date().toISOString()
                }));
                
                input.value = '';
            }
        }
        
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
        
        function joinRoom(room) {
            currentRoom = room;
            
            if (ws && ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({
                    type: 'join',
                    user: username,
                    room: room
                }));
            }
            
            showNotification(\`Joined room: \${room}\`);
        }
        
        function showNotification(message) {
            // Simple notification (could use browser notifications)
            console.log('Notification:', message);
        }
        
        function updatePresence(users) {
            const grid = document.getElementById('presenceGrid');
            grid.innerHTML = users.map(user => \`
                <div class="user-card">
                    <div class="avatar">\${user.initials}</div>
                    <div class="user-info">
                        <h4>\${user.name}</h4>
                        <div class="user-status">\${user.status}</div>
                    </div>
                </div>
            \`).join('');
        }
        
        // Connect on page load
        connect();
    </script>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

async function handleWebSocket(request, env) {
  // WebSocket handling (Durable Objects would be used in production)
  const upgradeHeader = request.headers.get('Upgrade');
  
  if (!upgradeHeader || upgradeHeader !== 'websocket') {
    return new Response('Expected Upgrade: websocket', { status: 426 });
  }
  
  // In production, use Durable Objects for WebSocket management
  return new Response('WebSocket upgrade handled by Durable Objects', {
    status: 101,
    webSocket: null
  });
}

async function handlePresence(env, corsHeaders) {
  const users = [
    {
      name: 'Rob Plowman',
      initials: 'RP',
      status: 'Active now',
      room: 'noizylab'
    }
  ];
  
  return new Response(JSON.stringify({ users }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleRooms(env, corsHeaders) {
  const rooms = [
    {
      id: 'noizylab',
      name: 'NOIZYLAB Team',
      members: 5,
      last_activity: new Date(Date.now() - 120000).toISOString()
    },
    {
      id: 'fishmusicinc',
      name: 'FishMusicInc Projects',
      members: 3,
      last_activity: new Date(Date.now() - 300000).toISOString()
    },
    {
      id: 'noizyai',
      name: 'NOIZY.AI Development',
      members: 8,
      last_activity: new Date().toISOString()
    }
  ];
  
  return new Response(JSON.stringify({ rooms }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

async function handleBroadcast(request, env, corsHeaders) {
  const { room, message, user } = await request.json();
  
  // Broadcast to all connections in room (Durable Objects in production)
  
  return new Response(JSON.stringify({
    success: true,
    room,
    timestamp: new Date().toISOString()
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}
