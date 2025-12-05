// AI GENIUS CLOUDFLARE WORKER
// Universal AI Router - Access all your paid models from anywhere
// GORUNFREEX1000 - Cloud Edition

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // Health check
      if (path === '/health' || path === '/api/health') {
        return jsonResponse({
          status: 'operational',
          timestamp: new Date().toISOString(),
          worker: 'ai-genius-cloud',
          version: '1.0.0'
        }, corsHeaders);
      }

      // Serve UI
      if (path === '/' || path === '/index.html') {
        return new Response(getHTML(), {
          headers: { ...corsHeaders, 'Content-Type': 'text/html' }
        });
      }

      // Get available models
      if (path === '/api/models') {
        return jsonResponse(getAvailableModels(env), corsHeaders);
      }

      // Get configuration
      if (path === '/api/config') {
        return jsonResponse({
          models: getAvailableModels(env),
          worker: 'ai-genius-cloud',
          timestamp: new Date().toISOString()
        }, corsHeaders);
      }

      // Ask AI endpoint
      if (path === '/api/ask' && request.method === 'POST') {
        const body = await request.json();
        return await askAI(body, env, corsHeaders);
      }

      // Compare multiple models
      if (path === '/api/compare' && request.method === 'POST') {
        const body = await request.json();
        return await compareModels(body, env, corsHeaders);
      }

      // Smart routing
      if (path === '/api/route' && request.method === 'POST') {
        const body = await request.json();
        return jsonResponse(smartRoute(body.task_type || body.message), corsHeaders);
      }

      return new Response('Not Found', { status: 404, headers: corsHeaders });

    } catch (error) {
      console.error('Worker error:', error);
      return jsonResponse({
        error: error.message,
        stack: error.stack
      }, corsHeaders, 500);
    }
  }
};

// Get available models based on configured API keys
function getAvailableModels(env) {
  const models = [];

  // Claude (Anthropic)
  if (env.ANTHROPIC_API_KEY) {
    models.push({
      id: 'claude-sonnet-4',
      name: 'Claude Sonnet 4',
      provider: 'Anthropic',
      icon: '⚡',
      cost: '$3/M input, $15/M output',
      context: '200K',
      available: true,
      best_for: ['reasoning', 'coding', 'writing', 'analysis']
    });
    models.push({
      id: 'claude-opus-4',
      name: 'Claude Opus 4',
      provider: 'Anthropic',
      icon: '👑',
      cost: '$15/M input, $75/M output',
      context: '200K',
      available: true,
      best_for: ['complex_reasoning', 'research', 'expert_analysis']
    });
  }

  // OpenAI (GPT)
  if (env.OPENAI_API_KEY) {
    models.push({
      id: 'gpt-4o',
      name: 'GPT-4o',
      provider: 'OpenAI',
      icon: '🔮',
      cost: '$2.50/M tokens',
      context: '128K',
      available: true,
      best_for: ['general', 'speed', 'vision']
    });
    models.push({
      id: 'gpt-4-turbo',
      name: 'GPT-4 Turbo',
      provider: 'OpenAI',
      icon: '🚀',
      cost: '$10/M tokens',
      context: '128K',
      available: true,
      best_for: ['complex_tasks', 'reasoning']
    });
    models.push({
      id: 'o1',
      name: 'OpenAI o1',
      provider: 'OpenAI',
      icon: '🧠',
      cost: '$15/M input, $60/M output',
      context: '200K',
      available: true,
      best_for: ['complex_reasoning', 'math', 'science']
    });
  }

  // Google (Gemini)
  if (env.GOOGLE_API_KEY) {
    models.push({
      id: 'gemini-2-flash',
      name: 'Gemini 2.0 Flash',
      provider: 'Google',
      icon: '💎',
      cost: '$0.075/M (FREE tier)',
      context: '1M',
      available: true,
      best_for: ['speed', 'long_documents', 'cost_effective']
    });
    models.push({
      id: 'gemini-pro',
      name: 'Gemini Pro',
      provider: 'Google',
      icon: '💠',
      cost: '$0.125/M',
      context: '2M',
      available: true,
      best_for: ['long_context', 'analysis']
    });
  }

  // Perplexity
  if (env.PERPLEXITY_API_KEY) {
    models.push({
      id: 'perplexity-online',
      name: 'Perplexity Online',
      provider: 'Perplexity',
      icon: '🔍',
      cost: 'Varies by plan',
      context: '128K',
      available: true,
      best_for: ['research', 'current_events', 'web_search']
    });
  }

  // Together AI (Llama, Mixtral, etc.)
  if (env.TOGETHER_API_KEY) {
    models.push({
      id: 'llama-3-3-70b',
      name: 'Llama 3.3 70B',
      provider: 'Together AI',
      icon: '🦙',
      cost: '$0.88/M',
      context: '128K',
      available: true,
      best_for: ['open_source', 'cost_effective']
    });
    models.push({
      id: 'mixtral-8x7b',
      name: 'Mixtral 8x7B',
      provider: 'Together AI',
      icon: '🎯',
      cost: '$0.60/M',
      context: '32K',
      available: true,
      best_for: ['speed', 'efficiency']
    });
  }

  // Cohere
  if (env.COHERE_API_KEY) {
    models.push({
      id: 'command-r-plus',
      name: 'Command R+',
      provider: 'Cohere',
      icon: '💫',
      cost: '$3/M',
      context: '128K',
      available: true,
      best_for: ['rag', 'search', 'enterprise']
    });
  }

  // Mistral
  if (env.MISTRAL_API_KEY) {
    models.push({
      id: 'mistral-large',
      name: 'Mistral Large',
      provider: 'Mistral',
      icon: '🌪️',
      cost: '$2/M',
      context: '128K',
      available: true,
      best_for: ['multilingual', 'reasoning']
    });
  }

  return models;
}

