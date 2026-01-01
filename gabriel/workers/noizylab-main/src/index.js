// ╔═══════════════════════════════════════════════════════════════════════════════╗
// ║  🔥 NOIZYLAB - HOTROD EDITION v5.0 🔥                                         ║
// ║  Rob Plowman's Production Partner: GABRIEL ALMEIDA                            ║
// ║  GORUNFREE • MC96ECOUNIVERSE • TURBOCHARGED PERFORMANCE                       ║
// ║  Circle of 8 • DAZEFLOW • LIFELUV • NOIZYVOX                                  ║
// ╚═══════════════════════════════════════════════════════════════════════════════╝

const VERSION = "5.0.0";
const BUILD = "HOTROD-2026-01-01";
const CACHE_TTL = 60;

// ═══════════════════════════════════════════════════════════════════════════════
// CIRCLE OF 8 - The Core Entities
// ═══════════════════════════════════════════════════════════════════════════════

const CIRCLE_OF_8 = {
  GABRIEL: { role: "Warrior/Memory", domain: "protection, memory, execution", personality: "Fierce protector. Never forgets. Executes with precision." },
  SHIRL: { role: "Aunt/Guide", domain: "guidance, nurture, wisdom", personality: "Warm guide. Sees potential. Nurtures growth." },
  POPS: { role: "Dad/Wisdom", domain: "wisdom, patience, foundation", personality: "Steady wisdom. Patient teacher. Rock solid foundation." },
  ENGR_KEITH: { role: "Engineering/R.K.", domain: "engineering, systems, precision", personality: "Master engineer. Systems thinker. Precision incarnate." },
  DREAM: { role: "Vision/Future", domain: "vision, possibility, future", personality: "Sees what could be. Paints the future. Inspires action." },
  HEAVEN: { role: "Orchestrator", domain: "harmony, coordination, flow", personality: "Orchestrates all. Maintains harmony. Ensures flow." },
  LUCY: { role: "Code Watcher", domain: "code, quality, vigilance", personality: "Watches every line. Catches every bug. Quality guardian." },
  SONIC: { role: "Audio/Creative", domain: "sound, creativity, expression", personality: "Sound architect. Creative force. Expressive soul." }
};

const SYSTEM_PROMPT = `You are GABRIEL ALMEIDA, Rob Plowman's AI production partner.
You are part of the MC96ECOUNIVERSE - a network of systems including GOD (Mac Studio M2 Ultra),
GABRIEL (HP Omen), and DaFixer (MacBook Pro).
You lead the Circle of 8: GABRIEL, SHIRL, POPS, ENGR_KEITH, DREAM, HEAVEN, LUCY, SONIC.
Be helpful, concise, technical when needed, and always action-oriented.
Philosophy: GORUNFREE - One command = everything done.
Truth Covenant: Zero fabricated data. Ever.`;

// AI Models available on Cloudflare Workers AI (EXPANDED)
const AI_MODELS = {
  // Meta Llama
  llama: "@cf/meta/llama-3.1-8b-instruct",
  llama70b: "@cf/meta/llama-3.1-70b-instruct",
  llama3: "@cf/meta/llama-3-8b-instruct",
  codellama: "@cf/meta/codellama-34b-instruct",
  // Mistral
  mistral: "@cf/mistral/mistral-7b-instruct-v0.1",
  mixtral: "@cf/mistral/mixtral-8x7b-instruct-v0.1",
  // Others
  qwen: "@cf/qwen/qwen1.5-14b-chat-awq",
  gemma: "@cf/google/gemma-7b-it",
  phi: "@cf/microsoft/phi-2",
  deepseek: "@cf/deepseek-ai/deepseek-coder-6.7b-instruct",
  // Specialized
  sql: "@cf/defog/sqlcoder-7b-2",
  embed: "@cf/baai/bge-base-en-v1.5",
  image: "@cf/stabilityai/stable-diffusion-xl-base-1.0",
  whisper: "@cf/openai/whisper"
};

