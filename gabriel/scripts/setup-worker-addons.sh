#!/usr/bin/env bash
#═══════════════════════════════════════════════════════════════════════════════
# M2G Worker Add-Ons Installer
# Adds: Provider health checks, dashboard, model registry, budget alerts
#═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

VOICE=0
for a in "$@"; do [[ "$a" == "--speak" ]] && VOICE=1; done

say_() {
  [[ $VOICE -eq 1 ]] && command -v say >/dev/null 2>&1 && say "$1" || true
  printf ">> %s\n" "$1"
}

die() {
  echo "ERR: $*" >&2
  exit 1
}

# Portable sed in-place
sed_inplace() {
  if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "$@"
  else
    sed -i "$@"
  fi
}

#───────────────────────────────────────────────────────────────────────────────
# Validation
#───────────────────────────────────────────────────────────────────────────────
[[ -f wrangler.toml ]] || die "Run this inside your Worker project (wrangler.toml not found)"
[[ -f src/index.js ]] || die "src/index.js missing"

# Create util.js if it doesn't exist
if [[ ! -f src/util.js ]]; then
  say_ "Creating src/util.js"
  mkdir -p src
  cat > src/util.js <<'JS'
// M2G Utility Functions

export function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "content-type": "application/json" }
  });
}

export function errorResponse(message, status = 400) {
  return jsonResponse({ error: message }, status);
}
JS
fi

#───────────────────────────────────────────────────────────────────────────────
# Step 1: Update wrangler.toml
#───────────────────────────────────────────────────────────────────────────────
say_ "Adding Add-Ons vars to wrangler.toml"
if ! grep -q "WEBHOOK_URL" wrangler.toml; then
  cat >> wrangler.toml <<'TOML'

# ═══════════════════════════════════════════════════════════════
# M2G ADD-ONS CONFIGURATION
# ═══════════════════════════════════════════════════════════════
[vars]
# Slack/Discord webhook URL for budget alerts
WEBHOOK_URL = ""
# Daily spend threshold before alerting (USD)
ALERT_THRESHOLD_USD = "4"
# KV key for model registry storage
MODEL_REGISTRY_KEY = "model-registry"
# JWT group claim value for admin access
ADMIN_GROUP = "admins"
TOML
  say_ "✓ Added vars to wrangler.toml"
else
  say_ "⊘ wrangler.toml already configured"
fi

#───────────────────────────────────────────────────────────────────────────────
# Step 2: Create src/addons.js
#───────────────────────────────────────────────────────────────────────────────
say_ "Creating src/addons.js"
mkdir -p src
cat > src/addons.js <<'JS'
/**
 * M2G Worker Add-Ons
 * 
 * Features:
 * - Provider health checks (/health/providers)
 * - Live dashboard (/dash.html)
 * - Model registry with group-based access control
 * - Budget alerts via webhooks
 */

import { postWebhook, jsonResponse, errorResponse } from "./util.js";

// ═══════════════════════════════════════════════════════════════════════════════
// Route Handlers
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Handle add-on routes (call early in fetch before main logic)
 */