// Ask AI
async function askAI(body, env, corsHeaders) {
  const { model_id, message, system_prompt, temperature = 0.7, max_tokens = 4000 } = body;

  if (!message) {
    return jsonResponse({ error: 'Message required' }, corsHeaders, 400);
  }

  const startTime = Date.now();

  try {
    let response;

    // Route to appropriate API
    if (model_id.includes('claude')) {
      response = await callAnthropic(model_id, message, system_prompt, env, temperature, max_tokens);
    } else if (model_id.includes('gpt') || model_id.includes('o1')) {
      response = await callOpenAI(model_id, message, system_prompt, env, temperature, max_tokens);
    } else if (model_id.includes('gemini')) {
      response = await callGoogle(model_id, message, system_prompt, env, temperature, max_tokens);
    } else if (model_id.includes('perplexity')) {
      response = await callPerplexity(model_id, message, system_prompt, env, temperature, max_tokens);
    } else if (model_id.includes('llama') || model_id.includes('mixtral')) {
      response = await callTogether(model_id, message, system_prompt, env, temperature, max_tokens);
    } else if (model_id.includes('command')) {
      response = await callCohere(model_id, message, system_prompt, env, temperature, max_tokens);
    } else if (model_id.includes('mistral')) {
      response = await callMistral(model_id, message, system_prompt, env, temperature, max_tokens);
    } else {
      return jsonResponse({ error: 'Unknown model' }, corsHeaders, 400);
    }

    const endTime = Date.now();
    const duration = endTime - startTime;

    return jsonResponse({
      model: model_id,
      response: response,
      duration_ms: duration,
      timestamp: new Date().toISOString()
    }, corsHeaders);

  } catch (error) {
    return jsonResponse({
      error: error.message,
      model: model_id
    }, corsHeaders, 500);
  }
}

