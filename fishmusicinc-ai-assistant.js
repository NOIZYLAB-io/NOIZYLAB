/**
 * FISHMUSICINC AI MUSIC ASSISTANT
 * Powered by Claude - 40 Years of Music Expertise + AI
 * 
 * Features:
 * - Music composition assistance
 * - Genre analysis & recommendations
 * - Music theory help
 * - Project proposal generation
 * - Sound design suggestions
 * - Orchestration advice
 * - Reference track analysis
 * - Budget estimation
 * - Timeline planning
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    try {
      if (path === '/') {
        return handleLandingPage();
      } else if (path === '/ask' && request.method === 'POST') {
        return await handleAskQuestion(request, env, corsHeaders);
      } else if (path === '/generate-proposal' && request.method === 'POST') {
        return await handleGenerateProposal(request, env, corsHeaders);
      } else if (path === '/analyze-reference' && request.method === 'POST') {
        return await handleAnalyzeReference(request, env, corsHeaders);
      } else if (path === '/suggest-instrumentation' && request.method === 'POST') {
        return await handleSuggestInstrumentation(request, env, corsHeaders);
      } else if (path === '/estimate-project' && request.method === 'POST') {
        return await handleEstimateProject(request, env, corsHeaders);
      } else if (path === '/health') {
        return new Response(JSON.stringify({ 
          status: 'healthy',
          service: 'music-assistant',
          expertise: '40 years + AI'
        }), {
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      return new Response('Not Found', { status: 404 });

    } catch (error) {
      console.error('Error:', error);
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }
};

// Landing page
function handleLandingPage() {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Music Assistant - Fish Music Inc.</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #fff;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }
        h1 {
            font-size: 3rem;
            color: #e94560;
            margin-bottom: 1rem;
            text-align: center;
        }
        .subtitle {
            text-align: center;
            font-size: 1.3rem;
            color: #aaa;
            margin-bottom: 3rem;
        }
        .chat-box {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 2px solid rgba(233,69,96,0.3);
        }
        textarea {
            width: 100%;
            min-height: 150px;
            padding: 1rem;
            background: rgba(255,255,255,0.1);
            border: 2px solid rgba(233,69,96,0.3);
            border-radius: 8px;
            color: #fff;
            font-size: 1rem;
            font-family: inherit;
        }
        button {
            background: #e94560;
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 50px;
            font-size: 1.1rem;
            cursor: pointer;
            margin-top: 1rem;
            transition: all 0.3s;
        }
        button:hover {
            background: #d63651;
            transform: scale(1.05);
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 3rem;
        }
        .feature {
            background: rgba(255,255,255,0.05);
            padding: 1.5rem;
            border-radius: 10px;
            border: 2px solid rgba(233,69,96,0.2);
        }
        .feature h3 {
            color: #e94560;
            margin-bottom: 0.5rem;
        }
        #response {
            margin-top: 2rem;
            padding: 2rem;
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            border: 2px solid rgba(34,197,94,0.3);
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎵 AI Music Assistant</h1>
        <div class="subtitle">40 Years of Expertise + Cutting-Edge AI</div>
        
        <div class="chat-box">
            <h2 style="margin-bottom: 1rem;">Ask Me Anything About Music</h2>
            <textarea id="question" placeholder="Example: I need a cinematic score for a 3-minute trailer. The mood should be epic and inspiring. What instrumentation would work best?"></textarea>
            <button onclick="askQuestion()">Get AI Advice</button>
        </div>
        
        <div id="response"></div>
        
        <div class="features">
            <div class="feature">
                <h3>🎼 Composition Help</h3>
                <p>Get advice on melody, harmony, structure, and more</p>
            </div>
            <div class="feature">
                <h3>🎹 Instrumentation</h3>
                <p>Discover the perfect instrument combinations</p>
            </div>
            <div class="feature">
                <h3>💡 Creative Ideas</h3>
                <p>Brainstorm concepts and overcome creative blocks</p>
            </div>
            <div class="feature">
                <h3>📊 Project Planning</h3>
                <p>Get timeline and budget estimates</p>
            </div>
            <div class="feature">
                <h3>🎨 Genre Guidance</h3>
                <p>Learn genre conventions and best practices</p>
            </div>
            <div class="feature">
                <h3>🔍 Analysis</h3>
                <p>Understand what makes reference tracks work</p>
            </div>
        </div>
    </div>
    
    <script>
        async function askQuestion() {
            const question = document.getElementById('question').value;
            if (!question) return;
            
            const responseDiv = document.getElementById('response');
            responseDiv.style.display = 'block';
            responseDiv.innerHTML = '<p>🎵 Thinking...</p>';
            
            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    responseDiv.innerHTML = \`
                        <h3 style="color: #22c55e; margin-bottom: 1rem;">✨ AI Music Expert Says:</h3>
                        <div style="line-height: 1.8;">\${data.response}</div>
                    \`;
                } else {
                    responseDiv.innerHTML = '<p style="color: #ef4444;">Error: ' + data.error + '</p>';
                }
            } catch (error) {
                responseDiv.innerHTML = '<p style="color: #ef4444;">Error: ' + error.message + '</p>';
            }
        }
        
        // Allow Enter to submit
        document.getElementById('question').addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && e.ctrlKey) {
                askQuestion();
            }
        });
    </script>
</body>
</html>`;

  return new Response(html, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Ask question
async function handleAskQuestion(request, env, corsHeaders) {
  const data = await request.json();
  
  if (!data.question) {
    return new Response(JSON.stringify({ error: 'Missing question' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }

  const systemPrompt = `You are an AI music assistant for Fish Music Inc., a studio with 40 years of award-winning experience in composition and sound design. The founder won the Q107 Homegrown Contest in the early 1990s and has decades of expertise in:
- Film scoring
- Commercial music
- Game audio
- Sound design
- Music production
- Audio post-production

Provide expert, professional advice that combines classical music theory with modern production techniques. Be specific, practical, and draw on real-world experience. Format responses in HTML with proper paragraphs and lists for readability.`;

  const response = await queryAI(env, systemPrompt, data.question);
  
  // Log the interaction
  await logInteraction(env, {
    question: data.question,
    response: response,
    timestamp: new Date().toISOString()
  });
  
  return new Response(JSON.stringify({ 
    success: true,
    response: response 
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Generate project proposal
async function handleGenerateProposal(request, env, corsHeaders) {
  const data = await request.json();
  
  const prompt = `Generate a professional music project proposal with these details:
  
Project Type: ${data.project_type}
Client: ${data.client_name}
Project Title: ${data.title}
Description: ${data.description}
Budget Range: ${data.budget || 'To be discussed'}
Deadline: ${data.deadline || 'Flexible'}

Include:
1. Project Overview
2. Scope of Work
3. Deliverables
4. Timeline Breakdown
5. Investment Breakdown
6. Why Fish Music Inc. is the right choice (40 years experience, Q107 winner)
7. Next Steps

Format in professional HTML. Make it persuasive but professional.`;

  const response = await queryAI(env, 'You are a professional music producer creating project proposals.', prompt);
  
  return new Response(JSON.stringify({ 
    success: true,
    proposal: response
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Analyze reference track
async function handleAnalyzeReference(request, env, corsHeaders) {
  const data = await request.json();
  
  const prompt = `Analyze this reference track description and provide insights:

Track: ${data.track_name || 'Unknown'}
Genre: ${data.genre || 'Unknown'}
Description: ${data.description}

Provide analysis of:
1. Key musical elements (melody, harmony, rhythm, structure)
2. Instrumentation and production techniques
3. Emotional impact and how it's achieved
4. Genre-specific conventions used
5. How to create something similar
6. Estimated production complexity and timeline

Format in clear HTML sections.`;

  const response = await queryAI(env, 'You are a professional music analyst with 40 years of experience.', prompt);
  
  return new Response(JSON.stringify({ 
    success: true,
    analysis: response
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Suggest instrumentation
async function handleSuggestInstrumentation(request, env, corsHeaders) {
  const data = await request.json();
  
  const prompt = `Suggest instrumentation for this project:

Project Type: ${data.project_type}
Mood/Emotion: ${data.mood}
Genre: ${data.genre || 'Not specified'}
Duration: ${data.duration || 'Not specified'}
Budget Level: ${data.budget_level || 'Medium'}

Provide:
1. Primary instruments (lead roles)
2. Supporting instruments (harmony/rhythm)
3. Atmospheric/textural elements
4. Why each instrument choice works
5. Recording vs. MIDI considerations
6. Budget implications
7. Alternative options at different budget levels

Format in HTML with clear sections.`;

  const response = await queryAI(env, 'You are an expert orchestrator and music producer.', prompt);
  
  return new Response(JSON.stringify({ 
    success: true,
    suggestions: response
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Estimate project
async function handleEstimateProject(request, env, corsHeaders) {
  const data = await request.json();
  
  const prompt = `Provide a professional project estimate:

Project Type: ${data.project_type}
Duration/Length: ${data.duration}
Complexity: ${data.complexity || 'Medium'}
Instrumentation: ${data.instrumentation || 'Standard'}
Revisions Included: ${data.revisions || '2'}
Deadline: ${data.deadline || 'Standard (2-3 weeks)'}

Calculate and provide:
1. Composition time estimate
2. Recording/production time
3. Mixing/mastering time
4. Total project timeline
5. Investment breakdown by phase
6. What's included at different price points
7. Timeline flexibility options

Be realistic and professional. Fish Music Inc. charges premium rates for award-winning quality. Format in HTML.`;

  const response = await queryAI(env, 'You are a professional music producer providing project estimates.', prompt);
  
  return new Response(JSON.stringify({ 
    success: true,
    estimate: response
  }), {
    headers: { 'Content-Type': 'application/json', ...corsHeaders }
  });
}

// Query AI (Claude)
async function queryAI(env, systemPrompt, userPrompt) {
  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': env.ANTHROPIC_API_KEY || '',
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 2000,
        system: systemPrompt,
        messages: [{
          role: 'user',
          content: userPrompt
        }]
      })
    });

    const result = await response.json();
    return result.content[0].text;

  } catch (error) {
    console.error('AI query failed:', error);
    throw new Error('Failed to get AI response');
  }
}

// Log interaction
async function logInteraction(env, data) {
  const logId = `music_ai_${Date.now()}_${Math.random().toString(36).substring(7)}`;
  
  try {
    await env.CACHE.put(logId, JSON.stringify(data), {
      expirationTtl: 86400 // 24 hours
    });
  } catch (error) {
    console.error('Failed to log interaction:', error);
  }
}
