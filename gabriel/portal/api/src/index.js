// GABRIEL Vision API Worker
// NoizyLab - AI Hardware Verification
// Cloudflare Worker for edge-deployed PCB analysis

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };
    
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }
    
    // Route handling
    try {
      if (url.pathname === '/api/v1/scan/quick') {
        return await handleQuickScan(request, env, corsHeaders);
      }
      
      if (url.pathname === '/api/v1/scan/deep') {
        return await handleDeepScan(request, env, corsHeaders);
      }
      
      if (url.pathname === '/api/v1/reference/compare') {
        return await handleReferenceCompare(request, env, corsHeaders);
      }
      
      if (url.pathname === '/api/v1/voice/guidance') {
        return await handleVoiceGuidance(request, env, corsHeaders);
      }
      
      if (url.pathname === '/health') {
        return Response.json({ status: 'ok', version: '1.0.0' }, { headers: corsHeaders });
      }
      
      // Landing page
      if (url.pathname === '/' || url.pathname === '') {
        return new Response(getIndexHTML(), {
          headers: { ...corsHeaders, 'Content-Type': 'text/html' }
        });
      }
      
      return Response.json({ error: 'Not Found' }, { status: 404, headers: corsHeaders });
      
    } catch (error) {
      console.error('Worker error:', error);
      return Response.json(
        { error: 'Internal Server Error', message: error.message },
        { status: 500, headers: corsHeaders }
      );
    }
  }
};

// ============================================
// QUICK SCAN HANDLER
// ============================================

async function handleQuickScan(request, env, corsHeaders) {
  const startTime = Date.now();
  
  // Parse multipart form data
  const formData = await request.formData();
  const image = formData.get('image');
  const componentHint = formData.get('component_hint') || '';
  
  if (!image) {
    return Response.json(
      { error: 'No image provided' },
      { status: 400, headers: corsHeaders }
    );
  }
  
  // Generate scan ID
  const scanId = crypto.randomUUID();
  
  // Convert image to base64
  const imageBuffer = await image.arrayBuffer();
  const base64Image = btoa(String.fromCharCode(...new Uint8Array(imageBuffer)));
  
  // Store image in R2 for reference
  await env.R2_SCANS.put(`scans/${scanId}/original.${getExtension(image.name)}`, imageBuffer);
  
  // Call Gemini for vision analysis
  const visionResult = await analyzeWithGemini(base64Image, componentHint, env);
  
  // If anomalies found, get Claude reasoning
  let reasoning = null;
  if (visionResult.anomalies && visionResult.anomalies.length > 0) {
    reasoning = await reasonWithClaude(visionResult, env);
  }
  
  // Determine final status
  let status = 'PASS';
  let confidence = 0.95;
  
  if (reasoning) {
    if (reasoning.tamper_probability > 0.7) {
      status = 'REJECT';
    } else if (reasoning.tamper_probability > 0.3) {
      status = 'SUSPECT';
    }
    confidence = 1 - reasoning.tamper_probability;
  }
  
  const result = {
    scan_id: scanId,
    status: status,
    confidence: confidence,
    anomalies_found: visionResult.anomalies?.length || 0,
    anomalies: visionResult.anomalies?.slice(0, 5) || [],
    processing_time_ms: Date.now() - startTime,
    reasoning_summary: reasoning?.summary || null,
    upgrade_to_deep: visionResult.anomalies?.length > 3
  };
  
  // Store result in KV
  await env.KV_RESULTS.put(`scan:${scanId}`, JSON.stringify(result), { expirationTtl: 86400 * 7 });
  
  return Response.json(result, { headers: corsHeaders });
}

// ============================================
// DEEP SCAN HANDLER
// ============================================

