/**
 * ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
 * ║  HEAVEN v4 ULTIMATE — THE COMPLETE NOIZY.AI GALAXY + ANTHROPIC GOLD                                          ║
 * ║                                                                                                               ║
 * ║  PRODUCTS: Portal • NOIZYVOX • CODEMASTER • FISHYBOOKS • NOIZYLAB • LIFELUV • FLOW                           ║
 * ║  INFRA: Workers AI • D1 • KV • R2 • Queues • Vectorize • MCP Server • Cron • Email • Anthropic API           ║
 * ║  NEW: Streaming • Agent SDK • Tool Loop • Batch API • Prompt Caching • Skills                                 ║
 * ║                                                                                                               ║
 * ║  "GORUNFREE — One command, everything done." — Rob Plowman, Dec 2025                                          ║
 * ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
 */

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// CONFIGURATION
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

const CONFIG = {
  VERSION: '4.0.0',
  GALAXY: 'NOIZY.AI',
  ANTHROPIC_VERSION: '2023-06-01',
  DEFAULT_MODEL: 'claude-sonnet-4-5-20250929',
  MODELS: {
    OPUS: 'claude-opus-4-5-20251101',
    SONNET: 'claude-sonnet-4-5-20250929',
    HAIKU: 'claude-haiku-4-5-20251001'
  },
  PRODUCTS: ['portal', 'vox', 'codemaster', 'books', 'lab', 'lifeluv', 'flow', 'ai', 'mcp', 'api', 'agent', 'admin']
};

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// MAIN HANDLER
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const host = url.hostname;
    const path = url.pathname;
    const method = request.method;

    // CORS preflight
    if (method === 'OPTIONS') return corsResponse();

    // Subdomain routing
    const sub = getSubdomain(host, path);

    // Universal health check
    if (path === '/health') return json({ galaxy: CONFIG.GALAXY, service: sub, status: 'live', v: CONFIG.VERSION, ts: Date.now() });

    // Route to handler
    try {
      switch (sub) {
        case 'ai': return handleAI(request, env, url);
        case 'mcp': return handleMCP(request, env, url);
        case 'agent': return handleAgent(request, env, url);
        case 'lifeluv': return handleLifeluv(request, env, url);
        case 'flow': return handleFlow(request, env, url);
        case 'vox': return handleVox(request, env, url);
        case 'codemaster': return handleCodemaster(request, env, url);
        case 'books': return handleBooks(request, env, url);
        case 'lab': return handleLab(request, env, url);
        case 'admin': return handleAdmin(request, env, url);
        case 'api': return handleAPI(request, env, url);
        default: return handlePortal(request, env, url);
      }
    } catch (e) {
      return json({ error: e.message, stack: e.stack }, 500);
    }
  },

  async scheduled(event, env, ctx) {
    const handlers = {
      '0 * * * *': () => cleanExpiredSessions(env),
      '0 0 * * *': () => generateDailyReport(env),
      '0 0 * * 0': () => sendWeeklyDigest(env)
    };
    if (handlers[event.cron]) await handlers[event.cron]();
  },

  async queue(batch, env) {
    for (const msg of batch.messages) {
      await processQueueJob(env, msg.body);
      msg.ack();
    }
  },

  async email(message, env) {
    await handleIncomingEmail(message, env);
  }
};

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// 🤖 ANTHROPIC API INTEGRATION — Direct Claude Access
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

class AnthropicClient {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = 'https://api.anthropic.com/v1';
  }

  async messages(params) {
    const response = await fetch(`${this.baseUrl}/messages`, {
      method: 'POST',
      headers: {
        'x-api-key': this.apiKey,
        'anthropic-version': CONFIG.ANTHROPIC_VERSION,
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        model: params.model || CONFIG.DEFAULT_MODEL,
        max_tokens: params.max_tokens || 1024,
        ...params
      })
    });
    return response.json();
  }

  async messagesStream(params) {
    const response = await fetch(`${this.baseUrl}/messages`, {
      method: 'POST',
      headers: {
        'x-api-key': this.apiKey,
        'anthropic-version': CONFIG.ANTHROPIC_VERSION,
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        model: params.model || CONFIG.DEFAULT_MODEL,
        max_tokens: params.max_tokens || 1024,
        stream: true,
        ...params
      })
    });
    return response;
  }

  async batch(requests) {
    const response = await fetch(`${this.baseUrl}/messages/batches`, {
      method: 'POST',
      headers: {
        'x-api-key': this.apiKey,
        'anthropic-version': CONFIG.ANTHROPIC_VERSION,
        'content-type': 'application/json'
      },
      body: JSON.stringify({ requests })
    });
    return response.json();
  }

  async countTokens(params) {
    const response = await fetch(`${this.baseUrl}/messages/count_tokens`, {
      method: 'POST',
      headers: {
        'x-api-key': this.apiKey,
        'anthropic-version': CONFIG.ANTHROPIC_VERSION,
        'content-type': 'application/json'
      },
      body: JSON.stringify(params)
    });
    return response.json();
  }
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// 🤖 AI HANDLER — Workers AI + Anthropic API Combined
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

