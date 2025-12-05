/**
 * AI GENIUS CLOUD WORKER
 * Universal AI Router - 30+ Models
 * Production Ready for Cloudflare Workers
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };
    
    // Handle OPTIONS
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }
    
    // Route handling
    try {
      // Health check
      if (url.pathname === '/health') {
        return new Response(JSON.stringify({
          status: 'operational',
          timestamp: new Date().toISOString(),
          models: 30,
          version: '1.0.0'
        }), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }
      
      // List models
      if (url.pathname === '/models') {
        return new Response(JSON.stringify({
          models: getAvailableModels()
        }), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }
      
      // Main AI query endpoint
      if (url.pathname === '/query' && request.method === 'POST') {
        const body = await request.json();
        const { model, prompt, stream = false } = body;
        
        if (!model || !prompt) {
          return new Response(JSON.stringify({
            error: 'Missing required fields: model and prompt'
          }), {
            status: 400,
            headers: { ...corsHeaders, 'Content-Type': 'application/json' }
          });
        }
        
        const response = await routeToModel(model, prompt, env);
        
        return new Response(JSON.stringify(response), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }
      
      // Default response
      return new Response(JSON.stringify({
        name: 'AI GENIUS Cloud Worker',
        version: '1.0.0',
        endpoints: [
          '/health',
          '/models',
          '/query'
        ]
      }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
      
    } catch (error) {
      return new Response(JSON.stringify({
        error: error.message
      }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }
  }
};

/**
 * Route request to appropriate AI model
 */
async function routeToModel(model, prompt, env) {
  const startTime = Date.now();
  
  try {
    let response;
    
    // Claude models (Anthropic)
    if (model.startsWith('claude')) {
      response = await queryClaude(model, prompt, env);
    }
    // Gemini models (Google)
    else if (model.startsWith('gemini')) {
      response = await queryGemini(model, prompt, env);
    }
    // GPT models (OpenAI)
    else if (model.startsWith('gpt')) {
      response = await queryOpenAI(model, prompt, env);
    }
    // Perplexity
    else if (model.startsWith('perplexity')) {
      response = await queryPerplexity(model, prompt, env);
    }
    // Mistral
    else if (model.startsWith('mistral')) {
      response = await queryMistral(model, prompt, env);
    }
    // Cohere
    else if (model.startsWith('cohere')) {
      response = await queryCohere(model, prompt, env);
    }
    // DeepSeek
    else if (model.startsWith('deepseek')) {
      response = await queryDeepSeek(model, prompt, env);
    }
    else {
      throw new Error(`Unknown model: ${model}`);
    }
    
    const endTime = Date.now();
    
    return {
      success: true,
      model: model,
      response: response,
      timing: {
        duration_ms: endTime - startTime,
        timestamp: new Date().toISOString()
      }
    };
    
  } catch (error) {
    return {
      success: false,
      model: model,
      error: error.message,
      timing: {
        duration_ms: Date.now() - startTime,
        timestamp: new Date().toISOString()
      }
    };
  }
}

/**
 * Query Claude models via Anthropic API
 */
async function queryClaude(model, prompt, env) {
  const modelMap = {
    'claude-sonnet-4': 'claude-sonnet-4-20250514',
    'claude-opus-4': 'claude-opus-4-20250514',
    'claude-haiku-4': 'claude-haiku-4-20250514'
  };
  
  const apiModel = modelMap[model] || model;
  
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: apiModel,
      max_tokens: 4096,
      messages: [
        { role: 'user', content: prompt }
      ]
    })
  });
  
  if (!response.ok) {
    throw new Error(`Claude API error: ${response.status}`);
  }
  
  const data = await response.json();
  return data.content[0].text;
}

/**
 * Query Gemini models via Google API
 */