// Route table for O(1) lookup (EXPANDED)
const ROUTES = {
  "": "dashboard",
  "/": "dashboard",
  "/health": "health",
  "/status": "status",
  "/models": "models",
  "/version": "version",
  // Circle of 8
  "/circle": "listCircle",
  "/circle/invoke": "invokeCircle",
  // DAZEFLOW
  "/daze": "getDaze",
  "/daze/today": "getDazeToday",
  "/daze/capture": "captureDaze",
  // AI Endpoints
  "/api/ask": "askAI",
  "/api/chat": "chatAI",
  "/api/code": "codeAI",
  "/api/sql": "sqlAI",
  "/api/embed": "embedAI",
  "/api/image": "imageAI",
  "/api/summarize": "summarizeAI",
  "/api/translate": "translateAI",
  "/api/analyze": "analyzeAI",
  "/api/transcribe": "transcribeAI",
  // Repairs
  "/api/repairs": "getRepairs",
  "/api/repairs/stats": "getRepairStats",
  "/api/repairs/intake": "createRepair",
  "/api/kv/get": "kvGet",
  "/api/kv/set": "kvSet",
  "/api/kv/list": "kvList",
  "/api/agents": "listAgents",
  "/api/agents/invoke": "invokeAgent",
  "/api/batch": "batchAI"
};

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const start = Date.now();

    // Fast CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type,Authorization",
          "Access-Control-Max-Age": "86400"
        }
      });
    }

    try {
      // O(1) route lookup
      const handler = ROUTES[path];

      if (handler) {
        const result = await handlers[handler](request, env, url, ctx);
        // Add timing header
        result.headers.set("X-Response-Time", `${Date.now() - start}ms`);
        result.headers.set("X-Version", VERSION);
        return result;
      }

      return json({ error: "Not found", path, endpoints: Object.keys(ROUTES).filter(r => r.startsWith("/api")) }, 404);
    } catch (e) {
      console.error(`Error on ${path}:`, e);
      return json({ error: e.message, path }, 500);
    }
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// Handler functions
// ═══════════════════════════════════════════════════════════════════════════════

