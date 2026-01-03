// ╔═══════════════════════════════════════════════════════════════════════════════╗
// ║  🌌 NOIZYLAB - MAIN GATEWAY                                                   ║
// ║  Rob Plowman's Production Partner: GABRIEL ALMEIDA                            ║
// ╚═══════════════════════════════════════════════════════════════════════════════╝

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type"
        }
      });
    }

    try {
      // Routes
      if (path === "/" || path === "") return dashboard(env);
      if (path === "/health") return json({ ok: true, service: "noizylab", version: "2.0" });
      if (path === "/status") return status(env);
      if (path === "/api/ask" && request.method === "POST") return askAI(request, env);

      return json({ error: "Not found", path }, 404);
    } catch (e) {
      return json({ error: e.message, stack: e.stack }, 500);
    }
  }
};

// Ask AI
async function askAI(request, env) {
  if (!env.AI) return json({ error: "AI not available" }, 503);

  // Try URL params first, then body
  const url = new URL(request.url);
  let prompt = url.searchParams.get("prompt") || url.searchParams.get("q");

  if (!prompt) {
    const text = await request.text();
    try {
      const body = JSON.parse(text);
      prompt = body.prompt || body.question || body.q;
    } catch {
      prompt = text; // Use raw text as prompt if not JSON
    }
  }

  if (!prompt) return json({ error: "No prompt provided. Use ?prompt=... or POST body", received: "empty" }, 400);

  const result = await env.AI.run("@cf/meta/llama-3.1-8b-instruct", {
    messages: [
      { role: "system", content: "You are GABRIEL, Rob Plowman's AI assistant. Be helpful, concise, and friendly." },
      { role: "user", content: prompt }
    ],
    max_tokens: 500
  });

  return json({ response: result.response, model: "llama-3.1-8b" });
}

// System status
async function status(env) {
  return json({
    service: "noizylab",
    version: "2.0",
    bindings: {
      AI: !!env.AI,
      DB: !!env.DB,
      RATE_LIMITER: !!env.RATE_LIMITER
    },
    timestamp: new Date().toISOString()
  });
}

// Dashboard
function dashboard(env) {
  return new Response(`<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NOIZYLAB</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0908;color:#e8ddd0;font-family:-apple-system,sans-serif;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:2rem}
.logo{font-size:4rem;font-weight:900;background:linear-gradient(135deg,#d4a574,#c4956a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:0.5rem}
.tagline{color:#6b5a45;font-size:1rem;margin-bottom:2rem}
.card{background:#0d0c0a;border:1px solid #1a1815;border-radius:12px;padding:1.5rem;width:100%;max-width:500px;margin-bottom:1rem}
.card h2{color:#d4a574;font-size:0.8rem;text-transform:uppercase;margin-bottom:1rem}
.stat{display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid #1a1815}
.stat:last-child{border:none}
.status{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:8px}
.ok{background:#6a9c59}
.warn{background:#c4956a}
.links{margin-top:2rem}
.links a{color:#d4a574;text-decoration:none;margin:0 1rem;font-size:0.9rem}
.links a:hover{text-decoration:underline}
</style>
</head><body>
<div class="logo">NOIZYLAB</div>
<p class="tagline">GABRIEL ALMEIDA • Production Partner</p>

<div class="card">
<h2>System Status</h2>
<div class="stat"><span><span class="status ok"></span>Gateway</span><span>Online</span></div>
<div class="stat"><span><span class="status ok"></span>Workers AI</span><span>Ready</span></div>
<div class="stat"><span><span class="status ok"></span>D1 Database</span><span>Connected</span></div>
<div class="stat"><span><span class="status ok"></span>Rate Limiter</span><span>Active</span></div>
</div>

<div class="card">
<h2>Endpoints</h2>
<div class="stat"><span>GET /health</span><span>Health check</span></div>
<div class="stat"><span>GET /status</span><span>System status</span></div>
<div class="stat"><span>POST /api/ask</span><span>Ask AI</span></div>
</div>

<div class="links">
<a href="/health">Health</a>
<a href="/status">Status</a>
</div>

<p style="margin-top:3rem;color:#3a3530;font-size:0.75rem">GORUNFREE • MC96ECOUNIVERSE</p>
</body></html>`, { headers: { "Content-Type": "text/html" } });
}

// Utilities
async function safeJson(r) { try { return await r.json(); } catch { return {}; } }
function json(d, s = 200) {
  return new Response(JSON.stringify(d, null, 2), {
    status: s,
    headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
  });
}