async function handleDeepScan(request, env, corsHeaders) {
  // Verify API key
  const authHeader = request.headers.get('Authorization');
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return Response.json({ error: 'Unauthorized' }, { status: 401, headers: corsHeaders });
  }
  
  const apiKey = authHeader.substring(7);
  const keyValid = await validateApiKey(apiKey, env);
  if (!keyValid) {
    return Response.json({ error: 'Invalid API key' }, { status: 403, headers: corsHeaders });
  }
  
  const startTime = Date.now();
  const formData = await request.formData();
  const image = formData.get('image');
  const boardModel = formData.get('board_model') || '';
  const compareReference = formData.get('compare_reference') === 'true';
  const includeRepairGuidance = formData.get('include_repair_guidance') === 'true';
  
  const scanId = crypto.randomUUID();
  const imageBuffer = await image.arrayBuffer();
  const base64Image = btoa(String.fromCharCode(...new Uint8Array(imageBuffer)));
  
  // Store original
  await env.R2_SCANS.put(`scans/${scanId}/original.${getExtension(image.name)}`, imageBuffer);
  
  // Deep vision analysis
  const visionResult = await analyzeWithGeminiDeep(base64Image, boardModel, env);
  
  // Reference comparison
  let referenceComparison = null;
  if (compareReference && boardModel) {
    referenceComparison = await compareToGoldenReference(base64Image, boardModel, env);
  }
  
  // Extended Claude reasoning
  const reasoning = await reasonWithClaudeExtended(visionResult, referenceComparison, env);
  
  // Repair guidance
  let repairGuidance = null;
  if (includeRepairGuidance && reasoning.issues?.length > 0) {
    repairGuidance = await generateRepairGuidance(reasoning.issues, env);
  }
  
  const result = {
    analysis_id: scanId,
    vision_results: visionResult,
    reasoning_results: reasoning,
    reference_comparison: referenceComparison,
    repair_guidance: repairGuidance,
    processing_time_ms: Date.now() - startTime
  };
  
  // Store result
  await env.KV_RESULTS.put(`deep:${scanId}`, JSON.stringify(result), { expirationTtl: 86400 * 30 });
  
  return Response.json(result, { headers: corsHeaders });
}

// ============================================
// GEMINI VISION ANALYSIS
// ============================================

async function analyzeWithGemini(base64Image, componentHint, env) {
  const prompt = `You are a hardware inspection AI. Analyze this circuit board image for:

1. Component authenticity (die markings, package integrity)
2. Signs of rework (flux residue, solder reflow patterns)
3. Physical damage (corrosion, burns, cracks, bent pins)
4. Missing or replaced components
${componentHint ? `\nFocus especially on: ${componentHint}` : ''}

Return JSON format:
{
  "anomalies": [
    {
      "type": "counterfeit_indicator|rework_evidence|physical_damage|missing_component",
      "confidence": 0.0-1.0,
      "coordinates": [x1, y1, x2, y2],
      "description": "what you see"
    }
  ],
  "component_identification": {
    "detected_type": "type of board/component",
    "manufacturer_guess": "if identifiable"
  },
  "overall_condition": "good|fair|poor|critical"
}`;

  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=${env.GEMINI_API_KEY}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          parts: [
            { text: prompt },
            { inline_data: { mime_type: 'image/jpeg', data: base64Image }}
          ]
        }],
        generationConfig: {
          response_mime_type: 'application/json',
          temperature: 0.1
        }
      })
    }
  );
  
  const data = await response.json();
  
  try {
    const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
    return JSON.parse(text);
  } catch (e) {
    return { anomalies: [], error: 'Failed to parse Gemini response' };
  }
}

async function analyzeWithGeminiDeep(base64Image, boardModel, env) {
  const prompt = `Perform deep analysis of this circuit board.
${boardModel ? `Board model: ${boardModel}` : ''}

Analyze for:
1. ALL component anomalies (counterfeits, damage, rework)
2. Trace integrity (hairline fractures, corrosion)
3. Solder joint quality
4. Missing components vs reference
5. Connector condition
6. Signs of liquid damage
7. Thermal damage patterns

Return comprehensive JSON:
{
  "anomalies": [...],
  "trace_analysis": {
    "integrity": "good|damaged|unknown",
    "corrosion_areas": []
  },
  "solder_quality": {
    "cold_joints": [],
    "bridging": [],
    "missing_solder": []
  },
  "component_map": {
    "identified_components": [],
    "suspicious_components": []
  },
  "overall_assessment": "detailed text"
}`;

  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=${env.GEMINI_API_KEY}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          parts: [
            { text: prompt },
            { inline_data: { mime_type: 'image/jpeg', data: base64Image }}
          ]
        }],
        generationConfig: {
          response_mime_type: 'application/json',
          temperature: 0.1,
          max_output_tokens: 4096
        }
      })
    }
  );
  
  const data = await response.json();
  
  try {
    const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
    return JSON.parse(text);
  } catch (e) {
    return { anomalies: [], error: 'Failed to parse deep analysis' };
  }
}

// ============================================
// CLAUDE REASONING ENGINE
// ============================================

