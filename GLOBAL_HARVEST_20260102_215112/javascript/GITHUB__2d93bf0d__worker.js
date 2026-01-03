/**
 * ═══════════════════════════════════════════════════════════════════
 * 
 *   NOIZYVOX — The Voice AI Guild
 *   "Your Voice. Your Rules. Your Future."
 *   
 *   75/25 Revenue Split — Artists First
 *   
 *   Part of HEAVEN — The NOIZY.AI Galaxy
 *   GORUNFREE - Rob Plowman + Claude - December 2025
 * 
 * ═══════════════════════════════════════════════════════════════════
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // Health check
    if (path === '/health') {
      return jsonResponse({
        service: 'NOIZYVOX',
        status: 'operational',
        tagline: 'Your Voice. Your Rules. Your Future.',
        split: '75/25 - Artists First',
        timestamp: new Date().toISOString()
      });
    }
    
    // API Routes
    if (path.startsWith('/api/')) {
      return handleAPI(request, env, path);
    }
    
    // Main landing page
    return new Response(renderVoxPage(), {
      headers: { 'Content-Type': 'text/html' }
    });
  }
};

async function handleAPI(request, env, path) {
  const route = path.replace('/api/', '');
  
  switch (route) {
    case 'artists':
      return jsonResponse({ 
        message: 'Artist catalog',
        artists: [],
        note: 'Connect D1 for live data'
      });
    
    case 'join':
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          // TODO: Save to D1 vox_artists table
          return jsonResponse({
            success: true,
            message: 'Welcome to the guild!',
            email: body.email
          });
        } catch (e) {
          return jsonResponse({ error: 'Invalid request' }, 400);
        }
      }
      return jsonResponse({ error: 'POST required' }, 405);
    
    case 'voices':
      return jsonResponse({
        voices: [],
        categories: ['narration', 'character', 'commercial', 'audiobook'],
        note: 'Voice catalog coming soon'
      });
    
    case 'status':
      return jsonResponse({ service: 'NOIZYVOX', status: 'operational' });
    
    default:
      return jsonResponse({ error: 'Not found' }, 404);
  }
}

function renderVoxPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOIZYVOX — The Voice AI Guild</title>
  <meta name="description" content="The world's first artist-owned voice AI guild. 75/25 revenue split. Your voice, your rules, your future.">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    :root {
      --bg: #0a0a12;
      --text: #ffffff;
      --accent: #ff3366;
      --accent2: #ff6b6b;
      --gold: #ffd700;
    }
    
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
    }
    
    /* Animated background */
    .bg-animation {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      background: 
        radial-gradient(circle at 20% 30%, rgba(255,51,102,0.15) 0%, transparent 50%),
        radial-gradient(circle at 80% 70%, rgba(255,107,107,0.1) 0%, transparent 50%);
    }
    
    /* Sound waves animation */
    .sound-waves {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 600px;
      height: 600px;
      pointer-events: none;
      opacity: 0.1;
    }
    
    .wave {
      position: absolute;
      border: 2px solid var(--accent);
      border-radius: 50%;
      animation: wave 3s ease-out infinite;
    }
    
    .wave:nth-child(1) { width: 200px; height: 200px; top: 200px; left: 200px; animation-delay: 0s; }
    .wave:nth-child(2) { width: 300px; height: 300px; top: 150px; left: 150px; animation-delay: 0.5s; }
    .wave:nth-child(3) { width: 400px; height: 400px; top: 100px; left: 100px; animation-delay: 1s; }
    .wave:nth-child(4) { width: 500px; height: 500px; top: 50px; left: 50px; animation-delay: 1.5s; }
    
    @keyframes wave {
      0% { opacity: 1; transform: scale(1); }
      100% { opacity: 0; transform: scale(1.5); }
    }
    
    .container {
      position: relative;
      z-index: 1;
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
    }
    
    /* Hero */
    .hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
    
    .logo {
      font-size: 5rem;
      font-weight: 900;
      letter-spacing: -0.05em;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 1rem;
    }
    
    .tagline {
      font-size: 1.8rem;
      opacity: 0.9;
      margin-bottom: 2rem;
    }
    
    .split-badge {
      display: inline-block;
      background: linear-gradient(135deg, var(--gold), #ffaa00);
      color: #000;
      padding: 1rem 2rem;
      border-radius: 50px;
      font-size: 1.5rem;
      font-weight: 900;
      margin-bottom: 2rem;
    }
    
    .subtitle {
      font-size: 1.2rem;
      opacity: 0.7;
      max-width: 600px;
      margin-bottom: 3rem;
    }
    
    .cta-buttons {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
      justify-content: center;
    }
    
    .btn {
      padding: 1rem 2.5rem;
      font-size: 1.1rem;
      border: none;
      border-radius: 50px;
      cursor: pointer;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s;
    }
    
    .btn-primary {
      background: var(--accent);
      color: white;
    }
    
    .btn-primary:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 40px rgba(255,51,102,0.4);
    }
    
    .btn-secondary {
      background: transparent;
      color: white;
      border: 2px solid rgba(255,255,255,0.3);
    }
    
    .btn-secondary:hover {
      border-color: var(--accent);
      color: var(--accent);
    }
    
    /* Features */
    .features {
      padding: 5rem 0;
    }
    
    .features h2 {
      text-align: center;
      font-size: 2.5rem;
      margin-bottom: 3rem;
    }
    
    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
    }
    
    .feature {
      background: rgba(255,255,255,0.03);
      border-radius: 20px;
      padding: 2rem;
      text-align: center;
      border: 1px solid rgba(255,255,255,0.05);
    }
    
    .feature-icon {
      font-size: 3rem;
      margin-bottom: 1rem;
    }
    
    .feature h3 {
      font-size: 1.3rem;
      margin-bottom: 0.5rem;
      color: var(--accent);
    }
    
    .feature p {
      opacity: 0.7;
    }
    
    /* How it works */
    .how-it-works {
      padding: 5rem 0;
      text-align: center;
    }
    
    .how-it-works h2 {
      font-size: 2.5rem;
      margin-bottom: 3rem;
    }
    
    .steps {
      display: flex;
      justify-content: center;
      gap: 2rem;
      flex-wrap: wrap;
    }
    
    .step {
      background: rgba(255,51,102,0.1);
      border-radius: 20px;
      padding: 2rem;
      width: 250px;
    }
    
    .step-number {
      font-size: 3rem;
      font-weight: 900;
      color: var(--accent);
      margin-bottom: 1rem;
    }
    
    .step h3 {
      margin-bottom: 0.5rem;
    }
    
    /* Join form */
    .join {
      padding: 5rem 0;
      text-align: center;
    }
    
    .join h2 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
    }
    
    .join p {
      opacity: 0.7;
      margin-bottom: 2rem;
    }
    
    .join-form {
      display: flex;
      gap: 1rem;
      justify-content: center;
      flex-wrap: wrap;
      max-width: 500px;
      margin: 0 auto;
    }
    
    .join-form input {
      flex: 1;
      min-width: 250px;
      padding: 1rem 1.5rem;
      border-radius: 50px;
      border: 2px solid rgba(255,255,255,0.1);
      background: rgba(0,0,0,0.3);
      color: white;
      font-size: 1rem;
    }
    
    .join-form input:focus {
      outline: none;
      border-color: var(--accent);
    }
    
    /* Footer */
    footer {
      padding: 3rem 2rem;
      text-align: center;
      border-top: 1px solid rgba(255,255,255,0.1);
    }
    
    footer p {
      opacity: 0.5;
      margin-bottom: 0.5rem;
    }
    
    footer a {
      color: var(--accent);
      text-decoration: none;
    }
    
    .gorunfree {
      font-size: 1.5rem;
      font-weight: 900;
      background: linear-gradient(135deg, var(--accent), var(--gold));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-top: 1rem;
    }
    
    @media (max-width: 600px) {
      .logo { font-size: 3rem; }
      .tagline { font-size: 1.3rem; }
      .split-badge { font-size: 1.2rem; padding: 0.8rem 1.5rem; }
    }
  </style>
