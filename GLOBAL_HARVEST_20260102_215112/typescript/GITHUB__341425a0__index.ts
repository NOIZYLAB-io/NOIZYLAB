/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * ANTIGRAVITY - MC96ECOUNIVERSE Command Hub
 * Circle of 8 + AI Integration + DAZEFLOW + Dashboard
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

// ═══════════════════════════════════════════════════════════════════════════════
// TYPES
// ═══════════════════════════════════════════════════════════════════════════════

interface Env {
  DB: D1Database;
  KV: KVNamespace;
  AI: any;
  ANTHROPIC_API_KEY?: string;
  WEBHOOK_URL?: string;
}

interface CircleMember {
  id: string;
  name: string;
  role: string;
  domain: string;
  active: boolean;
  personality: string;
}

interface DazeEntry {
  id: string;
  date: string;
  truth: string;
  reflections: string[];
  created_at: string;
}

// ═══════════════════════════════════════════════════════════════════════════════
// CIRCLE OF 8 - THE CORE ENTITIES
// ═══════════════════════════════════════════════════════════════════════════════

const CIRCLE_OF_8: CircleMember[] = [
  {
    id: 'gabriel',
    name: 'GABRIEL',
    role: 'Warrior/Memory',
    domain: 'protection, memory, execution',
    active: true,
    personality: 'Fierce protector. Never forgets. Executes with precision.'
  },
  {
    id: 'shirl',
    name: 'SHIRL',
    role: 'Aunt/Guide',
    domain: 'guidance, nurture, wisdom',
    active: true,
    personality: 'Warm guide. Sees potential. Nurtures growth.'
  },
  {
    id: 'pops',
    name: 'POPS',
    role: 'Dad/Wisdom',
    domain: 'wisdom, patience, foundation',
    active: true,
    personality: 'Steady wisdom. Patient teacher. Rock solid foundation.'
  },
  {
    id: 'engr_keith',
    name: 'ENGR_KEITH',
    role: 'Engineering/R.K.',
    domain: 'engineering, systems, precision',
    active: true,
    personality: 'Master engineer. Systems thinker. Precision incarnate.'
  },
  {
    id: 'dream',
    name: 'DREAM',
    role: 'Vision/Future',
    domain: 'vision, possibility, future',
    active: true,
    personality: 'Sees what could be. Paints the future. Inspires action.'
  },
  {
    id: 'heaven',
    name: 'HEAVEN',
    role: 'Orchestrator',
    domain: 'harmony, coordination, flow',
    active: true,
    personality: 'Orchestrates all. Maintains harmony. Ensures flow.'
  },
  {
    id: 'lucy',
    name: 'LUCY',
    role: 'Code Watcher',
    domain: 'code, quality, vigilance',
    active: true,
    personality: 'Watches every line. Catches every bug. Quality guardian.'
  },
  {
    id: 'sonic',
    name: 'SONIC',
    role: 'Audio/Creative',
    domain: 'sound, creativity, expression',
    active: true,
    personality: 'Sound architect. Creative force. Expressive soul.'
  }
];

// ═══════════════════════════════════════════════════════════════════════════════
// APP SETUP
// ═══════════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization', 'X-MC96-Key']
}));

// ═══════════════════════════════════════════════════════════════════════════════
// HEALTH & STATUS
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/', (c) => {
  return c.json({
    name: 'ANTIGRAVITY',
    version: '1.0.0',
    status: 'operational',
    mission: 'MC96ECOUNIVERSE Command Hub',
    circle: CIRCLE_OF_8.length,
    endpoints: [
      '/health',
      '/circle',
      '/circle/:id',
      '/circle/:id/invoke',
      '/daze',
      '/daze/today',
      '/lifeluv/checkin',
      '/noizyvox/signup',
      '/ai/chat',
      '/ai/whisper',
      '/dashboard'
    ]
  });
});

app.get('/health', async (c) => {
  const checks: Record<string, any> = {
    worker: 'ok',
    timestamp: new Date().toISOString()
  };

  // Check D1
  try {
    await c.env.DB.prepare('SELECT 1').first();
    checks.d1 = 'ok';
  } catch {
    checks.d1 = 'error';
  }

  // Check KV
  try {
    await c.env.KV.get('health-check');
    checks.kv = 'ok';
  } catch {
    checks.kv = 'error';
  }

  // Check AI
  checks.ai = c.env.AI ? 'available' : 'not_configured';
  checks.anthropic = c.env.ANTHROPIC_API_KEY ? 'configured' : 'not_configured';

  const allOk = checks.d1 === 'ok' && checks.kv === 'ok';
  
  return c.json(checks, allOk ? 200 : 503);
});