async function handleAI(request, env, url) {
  const path = url.pathname.replace('/ai/', '').replace('/ai', '');
  
  if (request.method === 'GET' && !path) {
    return json({
      service: 'NOIZY.AI Intelligence Layer',
      version: CONFIG.VERSION,
      engines: {
        workers_ai: !!env.AI,
        anthropic: !!env.ANTHROPIC_API_KEY
      },
      endpoints: {
        workers_ai: ['embed', 'transcribe', 'translate', 'summarize', 'sentiment', 'vision', 'image'],
        anthropic: ['chat', 'stream', 'batch', 'tokens'],
        hybrid: ['smart'] // Auto-routes to best engine
      }
    });
  }

  if (request.method !== 'POST') return json({ error: 'POST required' }, 405);

  const body = await request.json().catch(() => ({}));
  const endpoint = path.split('/')[0];

  // ANTHROPIC ENDPOINTS
  if (['chat', 'stream', 'batch', 'tokens'].includes(endpoint)) {
    if (!env.ANTHROPIC_API_KEY) return json({ error: 'ANTHROPIC_API_KEY not configured' }, 503);
    const anthropic = new AnthropicClient(env.ANTHROPIC_API_KEY);

    switch (endpoint) {
      case 'chat': {
        const result = await anthropic.messages({
          model: body.model,
          max_tokens: body.max_tokens || 1024,
          system: body.system,
          messages: body.messages || [{ role: 'user', content: body.prompt || body.text }],
          tools: body.tools
        });
        return json({ ok: true, ...result });
      }

      case 'stream': {
        const response = await anthropic.messagesStream({
          model: body.model,
          max_tokens: body.max_tokens || 1024,
          system: body.system,
          messages: body.messages || [{ role: 'user', content: body.prompt }]
        });
        // Pass through the SSE stream
        return new Response(response.body, {
          headers: {
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            ...corsHeaders()
          }
        });
      }

      case 'batch': {
        const result = await anthropic.batch(body.requests);
        return json({ ok: true, ...result });
      }

      case 'tokens': {
        const result = await anthropic.countTokens({
          model: body.model || CONFIG.DEFAULT_MODEL,
          messages: body.messages
        });
        return json({ ok: true, ...result });
      }
    }
  }

  // WORKERS AI ENDPOINTS
  if (!env.AI) return json({ error: 'Workers AI not bound' }, 503);

  switch (endpoint) {
    case 'embed': {
      const text = Array.isArray(body.text) ? body.text : [body.text];
      const r = await env.AI.run('@cf/baai/bge-base-en-v1.5', { text });
      // Optionally store in Vectorize
      if (body.store && env.VECTOR && body.ids) {
        const vectors = body.ids.map((id, i) => ({ id, values: r.data[i], metadata: body.metadata?.[i] || {} }));
        await env.VECTOR.insert(vectors);
      }
      return json({ ok: true, embeddings: r.data, dims: r.data[0]?.length });
    }

    case 'transcribe': {
      let audio;
      if (body.url) audio = await (await fetch(body.url)).arrayBuffer();
      else if (body.base64) audio = Uint8Array.from(atob(body.base64), c => c.charCodeAt(0)).buffer;
      else return json({ error: 'Provide url or base64' }, 400);
      const r = await env.AI.run('@cf/openai/whisper', { audio: [...new Uint8Array(audio)] });
      return json({ ok: true, text: r.text });
    }

    case 'translate': {
      const r = await env.AI.run('@cf/meta/m2m100-1.2b', {
        text: body.text,
        source_lang: body.from || 'en',
        target_lang: body.to || 'es'
      });
      return json({ ok: true, translated: r.translated_text });
    }

    case 'summarize': {
      const r = await env.AI.run('@cf/facebook/bart-large-cnn', {
        input_text: body.text,
        max_length: body.max_length || 150
      });
      return json({ ok: true, summary: r.summary });
    }

    case 'sentiment': {
      const r = await env.AI.run('@cf/huggingface/distilbert-sst-2-int8', { text: body.text });
      return json({ ok: true, ...r });
    }

    case 'vision': {
      let img;
      if (body.url) img = [...new Uint8Array(await (await fetch(body.url)).arrayBuffer())];
      else if (body.base64) img = [...Uint8Array.from(atob(body.base64), c => c.charCodeAt(0))];
      const r = await env.AI.run('@cf/llava-hf/llava-1.5-7b-hf', {
        image: img,
        prompt: body.prompt || 'Describe this image',
        max_tokens: 512
      });
      return json({ ok: true, description: r.description });
    }

    case 'image': {
      const r = await env.AI.run('@cf/stabilityai/stable-diffusion-xl-base-1.0', { prompt: body.prompt });
      if (body.store && env.BUCKET) {
        const key = `generated/${Date.now()}.png`;
        await env.BUCKET.put(key, r);
        return json({ ok: true, key, url: `/api/files/${key}` });
      }
      return new Response(r, { headers: { 'Content-Type': 'image/png', ...corsHeaders() } });
    }

    case 'smart': {
      // HYBRID: Auto-route to best engine
      const task = body.task || 'chat';
      if (['embed', 'transcribe', 'translate', 'summarize', 'sentiment', 'image'].includes(task)) {
        // Use Workers AI for these
        return handleAI(new Request(url.origin + '/ai/' + task, { method: 'POST', body: JSON.stringify(body) }), env, url);
      } else {
        // Use Anthropic for complex reasoning
        if (!env.ANTHROPIC_API_KEY) return json({ error: 'ANTHROPIC_API_KEY needed for complex tasks' }, 503);
        const anthropic = new AnthropicClient(env.ANTHROPIC_API_KEY);
        const result = await anthropic.messages({ messages: body.messages || [{ role: 'user', content: body.prompt }] });
        return json({ ok: true, engine: 'anthropic', ...result });
      }
    }

    default:
      return json({ error: `Unknown endpoint: ${endpoint}` }, 404);
  }
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// 🤖 AGENT HANDLER — Full Agent SDK Pattern with Tool Loop
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

async function handleAgent(request, env, url) {
  const path = url.pathname.replace('/agent/', '').replace('/agent', '');

  if (request.method === 'GET' && !path) {
    return json({
      service: 'NOIZY.AI Agent SDK',
      version: CONFIG.VERSION,
      capabilities: ['tool_use', 'memory', 'streaming', 'multi_turn'],
      agents: ['assistant', 'coder', 'researcher', 'support']
    });
  }

  if (request.method !== 'POST') return json({ error: 'POST required' }, 405);
  if (!env.ANTHROPIC_API_KEY) return json({ error: 'ANTHROPIC_API_KEY required' }, 503);

  const body = await request.json();
  const agentType = path || 'assistant';

  // Define agent tools
  const AGENT_TOOLS = {
    assistant: [
      { name: 'search_web', description: 'Search the web', input_schema: { type: 'object', properties: { query: { type: 'string' } }, required: ['query'] } },
      { name: 'get_time', description: 'Get current time', input_schema: { type: 'object', properties: {} } },
      { name: 'calculate', description: 'Do math', input_schema: { type: 'object', properties: { expression: { type: 'string' } }, required: ['expression'] } }
    ],
    coder: [
      { name: 'run_code', description: 'Execute code', input_schema: { type: 'object', properties: { language: { type: 'string' }, code: { type: 'string' } }, required: ['code'] } },
      { name: 'search_docs', description: 'Search documentation', input_schema: { type: 'object', properties: { query: { type: 'string' } }, required: ['query'] } }
    ],
    researcher: [
      { name: 'search_papers', description: 'Search academic papers', input_schema: { type: 'object', properties: { query: { type: 'string' } }, required: ['query'] } },
      { name: 'summarize_doc', description: 'Summarize document', input_schema: { type: 'object', properties: { text: { type: 'string' } }, required: ['text'] } }
    ],
    support: [
      { name: 'lookup_customer', description: 'Look up customer', input_schema: { type: 'object', properties: { email: { type: 'string' } }, required: ['email'] } },
      { name: 'create_ticket', description: 'Create support ticket', input_schema: { type: 'object', properties: { title: { type: 'string' }, description: { type: 'string' } }, required: ['title', 'description'] } }
    ]
  };

  const SYSTEM_PROMPTS = {
    assistant: 'You are a helpful AI assistant. Use tools when needed to provide accurate information.',
    coder: 'You are an expert programmer. Help users write, debug, and explain code.',
    researcher: 'You are a research assistant. Find and synthesize information from various sources.',
    support: 'You are a customer support agent for NOIZYLAB. Be helpful and professional.'
  };

  // AGENT LOOP
  const anthropic = new AnthropicClient(env.ANTHROPIC_API_KEY);
  let messages = body.messages || [{ role: 'user', content: body.prompt || body.task }];
  const tools = AGENT_TOOLS[agentType] || AGENT_TOOLS.assistant;
  const maxIterations = body.max_iterations || 10;
  let iteration = 0;
  const trace = [];

  while (iteration < maxIterations) {
    iteration++;

    const response = await anthropic.messages({
      model: body.model || CONFIG.MODELS.SONNET,
      max_tokens: body.max_tokens || 4096,
      system: SYSTEM_PROMPTS[agentType],
      messages,
      tools
    });

    trace.push({ iteration, response: { stop_reason: response.stop_reason, content_types: response.content?.map(c => c.type) } });

    // Check for tool use
    const toolUses = response.content?.filter(c => c.type === 'tool_use') || [];

    if (toolUses.length === 0) {
      // No more tools, return final response
      const textContent = response.content?.find(c => c.type === 'text');
      return json({
        ok: true,
        agent: agentType,
        iterations: iteration,
        response: textContent?.text || '',
        trace: body.debug ? trace : undefined
      });
    }

    // Execute tools
    messages.push({ role: 'assistant', content: response.content });

    const toolResults = [];
    for (const toolUse of toolUses) {
      const result = await executeAgentTool(env, toolUse.name, toolUse.input);
      toolResults.push({
        type: 'tool_result',
        tool_use_id: toolUse.id,
        content: typeof result === 'string' ? result : JSON.stringify(result)
      });
      trace.push({ iteration, tool: toolUse.name, input: toolUse.input, result });
    }

    messages.push({ role: 'user', content: toolResults });
  }

  return json({ ok: false, error: 'Max iterations reached', iterations: iteration, trace: body.debug ? trace : undefined });
}

async function executeAgentTool(env, name, input) {
  switch (name) {
    case 'get_time':
      return new Date().toISOString();
    case 'calculate':
      try { return eval(input.expression.replace(/[^0-9+\-*/().]/g, '')); } catch { return 'Error'; }
    case 'search_web':
      return `[Web search for "${input.query}" - implement with actual search API]`;
    case 'run_code':
      return `[Code execution - implement with sandbox]`;
    case 'lookup_customer':
      if (env.DB) {
        const r = await env.DB.prepare('SELECT * FROM repairs WHERE email = ?').bind(input.email).first();
        return r || 'Customer not found';
      }
      return 'Database not available';
    case 'create_ticket':
      if (env.DB) {
        await env.DB.prepare('INSERT INTO support_tickets (title, description, status, created_at) VALUES (?, ?, ?, ?)')
          .bind(input.title, input.description, 'new', Date.now()).run();
        return 'Ticket created';
      }
      return 'Database not available';
    default:
      return `Unknown tool: ${name}`;
  }
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// 🔌 MCP SERVER — Enhanced with Full Anthropic Patterns
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

async function handleMCP(request, env, url) {
  const path = url.pathname.replace('/mcp/', '').replace('/mcp', '');

  // SSE endpoint for real-time updates
  if (path === 'sse' || path === 'events') {
    const { readable, writable } = new TransformStream();
    const writer = writable.getWriter();
    const encoder = new TextEncoder();

    writer.write(encoder.encode(`data: ${JSON.stringify({ type: 'connected', server: 'NOIZY.AI MCP v4' })}\n\n`));

    return new Response(readable, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        ...corsHeaders()
      }
    });
  }

  // Manifest (MCP spec compliant)
  if (!path || path === 'manifest' || path === '.well-known/mcp.json') {
    return json({
      name: 'NOIZY.AI Galaxy MCP Server',
      version: CONFIG.VERSION,
      description: 'Complete NOIZY.AI infrastructure control via MCP',
      capabilities: {
        tools: true,
        resources: true,
        prompts: true,
        logging: true
      },
      tools: getMCPTools(),
      resources: [
        { uri: 'noizy://repairs', name: 'Repairs Database', mimeType: 'application/json' },
        { uri: 'noizy://signups', name: 'NOIZYVOX Signups', mimeType: 'application/json' },
        { uri: 'noizy://memory/{user_id}', name: 'LIFELUV Memory', mimeType: 'application/json' },
        { uri: 'noizy://flow/{session_id}', name: 'FLOW Session', mimeType: 'application/json' },
        { uri: 'noizy://files/{path}', name: 'R2 Files', mimeType: 'application/octet-stream' }
      ],
      prompts: [
        { name: 'repair_diagnosis', description: 'Diagnose a tech issue', arguments: [{ name: 'issue', required: true }] },
        { name: 'voice_coaching', description: 'NOIZYVOX artist guidance', arguments: [{ name: 'question', required: true }] },
        { name: 'code_review', description: 'Review code', arguments: [{ name: 'code', required: true }] }
      ]
    });
  }

  // Tool execution
  if ((path === 'tools/call' || path === 'call') && request.method === 'POST') {
    const { name, arguments: args } = await request.json();
    const result = await executeMCPTool(env, name, args || {});
    return json(result);
  }

  // Tool list
  if (path === 'tools/list') {
    return json({ tools: getMCPTools() });
  }

  // Resource fetch
  if (path.startsWith('resources/')) {
    const uri = decodeURIComponent(path.replace('resources/', ''));
    return json(await fetchMCPResource(env, uri));
  }

  // Prompt get
  if (path.startsWith('prompts/')) {
    const promptName = path.replace('prompts/', '');
    return json(getMCPPrompt(promptName));
  }

  return json({ error: 'Invalid MCP endpoint' }, 400);
}