export async function handleAddonRoute(request, env) {
  const url = new URL(request.url);
  const path = url.pathname;
  const method = request.method;

  // ─────────────────────────────────────────────────────────────
  // GET /health/providers - Check upstream API status
  // ─────────────────────────────────────────────────────────────
  if (method === "GET" && path === "/health/providers") {
    const checks = {};
    
    const providers = [
      { name: "anthropic", url: env.ANTHROPIC_BASE || "https://api.anthropic.com/v1/messages" },
      { name: "openai", url: env.OPENAI_BASE || "https://api.openai.com/v1/chat/completions" },
    ];
    
    if (env.CUSTOM_BASE) {
      providers.push({ name: "custom", url: env.CUSTOM_BASE });
    }

    const tasks = providers.map(async ({ name, url }) => {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 5000);
        
        const resp = await fetch(url, { 
          method: "OPTIONS",
          signal: controller.signal 
        });
        clearTimeout(timeoutId);
        
        checks[name] = { ok: resp.ok, status: resp.status };
      } catch (e) {
        checks[name] = { 
          ok: false, 
          error: e.name === "AbortError" ? "timeout" : e.message 
        };
      }
    });

    await Promise.allSettled(tasks);
    return jsonResponse(checks);
  }

  // ─────────────────────────────────────────────────────────────
  // GET /dash.html - Live monitoring dashboard
  // ─────────────────────────────────────────────────────────────
  if (method === "GET" && path === "/dash.html") {
    const html = generateDashboardHTML();
    return new Response(html, {
      status: 200,
      headers: { "content-type": "text/html; charset=utf-8" }
    });
  }

  // Not an add-on route
  return null;
}

/**
 * Handle admin API routes (requires authentication)
 */
export async function handleAdminRoute(request, env, identity) {
  const url = new URL(request.url);
  const path = url.pathname;
  const method = request.method;

  // Check admin access for all /admin/* routes
  if (path.startsWith("/admin/")) {
    if (!isAdmin(identity, env)) {
      return errorResponse("admin_access_required", 403);
    }
  }

  // ─────────────────────────────────────────────────────────────
  // GET /admin/models - Retrieve model registry
  // ─────────────────────────────────────────────────────────────
  if (method === "GET" && path === "/admin/models") {
    const registry = await loadRegistry(env);
    return jsonResponse(registry);
  }

  // ─────────────────────────────────────────────────────────────
  // POST /admin/models - Update entire registry
  // ─────────────────────────────────────────────────────────────
  if (method === "POST" && path === "/admin/models") {
    try {
      const body = await request.json();
      if (typeof body !== "object" || body === null) {
        return errorResponse("invalid_format: expected object", 400);
      }
      await saveRegistry(env, body);
      return jsonResponse({ ok: true, message: "Registry updated" });
    } catch (e) {
      return errorResponse(`parse_error: ${e.message}`, 400);
    }
  }

  // ─────────────────────────────────────────────────────────────
  // PUT /admin/models/:group - Update single group
  // ─────────────────────────────────────────────────────────────
  if (method === "PUT" && path.startsWith("/admin/models/")) {
    const group = path.replace("/admin/models/", "");
    if (!group) return errorResponse("group_required", 400);

    try {
      const config = await request.json();
      const registry = await loadRegistry(env);
      registry[group] = config;
      await saveRegistry(env, registry);
      return jsonResponse({ ok: true, group, config });
    } catch (e) {
      return errorResponse(`parse_error: ${e.message}`, 400);
    }
  }

  // ─────────────────────────────────────────────────────────────
  // DELETE /admin/models/:group - Remove group
  // ─────────────────────────────────────────────────────────────
  if (method === "DELETE" && path.startsWith("/admin/models/")) {
    const group = path.replace("/admin/models/", "");
    if (!group) return errorResponse("group_required", 400);
    if (group === "default") return errorResponse("cannot_delete_default", 400);

    const registry = await loadRegistry(env);
    delete registry[group];
    await saveRegistry(env, registry);
    return jsonResponse({ ok: true, deleted: group });
  }

  return null;
}

// ═══════════════════════════════════════════════════════════════════════════════
// Model Registry
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Load model registry from KV
 */
export async function loadRegistry(env) {
  if (!env.USAGE_KV) return getDefaultRegistry();

  const key = env.MODEL_REGISTRY_KEY || "model-registry";
  const raw = await env.USAGE_KV.get(key);
  
  if (!raw) return getDefaultRegistry();
  
  try {
    return JSON.parse(raw);
  } catch {
    return getDefaultRegistry();
  }
}

/**
 * Save model registry to KV
 */
