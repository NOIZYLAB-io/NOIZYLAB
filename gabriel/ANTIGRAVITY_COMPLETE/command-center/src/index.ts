/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * MC96 COMMAND CENTER - Unified Dashboard & Gateway
 * Central hub for all MC96ECOUNIVERSE workers and services
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

// ═══════════════════════════════════════════════════════════════════════════════
// TYPES
// ═══════════════════════════════════════════════════════════════════════════════

interface Env {
  AI: any;
  KV: KVNamespace;
  // Service bindings (if using Cloudflare Service Bindings)
  NOIZYLAB?: Fetcher;
  MEDIA_VAULT?: Fetcher;
  NEURAL_GATEWAY?: Fetcher;
  SONIC_ENGINE?: Fetcher;
  TASK_COMMANDER?: Fetcher;
  DAZEFLOW?: Fetcher;
}

interface ServiceConfig {
  name: string;
  description: string;
  agent?: string;
  endpoints: string[];
  status?: 'online' | 'offline' | 'degraded';
  version?: string;
}

// ═══════════════════════════════════════════════════════════════════════════════
// SERVICE REGISTRY
// ═══════════════════════════════════════════════════════════════════════════════

const SERVICES: Record<string, ServiceConfig> = {
  'noizylab': {
    name: 'NOIZYLAB',
    description: 'Main AI Gateway - HOTROD v5.0',
    agent: 'GABRIEL',
    endpoints: ['/ai/chat', '/ai/image', '/ai/embed', '/ai/transcribe', '/circle8']
  },
  'media-vault': {
    name: 'MEDIA VAULT',
    description: 'R2 Cloud Storage Gateway',
    endpoints: ['/upload', '/download', '/list', '/ai/generate-image', '/ai/transcribe']
  },
  'neural-gateway': {
    name: 'NEURAL GATEWAY',
    description: 'AI Model Router - 20+ Models',
    endpoints: ['/models', '/chat', '/image', '/embed', '/transcribe', '/sql', '/vision']
  },
  'sonic-engine': {
    name: 'SONIC ENGINE',
    description: 'Audio Processing Hub',
    agent: 'SONIC',
    endpoints: ['/tts/generate', '/stt/transcribe', '/music/analyze', '/theory/scale', '/theory/chord']
  },
  'task-commander': {
    name: 'TASK COMMANDER',
    description: 'Automation Hub - Cron + Webhooks',
    endpoints: ['/tasks', '/webhook', '/run']
  },
  'dazeflow': {
    name: 'DAZEFLOW',
    description: 'Truth Capture System',
    endpoints: ['/today', '/entries', '/stats', '/prompts', '/review']
  }
};

const CIRCLE_OF_8 = [
  { name: 'GABRIEL', role: 'Warrior/Memory', powers: 'protection, memory, execution', emoji: '⚔️' },
  { name: 'SHIRL', role: 'Aunt/Guide', powers: 'guidance, nurture, wisdom', emoji: '💫' },
  { name: 'POPS', role: 'Dad/Wisdom', powers: 'wisdom, patience, foundation', emoji: '🎯' },
  { name: 'ENGR_KEITH', role: 'Engineering/R.K.', powers: 'engineering, systems, precision', emoji: '⚙️' },
  { name: 'DREAM', role: 'Vision/Future', powers: 'vision, possibility, future', emoji: '✨' },
  { name: 'HEAVEN', role: 'Orchestrator', powers: 'harmony, coordination, flow', emoji: '🎭' },
  { name: 'LUCY', role: 'Code Watcher', powers: 'code, quality, vigilance', emoji: '👁️' },
  { name: 'SONIC', role: 'Audio Engine', powers: 'sound, rhythm, creativity', emoji: '🎵' }
];

// ═══════════════════════════════════════════════════════════════════════════════
// APP
// ═══════════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization']
}));