async function reasonWithClaude(visionResult, env) {
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2024-01-01',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 1024,
      messages: [{
        role: 'user',
        content: `Analyze these hardware inspection findings and provide a tamper/counterfeit probability assessment:

${JSON.stringify(visionResult, null, 2)}

Consider:
- Could anomalies be from normal wear?
- Are there multiple indicators suggesting tampering?
- What's the severity of findings?

Return JSON:
{
  "tamper_probability": 0.0-1.0,
  "counterfeit_probability": 0.0-1.0,
  "reasoning": "brief explanation",
  "summary": "one sentence verdict",
  "confidence_level": "high|medium|low"
}`
      }]
    })
  });
  
  const data = await response.json();
  
  try {
    const text = data.content?.[0]?.text;
    // Extract JSON from response
    const jsonMatch = text.match(/\{[\s\S]*\}/);
    return jsonMatch ? JSON.parse(jsonMatch[0]) : { tamper_probability: 0.5, summary: text };
  } catch (e) {
    return { tamper_probability: 0.5, error: 'Failed to parse Claude response' };
  }
}

async function reasonWithClaudeExtended(visionResult, referenceComparison, env) {
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2024-01-01',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 4096,
      messages: [{
        role: 'user',
        content: `Perform extended analysis of this hardware inspection.

Vision Analysis:
${JSON.stringify(visionResult, null, 2)}

${referenceComparison ? `Reference Comparison:\n${JSON.stringify(referenceComparison, null, 2)}` : ''}

Provide comprehensive assessment with:
1. Detailed reasoning for each anomaly
2. Root cause hypotheses
3. Repair recommendations
4. Risk assessment

Return JSON:
{
  "verdict": "PASS|SUSPECT|REJECT",
  "tamper_probability": 0.0-1.0,
  "issues": [
    {
      "component": "name",
      "issue": "description",
      "severity": "critical|high|medium|low",
      "root_cause": "hypothesis",
      "repair_possible": true|false,
      "repair_difficulty": 1-5
    }
  ],
  "evidence_chain": ["list of evidence supporting verdict"],
  "recommendations": ["what to do"],
  "summary": "overall assessment"
}`
      }]
    })
  });
  
  const data = await response.json();
  
  try {
    const text = data.content?.[0]?.text;
    const jsonMatch = text.match(/\{[\s\S]*\}/);
    return jsonMatch ? JSON.parse(jsonMatch[0]) : { verdict: 'UNKNOWN' };
  } catch (e) {
    return { verdict: 'ERROR', error: e.message };
  }
}

// ============================================
// GOLDEN REFERENCE COMPARISON
// ============================================

async function compareToGoldenReference(base64Image, boardModel, env) {
  // Look up reference in R2
  const referenceKey = `references/${boardModel.replace(/[^a-zA-Z0-9]/g, '_')}.json`;
  const reference = await env.R2_REFERENCES.get(referenceKey);
  
  if (!reference) {
    return {
      found: false,
      message: `No golden reference found for ${boardModel}`
    };
  }
  
  const refData = await reference.json();
  
  // Use Gemini to compare
  const prompt = `Compare this board image to the golden reference.
  
Reference data:
${JSON.stringify(refData.expected_components, null, 2)}

Identify:
1. Missing components vs reference
2. Extra/unexpected components
3. Position/alignment differences
4. Marking differences

Return JSON:
{
  "match_score": 0.0-1.0,
  "missing_components": [],
  "extra_components": [],
  "position_differences": [],
  "marking_differences": []
}`;

  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=${env.GEMINI_API_KEY}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          parts: [
            { text: prompt },
            { inline_data: { mime_type: 'image/jpeg', data: base64Image }}
          ]
        }],
        generationConfig: {
          response_mime_type: 'application/json'
        }
      })
    }
  );
  
  const data = await response.json();
  
  try {
    const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
    const result = JSON.parse(text);
    result.reference_id = refData.id;
    result.found = true;
    return result;
  } catch (e) {
    return { found: true, error: 'Comparison failed' };
  }
}

// ============================================
// VOICE GUIDANCE
// ============================================