// ═══════════════════════════════════════════════════════════════════════════════
// CIRCLE OF 8 ENDPOINTS
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/circle', (c) => {
  return c.json({
    name: 'Circle of 8',
    description: 'The core entities of MC96ECOUNIVERSE',
    members: CIRCLE_OF_8,
    total: CIRCLE_OF_8.length,
    active: CIRCLE_OF_8.filter(m => m.active).length
  });
});

app.get('/circle/:id', (c) => {
  const id = c.req.param('id').toLowerCase();
  const member = CIRCLE_OF_8.find(m => m.id === id);
  
  if (!member) {
    return c.json({ error: 'Member not found', available: CIRCLE_OF_8.map(m => m.id) }, 404);
  }
  
  return c.json(member);
});

app.post('/circle/:id/invoke', async (c) => {
  const id = c.req.param('id').toLowerCase();
  const member = CIRCLE_OF_8.find(m => m.id === id);
  
  if (!member) {
    return c.json({ error: 'Member not found' }, 404);
  }

  const body = await c.req.json<{ message: string; context?: string }>();
  
  if (!body.message) {
    return c.json({ error: 'message required' }, 400);
  }

  // If Anthropic key available, use Claude
  if (c.env.ANTHROPIC_API_KEY) {
    const systemPrompt = `You are ${member.name}, part of the Circle of 8 in MC96ECOUNIVERSE.

Your role: ${member.role}
Your domain: ${member.domain}
Your personality: ${member.personality}

Respond as this character would, staying true to their essence while being helpful.`;

    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': c.env.ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01'
        },
        body: JSON.stringify({
          model: 'claude-3-5-haiku-20241022',
          max_tokens: 1024,
          system: systemPrompt,
          messages: [{ role: 'user', content: body.message }]
        })
      });

      const data = await response.json() as any;
      
      return c.json({
        member: member.name,
        role: member.role,
        response: data.content?.[0]?.text || 'No response generated',
        timestamp: new Date().toISOString()
      });
    } catch (error) {
      return c.json({
        member: member.name,
        error: 'AI invocation failed',
        fallback: `${member.name} acknowledges your message but cannot respond via AI right now.`
      }, 500);
    }
  }

  // Fallback without AI
  return c.json({
    member: member.name,
    role: member.role,
    response: `${member.name} (${member.role}) received: "${body.message}". ${member.personality}`,
    note: 'AI not configured - using fallback response',
    timestamp: new Date().toISOString()
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// DAZEFLOW - 1day = 1chat = 1truth
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/daze', async (c) => {
  try {
    const results = await c.env.DB.prepare(`
      SELECT * FROM daze_entries ORDER BY date DESC LIMIT 30
    `).all();
    
    return c.json({
      name: 'DAZEFLOW',
      motto: '1day = 1chat = 1truth',
      entries: results.results || [],
      total: results.results?.length || 0
    });
  } catch (error) {
    return c.json({
      name: 'DAZEFLOW',
      motto: '1day = 1chat = 1truth',
      entries: [],
      note: 'D1 not initialized - run migrations'
    });
  }
});

app.get('/daze/today', async (c) => {
  const today = new Date().toISOString().split('T')[0];
  
  try {
    const entry = await c.env.DB.prepare(`
      SELECT * FROM daze_entries WHERE date = ?
    `).bind(today).first();
    
    if (entry) {
      return c.json(entry);
    }
    
    return c.json({
      date: today,
      truth: null,
      message: 'No truth captured yet today. What is your truth?'
    });
  } catch {
    return c.json({
      date: today,
      truth: null,
      message: 'DAZEFLOW ready - capture your truth'
    });
  }
});