export async function saveRegistry(env, registry) {
  if (!env.USAGE_KV) return false;
  
  const key = env.MODEL_REGISTRY_KEY || "model-registry";
  await env.USAGE_KV.put(key, JSON.stringify(registry, null, 2), {
    expirationTtl: 60 * 60 * 24 * 365 // 1 year
  });
  return true;
}

/**
 * Default registry config
 */
function getDefaultRegistry() {
  return {
    default: {
      allow: ["claude-3-5-haiku-*", "gpt-4o-mini"],
      fallback: "claude-3-5-haiku-20241022"
    },
    premium: {
      allow: ["claude-3-5-sonnet-*", "claude-sonnet-4-*", "gpt-4o"],
      fallback: "claude-3-5-sonnet-20241022"
    },
    admins: {
      allow: ["*"],
      fallback: null
    }
  };
}

/**
 * Check if a model is allowed for the given identity
 */
export function isModelAllowed(model, identity, registry) {
  if (!model || !registry) return true;

  const groups = identity?.groups || [];
  const checkGroups = ["default", ...groups];

  for (const group of checkGroups) {
    const config = registry[group];
    if (!config?.allow) continue;

    for (const pattern of config.allow) {
      // Wildcard allows everything
      if (pattern === "*") return true;
      // Exact match
      if (pattern === model) return true;
      // Prefix wildcard (e.g., "claude-3-5-*")
      if (pattern.endsWith("*") && model.startsWith(pattern.slice(0, -1))) {
        return true;
      }
    }
  }

  return false;
}

/**
 * Get fallback model for identity
 */
export function getFallbackModel(identity, registry) {
  if (!registry) return null;

  const groups = identity?.groups || [];
  const checkGroups = [...groups, "default"];

  for (const group of checkGroups) {
    const fallback = registry[group]?.fallback;
    if (fallback) return fallback;
  }

  return null;
}

/**
 * Check if identity has admin privileges
 */
export function isAdmin(identity, env) {
  const adminGroup = env?.ADMIN_GROUP || "admins";
  const groups = identity?.groups || [];
  return groups.includes(adminGroup);
}

// ═══════════════════════════════════════════════════════════════════════════════
// Budget Alerts
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Post-response hook for budget tracking and alerts
 */
export async function postResponse(env, identity, provider, payloadSize, status) {
  const threshold = Number(env.ALERT_THRESHOLD_USD || 0);
  if (!threshold || !env.USAGE_KV || !env.WEBHOOK_URL) return;

  const day = new Date().toISOString().slice(0, 10);
  const user = identity?.email || identity?.sub || "anonymous";
  const key = `spend:${user}:${day}`;

  try {
    const current = Number(await env.USAGE_KV.get(key)) || 0;

    if (current >= threshold) {
      await postWebhook(env.WEBHOOK_URL, {
        text: `🚨 M2G Budget Alert`,
        blocks: [
          {
            type: "section",
            text: {
              type: "mrkdwn",
              text: [
                `*Budget Threshold Exceeded*`,
                `• User: \`${user}\``,
                `• Today's Spend: $${current.toFixed(2)}`,
                `• Threshold: $${threshold.toFixed(2)}`,
                `• Provider: ${provider}`,
                `• Status: ${status}`,
              ].join("\n")
            }
          }
        ]
      });
    }
  } catch (e) {
    console.error("Budget alert error:", e);
  }
}

// ═══════════════════════════════════════════════════════════════════════════════
// Dashboard HTML
// ═══════════════════════════════════════════════════════════════════════════════