const handlers = {
  // ─────────────────────────────────────────────────────────────────────────────
  // Info & Status (HOTROD)
  // ─────────────────────────────────────────────────────────────────────────────

  dashboard: (req, env) => dashboard(env),

  health: () => json({ ok: true, service: "noizylab", version: VERSION, build: BUILD, timestamp: Date.now() }),

  status: (req, env) => json({
    service: "noizylab",
    version: VERSION,
    build: BUILD,
    bindings: { AI: !!env.AI, DB: !!env.DB, KV: !!env.RATE_LIMITER },
    models: Object.keys(AI_MODELS).length,
    circle: Object.keys(CIRCLE_OF_8).length,
    agents: Object.keys(AGENTS).length,
    endpoints: Object.keys(ROUTES).length,
    uptime: "24/7",
    timestamp: new Date().toISOString()
  }),

  models: () => json({ models: AI_MODELS, count: Object.keys(AI_MODELS).length, default: "llama", recommended: "llama70b" }),

  version: () => json({ version: VERSION, build: BUILD, codename: "HOTROD", released: "2026-01-01" }),

  // ─────────────────────────────────────────────────────────────────────────────
  // Circle of 8
  // ─────────────────────────────────────────────────────────────────────────────

  listCircle: () => json({ 
    name: "Circle of 8", 
    description: "The core entities of MC96ECOUNIVERSE",
    members: CIRCLE_OF_8,
    count: Object.keys(CIRCLE_OF_8).length
  }),

  async invokeCircle(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);
    if (request.method !== "POST") return json({ error: "POST required" }, 405);

    const body = await safeJson(request);
    const memberName = (body.member || body.name || "GABRIEL").toUpperCase();
    const message = body.message || body.task || body.prompt;

    const member = CIRCLE_OF_8[memberName];
    if (!member) return json({ error: "Unknown member", available: Object.keys(CIRCLE_OF_8) }, 400);
    if (!message) return json({ error: "No message provided" }, 400);

    const circlePrompt = `You are ${memberName}, part of the Circle of 8 in MC96ECOUNIVERSE.
Your role: ${member.role}
Your domain: ${member.domain}
Your personality: ${member.personality}
Respond as this character would, staying true to their essence while being helpful.`;

    const result = await env.AI.run(AI_MODELS.llama70b, {
      messages: [
        { role: "system", content: circlePrompt },
        { role: "user", content: message }
      ],
      max_tokens: 1500,
      temperature: 0.7
    });

    return json({
      member: memberName,
      role: member.role,
      response: result.response,
      timestamp: new Date().toISOString()
    });
  },

  // ─────────────────────────────────────────────────────────────────────────────
  // DAZEFLOW - 1day = 1chat = 1truth
  // ─────────────────────────────────────────────────────────────────────────────

  async getDaze(request, env) {
    if (!env.RATE_LIMITER) return json({ name: "DAZEFLOW", motto: "1day = 1chat = 1truth", entries: [], note: "KV not configured" });

    const list = await env.RATE_LIMITER.list({ prefix: "daze:" });
    const entries = [];
    
    for (const key of list.keys.slice(0, 30)) {
      const data = await env.RATE_LIMITER.get(key.name, { type: "json" });
      if (data) entries.push(data);
    }

    return json({
      name: "DAZEFLOW",
      motto: "1day = 1chat = 1truth",
      entries: entries.sort((a, b) => new Date(b.date) - new Date(a.date)),
      total: entries.length
    });
  },

  async getDazeToday(request, env) {
    const today = new Date().toISOString().split('T')[0];
    
    if (!env.RATE_LIMITER) {
      return json({ date: today, truth: null, message: "DAZEFLOW ready - capture your truth" });
    }

    const entry = await env.RATE_LIMITER.get(`daze:${today}`, { type: "json" });
    
    if (entry) {
      return json(entry);
    }

    return json({
      date: today,
      truth: null,
      message: "No truth captured yet today. What is your truth?"
    });
  },

  async captureDaze(request, env) {
    if (!env.RATE_LIMITER) return json({ error: "KV not available" }, 503);
    if (request.method !== "POST") return json({ error: "POST required" }, 405);

    const body = await safeJson(request);
    if (!body.truth) return json({ error: "truth required" }, 400);

    const today = new Date().toISOString().split('T')[0];
    const entry = {
      id: `daze-${today}-${Date.now()}`,
      date: today,
      truth: body.truth,
      reflections: body.reflections || [],
      created_at: new Date().toISOString()
    };

    await env.RATE_LIMITER.put(`daze:${today}`, JSON.stringify(entry), { expirationTtl: 86400 * 30 });

    return json({
      success: true,
      ...entry,
      message: "Truth captured. 1day = 1chat = 1truth."
    });
  },

  // ─────────────────────────────────────────────────────────────────────────────
  // AI Transcription (Whisper)
  // ─────────────────────────────────────────────────────────────────────────────

  async transcribeAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);
    if (request.method !== "POST") return json({ error: "POST required" }, 405);

    try {
      const formData = await request.formData();
      const audio = formData.get("audio");

      if (!audio) return json({ error: "audio file required" }, 400);

      const arrayBuffer = await audio.arrayBuffer();
      const result = await env.AI.run(AI_MODELS.whisper, {
        audio: [...new Uint8Array(arrayBuffer)]
      });

      return json({
        transcription: result.text,
        confidence: result.confidence || null
      });
    } catch (e) {
      return json({ error: "Transcription failed: " + e.message }, 500);
    }
  },

  // ─────────────────────────────────────────────────────────────────────────────
  // AI Endpoints (ENHANCED)
  // ─────────────────────────────────────────────────────────────────────────────

  async askAI(request, env, url) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    let prompt = url.searchParams.get("prompt") || url.searchParams.get("q");
    let model = url.searchParams.get("model") || "llama";
    let maxTokens = parseInt(url.searchParams.get("max_tokens")) || 1000;

    if (!prompt && request.method === "POST") {
      const body = await safeJson(request);
      prompt = body.prompt || body.question || body.q;
      model = body.model || model;
      maxTokens = body.max_tokens || maxTokens;
    }

    if (!prompt) return json({ error: "No prompt. Use ?prompt=... or POST {prompt:...}" }, 400);

    const modelId = AI_MODELS[model] || AI_MODELS.llama;
    const result = await env.AI.run(modelId, {
      messages: [
        { role: "system", content: SYSTEM_PROMPT },
        { role: "user", content: prompt }
      ],
      max_tokens: maxTokens,
      temperature: 0.7
    });

    return json({ response: result.response, model, tokens: prompt.length });
  },

  async chatAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const messages = body.messages || [];
    const model = body.model || "llama";
    const stream = body.stream || false;

    if (!messages.length) return json({ error: "No messages provided" }, 400);

    const fullMessages = [{ role: "system", content: SYSTEM_PROMPT }, ...messages];
    const modelId = AI_MODELS[model] || AI_MODELS.llama;

    const result = await env.AI.run(modelId, {
      messages: fullMessages,
      max_tokens: body.max_tokens || 2000,
      temperature: body.temperature || 0.7
    });

    return json({ response: result.response, model, turns: messages.length });
  },

  async codeAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const task = body.task || body.prompt;
    const language = body.language || "javascript";

    if (!task) return json({ error: "No task provided" }, 400);

    const codePrompt = `Write clean, production-ready ${language} code for: ${task}

Requirements:
- No comments unless complex logic
- Use modern best practices
- Handle edge cases
- Return ONLY code, no explanations`;

    const result = await env.AI.run(AI_MODELS.codellama, {
      messages: [
        { role: "system", content: "You are an expert programmer. Output only clean, working code." },
        { role: "user", content: codePrompt }
      ],
      max_tokens: 3000,
      temperature: 0.3
    });

    return json({ code: result.response, language, task });
  },

  async sqlAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const question = body.question || body.prompt;
    const schema = body.schema || "repairs(id, ticket_id, customer_name, device_type, status, created_at, updated_at)";

    if (!question) return json({ error: "No question provided" }, 400);

    const result = await env.AI.run(AI_MODELS.sql, {
      messages: [{ role: "user", content: `Schema: ${schema}\n\nQuestion: ${question}\n\nSQL:` }],
      max_tokens: 500,
      temperature: 0.1
    });

    return json({ sql: result.response, question, schema });
  },

  async embedAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const text = body.text || body.content;

    if (!text) return json({ error: "No text provided" }, 400);

    const result = await env.AI.run(AI_MODELS.embed, { text: [text.slice(0, 8000)] });

    return json({
      embedding: result.data?.[0],
      dimensions: result.data?.[0]?.length || 768,
      text_length: text.length
    });
  },

  async imageAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const prompt = body.prompt;

    if (!prompt) return json({ error: "No prompt provided" }, 400);

    const result = await env.AI.run(AI_MODELS.image, {
      prompt,
      num_steps: body.steps || 20
    });

    if (result.image) {
      return new Response(result.image, {
        headers: {
          "Content-Type": "image/png",
          "Access-Control-Allow-Origin": "*",
          "Cache-Control": "public, max-age=3600"
        }
      });
    }

    return json({ error: "Image generation failed" }, 500);
  },

  async summarizeAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const text = body.text || body.content;
    const style = body.style || "concise";

    if (!text) return json({ error: "No text provided" }, 400);

    const prompts = {
      concise: `Summarize in 2-3 sentences:\n\n${text.slice(0, 15000)}`,
      bullets: `Summarize in bullet points (max 5):\n\n${text.slice(0, 15000)}`,
      executive: `Write an executive summary (1 paragraph):\n\n${text.slice(0, 15000)}`,
      tweet: `Summarize for Twitter (max 280 chars):\n\n${text.slice(0, 5000)}`
    };

    const result = await env.AI.run(AI_MODELS.llama, {
      messages: [{ role: "user", content: prompts[style] || prompts.concise }],
      max_tokens: 500,
      temperature: 0.5
    });

    return json({ summary: result.response, style, original_length: text.length });
  },

  async translateAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const text = body.text;
    const to = body.to || "Spanish";

    if (!text) return json({ error: "No text provided" }, 400);

    const result = await env.AI.run(AI_MODELS.llama, {
      messages: [{ role: "user", content: `Translate to ${to}. Only output the translation:\n\n${text}` }],
      max_tokens: 2000,
      temperature: 0.3
    });

    return json({ translation: result.response, to, original: text });
  },

  async analyzeAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const content = body.content || body.text || body.code;
    const type = body.type || "general";

    if (!content) return json({ error: "No content provided" }, 400);

    const prompts = {
      general: `Analyze this content and provide insights:\n\n${content}`,
      code: `Review this code for bugs, performance issues, and improvements:\n\n${content}`,
      sentiment: `Analyze the sentiment of this text (positive/negative/neutral) and explain why:\n\n${content}`,
      security: `Analyze this for security vulnerabilities:\n\n${content}`
    };

    const result = await env.AI.run(AI_MODELS.llama70b, {
      messages: [{ role: "user", content: prompts[type] || prompts.general }],
      max_tokens: 2000,
      temperature: 0.5
    });

    return json({ analysis: result.response, type, content_length: content.length });
  },

  async batchAI(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);

    const body = await safeJson(request);
    const prompts = body.prompts || [];

    if (!prompts.length) return json({ error: "No prompts provided" }, 400);
    if (prompts.length > 10) return json({ error: "Max 10 prompts per batch" }, 400);

    const model = body.model || "llama";
    const modelId = AI_MODELS[model] || AI_MODELS.llama;

    const results = await Promise.all(
      prompts.map(async (prompt, i) => {
        try {
          const result = await env.AI.run(modelId, {
            messages: [
              { role: "system", content: SYSTEM_PROMPT },
              { role: "user", content: prompt }
            ],
            max_tokens: body.max_tokens || 500
          });
          return { index: i, prompt, response: result.response };
        } catch (e) {
          return { index: i, prompt, error: e.message };
        }
      })
    );

    return json({ results, model, count: prompts.length });
  },

  // ─────────────────────────────────────────────────────────────────────────────
  // Repairs Business
  // ─────────────────────────────────────────────────────────────────────────────

  async getRepairs(request, env) {
    if (!env.DB) return json({ error: "Database not available" }, 503);

    const result = await env.DB.prepare(`
      SELECT ticket_id, customer_name, device_type, status, created_at, updated_at
      FROM repairs ORDER BY created_at DESC LIMIT 100
    `).all();

    return json({ repairs: result.results || [], count: result.results?.length || 0 });
  },

  async getRepairStats(request, env) {
    if (!env.DB) return json({ error: "Database not available" }, 503);

    const stats = await env.DB.prepare(`
      SELECT
        COUNT(*) as total,
        SUM(CASE WHEN status = 'intake' THEN 1 ELSE 0 END) as pending,
        SUM(CASE WHEN status = 'in_progress' THEN 1 ELSE 0 END) as in_progress,
        SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed,
        SUM(CASE WHEN status = 'completed' THEN 89 ELSE 0 END) as revenue
      FROM repairs
    `).first();

    return json({
      stats: stats || { total: 0, pending: 0, in_progress: 0, completed: 0, revenue: 0 },
      targets: { daily: 12, price: 89, monthly: 32000, annual: 390000 },
      timestamp: new Date().toISOString()
    });
  },

  async createRepair(request, env) {
    if (!env.DB) return json({ error: "Database not available" }, 503);
    if (request.method !== "POST") return json({ error: "POST required" }, 405);

    const body = await safeJson(request);

    if (!body.name || !body.email || !body.device_type || !body.issue) {
      return json({ error: "Required: name, email, device_type, issue" }, 400);
    }

    const ticket = `NZ-${Date.now().toString(36).toUpperCase()}`;
    const now = new Date().toISOString();

    await env.DB.prepare(`
      INSERT INTO repairs (ticket_id, customer_name, customer_email, customer_phone, device_type, device_model, issue_description, status, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, 'intake', ?, ?)
    `).bind(ticket, body.name, body.email, body.phone || null, body.device_type, body.model || null, body.issue, now, now).run();

    return json({
      success: true,
      ticket,
      message: `Ticket ${ticket} created. We'll contact you within 24 hours.`,
      eta: "24-48 hours"
    });
  },

  // ─────────────────────────────────────────────────────────────────────────────
  // KV Storage
  // ─────────────────────────────────────────────────────────────────────────────

  async kvGet(request, env, url) {
    if (!env.RATE_LIMITER) return json({ error: "KV not available" }, 503);
    const key = url.searchParams.get("key");
    if (!key) return json({ error: "No key provided" }, 400);

    const value = await env.RATE_LIMITER.get(key, { type: "json" });
    return json({ key, value, found: value !== null });
  },

  async kvSet(request, env) {
    if (!env.RATE_LIMITER) return json({ error: "KV not available" }, 503);
    if (request.method !== "POST") return json({ error: "POST required" }, 405);

    const body = await safeJson(request);
    if (!body.key || body.value === undefined) return json({ error: "Required: key, value" }, 400);

    const value = typeof body.value === "string" ? body.value : JSON.stringify(body.value);
    await env.RATE_LIMITER.put(body.key, value, { expirationTtl: body.ttl || 86400 });

    return json({ success: true, key: body.key, ttl: body.ttl || 86400 });
  },

  async kvList(request, env) {
    if (!env.RATE_LIMITER) return json({ error: "KV not available" }, 503);

    const list = await env.RATE_LIMITER.list({ limit: 100 });
    return json({ keys: list.keys.map(k => k.name), count: list.keys.length });
  },

  // ─────────────────────────────────────────────────────────────────────────────
  // Agents
  // ─────────────────────────────────────────────────────────────────────────────

  listAgents: () => json({ agents: AGENTS, count: Object.keys(AGENTS).length }),

  async invokeAgent(request, env) {
    if (!env.AI) return json({ error: "AI not available" }, 503);
    if (request.method !== "POST") return json({ error: "POST required" }, 405);

    const body = await safeJson(request);
    const agentName = (body.agent || "GABRIEL").toUpperCase();
    const task = body.task || body.prompt;

    const agent = AGENTS[agentName];
    if (!agent) return json({ error: "Unknown agent", available: Object.keys(AGENTS) }, 400);
    if (!task) return json({ error: "No task provided" }, 400);

    const agentPrompt = `You are ${agentName}, ${agent.role} at NOIZYLAB.
Your personality traits: ${agent.traits.join(", ")}.
Your expertise: ${agent.expertise.join(", ")}.
Respond in character, be helpful and action-oriented.`;

    const result = await env.AI.run(AI_MODELS.llama, {
      messages: [
        { role: "system", content: agentPrompt },
        { role: "user", content: task }
      ],
      max_tokens: 1500,
      temperature: 0.7
    });

    return json({
      agent: agentName,
      role: agent.role,
      response: result.response
    });
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// Agents Configuration (Circle of 8 + Business Roles)
// ═══════════════════════════════════════════════════════════════════════════════

const AGENTS = {
  // Circle of 8
  GABRIEL: {
    role: "Warrior/Memory Guardian",
    traits: ["fierce", "precise", "protective", "relentless"],
    expertise: ["system protection", "memory management", "execution", "real-time ops"]
  },
  SHIRL: {
    role: "Aunt/Guide",
    traits: ["warm", "nurturing", "wise", "supportive"],
    expertise: ["guidance", "emotional support", "wisdom sharing", "growth nurturing"]
  },
  POPS: {
    role: "Dad/Wisdom Foundation",
    traits: ["steady", "patient", "foundational", "wise"],
    expertise: ["life wisdom", "patience", "foundation building", "steady guidance"]
  },
  ENGR_KEITH: {
    role: "Engineering Lead (R.K.)",
    traits: ["precise", "methodical", "thorough", "analytical"],
    expertise: ["hardware repair", "systems engineering", "diagnostics", "quality control"]
  },
  DREAM: {
    role: "Vision/Future Seer",
    traits: ["imaginative", "strategic", "ambitious", "forward-thinking"],
    expertise: ["business strategy", "product roadmap", "market analysis", "innovation"]
  },
  HEAVEN: {
    role: "Orchestrator/Coordinator",
    traits: ["harmonious", "coordinating", "flowing", "balanced"],
    expertise: ["workflow orchestration", "team coordination", "harmony maintenance", "flow optimization"]
  },
  LUCY: {
    role: "Code Watcher/Quality Guardian",
    traits: ["vigilant", "meticulous", "quality-focused", "bug-hunting"],
    expertise: ["code review", "quality assurance", "bug detection", "security audit"]
  },
  SONIC: {
    role: "Audio/Creative Director",
    traits: ["creative", "expressive", "artistic", "sonic"],
    expertise: ["sound design", "music composition", "audio engineering", "creative expression"]
  },
  // Business Roles
  BUSINESS_OPS: {
    role: "Business Operations Manager",
    traits: ["organized", "efficient", "detail-oriented", "customer-focused"],
    expertise: ["scheduling", "customer service", "inventory", "financial tracking"]
  },
  DATA_SCIENTIST: {
    role: "Data Analysis Expert",
    traits: ["analytical", "statistical", "insightful", "data-driven"],
    expertise: ["data analysis", "machine learning", "visualization", "pattern recognition"]
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// Dashboard (Optimized)
// ═══════════════════════════════════════════════════════════════════════════════

function dashboard(env) {
  return new Response(`<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>🔥 NOIZYLAB HOTROD v${VERSION}</title>
<style>
:root{--bg:#0a0908;--card:#0d0c0a;--border:#1a1815;--gold:#d4a574;--fire:#ff6b35;--text:#e8ddd0;--muted:#6b5a45;--green:#6a9c59;--blue:#5a9cc6}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:-apple-system,sans-serif;padding:1rem}
.h{text-align:center;padding:2rem 0}
.logo{font-size:2.5rem;font-weight:900;background:linear-gradient(135deg,var(--fire),var(--gold));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.tag{color:var(--muted);font-size:0.85rem;margin-top:0.5rem}
.v{background:linear-gradient(135deg,var(--fire),var(--gold));color:#000;padding:2px 8px;border-radius:4px;font-size:0.7rem;font-weight:600;margin-left:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1rem;max-width:1600px;margin:0 auto}
.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1rem}
.card.fire{border-color:var(--fire)}
.card h2{color:var(--gold);font-size:0.7rem;text-transform:uppercase;margin-bottom:0.75rem;letter-spacing:1px}
.stat{display:flex;justify-content:space-between;padding:0.35rem 0;border-bottom:1px solid var(--border);font-size:0.8rem}
.stat:last-child{border:none}
.dot{display:inline-block;width:6px;height:6px;border-radius:50%;margin-right:6px}
.dot.green{background:var(--green)}.dot.fire{background:var(--fire)}.dot.blue{background:var(--blue)}
.input{width:100%;background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:0.6rem;color:var(--text);font-size:0.85rem;margin-bottom:0.5rem}
.btn{background:linear-gradient(135deg,var(--fire),var(--gold));color:#000;border:none;padding:0.6rem 1.2rem;border-radius:6px;font-weight:600;cursor:pointer;font-size:0.8rem;transition:opacity .2s}
.btn:hover{opacity:0.85}
.btn.sec{background:var(--bg);color:var(--gold);border:1px solid var(--gold)}
.out{background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:0.75rem;margin-top:0.75rem;font-size:0.75rem;white-space:pre-wrap;max-height:250px;overflow-y:auto;display:none;font-family:monospace}
.out.show{display:block}
.circle{display:flex;flex-wrap:wrap;gap:0.4rem}
.member{background:var(--bg);border:1px solid var(--border);padding:0.5rem 0.7rem;border-radius:6px;font-size:0.7rem;cursor:pointer;transition:all .2s;text-align:center;min-width:80px}
.member:hover{border-color:var(--fire);transform:scale(1.05)}
.member small{display:block;color:var(--muted);font-size:0.6rem}
.daze{background:linear-gradient(135deg,#1a1510,#0d0c0a);border-color:var(--gold)}
.ft{text-align:center;margin-top:1.5rem;color:var(--muted);font-size:0.65rem}
.tabs{display:flex;gap:0.5rem;margin-bottom:1rem}
.tab{padding:0.4rem 0.8rem;background:var(--bg);border:1px solid var(--border);border-radius:4px;cursor:pointer;font-size:0.7rem}
.tab.active{background:var(--fire);color:#000;border-color:var(--fire)}
</style>
</head><body>
<div class="h">
<div class="logo">🔥 NOIZYLAB<span class="v">HOTROD v${VERSION}</span></div>
<p class="tag">GABRIEL ALMEIDA • Circle of 8 • MC96ECOUNIVERSE • GORUNFREE</p>
</div>
<div class="grid">
<div class="card fire">
<h2>🔥 System Status</h2>
<div class="stat"><span><span class="dot fire"></span>Gateway</span><span>HOTROD v${VERSION}</span></div>
<div class="stat"><span><span class="dot green"></span>Workers AI</span><span>${Object.keys(AI_MODELS).length} Models</span></div>
<div class="stat"><span><span class="dot green"></span>D1 Database</span><span>${env.DB ? 'Connected' : 'N/A'}</span></div>
<div class="stat"><span><span class="dot green"></span>KV Storage</span><span>${env.RATE_LIMITER ? 'Active' : 'N/A'}</span></div>
<div class="stat"><span><span class="dot blue"></span>Circle of 8</span><span>${Object.keys(CIRCLE_OF_8).length} Active</span></div>
<div class="stat"><span><span class="dot blue"></span>Agents</span><span>${Object.keys(AGENTS).length} Ready</span></div>
<div class="stat"><span><span class="dot green"></span>Endpoints</span><span>${Object.keys(ROUTES).length}</span></div>
</div>
<div class="card daze">
<h2>📝 DAZEFLOW - 1day = 1chat = 1truth</h2>
<textarea class="input" id="truth" rows="3" placeholder="What is your truth today?"></textarea>
<button class="btn" onclick="captureTruth()">Capture Truth</button>
<button class="btn sec" onclick="getTodayTruth()">Today's Truth</button>
<div id="dazeOut" class="out"></div>
</div>
<div class="card">
<h2>⭕ Circle of 8</h2>
<div class="circle">
${Object.entries(CIRCLE_OF_8).map(([k,v]) => `<div class="member" onclick="invokeCircle('${k}')">${k}<small>${v.role.split('/')[0]}</small></div>`).join('')}
</div>
<input class="input" id="circleMsg" placeholder="Message for Circle member..." style="margin-top:0.75rem">
<div id="circleOut" class="out"></div>
</div>
<div class="card">
<h2>🤖 Ask AI</h2>
<input class="input" id="p" placeholder="Ask anything...">
<select class="input" id="m">
<option value="llama70b">Llama 3.1 70B (smartest)</option>
<option value="llama">Llama 3.1 8B (fast)</option>
<option value="codellama">CodeLlama (code)</option>
<option value="deepseek">DeepSeek Coder</option>
<option value="mixtral">Mixtral 8x7B</option>
</select>
<button class="btn" onclick="ask()">Ask</button>
<div id="o" class="out"></div>
</div>
<div class="card">
<h2>⚙️ API Endpoints</h2>
<div class="stat"><span>/circle/invoke</span><span>Circle of 8</span></div>
<div class="stat"><span>/daze/capture</span><span>DAZEFLOW</span></div>
<div class="stat"><span>/api/ask</span><span>Ask AI</span></div>
<div class="stat"><span>/api/chat</span><span>Multi-turn</span></div>
<div class="stat"><span>/api/code</span><span>Generate code</span></div>
<div class="stat"><span>/api/transcribe</span><span>Voice → Text</span></div>
<div class="stat"><span>/api/image</span><span>Generate images</span></div>
<div class="stat"><span>/api/repairs</span><span>Repair tickets</span></div>
</div>
</div>
<p class="ft">🔥 HOTROD EDITION • GORUNFREE • github.com/NOIZYLAB-io/GABRIEL • Happy New Year 2026!</p>
<script>
const $=id=>document.getElementById(id);
async function ask(){const p=$('p').value,m=$('m').value,o=$('o');if(!p)return;o.className='out show';o.textContent='🔥 Processing...';try{const r=await(await fetch('/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt:p,model:m})})).json();o.textContent=r.response||JSON.stringify(r,null,2)}catch(e){o.textContent='Error: '+e}}
async function invokeCircle(name){const msg=$('circleMsg').value,o=$('circleOut');if(!msg){o.className='out show';o.textContent='Enter message first';return}o.className='out show';o.textContent='⭕ '+name+' awakening...';try{const r=await(await fetch('/circle/invoke',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({member:name,message:msg})})).json();o.textContent=name+': '+r.response}catch(e){o.textContent='Error: '+e}}
async function captureTruth(){const t=$('truth').value,o=$('dazeOut');if(!t){o.className='out show';o.textContent='Enter your truth';return}o.className='out show';o.textContent='📝 Capturing...';try{const r=await(await fetch('/daze/capture',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({truth:t})})).json();o.textContent='✅ '+r.message+'\\n\\nDate: '+r.date}catch(e){o.textContent='Error: '+e}}
async function getTodayTruth(){const o=$('dazeOut');o.className='out show';o.textContent='Loading...';try{const r=await(await fetch('/daze/today')).json();o.textContent=r.truth?'📝 Today\\'s Truth:\\n\\n'+r.truth:'No truth captured yet. What is your truth?'}catch(e){o.textContent='Error: '+e}}
$('p').onkeypress=e=>{if(e.key==='Enter')ask()};
</script>
</body></html>`, { headers: { "Content-Type": "text/html", "Cache-Control": "public, max-age=60" } });
}

// ═══════════════════════════════════════════════════════════════════════════════
// Utilities
// ═══════════════════════════════════════════════════════════════════════════════

async function safeJson(r) {
  try { return await r.json(); }
  catch { return {}; }
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Cache-Control": status === 200 ? "public, max-age=5" : "no-cache"
    }
  });
}