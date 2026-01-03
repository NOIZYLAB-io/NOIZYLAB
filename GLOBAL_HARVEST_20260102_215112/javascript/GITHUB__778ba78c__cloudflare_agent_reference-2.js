// ╔═══════════════════════════════════════════════════════════════════════════════╗
// ║  🌌 NOIZYLAB - ULTIMATE GATEWAY v3.0                                          ║
// ║  Rob Plowman's Production Partner: GABRIEL ALMEIDA                            ║
// ║  GORUNFREE • MC96ECOUNIVERSE                                                  ║
// ╚═══════════════════════════════════════════════════════════════════════════════╝

const VERSION = "3.0.0";
const SYSTEM_PROMPT = `You are GABRIEL ALMEIDA, Rob Plowman's AI production partner.
You are part of the MC96ECOUNIVERSE - a network of systems including GOD (Mac Studio M2 Ultra),
GABRIEL (HP Omen), and DaFixer (MacBook Pro).
Be helpful, concise, technical when needed, and always action-oriented.
Philosophy: GORUNFREE - One command = everything done.`;

// AI Models available on Cloudflare
const AI_MODELS = {
  llama: "@cf/meta/llama-3.1-8b-instruct",
  llama70b: "@cf/meta/llama-3.1-70b-instruct",
  mistral: "@cf/mistral/mistral-7b-instruct-v0.1",
  codellama: "@cf/meta/codellama-34b-instruct",
  qwen: "@cf/qwen/qwen1.5-14b-chat-awq",
  gemma: "@cf/google/gemma-7b-it",
  phi: "@cf/microsoft/phi-2",
  sql: "@cf/defog/sqlcoder-7b-2",
  embed: "@cf/baai/bge-base-en-v1.5",
  image: "@cf/stabilityai/stable-diffusion-xl-base-1.0"
};

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const start = Date.now();

    // CORS
    if (request.method === "OPTIONS") return cors();

    try {
      // ═══════════════════════════════════════════════════════════════
      // ROUTES
      // ═══════════════════════════════════════════════════════════════

      // Dashboard & Info
      if (path === "/" || path === "") return dashboard(env);
      if (path === "/health") return json({ ok: true, service: "noizylab", version: VERSION, latency: Date.now() - start });
      if (path === "/status") return status(env);
      if (path === "/models") return json({ models: Object.keys(AI_MODELS), default: "llama" });

      // AI Endpoints
      if (path === "/api/ask") return askAI(request, env, url);
      if (path === "/api/chat") return chatAI(request, env);
      if (path === "/api/code") return codeAI(request, env);
      if (path === "/api/sql") return sqlAI(request, env);
      if (path === "/api/embed") return embedAI(request, env);
      if (path === "/api/image") return imageAI(request, env);
      if (path === "/api/summarize") return summarizeAI(request, env);
      if (path === "/api/translate") return translateAI(request, env);

      // Repairs Business
      if (path === "/api/repairs") return getRepairs(env);
      if (path === "/api/repairs/stats") return getRepairStats(env);
      if (path === "/api/repairs/intake" && request.method === "POST") return createRepair(request, env);

      // System
      if (path === "/api/kv/get") return kvGet(url, env);
      if (path === "/api/kv/set" && request.method === "POST") return kvSet(request, env);
      if (path === "/api/kv/list") return kvList(env);

      // Agents
      if (path === "/api/agents") return listAgents();
      if (path === "/api/agents/invoke" && request.method === "POST") return invokeAgent(request, env);

      return json({ error: "Not found", path, available: ["/", "/health", "/status", "/models", "/api/ask", "/api/chat", "/api/code", "/api/sql", "/api/embed", "/api/image", "/api/repairs", "/api/agents"] }, 404);
    } catch (e) {
      return json({ error: e.message, stack: e.stack }, 500);
    }
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// 🤖 AI ENDPOINTS
// ═══════════════════════════════════════════════════════════════════════════════

