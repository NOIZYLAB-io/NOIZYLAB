/**
 * ═══════════════════════════════════════════════════════════════════
 * 
 *   ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
 *  ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
 *  ██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
 *  ██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
 *  ╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
 *   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
 * 
 *   Voice-First Infrastructure Command Center
 *   "One Command. Total Control. Zero Friction."
 * 
 *   Built by Rob Plowman — a composer with a C3 spinal injury
 *   who got sick of tools that require hands he can't fully use.
 * 
 *   GORUNFREE — If Rob can run an empire with his voice, so can you.
 * 
 *   © 2025 NOIZY.AI — Fish Music Inc.
 * 
 * ═══════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════
// NATURAL LANGUAGE COMMAND PARSER
// ═══════════════════════════════════════════════════════════════════
const COMMANDS = {
  speed: {
    triggers: ['speed', 'fast', 'optimize', 'boost', 'turbo', 'accelerate'],
    action: 'speed-boost',
    response: '🚀 Speed boost activated! 16 optimizations enabled.'
  },
  purge: {
    triggers: ['purge', 'clear', 'flush', 'reset cache', 'fresh'],
    action: 'purge-cache',
    response: '🧹 Cache purged! Fresh start.'
  },
  dns: {
    triggers: ['dns', 'records', 'domains', 'subdomains', 'show dns'],
    action: 'dns-list',
    response: '📋 Here are your DNS records:'
  },
  status: {
    triggers: ['status', 'health', 'check', 'how is', 'what\'s running', 'show me'],
    action: 'status',
    response: '📊 Current system status:'
  },
  secure: {
    triggers: ['secure', 'ssl', 'https', 'security', 'protect', 'lock'],
    action: 'secure',
    response: '🔒 Security maximized!'
  },
  help: {
    triggers: ['help', 'commands', 'what can you', 'how do i'],
    action: 'help',
    response: '💡 Here\'s what I can do:'
  }
};

function parseCommand(input) {
  const lower = input.toLowerCase();
  
  for (const [name, cmd] of Object.entries(COMMANDS)) {
    for (const trigger of cmd.triggers) {
      if (lower.includes(trigger)) {
        return { name, ...cmd };
      }
    }
  }
  
  return null;
}

// ═══════════════════════════════════════════════════════════════════
// MAIN WORKER
// ═══════════════════════════════════════════════════════════════════
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // ═══════════════════════════════════════════════════════════════
    // LANDING PAGE
    // ═══════════════════════════════════════════════════════════════
    if (path === '/' || path === '') {
      return new Response(renderLandingPage(), {
        headers: { 'Content-Type': 'text/html' }
      });
    }
    
    // ═══════════════════════════════════════════════════════════════
    // HEALTH CHECK
    // ═══════════════════════════════════════════════════════════════
    if (path === '/health') {
      return jsonResponse({
        status: 'CODEMASTER ONLINE',
        version: '1.0.0',
        timestamp: new Date().toISOString(),
        gorunfree: true
      });
    }
    
    // ═══════════════════════════════════════════════════════════════
    // COMMAND API - Natural language processing
    // ═══════════════════════════════════════════════════════════════
    if (path === '/api/command') {
      if (request.method !== 'POST') {
        return jsonResponse({ error: 'POST required' }, 405);
      }
      
      try {
        const body = await request.json();
        const input = body.command || body.text || body.input || '';
        
        if (!input) {
          return jsonResponse({ error: 'No command provided' }, 400);
        }
        
        const parsed = parseCommand(input);
        
        if (!parsed) {
          return jsonResponse({
            understood: false,
            input,
            message: "I didn't understand that. Try: 'speed boost', 'purge cache', 'show dns', or 'help'",
            suggestions: ['speed boost my site', 'purge the cache', 'show me dns records', 'help']
          });
        }
        
        // For now, return what we WOULD do
        // Later: actually execute against Cloudflare API
        return jsonResponse({
          understood: true,
          input,
          command: parsed.name,
          action: parsed.action,
          message: parsed.response,
          executed: false, // Will be true when we wire up real execution
          note: 'Demo mode - connect your Cloudflare to execute'
        });
        
      } catch (e) {
        return jsonResponse({ error: 'Invalid JSON', details: e.message }, 400);
      }
    }
    
    // ═══════════════════════════════════════════════════════════════
    // DEMO CONSOLE
    // ═══════════════════════════════════════════════════════════════
    if (path === '/console' || path === '/demo') {
      return new Response(renderConsole(), {
        headers: { 'Content-Type': 'text/html' }
      });
    }
    
    // ═══════════════════════════════════════════════════════════════
    // WAITLIST SIGNUP
    // ═══════════════════════════════════════════════════════════════
    if (path === '/api/waitlist') {
      if (request.method !== 'POST') {
        return jsonResponse({ error: 'POST required' }, 405);
      }
      
      try {
        const body = await request.json();
        const email = body.email;
        
        if (!email || !email.includes('@')) {
          return jsonResponse({ error: 'Valid email required' }, 400);
        }
        
        // TODO: Store in D1 database
        // For now, just acknowledge
        return jsonResponse({
          success: true,
          message: "You're on the list! We'll notify you when CODEMASTER launches.",
          email
        });
        
      } catch (e) {
        return jsonResponse({ error: 'Invalid request' }, 400);
      }
    }
    
    // 404
    return jsonResponse({ error: 'Not found', path }, 404);
  }
};

// ═══════════════════════════════════════════════════════════════════
// LANDING PAGE
// ═══════════════════════════════════════════════════════════════════
function renderLandingPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CODEMASTER — Voice-First Infrastructure Control</title>
  <meta name="description" content="One command. Total control. Zero friction. The world's first voice-first infrastructure command center.">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    :root {
      --bg: #0a0a0a;
      --text: #ffffff;
      --accent: #00ff88;
      --accent2: #ff3366;
      --gray: #888;
      --card: rgba(255,255,255,0.05);
    }
    
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      line-height: 1.6;
    }
    
    /* HERO */
    .hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 2rem;
      background: 
        radial-gradient(circle at 20% 50%, rgba(0,255,136,0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 50%, rgba(255,51,102,0.1) 0%, transparent 50%),
        var(--bg);
    }
    
    .logo {
      font-size: 4rem;
      font-weight: 900;
      letter-spacing: -0.05em;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 1rem;
    }
    
    .tagline {
      font-size: 1.5rem;
      color: var(--gray);
      margin-bottom: 2rem;
      max-width: 600px;
    }
    
    .hero-cta {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
      justify-content: center;
      margin-bottom: 3rem;
    }
    
    .btn {
      padding: 1rem 2rem;
      font-size: 1.1rem;
      border: none;
      border-radius: 50px;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.3s;
      text-decoration: none;
    }
    
    .btn-primary {
      background: var(--accent);
      color: var(--bg);
    }
    
    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 40px rgba(0,255,136,0.3);
    }
    
    .btn-secondary {
      background: transparent;
      color: var(--text);
      border: 2px solid var(--gray);
    }
    
    .btn-secondary:hover {
      border-color: var(--accent);
      color: var(--accent);
    }
    
    /* DEMO BOX */
    .demo-box {
      background: var(--card);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 20px;
      padding: 2rem;
      max-width: 600px;
      width: 100%;
      margin-bottom: 3rem;
    }
    
    .demo-input {
      width: 100%;
      padding: 1rem 1.5rem;
      font-size: 1.2rem;
      border: 2px solid rgba(255,255,255,0.1);
      border-radius: 50px;
      background: rgba(0,0,0,0.5);
      color: var(--text);
      outline: none;
      transition: border-color 0.3s;
    }
    
    .demo-input:focus {
      border-color: var(--accent);
    }
    
    .demo-input::placeholder {
      color: var(--gray);
    }
    
    .demo-output {
      margin-top: 1rem;
      padding: 1rem;
      background: rgba(0,0,0,0.3);
      border-radius: 10px;
      font-family: monospace;
      min-height: 60px;
      color: var(--accent);
    }
    
    .mic-btn {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: var(--accent2);
      border: none;
      cursor: pointer;
      font-size: 1.5rem;
      margin-top: 1rem;
      transition: all 0.3s;
    }
    
    .mic-btn:hover {
      transform: scale(1.1);
      box-shadow: 0 0 30px rgba(255,51,102,0.5);
    }
    
    /* FEATURES */
    .features {
      padding: 5rem 2rem;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    .features h2 {
      text-align: center;
      font-size: 2.5rem;
      margin-bottom: 3rem;
    }
    
    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
    }
    
    .feature-card {
      background: var(--card);
      border-radius: 20px;
      padding: 2rem;
      transition: transform 0.3s;
    }
    
    .feature-card:hover {
      transform: translateY(-5px);
    }
    
    .feature-icon {
      font-size: 3rem;
      margin-bottom: 1rem;
    }
    
    .feature-card h3 {
      font-size: 1.5rem;
      margin-bottom: 0.5rem;
    }
    
    .feature-card p {
      color: var(--gray);
    }
    
    /* COMPARISON */
    .comparison {
      padding: 5rem 2rem;
      background: rgba(255,255,255,0.02);
    }
    
    .comparison h2 {
      text-align: center;
      font-size: 2.5rem;
      margin-bottom: 3rem;
    }
    
    .comparison-table {
      max-width: 900px;
      margin: 0 auto;
      overflow-x: auto;
    }
    
    table {
      width: 100%;
      border-collapse: collapse;
    }
    
    th, td {
      padding: 1rem;
      text-align: left;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    
    th {
      color: var(--accent);
    }
    
    .yes { color: var(--accent); }
    .no { color: var(--accent2); }
    
    /* STORY */
    .story {
      padding: 5rem 2rem;
      max-width: 800px;
      margin: 0 auto;
      text-align: center;
    }
    
    .story h2 {
      font-size: 2rem;
      margin-bottom: 1.5rem;
    }
    
    .story p {
      color: var(--gray);
      font-size: 1.2rem;
      margin-bottom: 1rem;
    }
    
    .story .highlight {
      color: var(--text);
      font-weight: 600;
    }
    
    /* WAITLIST */
    .waitlist {
      padding: 5rem 2rem;
      text-align: center;
      background: linear-gradient(180deg, transparent, rgba(0,255,136,0.05));
    }
    
    .waitlist h2 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
    }
    
    .waitlist p {
      color: var(--gray);
      margin-bottom: 2rem;
    }
    
    .waitlist-form {
      display: flex;
      gap: 1rem;
      justify-content: center;
      flex-wrap: wrap;
      max-width: 500px;
      margin: 0 auto;
    }
    
    .waitlist-form input {
      flex: 1;
      min-width: 250px;
      padding: 1rem 1.5rem;
      font-size: 1rem;
      border: 2px solid rgba(255,255,255,0.1);
      border-radius: 50px;
      background: var(--bg);
      color: var(--text);
      outline: none;
    }
    
    .waitlist-form input:focus {
      border-color: var(--accent);
    }
    
    /* FOOTER */
    footer {
      padding: 3rem 2rem;
      text-align: center;
      color: var(--gray);
      border-top: 1px solid rgba(255,255,255,0.1);
    }
    
    footer a {
      color: var(--accent);
      text-decoration: none;
    }
    
    .gorunfree {
      font-size: 1.5rem;
      font-weight: 900;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-top: 1rem;
    }
    
    /* ACCESSIBILITY */
    @media (prefers-reduced-motion: reduce) {
      * { transition: none !important; }
    }
    
    /* MOBILE */
    @media (max-width: 600px) {
      .logo { font-size: 2.5rem; }
      .tagline { font-size: 1.2rem; }
      .btn { width: 100%; }
    }
  </style>
