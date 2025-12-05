#!/usr/bin/env node
// THE AI GENIUS - MASTER AI MANAGEMENT SYSTEM
// Complete automation and integration for all AI models
// GORUNFREE X1000

const http = require('http');
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

const PORT = 8888;

// Load configuration
const configPath = path.join(__dirname, 'ai-genius-config.js');
const { loadConfig, smartRoute, getEnabledModels, getFreeModels } = require(configPath);

let config = loadConfig();

// Active sessions
const sessions = new Map();
const conversations = new Map();

// ============================================
// AI CALLING FUNCTIONS
// ============================================

async function callAI(modelId, message, apiKeys = {}) {
  const model = config.models[modelId];
  if (!model || !model.enabled) {
    throw new Error(`Model ${modelId} not found or disabled`);
  }
  
  const startTime = Date.now();
  let response;
  
  try {
    switch (model.type) {
      case 'api':
        response = await callAPIModel(model, message, apiKeys);
        break;
      case 'web':
        response = await callWebModel(model, message);
        break;
      case 'local_server':
        response = await callLocalServer(model, message);
        break;
      case 'editor':
      case 'vscode_extension':
        response = await callEditorIntegration(model, message);
        break;
      default:
        throw new Error(`Unsupported model type: ${model.type}`);
    }
    
    const responseTime = Date.now() - startTime;
    
    return {
      success: true,
      model: modelId,
      model_name: model.name,
      response: response,
      response_time: responseTime,
      free: model.free,
      icon: model.icon
    };
    
  } catch (error) {
    return {
      success: false,
      model: modelId,
      error: error.message
    };
  }
}

