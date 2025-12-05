// NOIZYLAB AI GATEWAY - CLOUDFLARE WORKER
// Unified AI API for Gemini & Claude with authentication and monitoring
// Deploy to: your-gateway-name.yourusername.workers.dev

// Ensure environment variables are set in wrangler.toml or Cloudflare dashboard secrets manager
// Required secrets: GEMINI_API_KEY, CLAUDE_API_KEY, INTERNAL_AUTH_TOKEN

/**
 * Call AI API with standardized error handling
 */
async function callAIAPI(url, apiKey, body, provider) {
  const headers = {
    'Content-Type': 'application/json',
  };
  
  // Provider-specific headers
  if (provider === 'claude') {
    headers['x-api-key'] = apiKey;
    headers['anthropic-version'] = '2023-06-01';
  }
  
  let fullUrl = url;
  // Google uses API key as query parameter
  if (provider === 'gemini') {
    fullUrl = `${url}?key=${apiKey}`;
  }
  
  const response = await fetch(fullUrl, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error(`AI API request failed to ${url}: ${errorText}`);
    throw new Error(`Failed to fetch from ${provider}: ${response.status}`);
  }
  
  return response.json();
}

/**
 * Log request for analytics
 */
function logRequest(env, model, prompt, response, duration) {
  const logEntry = {
    timestamp: new Date().toISOString(),
    model: model,
    prompt_length: prompt.length,
    response_length: JSON.stringify(response).length,
    duration_ms: duration,
    status: 'success'
  };
  
  console.log('Request logged:', JSON.stringify(logEntry));
  // Could also send to analytics service or store in KV/Durable Objects
  return logEntry;
}

export default {
  async fetch(request, env, ctx) {
    const startTime = Date.now();
    
    // CORS headers for browser requests
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };
    
    // Handle preflight requests
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: corsHeaders,
      });
    }
    
    // SECURITY CHECK: Only allow POST requests
    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { 
        status: 405,
        headers: corsHeaders 
      });
    }

    // AUTHENTICATION: Use shared secret token for internal systems
    const authHeader = request.headers.get('Authorization');
    if (!authHeader || authHeader !== `Bearer ${env.INTERNAL_AUTH_TOKEN}`) {
      return new Response(JSON.stringify({ 
        error: 'Unauthorized Access',
        message: 'Valid authorization token required'
      }), { 
        status: 401,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }

    try {
      const { model_choice, prompt, max_tokens, temperature } = await request.json();
      
      // Validate input
      if (!prompt || !model_choice) {
        return new Response(JSON.stringify({
          error: 'Invalid request',
          message: 'Both model_choice and prompt are required'
        }), {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }
      
      let apiResponse;

      // ROUTING: Determine which AI model to use
      if (model_choice === 'gemini') {
        const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent';
        const body = {
          contents: [{ 
            role: "user", 
            parts: [{ text: prompt }] 
          }],
          generationConfig: {
            temperature: temperature || 0.7,
            maxOutputTokens: max_tokens || 2048,
          }
        };
        
        const rawResponse = await callAIAPI(url, env.GEMINI_API_KEY, body, 'gemini');
        
        // Standardize output for consistency
        apiResponse = { 
          model: 'gemini-pro',
          result: rawResponse.candidates[0].content.parts[0].text,
          usage: rawResponse.usageMetadata || {}
        };

      } else if (model_choice === 'claude') {
        const url = 'https://api.anthropic.com/v1/messages';
        const body = {
          model: 'claude-3-5-sonnet-20241022', // Latest Claude model
          max_tokens: max_tokens || 2048,
          temperature: temperature || 0.7,
          messages: [{ role: 'user', content: prompt }],
        };
        
        const rawResponse = await callAIAPI(url, env.CLAUDE_API_KEY, body, 'claude');
        
        // Standardize output for consistency
        apiResponse = { 
          model: 'claude-3-5-sonnet',
          result: rawResponse.content[0].text,
          usage: rawResponse.usage || {}
        };

      } else {
        return new Response(JSON.stringify({
          error: 'Invalid model specified',
          message: 'Choose "gemini" or "claude"',
          available_models: ['gemini', 'claude']
        }), { 
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }
      
      // Calculate request duration
      const duration = Date.now() - startTime;
      
      // Log request for analytics
      logRequest(env, model_choice, prompt, apiResponse, duration);
      
      // Add metadata to response
      apiResponse.metadata = {
        duration_ms: duration,
        timestamp: new Date().toISOString(),
        gateway: 'noizylab-ai-gateway'
      };

      return new Response(JSON.stringify(apiResponse), {
        headers: { 
          ...corsHeaders,
          'Content-Type': 'application/json' 
        },
      });

    } catch (error) {
      const duration = Date.now() - startTime;
      
      console.error('Gateway error:', error.message);
      
      return new Response(JSON.stringify({
        error: 'Gateway error',
        message: error.message,
        duration_ms: duration
      }), { 
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }
  },
};