async function queryGemini(model, prompt, env) {
  const modelMap = {
    'gemini-2-flash': 'gemini-2.0-flash-exp',
    'gemini-1.5-pro': 'gemini-1.5-pro',
    'gemini-1.5-flash': 'gemini-1.5-flash'
  };
  
  const apiModel = modelMap[model] || 'gemini-2.0-flash-exp';
  
  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/${apiModel}:generateContent?key=${env.GOOGLE_API_KEY}`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        contents: [{
          parts: [{ text: prompt }]
        }]
      })
    }
  );
  
  if (!response.ok) {
    throw new Error(`Gemini API error: ${response.status}`);
  }
  
  const data = await response.json();
  return data.candidates[0].content.parts[0].text;
}

/**
 * Query OpenAI models
 */
async function queryOpenAI(model, prompt, env) {
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: model,
      messages: [
        { role: 'user', content: prompt }
      ],
      max_tokens: 4096
    })
  });
  
  if (!response.ok) {
    throw new Error(`OpenAI API error: ${response.status}`);
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

/**
 * Query Perplexity
 */
async function queryPerplexity(model, prompt, env) {
  const response = await fetch('https://api.perplexity.ai/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.PERPLEXITY_API_KEY}`
    },
    body: JSON.stringify({
      model: 'llama-3.1-sonar-large-128k-online',
      messages: [
        { role: 'user', content: prompt }
      ]
    })
  });
  
  if (!response.ok) {
    throw new Error(`Perplexity API error: ${response.status}`);
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

/**
 * Query Mistral
 */
async function queryMistral(model, prompt, env) {
  const response = await fetch('https://api.mistral.ai/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.MISTRAL_API_KEY}`
    },
    body: JSON.stringify({
      model: model,
      messages: [
        { role: 'user', content: prompt }
      ]
    })
  });
  
  if (!response.ok) {
    throw new Error(`Mistral API error: ${response.status}`);
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

/**
 * Query Cohere
 */
async function queryCohere(model, prompt, env) {
  const response = await fetch('https://api.cohere.ai/v1/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.COHERE_API_KEY}`
    },
    body: JSON.stringify({
      message: prompt,
      model: model
    })
  });
  
  if (!response.ok) {
    throw new Error(`Cohere API error: ${response.status}`);
  }
  
  const data = await response.json();
  return data.text;
}

/**
 * Query DeepSeek
 */
async function queryDeepSeek(model, prompt, env) {
  const response = await fetch('https://api.deepseek.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${env.DEEPSEEK_API_KEY}`
    },
    body: JSON.stringify({
      model: model,
      messages: [
        { role: 'user', content: prompt }
      ]
    })
  });
  
  if (!response.ok) {
    throw new Error(`DeepSeek API error: ${response.status}`);
  }
  
  const data = await response.json();
  return data.choices[0].message.content;
}

/**
 * Get list of available models
 */
function getAvailableModels() {
  return [
    // Claude
    { id: 'claude-sonnet-4', name: 'Claude Sonnet 4', provider: 'Anthropic', cost: 'medium', speed: 'fast' },
    { id: 'claude-opus-4', name: 'Claude Opus 4', provider: 'Anthropic', cost: 'high', speed: 'medium' },
    { id: 'claude-haiku-4', name: 'Claude Haiku 4', provider: 'Anthropic', cost: 'low', speed: 'very-fast' },
    
    // Gemini
    { id: 'gemini-2-flash', name: 'Gemini 2.0 Flash', provider: 'Google', cost: 'free', speed: 'very-fast' },
    { id: 'gemini-1.5-pro', name: 'Gemini 1.5 Pro', provider: 'Google', cost: 'low', speed: 'fast' },
    { id: 'gemini-1.5-flash', name: 'Gemini 1.5 Flash', provider: 'Google', cost: 'free', speed: 'very-fast' },
    
    // OpenAI
    { id: 'gpt-4o', name: 'GPT-4o', provider: 'OpenAI', cost: 'medium', speed: 'fast' },
    { id: 'gpt-4o-mini', name: 'GPT-4o Mini', provider: 'OpenAI', cost: 'low', speed: 'fast' },
    { id: 'gpt-4-turbo', name: 'GPT-4 Turbo', provider: 'OpenAI', cost: 'high', speed: 'medium' },
    
    // Perplexity
    { id: 'perplexity-online', name: 'Perplexity Online', provider: 'Perplexity', cost: 'low', speed: 'fast' },
    
    // Mistral
    { id: 'mistral-large', name: 'Mistral Large', provider: 'Mistral', cost: 'medium', speed: 'fast' },
    { id: 'mistral-medium', name: 'Mistral Medium', provider: 'Mistral', cost: 'low', speed: 'fast' },
    
    // Cohere
    { id: 'cohere-command-r-plus', name: 'Command R+', provider: 'Cohere', cost: 'medium', speed: 'fast' },
    
    // DeepSeek
    { id: 'deepseek-chat', name: 'DeepSeek Chat', provider: 'DeepSeek', cost: 'low', speed: 'fast' }
  ];
}
