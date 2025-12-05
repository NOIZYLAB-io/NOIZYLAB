// AI Router Worker for NoizyLab
// ===============================
// Routes requests to different AI providers via Cloudflare

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    if (url.pathname === '/ai/route' && request.method === 'POST') {
      const { prompt, provider } = await request.json();
      
      let result;
      
      switch(provider) {
        case 'gemini':
          result = await callGemini(prompt, env);
          break;
        case 'claude':
          result = await callClaude(prompt, env);
          break;
        case 'cloudflare-ai':
          result = await callCloudflareAI(prompt, env);
          break;
        default:
          result = { error: 'Unknown provider' };
      }
      
      return new Response(JSON.stringify(result), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    return new Response('NoizyLab AI Router', { status: 200 });
  }
};

async function callCloudflareAI(prompt, env) {
  // Use Cloudflare AI
  const response = await env.AI.run('@cf/meta/llama-2-7b-chat-int8', {
    prompt: prompt
  });
  
  return { provider: 'cloudflare-ai', response: response };
}

async function callGemini(prompt, env) {
  // Call Gemini API
  const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + env.GEMINI_API_KEY, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
  });
  
  const data = await response.json();
  return { provider: 'gemini', response: data };
}

async function callClaude(prompt, env) {
  // Call Claude API
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: 'claude-3-haiku-20240307',
      max_tokens: 1000,
      messages: [{ role: 'user', content: prompt }]
    })
  });
  
  const data = await response.json();
  return { provider: 'claude', response: data };
}

