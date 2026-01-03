/**
 * ═══════════════════════════════════════════════════════════════════
 * 
 *   N O I Z Y . A I   G A L A X Y   P O R T A L
 *   
 *   "Where Sound is the Soul of Everything"
 *   
 *   The central hub connecting all NOIZY.AI products.
 *   Every interaction has sound. Every sound has soul.
 *   
 *   GORUNFREE - Rob Plowman + Claude - December 2025
 * 
 * ═══════════════════════════════════════════════════════════════════
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    if (url.pathname === '/health') {
      return jsonResponse({ status: 'NOIZY GALAXY ONLINE', gorunfree: true });
    }
    
    return new Response(renderGalaxyPortal(), {
      headers: { 'Content-Type': 'text/html' }
    });
  }
};

function renderGalaxyPortal() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOIZY.AI — Where Sound is the Soul of Everything</title>
  <meta name="description" content="The NOIZY.AI Galaxy - Voice AI, Infrastructure Control, Children's Audiobooks, and more. All powered by 40 years of Fish Music.">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    :root {
      --bg: #050510;
      --text: #ffffff;
      --vox: #ff3366;
      --code: #00ff88;
      --books: #ff9500;
      --lab: #00aaff;
      --portal: #8855ff;
    }
    
    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-20px); }
    }
    
    @keyframes pulse {
      0%, 100% { opacity: 0.5; }
      50% { opacity: 1; }
    }
    
    @keyframes rotate {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
    }
    
    /* STARFIELD BACKGROUND */
    .stars {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      background: 
        radial-gradient(2px 2px at 20px 30px, #fff, transparent),
        radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.8), transparent),
        radial-gradient(1px 1px at 90px 40px, #fff, transparent),
        radial-gradient(2px 2px at 160px 120px, rgba(255,255,255,0.9), transparent),
        radial-gradient(1px 1px at 230px 80px, #fff, transparent),
        radial-gradient(2px 2px at 300px 150px, rgba(255,255,255,0.7), transparent);
      background-size: 350px 200px;
      animation: pulse 4s ease-in-out infinite;
    }
    
    /* SOUND VISUALIZER */
    .visualizer {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 100px;
      display: flex;
      align-items: flex-end;
      justify-content: center;
      gap: 4px;
      opacity: 0.3;
      pointer-events: none;
    }
    
    .bar {
      width: 4px;
      background: linear-gradient(to top, var(--vox), var(--code));
      border-radius: 2px;
      animation: soundbar 0.5s ease-in-out infinite alternate;
    }
    
    @keyframes soundbar {
      to { height: var(--h); }
    }
    
    /* HEADER */
    header {
      position: relative;
      text-align: center;
      padding: 4rem 2rem;
    }
    
    .logo {
      font-size: 5rem;
      font-weight: 900;
      letter-spacing: -0.05em;
      background: linear-gradient(135deg, var(--vox), var(--portal), var(--code));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 1rem;
      animation: float 6s ease-in-out infinite;
    }
    
    .tagline {
      font-size: 1.5rem;
      opacity: 0.8;
      max-width: 600px;
      margin: 0 auto 1rem;
    }
    
    .powered-by {
      font-size: 0.9rem;
      opacity: 0.5;
    }
    
    .powered-by a {
      color: var(--code);
      text-decoration: none;
    }
    
    /* SOUND TOGGLE */
    .sound-toggle {
      position: fixed;
      top: 2rem;
      right: 2rem;
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: rgba(255,255,255,0.1);
      border: 2px solid rgba(255,255,255,0.2);
      color: var(--text);
      font-size: 1.5rem;
      cursor: pointer;
      z-index: 100;
      transition: all 0.3s;
    }
    
    .sound-toggle:hover {
      background: rgba(255,255,255,0.2);
      transform: scale(1.1);
    }
    
    /* GALAXY GRID */
    .galaxy {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      padding: 2rem;
      max-width: 1400px;
      margin: 0 auto;
    }
    
    .planet {
      position: relative;
      background: rgba(255,255,255,0.03);
      border-radius: 30px;
      padding: 2.5rem;
      text-align: center;
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      border: 2px solid transparent;
      overflow: hidden;
    }
    
    .planet::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(circle at 50% 0%, var(--glow), transparent 70%);
      opacity: 0;
      transition: opacity 0.4s;
    }
    
    .planet:hover {
      transform: translateY(-10px) scale(1.02);
      border-color: var(--glow);
      box-shadow: 0 20px 60px -20px var(--glow);
    }
    
    .planet:hover::before {
      opacity: 0.2;
    }
    
    .planet-icon {
      font-size: 4rem;
      margin-bottom: 1rem;
      display: block;
      animation: float 4s ease-in-out infinite;
    }
    
    .planet h2 {
      font-size: 1.8rem;
      margin-bottom: 0.5rem;
    }
    
    .planet p {
      opacity: 0.7;
      margin-bottom: 1rem;
    }
    
    .planet .sound-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      padding: 0.4rem 0.8rem;
      background: rgba(255,255,255,0.1);
      border-radius: 20px;
      opacity: 0.6;
    }
    
    /* PLANET COLORS */
    .planet.vox { --glow: var(--vox); }
    .planet.vox h2 { color: var(--vox); }
    
    .planet.code { --glow: var(--code); }
    .planet.code h2 { color: var(--code); }
    
    .planet.books { --glow: var(--books); }
    .planet.books h2 { color: var(--books); }
    
    .planet.lab { --glow: var(--lab); }
    .planet.lab h2 { color: var(--lab); }
    
    /* FISH MUSIC VAULT */
    .vault {
      text-align: center;
      padding: 4rem 2rem;
      margin-top: 2rem;
      background: linear-gradient(180deg, transparent, rgba(136,85,255,0.05));
    }
    
    .vault h2 {
      font-size: 2rem;
      margin-bottom: 1rem;
    }
    
    .vault p {
      opacity: 0.7;
      max-width: 600px;
      margin: 0 auto 2rem;
    }
    
    .credits {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem;
      max-width: 800px;
      margin: 0 auto;
    }
    
    .credit {
      padding: 0.5rem 1rem;
      background: rgba(255,255,255,0.05);
      border-radius: 20px;
      font-size: 0.9rem;
      opacity: 0.6;
    }
    
    /* FOOTER */
    footer {
      text-align: center;
      padding: 3rem 2rem;
      border-top: 1px solid rgba(255,255,255,0.1);
    }
    
    .gorunfree {
      font-size: 2rem;
      font-weight: 900;
      background: linear-gradient(135deg, var(--code), var(--vox));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-top: 1rem;
    }
    
    footer p {
      opacity: 0.5;
      margin-bottom: 0.5rem;
    }
    
    footer a {
      color: var(--code);
      text-decoration: none;
    }
    
    /* MOBILE */
    @media (max-width: 600px) {
      .logo { font-size: 3rem; }
      .tagline { font-size: 1.2rem; }
      .galaxy { padding: 1rem; gap: 1rem; }
      .planet { padding: 1.5rem; }
    }
  </style>
