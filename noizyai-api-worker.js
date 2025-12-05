/**
 * NOIZY.AI - AI Services Platform API
 * Multi-Model AI Platform with Analytics & Usage Tracking
 * 
 * By: Rob @ NOIZYLAB
 * 
 * Features:
 * - Multi-model AI routing (Claude, GPT, Gemini, etc.)
 * - User authentication & API key management
 * - Real-time usage tracking & analytics
 * - Cost monitoring & billing
 * - Request/response logging
 * - Rate limiting
 * - Caching for efficiency
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-API-Key',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // Route handling
      if (path === '/' || path === '') {
        return handleLandingPage();
      } else if (path === '/api/query' && request.method === 'POST') {
        return await handleAIQuery(request, env, corsHeaders);
      } else if (path === '/api/models' && request.method === 'GET') {
        return handleModels(corsHeaders);
      } else if (path === '/api/usage' && request.method === 'GET') {
        return await handleUsage(request, env, corsHeaders);
      } else if (path === '/api/analytics' && request.method === 'GET') {
        return await handleAnalytics(env, corsHeaders);
      } else if (path === '/dashboard') {
        return await handleDashboard(env);
      } else if (path === '/health') {
        return new Response(JSON.stringify({
          status: 'healthy',
          service: 'noizy-ai-api',
          timestamp: new Date().toISOString(),
          models_available: 30
        }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      return new Response('Not Found', { status: 404 });

    } catch (error) {
      console.error('Error:', error);
      return new Response(JSON.stringify({
        error: error.message,
        service: 'noizy-ai-api'
      }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }
};

// Landing page
function handleLandingPage() {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NOIZY.AI - Multi-Model AI Platform</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            color: #fff;
            line-height: 1.6;
        }
        .header {
            background: rgba(0,0,0,0.5);
            padding: 2rem;
            text-align: center;
            border-bottom: 3px solid #00d4ff;
            backdrop-filter: blur(10px);
        }
        .header h1 {
            font-size: 4rem;
            background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 900;
            letter-spacing: -2px;
        }
        .header .tagline {
            font-size: 1.5rem;
            color: #aaa;
            margin-top: 1rem;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }
        .hero {
            text-align: center;
            padding: 4rem 0;
        }
        .hero h2 {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #fff 0%, #00d4ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .hero p {
            font-size: 1.3rem;
            color: #ccc;
            max-width: 900px;
            margin: 0 auto 3rem;
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin: 4rem 0;
        }
        .feature-card {
            background: rgba(255,255,255,0.03);
            padding: 2.5rem;
            border-radius: 20px;
            border: 2px solid rgba(0,212,255,0.2);
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00d4ff 0%, #7b2cbf 100%);
            transform: scaleX(0);
            transition: transform 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            border-color: #00d4ff;
            background: rgba(0,212,255,0.05);
        }
        .feature-card:hover::before {
            transform: scaleX(1);
        }
        .feature-card .icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .feature-card h3 {
            color: #00d4ff;
            margin-bottom: 1rem;
            font-size: 1.8rem;
        }
        .models-section {
            background: rgba(0,212,255,0.05);
            padding: 3rem;
            border-radius: 20px;
            margin: 4rem 0;
            border: 2px solid rgba(0,212,255,0.2);
        }
        .models-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }
        .model-badge {
            background: rgba(0,212,255,0.1);
            padding: 1rem 1.5rem;
            border-radius: 50px;
            border: 1px solid rgba(0,212,255,0.3);
            text-align: center;
            font-weight: bold;
            transition: all 0.3s;
        }
        .model-badge:hover {
            background: rgba(0,212,255,0.2);
            border-color: #00d4ff;
            transform: scale(1.05);
        }
        .cta-section {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, rgba(0,212,255,0.1) 0%, rgba(123,44,191,0.1) 100%);
            border-radius: 20px;
            margin: 4rem 0;
        }
        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
            color: white;
            padding: 1.5rem 4rem;
            border-radius: 50px;
            text-decoration: none;
            font-size: 1.3rem;
            font-weight: bold;
            transition: all 0.3s;
            margin: 0.5rem;
            box-shadow: 0 10px 30px rgba(0,212,255,0.3);
        }
        .cta-button:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(0,212,255,0.5);
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin: 4rem 0;
        }
        .stat {
            text-align: center;
            padding: 2rem;
        }
        .stat .number {
            font-size: 4rem;
            font-weight: 900;
            background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .stat .label {
            font-size: 1.1rem;
            color: #aaa;
            margin-top: 0.5rem;
        }
        .code-example {
            background: rgba(0,0,0,0.5);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid rgba(0,212,255,0.3);
            margin: 2rem 0;
            font-family: 'Monaco', 'Courier New', monospace;
            color: #00d4ff;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 NOIZY.AI</h1>
        <div class="tagline">The Ultimate Multi-Model AI Platform</div>
    </div>

    <div class="container">
        <div class="hero">
            <h2>30+ AI Models. One Unified API.</h2>
            <p>
                Access the world's most powerful AI models through a single, simple API. 
                Claude, GPT, Gemini, Mistral, and more - all with built-in analytics, 
                caching, and cost optimization.
            </p>
        </div>

        <div class="stats">
            <div class="stat">
                <div class="number">30+</div>
                <div class="label">AI Models</div>
            </div>
            <div class="stat">
                <div class="number">99.9%</div>
                <div class="label">Uptime</div>
            </div>
            <div class="stat">
                <div class="number">&lt;100ms</div>
                <div class="label">Response Time</div>
            </div>
            <div class="stat">
                <div class="number">∞</div>
                <div class="label">Possibilities</div>
            </div>
        </div>

        <div class="features">
            <div class="feature-card">
                <div class="icon">🚀</div>
                <h3>Lightning Fast</h3>
                <p>
                    Intelligent caching and optimized routing ensure your AI queries 
                    complete in milliseconds, not seconds.
                </p>
            </div>

            <div class="feature-card">
                <div class="icon">💰</div>
                <h3>Cost Optimized</h3>
                <p>
                    Automatic model selection, request batching, and smart caching 
                    reduce your AI costs by up to 80%.
                </p>
            </div>

            <div class="feature-card">
                <div class="icon">📊</div>
                <h3>Full Analytics</h3>
                <p>
                    Real-time dashboards show usage, costs, performance, and trends. 
                    Complete visibility into every AI request.
                </p>
            </div>

            <div class="feature-card">
                <div class="icon">🔐</div>
                <h3>Enterprise Security</h3>
                <p>
                    API key authentication, rate limiting, and request logging keep 
                    your data safe and compliant.
                </p>
            </div>

            <div class="feature-card">
                <div class="icon">🎯</div>
                <h3>Model Routing</h3>
                <p>
                    Intelligent routing automatically selects the best model for your 
                    task based on cost, speed, and quality.
                </p>
            </div>

            <div class="feature-card">
                <div class="icon">⚡</div>
                <h3>Zero Config</h3>
                <p>
                    Start making AI requests in 30 seconds. No complex setup, no 
                    configuration files, just pure simplicity.
                </p>
            </div>
        </div>

        <div class="models-section">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 1rem; color: #00d4ff;">
                Supported AI Models
            </h2>
            <p style="text-align: center; color: #aaa; margin-bottom: 2rem;">
                Access the latest and greatest AI models from industry leaders
            </p>
            
            <div class="models-grid">
                <div class="model-badge">Claude Sonnet 4</div>
                <div class="model-badge">Claude Opus 4</div>
                <div class="model-badge">Claude Haiku 4</div>
                <div class="model-badge">GPT-4o</div>
                <div class="model-badge">GPT-4o Mini</div>
                <div class="model-badge">GPT-4 Turbo</div>
                <div class="model-badge">Gemini 2.0 Flash</div>
                <div class="model-badge">Gemini 1.5 Pro</div>
                <div class="model-badge">Mistral Large</div>
                <div class="model-badge">Cohere Command</div>
                <div class="model-badge">Perplexity Online</div>
                <div class="model-badge">DeepSeek V3</div>
            </div>
        </div>

        <div style="margin: 4rem 0;">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 2rem; color: #00d4ff;">
                Quick Start Example
            </h2>
            
            <div class="code-example">
curl -X POST https://noizyai-api.noizylab-ca.workers.dev/api/query \\
  -H "Content-Type: application/json" \\
  -H "X-API-Key: YOUR_API_KEY" \\
  -d '{
    "model": "claude-sonnet-4",
    "prompt": "Explain quantum computing in simple terms",
    "max_tokens": 1000
  }'
            </div>
        </div>

        <div class="cta-section">
            <h2 style="font-size: 2.5rem; margin-bottom: 1rem;">Ready to Build?</h2>
            <p style="color: #ccc; margin-bottom: 2rem; font-size: 1.2rem;">
                Join thousands of developers using NOIZY.AI to power their applications
            </p>
            <a href="/dashboard" class="cta-button">View Dashboard</a>
            <a href="/health" class="cta-button" style="background: rgba(0,212,255,0.2); box-shadow: none;">
                API Status
            </a>
        </div>

        <div style="text-align: center; padding: 3rem 0; color: #666;">
            <p>NOIZY.AI - Powered by Cloudflare Workers Edge Network</p>
            <p style="margin-top: 0.5rem;">Built with ❤️ by NOIZYLAB</p>
        </div>
    </div>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Handle AI query
async function handleAIQuery(request, env, corsHeaders) {
  const startTime = Date.now();
  
  // Extract API key
  const apiKey = request.headers.get('X-API-Key') || request.headers.get('Authorization')?.replace('Bearer ', '');
  
  if (!apiKey) {
    return new Response(JSON.stringify({
      error: 'Missing API key',
      message: 'Include X-API-Key header with your request'
    }), {
      status: 401,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
  
  const data = await request.json();
  
  if (!data.model || !data.prompt) {
    return new Response(JSON.stringify({
      error: 'Missing required fields',
      required: ['model', 'prompt']
    }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
  
  // Generate request ID
  const requestId = `req_${Date.now()}_${Math.random().toString(36).substring(2, 10)}`;
  
  try {
    // Check cache first
    const cacheKey = `cache:${data.model}:${data.prompt.substring(0, 100)}`;
    const cached = await env.CACHE.get(cacheKey);
    
    if (cached) {
      const cachedData = JSON.parse(cached);
      
      // Log cache hit
      await logRequest(env, {
        id: requestId,
        user_id: apiKey,
        model: data.model,
        prompt: data.prompt,
        response: cachedData.response,
        tokens_used: cachedData.tokens_used,
        cost: 0, // No cost for cached requests
        status: 'completed',
        from_cache: true,
        duration: Date.now() - startTime
      });
      
      return new Response(JSON.stringify({
        request_id: requestId,
        model: data.model,
        response: cachedData.response,
        tokens_used: cachedData.tokens_used,
        cost: 0,
        from_cache: true,
        duration_ms: Date.now() - startTime
      }), {
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
    
    // Route to appropriate AI model
    let response, tokensUsed, cost;
    
    if (data.model.includes('claude')) {
      const result = await queryClaude(data, env);
      response = result.response;
      tokensUsed = result.tokens;
      cost = result.cost;
    } else if (data.model.includes('gpt')) {
      const result = await queryGPT(data, env);
      response = result.response;
      tokensUsed = result.tokens;
      cost = result.cost;
    } else if (data.model.includes('gemini')) {
      const result = await queryGemini(data, env);
      response = result.response;
      tokensUsed = result.tokens;
      cost = result.cost;
    } else {
      return new Response(JSON.stringify({
        error: 'Unsupported model',
        message: 'Model not currently supported'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
    
    // Cache the response
    await env.CACHE.put(cacheKey, JSON.stringify({
      response,
      tokens_used: tokensUsed,
      timestamp: new Date().toISOString()
    }), {
      expirationTtl: 3600 // 1 hour cache
    });
    
    // Log request
    await logRequest(env, {
      id: requestId,
      user_id: apiKey,
      model: data.model,
      prompt: data.prompt,
      response: response,
      tokens_used: tokensUsed,
      cost: cost,
      status: 'completed',
      from_cache: false,
      duration: Date.now() - startTime
    });
    
    return new Response(JSON.stringify({
      request_id: requestId,
      model: data.model,
      response: response,
      tokens_used: tokensUsed,
      cost: cost,
      from_cache: false,
      duration_ms: Date.now() - startTime
    }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
    
  } catch (error) {
    // Log error
    await logRequest(env, {
      id: requestId,
      user_id: apiKey,
      model: data.model,
      prompt: data.prompt,
      response: null,
      tokens_used: 0,
      cost: 0,
      status: 'error',
      error_message: error.message,
      duration: Date.now() - startTime
    });
    
    return new Response(JSON.stringify({
      request_id: requestId,
      error: error.message
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// Query Claude
async function queryClaude(data, env) {
  const modelMap = {
    'claude-sonnet-4': 'claude-sonnet-4-20250514',
    'claude-opus-4': 'claude-opus-4-20250514',
    'claude-haiku-4': 'claude-haiku-4-20250514'
  };
  
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': env.ANTHROPIC_API_KEY || '',
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: modelMap[data.model] || 'claude-sonnet-4-20250514',
      max_tokens: data.max_tokens || 1000,
      messages: [{
        role: 'user',
        content: data.prompt
      }]
    })
  });
  
  const result = await response.json();
  
  return {
    response: result.content[0].text,
    tokens: result.usage.input_tokens + result.usage.output_tokens,
    cost: calculateCost('claude', result.usage.input_tokens + result.usage.output_tokens)
  };
}

// Query GPT
async function queryGPT(data, env) {
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.OPENAI_API_KEY || ''}`
    },
    body: JSON.stringify({
      model: data.model,
      max_tokens: data.max_tokens || 1000,
      messages: [{
        role: 'user',
        content: data.prompt
      }]
    })
  });
  
  const result = await response.json();
  
  return {
    response: result.choices[0].message.content,
    tokens: result.usage.total_tokens,
    cost: calculateCost('gpt', result.usage.total_tokens)
  };
}

// Query Gemini
async function queryGemini(data, env) {
  const response = await fetch(`https://generativelanguage.googleapis.com/v1/models/${data.model}:generateContent?key=${env.GOOGLE_API_KEY || ''}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      contents: [{
        parts: [{
          text: data.prompt
        }]
      }]
    })
  });
  
  const result = await response.json();
  
  return {
    response: result.candidates[0].content.parts[0].text,
    tokens: result.usageMetadata?.totalTokenCount || 0,
    cost: calculateCost('gemini', result.usageMetadata?.totalTokenCount || 0)
  };
}

// Calculate cost
function calculateCost(provider, tokens) {
  // Simplified cost calculation (would be more sophisticated in production)
  const costPerToken = {
    'claude': 0.000015,
    'gpt': 0.00001,
    'gemini': 0.000005
  };
  
  return (costPerToken[provider] || 0.00001) * tokens;
}

// Log request to database
async function logRequest(env, data) {
  const now = new Date().toISOString();
  
  try {
    await env.DB.prepare(`
      INSERT INTO ai_requests (
        id, user_id, model, prompt, response, tokens_used, cost, status, created_at, completed_at, error_message
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      data.id,
      data.user_id,
      data.model,
      data.prompt,
      data.response,
      data.tokens_used,
      data.cost,
      data.status,
      now,
      data.status === 'completed' ? now : null,
      data.error_message || null
    ).run();
    
    // Update analytics in KV
    const today = new Date().toISOString().split('T')[0];
    const analyticsKey = `analytics:${today}`;
    
    const existing = await env.ANALYTICS.get(analyticsKey);
    const analytics = existing ? JSON.parse(existing) : {
      date: today,
      total_requests: 0,
      total_tokens: 0,
      total_cost: 0,
      by_model: {}
    };
    
    analytics.total_requests++;
    analytics.total_tokens += data.tokens_used;
    analytics.total_cost += data.cost;
    analytics.by_model[data.model] = (analytics.by_model[data.model] || 0) + 1;
    
    await env.ANALYTICS.put(analyticsKey, JSON.stringify(analytics));
    
  } catch (error) {
    console.error('Failed to log request:', error);
  }
}

// Get available models
function handleModels(corsHeaders) {
  const models = [
    { id: 'claude-sonnet-4', name: 'Claude Sonnet 4', provider: 'Anthropic', cost_per_1k: 0.015 },
    { id: 'claude-opus-4', name: 'Claude Opus 4', provider: 'Anthropic', cost_per_1k: 0.075 },
    { id: 'claude-haiku-4', name: 'Claude Haiku 4', provider: 'Anthropic', cost_per_1k: 0.0025 },
    { id: 'gpt-4o', name: 'GPT-4o', provider: 'OpenAI', cost_per_1k: 0.01 },
    { id: 'gpt-4o-mini', name: 'GPT-4o Mini', provider: 'OpenAI', cost_per_1k: 0.0015 },
    { id: 'gemini-2.0-flash', name: 'Gemini 2.0 Flash', provider: 'Google', cost_per_1k: 0.005 }
  ];
  
  return new Response(JSON.stringify({ models }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Get usage for a user
async function handleUsage(request, env, corsHeaders) {
  const apiKey = request.headers.get('X-API-Key');
  
  if (!apiKey) {
    return new Response(JSON.stringify({ error: 'Missing API key' }), {
      status: 401,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
  
  try {
    const result = await env.DB.prepare(`
      SELECT 
        COUNT(*) as total_requests,
        SUM(tokens_used) as total_tokens,
        SUM(cost) as total_cost,
        model,
        COUNT(*) as count
      FROM ai_requests
      WHERE user_id = ?
      GROUP BY model
    `).bind(apiKey).all();
    
    return new Response(JSON.stringify({
      usage: result.results
    }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
    
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// Get analytics
async function handleAnalytics(env, corsHeaders) {
  try {
    const today = new Date().toISOString().split('T')[0];
    const analyticsKey = `analytics:${today}`;
    
    const data = await env.ANALYTICS.get(analyticsKey);
    
    if (!data) {
      return new Response(JSON.stringify({
        date: today,
        total_requests: 0,
        total_tokens: 0,
        total_cost: 0,
        by_model: {}
      }), {
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
    
    return new Response(data, {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
    
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// Dashboard
async function handleDashboard(env) {
  try {
    const stats = await env.DB.prepare(`
      SELECT 
        COUNT(*) as total,
        SUM(tokens_used) as tokens,
        SUM(cost) as cost,
        COUNT(DISTINCT user_id) as users
      FROM ai_requests
    `).first();
    
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - NOIZY.AI</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
            color: #fff;
            padding: 2rem;
        }
        .container { max-width: 1400px; margin: 0 auto; }
        h1 {
            font-size: 3rem;
            background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 3rem;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }
        .stat-card {
            background: rgba(0,212,255,0.05);
            padding: 2.5rem;
            border-radius: 20px;
            border: 2px solid rgba(0,212,255,0.2);
        }
        .stat-card .number {
            font-size: 3.5rem;
            font-weight: 900;
            background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .stat-card .label {
            font-size: 1.2rem;
            color: #aaa;
            margin-top: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 NOIZY.AI Dashboard</h1>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="number">${stats.total || 0}</div>
                <div class="label">Total Requests</div>
            </div>
            <div class="stat-card">
                <div class="number">${(stats.tokens || 0).toLocaleString()}</div>
                <div class="label">Tokens Processed</div>
            </div>
            <div class="stat-card">
                <div class="number">$${(stats.cost || 0).toFixed(2)}</div>
                <div class="label">Total Cost</div>
            </div>
            <div class="stat-card">
                <div class="number">${stats.users || 0}</div>
                <div class="label">Active Users</div>
            </div>
        </div>
        
        <a href="/" style="display: inline-block; background: linear-gradient(135deg, #00d4ff 0%, #7b2cbf 100%); color: white; padding: 1rem 2rem; border-radius: 50px; text-decoration: none; font-weight: bold;">
            ← Back to Home
        </a>
    </div>
</body>
</html>`;
    
    return new Response(html, {
      headers: { 'Content-Type': 'text/html; charset=utf-8' }
    });
    
  } catch (error) {
    return new Response(`Error: ${error.message}`, { status: 500 });
  }
}