function generateDashboardHTML() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>M2G Dashboard</title>
  <style>
    :root {
      --bg: #0b1020;
      --card: #141b34;
      --border: #1f284d;
      --text: #e6e9f2;
      --muted: #6b7280;
      --accent: #9fb3ff;
      --success: #4ade80;
      --warning: #fbbf24;
      --error: #f87171;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: ui-sans-serif, system-ui, -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      padding: 24px;
    }
    .header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
    }
    h1 { font-size: 24px; font-weight: 700; }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: 999px;
      background: var(--border);
      color: var(--accent);
      font-size: 12px;
    }
    .badge::before {
      content: "";
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--success);
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.4; }
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 16px;
    }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
    }
    .card h2 {
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--accent);
      margin-bottom: 16px;
    }
    .status-row {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 0;
      border-bottom: 1px solid var(--border);
    }
    .status-row:last-child { border-bottom: none; }
    .dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      flex-shrink: 0;
    }
    .dot.ok { background: var(--success); }
    .dot.err { background: var(--error); }
    .dot.warn { background: var(--warning); }
    .status-name { flex: 1; }
    .status-detail { color: var(--muted); font-size: 13px; }
    pre {
      font-family: ui-monospace, monospace;
      font-size: 12px;
      line-height: 1.6;
      white-space: pre-wrap;
      word-break: break-word;
      background: var(--bg);
      padding: 12px;
      border-radius: 8px;
      max-height: 300px;
      overflow: auto;
    }
    .btn {
      background: var(--border);
      color: var(--text);
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 14px;
      transition: all 0.2s;
    }
    .btn:hover { background: var(--accent); color: var(--bg); }
    .footer {
      margin-top: 32px;
      text-align: center;
      color: var(--muted);
      font-size: 12px;
    }
    .loading { color: var(--muted); }
  </style>
</head>
<body>
  <div class="header">
    <h1>M2G Dashboard</h1>
    <span class="badge">live</span>
    <button class="btn" onclick="refresh()">↻ Refresh</button>
  </div>

  <div class="grid">
    <div class="card">
      <h2>Provider Status</h2>
      <div id="providers" class="loading">Loading...</div>
    </div>
    
    <div class="card">
      <h2>System Health</h2>
      <div id="health" class="loading">Loading...</div>
    </div>
    
    <div class="card">
      <h2>Model Registry</h2>
      <pre id="registry">Loading...</pre>
    </div>
  </div>

  <div class="footer">
    M2G AI Proxy • Last updated: <span id="timestamp">-</span>
  </div>

  <script>
    async function loadProviders() {
      try {
        const data = await fetch('/health/providers').then(r => r.json());
        const el = document.getElementById('providers');
        el.innerHTML = Object.entries(data).map(([name, info]) => \`
          <div class="status-row">
            <span class="dot \${info.ok ? 'ok' : 'err'}"></span>
            <span class="status-name">\${name}</span>
            <span class="status-detail">\${info.ok ? 'OK (' + info.status + ')' : info.error || 'Error'}</span>
          </div>
        \`).join('');
      } catch (e) {
        document.getElementById('providers').innerHTML = '<div class="status-row"><span class="dot err"></span>Error: ' + e.message + '</div>';
      }
    }

    async function loadHealth() {
      try {
        const data = await fetch('/health').then(r => r.json());
        const el = document.getElementById('health');
        el.innerHTML = \`
          <div class="status-row">
            <span class="dot ok"></span>
            <span class="status-name">Worker</span>
            <span class="status-detail">\${data.version || 'running'}</span>
          </div>
          <div class="status-row">
            <span class="dot \${data.kv ? 'ok' : 'warn'}"></span>
            <span class="status-name">KV Storage</span>
            <span class="status-detail">\${data.kv ? 'connected' : 'not configured'}</span>
          </div>
          <div class="status-row">
            <span class="dot \${data.d1 ? 'ok' : 'warn'}"></span>
            <span class="status-name">D1 Database</span>
            <span class="status-detail">\${data.d1 ? 'connected' : 'not configured'}</span>
          </div>
        \`;
      } catch (e) {
        document.getElementById('health').innerHTML = '<div class="status-row"><span class="dot err"></span>Error loading health</div>';
      }
    }

    async function loadRegistry() {
      try {
        const data = await fetch('/admin/models').then(r => r.json());
        document.getElementById('registry').textContent = JSON.stringify(data, null, 2);
      } catch {
        document.getElementById('registry').textContent = '(Admin access required)';
      }
    }

    function refresh() {
      document.getElementById('timestamp').textContent = new Date().toLocaleString();
      loadProviders();
      loadHealth();
      loadRegistry();
    }

    refresh();
    setInterval(refresh, 15000);
  </script>
</body>
</html>`;
}
JS

say_ "✓ Created src/addons.js"

#───────────────────────────────────────────────────────────────────────────────
# Step 3: Update src/util.js
#───────────────────────────────────────────────────────────────────────────────
say_ "Patching src/util.js with helper functions"

if ! grep -q "export async function postWebhook" src/util.js; then
  cat >> src/util.js <<'JS'

/**
 * Post payload to webhook (Slack/Discord compatible)
 */
export async function postWebhook(url, payload) {
  if (!url) return;
  try {
    await fetch(url, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload)
    });
  } catch (_) {
    // Silently ignore webhook errors
  }
}
JS
  say_ "✓ Added postWebhook"