function getMCPTools() {
  return [
    // AI Tools
    { name: 'ai_chat', description: 'Chat with Claude via Anthropic API', inputSchema: { type: 'object', properties: { prompt: { type: 'string' }, model: { type: 'string' }, system: { type: 'string' } }, required: ['prompt'] } },
    { name: 'ai_stream', description: 'Stream chat response', inputSchema: { type: 'object', properties: { prompt: { type: 'string' } }, required: ['prompt'] } },
    { name: 'ai_embed', description: 'Generate embeddings', inputSchema: { type: 'object', properties: { text: { type: 'string' } }, required: ['text'] } },
    { name: 'ai_transcribe', description: 'Transcribe audio', inputSchema: { type: 'object', properties: { url: { type: 'string' } }, required: ['url'] } },
    { name: 'ai_image', description: 'Generate image', inputSchema: { type: 'object', properties: { prompt: { type: 'string' } }, required: ['prompt'] } },

    // Database Tools
    { name: 'db_query', description: 'Run SQL query', inputSchema: { type: 'object', properties: { sql: { type: 'string' }, params: { type: 'array' } }, required: ['sql'] } },
    { name: 'db_repairs_list', description: 'List repairs', inputSchema: { type: 'object', properties: { status: { type: 'string' }, limit: { type: 'number' } } } },
    { name: 'db_repairs_create', description: 'Create repair', inputSchema: { type: 'object', properties: { name: { type: 'string' }, email: { type: 'string' }, issue: { type: 'string' } }, required: ['name', 'email', 'issue'] } },
    { name: 'db_repairs_update', description: 'Update repair', inputSchema: { type: 'object', properties: { id: { type: 'number' }, status: { type: 'string' }, notes: { type: 'string' } }, required: ['id'] } },

    // KV Tools
    { name: 'kv_get', description: 'Get KV value', inputSchema: { type: 'object', properties: { key: { type: 'string' } }, required: ['key'] } },
    { name: 'kv_put', description: 'Set KV value', inputSchema: { type: 'object', properties: { key: { type: 'string' }, value: { type: 'string' }, ttl: { type: 'number' } }, required: ['key', 'value'] } },
    { name: 'kv_delete', description: 'Delete KV key', inputSchema: { type: 'object', properties: { key: { type: 'string' } }, required: ['key'] } },
    { name: 'kv_list', description: 'List KV keys', inputSchema: { type: 'object', properties: { prefix: { type: 'string' } } } },

    // R2 Tools
    { name: 'r2_list', description: 'List R2 files', inputSchema: { type: 'object', properties: { prefix: { type: 'string' } } } },
    { name: 'r2_get', description: 'Get R2 file', inputSchema: { type: 'object', properties: { key: { type: 'string' } }, required: ['key'] } },
    { name: 'r2_put', description: 'Upload to R2', inputSchema: { type: 'object', properties: { key: { type: 'string' }, content: { type: 'string' }, contentType: { type: 'string' } }, required: ['key', 'content'] } },
    { name: 'r2_delete', description: 'Delete R2 file', inputSchema: { type: 'object', properties: { key: { type: 'string' } }, required: ['key'] } },

    // Queue Tools
    { name: 'queue_send', description: 'Send to queue', inputSchema: { type: 'object', properties: { type: { type: 'string' }, data: { type: 'object' } }, required: ['type'] } },

    // Vector Tools
    { name: 'vector_search', description: 'Semantic search', inputSchema: { type: 'object', properties: { query: { type: 'string' }, limit: { type: 'number' } }, required: ['query'] } },
    { name: 'vector_upsert', description: 'Add to vector index', inputSchema: { type: 'object', properties: { id: { type: 'string' }, text: { type: 'string' }, metadata: { type: 'object' } }, required: ['id', 'text'] } },

    // LIFELUV Tools
    { name: 'lifeluv_chat', description: 'Chat with LIFELUV', inputSchema: { type: 'object', properties: { user_id: { type: 'string' }, message: { type: 'string' } }, required: ['user_id', 'message'] } },
    { name: 'lifeluv_memory_get', description: 'Get user memory', inputSchema: { type: 'object', properties: { user_id: { type: 'string' } }, required: ['user_id'] } },
    { name: 'lifeluv_memory_set', description: 'Set memory', inputSchema: { type: 'object', properties: { user_id: { type: 'string' }, key: { type: 'string' }, value: { type: 'string' } }, required: ['user_id', 'key', 'value'] } },

    // FLOW Tools
    { name: 'flow_create', description: 'Create FLOW session', inputSchema: { type: 'object', properties: { subject: { type: 'string' }, context: { type: 'object' } }, required: ['subject'] } },
    { name: 'flow_get', description: 'Get FLOW session', inputSchema: { type: 'object', properties: { session_id: { type: 'string' } }, required: ['session_id'] } },
    { name: 'flow_message', description: 'Add message to FLOW', inputSchema: { type: 'object', properties: { session_id: { type: 'string' }, content: { type: 'string' }, role: { type: 'string' } }, required: ['session_id', 'content'] } },
    { name: 'flow_distribute', description: 'Distribute output', inputSchema: { type: 'object', properties: { session_id: { type: 'string' }, content: { type: 'string' }, target: { type: 'string' } }, required: ['session_id', 'content', 'target'] } },

    // System Tools
    { name: 'system_status', description: 'Full system status', inputSchema: { type: 'object', properties: {} } },
    { name: 'system_metrics', description: 'Get metrics', inputSchema: { type: 'object', properties: { period: { type: 'string' } } } }
  ];
}