// Anthropic API
async function callAnthropic(model_id, message, system_prompt, env, temperature, max_tokens) {
  const modelMap = {
    'claude-sonnet-4': 'claude-sonnet-4-20250514',
    'claude-opus-4': 'claude-opus-4-20250514'
  };

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: modelMap[model_id] || model_id,
      max_tokens: max_tokens,
      temperature: temperature,
      system: system_prompt || undefined,
      messages: [{ role: 'user', content: message }]
    })
  });

  if (!response.ok) {
    throw new Error(`Anthropic API error: ${response.status}`);
  }

  const data = await response.json();
  return data.content[0].text;
}

// OpenAI API
async function callOpenAI(model_id, message, system_prompt, env, temperature, max_tokens) {
  const modelMap = {
    'gpt-4o': 'gpt-4o',
    'gpt-4-turbo': 'gpt-4-turbo-preview',
    'o1': 'o1-preview'
  };

  const messages = [];
  if (system_prompt) {
    messages.push({ role: 'system', content: system_prompt });
  }
  messages.push({ role: 'user', content: message });

  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: modelMap[model_id] || model_id,
      messages: messages,
      temperature: model_id === 'o1' ? 1 : temperature,
      max_tokens: max_tokens
    })
  });

  if (!response.ok) {
    throw new Error(`OpenAI API error: ${response.status}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

// Google API
async function callGoogle(model_id, message, system_prompt, env, temperature, max_tokens) {
  const modelMap = {
    'gemini-2-flash': 'gemini-2.0-flash-exp',
    'gemini-pro': 'gemini-pro'
  };

  const fullPrompt = system_prompt ? `${system_prompt}\n\n${message}` : message;

  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/${modelMap[model_id]}:generateContent?key=${env.GOOGLE_API_KEY}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: fullPrompt }] }],
        generationConfig: {
          temperature: temperature,
          maxOutputTokens: max_tokens
        }
      })
    }
  );

  if (!response.ok) {
    throw new Error(`Google API error: ${response.status}`);
  }

  const data = await response.json();
  return data.candidates[0].content.parts[0].text;
}

// Perplexity API
async function callPerplexity(model_id, message, system_prompt, env, temperature, max_tokens) {
  const messages = [];
  if (system_prompt) {
    messages.push({ role: 'system', content: system_prompt });
  }
  messages.push({ role: 'user', content: message });

  const response = await fetch('https://api.perplexity.ai/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.PERPLEXITY_API_KEY}`
    },
    body: JSON.stringify({
      model: 'llama-3.1-sonar-large-128k-online',
      messages: messages,
      temperature: temperature,
      max_tokens: max_tokens
    })
  });

  if (!response.ok) {
    throw new Error(`Perplexity API error: ${response.status}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

// Together AI API
async function callTogether(model_id, message, system_prompt, env, temperature, max_tokens) {
  const modelMap = {
    'llama-3-3-70b': 'meta-llama/Meta-Llama-3.3-70B-Instruct-Turbo',
    'mixtral-8x7b': 'mistralai/Mixtral-8x7B-Instruct-v0.1'
  };

  const messages = [];
  if (system_prompt) {
    messages.push({ role: 'system', content: system_prompt });
  }
  messages.push({ role: 'user', content: message });

  const response = await fetch('https://api.together.xyz/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.TOGETHER_API_KEY}`
    },
    body: JSON.stringify({
      model: modelMap[model_id] || model_id,
      messages: messages,
      temperature: temperature,
      max_tokens: max_tokens
    })
  });

  if (!response.ok) {
    throw new Error(`Together API error: ${response.status}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

// Cohere API
async function callCohere(model_id, message, system_prompt, env, temperature, max_tokens) {
  const response = await fetch('https://api.cohere.ai/v1/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.COHERE_API_KEY}`
    },
    body: JSON.stringify({
      model: 'command-r-plus',
      message: message,
      preamble: system_prompt || undefined,
      temperature: temperature,
      max_tokens: max_tokens
    })
  });

  if (!response.ok) {
    throw new Error(`Cohere API error: ${response.status}`);
  }

  const data = await response.json();
  return data.text;
}