fi

if ! grep -q "export function jsonResponse" src/util.js; then
  cat >> src/util.js <<'JS'

/**
 * Create JSON response
 */
export function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "content-type": "application/json" }
  });
}

/**
 * Create error JSON response  
 */
export function errorResponse(message, status = 400) {
  return jsonResponse({ error: message }, status);
}
JS
  say_ "✓ Added jsonResponse/errorResponse"
fi

#───────────────────────────────────────────────────────────────────────────────
# Step 4: Create integration helper
#───────────────────────────────────────────────────────────────────────────────
say_ "Creating src/addons-integration.js"
cat > src/addons-integration.js <<'JS'
/**
 * M2G Add-Ons Integration Layer
 * 
 * Usage in src/index.js:
 * 
 *   import * as integration from "./addons-integration.js";
 * 
 *   export default {
 *     async fetch(request, env, ctx) {
 *       const identity = getIdentity(request);
 *       
 *       // 1. Handle add-on routes early
 *       const addonResp = await integration.handleRequest(request, env, identity);
 *       if (addonResp) return addonResp;
 *       
 *       // 2. Before relay - enforce model policy
 *       let body = await request.text();
 *       body = await integration.enforceModelPolicy(body, identity, env);
 *       
 *       // 3. Proxy to provider...
 *       const response = await fetch(providerUrl, { body, ... });
 *       
 *       // 4. After response - run hooks
 *       ctx.waitUntil(integration.postResponseHook(env, identity, provider, response.status));
 *       
 *       return response;
 *     }
 *   };
 */

import * as addons from "./addons.js";

/**
 * Handle add-on and admin routes
 */
export async function handleRequest(request, env, identity) {
  // Add-on routes (public)
  const addonResp = await addons.handleAddonRoute(request, env);
  if (addonResp) return addonResp;

  // Admin routes (authenticated)
  const adminResp = await addons.handleAdminRoute(request, env, identity);
  if (adminResp) return adminResp;

  return null;
}

/**
 * Enforce model access policy before relay
 */
export async function enforceModelPolicy(bodyStr, identity, env) {
  try {
    const body = JSON.parse(bodyStr);
    const model = body.model;
    
    if (!model) return bodyStr;

    // Admins bypass restrictions
    if (addons.isAdmin(identity, env)) return bodyStr;

    const registry = await addons.loadRegistry(env);
    
    if (!addons.isModelAllowed(model, identity, registry)) {
      const fallback = addons.getFallbackModel(identity, registry);
      
      if (fallback) {
        console.log(`[M2G] Model policy: ${model} → ${fallback} (user: ${identity?.email || "anon"})`);
        body.model = fallback;
        return JSON.stringify(body);
      }
      
      console.warn(`[M2G] Model ${model} not allowed, no fallback available`);
    }

    return bodyStr;
  } catch {
    return bodyStr;
  }
}