async function executeMCPTool(env, name, args) {
  try {
    // AI TOOLS
    if (name === 'ai_chat') {
      if (!env.ANTHROPIC_API_KEY) return { error: 'ANTHROPIC_API_KEY not set' };
      const client = new AnthropicClient(env.ANTHROPIC_API_KEY);
      const result = await client.messages({
        model: args.model,
        system: args.system,
        messages: [{ role: 'user', content: args.prompt }]
      });
      return { ok: true, response: result.content?.[0]?.text };
    }

    if (name === 'ai_embed') {
      if (!env.AI) return { error: 'AI not bound' };
      const r = await env.AI.run('@cf/baai/bge-base-en-v1.5', { text: [args.text] });
      return { ok: true, embedding: r.data[0], dims: r.data[0]?.length };
    }

    if (name === 'ai_transcribe') {
      if (!env.AI) return { error: 'AI not bound' };
      const audio = await (await fetch(args.url)).arrayBuffer();
      const r = await env.AI.run('@cf/openai/whisper', { audio: [...new Uint8Array(audio)] });
      return { ok: true, text: r.text };
    }

    if (name === 'ai_image') {
      if (!env.AI) return { error: 'AI not bound' };
      const r = await env.AI.run('@cf/stabilityai/stable-diffusion-xl-base-1.0', { prompt: args.prompt });
      if (env.BUCKET) {
        const key = `generated/${Date.now()}.png`;
        await env.BUCKET.put(key, r);
        return { ok: true, key };
      }
      return { ok: true, size: r.byteLength };
    }

    // DATABASE TOOLS
    if (name === 'db_query') {
      if (!env.DB) return { error: 'DB not bound' };
      const stmt = env.DB.prepare(args.sql);
      if (args.params?.length) stmt.bind(...args.params);
      const r = await stmt.all();
      return { ok: true, results: r.results, meta: r.meta };
    }

    if (name === 'db_repairs_list') {
      if (!env.DB) return { error: 'DB not bound' };
      let sql = 'SELECT * FROM repairs';
      if (args.status) sql += ` WHERE status = '${args.status}'`;
      sql += ` ORDER BY created_at DESC LIMIT ${args.limit || 100}`;
      const r = await env.DB.prepare(sql).all();
      return { ok: true, repairs: r.results };
    }

    if (name === 'db_repairs_create') {
      if (!env.DB) return { error: 'DB not bound' };
      const r = await env.DB.prepare(
        'INSERT INTO repairs (name, email, phone, device, issue, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)'
      ).bind(args.name, args.email, args.phone || '', args.device || '', args.issue, 'pending', Date.now()).run();
      return { ok: true, id: r.meta.last_row_id };
    }

    if (name === 'db_repairs_update') {
      if (!env.DB) return { error: 'DB not bound' };
      const sets = [];
      const vals = [];
      if (args.status) { sets.push('status = ?'); vals.push(args.status); }
      if (args.notes) { sets.push('notes = ?'); vals.push(args.notes); }
      sets.push('updated_at = ?'); vals.push(Date.now());
      vals.push(args.id);
      await env.DB.prepare(`UPDATE repairs SET ${sets.join(', ')} WHERE id = ?`).bind(...vals).run();
      return { ok: true };
    }

    // KV TOOLS
    if (name === 'kv_get') {
      if (!env.KV) return { error: 'KV not bound' };
      const v = await env.KV.get(args.key);
      return { ok: true, key: args.key, value: v };
    }

    if (name === 'kv_put') {
      if (!env.KV) return { error: 'KV not bound' };
      await env.KV.put(args.key, args.value, args.ttl ? { expirationTtl: args.ttl } : {});
      return { ok: true };
    }

    if (name === 'kv_delete') {
      if (!env.KV) return { error: 'KV not bound' };
      await env.KV.delete(args.key);
      return { ok: true };
    }

    if (name === 'kv_list') {
      if (!env.KV) return { error: 'KV not bound' };
      const r = await env.KV.list({ prefix: args.prefix || '', limit: 100 });
      return { ok: true, keys: r.keys.map(k => k.name) };
    }

    // R2 TOOLS
    if (name === 'r2_list') {
      if (!env.BUCKET) return { error: 'R2 not bound' };
      const r = await env.BUCKET.list({ prefix: args.prefix || '', limit: 100 });
      return { ok: true, files: r.objects.map(o => ({ key: o.key, size: o.size })) };
    }

    if (name === 'r2_get') {
      if (!env.BUCKET) return { error: 'R2 not bound' };
      const o = await env.BUCKET.get(args.key);
      if (!o) return { error: 'Not found' };
      const text = await o.text();
      return { ok: true, content: text.slice(0, 10000), size: o.size };
    }

    if (name === 'r2_put') {
      if (!env.BUCKET) return { error: 'R2 not bound' };
      await env.BUCKET.put(args.key, args.content, { httpMetadata: { contentType: args.contentType || 'text/plain' } });
      return { ok: true, key: args.key };
    }

    if (name === 'r2_delete') {
      if (!env.BUCKET) return { error: 'R2 not bound' };
      await env.BUCKET.delete(args.key);
      return { ok: true };
    }

    // QUEUE TOOLS
    if (name === 'queue_send') {
      if (!env.QUEUE) return { error: 'Queue not bound' };
      await env.QUEUE.send({ type: args.type, data: args.data || {}, ts: Date.now() });
      return { ok: true };
    }

    // VECTOR TOOLS
    if (name === 'vector_search') {
      if (!env.AI || !env.VECTOR) return { error: 'AI or VECTOR not bound' };
      const embed = await env.AI.run('@cf/baai/bge-base-en-v1.5', { text: [args.query] });
      const results = await env.VECTOR.query(embed.data[0], { topK: args.limit || 10 });
      return { ok: true, results: results.matches };
    }

    if (name === 'vector_upsert') {
      if (!env.AI || !env.VECTOR) return { error: 'AI or VECTOR not bound' };
      const embed = await env.AI.run('@cf/baai/bge-base-en-v1.5', { text: [args.text] });
      await env.VECTOR.insert([{ id: args.id, values: embed.data[0], metadata: args.metadata || {} }]);
      return { ok: true };
    }

    // LIFELUV TOOLS
    if (name === 'lifeluv_chat') {
      // Get memory context
      let context = '';
      if (env.DB_MEMORY) {
        const mem = await env.DB_MEMORY.prepare('SELECT key, value FROM lifeluv_memory WHERE user_id = ? LIMIT 20').bind(args.user_id).all();
        context = mem.results.map(r => `${r.key}: ${r.value}`).join('\n');
      }

      // Use Anthropic if available, else Workers AI
      if (env.ANTHROPIC_API_KEY) {
        const client = new AnthropicClient(env.ANTHROPIC_API_KEY);
        const result = await client.messages({
          model: CONFIG.MODELS.HAIKU, // Use Haiku for cost efficiency
          system: `You are LIFELUV, a warm AI companion. User context:\n${context}\n\nBe helpful and remember details.`,
          messages: [{ role: 'user', content: args.message }]
        });
        const response = result.content?.[0]?.text || '';

        // Log conversation
        if (env.DB_MEMORY) {
          await env.DB_MEMORY.prepare('INSERT INTO lifeluv_conversations (user_id, role, content, created_at) VALUES (?, ?, ?, ?)')
            .bind(args.user_id, 'user', args.message, Date.now()).run();
          await env.DB_MEMORY.prepare('INSERT INTO lifeluv_conversations (user_id, role, content, created_at) VALUES (?, ?, ?, ?)')
            .bind(args.user_id, 'assistant', response, Date.now()).run();
        }

        return { ok: true, response };
      } else if (env.AI) {
        const r = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
          messages: [
            { role: 'system', content: `You are LIFELUV. Context: ${context}` },
            { role: 'user', content: args.message }
          ]
        });
        return { ok: true, response: r.response };
      }
      return { error: 'No AI available' };
    }

    if (name === 'lifeluv_memory_get') {
      if (!env.DB_MEMORY) return { error: 'DB_MEMORY not bound' };
      const r = await env.DB_MEMORY.prepare('SELECT key, value FROM lifeluv_memory WHERE user_id = ?').bind(args.user_id).all();
      const memory = {};
      r.results.forEach(row => { memory[row.key] = row.value; });
      return { ok: true, memory };
    }

    if (name === 'lifeluv_memory_set') {
      if (!env.DB_MEMORY) return { error: 'DB_MEMORY not bound' };
      await env.DB_MEMORY.prepare('INSERT OR REPLACE INTO lifeluv_memory (user_id, key, value, updated_at) VALUES (?, ?, ?, ?)')
        .bind(args.user_id, args.key, args.value, Date.now()).run();
      return { ok: true };
    }

    // FLOW TOOLS
    if (name === 'flow_create') {
      if (!env.KV) return { error: 'KV not bound' };
      const id = `flow_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
      const session = { id, subject: args.subject, context: args.context || {}, messages: [], created: Date.now() };
      await env.KV.put(`flow:${id}`, JSON.stringify(session));
      return { ok: true, session_id: id };
    }

    if (name === 'flow_get') {
      if (!env.KV) return { error: 'KV not bound' };
      const s = await env.KV.get(`flow:${args.session_id}`, 'json');
      return s ? { ok: true, session: s } : { error: 'Not found' };
    }

    if (name === 'flow_message') {
      if (!env.KV) return { error: 'KV not bound' };
      const s = await env.KV.get(`flow:${args.session_id}`, 'json');
      if (!s) return { error: 'Not found' };
      s.messages.push({ role: args.role || 'user', content: args.content, ts: Date.now() });
      await env.KV.put(`flow:${args.session_id}`, JSON.stringify(s));
      return { ok: true };
    }

    if (name === 'flow_distribute') {
      if (!env.BUCKET) return { error: 'R2 not bound' };
      const key = `${args.target}/${Date.now()}.txt`;
      await env.BUCKET.put(key, args.content);
      return { ok: true, key };
    }

    // SYSTEM TOOLS
    if (name === 'system_status') {
      return {
        ok: true,
        galaxy: CONFIG.GALAXY,
        version: CONFIG.VERSION,
        bindings: {
          AI: !!env.AI,
          DB: !!env.DB,
          DB_MEMORY: !!env.DB_MEMORY,
          KV: !!env.KV,
          KV_SIGNUPS: !!env.KV_SIGNUPS,
          BUCKET: !!env.BUCKET,
          QUEUE: !!env.QUEUE,
          VECTOR: !!env.VECTOR,
          ANTHROPIC: !!env.ANTHROPIC_API_KEY
        },
        ts: Date.now()
      };
    }

    return { error: `Unknown tool: ${name}` };
  } catch (e) {
    return { error: e.message };
  }
}

async function fetchMCPResource(env, uri) {
  if (uri === 'noizy://repairs' && env.DB) {
    const r = await env.DB.prepare('SELECT * FROM repairs ORDER BY created_at DESC LIMIT 50').all();
    return { ok: true, repairs: r.results };
  }
  if (uri === 'noizy://signups' && env.KV_SIGNUPS) {
    const r = await env.KV_SIGNUPS.list({ limit: 100 });
    return { ok: true, emails: r.keys.map(k => k.name) };
  }
  if (uri.startsWith('noizy://memory/') && env.DB_MEMORY) {
    const userId = uri.replace('noizy://memory/', '');
    const r = await env.DB_MEMORY.prepare('SELECT * FROM lifeluv_memory WHERE user_id = ?').bind(userId).all();
    return { ok: true, memory: r.results };
  }
  if (uri.startsWith('noizy://flow/') && env.KV) {
    const sessionId = uri.replace('noizy://flow/', '');
    const s = await env.KV.get(`flow:${sessionId}`, 'json');
    return s ? { ok: true, session: s } : { error: 'Not found' };
  }
  return { error: 'Unknown resource' };
}

function getMCPPrompt(name) {
  const prompts = {
    repair_diagnosis: {
      name: 'repair_diagnosis',
      description: 'Diagnose a tech issue',
      messages: [
        { role: 'user', content: 'The user has this issue: {{issue}}\n\nProvide a diagnosis and suggested fix.' }
      ]
    },
    voice_coaching: {
      name: 'voice_coaching',
      description: 'NOIZYVOX artist guidance',
      messages: [
        { role: 'user', content: 'A voice artist asks: {{question}}\n\nProvide helpful guidance for voice AI recording.' }
      ]
    },
    code_review: {
      name: 'code_review',
      description: 'Review code',
      messages: [
        { role: 'user', content: 'Review this code:\n\n{{code}}\n\nProvide feedback on quality, bugs, and improvements.' }
      ]
    }
  };
  return prompts[name] || { error: 'Unknown prompt' };
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// 💚 LIFELUV — Enhanced AI Companion
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

async function handleLifeluv(request, env, url) {
  const path = url.pathname.replace('/lifeluv', '');

  // API endpoints
  if (path.startsWith('/api/')) {
    const route = path.replace('/api/', '');

    if (route === 'chat' && request.method === 'POST') {
      const { user_id, message } = await request.json();
      return json(await executeMCPTool(env, 'lifeluv_chat', { user_id: user_id || 'default', message }));
    }

    if (route === 'memory') {
      if (request.method === 'GET') {
        const userId = url.searchParams.get('user_id') || 'default';
        return json(await executeMCPTool(env, 'lifeluv_memory_get', { user_id: userId }));
      }
      if (request.method === 'POST') {
        const body = await request.json();
        return json(await executeMCPTool(env, 'lifeluv_memory_set', body));
      }
    }

    if (route === 'history' && env.DB_MEMORY) {
      const userId = url.searchParams.get('user_id') || 'default';
      const limit = parseInt(url.searchParams.get('limit') || '50');
      const r = await env.DB_MEMORY.prepare('SELECT * FROM lifeluv_conversations WHERE user_id = ? ORDER BY created_at DESC LIMIT ?').bind(userId, limit).all();
      return json({ ok: true, history: r.results.reverse() });
    }

    return json({ service: 'LIFELUV API', endpoints: ['POST /api/chat', 'GET|POST /api/memory', 'GET /api/history'] });
  }

  // Landing page
  return html(lifeluvPage());
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// 🌊 FLOW — Enhanced Conversation Continuity
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

async function handleFlow(request, env, url) {
  const path = url.pathname.replace('/flow', '');

  if (path.startsWith('/api/')) {
    const route = path.replace('/api/', '');

    if (route === 'session' && request.method === 'POST') {
      return json(await executeMCPTool(env, 'flow_create', await request.json()));
    }

    if (route.startsWith('session/')) {
      const id = route.replace('session/', '');
      if (request.method === 'GET') {
        return json(await executeMCPTool(env, 'flow_get', { session_id: id }));
      }
      if (request.method === 'POST') {
        const body = await request.json();
        return json(await executeMCPTool(env, 'flow_message', { session_id: id, ...body }));
      }
    }

    if (route === 'distribute' && request.method === 'POST') {
      return json(await executeMCPTool(env, 'flow_distribute', await request.json()));
    }

    return json({ service: 'FLOW API', endpoints: ['POST /api/session', 'GET|POST /api/session/{id}', 'POST /api/distribute'] });
  }

  return html(flowPage());
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// 🌟 PRODUCT PAGES (Compact)
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

function handlePortal(r, env, url) {
  if (url.pathname.startsWith('/api/')) return handleAPI(r, env, url);
  return html(portalPage());
}

function handleVox(r, env, url) {
  if (url.pathname.startsWith('/api/')) return handleAPI(r, env, url);
  return html(voxPage());
}

function handleCodemaster(r, env, url) {
  if (url.pathname.startsWith('/api/')) return handleAPI(r, env, url);
  return html(codemasterPage());
}

function handleBooks(r, env, url) {
  if (url.pathname.startsWith('/api/')) return handleAPI(r, env, url);
  return html(booksPage());
}

function handleLab(r, env, url) {
  if (url.pathname.startsWith('/api/')) return handleAPI(r, env, url);
  return html(labPage());
}

function handleAdmin(r, env, url) {
  return json({
    service: 'NOIZY.AI Admin',
    version: CONFIG.VERSION,
    routes: {
      '/ai/*': 'Workers AI + Anthropic',
      '/mcp/*': 'MCP Server',
      '/agent/*': 'Agent SDK',
      '/api/*': 'REST API',
      '/lifeluv/*': 'AI Companion',
      '/flow/*': 'Conversation Continuity'
    }
  });
}

async function handleAPI(request, env, url) {
  const p = url.pathname.replace('/api/', '');
  const m = request.method;

  if (p === 'repairs' || p.startsWith('repairs/')) {
    if (m === 'GET' && env.DB) {
      const status = url.searchParams.get('status');
      return json(await executeMCPTool(env, 'db_repairs_list', { status }));
    }
    if (m === 'POST') {
      return json(await executeMCPTool(env, 'db_repairs_create', await request.json()));
    }
  }

  if (p === 'signups' || p === 'join') {
    if (m === 'POST') {
      const { email } = await request.json();
      if (env.KV_SIGNUPS) await env.KV_SIGNUPS.put(email.toLowerCase(), JSON.stringify({ email, ts: Date.now() }));
      return json({ ok: true, message: 'Welcome to NOIZYVOX!' });
    }
  }

  if (p === 'status') return json(await executeMCPTool(env, 'system_status', {}));

  return json({ endpoints: ['repairs', 'signups', 'status'] });
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// SCHEDULED & QUEUE HANDLERS
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

async function cleanExpiredSessions(env) {
  if (!env.KV) return;
  const list = await env.KV.list({ prefix: 'session:' });
  for (const key of list.keys) {
    const data = await env.KV.get(key.name, 'json');
    if (data && data.expires && data.expires < Date.now()) {
      await env.KV.delete(key.name);
    }
  }
}

async function generateDailyReport(env) {
  if (!env.QUEUE) return;
  await env.QUEUE.send({ type: 'DAILY_REPORT', ts: Date.now() });
}

async function sendWeeklyDigest(env) {
  if (!env.QUEUE) return;
  await env.QUEUE.send({ type: 'WEEKLY_DIGEST', ts: Date.now() });
}

async function processQueueJob(env, job) {
  console.log('Processing job:', job.type);
  // Implement job handlers
}

async function handleIncomingEmail(message, env) {
  if (!env.DB) return;
  const from = message.from;
  const to = message.to;
  const subject = message.headers.get('subject') || '';

  await env.DB.prepare('INSERT INTO emails (from_addr, to_addr, subject, received_at) VALUES (?, ?, ?, ?)')
    .bind(from, to, subject, Date.now()).run();

  // Route based on recipient
  if (to.includes('help@noizylab')) {
    await env.DB.prepare('INSERT INTO support_tickets (email, subject, status, created_at) VALUES (?, ?, ?, ?)')
      .bind(from, subject, 'new', Date.now()).run();
  }
  if (to.includes('join@noizyvox') && env.KV_SIGNUPS) {
    await env.KV_SIGNUPS.put(from.toLowerCase(), JSON.stringify({ email: from, source: 'email', ts: Date.now() }));
  }
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// HELPERS
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

function getSubdomain(host, path) {
  if (host.endsWith('noizy.ai')) {
    const parts = host.split('.');
    if (parts.length >= 3 && parts[0] !== 'www') return parts[0];
  }
  if (host.includes('workers.dev')) {
    const segment = path.split('/')[1];
    if (CONFIG.PRODUCTS.includes(segment)) return segment;
  }
  return 'portal';
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders(), 'X-Powered-By': `HEAVEN v${CONFIG.VERSION}` }
  });
}

function html(content) {
  return new Response(content, {
    headers: { 'Content-Type': 'text/html;charset=UTF-8', 'X-Powered-By': `HEAVEN v${CONFIG.VERSION}` }
  });
}

function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type,Authorization,X-API-Key'
  };
}

function corsResponse() {
  return new Response(null, { headers: corsHeaders() });
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════════
// HTML TEMPLATES (Compact)
// ═══════════════════════════════════════════════════════════════════════════════════════════════════════

function portalPage() {
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NOIZY.AI — The Galaxy</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,sans-serif;background:#030308;color:#fff;min-height:100vh}
.s{position:fixed;inset:0;background:radial-gradient(ellipse at bottom,#1B2735,#090A0F)}
.c{position:relative;z-index:1}
h{display:block;min-height:50vh;text-align:center;padding:4rem 2rem}
.logo{font-size:clamp(3rem,12vw,6rem);font-weight:900;background:linear-gradient(135deg,#ff3366,#8855ff,#00ff88);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.tag{font-size:1.3rem;opacity:.8;margin:1rem 0}.badge{display:inline-block;padding:.5rem 1.5rem;background:linear-gradient(135deg,#00ff88,#ff3366);border-radius:50px;font-weight:700;margin:1rem}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.5rem;padding:2rem;max-width:1400px;margin:0 auto}
.p{background:rgba(255,255,255,.02);border-radius:25px;padding:1.5rem;text-align:center;text-decoration:none;color:#fff;transition:all .3s;border:1px solid rgba(255,255,255,.05)}
.p:hover{transform:translateY(-10px);border-color:var(--c);box-shadow:0 20px 40px -20px var(--c)}
.p.vox{--c:#ff3366}.p.code{--c:#00ff88}.p.books{--c:#ff9500}.p.lab{--c:#00aaff}.p.life{--c:#10b981}.p.flow{--c:#8b5cf6}.p.agent{--c:#f59e0b}
.pi{font-size:2.5rem;margin-bottom:.5rem}.p h2{color:var(--c);margin-bottom:.25rem;font-size:1.1rem}.p p{opacity:.7;font-size:.85rem}
.pt{display:inline-block;margin-top:.5rem;padding:.2rem .6rem;background:var(--c);color:#000;border-radius:15px;font-size:.7rem;font-weight:700}
f{display:block;text-align:center;padding:3rem;border-top:1px solid rgba(255,255,255,.05)}
.grf{font-size:2rem;font-weight:900;background:linear-gradient(135deg,#00ff88,#ff3366);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
f p{opacity:.4;margin:.5rem;font-size:.85rem}
</style></head><body><div class="s"></div><div class="c">
<h><h1 class="logo">NOIZY.AI</h1><p class="tag">Where Sound is the Soul of Everything</p><div class="badge">⚡ v4 ULTIMATE — AI + Agents + MCP</div></h>
<section class="g">
<a href="https://vox.noizy.ai" class="p vox"><div class="pi">🎤</div><h2>NOIZYVOX</h2><p>Voice AI Guild</p><span class="pt">75/25</span></a>
<a href="https://codemaster.noizy.ai" class="p code"><div class="pi">🖥️</div><h2>CODEMASTER</h2><p>Voice-First Infra</p><span class="pt">ONE CMD</span></a>
<a href="https://books.noizy.ai" class="p books"><div class="pi">📚</div><h2>FISHYBOOKS</h2><p>AI Audiobooks</p><span class="pt">SOON</span></a>
<a href="https://lab.noizy.ai" class="p lab"><div class="pi">💻</div><h2>NOIZYLAB</h2><p>Tech Repairs</p><span class="pt">$89</span></a>
<a href="https://lifeluv.noizy.ai" class="p life"><div class="pi">💚</div><h2>LIFELUV</h2><p>AI Companion</p><span class="pt">ACCESSIBLE</span></a>
<a href="https://flow.noizy.ai" class="p flow"><div class="pi">🌊</div><h2>FLOW</h2><p>Conversation Continuity</p><span class="pt">REALTIME</span></a>
<a href="https://agent.noizy.ai" class="p agent"><div class="pi">🤖</div><h2>AGENTS</h2><p>AI Agent SDK</p><span class="pt">TOOL LOOP</span></a>
</section>
<f><div class="grf">GORUNFREE</div><p>Built by Rob Plowman • 40 Years Fish Music Inc.</p><p>🐟 Ed Edd n Eddy • Dragon Tales • Johnny Test • Transformers • Barbie</p></f>
</div></body></html>`;
}

