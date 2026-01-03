/**
 * ═══════════════════════════════════════════════════════════════════
 * 
 *   FISHYBOOKS — Stories for Munchkins
 *   "Where Every Story Has a Voice"
 *   
 *   Audiobooks powered by NOIZYVOX artists
 *   Music beds from THE AQUARIUM
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
    
    if (path === '/health') {
      return jsonResponse({
        service: 'FISHYBOOKS',
        status: 'operational',
        tagline: 'Stories for Munchkins',
        powered_by: ['NOIZYVOX', 'THE AQUARIUM']
      });
    }
    
    if (path.startsWith('/api/')) {
      return handleAPI(path);
    }
    
    return new Response(renderBooksPage(), {
      headers: { 'Content-Type': 'text/html' }
    });
  }
};

function handleAPI(path) {
  const route = path.replace('/api/', '');
  
  switch (route) {
    case 'books':
      return jsonResponse({
        books: [
          { id: 1, title: "Finley's First Day", category: "adventure", age: "3-5", duration: "8:00" },
          { id: 2, title: "Space Puppy Quest", category: "science", age: "4-7", duration: "12:00" },
          { id: 3, title: "Sparkle Dreams", category: "bedtime", age: "2-4", duration: "6:00" },
        ],
        note: "Demo catalog - more coming!"
      });
    
    case 'narrators':
      return jsonResponse({
        narrators: [
          { id: 1, name: "Grandma Rose", style: "warm", voice_id: "vox_warm_01" },
          { id: 2, name: "Captain Dan", style: "adventure", voice_id: "vox_adventure_01" },
          { id: 3, name: "Sleepy Sarah", style: "bedtime", voice_id: "vox_calm_01" },
        ],
        powered_by: "NOIZYVOX"
      });
    
    case 'status':
      return jsonResponse({ service: 'FISHYBOOKS', status: 'operational' });
    
    default:
      return jsonResponse({ error: 'Not found' }, 404);
  }
}

function renderBooksPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FISHYBOOKS — Stories for Munchkins</title>
  <meta name="description" content="Magical audiobooks for children, narrated by real artists. Where every story has a voice.">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    :root {
      --bg: #0f1629;
      --text: #ffffff;
      --accent: #ff9500;
      --accent2: #ffcc00;
      --purple: #8b5cf6;
      --pink: #ec4899;
    }
    
    body {
      font-family: 'Comic Sans MS', 'Chalkboard', cursive, sans-serif;
      background: linear-gradient(180deg, #0f1629 0%, #1e1b4b 100%);
      color: var(--text);
      min-height: 100vh;
    }
    
    /* Stars */
    .stars {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background-image: 
        radial-gradient(2px 2px at 20px 30px, white, transparent),
        radial-gradient(2px 2px at 40px 70px, white, transparent),
        radial-gradient(1px 1px at 90px 40px, white, transparent),
        radial-gradient(2px 2px at 160px 120px, white, transparent);
      background-size: 200px 200px;
      animation: twinkle 5s ease-in-out infinite;
      pointer-events: none;
    }
    
    @keyframes twinkle {
      0%, 100% { opacity: 0.5; }
      50% { opacity: 1; }
    }
    
    .container {
      position: relative;
      z-index: 1;
      max-width: 1000px;
      margin: 0 auto;
      padding: 2rem;
    }
    
    /* Header */
    header {
      text-align: center;
      padding: 4rem 0;
    }
    
    .logo {
      font-size: 4rem;
      margin-bottom: 0.5rem;
    }
    
    .logo span {
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    
    .tagline {
      font-size: 1.5rem;
      opacity: 0.9;
    }
    
    /* Book shelf */
    .bookshelf {
      padding: 3rem 0;
    }
    
    .bookshelf h2 {
      text-align: center;
      font-size: 2rem;
      margin-bottom: 2rem;
      color: var(--accent);
    }
    
    .books {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
    }
    
    .book {
      background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(236,72,153,0.2));
      border-radius: 20px;
      padding: 1.5rem;
      text-align: center;
      cursor: pointer;
      transition: transform 0.3s, box-shadow 0.3s;
      border: 2px solid rgba(255,255,255,0.1);
    }
    
    .book:hover {
      transform: translateY(-10px) rotate(-2deg);
      box-shadow: 0 20px 40px rgba(139,92,246,0.3);
    }
    
    .book-cover {
      font-size: 4rem;
      margin-bottom: 1rem;
    }
    
    .book h3 {
      font-size: 1.2rem;
      margin-bottom: 0.5rem;
    }
    
    .book p {
      font-size: 0.9rem;
      opacity: 0.7;
    }
    
    .book .age {
      display: inline-block;
      background: var(--accent);
      color: #000;
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.8rem;
      margin-top: 0.5rem;
    }
    
    /* Player */
    .player {
      background: rgba(0,0,0,0.3);
      border-radius: 30px;
      padding: 2rem;
      margin: 3rem 0;
      text-align: center;
    }
    
    .player h3 {
      font-size: 1.5rem;
      margin-bottom: 1rem;
      color: var(--accent);
    }
    
    .player-controls {
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 1rem;
    }
    
    .play-btn {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      border: none;
      font-size: 2rem;
      cursor: pointer;
      transition: transform 0.2s;
    }
    
    .play-btn:hover {
      transform: scale(1.1);
    }
    
    .progress {
      width: 100%;
      height: 10px;
      background: rgba(255,255,255,0.1);
      border-radius: 5px;
      overflow: hidden;
    }
    
    .progress-bar {
      width: 30%;
      height: 100%;
      background: linear-gradient(90deg, var(--accent), var(--accent2));
      border-radius: 5px;
    }
    
    /* Narrator picker */
    .narrators {
      text-align: center;
      padding: 3rem 0;
    }
    
    .narrators h2 {
      font-size: 2rem;
      margin-bottom: 2rem;
      color: var(--purple);
    }
    
    .narrator-list {
      display: flex;
      justify-content: center;
      gap: 2rem;
      flex-wrap: wrap;
    }
    
    .narrator {
      background: rgba(139,92,246,0.2);
      border-radius: 20px;
      padding: 1.5rem;
      width: 150px;
      cursor: pointer;
      transition: all 0.3s;
      border: 2px solid transparent;
    }
    
    .narrator:hover, .narrator.active {
      border-color: var(--purple);
      transform: scale(1.05);
    }
    
    .narrator-avatar {
      font-size: 3rem;
      margin-bottom: 0.5rem;
    }
    
    .narrator h4 {
      font-size: 1rem;
    }
    
    .narrator p {
      font-size: 0.8rem;
      opacity: 0.7;
    }
    
    /* CTA */
    .cta {
      text-align: center;
      padding: 3rem 0;
    }
    
    .cta h2 {
      font-size: 2rem;
      margin-bottom: 1rem;
    }
    
    .btn {
      display: inline-block;
      padding: 1rem 2.5rem;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      color: #000;
      font-size: 1.2rem;
      font-weight: bold;
      border-radius: 50px;
      text-decoration: none;
      transition: transform 0.3s;
    }
    
    .btn:hover {
      transform: scale(1.05);
    }
    
    /* Footer */
    footer {
      text-align: center;
      padding: 3rem;
      border-top: 1px solid rgba(255,255,255,0.1);
      font-family: -apple-system, sans-serif;
    }
    
    footer p {
      opacity: 0.5;
      margin-bottom: 0.5rem;
    }
    
    footer a {
      color: var(--accent);
      text-decoration: none;
    }
    
    .powered {
      display: flex;
      justify-content: center;
      gap: 2rem;
      margin-top: 1rem;
      opacity: 0.6;
      font-size: 0.9rem;
    }
  </style>
