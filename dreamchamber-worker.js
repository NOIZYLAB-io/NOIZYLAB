// THE DREAMCHAMBER - UNIFIED AI MODEL INTERFACE
// Access Claude, GPT-4, Gemini, Llama, and more from one place
// Voice-controlled, touchscreen-optimized, GORUNFREE compliant

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    if (url.pathname === '/') {
      return new Response(getDreamChamberHTML(), {
        headers: { 'Content-Type': 'text/html' }
      });
    }
    
    if (url.pathname === '/api/query' && request.method === 'POST') {
      return await handleQuery(request, env);
    }
    
    if (url.pathname === '/api/compare' && request.method === 'POST') {
      return await handleCompare(request, env);
    }
    
    return new Response('Not Found', { status: 404 });
  }
};

// Query single model
async function handleQuery(request, env) {
  const { model, prompt, context } = await request.json();
  
  const startTime = Date.now();
  let response;
  
  try {
    switch(model) {
      case 'claude-sonnet-4':
        response = await queryClaude(prompt, context, env, 'claude-sonnet-4-20250514');
        break;
      case 'claude-opus-4':
        response = await queryClaude(prompt, context, env, 'claude-opus-4-20250514');
        break;
      case 'gpt-4':
        response = await queryGPT4(prompt, context, env);
        break;
      case 'gpt-4o':
        response = await queryGPT4o(prompt, context, env);
        break;
      case 'gemini-pro':
        response = await queryGemini(prompt, context, env, 'gemini-pro');
        break;
      case 'gemini-ultra':
        response = await queryGemini(prompt, context, env, 'gemini-ultra');
        break;
      case 'llama-3':
        response = await queryLlama(prompt, context, env);
        break;
      case 'mistral-large':
        response = await queryMistral(prompt, context, env);
        break;
      case 'perplexity':
        response = await queryPerplexity(prompt, context, env);
        break;
      case 'grok':
        response = await queryGrok(prompt, context, env);
        break;
      default:
        throw new Error('Unknown model');
    }
    
    const processingTime = Date.now() - startTime;
    
    return Response.json({
      success: true,
      model,
      response,
      processing_time: processingTime,
      cost: estimateCost(model, prompt, response)
    });
    
  } catch (error) {
    return Response.json({
      success: false,
      error: error.message
    }, { status: 500 });
  }
}

// Compare multiple models
async function handleCompare(request, env) {
  const { models, prompt, context } = await request.json();
  
  const results = await Promise.all(
    models.map(async model => {
      try {
        const startTime = Date.now();
        let response;
        
        switch(model) {
          case 'claude-sonnet-4':
            response = await queryClaude(prompt, context, env, 'claude-sonnet-4-20250514');
            break;
          case 'claude-opus-4':
            response = await queryClaude(prompt, context, env, 'claude-opus-4-20250514');
            break;
          case 'gpt-4':
            response = await queryGPT4(prompt, context, env);
            break;
          case 'gpt-4o':
            response = await queryGPT4o(prompt, context, env);
            break;
          case 'gemini-pro':
            response = await queryGemini(prompt, context, env, 'gemini-pro');
            break;
          default:
            response = 'Model not available';
        }
        
        return {
          model,
          response,
          processing_time: Date.now() - startTime,
          success: true
        };
      } catch (error) {
        return {
          model,
          error: error.message,
          success: false
        };
      }
    })
  );
  
  return Response.json({ results });
}

// Claude API
async function queryClaude(prompt, context, env, model) {
  const messages = context?.history || [];
  messages.push({ role: 'user', content: prompt });
  
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'anthropic-version': '2023-06-01',
      'x-api-key': env.ANTHROPIC_API_KEY
    },
    body: JSON.stringify({
      model,
      max_tokens: 4000,
      messages
    })
  });
  
  if (!response.ok) {
    throw new Error('Claude API error: ' + await response.text());
  }
  
  const data = await response.json();
  return data.content[0].text;
}

// OpenAI GPT-4 API
async function queryGPT4(prompt, context, env) {
  const messages = context?.history?.map(m => ({
    role: m.role,
    content: m.content
  })) || [];
  messages.push({ role: 'user', content: prompt });
  
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-4',
      messages,
      max_tokens: 4000
    })
  });
  
  if (!response.ok) {
    throw new Error('OpenAI API error: ' + await response.text());
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

// OpenAI GPT-4o API
async function queryGPT4o(prompt, context, env) {
  const messages = context?.history?.map(m => ({
    role: m.role,
    content: m.content
  })) || [];
  messages.push({ role: 'user', content: prompt });
  
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-4o',
      messages,
      max_tokens: 4000
    })
  });
  
  if (!response.ok) {
    throw new Error('OpenAI API error: ' + await response.text());
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

// Google Gemini API
async function queryGemini(prompt, context, env, model) {
  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${env.GOOGLE_API_KEY}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          parts: [{ text: prompt }]
        }]
      })
    }
  );
  
  if (!response.ok) {
    throw new Error('Gemini API error: ' + await response.text());
  }
  
  const data = await response.json();
  return data.candidates[0].content.parts[0].text;
}