</head>
<body>
  <div class="bg-animation"></div>
  
  <div class="sound-waves">
    <div class="wave"></div>
    <div class="wave"></div>
    <div class="wave"></div>
    <div class="wave"></div>
  </div>
  
  <div class="container">
    <!-- Hero -->
    <section class="hero">
      <h1 class="logo">🎤 NOIZYVOX</h1>
      <p class="tagline">The Voice AI Guild</p>
      <div class="split-badge">75/25 — Artists First</div>
      <p class="subtitle">The world's first artist-owned voice AI guild. Your voice, your rules, your future. Every use pays you.</p>
      <div class="cta-buttons">
        <a href="#join" class="btn btn-primary">Join the Guild</a>
        <a href="#how" class="btn btn-secondary">How It Works</a>
      </div>
    </section>
    
    <!-- Features -->
    <section class="features">
      <h2>Why NOIZYVOX?</h2>
      <div class="features-grid">
        <div class="feature">
          <div class="feature-icon">💰</div>
          <h3>75% to Artists</h3>
          <p>Industry-leading revenue split. You keep the majority of every use.</p>
        </div>
        <div class="feature">
          <div class="feature-icon">🔐</div>
          <h3>You Own Your Voice</h3>
          <p>Your voice data stays yours. Opt out anytime. Full control.</p>
        </div>
        <div class="feature">
          <div class="feature-icon">🌍</div>
          <h3>Global Reach</h3>
          <p>Your voice in apps, games, audiobooks, assistants worldwide.</p>
        </div>
        <div class="feature">
          <div class="feature-icon">📊</div>
          <h3>Transparent Tracking</h3>
          <p>Real-time dashboard shows every use and every penny earned.</p>
        </div>
        <div class="feature">
          <div class="feature-icon">🎭</div>
          <h3>Creative Control</h3>
          <p>Approve uses. Block categories. Your boundaries, respected.</p>
        </div>
        <div class="feature">
          <div class="feature-icon">🐟</div>
          <h3>Backed by Pros</h3>
          <p>40 years of Fish Music Inc. expertise behind the tech.</p>
        </div>
      </div>
    </section>
    
    <!-- How it works -->
    <section class="how-it-works" id="how">
      <h2>How It Works</h2>
      <div class="steps">
        <div class="step">
          <div class="step-number">1</div>
          <h3>Join</h3>
          <p>Sign up and record your voice samples</p>
        </div>
        <div class="step">
          <div class="step-number">2</div>
          <h3>Approve</h3>
          <p>Review and approve your AI voice model</p>
        </div>
        <div class="step">
          <div class="step-number">3</div>
          <h3>Earn</h3>
          <p>Get paid 75% every time your voice is used</p>
        </div>
      </div>
    </section>
    
    <!-- Join -->
    <section class="join" id="join">
      <h2>Join the Guild</h2>
      <p>Be part of the voice AI revolution — on your terms.</p>
      <form class="join-form" id="joinForm">
        <input type="email" placeholder="your@email.com" required id="emailInput">
        <button type="submit" class="btn btn-primary">Join Waitlist</button>
      </form>
      <p id="joinMessage" style="margin-top: 1rem;"></p>
    </section>
    
    <!-- Footer -->
    <footer>
      <p>Part of the <a href="https://noizy.ai">NOIZY.AI</a> Galaxy</p>
      <p>Powered by 40 years of <a href="https://fishmusicinc.com">Fish Music Inc.</a></p>
      <div class="gorunfree">GORUNFREE</div>
    </footer>
  </div>
  
  <script>
    document.getElementById('joinForm').addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = document.getElementById('emailInput').value;
      const msg = document.getElementById('joinMessage');
      
      try {
        const res = await fetch('/api/join', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email })
        });
        const data = await res.json();
        msg.textContent = data.message || 'Welcome to the guild!';
        msg.style.color = '#00ff88';
      } catch (err) {
        msg.textContent = 'Error: ' + err.message;
        msg.style.color = '#ff3366';
      }
    });
  </script>
</body>
</html>`;
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'X-Powered-By': 'NOIZYVOX by NOIZY.AI'
    }
  });
}