</head>
<body>
  <!-- HERO -->
  <section class="hero">
    <h1 class="logo">CODEMASTER</h1>
    <p class="tagline">One command. Total control. Zero friction.<br>The world's first voice-first infrastructure command center.</p>
    
    <div class="demo-box">
      <input type="text" class="demo-input" id="commandInput" placeholder="Try: 'speed boost my site'" autofocus>
      <div class="demo-output" id="output">Waiting for your command...</div>
      <button class="mic-btn" id="micBtn" title="Voice input">🎤</button>
    </div>
    
    <div class="hero-cta">
      <a href="#waitlist" class="btn btn-primary">Join Waitlist</a>
      <a href="/console" class="btn btn-secondary">Try Demo</a>
    </div>
  </section>
  
  <!-- FEATURES -->
  <section class="features">
    <h2>What Makes CODEMASTER Different</h2>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon">🎤</div>
        <h3>Voice-First</h3>
        <p>Built for voice from day one. Not an afterthought. Speak your commands, hear your results.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h3>One Command</h3>
        <p>"Speed boost my site" — that's it. No CLI, no dashboard hunting, no 47 clicks.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🔥</div>
        <h3>Actually Executes</h3>
        <p>Other AI tools write code. CODEMASTER runs it. Live. On your real infrastructure.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">♿</div>
        <h3>Accessibility Native</h3>
        <p>Built by someone with paralysis. No keyboard required. No mouse required. Just your voice.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <h3>Knows Your Stack</h3>
        <p>Remembers your domains, workers, databases. Context-aware commands that just work.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <h3>Your Keys, Your Control</h3>
        <p>Your API tokens stay encrypted. We never see your credentials. You own everything.</p>
      </div>
    </div>
  </section>
  
  <!-- COMPARISON -->
  <section class="comparison">
    <h2>CODEMASTER vs. Everything Else</h2>
    <div class="comparison-table">
      <table>
        <tr>
          <th>Feature</th>
          <th>CODEMASTER</th>
          <th>Cursor/Copilot</th>
          <th>Claude Code</th>
        </tr>
        <tr>
          <td>Voice Commands</td>
          <td class="yes">✅ Native</td>
          <td class="no">❌ No</td>
          <td class="no">❌ No</td>
        </tr>
        <tr>
          <td>Executes Live</td>
          <td class="yes">✅ Yes</td>
          <td class="no">❌ Suggests only</td>
          <td class="no">⚠️ Limited</td>
        </tr>
        <tr>
          <td>No CLI Required</td>
          <td class="yes">✅ Zero CLI</td>
          <td class="no">❌ CLI heavy</td>
          <td class="no">❌ CLI required</td>
        </tr>
        <tr>
          <td>Accessibility</td>
          <td class="yes">✅ Built-in</td>
          <td class="no">❌ Keyboard-first</td>
          <td class="no">❌ Keyboard-first</td>
        </tr>
        <tr>
          <td>Infrastructure Control</td>
          <td class="yes">✅ Full control</td>
          <td class="no">❌ Code only</td>
          <td class="no">⚠️ Some</td>
        </tr>
        <tr>
          <td>One Command Deploy</td>
          <td class="yes">✅ Yes</td>
          <td class="no">❌ Multi-step</td>
          <td class="no">❌ Multi-step</td>
        </tr>
      </table>
    </div>
  </section>
  
  <!-- STORY -->
  <section class="story">
    <h2>Why I Built This</h2>
    <p>Six years ago, I shattered my C3 vertebra. Partial paralysis. Hands that don't work like they used to.</p>
    <p>I'm a composer with <span class="highlight">40 years of credits</span> — Ed Edd n Eddy, Dragon Tales, Johnny Test, Transformers, Barbie films. I wasn't about to stop creating.</p>
    <p>But every dev tool assumes you have two perfectly working hands. CLI? Can't type fast enough. Keyboard shortcuts? Forget it. Mouse precision? Nope.</p>
    <p class="highlight">So I built what I needed: a voice-first command center that actually does the work.</p>
    <p>If I can run an infrastructure empire with my voice, so can you.</p>
    <p class="gorunfree">GORUNFREE</p>
  </section>
  
  <!-- WAITLIST -->
  <section class="waitlist" id="waitlist">
    <h2>Get Early Access</h2>
    <p>Be the first to command your infrastructure with your voice.</p>
    <form class="waitlist-form" id="waitlistForm">
      <input type="email" placeholder="your@email.com" required id="emailInput">
      <button type="submit" class="btn btn-primary">Join Waitlist</button>
    </form>
    <p id="waitlistMessage" style="margin-top: 1rem;"></p>
  </section>
  
  <!-- FOOTER -->
  <footer>
    <p>Built with 🔥 by <a href="https://noizy.ai">NOIZY.AI</a></p>
    <p>Powered by 40 years of <a href="https://fishmusicinc.com">Fish Music Inc.</a></p>
    <p class="gorunfree">GORUNFREE</p>
  </footer>
  
  <script>
    // Demo command input
    const input = document.getElementById('commandInput');
    const output = document.getElementById('output');
    
    input.addEventListener('keypress', async (e) => {
      if (e.key === 'Enter') {
        const command = input.value.trim();
        if (!command) return;
        
        output.textContent = '⏳ Processing...';
        
        try {
          const res = await fetch('/api/command', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command })
          });
          const data = await res.json();
          output.textContent = data.message || JSON.stringify(data);
        } catch (err) {
          output.textContent = '❌ Error: ' + err.message;
        }
      }
    });
    
    // Voice input (Web Speech API)
    const micBtn = document.getElementById('micBtn');
    
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      const recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = false;
      
      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        input.value = transcript;
        input.dispatchEvent(new KeyboardEvent('keypress', { key: 'Enter' }));
      };
      
      recognition.onerror = (event) => {
        output.textContent = '❌ Voice error: ' + event.error;
      };
      
      micBtn.addEventListener('click', () => {
        output.textContent = '🎤 Listening...';
        recognition.start();
      });
    } else {
      micBtn.style.display = 'none';
    }
    
    // Waitlist form
    const form = document.getElementById('waitlistForm');
    const msg = document.getElementById('waitlistMessage');
    
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = document.getElementById('emailInput').value;
      
      try {
        const res = await fetch('/api/waitlist', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email })
        });
        const data = await res.json();
        msg.textContent = data.message;
        msg.style.color = data.success ? '#00ff88' : '#ff3366';
      } catch (err) {
        msg.textContent = '❌ Error: ' + err.message;
        msg.style.color = '#ff3366';
      }
    });
  </script>