// Mistral API
async function callMistral(model_id, message, system_prompt, env, temperature, max_tokens) {
  const messages = [];
  if (system_prompt) {
    messages.push({ role: 'system', content: system_prompt });
  }
  messages.push({ role: 'user', content: message });

  const response = await fetch('https://api.mistral.ai/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.MISTRAL_API_KEY}`
    },
    body: JSON.stringify({
      model: 'mistral-large-latest',
      messages: messages,
      temperature: temperature,
      max_tokens: max_tokens
    })
  });

  if (!response.ok) {
    throw new Error(`Mistral API error: ${response.status}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

// Compare multiple models
async function compareModels(body, env, corsHeaders) {
  const { model_ids, message, system_prompt } = body;

  if (!model_ids || !Array.isArray(model_ids) || model_ids.length === 0) {
    return jsonResponse({ error: 'model_ids array required' }, corsHeaders, 400);
  }

  if (!message) {
    return jsonResponse({ error: 'Message required' }, corsHeaders, 400);
  }

  const results = await Promise.allSettled(
    model_ids.map(async (model_id) => {
      const startTime = Date.now();
      try {
        const result = await askAI({ model_id, message, system_prompt }, env, corsHeaders);
        const data = await result.json();
        return {
          model: model_id,
          response: data.response,
          duration_ms: Date.now() - startTime,
          status: 'success'
        };
      } catch (error) {
        return {
          model: model_id,
          error: error.message,
          duration_ms: Date.now() - startTime,
          status: 'error'
        };
      }
    })
  );

  return jsonResponse({
    message: message,
    results: results.map(r => r.value || r.reason),
    timestamp: new Date().toISOString()
  }, corsHeaders);
}

// Smart routing
function smartRoute(task) {
  const routes = {
    'code': ['claude-sonnet-4', 'gpt-4o', 'claude-opus-4'],
    'reasoning': ['claude-opus-4', 'o1', 'claude-sonnet-4'],
    'research': ['perplexity-online', 'claude-sonnet-4', 'gpt-4o'],
    'speed': ['gemini-2-flash', 'gpt-4o', 'mixtral-8x7b'],
    'cost': ['gemini-2-flash', 'mixtral-8x7b', 'llama-3-3-70b'],
    'long_context': ['gemini-pro', 'claude-sonnet-4', 'gpt-4-turbo']
  };

  // Detect task type from message
  const taskLower = (task || '').toLowerCase();
  for (const [type, models] of Object.entries(routes)) {
    if (taskLower.includes(type)) {
      return { task_type: type, recommended_models: models };
    }
  }

  // Default
  return { task_type: 'general', recommended_models: ['claude-sonnet-4', 'gpt-4o', 'gemini-2-flash'] };
}

// Helper function
function jsonResponse(data, headers = {}, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status: status,
    headers: { ...headers, 'Content-Type': 'application/json' }
  });
}

// HTML UI
function getHTML() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI GENIUS Cloud - Universal AI Router</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            background: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            text-align: center;
        }
        .header h1 {
            font-size: 2.5em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .header p {
            color: #666;
            font-size: 1.1em;
        }
        .card {
            background: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        .models-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }
        .model-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            border-radius: 15px;
            cursor: pointer;
            transition: all 0.3s;
            border: 3px solid transparent;
        }
        .model-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
        .model-card.selected {
            border-color: #667eea;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .model-icon {
            font-size: 2em;
            margin-bottom: 10px;
        }
        .model-name {
            font-weight: bold;
            margin-bottom: 5px;
        }
        .model-provider {
            font-size: 0.9em;
            opacity: 0.8;
            margin-bottom: 5px;
        }
        .model-cost {
            font-size: 0.85em;
            opacity: 0.7;
        }
        .chat-area {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        textarea {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1em;
            font-family: inherit;
            resize: vertical;
            min-height: 120px;
        }
        textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        .button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 10px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }
        .button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }
        .button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        .response {
            background: #f5f7fa;
            padding: 20px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-family: 'Monaco', 'Courier New', monospace;
            font-size: 0.9em;
            line-height: 1.6;
            max-height: 400px;
            overflow-y: auto;
        }
        .loading {
            text-align: center;
            padding: 20px;
            color: #667eea;
            font-size: 1.1em;
        }
        .stats {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
            font-size: 0.9em;
            color: #666;
        }
        .tab-buttons {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        .tab-button {
            padding: 10px 20px;
            background: white;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .tab-button.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-color: transparent;
        }
        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 AI GENIUS Cloud</h1>
            <p>Universal AI Router - Access All Your Paid Models</p>
            <p style="font-size: 0.9em; color: #999; margin-top: 10px;">GORUNFREEX1000 - Cloud Edition</p>
        </div>

        <div class="card">
            <div class="tab-buttons">
                <div class="tab-button active" onclick="switchTab('chat')">💬 Chat</div>
                <div class="tab-button" onclick="switchTab('compare')">🔀 Compare</div>
                <div class="tab-button" onclick="switchTab('models')">🤖 Models</div>
            </div>

            <div id="chat-tab" class="tab-content active">
                <h2 style="margin-bottom: 20px;">Select a Model</h2>
                <div id="models-grid" class="models-grid"></div>
                
                <div class="chat-area" style="margin-top: 30px;">
                    <textarea id="message" placeholder="Enter your message..."></textarea>
                    <button class="button" onclick="askAI()">Send to AI</button>
                    <div id="response-area" style="display: none;">
                        <h3 style="margin-bottom: 10px;">Response:</h3>
                        <div id="response" class="response"></div>
                        <div id="stats" class="stats"></div>
                    </div>
                </div>
            </div>

            <div id="compare-tab" class="tab-content">
                <h2 style="margin-bottom: 20px;">Compare Multiple Models</h2>
                <p style="margin-bottom: 20px; color: #666;">Select multiple models to compare their responses</p>
                <div id="compare-models-grid" class="models-grid"></div>
                
                <div class="chat-area" style="margin-top: 30px;">
                    <textarea id="compare-message" placeholder="Enter your message..."></textarea>
                    <button class="button" onclick="compareModels()">Compare Responses</button>
                    <div id="compare-results" style="margin-top: 20px;"></div>
                </div>
            </div>

            <div id="models-tab" class="tab-content">
                <h2 style="margin-bottom: 20px;">Available Models</h2>
                <div id="all-models-list"></div>
            </div>
        </div>
    </div>

    <script>
        let models = [];
        let selectedModel = null;
        let selectedCompareModels = new Set();

        async function loadModels() {
            try {
                const response = await fetch('/api/models');
                models = await response.json();
                renderModels();
            } catch (error) {
                console.error('Error loading models:', error);
            }
        }

        function renderModels() {
            const grid = document.getElementById('models-grid');
            const compareGrid = document.getElementById('compare-models-grid');
            const allModelsList = document.getElementById('all-models-list');
            
            grid.innerHTML = models.map(m => \`
                <div class="model-card" onclick="selectModel('\${m.id}')">
                    <div class="model-icon">\${m.icon}</div>
                    <div class="model-name">\${m.name}</div>
                    <div class="model-provider">\${m.provider}</div>
                    <div class="model-cost">\${m.cost}</div>
                </div>
            \`).join('');

            compareGrid.innerHTML = models.map(m => \`
                <div class="model-card" onclick="toggleCompareModel('\${m.id}')">
                    <div class="model-icon">\${m.icon}</div>
                    <div class="model-name">\${m.name}</div>
                    <div class="model-provider">\${m.provider}</div>
                    <div class="model-cost">\${m.cost}</div>
                </div>
            \`).join('');

            allModelsList.innerHTML = models.map(m => \`
                <div style="padding: 20px; background: #f5f7fa; border-radius: 10px; margin-bottom: 15px;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
                        <div style="font-size: 2em;">\${m.icon}</div>
                        <div>
                            <div style="font-weight: bold; font-size: 1.2em;">\${m.name}</div>
                            <div style="color: #666;">\${m.provider}</div>
                        </div>
                    </div>
                    <div style="color: #666; margin-bottom: 5px;">Cost: \${m.cost}</div>
                    <div style="color: #666; margin-bottom: 5px;">Context: \${m.context} tokens</div>
                    <div style="color: #666;">Best for: \${m.best_for.join(', ')}</div>
                </div>
            \`).join('');
        }

        function selectModel(modelId) {
            selectedModel = modelId;
            document.querySelectorAll('#models-grid .model-card').forEach(card => {
                card.classList.remove('selected');
            });
            event.currentTarget.classList.add('selected');
        }

        function toggleCompareModel(modelId) {
            if (selectedCompareModels.has(modelId)) {
                selectedCompareModels.delete(modelId);
                event.currentTarget.classList.remove('selected');
            } else {
                selectedCompareModels.add(modelId);
                event.currentTarget.classList.add('selected');
            }
        }

        async function askAI() {
            if (!selectedModel) {
                alert('Please select a model first');
                return;
            }

            const message = document.getElementById('message').value;
            if (!message) {
                alert('Please enter a message');
                return;
            }

            const responseArea = document.getElementById('response-area');
            const responseDiv = document.getElementById('response');
            const statsDiv = document.getElementById('stats');
            
            responseArea.style.display = 'block';
            responseDiv.innerHTML = '<div class="loading">🤖 Thinking...</div>';
            statsDiv.innerHTML = '';

            try {
                const startTime = Date.now();
                const response = await fetch('/api/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ model_id: selectedModel, message })
                });

                const data = await response.json();
                const endTime = Date.now();

                if (data.error) {
                    responseDiv.innerHTML = \`<div style="color: red;">Error: \${data.error}</div>\`;
                } else {
                    responseDiv.textContent = data.response;
                    statsDiv.innerHTML = \`
                        <span>Model: \${data.model}</span>
                        <span>Duration: \${data.duration_ms}ms</span>
                        <span>Time: \${new Date(data.timestamp).toLocaleTimeString()}</span>
                    \`;
                }
            } catch (error) {
                responseDiv.innerHTML = \`<div style="color: red;">Error: \${error.message}</div>\`;
            }
        }

        async function compareModels() {
            if (selectedCompareModels.size === 0) {
                alert('Please select at least one model');
                return;
            }

            const message = document.getElementById('compare-message').value;
            if (!message) {
                alert('Please enter a message');
                return;
            }

            const resultsDiv = document.getElementById('compare-results');
            resultsDiv.innerHTML = '<div class="loading">🤖 Comparing models...</div>';

            try {
                const response = await fetch('/api/compare', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        model_ids: Array.from(selectedCompareModels),
                        message
                    })
                });

                const data = await response.json();
                
                resultsDiv.innerHTML = data.results.map(r => \`
                    <div style="margin-bottom: 20px; padding: 20px; background: #f5f7fa; border-radius: 10px;">
                        <h3 style="margin-bottom: 10px;">\${r.model}</h3>
                        \${r.status === 'success' ? \`
                            <div class="response">\${r.response}</div>
                            <div style="margin-top: 10px; color: #666; font-size: 0.9em;">
                                Duration: \${r.duration_ms}ms
                            </div>
                        \` : \`
                            <div style="color: red;">Error: \${r.error}</div>
                        \`}
                    </div>
                \`).join('');
            } catch (error) {
                resultsDiv.innerHTML = \`<div style="color: red;">Error: \${error.message}</div>\`;
            }
        }

        function switchTab(tab) {
            document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            event.currentTarget.classList.add('active');
            document.getElementById(tab + '-tab').classList.add('active');
        }

        loadModels();
    </script>
</body>
</html>`;
}
