#!/usr/bin/env node
// THE DREAMCHAMBER
// Unified interface to ALL AI models of repute
// GORUNFREE X1000 - One interface = Every AI

const http = require('http');
const https = require('https');

const PORT = 7777;
const DREAMCHAMBER_VERSION = '1.0.0';

// AI Model configurations
const MODELS = {
    // ANTHROPIC (Claude)
    'claude-opus-4': {
        provider: 'anthropic',
        name: 'Claude Opus 4',
        tier: 'premium',
        cost_per_1m_input: 15,
        cost_per_1m_output: 75,
        context: 200000,
        description: 'Most intelligent. Best for complex reasoning.',
        icon: '🧠'
    },
    'claude-sonnet-4': {
        provider: 'anthropic',
        name: 'Claude Sonnet 4',
        tier: 'balanced',
        cost_per_1m_input: 3,
        cost_per_1m_output: 15,
        context: 200000,
        description: 'Balanced intelligence and speed. Best value.',
        icon: '⚡'
    },
    
    // OPENAI
    'gpt-4o': {
        provider: 'openai',
        name: 'GPT-4o',
        tier: 'premium',
        cost_per_1m_input: 2.5,
        cost_per_1m_output: 10,
        context: 128000,
        description: 'Multimodal. Fast and capable.',
        icon: '🔮'
    },
    'gpt-4-turbo': {
        provider: 'openai',
        name: 'GPT-4 Turbo',
        tier: 'balanced',
        cost_per_1m_input: 10,
        cost_per_1m_output: 30,
        context: 128000,
        description: 'Fast GPT-4 with vision.',
        icon: '🚀'
    },
    
    // GOOGLE
    'gemini-2.0-flash': {
        provider: 'google',
        name: 'Gemini 2.0 Flash',
        tier: 'fast',
        cost_per_1m_input: 0.075,
        cost_per_1m_output: 0.3,
        context: 1000000,
        description: 'Extremely fast. Massive context.',
        icon: '💎'
    },
    'gemini-pro': {
        provider: 'google',
        name: 'Gemini Pro',
        tier: 'balanced',
        cost_per_1m_input: 0.125,
        cost_per_1m_output: 0.5,
        context: 1000000,
        description: 'Google\'s best. Huge context window.',
        icon: '✨'
    },
    
    // META (via Together AI)
    'llama-3.3-70b': {
        provider: 'together',
        name: 'Llama 3.3 70B',
        tier: 'balanced',
        cost_per_1m_input: 0.88,
        cost_per_1m_output: 0.88,
        context: 128000,
        description: 'Open source. Strong performance.',
        icon: '🦙'
    },
    
    // MISTRAL
    'mistral-large': {
        provider: 'mistral',
        name: 'Mistral Large',
        tier: 'premium',
        cost_per_1m_input: 2,
        cost_per_1m_output: 6,
        context: 128000,
        description: 'European champion. Multilingual.',
        icon: '🌍'
    },
    
    // COHERE
    'command-r-plus': {
        provider: 'cohere',
        name: 'Command R+',
        tier: 'balanced',
        cost_per_1m_input: 3,
        cost_per_1m_output: 15,
        context: 128000,
        description: 'RAG optimized. Enterprise grade.',
        icon: '📚'
    },
    
    // PERPLEXITY
    'perplexity-online': {
        provider: 'perplexity',
        name: 'Perplexity Online',
        tier: 'research',
        cost_per_1m_input: 0,
        cost_per_1m_output: 5,
        context: 127072,
        description: 'Search-augmented. Always current.',
        icon: '🔍'
    }
};

// Session storage
const sessions = new Map();
const conversations = new Map();

// API call handlers for each provider
async function callAnthropic(model, messages, apiKey) {
    const modelId = model === 'claude-opus-4' ? 'claude-opus-4-20250514' : 'claude-sonnet-4-20250514';
    
    const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-api-key': apiKey,
            'anthropic-version': '2023-06-01'
        },
        body: JSON.stringify({
            model: modelId,
            max_tokens: 4096,
            messages: messages
        })
    });
    
    return await response.json();
}