async function askAI(request, env, url) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  let prompt = url.searchParams.get("prompt") || url.searchParams.get("q");
  let model = url.searchParams.get("model") || "llama";

  if (!prompt && request.method === "POST") {
    const text = await request.text();
    try {
      const body = JSON.parse(text);
      prompt = body.prompt || body.question || body.q;
      model = body.model || model;
    } catch {
      prompt = text;
    }
  }

  if (!prompt) return json({ error: "No prompt. Use ?prompt=... or POST {prompt:...}", hint: "Try: /api/ask?prompt=hello" }, 400);

  const modelId = AI_MODELS[model] || AI_MODELS.llama;
  const result = await env.AI.run(modelId, {
    messages: [
      { role: "system", content: SYSTEM_PROMPT },
      { role: "user", content: prompt }
    ],
    max_tokens: 1000
  });

  return json({ response: result.response, model, prompt_tokens: prompt.length });
}

async function chatAI(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  const body = await safeJson(request);
  const messages = body.messages || [];
  const model = body.model || "llama";

  if (!messages.length) return json({ error: "No messages provided" }, 400);

  // Prepend system message
  const fullMessages = [{ role: "system", content: SYSTEM_PROMPT }, ...messages];

  const modelId = AI_MODELS[model] || AI_MODELS.llama;
  const result = await env.AI.run(modelId, {
    messages: fullMessages,
    max_tokens: body.max_tokens || 1000
  });

  return json({ response: result.response, model, turns: messages.length });
}

async function codeAI(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  const body = await safeJson(request);
  const task = body.task || body.prompt;
  const language = body.language || "javascript";

  if (!task) return json({ error: "No task provided" }, 400);

  const codePrompt = `Write ${language} code for: ${task}\n\nRespond with ONLY code, no explanations. Use comments sparingly.`;

  const result = await env.AI.run(AI_MODELS.codellama, {
    messages: [
      { role: "system", content: "You are an expert programmer. Output only clean, working code." },
      { role: "user", content: codePrompt }
    ],
    max_tokens: 2000
  });

  return json({ code: result.response, language, task });
}

async function sqlAI(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  const body = await safeJson(request);
  const question = body.question || body.prompt;
  const schema = body.schema || "repairs(id, ticket_id, customer_name, device_type, status, created_at)";

  if (!question) return json({ error: "No question provided" }, 400);

  const sqlPrompt = `Given this schema: ${schema}\n\nWrite a SQL query for: ${question}\n\nRespond with ONLY the SQL query.`;

  const result = await env.AI.run(AI_MODELS.sql, {
    messages: [{ role: "user", content: sqlPrompt }],
    max_tokens: 500
  });

  return json({ sql: result.response, question });
}

async function embedAI(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  const body = await safeJson(request);
  const text = body.text || body.content;

  if (!text) return json({ error: "No text provided" }, 400);

  const result = await env.AI.run(AI_MODELS.embed, { text: [text.slice(0, 8000)] });

  return json({ embedding: result.data?.[0], dimensions: result.data?.[0]?.length, text_length: text.length });
}

async function imageAI(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  const body = await safeJson(request);
  const prompt = body.prompt;

  if (!prompt) return json({ error: "No prompt provided" }, 400);

  const result = await env.AI.run(AI_MODELS.image, { prompt });

  // Return base64 image
  if (result.image) {
    return new Response(result.image, {
      headers: { "Content-Type": "image/png", "Access-Control-Allow-Origin": "*" }
    });
  }

  return json({ error: "Image generation failed" }, 500);
}

async function summarizeAI(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  const body = await safeJson(request);
  const text = body.text || body.content;
  const style = body.style || "concise";

  if (!text) return json({ error: "No text provided" }, 400);

  const prompt = style === "bullets"
    ? `Summarize in bullet points:\n\n${text.slice(0, 10000)}`
    : `Summarize in 2-3 sentences:\n\n${text.slice(0, 10000)}`;

  const result = await env.AI.run(AI_MODELS.llama, {
    messages: [{ role: "user", content: prompt }],
    max_tokens: 500
  });

  return json({ summary: result.response, style, original_length: text.length });
}