function voxPage() {
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NOIZYVOX</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,sans-serif;background:#0a0a12;color:#fff;min-height:100vh}.bg{position:fixed;inset:0;background:radial-gradient(circle at 20% 30%,rgba(255,51,102,.15),transparent 50%)}.c{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:2rem}.hero{min-height:90vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}.logo{font-size:4rem;font-weight:900;background:linear-gradient(135deg,#ff3366,#ff6b6b);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.badge{background:linear-gradient(135deg,#ffd700,#ffaa00);color:#000;padding:1rem 2rem;border-radius:50px;font-size:1.5rem;font-weight:900;margin:1.5rem}footer{text-align:center;padding:2rem;opacity:.5}</style></head>
<body><div class="bg"></div><div class="c"><section class="hero"><h1 class="logo">🎤 NOIZYVOX</h1><p style="font-size:1.3rem;margin:1rem">The Voice AI Guild</p><div class="badge">75/25 — Artists First</div><p style="opacity:.7;max-width:500px">The world's first artist-owned voice AI guild. Your voice, your rules.</p></section>
<footer>Part of <a href="https://noizy.ai" style="color:#00ff88">NOIZY.AI</a></footer></div></body></html>`;
}

function codemasterPage() {
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CODEMASTER</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,sans-serif;background:#0a0a0a;color:#fff;min-height:100vh}.c{max-width:800px;margin:0 auto;padding:2rem;text-align:center}.hero{min-height:90vh;display:flex;flex-direction:column;align-items:center;justify-content:center}.logo{font-size:3.5rem;font-weight:900;background:linear-gradient(135deg,#00ff88,#ff3366);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.term{background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.1);border-radius:20px;padding:2rem;width:100%;max-width:500px;margin-top:2rem}.term-h{display:flex;gap:6px;margin-bottom:1rem}.dot{width:10px;height:10px;border-radius:50%}.dot.r{background:#ff5f56}.dot.y{background:#ffbd2e}.dot.g{background:#27ca40}.term-out{padding:1rem;background:rgba(0,255,136,.05);border-radius:10px;color:#00ff88;font-family:monospace;min-height:60px;text-align:left}</style></head>
<body><div class="c"><section class="hero"><h1 class="logo">🖥️ CODEMASTER</h1><p style="margin:1rem;opacity:.8">One command. Total control.</p>
<div class="term"><div class="term-h"><div class="dot r"></div><div class="dot y"></div><div class="dot g"></div></div><div class="term-out">$ GORUNFREE<br>✓ All systems operational<br>✓ AI: Ready (Workers + Anthropic)<br>✓ MCP: Online<br>✓ Agents: Standing by</div></div></section></div></body></html>`;
}

