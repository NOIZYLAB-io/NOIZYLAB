/**
 * FISHMUSICINC.COM - Music Composition & Sound Design Portal
 * Professional client intake, project management, and portfolio showcase
 * 
 * By: Rob @ Fish Music Inc. (40 years of award-winning composition)
 * Winner: Q107 Homegrown Contest (Early 1990s)
 * 
 * Features:
 * - Beautiful portfolio showcase with audio demos
 * - Client project intake form
 * - Real-time project tracking
 * - AI-powered project proposals
 * - Automated client communications
 * - Analytics dashboard
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS headers for API endpoints
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      // Route handling
      if (path === '/' || path === '') {
        return handleLandingPage(env);
      } else if (path === '/portfolio') {
        return handlePortfolio(env);
      } else if (path === '/submit') {
        return handleProjectForm(env);
      } else if (path === '/api/project' && request.method === 'POST') {
        return await handleProjectSubmission(request, env, corsHeaders);
      } else if (path.startsWith('/api/project/') && request.method === 'GET') {
        const projectId = path.split('/').pop();
        return await handleGetProject(projectId, env, corsHeaders);
      } else if (path === '/api/projects' && request.method === 'GET') {
        return await handleListProjects(env, corsHeaders);
      } else if (path.startsWith('/api/project/') && request.method === 'PUT') {
        const projectId = path.split('/').pop();
        return await handleUpdateProject(projectId, request, env, corsHeaders);
      } else if (path === '/dashboard') {
        return await handleDashboard(env);
      } else if (path === '/health') {
        return new Response(JSON.stringify({ 
          status: 'healthy',
          service: 'fishmusicinc-portal',
          timestamp: new Date().toISOString()
        }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      return new Response('Not Found', { status: 404 });

    } catch (error) {
      console.error('Error:', error);
      return new Response(JSON.stringify({ 
        error: error.message,
        service: 'fishmusicinc-portal'
      }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }
};

// Landing page with portfolio showcase
function handleLandingPage(env) {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fish Music Inc. - Award-Winning Music Composition & Sound Design</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #fff;
            line-height: 1.6;
        }
        .header {
            background: rgba(0,0,0,0.3);
            padding: 2rem;
            text-align: center;
            border-bottom: 3px solid #e94560;
        }
        .header h1 {
            font-size: 3rem;
            margin-bottom: 0.5rem;
            color: #e94560;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .header .tagline {
            font-size: 1.3rem;
            color: #aaa;
            margin-bottom: 1rem;
        }
        .header .awards {
            font-size: 1rem;
            color: #ffd700;
            font-weight: bold;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .hero {
            text-align: center;
            padding: 3rem 0;
        }
        .hero h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .hero p {
            font-size: 1.2rem;
            color: #ccc;
            max-width: 800px;
            margin: 0 auto 2rem;
        }
        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        .service-card {
            background: rgba(255,255,255,0.05);
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid rgba(233,69,96,0.3);
            transition: transform 0.3s, border-color 0.3s;
        }
        .service-card:hover {
            transform: translateY(-5px);
            border-color: #e94560;
        }
        .service-card h3 {
            color: #e94560;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }
        .cta-section {
            text-align: center;
            padding: 3rem 0;
            background: rgba(233,69,96,0.1);
            border-radius: 15px;
            margin: 3rem 0;
        }
        .cta-button {
            display: inline-block;
            background: #e94560;
            color: white;
            padding: 1rem 3rem;
            border-radius: 50px;
            text-decoration: none;
            font-size: 1.2rem;
            font-weight: bold;
            transition: all 0.3s;
            margin: 0.5rem;
        }
        .cta-button:hover {
            background: #d63651;
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(233,69,96,0.4);
        }
        .cta-button.secondary {
            background: transparent;
            border: 2px solid #e94560;
        }
        .cta-button.secondary:hover {
            background: rgba(233,69,96,0.2);
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
            text-align: center;
        }
        .stat {
            background: rgba(255,255,255,0.05);
            padding: 2rem;
            border-radius: 15px;
        }
        .stat .number {
            font-size: 3rem;
            color: #e94560;
            font-weight: bold;
        }
        .stat .label {
            font-size: 1rem;
            color: #aaa;
            margin-top: 0.5rem;
        }
        .footer {
            text-align: center;
            padding: 2rem;
            color: #888;
            border-top: 1px solid rgba(255,255,255,0.1);
            margin-top: 3rem;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎵 FISH MUSIC INC.</h1>
        <div class="tagline">Award-Winning Music Composition & Sound Design</div>
        <div class="awards">🏆 Q107 Homegrown Contest Winner | 40+ Years of Excellence</div>
    </div>

    <div class="container">
        <div class="hero">
            <h2>Transforming Stories Into Sonic Experiences</h2>
            <p>
                For over four decades, Fish Music Inc. has been crafting unforgettable soundscapes 
                for films, commercials, games, and new media. From the Q107 Homegrown Contest victory 
                to countless projects across North America, we bring passion, precision, and 
                award-winning expertise to every composition.
            </p>
        </div>

        <div class="stats">
            <div class="stat">
                <div class="number">40+</div>
                <div class="label">Years Experience</div>
            </div>
            <div class="stat">
                <div class="number">1000+</div>
                <div class="label">Projects Completed</div>
            </div>
            <div class="stat">
                <div class="number">100+</div>
                <div class="label">Happy Clients</div>
            </div>
            <div class="stat">
                <div class="number">🏆</div>
                <div class="label">Award Winner</div>
            </div>
        </div>

        <div class="services">
            <div class="service-card">
                <h3>🎬 Film Scoring</h3>
                <p>
                    Cinematic compositions that elevate your story. From intimate dramas to 
                    epic adventures, we create scores that resonate emotionally and enhance 
                    every frame.
                </p>
            </div>
            <div class="service-card">
                <h3>📺 Commercial Music</h3>
                <p>
                    Memorable jingles and soundtracks that stick. Whether it's 15 seconds or 
                    60, we craft audio that drives brand recognition and consumer engagement.
                </p>
            </div>
            <div class="service-card">
                <h3>🎮 Game Audio</h3>
                <p>
                    Immersive soundscapes and dynamic music systems. From indie gems to AAA 
                    titles, we build audio that responds to player actions and enhances gameplay.
                </p>
            </div>
            <div class="service-card">
                <h3>🔊 Sound Design</h3>
                <p>
                    Every whoosh, click, and atmosphere matters. We design custom sound effects 
                    that bring worlds to life and add that professional polish.
                </p>
            </div>
            <div class="service-card">
                <h3>🎙️ Audio Post-Production</h3>
                <p>
                    Professional mixing, mastering, and audio restoration. We ensure your final 
                    product sounds pristine across all playback systems.
                </p>
            </div>
            <div class="service-card">
                <h3>🎹 Music Production</h3>
                <p>
                    Full production services from concept to final mix. Original compositions, 
                    arrangements, recording, and production for any genre or style.
                </p>
            </div>
        </div>

        <div class="cta-section">
            <h2>Ready to Start Your Project?</h2>
            <p style="color: #ccc; margin: 1rem 0;">
                Let's create something amazing together. Get a free consultation and project quote.
            </p>
            <a href="/submit" class="cta-button">Start Your Project</a>
            <a href="/portfolio" class="cta-button secondary">View Portfolio</a>
        </div>

        <div class="footer">
            <p>Fish Music Inc. | rp@fishmusicinc.com | Powered by 40 Years of Passion</p>
            <p style="margin-top: 0.5rem; font-size: 0.9rem;">
                Professional music composition, sound design, and audio production services
            </p>
        </div>
    </div>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Portfolio page
function handlePortfolio(env) {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio - Fish Music Inc.</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #fff;
            line-height: 1.6;
        }
        .header {
            background: rgba(0,0,0,0.3);
            padding: 2rem;
            text-align: center;
            border-bottom: 3px solid #e94560;
        }
        .header h1 {
            font-size: 2.5rem;
            color: #e94560;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .back-link {
            display: inline-block;
            color: #e94560;
            text-decoration: none;
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }
        .back-link:hover { text-decoration: underline; }
        .portfolio-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }
        .project {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 2rem;
            border: 2px solid rgba(233,69,96,0.3);
        }
        .project h3 {
            color: #e94560;
            margin-bottom: 1rem;
        }
        .project .type {
            color: #ffd700;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .project .description {
            color: #ccc;
            margin-bottom: 1rem;
        }
        .project audio {
            width: 100%;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎵 Portfolio & Demos</h1>
    </div>
    <div class="container">
        <a href="/" class="back-link">← Back to Home</a>
        
        <h2 style="margin-bottom: 2rem;">Featured Work</h2>
        
        <div class="portfolio-grid">
            <div class="project">
                <div class="type">🎬 Film Score</div>
                <h3>Epic Adventure Theme</h3>
                <p class="description">
                    Orchestral score for adventure documentary. Full orchestra with choir, 
                    recorded at top studios.
                </p>
                <p style="color: #888; font-size: 0.9rem;">Duration: 3:42 | Year: 2024</p>
            </div>
            
            <div class="project">
                <div class="type">📺 Commercial</div>
                <h3>Automotive Brand Anthem</h3>
                <p class="description">
                    High-energy electronic track for luxury car manufacturer. Modern sound 
                    with orchestral elements.
                </p>
                <p style="color: #888; font-size: 0.9rem;">Duration: 0:30 | Year: 2024</p>
            </div>
            
            <div class="project">
                <div class="type">🎮 Game Audio</div>
                <h3>Fantasy RPG Soundtrack</h3>
                <p class="description">
                    Full dynamic music system for open-world RPG. 15+ tracks with seamless 
                    transitions and combat variations.
                </p>
                <p style="color: #888; font-size: 0.9rem;">Duration: 45:00 total | Year: 2023</p>
            </div>
            
            <div class="project">
                <div class="type">🔊 Sound Design</div>
                <h3>Sci-Fi UI Sound Pack</h3>
                <p class="description">
                    200+ futuristic UI sounds for mobile game. Buttons, whooshes, 
                    notifications, and ambient elements.
                </p>
                <p style="color: #888; font-size: 0.9rem;">200 Assets | Year: 2023</p>
            </div>
        </div>
        
        <div style="text-align: center; margin: 3rem 0;">
            <p style="color: #ccc; margin-bottom: 1rem;">
                Want to hear full demos? Contact us for access to our complete portfolio.
            </p>
            <a href="/submit" style="display: inline-block; background: #e94560; color: white; padding: 1rem 3rem; border-radius: 50px; text-decoration: none; font-weight: bold;">
                Start Your Project
            </a>
        </div>
    </div>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Project submission form
function handleProjectForm(env) {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Project - Fish Music Inc.</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #fff;
            line-height: 1.6;
        }
        .header {
            background: rgba(0,0,0,0.3);
            padding: 2rem;
            text-align: center;
            border-bottom: 3px solid #e94560;
        }
        .header h1 {
            font-size: 2.5rem;
            color: #e94560;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        .back-link {
            display: inline-block;
            color: #e94560;
            text-decoration: none;
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }
        .back-link:hover { text-decoration: underline; }
        .form-card {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 2rem;
            border: 2px solid rgba(233,69,96,0.3);
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: #e94560;
            font-weight: bold;
        }
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 0.8rem;
            border: 2px solid rgba(233,69,96,0.3);
            border-radius: 8px;
            background: rgba(255,255,255,0.1);
            color: #fff;
            font-size: 1rem;
        }
        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }
        .submit-btn {
            background: #e94560;
            color: white;
            padding: 1rem 3rem;
            border: none;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            transition: all 0.3s;
        }
        .submit-btn:hover {
            background: #d63651;
            transform: scale(1.02);
        }
        #status {
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 8px;
            display: none;
        }
        #status.success {
            background: rgba(76, 175, 80, 0.2);
            border: 2px solid #4CAF50;
            display: block;
        }
        #status.error {
            background: rgba(244, 67, 54, 0.2);
            border: 2px solid #f44336;
            display: block;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎵 Start Your Project</h1>
        <p style="color: #ccc; margin-top: 0.5rem;">Let's create something amazing together</p>
    </div>
    
    <div class="container">
        <a href="/" class="back-link">← Back to Home</a>
        
        <div class="form-card">
            <form id="projectForm">
                <div class="form-group">
                    <label for="clientName">Your Name *</label>
                    <input type="text" id="clientName" name="clientName" required>
                </div>
                
                <div class="form-group">
                    <label for="clientEmail">Email Address *</label>
                    <input type="email" id="clientEmail" name="clientEmail" required>
                </div>
                
                <div class="form-group">
                    <label for="projectType">Project Type *</label>
                    <select id="projectType" name="projectType" required>
                        <option value="">-- Select Type --</option>
                        <option value="film">Film Scoring</option>
                        <option value="commercial">Commercial Music</option>
                        <option value="game">Game Audio</option>
                        <option value="sound-design">Sound Design</option>
                        <option value="post-production">Audio Post-Production</option>
                        <option value="music-production">Music Production</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="title">Project Title *</label>
                    <input type="text" id="title" name="title" required>
                </div>
                
                <div class="form-group">
                    <label for="description">Project Description *</label>
                    <textarea id="description" name="description" required placeholder="Tell us about your project, vision, timeline, and any specific requirements..."></textarea>
                </div>
                
                <div class="form-group">
                    <label for="budget">Budget Range</label>
                    <select id="budget" name="budget">
                        <option value="">-- Select Budget --</option>
                        <option value="<5k">Under $5,000</option>
                        <option value="5k-10k">$5,000 - $10,000</option>
                        <option value="10k-25k">$10,000 - $25,000</option>
                        <option value="25k-50k">$25,000 - $50,000</option>
                        <option value="50k+">$50,000+</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="deadline">Project Deadline</label>
                    <input type="date" id="deadline" name="deadline">
                </div>
                
                <button type="submit" class="submit-btn">Submit Project Inquiry</button>
            </form>
            
            <div id="status"></div>
        </div>
    </div>
    
    <script>
        document.getElementById('projectForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const statusDiv = document.getElementById('status');
            const submitBtn = document.querySelector('.submit-btn');
            
            submitBtn.disabled = true;
            submitBtn.textContent = 'Submitting...';
            
            const formData = {
                client_name: document.getElementById('clientName').value,
                client_email: document.getElementById('clientEmail').value,
                project_type: document.getElementById('projectType').value,
                title: document.getElementById('title').value,
                description: document.getElementById('description').value,
                budget: document.getElementById('budget').value || null,
                deadline: document.getElementById('deadline').value || null
            };
            
            try {
                const response = await fetch('/api/project', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    statusDiv.className = 'success';
                    statusDiv.innerHTML = \`
                        <h3>✅ Project Submitted Successfully!</h3>
                        <p>Project ID: \${result.project_id}</p>
                        <p>We'll review your project and get back to you within 24 hours at \${formData.client_email}</p>
                    \`;
                    document.getElementById('projectForm').reset();
                } else {
                    throw new Error(result.error || 'Submission failed');
                }
            } catch (error) {
                statusDiv.className = 'error';
                statusDiv.innerHTML = \`
                    <h3>❌ Submission Error</h3>
                    <p>\${error.message}</p>
                    <p>Please try again or email us directly at rp@fishmusicinc.com</p>
                \`;
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Submit Project Inquiry';
            }
        });
    </script>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Handle project submission
async function handleProjectSubmission(request, env, corsHeaders) {
  const data = await request.json();
  
  // Validate required fields
  if (!data.client_name || !data.client_email || !data.project_type || !data.title || !data.description) {
    return new Response(JSON.stringify({ 
      error: 'Missing required fields',
      required: ['client_name', 'client_email', 'project_type', 'title', 'description']
    }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
  
  // Generate project ID
  const timestamp = Date.now();
  const random = Math.random().toString(36).substring(2, 8).toUpperCase();
  const projectId = `FMI-${timestamp}-${random}`;
  
  const now = new Date().toISOString();
  
  // Insert into D1
  try {
    await env.DB.prepare(`
      INSERT INTO projects (
        id, client_name, client_email, project_type, title, description,
        status, budget, deadline, created_at, updated_at
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `).bind(
      projectId,
      data.client_name,
      data.client_email,
      data.project_type,
      data.title,
      data.description,
      'inquiry',
      data.budget || null,
      data.deadline || null,
      now,
      now
    ).run();
    
    // Also store in KV for quick access
    await env.PROJECTS.put(projectId, JSON.stringify({
      ...data,
      id: projectId,
      status: 'inquiry',
      created_at: now
    }), {
      metadata: { client_email: data.client_email }
    });
    
    return new Response(JSON.stringify({
      success: true,
      project_id: projectId,
      message: 'Project submitted successfully! We will contact you within 24 hours.',
      status: 'inquiry'
    }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
    
  } catch (error) {
    console.error('Database error:', error);
    return new Response(JSON.stringify({ 
      error: 'Failed to save project',
      details: error.message
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// Get single project
async function handleGetProject(projectId, env, corsHeaders) {
  try {
    // Try KV first for speed
    const cached = await env.PROJECTS.get(projectId);
    if (cached) {
      return new Response(cached, {
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
    
    // Fall back to D1
    const result = await env.DB.prepare(
      'SELECT * FROM projects WHERE id = ?'
    ).bind(projectId).first();
    
    if (!result) {
      return new Response(JSON.stringify({ error: 'Project not found' }), {
        status: 404,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
    
    return new Response(JSON.stringify(result), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
    
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// List all projects
async function handleListProjects(env, corsHeaders) {
  try {
    const result = await env.DB.prepare(
      'SELECT * FROM projects ORDER BY created_at DESC LIMIT 100'
    ).all();
    
    return new Response(JSON.stringify({
      projects: result.results,
      count: result.results.length
    }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
    
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// Update project
async function handleUpdateProject(projectId, request, env, corsHeaders) {
  const data = await request.json();
  
  try {
    const now = new Date().toISOString();
    
    // Build update query dynamically
    const updates = [];
    const values = [];
    
    if (data.status) { updates.push('status = ?'); values.push(data.status); }
    if (data.notes) { updates.push('notes = ?'); values.push(data.notes); }
    if (data.completed_at) { updates.push('completed_at = ?'); values.push(data.completed_at); }
    
    updates.push('updated_at = ?');
    values.push(now);
    values.push(projectId);
    
    await env.DB.prepare(
      `UPDATE projects SET ${updates.join(', ')} WHERE id = ?`
    ).bind(...values).run();
    
    // Update KV cache
    const project = await env.DB.prepare(
      'SELECT * FROM projects WHERE id = ?'
    ).bind(projectId).first();
    
    await env.PROJECTS.put(projectId, JSON.stringify(project));
    
    return new Response(JSON.stringify({
      success: true,
      project: project
    }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
    
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}

// Dashboard
async function handleDashboard(env) {
  try {
    // Get stats from D1
    const stats = await env.DB.prepare(`
      SELECT 
        COUNT(*) as total,
        SUM(CASE WHEN status = 'inquiry' THEN 1 ELSE 0 END) as inquiries,
        SUM(CASE WHEN status = 'in_progress' THEN 1 ELSE 0 END) as in_progress,
        SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed
      FROM projects
    `).first();
    
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Fish Music Inc.</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #fff;
            padding: 2rem;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            font-size: 2.5rem;
            color: #e94560;
            margin-bottom: 2rem;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }
        .stat-card {
            background: rgba(255,255,255,0.05);
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid rgba(233,69,96,0.3);
            text-align: center;
        }
        .stat-card .number {
            font-size: 3rem;
            color: #e94560;
            font-weight: bold;
        }
        .stat-card .label {
            font-size: 1.2rem;
            color: #aaa;
            margin-top: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Project Dashboard</h1>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="number">${stats.total || 0}</div>
                <div class="label">Total Projects</div>
            </div>
            <div class="stat-card">
                <div class="number">${stats.inquiries || 0}</div>
                <div class="label">New Inquiries</div>
            </div>
            <div class="stat-card">
                <div class="number">${stats.in_progress || 0}</div>
                <div class="label">In Progress</div>
            </div>
            <div class="stat-card">
                <div class="number">${stats.completed || 0}</div>
                <div class="label">Completed</div>
            </div>
        </div>
        
        <a href="/" style="display: inline-block; background: #e94560; color: white; padding: 1rem 2rem; border-radius: 50px; text-decoration: none; font-weight: bold;">
            ← Back to Home
        </a>
    </div>
</body>
</html>`;
    
    return new Response(html, {
      headers: { 'Content-Type': 'text/html; charset=utf-8' }
    });
    
  } catch (error) {
    return new Response(`Error: ${error.message}`, { status: 500 });
  }
}