</head>
<body>
  <div class="stars"></div>
  
  <div class="container">
    <header>
      <h1 class="logo">📚 <span>FISHYBOOKS</span></h1>
      <p class="tagline">Stories for Munchkins ✨</p>
    </header>
    
    <!-- Book Shelf -->
    <section class="bookshelf">
      <h2>📖 Pick a Story!</h2>
      <div class="books">
        <div class="book">
          <div class="book-cover">🐠</div>
          <h3>Finley's First Day</h3>
          <p>A little fish finds courage</p>
          <span class="age">Ages 3-5</span>
        </div>
        <div class="book">
          <div class="book-cover">🚀🐕</div>
          <h3>Space Puppy Quest</h3>
          <p>Adventure among the stars</p>
          <span class="age">Ages 4-7</span>
        </div>
        <div class="book">
          <div class="book-cover">🦄✨</div>
          <h3>Sparkle Dreams</h3>
          <p>A magical bedtime story</p>
          <span class="age">Ages 2-4</span>
        </div>
        <div class="book">
          <div class="book-cover">🐻🌲</div>
          <h3>Bear's Big Journey</h3>
          <p>Finding your way home</p>
          <span class="age">Ages 3-6</span>
        </div>
      </div>
    </section>
    
    <!-- Player -->
    <section class="player">
      <h3>🎧 Now Playing: Finley's First Day</h3>
      <div class="player-controls">
        <button class="play-btn">▶️</button>
      </div>
      <div class="progress">
        <div class="progress-bar"></div>
      </div>
      <p style="margin-top: 1rem; opacity: 0.6;">2:34 / 8:12</p>
    </section>
    
    <!-- Narrators -->
    <section class="narrators">
      <h2>🎤 Choose Your Narrator</h2>
      <div class="narrator-list">
        <div class="narrator active">
          <div class="narrator-avatar">👵</div>
          <h4>Grandma Rose</h4>
          <p>Warm & Cozy</p>
        </div>
        <div class="narrator">
          <div class="narrator-avatar">🦸‍♂️</div>
          <h4>Captain Dan</h4>
          <p>Adventure!</p>
        </div>
        <div class="narrator">
          <div class="narrator-avatar">🧚‍♀️</div>
          <h4>Sleepy Sarah</h4>
          <p>Bedtime</p>
        </div>
      </div>
      <p style="margin-top: 1.5rem; opacity: 0.6;">Voices by <a href="https://vox.noizy.ai" style="color: #ff3366;">NOIZYVOX</a> artists</p>
    </section>
    
    <!-- CTA -->
    <section class="cta">
      <h2>Ready for Storytime? 🌙</h2>
      <a href="#" class="btn">Start Listening — Free!</a>
    </section>
    
    <!-- Footer -->
    <footer>
      <p>Part of the <a href="https://noizy.ai">NOIZY.AI</a> Galaxy</p>
      <div class="powered">
        <span>🎤 Voices by NOIZYVOX</span>
        <span>🎵 Music by THE AQUARIUM</span>
      </div>
    </footer>
  </div>
</body>
</html>`;
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}