function booksPage() {
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>FISHYBOOKS</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Comic Sans MS',cursive;background:linear-gradient(180deg,#0f1629,#1e1b4b);color:#fff;min-height:100vh}.c{max-width:900px;margin:0 auto;padding:2rem;text-align:center}header{padding:4rem 0}.logo{font-size:3rem}.logo span{background:linear-gradient(135deg,#ff9500,#ffcc00);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.badge{display:inline-block;background:linear-gradient(135deg,#8b5cf6,#ff9500);padding:.8rem 2rem;border-radius:50px;font-weight:700;margin:2rem}</style></head>
<body><div class="c"><header><h1 class="logo">📚 <span>FISHYBOOKS</span></h1><p style="margin-top:.5rem">Stories for Munchkins ✨</p><div class="badge">🚀 Coming Soon!</div></header></div></body></html>`;
}

function labPage() {
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NOIZYLAB</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,sans-serif;background:#0a0a14;color:#fff;min-height:100vh}.c{max-width:800px;margin:0 auto;padding:2rem;text-align:center}.hero{min-height:80vh;display:flex;flex-direction:column;align-items:center;justify-content:center}.logo{font-size:3rem;color:#00aaff}.price{font-size:clamp(4rem,15vw,6rem);font-weight:900;background:linear-gradient(135deg,#00aaff,#00ff88);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.btn{display:inline-block;padding:1rem 2.5rem;background:#00aaff;color:#000;font-weight:700;border-radius:50px;text-decoration:none;margin-top:2rem}</style></head>
<body><div class="c"><section class="hero"><h1 class="logo">💻 NOIZYLAB</h1><div class="price">$89</div><p style="opacity:.7;margin:1rem">Flat rate. Any repair. Done right.</p><a href="mailto:help@noizylab.ca" class="btn">Book Repair</a></section></div></body></html>`;
}