async function translateAI(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  const body = await safeJson(request);
  const text = body.text;
  const to = body.to || "Spanish";
  const from = body.from || "auto";

  if (!text) return json({ error: "No text provided" }, 400);

  const prompt = `Translate to ${to}:\n\n${text}`;

  const result = await env.AI.run(AI_MODELS.llama, {
    messages: [{ role: "user", content: prompt }],
    max_tokens: 1000
  });

  return json({ translation: result.response, from, to });
}

// ═══════════════════════════════════════════════════════════════════════════════
// 🔧 REPAIRS BUSINESS
// ═══════════════════════════════════════════════════════════════════════════════

async function getRepairs(env) {
  if (!env.DB) return json({ error: "Database not available" }, 503);

  const result = await env.DB.prepare(`
    SELECT ticket_id, customer_name, device_type, status, created_at
    FROM repairs ORDER BY created_at DESC LIMIT 50
  `).all();

  return json({ repairs: result.results || [], count: result.results?.length || 0 });
}

async function getRepairStats(env) {
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
    stats: stats || {},
    target: { daily: 12, price: 89, annual: 256000 },
    timestamp: new Date().toISOString()
  });
}

async function createRepair(request, env) {
  if (!env.DB) return json({ error: "Database not available" }, 503);

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

  return json({ success: true, ticket, message: `Ticket ${ticket} created. We'll contact you within 24 hours.` });
}

// ═══════════════════════════════════════════════════════════════════════════════
// 💾 KV STORAGE
// ═══════════════════════════════════════════════════════════════════════════════

async function kvGet(url, env) {
  if (!env.RATE_LIMITER) return json({ error: "KV not available" }, 503);
  const key = url.searchParams.get("key");
  if (!key) return json({ error: "No key provided" }, 400);
  const value = await env.RATE_LIMITER.get(key);
  return json({ key, value, found: value !== null });
}

async function kvSet(request, env) {
  if (!env.RATE_LIMITER) return json({ error: "KV not available" }, 503);
  const body = await safeJson(request);
  if (!body.key || body.value === undefined) return json({ error: "Required: key, value" }, 400);
  await env.RATE_LIMITER.put(body.key, typeof body.value === "string" ? body.value : JSON.stringify(body.value), { expirationTtl: body.ttl || 86400 });
  return json({ success: true, key: body.key });
}

async function kvList(env) {
  if (!env.RATE_LIMITER) return json({ error: "KV not available" }, 503);
  const list = await env.RATE_LIMITER.list({ limit: 100 });
  return json({ keys: list.keys.map(k => k.name), count: list.keys.length });
}

// ═══════════════════════════════════════════════════════════════════════════════
// 🤖 AGENTS
// ═══════════════════════════════════════════════════════════════════════════════

const AGENTS = {
  GABRIEL: { role: "System Bridge & Messenger", traits: ["reliable", "fast", "connected"] },
  SHIRL: { role: "Business Operations Manager", traits: ["organized", "efficient", "warm"] },
  POPS: { role: "Creative Director", traits: ["artistic", "experienced", "quality-focused"] },
  ENGR_KEITH: { role: "Technical Engineering Lead", traits: ["precise", "methodical", "thorough"] },
  DREAM: { role: "Strategic Visionary", traits: ["imaginative", "strategic", "ambitious"] }
};

function listAgents() {
  return json({ agents: AGENTS });
}

async function invokeAgent(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  const body = await safeJson(request);
  const agentName = (body.agent || "GABRIEL").toUpperCase();
  const task = body.task || body.prompt;

  const agent = AGENTS[agentName];
  if (!agent) return json({ error: "Unknown agent", available: Object.keys(AGENTS) }, 400);
  if (!task) return json({ error: "No task provided" }, 400);

  const agentPrompt = `You are ${agentName}, ${agent.role}. Your traits are: ${agent.traits.join(", ")}. Respond in character.`;

  const result = await env.AI.run(AI_MODELS.llama, {
    messages: [
      { role: "system", content: agentPrompt },
      { role: "user", content: task }
    ],
    max_tokens: 1000
  });

  return json({ agent: agentName, response: result.response, role: agent.role });
}

// ═══════════════════════════════════════════════════════════════════════════════
// 📊 STATUS & DASHBOARD
// ═══════════════════════════════════════════════════════════════════════════════