/**
 * Post-response hooks (budget alerts, logging)
 */
export async function postResponseHook(env, identity, provider, status) {
  await addons.postResponse(env, identity, provider, 0, status);
}

// Re-export for convenience
export { isAdmin, isModelAllowed, loadRegistry } from "./addons.js";
JS

say_ "✓ Created src/addons-integration.js"

#───────────────────────────────────────────────────────────────────────────────
# Step 5: Create GitHub Actions workflow
#───────────────────────────────────────────────────────────────────────────────
say_ "Creating GitHub Actions workflow"
mkdir -p .github/workflows
cat > .github/workflows/deploy.yml <<'YML'
name: Deploy Worker

on:
  push:
    branches: [main]
    paths:
      - 'wrangler.toml'
      - 'src/**'
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    name: Deploy to Cloudflare
    
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Wrangler
        run: npm install -g wrangler

      - name: Deploy Worker
        env:
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
        run: |
          echo "Deploying to Cloudflare Workers..."
          wrangler deploy
          echo "✅ Deployment complete"
YML

say_ "✓ Created .github/workflows/deploy.yml"

#───────────────────────────────────────────────────────────────────────────────
# Step 6: Create voice wrapper scripts
#───────────────────────────────────────────────────────────────────────────────
say_ "Creating voice wrapper scripts"
mkdir -p "$HOME/m2g/voice"

cat > "$HOME/m2g/voice/run-claude.sh" <<'SH'
#!/usr/bin/env bash
# M2G Voice-enabled Claude CLI wrapper
set -e

prompt="${1:-$(pbpaste 2>/dev/null || xclip -selection clipboard -o 2>/dev/null || echo '')}"

if [[ -z "$prompt" ]]; then
  echo "Usage: run-claude.sh '<prompt>'"
  echo "       Or copy text to clipboard first"
  exit 1
fi

export M2G_ENDPOINT="${M2G_ENDPOINT:-relay}"
export M2G_RELAY_BASE="${M2G_RELAY_BASE:-https://ai-genius.workers.dev}"

m2g-claude "$prompt" \
  --speak Samantha \
  --model "${M2G_MODEL:-claude-sonnet-4-20250514}"
SH
chmod +x "$HOME/m2g/voice/run-claude.sh"

say_ "✓ Created ~/m2g/voice/run-claude.sh"

# Windows PowerShell version (if running in WSL or cross-platform)
if [[ -d "/mnt/c" ]] || [[ "${OS:-}" == "Windows_NT" ]]; then
  mkdir -p "/mnt/c/m2g" 2>/dev/null || mkdir -p "C:/m2g" 2>/dev/null || true
  
  cat > "${HOME}/m2g/voice/run-claude.ps1" <<'PS1'
# M2G Voice-enabled Claude CLI wrapper (PowerShell)
param(
  [string]$Prompt
)

if (-not $Prompt) {
  $Prompt = Get-Clipboard
}

if (-not $Prompt) {
  Write-Host "Usage: run-claude.ps1 '<prompt>'"
  Write-Host "       Or copy text to clipboard first"
  exit 1
}

$env:M2G_ENDPOINT = if ($env:M2G_ENDPOINT) { $env:M2G_ENDPOINT } else { "relay" }
$env:M2G_RELAY_BASE = if ($env:M2G_RELAY_BASE) { $env:M2G_RELAY_BASE } else { "https://ai-genius.workers.dev" }
$model = if ($env:M2G_MODEL) { $env:M2G_MODEL } else { "claude-sonnet-4-20250514" }

m2g-claude $Prompt --model $model
PS1
  say_ "✓ Created PowerShell wrapper"
fi

#───────────────────────────────────────────────────────────────────────────────
# Step 7: Create integration example
#───────────────────────────────────────────────────────────────────────────────
say_ "Creating integration documentation"
cat > src/INTEGRATION.md <<'MD'
# M2G Add-Ons Integration Guide