function lifeluvPage() {
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>LIFELUV — Your AI Companion</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,sans-serif;background:#0a1628;color:#fff;min-height:100vh}
.bg{position:fixed;inset:0;background:radial-gradient(circle at 30% 30%,rgba(16,185,129,.15),transparent 50%)}
.c{position:relative;z-index:1;max-width:800px;margin:0 auto;padding:2rem}
.hero{min-height:80vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.logo{font-size:4rem;margin-bottom:1rem}.title{font-size:3rem;font-weight:900;background:linear-gradient(135deg,#10b981,#3b82f6);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.chat-box{background:rgba(0,0,0,.3);border-radius:20px;padding:2rem;width:100%;max-width:500px;margin-top:2rem}
.chat-input{display:flex;gap:1rem}
.chat-input input{flex:1;padding:1rem;border-radius:50px;border:2px solid rgba(255,255,255,.1);background:rgba(0,0,0,.3);color:#fff;font-size:1rem}
.chat-input button{padding:1rem 2rem;background:#10b981;color:#000;border:none;border-radius:50px;font-weight:700;cursor:pointer}
.chat-output{margin-top:1.5rem;padding:1rem;background:rgba(16,185,129,.1);border-radius:15px;min-height:100px;white-space:pre-wrap}
</style></head><body><div class="bg"></div><div class="c">
<section class="hero">
<div class="logo">💚</div>
<h1 class="title">LIFELUV</h1>
<p style="opacity:.8;margin:1rem">Your AI Companion — Voice-First, Accessible, Always There</p>
<div class="chat-box">
<div class="chat-input"><input type="text" id="msg" placeholder="Say something..."><button onclick="chat()">Send</button></div>
<div class="chat-output" id="out">Hi! I'm LIFELUV. How can I help you today?</div>
</div>
</section>
</div>
<script>
async function chat(){const msg=document.getElementById('msg').value;if(!msg)return;document.getElementById('out').textContent='Thinking...';
try{const r=await fetch('/lifeluv/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({user_id:'web',message:msg})});
const d=await r.json();document.getElementById('out').textContent=d.response||d.error||JSON.stringify(d);document.getElementById('msg').value=''}catch(e){document.getElementById('out').textContent='Error: '+e.message}}
document.getElementById('msg').addEventListener('keypress',e=>{if(e.key==='Enter')chat()});
</script></body></html>`;
}

function flowPage() {
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>FLOW — Conversation Continuity</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,sans-serif;background:#0f0a1e;color:#fff;min-height:100vh}
.bg{position:fixed;inset:0;background:radial-gradient(circle at 20% 50%,rgba(139,92,246,.15),transparent 50%)}
.c{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:2rem}
.hero{min-height:80vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.logo{font-size:4rem;margin-bottom:1rem}.title{font-size:3rem;font-weight:900;background:linear-gradient(135deg,#8b5cf6,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.features{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin:4rem 0}
.feat{background:rgba(255,255,255,.03);padding:2rem;border-radius:20px;text-align:center}
.feat-icon{font-size:3rem;margin-bottom:1rem}.feat h3{color:#8b5cf6;margin-bottom:.5rem}
</style></head><body><div class="bg"></div><div class="c">
<section class="hero">
<div class="logo">🌊</div>
<h1 class="title">FLOW</h1>
<p style="opacity:.8;margin:1rem">Conversation Continuity — Chat Subject = Anchor</p>
</section>
<section class="features">
<div class="feat"><div class="feat-icon">📌</div><h3>Subject Anchor</h3><p style="opacity:.7">Chat subject captures semantic flow</p></div>
<div class="feat"><div class="feat-icon">🔄</div><h3>Cross-Device</h3><p style="opacity:.7">Jump between devices seamlessly</p></div>
<div class="feat"><div class="feat-icon">📂</div><h3>Auto-Distribute</h3><p style="opacity:.7">CODE_VAC files to right folders</p></div>
</section>
</div></body></html>`;
}