async function callAPIModel(model, message, apiKeys) {
  const apiKey = apiKeys[model.api_key_name] || process.env[model.api_key_name];
  if (!apiKey && !model.free) {
    throw new Error(`API key required: ${model.api_key_name}`);
  }
  
  let response;
  
  // Anthropic (Claude)
  if (model.api.includes('anthropic.com')) {
    response = await fetch(model.api, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: model.model_id,
        max_tokens: 4096,
        messages: [{ role: 'user', content: message }]
      })
    });
    
    const data = await response.json();
    return data.content[0].text;
  }
  
  // Google (Gemini)
  if (model.api.includes('generativelanguage.googleapis.com')) {
    response = await fetch(`${model.api}?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: message }] }]
      })
    });
    
    const data = await response.json();
    return data.candidates[0].content.parts[0].text;
  }
  
  // Together AI (Llama)
  if (model.api.includes('together.xyz')) {
    response = await fetch(model.api, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: model.model_id,
        messages: [{ role: 'user', content: message }],
        max_tokens: 4096
      })
    });
    
    const data = await response.json();
    return data.choices[0].message.content;
  }
  
  // Perplexity
  if (model.api.includes('perplexity.ai')) {
    response = await fetch(model.api, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: model.model_id,
        messages: [{ role: 'user', content: message }]
      })
    });
    
    const data = await response.json();
    return data.choices[0].message.content;
  }
  
  throw new Error('Unsupported API model');
}

async function callWebModel(model, message) {
  // For web-based models, open browser and return instruction
  exec(`open "${model.url}"`);
  return `Opening ${model.name} in browser. Please paste your query:\n\n${message}`;
}

async function callLocalServer(model, message) {
  // Ollama local
  if (model.url.includes('localhost:11434')) {
    const response = await fetch(model.api, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'llama3.3',
        prompt: message,
        stream: false
      })
    });
    
    const data = await response.json();
    return data.response;
  }
  
  // LM Studio
  if (model.url.includes('localhost:1234')) {
    const response = await fetch(model.api, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        messages: [{ role: 'user', content: message }],
        max_tokens: 4096
      })
    });
    
    const data = await response.json();
    return data.choices[0].message.content;
  }
  
  throw new Error('Local server not running');
}

async function callEditorIntegration(model, message) {
  if (model.name.includes('Cursor')) {
    // Open Cursor with command
    exec(`open -a Cursor`);
    // Copy message to clipboard
    exec(`echo "${message}" | pbcopy`);
    return `Opening Cursor AI. Message copied to clipboard. Press ${model.hotkey} to chat with Cursor AI.`;
  }
  
  return `${model.name} integration: ${message}`;
}

// ============================================
// HTTP SERVER
// ============================================

const server = http.createServer(async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }
  
  const url = new URL(req.url, `http://localhost:${PORT}`);
  
  // Home page - AI GENIUS Dashboard
  if (url.pathname === '/') {
    const html = getAIGeniusDashboard();
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(html);
    return;
  }
  
  // API: Get configuration
  if (url.pathname === '/api/config') {
    config = loadConfig(); // Reload in case edited
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(config));
    return;
  }
  
  // API: Get enabled models
  if (url.pathname === '/api/models') {
    const models = getEnabledModels();
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ models }));
    return;
  }
  
  // API: Get free models only
  if (url.pathname === '/api/models/free') {
    const models = getFreeModels();
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ models }));
    return;
  }
  
  // API: Smart routing
  if (url.pathname === '/api/route' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', async () => {
      try {
        const { task_type, message } = JSON.parse(body);
        const models = smartRoute(task_type);
        
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          task_type,
          recommended_models: models.map(m => m.name),
          message: `Recommended: ${models[0].name} ${models[0].icon}`
        }));
      } catch (error) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: error.message }));
      }
    });
    return;
  }
  
  // API: Ask AI
  if (url.pathname === '/api/ask' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', async () => {
      try {
        const { model_id, message, api_keys } = JSON.parse(body);
        const result = await callAI(model_id, message, api_keys || {});
        
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(result));
      } catch (error) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: error.message }));
      }
    });
    return;
  }
  
  // API: Compare multiple models
  if (url.pathname === '/api/compare' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', async () => {
      try {
        const { model_ids, message, api_keys } = JSON.parse(body);
        
        const results = await Promise.all(
          model_ids.map(id => callAI(id, message, api_keys || {}))
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
  
  // API: Update configuration
  if (url.pathname === '/api/config' && req.method === 'PUT') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const newConfig = JSON.parse(body);
        fs.writeFileSync(
          path.join(__dirname, 'ai-genius-config.json'),
          JSON.stringify(newConfig, null, 2)
        );
        config = newConfig;
        
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, message: 'Configuration updated' }));
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