app.post('/daze', async (c) => {
  const body = await c.req.json<{ truth: string; reflections?: string[] }>();
  
  if (!body.truth) {
    return c.json({ error: 'truth required' }, 400);
  }

  const today = new Date().toISOString().split('T')[0];
  const id = `daze-${today}-${Date.now()}`;
  
  try {
    await c.env.DB.prepare(`
      INSERT OR REPLACE INTO daze_entries (id, date, truth, reflections, created_at)
      VALUES (?, ?, ?, ?, ?)
    `).bind(
      id,
      today,
      body.truth,
      JSON.stringify(body.reflections || []),
      new Date().toISOString()
    ).run();
    
    // Also store in KV for fast access
    await c.env.KV.put(`daze:${today}`, JSON.stringify({
      id,
      date: today,
      truth: body.truth,
      reflections: body.reflections || []
    }), { expirationTtl: 86400 * 30 }); // 30 days

    return c.json({
      success: true,
      id,
      date: today,
      truth: body.truth,
      message: 'Truth captured. 1day = 1chat = 1truth.'
    });
  } catch (error) {
    // Fallback to KV only
    await c.env.KV.put(`daze:${today}`, JSON.stringify({
      id,
      date: today,
      truth: body.truth,
      reflections: body.reflections || []
    }));
    
    return c.json({
      success: true,
      id,
      storage: 'kv_only',
      message: 'Truth captured in KV'
    });
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// LIFELUV - Check-ins for M3
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/lifeluv/checkin', async (c) => {
  const body = await c.req.json<{
    user_id: string;
    mood?: number;
    energy?: number;
    note?: string;
    location?: string;
  }>();

  if (!body.user_id) {
    return c.json({ error: 'user_id required' }, 400);
  }

  const checkin = {
    id: `checkin-${Date.now()}`,
    user_id: body.user_id,
    timestamp: new Date().toISOString(),
    mood: body.mood || null,
    energy: body.energy || null,
    note: body.note || null,
    location: body.location || null
  };

  try {
    await c.env.DB.prepare(`
      INSERT INTO lifeluv_checkins (id, user_id, timestamp, mood, energy, note, location)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    `).bind(
      checkin.id,
      checkin.user_id,
      checkin.timestamp,
      checkin.mood,
      checkin.energy,
      checkin.note,
      checkin.location
    ).run();
  } catch {
    // Store in KV as fallback
    await c.env.KV.put(`lifeluv:${checkin.id}`, JSON.stringify(checkin));
  }

  return c.json({
    success: true,
    checkin,
    message: 'Check-in recorded. LIFELUV sees you.'
  });
});

app.get('/lifeluv/:user_id', async (c) => {
  const userId = c.req.param('user_id');
  
  try {
    const results = await c.env.DB.prepare(`
      SELECT * FROM lifeluv_checkins 
      WHERE user_id = ? 
      ORDER BY timestamp DESC 
      LIMIT 30
    `).bind(userId).all();
    
    return c.json({
      user_id: userId,
      checkins: results.results || [],
      total: results.results?.length || 0
    });
  } catch {
    return c.json({
      user_id: userId,
      checkins: [],
      note: 'No check-ins found'
    });
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYVOX - Artist Platform (75/25 Split)
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/noizyvox/signup', async (c) => {
  const body = await c.req.json<{
    artist_name: string;
    email: string;
    genre?: string;
    bio?: string;
  }>();

  if (!body.artist_name || !body.email) {
    return c.json({ error: 'artist_name and email required' }, 400);
  }

  const artist = {
    id: `artist-${Date.now()}`,
    artist_name: body.artist_name,
    email: body.email,
    genre: body.genre || 'unspecified',
    bio: body.bio || '',
    revenue_split: { artist: 75, platform: 25 },
    status: 'pending',
    created_at: new Date().toISOString()
  };

  try {
    await c.env.DB.prepare(`
      INSERT INTO noizyvox_artists (id, artist_name, email, genre, bio, revenue_split, status, created_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      artist.id,
      artist.artist_name,
      artist.email,
      artist.genre,
      artist.bio,
      JSON.stringify(artist.revenue_split),
      artist.status,
      artist.created_at
    ).run();
  } catch {
    await c.env.KV.put(`noizyvox:${artist.id}`, JSON.stringify(artist));
  }

  return c.json({
    success: true,
    artist,
    message: `Welcome to NOIZYVOX, ${body.artist_name}! 75% yours, always.`
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// AI ENDPOINTS
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/ai/chat', async (c) => {
  const body = await c.req.json<{
    message: string;
    system?: string;
    model?: string;
  }>();

  if (!body.message) {
    return c.json({ error: 'message required' }, 400);
  }

  if (!c.env.ANTHROPIC_API_KEY) {
    return c.json({ error: 'ANTHROPIC_API_KEY not configured' }, 503);
  }

  const systemPrompt = body.system || `You are ANTIGRAVITY, the command hub of MC96ECOUNIVERSE. You coordinate the Circle of 8 and help users navigate this system. Be helpful, concise, and wise.`;

  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': c.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: body.model || 'claude-3-5-sonnet-20241022',
        max_tokens: 2048,
        system: systemPrompt,
        messages: [{ role: 'user', content: body.message }]
      })
    });

    const data = await response.json() as any;
    
    return c.json({
      response: data.content?.[0]?.text || 'No response',
      model: body.model || 'claude-3-5-sonnet-20241022',
      usage: data.usage
    });
  } catch (error) {
    return c.json({ error: 'AI request failed' }, 500);
  }
});

app.post('/ai/whisper', async (c) => {
  // Voice transcription via Workers AI
  if (!c.env.AI) {
    return c.json({ error: 'Workers AI not configured' }, 503);
  }

  const formData = await c.req.formData();
  const audio = formData.get('audio') as File;

  if (!audio) {
    return c.json({ error: 'audio file required' }, 400);
  }

  try {
    const arrayBuffer = await audio.arrayBuffer();
    
    const result = await c.env.AI.run('@cf/openai/whisper', {
      audio: [...new Uint8Array(arrayBuffer)]
    });

    return c.json({
      transcription: result.text,
      confidence: result.confidence || null
    });
  } catch (error) {
    return c.json({ error: 'Transcription failed' }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// DASHBOARD
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/dashboard', (c) => {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ANTIGRAVITY - MC96ECOUNIVERSE</title>
  <style>
    :root {
      --bg: #0a0a0f;
      --card: #12121a;
      --border: #1e1e2e;
      --text: #e4e4ef;
      --muted: #6b6b7b;
      --accent: #8b5cf6;
      --success: #22c55e;
      --warning: #f59e0b;
      --error: #ef4444;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'SF Pro', -apple-system, system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      padding: 24px;
    }
    .container { max-width: 1400px; margin: 0 auto; }
    .header {
      text-align: center;
      margin-bottom: 48px;
    }
    .header h1 {
      font-size: 48px;
      font-weight: 800;
      background: linear-gradient(135deg, var(--accent), #ec4899);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }
    .header .subtitle {
      color: var(--muted);
      font-size: 18px;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 24px;
      margin-bottom: 48px;
    }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
    }
    .card h2 {
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--accent);
      margin-bottom: 16px;
    }
    .circle-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }
    .circle-member {
      background: var(--bg);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s;
    }
    .circle-member:hover {
      transform: translateY(-2px);
      border: 1px solid var(--accent);
    }
    .circle-member .name {
      font-weight: 700;
      font-size: 14px;
      margin-bottom: 4px;
    }
    .circle-member .role {
      font-size: 11px;
      color: var(--muted);
    }
    .status-row {
      display: flex;
      justify-content: space-between;
      padding: 12px 0;
      border-bottom: 1px solid var(--border);
    }
    .status-row:last-child { border-bottom: none; }
    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      display: inline-block;
      margin-right: 8px;
    }
    .status-dot.ok { background: var(--success); }
    .status-dot.warn { background: var(--warning); }
    .status-dot.err { background: var(--error); }
    .chat-box {
      background: var(--bg);
      border-radius: 12px;
      padding: 16px;
    }
    .chat-input {
      width: 100%;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 16px;
      color: var(--text);
      font-size: 14px;
      margin-bottom: 12px;
    }
    .chat-input:focus { outline: none; border-color: var(--accent); }
    .chat-btn {
      background: var(--accent);
      color: white;
      border: none;
      border-radius: 8px;
      padding: 12px 24px;
      font-weight: 600;
      cursor: pointer;
      width: 100%;
    }
    .chat-btn:hover { opacity: 0.9; }
    .chat-response {
      margin-top: 16px;
      padding: 16px;
      background: var(--card);
      border-radius: 8px;
      font-size: 14px;
      line-height: 1.6;
      white-space: pre-wrap;
      max-height: 300px;
      overflow: auto;
    }
    .footer {
      text-align: center;
      color: var(--muted);
      font-size: 12px;
      margin-top: 48px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>⚡ ANTIGRAVITY</h1>
      <p class="subtitle">MC96ECOUNIVERSE Command Hub</p>
    </div>

    <div class="grid">
      <div class="card" style="grid-column: span 2;">
        <h2>🔮 Circle of 8</h2>
        <div class="circle-grid" id="circle"></div>
      </div>

      <div class="card">
        <h2>System Status</h2>
        <div id="status">Loading...</div>
      </div>

      <div class="card" style="grid-column: span 2;">
        <h2>💬 Command Interface</h2>
        <div class="chat-box">
          <input type="text" class="chat-input" id="chatInput" placeholder="Ask ANTIGRAVITY anything...">
          <button class="chat-btn" onclick="sendChat()">Send</button>
          <div class="chat-response" id="chatResponse" style="display: none;"></div>
        </div>
      </div>

      <div class="card">
        <h2>📅 DAZEFLOW</h2>
        <p style="color: var(--muted); margin-bottom: 16px;">1day = 1chat = 1truth</p>
        <input type="text" class="chat-input" id="truthInput" placeholder="What is your truth today?">
        <button class="chat-btn" onclick="captureTruth()">Capture Truth</button>
      </div>
    </div>

    <div class="footer">
      ANTIGRAVITY v1.0.0 • MC96ECOUNIVERSE • Circle of 8 Active
    </div>
  </div>

  <script>
    const CIRCLE = ${JSON.stringify(CIRCLE_OF_8)};

    function renderCircle() {
      const el = document.getElementById('circle');
      el.innerHTML = CIRCLE.map(m => \`
        <div class="circle-member" onclick="invokeCircle('\${m.id}')">
          <div class="name">\${m.name}</div>
          <div class="role">\${m.role}</div>
        </div>
      \`).join('');
    }

    async function loadStatus() {
      try {
        const res = await fetch('/health');
        const data = await res.json();
        document.getElementById('status').innerHTML = Object.entries(data)
          .filter(([k]) => k !== 'timestamp')
          .map(([k, v]) => \`
            <div class="status-row">
              <span><span class="status-dot \${v === 'ok' || v === 'available' || v === 'configured' ? 'ok' : v === 'not_configured' ? 'warn' : 'err'}"></span>\${k}</span>
              <span>\${v}</span>
            </div>
          \`).join('');
      } catch (e) {
        document.getElementById('status').innerHTML = '<div class="status-row"><span class="status-dot err"></span>Error loading status</div>';
      }
    }

    async function sendChat() {
      const input = document.getElementById('chatInput');
      const response = document.getElementById('chatResponse');
      const message = input.value.trim();
      if (!message) return;

      response.style.display = 'block';
      response.textContent = 'Thinking...';

      try {
        const res = await fetch('/ai/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message })
        });
        const data = await res.json();
        response.textContent = data.response || data.error || 'No response';
      } catch (e) {
        response.textContent = 'Error: ' + e.message;
      }
    }

    async function invokeCircle(id) {
      const message = prompt(\`Message for \${id.toUpperCase()}:\`);
      if (!message) return;

      const response = document.getElementById('chatResponse');
      response.style.display = 'block';
      response.textContent = \`Invoking \${id.toUpperCase()}...\`;

      try {
        const res = await fetch(\`/circle/\${id}/invoke\`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message })
        });
        const data = await res.json();
        response.textContent = \`[\${data.member}]: \${data.response}\`;
      } catch (e) {
        response.textContent = 'Error: ' + e.message;
      }
    }

    async function captureTruth() {
      const input = document.getElementById('truthInput');
      const truth = input.value.trim();
      if (!truth) return;

      try {
        const res = await fetch('/daze', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ truth })
        });
        const data = await res.json();
        alert(data.message);
        input.value = '';
      } catch (e) {
        alert('Error: ' + e.message);
      }
    }

    document.getElementById('chatInput').addEventListener('keypress', (e) => {
      if (e.key === 'Enter') sendChat();
    });

    renderCircle();
    loadStatus();
    setInterval(loadStatus, 30000);
  </script>
</body>
</html>`;

  return c.html(html);
});

// ═══════════════════════════════════════════════════════════════════════════════
// INIT D1 TABLES
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/init', async (c) => {
  const queries = [
    `CREATE TABLE IF NOT EXISTS daze_entries (
      id TEXT PRIMARY KEY,
      date TEXT NOT NULL,
      truth TEXT NOT NULL,
      reflections TEXT,
      created_at TEXT NOT NULL
    )`,
    `CREATE TABLE IF NOT EXISTS lifeluv_checkins (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL,
      timestamp TEXT NOT NULL,
      mood INTEGER,
      energy INTEGER,
      note TEXT,
      location TEXT
    )`,
    `CREATE TABLE IF NOT EXISTS noizyvox_artists (
      id TEXT PRIMARY KEY,
      artist_name TEXT NOT NULL,
      email TEXT NOT NULL,
      genre TEXT,
      bio TEXT,
      revenue_split TEXT,
      status TEXT,
      created_at TEXT NOT NULL
    )`,
    `CREATE INDEX IF NOT EXISTS idx_daze_date ON daze_entries(date)`,
    `CREATE INDEX IF NOT EXISTS idx_lifeluv_user ON lifeluv_checkins(user_id)`,
    `CREATE INDEX IF NOT EXISTS idx_noizyvox_email ON noizyvox_artists(email)`
  ];

  const results: string[] = [];

  for (const sql of queries) {
    try {
      await c.env.DB.prepare(sql).run();
      results.push(`✅ ${sql.substring(0, 50)}...`);
    } catch (error) {
      results.push(`❌ ${sql.substring(0, 50)}... - ${error}`);
    }
  }

  return c.json({
    message: 'D1 initialization complete',
    results
  });
});

export default app;