// Meta Llama (via Replicate or Together AI)
async function queryLlama(prompt, context, env) {
  const response = await fetch('https://api.together.xyz/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.TOGETHER_API_KEY}`
    },
    body: JSON.stringify({
      model: 'meta-llama/Llama-3-70b-chat-hf',
      messages: [{ role: 'user', content: prompt }],
      max_tokens: 4000
    })
  });
  
  if (!response.ok) {
    throw new Error('Llama API error: ' + await response.text());
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

// Mistral API
async function queryMistral(prompt, context, env) {
  const response = await fetch('https://api.mistral.ai/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.MISTRAL_API_KEY}`
    },
    body: JSON.stringify({
      model: 'mistral-large-latest',
      messages: [{ role: 'user', content: prompt }],
      max_tokens: 4000
    })
  });
  
  if (!response.ok) {
    throw new Error('Mistral API error: ' + await response.text());
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

// Perplexity API
async function queryPerplexity(prompt, context, env) {
  const response = await fetch('https://api.perplexity.ai/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.PERPLEXITY_API_KEY}`
    },
    body: JSON.stringify({
      model: 'llama-3.1-sonar-large-128k-online',
      messages: [{ role: 'user', content: prompt }]
    })
  });
  
  if (!response.ok) {
    throw new Error('Perplexity API error: ' + await response.text());
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

// xAI Grok API
async function queryGrok(prompt, context, env) {
  const response = await fetch('https://api.x.ai/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.XAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'grok-beta',
      messages: [{ role: 'user', content: prompt }]
    })
  });
  
  if (!response.ok) {
    throw new Error('Grok API error: ' + await response.text());
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

// Cost estimation
function estimateCost(model, prompt, response) {
  const promptTokens = Math.ceil(prompt.length / 4);
  const responseTokens = Math.ceil(response.length / 4);
  
  const costs = {
    'claude-sonnet-4': { input: 3, output: 15 },
    'claude-opus-4': { input: 15, output: 75 },
    'gpt-4': { input: 30, output: 60 },
    'gpt-4o': { input: 5, output: 15 },
    'gemini-pro': { input: 0.5, output: 1.5 },
    'gemini-ultra': { input: 5, output: 15 },
    'llama-3': { input: 0.2, output: 0.2 },
    'mistral-large': { input: 4, output: 12 },
    'perplexity': { input: 1, output: 1 },
    'grok': { input: 5, output: 15 }
  };
  
  const modelCost = costs[model] || { input: 1, output: 1 };
  
  return (
    (promptTokens * modelCost.input / 1000000) +
    (responseTokens * modelCost.output / 1000000)
  ).toFixed(4);
}

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
            overflow-x: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
        }
        
        .logo {
            font-size: 64px;
            font-weight: 900;
            text-shadow: 0 4px 20px rgba(0,0,0,0.3);
            margin-bottom: 10px;
        }
        
        .tagline {
            font-size: 20px;
            opacity: 0.9;
        }
        
        .container {
            max-width: 1800px;
            margin: 0 auto;
            padding: 30px;
        }
        
        .model-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }
        
        .model-btn {
            padding: 30px 20px;
            background: #1a1f3a;
            border: 3px solid transparent;
            border-radius: 16px;
            cursor: pointer;
            transition: all 0.3s;
            text-align: center;
        }
        
        .model-btn:hover {
            border-color: #667eea;
            transform: translateY(-2px);
        }
        
        .model-btn.selected {
            border-color: #667eea;
            background: linear-gradient(135deg, #667eea20, #764ba220);
        }
        
        .model-name {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 5px;
        }
        
        .model-desc {
            font-size: 12px;
            color: #888;
        }
        
        .input-area {
            background: #1a1f3a;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
        }
        
        textarea {
            width: 100%;
            min-height: 150px;
            background: #0a0e27;
            border: 2px solid #667eea;
            border-radius: 12px;
            padding: 20px;
            color: white;
            font-size: 18px;
            font-family: inherit;
            resize: vertical;
        }
        
        .action-bar {
            display: flex;
            gap: 15px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        
        .btn {
            padding: 20px 40px;
            border: none;
            border-radius: 12px;
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
            transition: transform 0.2s;
            flex: 1;
            min-width: 200px;
        }
        
        .btn:active {
            transform: scale(0.98);
        }
        
        .btn-query {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        
        .btn-compare {
            background: linear-gradient(135deg, #f093fb, #f5576c);
            color: white;
        }
        
        .btn-voice {
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            color: white;
        }
        
        .btn-clear {
            background: #2a3050;
            color: white;
        }
        
        .results {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
        }
        
        .result-card {
            background: #1a1f3a;
            border-radius: 16px;
            padding: 25px;
            border-left: 4px solid #667eea;
        }
        
        .result-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .result-model {
            font-size: 24px;
            font-weight: 700;
        }
        
        .result-meta {
            font-size: 12px;
            color: #888;
        }
        
        .result-content {
            background: #0a0e27;
            padding: 20px;
            border-radius: 12px;
            max-height: 500px;
            overflow-y: auto;
            line-height: 1.6;
            white-space: pre-wrap;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            font-size: 24px;
            color: #667eea;
        }
        
        .voice-indicator {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0,0,0,0.9);
            padding: 60px;
            border-radius: 30px;
            display: none;
            z-index: 1000;
        }
        
        .voice-indicator.active {
            display: block;
        }
        
        .voice-icon {
            font-size: 80px;
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.7; transform: scale(1.1); }
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: #1a1f3a;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }
        
        .stat-value {
            font-size: 32px;
            font-weight: 900;
            color: #667eea;
        }
        
        .stat-label {
            font-size: 12px;
            color: #888;
            text-transform: uppercase;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">🌌 THE DREAMCHAMBER</div>
        <div class="tagline">All AI Models of Repute • Unified Interface • Voice Controlled</div>
    </div>
    
    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value" id="totalQueries">0</div>
                <div class="stat-label">Total Queries</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="totalCost">$0.00</div>
                <div class="stat-label">Total Cost</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="avgTime">0ms</div>
                <div class="stat-label">Avg Response</div>
            </div>
        </div>
        
        <h2 style="margin-bottom: 20px; font-size: 28px;">Select Models</h2>
        <div class="model-grid">
            <div class="model-btn" data-model="claude-sonnet-4" onclick="toggleModel(this)">
                <div class="model-name">Claude Sonnet 4</div>
                <div class="model-desc">Anthropic • Balanced</div>
            </div>
            <div class="model-btn" data-model="claude-opus-4" onclick="toggleModel(this)">
                <div class="model-name">Claude Opus 4</div>
                <div class="model-desc">Anthropic • Most Capable</div>
            </div>
            <div class="model-btn" data-model="gpt-4" onclick="toggleModel(this)">
                <div class="model-name">GPT-4</div>
                <div class="model-desc">OpenAI • Original</div>
            </div>
            <div class="model-btn" data-model="gpt-4o" onclick="toggleModel(this)">
                <div class="model-name">GPT-4o</div>
                <div class="model-desc">OpenAI • Omni</div>
            </div>
            <div class="model-btn" data-model="gemini-pro" onclick="toggleModel(this)">
                <div class="model-name">Gemini Pro</div>
                <div class="model-desc">Google • Fast</div>
            </div>
            <div class="model-btn" data-model="gemini-ultra" onclick="toggleModel(this)">
                <div class="model-name">Gemini Ultra</div>
                <div class="model-desc">Google • Advanced</div>
            </div>
            <div class="model-btn" data-model="llama-3" onclick="toggleModel(this)">
                <div class="model-name">Llama 3</div>
                <div class="model-desc">Meta • Open Source</div>
            </div>
            <div class="model-btn" data-model="mistral-large" onclick="toggleModel(this)">
                <div class="model-name">Mistral Large</div>
                <div class="model-desc">Mistral AI • European</div>
            </div>
            <div class="model-btn" data-model="perplexity" onclick="toggleModel(this)">
                <div class="model-name">Perplexity</div>
                <div class="model-desc">Perplexity • Online</div>
            </div>
            <div class="model-btn" data-model="grok" onclick="toggleModel(this)">
                <div class="model-name">Grok</div>
                <div class="model-desc">xAI • Elon Musk</div>
            </div>
        </div>
        
        <div class="input-area">
            <textarea id="prompt" placeholder="Ask anything... All selected models will respond."></textarea>
            <div class="action-bar">
                <button class="btn btn-query" onclick="queryModels()">🚀 Query Selected</button>
                <button class="btn btn-compare" onclick="compareAll()">⚔️ Compare All</button>
                <button class="btn btn-voice" onclick="startVoice()">🎤 Voice Input</button>
                <button class="btn btn-clear" onclick="clearAll()">🗑️ Clear</button>
            </div>
        </div>
        
        <div id="results" class="results"></div>
    </div>
    
    <div class="voice-indicator" id="voiceIndicator">
        <div class="voice-icon">🎤</div>
        <div style="text-align: center; margin-top: 20px; font-size: 20px;">Listening...</div>
    </div>
    
    <script>
        const API_URL = window.location.origin;
        let selectedModels = new Set(['claude-sonnet-4']);
        let totalQueries = 0;
        let totalCost = 0;
        let totalTime = 0;
        let recognition = null;
        
        // Auto-select Claude by default
        document.querySelector('[data-model="claude-sonnet-4"]').classList.add('selected');
        
        // Voice recognition setup
        if ('webkitSpeechRecognition' in window) {
            recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            
            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                document.getElementById('prompt').value = transcript;
                document.getElementById('voiceIndicator').classList.remove('active');
            };
            
            recognition.onend = () => {
                document.getElementById('voiceIndicator').classList.remove('active');
            };
        }
        
        function toggleModel(element) {
            const model = element.dataset.model;
            if (selectedModels.has(model)) {
                selectedModels.delete(model);
                element.classList.remove('selected');
            } else {
                selectedModels.add(model);
                element.classList.add('selected');
            }
        }
        
        function startVoice() {
            if (recognition) {
                document.getElementById('voiceIndicator').classList.add('active');
                recognition.start();
            } else {
                alert('Voice recognition not supported');
            }
        }
        
        async function queryModels() {
            if (selectedModels.size === 0) {
                alert('Select at least one model');
                return;
            }
            
            const prompt = document.getElementById('prompt').value;
            if (!prompt) {
                alert('Enter a prompt');
                return;
            }
            
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<div class="loading">Querying models...</div>';
            
            if (selectedModels.size === 1) {
                // Single model query
                const model = Array.from(selectedModels)[0];
                
                const response = await fetch(API_URL + '/api/query', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ model, prompt })
                });
                
                const data = await response.json();
                displaySingleResult(data);
                
            } else {
                // Multiple model query
                const response = await fetch(API_URL + '/api/compare', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        models: Array.from(selectedModels), 
                        prompt 
                    })
                });
                
                const data = await response.json();
                displayCompareResults(data.results);
            }
        }
        
        async function compareAll() {
            document.getElementById('prompt').value || alert('Enter a prompt first');
            
            // Select all models
            document.querySelectorAll('.model-btn').forEach(btn => {
                selectedModels.add(btn.dataset.model);
                btn.classList.add('selected');
            });
            
            await queryModels();
        }
        
        function displaySingleResult(data) {
            const resultsDiv = document.getElementById('results');
            
            if (!data.success) {
                resultsDiv.innerHTML = \`<div class="result-card"><div class="result-content">Error: \${data.error}</div></div>\`;
                return;
            }
            
            resultsDiv.innerHTML = \`
                <div class="result-card">
                    <div class="result-header">
                        <div class="result-model">\${data.model}</div>
                        <div class="result-meta">
                            \${data.processing_time}ms • $\${data.cost}
                        </div>
                    </div>
                    <div class="result-content">\${data.response}</div>
                </div>
            \`;
            
            updateStats(1, parseFloat(data.cost), data.processing_time);
        }
        
        function displayCompareResults(results) {
            const resultsDiv = document.getElementById('results');
            
            resultsDiv.innerHTML = results.map(result => {
                if (!result.success) {
                    return \`
                        <div class="result-card">
                            <div class="result-header">
                                <div class="result-model">\${result.model}</div>
                            </div>
                            <div class="result-content">Error: \${result.error}</div>
                        </div>
                    \`;
                }
                
                return \`
                    <div class="result-card">
                        <div class="result-header">
                            <div class="result-model">\${result.model}</div>
                            <div class="result-meta">\${result.processing_time}ms</div>
                        </div>
                        <div class="result-content">\${result.response}</div>
                    </div>
                \`;
            }).join('');
            
            const successfulResults = results.filter(r => r.success);
            const avgTime = successfulResults.reduce((sum, r) => sum + r.processing_time, 0) / successfulResults.length;
            updateStats(successfulResults.length, 0, avgTime);
        }
        
        function updateStats(queries, cost, time) {
            totalQueries += queries;
            totalCost += cost;
            totalTime = (totalTime * (totalQueries - queries) + time * queries) / totalQueries;
            
            document.getElementById('totalQueries').textContent = totalQueries;
            document.getElementById('totalCost').textContent = '$' + totalCost.toFixed(4);
            document.getElementById('avgTime').textContent = Math.round(totalTime) + 'ms';
        }
        
        function clearAll() {
            document.getElementById('prompt').value = '';
            document.getElementById('results').innerHTML = '';
        }
    </script>
</body>
</html>`;
}