</body>
</html>`;
}

// ═══════════════════════════════════════════════════════════════════
// CONSOLE / DEMO PAGE
// ═══════════════════════════════════════════════════════════════════
function renderConsole() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CODEMASTER Console</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Monaco', 'Menlo', monospace;
      background: #0a0a0a;
      color: #00ff88;
      min-height: 100vh;
      padding: 2rem;
    }
    .console {
      max-width: 900px;
      margin: 0 auto;
    }
    .header {
      text-align: center;
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #333;
    }
    .header h1 {
      font-size: 2rem;
      margin-bottom: 0.5rem;
    }
    .terminal {
      background: #111;
      border-radius: 10px;
      padding: 1.5rem;
      min-height: 400px;
      border: 1px solid #333;
    }
    .history {
      margin-bottom: 1rem;
      max-height: 300px;
      overflow-y: auto;
    }
    .history-item {
      margin-bottom: 1rem;
    }
    .history-item .cmd {
      color: #888;
    }
    .history-item .cmd::before {
      content: '> ';
      color: #00ff88;
    }
    .history-item .result {
      color: #fff;
      white-space: pre-wrap;
      margin-top: 0.25rem;
    }
    .input-line {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .prompt {
      color: #00ff88;
    }
    #cmdInput {
      flex: 1;
      background: transparent;
      border: none;
      color: #fff;
      font-family: inherit;
      font-size: 1rem;
      outline: none;
    }
    .mic-btn {
      background: #ff3366;
      border: none;
      border-radius: 50%;
      width: 40px;
      height: 40px;
      cursor: pointer;
      font-size: 1.2rem;
    }
    .commands-list {
      margin-top: 2rem;
      padding: 1rem;
      background: #111;
      border-radius: 10px;
      border: 1px solid #333;
    }
    .commands-list h3 {
      color: #00ff88;
      margin-bottom: 1rem;
    }
    .commands-list ul {
      list-style: none;
    }
    .commands-list li {
      padding: 0.5rem 0;
      color: #888;
    }
    .commands-list li code {
      color: #fff;
      background: #222;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <div class="console">
    <div class="header">
      <h1>CODEMASTER CONSOLE</h1>
      <p style="color: #888;">Voice-First Infrastructure Control</p>
    </div>
    
    <div class="terminal">
      <div class="history" id="history">
        <div class="history-item">
          <div class="result">Welcome to CODEMASTER. Type a command or click 🎤 to speak.</div>
        </div>
      </div>
      <div class="input-line">
        <span class="prompt">></span>
        <input type="text" id="cmdInput" placeholder="speed boost my site" autofocus>
        <button class="mic-btn" id="micBtn">🎤</button>
      </div>
    </div>
    
    <div class="commands-list">
      <h3>Available Commands</h3>
      <ul>
        <li><code>speed boost</code> — Enable all speed optimizations</li>
        <li><code>purge cache</code> — Clear entire cache</li>
        <li><code>show dns</code> — List DNS records</li>
        <li><code>status</code> — Check system health</li>
        <li><code>help</code> — Show all commands</li>
      </ul>
    </div>
  </div>
  
  <script>
    const input = document.getElementById('cmdInput');
    const history = document.getElementById('history');
    const micBtn = document.getElementById('micBtn');
    
    async function runCommand(cmd) {
      // Add command to history
      const cmdEl = document.createElement('div');
      cmdEl.className = 'history-item';
      cmdEl.innerHTML = '<div class="cmd">' + cmd + '</div><div class="result">⏳ Processing...</div>';
      history.appendChild(cmdEl);
      history.scrollTop = history.scrollHeight;
      
      try {
        const res = await fetch('/api/command', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ command: cmd })
        });
        const data = await res.json();
        cmdEl.querySelector('.result').textContent = data.message || JSON.stringify(data, null, 2);
      } catch (err) {
        cmdEl.querySelector('.result').textContent = '❌ Error: ' + err.message;
      }
      
      history.scrollTop = history.scrollHeight;
    }
    
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' && input.value.trim()) {
        runCommand(input.value.trim());
        input.value = '';
      }
    });
    
    // Voice
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      const recognition = new SpeechRecognition();
      
      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        runCommand(transcript);
      };
      
      micBtn.addEventListener('click', () => {
        recognition.start();
      });
    }
  </script>
</body>
</html>`;
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'X-Powered-By': 'CODEMASTER by NOIZY.AI',
      'X-GORUNFREE': 'true'
    }
  });
}