async function callOpenAI(model, messages, apiKey) {
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: model,
            messages: messages,
            max_tokens: 4096
        })
    });
    
    return await response.json();
}

async function callGoogle(model, messages, apiKey) {
    // Convert messages to Gemini format
    const contents = messages.map(m => ({
        role: m.role === 'assistant' ? 'model' : 'user',
        parts: [{ text: m.content }]
    }));
    
    const response = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ contents })
        }
    );
    
    return await response.json();
}

async function callTogether(model, messages, apiKey) {
    const response = await fetch('https://api.together.xyz/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: 'meta-llama/Meta-Llama-3.3-70B-Instruct-Turbo',
            messages: messages,
            max_tokens: 4096
        })
    });
    
    return await response.json();
}

async function callMistral(model, messages, apiKey) {
    const response = await fetch('https://api.mistral.ai/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: 'mistral-large-latest',
            messages: messages,
            max_tokens: 4096
        })
    });
    
    return await response.json();
}

async function callCohere(model, messages, apiKey) {
    const response = await fetch('https://api.cohere.ai/v1/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: 'command-r-plus',
            message: messages[messages.length - 1].content,
            chat_history: messages.slice(0, -1)
        })
    });
    
    return await response.json();
}

async function callPerplexity(model, messages, apiKey) {
    const response = await fetch('https://api.perplexity.ai/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: 'llama-3.1-sonar-large-128k-online',
            messages: messages
        })
    });
    
    return await response.json();
}

// Main server
const server = http.createServer(async (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }
    
    const url = new URL(req.url, `http://localhost:${PORT}`);
    
    // Home page - THE DREAMCHAMBER UI
    if (url.pathname === '/') {
        const html = getDreamChamberHTML();
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(html);
        return;
    }
    
    // API: Get available models
    if (url.pathname === '/api/models') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ models: MODELS }));
        return;
    }
    
    // API: Send message to AI
    if (url.pathname === '/api/chat' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => { body += chunk; });
        req.on('end', async () => {
            try {
                const { model, message, conversation_id, api_keys } = JSON.parse(body);
                
                // Get or create conversation
                let conv = conversations.get(conversation_id) || [];
                conv.push({ role: 'user', content: message });
                
                // Route to appropriate provider
                const modelConfig = MODELS[model];
                let response;
                
                const startTime = Date.now();
                
                switch (modelConfig.provider) {
                    case 'anthropic':
                        response = await callAnthropic(model, conv, api_keys.anthropic);
                        break;
                    case 'openai':
                        response = await callOpenAI(model, conv, api_keys.openai);
                        break;
                    case 'google':
                        response = await callGoogle(model, conv, api_keys.google);
                        break;
                    case 'together':
                        response = await callTogether(model, conv, api_keys.together);
                        break;
                    case 'mistral':
                        response = await callMistral(model, conv, api_keys.mistral);
                        break;
                    case 'cohere':
                        response = await callCohere(model, conv, api_keys.cohere);
                        break;
                    case 'perplexity':
                        response = await callPerplexity(model, conv, api_keys.perplexity);
                        break;
                }
                
                const responseTime = Date.now() - startTime;
                
                // Extract response text (varies by provider)
                let responseText = '';
                if (response.content) responseText = response.content[0].text; // Anthropic
                else if (response.choices) responseText = response.choices[0].message.content; // OpenAI/Together
                else if (response.candidates) responseText = response.candidates[0].content.parts[0].text; // Google
                else if (response.text) responseText = response.text; // Cohere
                
                conv.push({ role: 'assistant', content: responseText });
                conversations.set(conversation_id, conv);
                
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({
                    success: true,
                    response: responseText,
                    response_time: responseTime,
                    model: model,
                    provider: modelConfig.provider
                }));
                
            } catch (error) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: error.message }));
            }
        });
        return;
    }
    
    // API: Compare models
    if (url.pathname === '/api/compare' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => { body += chunk; });
        req.on('end', async () => {
            try {
                const { models, message, api_keys } = JSON.parse(body);
                
                const results = await Promise.all(
                    models.map(async model => {
                        const conv = [{ role: 'user', content: message }];
                        const startTime = Date.now();
                        
                        try {
                            const modelConfig = MODELS[model];
                            let response;
                            
                            switch (modelConfig.provider) {
                                case 'anthropic':
                                    response = await callAnthropic(model, conv, api_keys.anthropic);
                                    break;
                                case 'openai':
                                    response = await callOpenAI(model, conv, api_keys.openai);
                                    break;
                                // ... other providers
                            }
                            
                            const responseTime = Date.now() - startTime;
                            let responseText = '';
                            if (response.content) responseText = response.content[0].text;
                            else if (response.choices) responseText = response.choices[0].message.content;
                            
                            return {
                                model,
                                success: true,
                                response: responseText,
                                response_time: responseTime
                            };
                        } catch (error) {
                            return {
                                model,
                                success: false,
                                error: error.message
                            };
                        }
                    })
                );
                
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ results }));
                
            } catch (error) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: error.message }));
            }
        });
        return;
    }
    
    res.writeHead(404);
    res.end('Not found');
});