function getAIGeniusDashboard() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI GENIUS - Master Control</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1f3a 0%, #0a0e27 100%);
            color: white;
            min-height: 100vh;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
            padding: 50px;
            text-align: center;
        }
        
        .logo {
            font-size: 72px;
            font-weight: 900;
            margin-bottom: 10px;
        }
        
        .container {
            max-width: 1800px;
            margin: 40px auto;
            padding: 0 40px;
        }
        
        .tabs {
            display: flex;
            gap: 20px;
            margin-bottom: 40px;
            border-bottom: 2px solid #2a3050;
        }
        
        .tab {
            padding: 15px 30px;
            background: none;
            border: none;
            color: #888;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: all 0.3s;
        }
        
        .tab.active {
            color: white;
            border-bottom-color: #667eea;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .models-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
        }
        
        .model-card {
            background: #1a1f3a;
            border-radius: 16px;
            padding: 30px;
            border: 2px solid #2a3050;
            transition: all 0.3s;
            cursor: pointer;
        }
        
        .model-card:hover {
            border-color: #667eea;
            transform: translateY(-5px);
        }
        
        .model-card.selected {
            border-color: #f093fb;
            background: #242943;
        }
        
        .model-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 15px;
        }
        
        .model-icon {
            font-size: 48px;
        }
        
        .model-name {
            font-size: 24px;
            font-weight: 700;
        }
        
        .model-desc {
            color: #aaa;
            margin-bottom: 15px;
            line-height: 1.5;
        }
        
        .model-badges {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .badge {
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .badge.free { background: #4caf50; }
        .badge.api { background: #2196f3; }
        .badge.local { background: #ff9800; }
        .badge.coding { background: #9c27b0; }
        
        .chat-container {
            background: #1a1f3a;
            border-radius: 20px;
            padding: 30px;
            margin-top: 40px;
        }
        
        .messages {
            max-height: 500px;
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
        
        .message.ai {
            background: linear-gradient(135deg, #667eea20, #764ba220);
            margin-right: 80px;
            border-left: 4px solid #667eea;
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
        
        .btn {
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
        
        .btn:hover { transform: translateY(-2px); }
        .btn:active { transform: translateY(0); }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .stat-card {
            background: #1a1f3a;
            border-radius: 16px;
            padding: 30px;
            text-align: center;
        }
        
        .stat-value {
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 10px;
        }
        
        .stat-label {
            color: #888;
            font-size: 14px;
            text-transform: uppercase;
        }
        
        .config-editor {
            background: #0a0e27;
            border: 2px solid #2a3050;
            border-radius: 12px;
            padding: 20px;
            font-family: 'Monaco', 'Courier New', monospace;
            font-size: 14px;
            color: #4caf50;
            min-height: 500px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">🤖 AI GENIUS</div>
        <h2>Master AI Management & Automation System</h2>
    </div>
    
    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value" id="totalModels">16</div>
                <div class="stat-label">Total Models</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="freeModels">10</div>
                <div class="stat-label">Free Models</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="enabledModels">16</div>
                <div class="stat-label">Enabled</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="messagesCount">0</div>
                <div class="stat-label">Messages Today</div>
            </div>
        </div>
        
        <div class="tabs">
            <button class="tab active" onclick="showTab('models')">📋 All Models</button>
            <button class="tab" onclick="showTab('chat')">💬 Chat</button>
            <button class="tab" onclick="showTab('compare')">🔀 Compare</button>
            <button class="tab" onclick="showTab('config')">⚙️ Configuration</button>
            <button class="tab" onclick="showTab('routing')">🧠 Smart Routing</button>
        </div>
        
        <div id="models-tab" class="tab-content active">
            <h2 style="margin-bottom: 20px;">Select AI Models</h2>
            <div class="models-grid" id="modelsGrid"></div>
        </div>
        
        <div id="chat-tab" class="tab-content">
            <h2 style="margin-bottom: 20px;">Chat with AI</h2>
            <div class="chat-container">
                <div class="messages" id="messages"></div>
                <div class="input-area">
                    <textarea id="messageInput" placeholder="Ask anything..."></textarea>
                    <button class="btn" onclick="sendMessage()">Send</button>
                </div>
            </div>
        </div>
        
        <div id="compare-tab" class="tab-content">
            <h2 style="margin-bottom: 20px;">Compare Multiple Models</h2>
            <div class="chat-container">
                <p style="margin-bottom: 20px; color: #aaa;">Select models to compare, then ask your question</p>
                <div id="compareModels"></div>
                <div class="input-area" style="margin-top: 20px;">
                    <textarea id="compareInput" placeholder="Question to compare..."></textarea>
                    <button class="btn" onclick="compareModels()">Compare</button>
                </div>
                <div id="compareResults" style="margin-top: 30px;"></div>
            </div>
        </div>
        
        <div id="config-tab" class="tab-content">
            <h2 style="margin-bottom: 20px;">Edit Configuration</h2>
            <p style="color: #aaa; margin-bottom: 20px;">Edit the JSON configuration below and click Save</p>
            <pre id="configEditor" class="config-editor" contenteditable="true"></pre>
            <button class="btn" onclick="saveConfig()" style="margin-top: 20px;">Save Configuration</button>
        </div>
        
        <div id="routing-tab" class="tab-content">
            <h2 style="margin-bottom: 20px;">Smart Routing</h2>
            <p style="color: #aaa; margin-bottom: 20px;">Let AI GENIUS choose the best model for your task</p>
            <div class="models-grid" id="routingGrid"></div>
        </div>
    </div>
    
    <script>
        let config = {};
        let selectedModels = [];
        let currentModel = null;
        
        // Load configuration
        async function loadConfig() {
            const response = await fetch('/api/config');
            config = await response.json();
            updateStats();
            renderModels();
            renderConfigEditor();
            renderRouting();
        }
        
        function updateStats() {
            const models = Object.values(config.models);
            const enabled = models.filter(m => m.enabled);
            const free = enabled.filter(m => m.free);
            
            document.getElementById('totalModels').textContent = models.length;
            document.getElementById('freeModels').textContent = free.length;
            document.getElementById('enabledModels').textContent = enabled.length;
        }
        
        function renderModels() {
            const grid = document.getElementById('modelsGrid');
            const compareGrid = document.getElementById('compareModels');
            grid.innerHTML = '';
            compareGrid.innerHTML = '';
            
            Object.entries(config.models).forEach(([id, model]) => {
                if (!model.enabled) return;
                
                const card = document.createElement('div');
                card.className = 'model-card';
                card.onclick = () => selectModel(id, card);
                
                const freeB badge = model.free ? '<span class="badge free">FREE</span>' : '';
                const typeB badge = \`<span class="badge \${model.category}">\${model.category}</span>\`;
                
                card.innerHTML = \`
                    <div class="model-header">
                        <div class="model-icon">\${model.icon}</div>
                        <div class="model-name">\${model.name}</div>
                    </div>
                    <div class="model-desc">\${model.description}</div>
                    <div class="model-badges">
                        \${freeBadge}
                        \${typeBadge}
                    </div>
                \`;
                
                grid.appendChild(card);
                
                // Add to compare grid
                const compareCard = card.cloneNode(true);
                compareCard.onclick = () => toggleCompareModel(id, compareCard);
                compareGrid.appendChild(compareCard);
            });
        }
        
        function selectModel(id, card) {
            document.querySelectorAll('#modelsGrid .model-card').forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            currentModel = id;
        }
        
        function toggleCompareModel(id, card) {
            if (selectedModels.includes(id)) {
                selectedModels = selectedModels.filter(m => m !== id);
                card.classList.remove('selected');
            } else {
                selectedModels.push(id);
                card.classList.add('selected');
            }
        }
        
        async function sendMessage() {
            if (!currentModel) {
                alert('Please select a model first');
                return;
            }
            
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            if (!message) return;
            
            input.value = '';
            addMessage('user', message);
            
            const response = await fetch('/api/ask', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    model_id: currentModel,
                    message: message,
                    api_keys: getAPIKeys()
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                addMessage('ai', data.response, data.model_name, data.icon);
            } else {
                addMessage('ai', 'Error: ' + data.error, currentModel);
            }
        }
        
        function addMessage(type, content, modelName, icon) {
            const container = document.getElementById('messages');
            const div = document.createElement('div');
            div.className = \`message \${type}\`;
            
            const header = type === 'user' ? 'You' : \`\${icon || '🤖'} \${modelName || 'AI'}\`;
            
            div.innerHTML = \`
                <div style="font-size: 12px; color: #888; margin-bottom: 10px;">\${header}</div>
                <div>\${content}</div>
            \`;
            
            container.appendChild(div);
            container.scrollTop = container.scrollHeight;
        }
        
        async function compareModels() {
            if (selectedModels.length === 0) {
                alert('Select at least one model to compare');
                return;
            }
            
            const input = document.getElementById('compareInput');
            const message = input.value.trim();
            if (!message) return;
            
            const results = document.getElementById('compareResults');
            results.innerHTML = '<p>Comparing models...</p>';
            
            const response = await fetch('/api/compare', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    model_ids: selectedModels,
                    message: message,
                    api_keys: getAPIKeys()
                })
            });
            
            const data = await response.json();
            
            results.innerHTML = '';
            data.results.forEach(result => {
                const card = document.createElement('div');
                card.className = 'model-card';
                card.style.marginBottom = '20px';
                
                card.innerHTML = \`
                    <div style="font-size: 24px; margin-bottom: 10px;">
                        \${result.icon} \${result.model_name}
                    </div>
                    <div style="color: #aaa; font-size: 12px; margin-bottom: 10px;">
                        \${result.response_time}ms · \${result.free ? 'FREE' : 'Paid'}
                    </div>
                    <div style="white-space: pre-wrap;">\${result.response}</div>
                \`;
                
                results.appendChild(card);
            });
        }
        
        function renderConfigEditor() {
            const editor = document.getElementById('configEditor');
            editor.textContent = JSON.stringify(config, null, 2);
        }
        
        async function saveConfig() {
            try {
                const newConfig = JSON.parse(document.getElementById('configEditor').textContent);
                
                const response = await fetch('/api/config', {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(newConfig)
                });
                
                const data = await response.json();
                if (data.success) {
                    alert('Configuration saved!');
                    await loadConfig();
                }
            } catch (error) {
                alert('Error saving configuration: ' + error.message);
            }
        }
        
        function renderRouting() {
            const grid = document.getElementById('routingGrid');
            grid.innerHTML = '';
            
            const tasks = [
                { type: 'code_review', name: 'Code Review', icon: '🔍' },
                { type: 'code_generation', name: 'Code Generation', icon: '💻' },
                { type: 'debugging', name: 'Debugging', icon: '🐛' },
                { type: 'research', name: 'Research', icon: '📚' },
                { type: 'writing', name: 'Writing', icon: '✍️' },
                { type: 'analysis', name: 'Analysis', icon: '📊' }
            ];
            
            tasks.forEach(task => {
                const models = config.routing[task.type] || [];
                
                const card = document.createElement('div');
                card.className = 'model-card';
                card.innerHTML = \`
                    <div style="font-size: 48px; margin-bottom: 15px;">\${task.icon}</div>
                    <div style="font-size: 20px; font-weight: 700; margin-bottom: 10px;">\${task.name}</div>
                    <div style="color: #aaa; font-size: 14px;">
                        Best models:<br>
                        \${models.map(m => config.models[m]?.name || m).join(', ')}
                    </div>
                \`;
                
                grid.appendChild(card);
            });
        }
        
        function showTab(tabName) {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            
            event.target.classList.add('active');
            document.getElementById(\`\${tabName}-tab\`).classList.add('active');
        }
        
        function getAPIKeys() {
            return {
                ANTHROPIC_API_KEY: localStorage.getItem('anthropic_key'),
                GOOGLE_API_KEY: localStorage.getItem('google_key'),
                TOGETHER_API_KEY: localStorage.getItem('together_key'),
                PERPLEXITY_API_KEY: localStorage.getItem('perplexity_key')
            };
        }
        
        // Load on start
        loadConfig();
    </script>
</body>
</html>`;
}

server.listen(PORT, '0.0.0.0', () => {
  console.log('🤖 AI GENIUS - Master AI Management System');
  console.log('===========================================');
  console.log('');
  console.log(`✅ Running on port ${PORT}`);
  console.log('');
  console.log('Access:');
  console.log(`  http://localhost:${PORT}`);
  console.log(`  http://GOD.local:${PORT}`);
  console.log(`  http://10.90.90.x:${PORT} (iPad)`);
  console.log('');
  console.log('Features:');
  console.log('  • 16+ AI models managed');
  console.log('  • 10+ FREE models included');
  console.log('  • Smart routing by task type');
  console.log('  • Multi-model comparison');
  console.log('  • Editable configuration');
  console.log('  • Full automation');
  console.log('');
  console.log('Edit config:');
  console.log('  nano ai-genius-config.json');
  console.log('  OR use web dashboard');
  console.log('');
  console.log('GORUNFREE X1000 ✨');
});