async function handleVoiceGuidance(request, env, corsHeaders) {
  const { scan_id, issue_index } = await request.json();
  
  // Get scan results
  const scanData = await env.KV_RESULTS.get(`deep:${scan_id}`);
  if (!scanData) {
    return Response.json({ error: 'Scan not found' }, { status: 404, headers: corsHeaders });
  }
  
  const scan = JSON.parse(scanData);
  const issues = scan.reasoning_results?.issues || [];
  const issue = issues[issue_index] || issues[0];
  
  if (!issue) {
    return Response.json({ error: 'No issues to guide' }, { status: 404, headers: corsHeaders });
  }
  
  // Generate script
  const script = generateGuidanceScript(issue);
  
  // Call ElevenLabs
  const audioResponse = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${env.ELEVENLABS_VOICE_ID}`,
    {
      method: 'POST',
      headers: {
        'xi-api-key': env.ELEVENLABS_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text: script,
        model_id: 'eleven_turbo_v2_5',
        voice_settings: {
          stability: 0.7,
          similarity_boost: 0.9,
          style: 0.3
        }
      })
    }
  );
  
  if (!audioResponse.ok) {
    return Response.json({ error: 'Voice generation failed' }, { status: 500, headers: corsHeaders });
  }
  
  // Store and return audio URL
  const audioBuffer = await audioResponse.arrayBuffer();
  const audioId = crypto.randomUUID();
  await env.R2_SCANS.put(`audio/${audioId}.mp3`, audioBuffer);
  
  return Response.json({
    audio_url: `https://cdn.noizylab.ai/audio/${audioId}.mp3`,
    script: script,
    issue: issue
  }, { headers: corsHeaders });
}

function generateGuidanceScript(issue) {
  let script = `I found an issue with ${issue.component}. `;
  script += `${issue.issue}. `;
  
  if (issue.severity === 'critical') {
    script += `This is a critical issue that needs immediate attention. `;
  }
  
  if (issue.repair_possible) {
    script += `The good news is this can be repaired. `;
    script += `Difficulty level is ${issue.repair_difficulty} out of 5. `;
  } else {
    script += `Unfortunately, this component may need replacement. `;
  }
  
  if (issue.root_cause) {
    script += `The likely cause is ${issue.root_cause}. `;
  }
  
  return script;
}

async function generateRepairGuidance(issues, env) {
  const prompt = `Generate repair guidance for these issues:
${JSON.stringify(issues, null, 2)}

For each issue, provide:
1. Step-by-step repair instructions
2. Required tools
3. Difficulty level
4. Estimated time
5. Warnings/precautions

Return JSON array with repair steps for each issue.`;

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2024-01-01',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 2048,
      messages: [{ role: 'user', content: prompt }]
    })
  });
  
  const data = await response.json();
  
  try {
    const text = data.content?.[0]?.text;
    const jsonMatch = text.match(/\[[\s\S]*\]/);
    return jsonMatch ? JSON.parse(jsonMatch[0]) : [];
  } catch (e) {
    return [];
  }
}

// ============================================
// UTILITIES
// ============================================

async function validateApiKey(apiKey, env) {
  const keyData = await env.KV_API_KEYS.get(`key:${apiKey}`);
  if (!keyData) return false;
  
  const key = JSON.parse(keyData);
  return key.active && (!key.expires || key.expires > Date.now());
}

function getExtension(filename) {
  return filename?.split('.').pop()?.toLowerCase() || 'jpg';
}

function getIndexHTML() {
  return `<!DOCTYPE html>
<html>
<head>
  <title>GABRIEL API - NoizyLab</title>
  <style>
    body { font-family: system-ui; background: #0a0a0b; color: white; padding: 40px; }
    h1 { color: #ff6b00; }
    code { background: #1a1a1b; padding: 2px 6px; border-radius: 4px; }
    pre { background: #1a1a1b; padding: 20px; border-radius: 8px; overflow-x: auto; }
    a { color: #ff6b00; }
  </style>
</head>
<body>
  <h1>🔬 GABRIEL Vision API</h1>
  <p>AI-powered hardware verification by <a href="https://noizylab.ai">NoizyLab</a></p>
  
  <h2>Endpoints</h2>
  <pre>
POST /api/v1/scan/quick    - Quick authenticity check ($4.99)
POST /api/v1/scan/deep     - Deep analysis (Pro/Enterprise)
POST /api/v1/voice/guidance - Voice repair guidance
GET  /health               - API health check
  </pre>
  
  <h2>Quick Scan Example</h2>
  <pre>
curl -X POST https://api.noizylab.ai/api/v1/scan/quick \\
  -F "image=@board.jpg" \\
  -F "component_hint=CPU socket"
  </pre>
  
  <p>Version: 1.0.0 | <a href="https://docs.noizylab.ai">Documentation</a></p>
</body>
</html>`;
}