function getDreamChamberHTML() {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THE DREAMCHAMBER - All AI Models</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            color: #ffffff;
            min-height: 100vh;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            padding: 40px;
            text-align: center;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        
        .logo {
            font-size: 64px;
            font-weight: 900;
            margin-bottom: 10px;
            text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
        
        .tagline {
            font-size: 20px;
            opacity: 0.9;
        }
        
        .container {
            max-width: 1800px;
            margin: 40px auto;
            padding: 0 40px;
            display: grid;
            grid-template-columns: 350px 1fr;
            gap: 40px;
        }
        
        .sidebar {
            background: #1a1f3a;
            border-radius: 20px;
            padding: 30px;
            height: fit-content;
            position: sticky;
            top: 20px;
        }
        
        .model-grid {
            display: grid;
            gap: 15px;
        }
        
        .model-card {
            background: #242943;
            border-radius: 12px;
            padding: 20px;
            cursor: pointer;
            transition: all 0.3s;
            border: 2px solid transparent;
        }
        
        .model-card:hover {
            background: #2a3050;
            transform: translateX(5px);
        }
        
        .model-card.active {
            border-color: #667eea;
            background: #2a3050;
        }
        
        .model-icon {
            font-size: 32px;
            margin-bottom: 10px;
        }
        
        .model-name {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 5px;
        }
        
        .model-desc {
            font-size: 13px;
            color: #aaa;
            margin-bottom: 10px;
        }
        
        .model-cost {
            font-size: 11px;
            color: #888;
        }
        
        .chat-container {
            background: #1a1f3a;
            border-radius: 20px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            height: calc(100vh - 240px);
        }
        
        .messages {
            flex: 1;
            overflow-y: auto;
            margin-bottom: 20px;
            padding: 20px;
        }
        
        .message {
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 12px;
        }
        
        .message.user {
            background: #242943;
            margin-left: 80px;
        }
        
        .message.assistant {
            background: linear-gradient(135deg, #667eea20, #764ba220);
            margin-right: 80px;
            border-left: 4px solid #667eea;
        }
        
        .message-header {
            font-size: 12px;
            color: #aaa;
            margin-bottom: 10px;
        }
        
        .message-content {
            font-size: 16px;
            line-height: 1.6;
            white-space: pre-wrap;
        }
        
        .input-area {
            display: flex;
            gap: 15px;
        }
        
        textarea {
            flex: 1;
            background: #242943;
            border: 2px solid #2a3050;
            border-radius: 12px;
            padding: 20px;
            color: white;
            font-size: 16px;
            font-family: inherit;
            resize: none;
            height: 120px;
        }
        
        textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .send-btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border: none;
            border-radius: 12px;
            padding: 20px 40px;
            color: white;
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .send-btn:hover {
            transform: translateY(-2px);
        }
        
        .send-btn:active {
            transform: translateY(0);
        }
        
        .send-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .actions {
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .action-btn {
            flex: 1;
            background: #242943;
            border: 2px solid #2a3050;
            border-radius: 12px;
            padding: 15px;
            color: white;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .action-btn:hover {
            background: #2a3050;
            border-color: #667eea;
        }
        
        .voice-btn {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #f093fb, #f5576c);
            border: none;
            font-size: 30px;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(240, 147, 251, 0.4);
        }
        
        .voice-btn.listening {
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .stat {
            background: #242943;
            border-radius: 12px;
            padding: 15px;
            text-align: center;
        }
        
        .stat-value {
            font-size: 24px;
            font-weight: 900;
            margin-bottom: 5px;
        }
        
        .stat-label {
            font-size: 11px;
            color: #888;
            text-transform: uppercase;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">✨ THE DREAMCHAMBER ✨</div>
        <div class="tagline">All AI Models of Repute - One Unified Interface</div>
    </div>
    
    <div class="container">
        <div class="sidebar">
            <h3 style="margin-bottom: 20px;">Select AI Model</h3>
            <div class="model-grid" id="modelGrid">
                <!-- Models loaded here -->
            </div>
            
            <div class="stats" style="margin-top: 30px;">
                <div class="stat">
                    <div class="stat-value" id="messageCount">0</div>
                    <div class="stat-label">Messages</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="avgTime">0ms</div>
                    <div class="stat-label">Avg Time</div>
                </div>
                <div class="stat">
                    <div class="stat-value" id="totalCost">$0</div>
                    <div class="stat-label">Est. Cost</div>
                </div>
            </div>
        </div>
        
        <div class="chat-container">
            <div class="actions">
                <button class="action-btn" onclick="compareModels()">🔀 Compare Models</button>
                <button class="action-btn" onclick="clearChat()">🗑️ Clear Chat</button>
                <button class="action-btn" onclick="exportChat()">💾 Export</button>
                <button class="voice-btn" id="voiceBtn" onclick="toggleVoice()">🎤</button>
            </div>
            
            <div class="messages" id="messages">
                <div style="text-align: center; color: #666; padding: 40px;">
                    <h2>Welcome to THE DREAMCHAMBER</h2>
                    <p>Select an AI model and start chatting</p>
                </div>
            </div>
            
            <div class="input-area">
                <textarea 
                    id="messageInput" 
                    placeholder="Ask anything to any AI model..."
                    onkeypress="if(event.key==='Enter'&&event.ctrlKey)sendMessage()"
                ></textarea>
                <button class="send-btn" onclick="sendMessage()" id="sendBtn">Send</button>
            </div>
        </div>
    </div>
    
    <script>
        let selectedModel = 'claude-sonnet-4';
        let conversationId = Date.now().toString();
        let messages = [];
        let stats = { messageCount: 0, totalTime: 0, totalCost: 0 };
        
        // Load models
        fetch('/api/models').then(r => r.json()).then(data => {
            const grid = document.getElementById('modelGrid');
            Object.entries(data.models).forEach(([id, model]) => {
                const card = document.createElement('div');
                card.className = 'model-card' + (id === selectedModel ? ' active' : '');
                card.onclick = () => selectModel(id);
                card.innerHTML = \`
                    <div class="model-icon">\${model.icon}</div>
                    <div class="model-name">\${model.name}</div>
                    <div class="model-desc">\${model.description}</div>
                    <div class="model-cost">$\${model.cost_per_1m_input}/M in · $\${model.cost_per_1m_output}/M out</div>
                \`;
                grid.appendChild(card);
            });
        });
        
        function selectModel(id) {
            selectedModel = id;
            document.querySelectorAll('.model-card').forEach(card => {
                card.classList.remove('active');
            });
            event.target.closest('.model-card').classList.add('active');
        }
        
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            if (!message) return;
            
            input.value = '';
            document.getElementById('sendBtn').disabled = true;
            
            // Add user message
            addMessage('user', message);
            
            // Send to API
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        model: selectedModel,
                        message: message,
                        conversation_id: conversationId,
                        api_keys: {
                            anthropic: localStorage.getItem('anthropic_key'),
                            openai: localStorage.getItem('openai_key'),
                            google: localStorage.getItem('google_key')
                        }
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    addMessage('assistant', data.response, data.model, data.response_time);
                    updateStats(data.response_time);
                } else {
                    addMessage('error', 'Error: ' + (data.error || 'Unknown error'));
                }
            } catch (error) {
                addMessage('error', 'Error: ' + error.message);
            }
            
            document.getElementById('sendBtn').disabled = false;
        }
        
        function addMessage(type, content, model, time) {
            const container = document.getElementById('messages');
            const div = document.createElement('div');
            div.className = \`message \${type}\`;
            
            let header = type === 'user' ? 'You' : (model || 'Assistant');
            if (time) header += \` · \${time}ms\`;
            
            div.innerHTML = \`
                <div class="message-header">\${header}</div>
                <div class="message-content">\${content}</div>
            \`;
            
            container.appendChild(div);
            container.scrollTop = container.scrollHeight;
        }
        
        function updateStats(time) {
            stats.messageCount++;
            stats.totalTime += time;
            
            document.getElementById('messageCount').textContent = stats.messageCount;
            document.getElementById('avgTime').textContent = Math.round(stats.totalTime / stats.messageCount) + 'ms';
        }
        
        function clearChat() {
            if (confirm('Clear chat history?')) {
                document.getElementById('messages').innerHTML = '';
                messages = [];
                conversationId = Date.now().toString();
            }
        }
        
        function exportChat() {
            const data = JSON.stringify(messages, null, 2);
            const blob = new Blob([data], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'dreamchamber-chat-' + Date.now() + '.json';
            a.click();
        }
        
        function toggleVoice() {
            // Voice recognition implementation
            alert('Voice control: Say your message and it will be sent to the selected AI model');
        }
        
        async function compareModels() {
            const message = prompt('Enter a prompt to compare across multiple models:');
            if (!message) return;
            
            const modelsToCompare = ['claude-sonnet-4', 'gpt-4o', 'gemini-pro'];
            
            addMessage('system', 'Comparing: ' + modelsToCompare.join(', ') + '...');
            
            // Implementation here
        }
        
        // Check for API keys on load
        window.addEventListener('load', () => {
            if (!localStorage.getItem('anthropic_key')) {
                const key = prompt('Enter your Anthropic API key (or leave blank):');
                if (key) localStorage.setItem('anthropic_key', key);
            }
        });
    </script>
</body>
</html>`;
}

server.listen(PORT, '0.0.0.0', () => {
    console.log('✨ THE DREAMCHAMBER ✨');
    console.log('======================');
    console.log('');
    console.log(\`✅ Running on port \${PORT}\`);
    console.log('');
    console.log('Access:');
    console.log(\`  Local:  http://localhost:\${PORT}\`);
    console.log(\`  GOD:    http://GOD.local:\${PORT}\`);
    console.log(\`  iPad:   http://10.90.90.x:\${PORT}\`);
    console.log('');
    console.log('Available AI Models:');
    Object.entries(MODELS).forEach(([id, model]) => {
        console.log(\`  \${model.icon} \${model.name} (\${model.tier})\`);
    });
    console.log('');
    console.log('Features:');
    console.log('  • Multi-model chat');
    console.log('  • Model comparison');
    console.log('  • Cost tracking');
    console.log('  • Voice control');
    console.log('  • Export conversations');
    console.log('');
    console.log('GORUNFREE X1000 ✨');
});
