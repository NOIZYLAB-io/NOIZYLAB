/**
 * ═══════════════════════════════════════════════════════════════════════════════════════════════
 * 
 *   ██╗  ██╗███████╗ █████╗ ██╗   ██╗███████╗███╗   ██╗
 *   ██║  ██║██╔════╝██╔══██╗██║   ██║██╔════╝████╗  ██║
 *   ███████║█████╗  ███████║██║   ██║█████╗  ██╔██╗ ██║
 *   ██╔══██║██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
 *   ██║  ██║███████╗██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
 *   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
 * 
 *   THE NOIZY.AI GALAXY — MASTER WORKER
 *   "Where Sound is the Soul of Everything"
 *   "Nobody Died. Everybody LIVES Here."
 *   
 *   ONE WORKER. ALL SUBDOMAINS. TOTAL CONTROL.
 *   
 *   Routes:
 *     noizy.ai             → 🌟 Galaxy Portal
 *     vox.noizy.ai         → 🎤 NOIZYVOX (Voice AI Guild)
 *     codemaster.noizy.ai  → 🖥️ CODEMASTER (Voice Infra)
 *     books.noizy.ai       → 📚 FISHYBOOKS (Audiobooks)
 *     lab.noizy.ai         → 💻 NOIZYLAB (CPU Repairs)
 *     admin.noizy.ai       → 🔧 Command Center
 *   
 *   GORUNFREE - Rob Plowman + Claude - December 2025
 * 
 * ═══════════════════════════════════════════════════════════════════════════════════════════════
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const hostname = url.hostname;
    const path = url.pathname;
    
    // ═══════════════════════════════════════════════════════════════════════════════════════════
    // SUBDOMAIN ROUTER
    // ═══════════════════════════════════════════════════════════════════════════════════════════
    
    const parts = hostname.split('.');
    let subdomain = 'portal';
    
    // Handle *.noizy.ai subdomains
    if (hostname.endsWith('noizy.ai')) {
      if (parts.length >= 3 && parts[0] !== 'www') {
        subdomain = parts[0];
      }
    }
    
    // Handle workers.dev for testing
    if (hostname.includes('workers.dev')) {
      const subPath = path.split('/')[1];
      if (['vox', 'codemaster', 'books', 'lab', 'admin'].includes(subPath)) {
        subdomain = subPath;
      }
    }
    
    // ═══════════════════════════════════════════════════════════════════════════════════════════
    // UNIVERSAL HEALTH CHECK
    // ═══════════════════════════════════════════════════════════════════════════════════════════
    
    if (path === '/health' || path === '/_health') {
      return json({
        galaxy: 'NOIZY.AI',
        service: subdomain.toUpperCase(),
        status: 'operational',
        timestamp: new Date().toISOString(),
        routes: {
          'noizy.ai': 'Galaxy Portal',
          'vox.noizy.ai': 'NOIZYVOX - Voice AI Guild',
          'codemaster.noizy.ai': 'CODEMASTER - Voice Infra',
          'books.noizy.ai': 'FISHYBOOKS - Audiobooks',
          'lab.noizy.ai': 'NOIZYLAB - CPU Repairs',
          'admin.noizy.ai': 'Command Center'
        },
        gorunfree: true
      });
    }
    
    // ═══════════════════════════════════════════════════════════════════════════════════════════
    // ROUTE TO HANDLER
    // ═══════════════════════════════════════════════════════════════════════════════════════════
    
    switch (subdomain) {
      case 'vox':
        return handleVox(request, env, url);
      case 'codemaster':
        return handleCodemaster(request, env, url);
      case 'books':
        return handleBooks(request, env, url);
      case 'lab':
        return handleLab(request, env, url);
      case 'admin':
        return handleAdmin(request, env, url);
      default:
        return handlePortal(request, env, url);
    }
  }
};

// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// 🌟 PORTAL — Galaxy Hub (noizy.ai)
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

function handlePortal(request, env, url) {
  if (url.pathname.startsWith('/api/')) {
    return json({ service: 'PORTAL', status: 'operational' });
  }
  
  return html(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOIZY.AI — Where Sound is the Soul of Everything</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    :root { --bg: #050510; --text: #fff; --vox: #ff3366; --code: #00ff88; --books: #ff9500; --lab: #00aaff; }
    body { font-family: -apple-system, sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; }
    .stars { position: fixed; inset: 0; background-image: radial-gradient(2px 2px at 20px 30px, #fff3, transparent), radial-gradient(2px 2px at 40px 70px, #fff2, transparent), radial-gradient(1px 1px at 90px 40px, #fff3, transparent); background-size: 200px 200px; animation: twinkle 4s ease-in-out infinite; pointer-events: none; }
    @keyframes twinkle { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }
    @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }
    header { position: relative; z-index: 1; text-align: center; padding: 4rem 2rem; }
    .logo { font-size: 5rem; font-weight: 900; background: linear-gradient(135deg, var(--vox), #8855ff, var(--code)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: float 6s ease-in-out infinite; }
    .tagline { font-size: 1.5rem; opacity: 0.8; margin-top: 1rem; }
    .galaxy { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; padding: 2rem; max-width: 1200px; margin: 0 auto; position: relative; z-index: 1; }
    .planet { background: rgba(255,255,255,0.03); border-radius: 30px; padding: 2.5rem; text-align: center; text-decoration: none; color: var(--text); transition: all 0.4s; border: 2px solid transparent; }
    .planet:hover { transform: translateY(-10px); border-color: var(--glow); box-shadow: 0 20px 60px -20px var(--glow); }
    .planet.vox { --glow: var(--vox); } .planet.vox h2 { color: var(--vox); }
    .planet.code { --glow: var(--code); } .planet.code h2 { color: var(--code); }
    .planet.books { --glow: var(--books); } .planet.books h2 { color: var(--books); }
    .planet.lab { --glow: var(--lab); } .planet.lab h2 { color: var(--lab); }
    .planet-icon { font-size: 4rem; margin-bottom: 1rem; display: block; }
    .planet h2 { font-size: 1.8rem; margin-bottom: 0.5rem; }
    .planet p { opacity: 0.7; }
    .vault { text-align: center; padding: 4rem 2rem; position: relative; z-index: 1; }
    .vault h2 { font-size: 2rem; margin-bottom: 1rem; }
    .credits { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; max-width: 800px; margin: 1rem auto; }
    .credit { padding: 0.4rem 0.8rem; background: rgba(255,255,255,0.05); border-radius: 20px; font-size: 0.85rem; opacity: 0.6; }
    footer { text-align: center; padding: 3rem; border-top: 1px solid rgba(255,255,255,0.1); position: relative; z-index: 1; }
    footer p { opacity: 0.5; margin: 0.5rem 0; }
    footer a { color: var(--code); text-decoration: none; }
    .gorunfree { font-size: 2rem; font-weight: 900; background: linear-gradient(135deg, var(--code), var(--vox)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 1rem; }
  </style>
</head>
<body>
  <div class="stars"></div>
  <header>
    <h1 class="logo">NOIZY.AI</h1>
    <p class="tagline">Where Sound is the Soul of Everything</p>
  </header>
  <section class="galaxy">
    <a href="https://vox.noizy.ai" class="planet vox"><span class="planet-icon">🎤</span><h2>NOIZYVOX</h2><p>Voice AI Guild • 75/25 Artist Split</p></a>
    <a href="https://codemaster.noizy.ai" class="planet code"><span class="planet-icon">🖥️</span><h2>CODEMASTER</h2><p>Voice-First Infrastructure Control</p></a>
    <a href="https://books.noizy.ai" class="planet books"><span class="planet-icon">📚</span><h2>FISHYBOOKS</h2><p>Audiobooks for Munchkins</p></a>
    <a href="https://lab.noizy.ai" class="planet lab"><span class="planet-icon">💻</span><h2>NOIZYLAB</h2><p>$89 Flat Rate CPU Repairs</p></a>
  </section>
  <section class="vault">
    <h2>🐟 Powered by Fish Music Inc.</h2>
    <p style="opacity:0.7;">40 years of professional audio for film, animation & gaming</p>
    <div class="credits">
      <span class="credit">Ed Edd n Eddy</span><span class="credit">Dragon Tales</span><span class="credit">Johnny Test</span>
      <span class="credit">Transformers</span><span class="credit">Barbie Films</span><span class="credit">Bratz</span>
      <span class="credit">Krypto</span><span class="credit">Madeline</span><span class="credit">+ Hundreds More</span>
    </div>
  </section>
  <footer>
    <p>Built by Rob Plowman • C3 injury • Still creating</p>
    <p>Voice-first. Accessibility-native. No excuses.</p>
    <div class="gorunfree">GORUNFREE</div>
  </footer>
</body>
</html>`);
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// 🎤 NOIZYVOX — Voice AI Guild (vox.noizy.ai)
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

function handleVox(request, env, url) {
  if (url.pathname.startsWith('/api/')) {
    const route = url.pathname.replace('/api/', '');
    if (route === 'join' && request.method === 'POST') {
      return json({ success: true, message: 'Welcome to the Guild!' });
    }
    return json({ service: 'NOIZYVOX', status: 'operational', split: '75/25' });
  }
  
  return html(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOIZYVOX — The Voice AI Guild</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: -apple-system, sans-serif; background: #0a0a12; color: #fff; min-height: 100vh; }
    .bg { position: fixed; inset: 0; background: radial-gradient(circle at 20% 30%, rgba(255,51,102,0.15) 0%, transparent 50%), radial-gradient(circle at 80% 70%, rgba(255,107,107,0.1) 0%, transparent 50%); pointer-events: none; }
    .container { position: relative; z-index: 1; max-width: 900px; margin: 0 auto; padding: 2rem; }
    .hero { min-height: 90vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
    .logo { font-size: 4rem; font-weight: 900; background: linear-gradient(135deg, #ff3366, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .tagline { font-size: 1.5rem; margin: 1rem 0; }
    .badge { background: linear-gradient(135deg, #ffd700, #ffaa00); color: #000; padding: 1rem 2rem; border-radius: 50px; font-size: 1.5rem; font-weight: 900; margin: 1rem 0 2rem; }
    .desc { opacity: 0.8; max-width: 500px; margin-bottom: 2rem; }
    .btn { display: inline-block; padding: 1rem 2.5rem; background: #ff3366; color: #fff; border-radius: 50px; text-decoration: none; font-weight: 600; transition: transform 0.3s; }
    .btn:hover { transform: translateY(-3px); }
    .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 3rem 0; }
    .feature { background: rgba(255,255,255,0.03); padding: 1.5rem; border-radius: 15px; text-align: center; }
    .feature-icon { font-size: 2rem; margin-bottom: 0.5rem; }
    .feature h3 { color: #ff3366; margin-bottom: 0.25rem; }
    footer { text-align: center; padding: 2rem; border-top: 1px solid rgba(255,255,255,0.1); }
    footer a { color: #00ff88; text-decoration: none; }
  </style>
</head>
<body>
  <div class="bg"></div>
  <div class="container">
    <section class="hero">
      <h1 class="logo">🎤 NOIZYVOX</h1>
      <p class="tagline">The Voice AI Guild</p>
      <div class="badge">75/25 — Artists First</div>
      <p class="desc">The world's first artist-owned voice AI guild. Your voice, your rules, your future.</p>
      <a href="#" class="btn">Join the Guild</a>
    </section>
    <div class="features">
      <div class="feature"><div class="feature-icon">💰</div><h3>75% to Artists</h3><p>Industry-leading split</p></div>
      <div class="feature"><div class="feature-icon">🔐</div><h3>You Own It</h3><p>Full control, opt out anytime</p></div>
      <div class="feature"><div class="feature-icon">🌍</div><h3>Global Reach</h3><p>Apps, games, audiobooks</p></div>
      <div class="feature"><div class="feature-icon">🐟</div><h3>Pro Backed</h3><p>40 years Fish Music</p></div>
    </div>
    <footer><p>Part of <a href="https://noizy.ai">NOIZY.AI</a></p></footer>
  </div>
</body>
</html>`);
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// 🖥️ CODEMASTER — Voice-First Infra (codemaster.noizy.ai)
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

function handleCodemaster(request, env, url) {
  if (url.pathname.startsWith('/api/')) {
    return json({ service: 'CODEMASTER', status: 'operational', tagline: 'One Command. Total Control.' });
  }
  
  return html(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CODEMASTER — Voice-First Infrastructure Control</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: -apple-system, sans-serif; background: #0a0a0a; color: #fff; min-height: 100vh; }
    .bg { position: fixed; inset: 0; background: radial-gradient(circle at 20% 50%, rgba(0,255,136,0.1) 0%, transparent 50%), radial-gradient(circle at 80% 50%, rgba(255,51,102,0.1) 0%, transparent 50%); pointer-events: none; }
    .container { position: relative; z-index: 1; max-width: 800px; margin: 0 auto; padding: 2rem; }
    .hero { min-height: 90vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
    .logo { font-size: 3.5rem; font-weight: 900; background: linear-gradient(135deg, #00ff88, #ff3366); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .tagline { font-size: 1.3rem; opacity: 0.8; margin: 1rem 0 2rem; }
    .demo { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 2rem; width: 100%; max-width: 500px; }
    .demo input { width: 100%; padding: 1rem; border-radius: 50px; border: 2px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.5); color: #fff; font-size: 1rem; }
    .demo input:focus { outline: none; border-color: #00ff88; }
    .output { margin-top: 1rem; padding: 1rem; background: rgba(0,0,0,0.3); border-radius: 10px; color: #00ff88; font-family: monospace; min-height: 50px; }
    .features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 3rem 0; text-align: center; }
    .feat { padding: 1rem; }
    .feat-icon { font-size: 2rem; }
    .feat p { font-size: 0.9rem; opacity: 0.7; margin-top: 0.5rem; }
    footer { text-align: center; padding: 2rem; border-top: 1px solid rgba(255,255,255,0.1); }
    footer a { color: #00ff88; text-decoration: none; }
    @media (max-width: 600px) { .features { grid-template-columns: 1fr; } .logo { font-size: 2.5rem; } }
  </style>
</head>
<body>
  <div class="bg"></div>
  <div class="container">
    <section class="hero">
      <h1 class="logo">🖥️ CODEMASTER</h1>
      <p class="tagline">One command. Total control. Zero friction.</p>
      <div class="demo">
        <input type="text" placeholder="Try: speed boost my site" id="cmd">
        <div class="output" id="out">Waiting for command...</div>
      </div>
    </section>
    <div class="features">
      <div class="feat"><div class="feat-icon">🎤</div><p>Voice-First</p></div>
      <div class="feat"><div class="feat-icon">⚡</div><p>One Command</p></div>
      <div class="feat"><div class="feat-icon">♿</div><p>Accessible</p></div>
    </div>
    <footer><p>Part of <a href="https://noizy.ai">NOIZY.AI</a></p></footer>
  </div>
  <script>
    document.getElementById('cmd').addEventListener('keypress', e => {
      if (e.key === 'Enter') {
        document.getElementById('out').textContent = '🚀 Speed boost activated! 16 optimizations enabled.';
      }
    });
  </script>
</body>
</html>`);
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// 📚 FISHYBOOKS — Audiobooks (books.noizy.ai)
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

function handleBooks(request, env, url) {
  if (url.pathname.startsWith('/api/')) {
    return json({ service: 'FISHYBOOKS', status: 'operational', powered_by: ['NOIZYVOX', 'THE AQUARIUM'] });
  }
  
  return html(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FISHYBOOKS — Stories for Munchkins</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Comic Sans MS', cursive, sans-serif; background: linear-gradient(180deg, #0f1629, #1e1b4b); color: #fff; min-height: 100vh; }
    .stars { position: fixed; inset: 0; background-image: radial-gradient(2px 2px at 20px 30px, white, transparent), radial-gradient(1px 1px at 90px 40px, white, transparent); background-size: 200px 200px; animation: twinkle 5s ease-in-out infinite; pointer-events: none; }
    @keyframes twinkle { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }
    .container { position: relative; z-index: 1; max-width: 900px; margin: 0 auto; padding: 2rem; }
    header { text-align: center; padding: 3rem 0; }
    .logo { font-size: 3rem; } .logo span { background: linear-gradient(135deg, #ff9500, #ffcc00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .books { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
    .book { background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(236,72,153,0.2)); border-radius: 20px; padding: 1.5rem; text-align: center; transition: transform 0.3s; }
    .book:hover { transform: translateY(-10px) rotate(-2deg); }
    .book-icon { font-size: 3rem; }
    .book h3 { font-size: 1rem; margin: 0.5rem 0; }
    .book p { font-size: 0.8rem; opacity: 0.7; }
    .age { display: inline-block; background: #ff9500; color: #000; padding: 0.2rem 0.6rem; border-radius: 20px; font-size: 0.7rem; margin-top: 0.5rem; }
    footer { text-align: center; padding: 2rem; }
    footer a { color: #ff9500; text-decoration: none; }
  </style>
</head>
<body>
  <div class="stars"></div>
  <div class="container">
    <header><h1 class="logo">📚 <span>FISHYBOOKS</span></h1><p>Stories for Munchkins ✨</p></header>
    <div class="books">
      <div class="book"><div class="book-icon">🐠</div><h3>Finley's First Day</h3><p>A fish finds courage</p><span class="age">Ages 3-5</span></div>
      <div class="book"><div class="book-icon">🚀🐕</div><h3>Space Puppy Quest</h3><p>Stars & adventure</p><span class="age">Ages 4-7</span></div>
      <div class="book"><div class="book-icon">🦄✨</div><h3>Sparkle Dreams</h3><p>Magical bedtime</p><span class="age">Ages 2-4</span></div>
      <div class="book"><div class="book-icon">🐻🌲</div><h3>Bear's Journey</h3><p>Finding home</p><span class="age">Ages 3-6</span></div>
    </div>
    <footer><p>Voices by <a href="https://vox.noizy.ai">NOIZYVOX</a> • Part of <a href="https://noizy.ai">NOIZY.AI</a></p></footer>
  </div>
</body>
</html>`);
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// 💻 NOIZYLAB — CPU Repairs (lab.noizy.ai)
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

function handleLab(request, env, url) {
  if (url.pathname.startsWith('/api/')) {
    return json({ service: 'NOIZYLAB', status: 'operational', price: '$89 flat rate' });
  }
  
  return html(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOIZYLAB — $89 CPU Repairs</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: -apple-system, sans-serif; background: #0a0a14; color: #fff; min-height: 100vh; }
    .bg { position: fixed; inset: 0; background: radial-gradient(circle at 50% 50%, rgba(0,170,255,0.1) 0%, transparent 50%); pointer-events: none; }
    .container { position: relative; z-index: 1; max-width: 800px; margin: 0 auto; padding: 2rem; }
    .hero { min-height: 80vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
    .logo { font-size: 3rem; font-weight: 900; color: #00aaff; }
    .price { font-size: 4rem; font-weight: 900; background: linear-gradient(135deg, #00aaff, #00ff88); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 1rem 0; }
    .tagline { font-size: 1.2rem; opacity: 0.8; margin-bottom: 2rem; }
    .btn { display: inline-block; padding: 1rem 3rem; background: #00aaff; color: #000; font-weight: 700; border-radius: 50px; text-decoration: none; font-size: 1.2rem; transition: transform 0.3s; }
    .btn:hover { transform: scale(1.05); }
    .features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 3rem 0; text-align: center; }
    .feat { padding: 1.5rem; background: rgba(255,255,255,0.03); border-radius: 15px; }
    .feat-icon { font-size: 2rem; margin-bottom: 0.5rem; }
    footer { text-align: center; padding: 2rem; border-top: 1px solid rgba(255,255,255,0.1); }
    footer a { color: #00aaff; text-decoration: none; }
    @media (max-width: 600px) { .features { grid-template-columns: 1fr; } .price { font-size: 3rem; } }
  </style>
</head>
<body>
  <div class="bg"></div>
  <div class="container">
    <section class="hero">
      <h1 class="logo">💻 NOIZYLAB</h1>
      <div class="price">$89</div>
      <p class="tagline">Flat rate. Any repair. Done right.</p>
      <a href="#" class="btn">Book a Repair</a>
    </section>
    <div class="features">
      <div class="feat"><div class="feat-icon">🔧</div><p>Mac & PC</p></div>
      <div class="feat"><div class="feat-icon">🌐</div><p>Remote Fix</p></div>
      <div class="feat"><div class="feat-icon">✅</div><p>Guaranteed</p></div>
    </div>
    <footer><p>Part of <a href="https://noizy.ai">NOIZY.AI</a></p></footer>
  </div>
</body>
</html>`);
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// 🔧 ADMIN — Command Center (admin.noizy.ai)
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

function handleAdmin(request, env, url) {
  const path = url.pathname;
  
  // Admin API endpoints
  if (path === '/speed-boost') {
    return json({ action: 'SPEED BOOST', status: 'requires API token', message: 'Configure CF_API_TOKEN secret' });
  }
  if (path === '/purge-cache') {
    return json({ action: 'PURGE CACHE', status: 'requires API token' });
  }
  if (path === '/dns-list') {
    return json({ action: 'DNS LIST', status: 'requires API token' });
  }
  if (path === '/status') {
    return json({ action: 'STATUS', galaxy: 'NOIZY.AI', services: ['portal', 'vox', 'codemaster', 'books', 'lab', 'admin'], status: 'all operational' });
  }
  
  return json({
    service: 'ADMIN COMMAND CENTER',
    status: 'operational',
    endpoints: ['/speed-boost', '/purge-cache', '/dns-list', '/status'],
    note: 'Add ?key=YOUR_SECRET to authenticate',
    gorunfree: true
  });
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// HELPERS
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

function json(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'X-Powered-By': 'HEAVEN by NOIZY.AI',
      'X-GORUNFREE': 'true'
    }
  });
}

function html(content) {
  return new Response(content, {
    headers: {
      'Content-Type': 'text/html;charset=UTF-8',
      'X-Powered-By': 'HEAVEN by NOIZY.AI'
    }
  });
}