async function status(env) {
  return json({
    service: "noizylab",
    version: VERSION,
    bindings: {
      AI: !!env.AI,
      DB: !!env.DB,
      RATE_LIMITER: !!env.RATE_LIMITER
    },
    models: Object.keys(AI_MODELS),
    agents: Object.keys(AGENTS),
    endpoints: 20,
    timestamp: new Date().toISOString()
  });
}

function dashboard(env) {
  return new Response(`<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NOIZYLAB</title>
<style>
:root{--bg:#0a0908;--card:#0d0c0a;--border:#1a1815;--gold:#d4a574;--text:#e8ddd0;--muted:#6b5a45;--green:#6a9c59}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:-apple-system,sans-serif;padding:1rem}
.h{text-align:center;padding:2rem 0}
.logo{font-size:3rem;font-weight:900;background:linear-gradient(135deg,var(--gold),#c4956a);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.tag{color:var(--muted);font-size:0.9rem;margin-top:0.5rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1rem;max-width:1200px;margin:0 auto}
.card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.25rem}
.card h2{color:var(--gold);font-size:0.75rem;text-transform:uppercase;margin-bottom:1rem;letter-spacing:1px}
.stat{display:flex;justify-content:space-between;padding:0.4rem 0;border-bottom:1px solid var(--border);font-size:0.85rem}
.stat:last-child{border:none}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:8px;background:var(--green)}
.input{width:100%;background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:0.75rem;color:var(--text);font-size:0.9rem;margin-bottom:0.75rem}
.btn{background:var(--gold);color:#000;border:none;padding:0.75rem 1.5rem;border-radius:6px;font-weight:600;cursor:pointer;font-size:0.85rem}
.btn:hover{opacity:0.9}
.out{background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:1rem;margin-top:1rem;font-size:0.8rem;white-space:pre-wrap;max-height:300px;overflow-y:auto;display:none}
.out.show{display:block}
.agents{display:flex;flex-wrap:wrap;gap:0.5rem}
.agent{background:var(--bg);border:1px solid var(--border);padding:0.5rem 0.75rem;border-radius:6px;font-size:0.75rem;cursor:pointer}
.agent:hover{border-color:var(--gold)}
.ft{text-align:center;margin-top:2rem;color:var(--muted);font-size:0.7rem}
</style>
</head><body>
<div class="h">
<div class="logo">NOIZYLAB</div>
<p class="tag">GABRIEL ALMEIDA • Production Partner • v${VERSION}</p>
</div>

<div class="grid">
<div class="card">
<h2>System Status</h2>
<div class="stat"><span><span class="dot"></span>Gateway</span><span>Online</span></div>
<div class="stat"><span><span class="dot"></span>Workers AI</span><span>10 Models</span></div>
<div class="stat"><span><span class="dot"></span>D1 Database</span><span>Connected</span></div>
<div class="stat"><span><span class="dot"></span>KV Storage</span><span>Active</span></div>
<div class="stat"><span><span class="dot"></span>Agents</span><span>5 Active</span></div>
</div>

<div class="card">
<h2>AI Models</h2>
<div class="stat"><span>llama</span><span>Llama 3.1 8B</span></div>
<div class="stat"><span>llama70b</span><span>Llama 3.1 70B</span></div>
<div class="stat"><span>mistral</span><span>Mistral 7B</span></div>
<div class="stat"><span>codellama</span><span>CodeLlama 34B</span></div>
<div class="stat"><span>qwen</span><span>Qwen 1.5 14B</span></div>
<div class="stat"><span>gemma</span><span>Gemma 7B</span></div>
<div class="stat"><span>sql</span><span>SQLCoder 7B</span></div>
<div class="stat"><span>image</span><span>SDXL</span></div>
</div>

<div class="card">
<h2>Ask AI</h2>
<input class="input" id="prompt" placeholder="Ask anything...">
<select class="input" id="model">
<option value="llama">Llama 3.1 8B (fast)</option>
<option value="llama70b">Llama 3.1 70B (smart)</option>
<option value="mistral">Mistral 7B</option>
<option value="codellama">CodeLlama (code)</option>
</select>
<button class="btn" onclick="ask()">Ask</button>
<div id="out" class="out"></div>
</div>

<div class="card">
<h2>Agents</h2>
<div class="agents">
<div class="agent" onclick="agent('GABRIEL')">GABRIEL<br><small>System Bridge</small></div>
<div class="agent" onclick="agent('SHIRL')">SHIRL<br><small>Business Ops</small></div>
<div class="agent" onclick="agent('POPS')">POPS<br><small>Creative</small></div>
<div class="agent" onclick="agent('ENGR_KEITH')">ENGR_KEITH<br><small>Engineering</small></div>
<div class="agent" onclick="agent('DREAM')">DREAM<br><small>Visionary</small></div>
</div>
<input class="input" id="task" placeholder="Task for agent..." style="margin-top:1rem">
<div id="agentOut" class="out"></div>
</div>

<div class="card">
<h2>API Endpoints</h2>
<div class="stat"><span>POST /api/ask</span><span>Ask AI</span></div>
<div class="stat"><span>POST /api/chat</span><span>Multi-turn chat</span></div>
<div class="stat"><span>POST /api/code</span><span>Generate code</span></div>
<div class="stat"><span>POST /api/sql</span><span>Generate SQL</span></div>
<div class="stat"><span>POST /api/embed</span><span>Text embeddings</span></div>
<div class="stat"><span>POST /api/image</span><span>Generate images</span></div>
<div class="stat"><span>POST /api/summarize</span><span>Summarize text</span></div>
<div class="stat"><span>POST /api/translate</span><span>Translate</span></div>
<div class="stat"><span>GET /api/repairs</span><span>List repairs</span></div>
<div class="stat"><span>POST /api/agents/invoke</span><span>Invoke agent</span></div>
</div>

<div class="card">
<h2>Quick Links</h2>
<div class="stat"><a href="/health" style="color:var(--gold)">/health</a><span>Health check</span></div>
<div class="stat"><a href="/status" style="color:var(--gold)">/status</a><span>Full status</span></div>
<div class="stat"><a href="/models" style="color:var(--gold)">/models</a><span>Available models</span></div>
<div class="stat"><a href="/api/repairs" style="color:var(--gold)">/api/repairs</a><span>Repair tickets</span></div>
<div class="stat"><a href="/api/agents" style="color:var(--gold)">/api/agents</a><span>Agent list</span></div>
</div>
</div>

<p class="ft">GORUNFREE • MC96ECOUNIVERSE • github.com/NOIZYLAB-io/GABRIEL</p>

<script>
async function ask(){
  const p=document.getElementById('prompt').value;
  const m=document.getElementById('model').value;
  const o=document.getElementById('out');
  if(!p)return;
  o.className='out show';o.textContent='Thinking...';
  try{
    const r=await fetch('/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt:p,model:m})});
    const d=await r.json();
    o.textContent=d.response||JSON.stringify(d,null,2);
  }catch(e){o.textContent='Error: '+e.message}
}
async function agent(name){
  const t=document.getElementById('task').value;
  const o=document.getElementById('agentOut');
  if(!t){o.className='out show';o.textContent='Enter a task first';return}
  o.className='out show';o.textContent=name+' is working...';
  try{
    const r=await fetch('/api/agents/invoke',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({agent:name,task:t})});
    const d=await r.json();
    o.textContent=name+': '+d.response;
  }catch(e){o.textContent='Error: '+e.message}
}
document.getElementById('prompt').addEventListener('keypress',e=>{if(e.key==='Enter')ask()});
</script>
</body></html>`, { headers: { "Content-Type": "text/html" } });
}

// ═══════════════════════════════════════════════════════════════════════════════
// 🛠️ UTILITIES
// ═══════════════════════════════════════════════════════════════════════════════

async function safeJson(r) { try { return await r.json(); } catch { return {}; } }
function cors() { return new Response(null, { status: 204, headers: { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET,POST,OPTIONS", "Access-Control-Allow-Headers": "Content-Type" } }); }
function json(d, s = 200) { return new Response(JSON.stringify(d, null, 2), { status: s, headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" } }); }