</head>
<body>
  <div class="stars"></div>
  
  <!-- SOUND VISUALIZER -->
  <div class="visualizer" id="visualizer"></div>
  
  <!-- SOUND TOGGLE -->
  <button class="sound-toggle" id="soundToggle" title="Toggle Sound">🔊</button>
  
  <!-- HEADER -->
  <header>
    <h1 class="logo">NOIZY.AI</h1>
    <p class="tagline">Where Sound is the Soul of Everything</p>
    <p class="powered-by">Powered by 40 years of <a href="https://fishmusicinc.com">Fish Music Inc.</a></p>
  </header>
  
  <!-- GALAXY -->
  <section class="galaxy">
    
    <!-- NOIZYVOX -->
    <a href="https://vox.noizy.ai" class="planet vox" data-sound="vox">
      <span class="planet-icon">🎤</span>
      <h2>NOIZYVOX</h2>
      <p>The Voice AI Guild<br>Artists own their voice. 75/25 split.</p>
      <span class="sound-badge">🔈 Voice Layer</span>
    </a>
    
    <!-- CODEMASTER -->
    <a href="https://codemaster.noizy.ai" class="planet code" data-sound="code">
      <span class="planet-icon">🖥️</span>
      <h2>CODEMASTER</h2>
      <p>Voice-First Infrastructure<br>One command. Total control.</p>
      <span class="sound-badge">🔈 Spoken Feedback</span>
    </a>
    
    <!-- FISHYBOOKS -->
    <a href="https://books.noizy.ai" class="planet books" data-sound="books">
      <span class="planet-icon">📚</span>
      <h2>FISHYBOOKS</h2>
      <p>Stories for Munchkins<br>Audiobooks with heart.</p>
      <span class="sound-badge">🔈 Narration + Music</span>
    </a>
    
    <!-- NOIZYLAB -->
    <a href="https://lab.noizy.ai" class="planet lab" data-sound="lab">
      <span class="planet-icon">💻</span>
      <h2>NOIZYLAB</h2>
      <p>CPU Repair Service<br>$89 flat rate. Done right.</p>
      <span class="sound-badge">🔈 Voice Support</span>
    </a>
    
  </section>
  
  <!-- THE VAULT -->
  <section class="vault">
    <h2>🐟 The Vault: Fish Music Inc.</h2>
    <p>40 years of professional audio for film, animation, and gaming. THE AQUARIUM archive powers every sound in the NOIZY.AI galaxy.</p>
    <div class="credits">
      <span class="credit">Ed Edd n Eddy</span>
      <span class="credit">Dragon Tales</span>
      <span class="credit">Johnny Test</span>
      <span class="credit">Transformers</span>
      <span class="credit">Barbie Films</span>
      <span class="credit">Bratz</span>
      <span class="credit">Krypto</span>
      <span class="credit">Madeline</span>
      <span class="credit">Martin Mystery</span>
      <span class="credit">Strawberry Shortcake</span>
      <span class="credit">+ Hundreds More</span>
    </div>
  </section>
  
  <!-- FOOTER -->
  <footer>
    <p>Built with 🔥 by Rob Plowman</p>
    <p>C3 injury. Partial paralysis. Still creating.</p>
    <p>Voice-first. Accessibility-native. No excuses.</p>
    <div class="gorunfree">GORUNFREE</div>
  </footer>
  
  <script>
    // Initialize sound visualizer bars
    const visualizer = document.getElementById('visualizer');
    for (let i = 0; i < 50; i++) {
      const bar = document.createElement('div');
      bar.className = 'bar';
      bar.style.setProperty('--h', Math.random() * 60 + 10 + 'px');
      bar.style.animationDelay = Math.random() * 0.5 + 's';
      visualizer.appendChild(bar);
    }
    
    // Sound toggle
    let soundEnabled = false;
    const soundToggle = document.getElementById('soundToggle');
    
    soundToggle.addEventListener('click', () => {
      soundEnabled = !soundEnabled;
      soundToggle.textContent = soundEnabled ? '🔊' : '🔇';
      
      if (soundEnabled) {
        playSound('ambient');
      }
    });
    
    // Planet hover sounds
    const planets = document.querySelectorAll('.planet');
    planets.forEach(planet => {
      planet.addEventListener('mouseenter', () => {
        if (soundEnabled) playSound('hover');
      });
      planet.addEventListener('click', (e) => {
        if (soundEnabled) playSound('click');
      });
    });
    
    // Simple sound player (placeholder - would connect to actual files)
    function playSound(type) {
      // Web Audio API implementation would go here
      // For now, use Web Speech for demo
      if (type === 'hover') {
        // Short blip sound via oscillator
        try {
          const ctx = new (window.AudioContext || window.webkitAudioContext)();
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.frequency.value = 800;
          gain.gain.value = 0.1;
          osc.start();
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.1);
          osc.stop(ctx.currentTime + 0.1);
        } catch(e) {}
      }
    }
    
    // Animate visualizer to "music"
    setInterval(() => {
      document.querySelectorAll('.bar').forEach(bar => {
        bar.style.setProperty('--h', Math.random() * 60 + 10 + 'px');
      });
    }, 200);
  </script>
</body>
</html>`;
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}
