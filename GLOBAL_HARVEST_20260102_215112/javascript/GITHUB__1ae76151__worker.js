/**
 * NOIZY.AI - MASTER ROUTING WORKER
 * Routes traffic for the NOIZY EMPIRE
 * 
 * vox.noizy.ai  → NOIZYVOX (Voice AI Guild)
 * lab.noizy.ai  → NOIZYLAB (CPU Repairs)
 * noizy.ai      → Main Hub
 * 
 * GORUNFREE - Rob Plowman 2025
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const hostname = url.hostname;
    const subdomain = hostname.split('.')[0];
    
    // Health check endpoint - always respond
    if (url.pathname === '/health' || url.pathname === '/_health') {
      return new Response(JSON.stringify({
        status: 'healthy',
        timestamp: new Date().toISOString(),
        subdomain: subdomain,
        hostname: hostname,
        empire: 'NOIZY.AI',
        version: '1.0.0'
      }), {
        status: 200,
        headers: { 
          'Content-Type': 'application/json',
          'X-Noizy-Empire': 'GORUNFREE'
        }
      });
    }

    // Route based on subdomain
    switch (subdomain) {
      case 'vox':
        return handleVox(request, env, url);
      
      case 'lab':
        return handleLab(request, env, url);
      
      case 'www':
      case 'noizy':
      default:
        return handleMain(request, env, url);
    }
  }
};

/**
 * NOIZYVOX - Voice AI Guild
 * "The world's first artist-owned voice AI guild"
 */
async function handleVox(request, env, url) {
  // API endpoints for NOIZYVOX
  if (url.pathname.startsWith('/api/')) {
    return handleVoxAPI(request, env, url);
  }
  
  // Landing page
  return new Response(renderVoxPage(), {
    headers: { 'Content-Type': 'text/html' }
  });
}

/**
 * NOIZYLAB - CPU Repair Service
 * "$89 repairs, 12/day = freedom"
 */
async function handleLab(request, env, url) {
  // API endpoints for NOIZYLAB
  if (url.pathname.startsWith('/api/')) {
    return handleLabAPI(request, env, url);
  }
  
  // Landing page
  return new Response(renderLabPage(), {
    headers: { 'Content-Type': 'text/html' }
  });
}

/**
 * NOIZY.AI Main Hub
 * "Everything New, Creative & AI"
 */
async function handleMain(request, env, url) {
  return new Response(renderMainPage(), {
    headers: { 'Content-Type': 'text/html' }
  });
}

/**
 * NOIZYVOX API Handler
 */
async function handleVoxAPI(request, env, url) {
  const path = url.pathname.replace('/api/', '');
  
  // Add your API routes here
  switch (path) {
    case 'voices':
      return jsonResponse({ message: 'Voice catalog coming soon', artists: [] });
    case 'status':
      return jsonResponse({ service: 'NOIZYVOX', status: 'operational' });
    default:
      return jsonResponse({ error: 'Not found' }, 404);
  }
}

/**
 * NOIZYLAB API Handler
 */
async function handleLabAPI(request, env, url) {
  const path = url.pathname.replace('/api/', '');
  
  // Add your API routes here
  switch (path) {
    case 'repairs':
      return jsonResponse({ message: 'Repair system ready', queue: [] });
    case 'status':
      return jsonResponse({ service: 'NOIZYLAB', status: 'operational' });
    case 'book':
      // TODO: Connect to D1 database for bookings
      return jsonResponse({ message: 'Booking endpoint ready' });
    default:
      return jsonResponse({ error: 'Not found' }, 404);
  }
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 
      'Content-Type': 'application/json',
      'X-Noizy-Empire': 'GORUNFREE'
    }
  });
}

/**
 * NOIZYVOX Landing Page
 */
function renderVoxPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOIZYVOX - Voice AI Guild</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
      color: #fff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 2rem;
    }
    .logo { font-size: 4rem; margin-bottom: 1rem; }
    h1 { font-size: 3rem; margin-bottom: 0.5rem; background: linear-gradient(90deg, #e94560, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .tagline { font-size: 1.5rem; opacity: 0.9; margin-bottom: 2rem; }
    .split { font-size: 2rem; color: #e94560; font-weight: bold; margin: 1rem 0; }
    .cta { background: #e94560; color: white; padding: 1rem 2rem; font-size: 1.2rem; border: none; border-radius: 50px; cursor: pointer; margin-top: 2rem; }
    .cta:hover { background: #ff6b6b; }
    .powered { margin-top: 3rem; opacity: 0.7; font-size: 0.9rem; }
  </style>
</head>
<body>
  <div class="logo">🎤</div>
  <h1>NOIZYVOX</h1>
  <p class="tagline">The World's First Artist-Owned Voice AI Guild</p>
  <p class="split">75/25 Revenue Split — Artists First</p>
  <p>Your voice. Your rules. Your future.</p>
  <button class="cta">Join the Guild</button>
  <p class="powered">Powered by 40 years of Fish Music Inc.</p>
</body>
</html>`;
}

/**
 * NOIZYLAB Landing Page
 */
function renderLabPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOIZYLAB - CPU Repair Service</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 50%, #2d2d2d 100%);
      color: #fff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 2rem;
    }
    .logo { font-size: 4rem; margin-bottom: 1rem; }
    h1 { font-size: 3rem; margin-bottom: 0.5rem; background: linear-gradient(90deg, #00ff88, #00cc6a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .tagline { font-size: 1.5rem; opacity: 0.9; margin-bottom: 2rem; }
    .price { font-size: 3rem; color: #00ff88; font-weight: bold; margin: 1rem 0; }
    .features { list-style: none; margin: 1rem 0; }
    .features li { padding: 0.5rem; font-size: 1.1rem; }
    .features li::before { content: '✓ '; color: #00ff88; }
    .cta { background: #00ff88; color: #0d0d0d; padding: 1rem 2rem; font-size: 1.2rem; border: none; border-radius: 50px; cursor: pointer; margin-top: 2rem; font-weight: bold; }
    .cta:hover { background: #00cc6a; }
    .location { margin-top: 2rem; opacity: 0.7; }
  </style>
</head>
<body>
  <div class="logo">💻</div>
  <h1>NOIZYLAB</h1>
  <p class="tagline">Fast. Fair. Fixed.</p>
  <p class="price">$89 Flat Rate</p>
  <ul class="features">
    <li>Mac & PC Repairs</li>
    <li>Remote Diagnostics</li>
    <li>Same-Day Service</li>
    <li>No Hidden Fees</li>
  </ul>
  <button class="cta">Book a Repair</button>
  <p class="location">📍 Montreal, QC | help@noizy.ai</p>
</body>
</html>`;
}

/**
 * NOIZY.AI Main Hub Page
 */
function renderMainPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOIZY.AI - Everything New, Creative & AI</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #0a0a0a;
      color: #fff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 2rem;
    }
    h1 { 
      font-size: 5rem; 
      margin-bottom: 1rem; 
      background: linear-gradient(90deg, #e94560, #00ff88, #4d9fff); 
      -webkit-background-clip: text; 
      -webkit-text-fill-color: transparent;
      animation: gradient 3s ease infinite;
      background-size: 200% 200%;
    }
    @keyframes gradient {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    .tagline { font-size: 1.5rem; opacity: 0.8; margin-bottom: 3rem; }
    .services { display: flex; gap: 2rem; flex-wrap: wrap; justify-content: center; margin: 2rem 0; }
    .service { 
      background: rgba(255,255,255,0.05); 
      padding: 2rem; 
      border-radius: 20px; 
      width: 280px;
      transition: transform 0.3s, background 0.3s;
      text-decoration: none;
      color: inherit;
    }
    .service:hover { transform: translateY(-10px); background: rgba(255,255,255,0.1); }
    .service .icon { font-size: 3rem; margin-bottom: 1rem; }
    .service h2 { font-size: 1.5rem; margin-bottom: 0.5rem; }
    .service p { opacity: 0.7; }
    .vox { border: 2px solid #e94560; }
    .vox:hover { box-shadow: 0 0 30px rgba(233,69,96,0.3); }
    .lab { border: 2px solid #00ff88; }
    .lab:hover { box-shadow: 0 0 30px rgba(0,255,136,0.3); }
    .legacy { margin-top: 3rem; padding: 1.5rem; background: rgba(255,255,255,0.03); border-radius: 10px; }
    .legacy p { opacity: 0.6; font-size: 0.9rem; }
    .legacy a { color: #4d9fff; text-decoration: none; }
  </style>
</head>
<body>
  <h1>NOIZY.AI</h1>
  <p class="tagline">Everything New, Creative & AI</p>
  
  <div class="services">
    <a href="https://vox.noizy.ai" class="service vox">
      <div class="icon">🎤</div>
      <h2>NOIZYVOX</h2>
      <p>Voice AI Guild<br>Artists First. 75/25 Split.</p>
    </a>
    
    <a href="https://lab.noizy.ai" class="service lab">
      <div class="icon">💻</div>
      <h2>NOIZYLAB</h2>
      <p>CPU Repair Service<br>$89 Flat Rate. Done Right.</p>
    </a>
  </div>
  
  <div class="legacy">
    <p>Powered by 40 years of professional audio</p>
    <p><a href="https://fishmusicinc.com">Fish Music Inc.</a> — Music for Film, Animation & Gaming</p>
  </div>
</body>
</html>`;
}