// ═══════════════════════════════════════════════════════════════════════════════
// MAIN DASHBOARD
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/', (c) => {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MC96 Command Center</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'SF Mono', 'Fira Code', monospace;
      background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
      color: #e0e0e0;
      min-height: 100vh;
      padding: 20px;
    }
    .container { max-width: 1400px; margin: 0 auto; }
    
    .header {
      text-align: center;
      padding: 40px 0;
      border-bottom: 1px solid #333;
      margin-bottom: 40px;
    }
    .logo {
      font-size: 3rem;
      font-weight: bold;
      background: linear-gradient(45deg, #00d4ff, #7b2cbf, #ff006e);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 10px;
    }
    .subtitle { color: #888; font-size: 1.1rem; }
    
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-bottom: 40px;
    }
    
    .card {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 16px;
      padding: 24px;
      transition: all 0.3s;
    }
    .card:hover {
      border-color: #00d4ff;
      transform: translateY(-4px);
      box-shadow: 0 10px 40px rgba(0,212,255,0.2);
    }
    
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }
    .card-title { font-size: 1.3rem; font-weight: bold; color: #00d4ff; }
    .status {
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: bold;
    }
    .status.online { background: #00ff88; color: #000; }
    .status.offline { background: #ff4444; color: #fff; }
    
    .card-desc { color: #888; margin-bottom: 16px; }
    
    .endpoints {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .endpoint {
      background: rgba(0,212,255,0.1);
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      color: #00d4ff;
    }
    
    .circle-section {
      background: rgba(123,44,191,0.1);
      border: 1px solid rgba(123,44,191,0.3);
      border-radius: 16px;
      padding: 32px;
      margin-bottom: 40px;
    }
    .circle-title {
      font-size: 1.5rem;
      margin-bottom: 24px;
      color: #7b2cbf;
    }
    .agents {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
    }
    .agent {
      background: rgba(255,255,255,0.03);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
    }
    .agent-emoji { font-size: 2rem; margin-bottom: 8px; }
    .agent-name { font-weight: bold; color: #7b2cbf; }
    .agent-role { font-size: 0.85rem; color: #888; }
    
    .stats {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
      margin-bottom: 40px;
    }
    .stat {
      background: rgba(255,255,255,0.05);
      border-radius: 12px;
      padding: 24px;
      text-align: center;
    }
    .stat-value {
      font-size: 2.5rem;
      font-weight: bold;
      background: linear-gradient(45deg, #00d4ff, #7b2cbf);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .stat-label { color: #888; margin-top: 8px; }
    
    .footer {
      text-align: center;
      padding: 40px 0;
      border-top: 1px solid #333;
      color: #666;
    }
    
    @media (max-width: 768px) {
      .stats { grid-template-columns: repeat(2, 1fr); }
      .logo { font-size: 2rem; }
    }
  </style>
</head>
<body>
  <div class="container">
    <header class="header">
      <div class="logo">MC96 COMMAND CENTER</div>
      <div class="subtitle">MC96ECOUNIVERSE • GORUNFREE • NOIZY.AI</div>
    </header>
    
    <div class="stats">
      <div class="stat">
        <div class="stat-value">${Object.keys(SERVICES).length}</div>
        <div class="stat-label">Active Services</div>
      </div>
      <div class="stat">
        <div class="stat-value">8</div>
        <div class="stat-label">Circle Agents</div>
      </div>
      <div class="stat">
        <div class="stat-value">20+</div>
        <div class="stat-label">AI Models</div>
      </div>
      <div class="stat">
        <div class="stat-value">∞</div>
        <div class="stat-label">Possibilities</div>
      </div>
    </div>
    
    <div class="circle-section">
      <div class="circle-title">⭕ Circle of 8 - AI Agent Network</div>
      <div class="agents">
        ${CIRCLE_OF_8.map(agent => `
          <div class="agent">
            <div class="agent-emoji">${agent.emoji}</div>
            <div class="agent-name">${agent.name}</div>
            <div class="agent-role">${agent.role}</div>
          </div>
        `).join('')}
      </div>
    </div>
    
    <div class="grid">
      ${Object.entries(SERVICES).map(([key, service]) => `
        <div class="card">
          <div class="card-header">
            <div class="card-title">${service.name}</div>
            <div class="status online">ONLINE</div>
          </div>
          <div class="card-desc">${service.description}</div>
          <div class="endpoints">
            ${service.endpoints.map(ep => `<span class="endpoint">${ep}</span>`).join('')}
          </div>
        </div>
      `).join('')}
    </div>
    
    <footer class="footer">
      <p>MC96ECOUNIVERSE © 2026 • Built with ❤️ by NOIZYLAB</p>
      <p style="margin-top: 8px;">Powered by Cloudflare Workers + Workers AI</p>
    </footer>
  </div>
</body>
</html>`;

  return c.html(html);
});

// ═══════════════════════════════════════════════════════════════════════════════
// API ENDPOINTS
// ═══════════════════════════════════════════════════════════════════════════════

// System status
app.get('/api/status', (c) => c.json({
  system: 'MC96 COMMAND CENTER',
  version: '1.0.0',
  status: 'OPERATIONAL',
  services: Object.keys(SERVICES).length,
  agents: CIRCLE_OF_8.length,
  timestamp: new Date().toISOString()
}));

// List all services
app.get('/api/services', (c) => c.json({
  success: true,
  services: Object.entries(SERVICES).map(([key, service]) => ({
    id: key,
    ...service,
    status: 'online'
  }))
}));

// Circle of 8
app.get('/api/circle8', (c) => c.json({
  success: true,
  agents: CIRCLE_OF_8
}));

// ═══════════════════════════════════════════════════════════════════════════════
// UNIFIED AI INTERFACE
// ═══════════════════════════════════════════════════════════════════════════════

// Universal chat endpoint
app.post('/api/ai/chat', async (c) => {
  try {
    const { messages, model = '@cf/meta/llama-3.1-70b-instruct', agent } = await c.req.json();

    if (!c.env.AI) {
      return c.json({ success: false, error: 'AI not configured' }, 500);
    }

    // If specific agent requested, add their personality
    let systemPrompt = '';
    if (agent) {
      const agentConfig = CIRCLE_OF_8.find(a => a.name.toLowerCase() === agent.toLowerCase());
      if (agentConfig) {
        systemPrompt = `You are ${agentConfig.name}, the ${agentConfig.role} of the Circle of 8. Your powers include: ${agentConfig.powers}. Respond in character.`;
      }
    }

    const aiMessages = systemPrompt 
      ? [{ role: 'system', content: systemPrompt }, ...messages]
      : messages;

    const result = await c.env.AI.run(model, { messages: aiMessages });

    return c.json({
      success: true,
      response: result.response,
      agent: agent || 'default',
      model
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Quick AI query
app.get('/api/ai/ask', async (c) => {
  try {
    const question = c.req.query('q');
    if (!question) {
      return c.json({ success: false, error: 'Query parameter "q" required' }, 400);
    }

    if (!c.env.AI) {
      return c.json({ success: false, error: 'AI not configured' }, 500);
    }

    const result = await c.env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{ role: 'user', content: question }]
    });

    return c.json({
      success: true,
      question,
      answer: result.response
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// HEALTH CHECKS
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/health', (c) => c.json({ ok: true, service: 'command-center' }));

app.get('/api/health/all', async (c) => {
  const health: Record<string, any> = {
    timestamp: new Date().toISOString()
  };

  // Check KV
  if (c.env.KV) {
    try {
      await c.env.KV.get('health:ping');
      health.kv = 'healthy';
    } catch {
      health.kv = 'error';
    }
  } else {
    health.kv = 'not configured';
  }

  // Check AI
  if (c.env.AI) {
    try {
      await c.env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
        messages: [{ role: 'user', content: 'ping' }],
        max_tokens: 5
      });
      health.ai = 'healthy';
    } catch {
      health.ai = 'error';
    }
  } else {
    health.ai = 'not configured';
  }

  return c.json({ success: true, health });
});

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORT
// ═══════════════════════════════════════════════════════════════════════════════

export default app;