## Quick Integration

Add these changes to your `src/index.js`:

### 1. Import at top

```javascript
import * as integration from "./addons-integration.js";
```

### 2. In your fetch handler

```javascript
export default {
  async fetch(request, env, ctx) {
    const identity = getIdentity(request); // Your auth function
    
    // ═══ ADD-ONS STEP 1: Handle add-on routes ═══
    const addonResp = await integration.handleRequest(request, env, identity);
    if (addonResp) return addonResp;
    
    // Your existing routing...
    if (url.pathname !== "/v1/relay") {
      return new Response("Not found", { status: 404 });
    }
    
    // ═══ ADD-ONS STEP 2: Enforce model policy ═══
    let body = await request.text();
    body = await integration.enforceModelPolicy(body, identity, env);
    
    // Proxy to provider
    const response = await fetch(providerUrl, {
      method: "POST",
      headers: { ... },
      body
    });
    
    // ═══ ADD-ONS STEP 3: Post-response hooks ═══
    ctx.waitUntil(
      integration.postResponseHook(env, identity, provider, response.status)
    );
    
    return response;
  }
};
```

## New Routes

| Route | Method | Auth | Description |
|-------|--------|------|-------------|
| `/health/providers` | GET | No | Check upstream API status |
| `/dash.html` | GET | No | Live monitoring dashboard |
| `/admin/models` | GET | Admin | Get model registry |
| `/admin/models` | POST | Admin | Replace model registry |
| `/admin/models/:group` | PUT | Admin | Update single group |
| `/admin/models/:group` | DELETE | Admin | Delete group |

## Model Registry Format

```json
{
  "default": {
    "allow": ["claude-3-5-haiku-*", "gpt-4o-mini"],
    "fallback": "claude-3-5-haiku-20241022"
  },
  "premium": {
    "allow": ["claude-3-5-sonnet-*", "gpt-4o"],
    "fallback": "claude-3-5-sonnet-20241022"
  },
  "admins": {
    "allow": ["*"],
    "fallback": null
  }
}
```

## Required Secrets

```bash
# Set via wrangler
wrangler secret put WEBHOOK_URL      # Slack/Discord webhook
wrangler secret put ANTHROPIC_API_KEY
wrangler secret put OPENAI_API_KEY

# Seed the model registry
wrangler kv:key put --binding=USAGE_KV model-registry '{
  "default": { "allow": ["gpt-4o-mini"], "fallback": "gpt-4o-mini" }
}'
```
MD

say_ "✓ Created src/INTEGRATION.md"

#───────────────────────────────────────────────────────────────────────────────
# Done
#───────────────────────────────────────────────────────────────────────────────
say_ "Add-ons installation complete!"

cat <<'SUMMARY'

═══════════════════════════════════════════════════════════════════════════════
  M2G WORKER ADD-ONS INSTALLED
═══════════════════════════════════════════════════════════════════════════════

📁 Files created:
   • src/addons.js              - Core add-on functionality
   • src/addons-integration.js  - Integration helpers
   • src/util.js                - Updated with helpers
   • src/INTEGRATION.md         - Integration guide
   • .github/workflows/deploy.yml

🔧 NEXT STEPS:

1. Integrate into src/index.js (see src/INTEGRATION.md)

2. Set secrets:
   wrangler secret put WEBHOOK_URL
   wrangler secret put ANTHROPIC_API_KEY

3. Seed model registry (optional):
   wrangler kv:key put --binding=USAGE_KV model-registry \
     '{"default":{"allow":["gpt-4o-mini"],"fallback":"gpt-4o-mini"}}'

4. Deploy:
   wrangler deploy

5. Test:
   curl https://YOUR-WORKER.workers.dev/health/providers | jq
   open https://YOUR-WORKER.workers.dev/dash.html

═══════════════════════════════════════════════════════════════════════════════
SUMMARY

say_ "Happy shipping!"
