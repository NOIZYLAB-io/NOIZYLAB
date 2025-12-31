/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * GORUNFREE - Voice Command Processor
 * Real-time voice transcription + command execution
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  AI: any;
  KV: KVNamespace;
  ANTHROPIC_API_KEY?: string;
  ANTIGRAVITY_URL?: string;
}

interface VoiceCommand {
  id: string;
  transcription: string;
  intent: string | null;
  action: string | null;
  confidence: number;
  processed_at: string;
}

// ═══════════════════════════════════════════════════════════════════════════════
// COMMAND PATTERNS
// ═══════════════════════════════════════════════════════════════════════════════

const COMMAND_PATTERNS = [
  { pattern: /^(hey |ok )?(antigravity|gabriel|heaven)/i, intent: 'invoke_circle' },
  { pattern: /(truth|daze|today)/i, intent: 'dazeflow' },
  { pattern: /(check.?in|how.?am.?i|feeling)/i, intent: 'lifeluv' },
  { pattern: /(play|music|song|noizyvox)/i, intent: 'noizyvox' },
  { pattern: /(status|health|system)/i, intent: 'status' },
  { pattern: /(help|what can|commands)/i, intent: 'help' }
];

// ═══════════════════════════════════════════════════════════════════════════════
// APP SETUP
// ═══════════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization']
}));

// ═══════════════════════════════════════════════════════════════════════════════
// ROUTES
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/', (c) => {
  return c.json({
    name: 'GORUNFREE',
    version: '1.0.0',
    status: 'operational',
    mission: 'Voice Command Processor',
    endpoints: [
      '/health',
      '/transcribe',
      '/process',
      '/commands',
      '/speak'
    ]
  });
});

app.get('/health', async (c) => {
  return c.json({
    worker: 'ok',
    ai: c.env.AI ? 'available' : 'not_configured',
    anthropic: c.env.ANTHROPIC_API_KEY ? 'configured' : 'not_configured',
    timestamp: new Date().toISOString()
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// VOICE TRANSCRIPTION
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/transcribe', async (c) => {
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

    const transcription = result.text || '';
    
    // Detect intent from transcription
    let intent = null;
    for (const cmd of COMMAND_PATTERNS) {
      if (cmd.pattern.test(transcription)) {
        intent = cmd.intent;
        break;
      }
    }

    const command: VoiceCommand = {
      id: `voice-${Date.now()}`,
      transcription,
      intent,
      action: null,
      confidence: result.confidence || 0.9,
      processed_at: new Date().toISOString()
    };

    // Store in KV for history
    await c.env.KV.put(
      `gorunfree:${command.id}`,
      JSON.stringify(command),
      { expirationTtl: 86400 * 7 } // 7 days
    );

    return c.json(command);
  } catch (error) {
    return c.json({ 
      error: 'Transcription failed',
      details: error instanceof Error ? error.message : 'Unknown error'
    }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// COMMAND PROCESSING
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/process', async (c) => {
  const body = await c.req.json<{ text: string }>();

  if (!body.text) {
    return c.json({ error: 'text required' }, 400);
  }

  const text = body.text.toLowerCase();

  // Detect intent
  let intent = 'general';
  let action = null;

  for (const cmd of COMMAND_PATTERNS) {
    if (cmd.pattern.test(text)) {
      intent = cmd.intent;
      break;
    }
  }

  // Process based on intent
  switch (intent) {
    case 'invoke_circle':
      // Extract member name
      const members = ['gabriel', 'shirl', 'pops', 'engr_keith', 'dream', 'heaven', 'lucy', 'sonic'];
      const foundMember = members.find(m => text.includes(m));
      action = foundMember 
        ? { type: 'invoke_circle', member: foundMember, endpoint: `/circle/${foundMember}/invoke` }
        : { type: 'invoke_circle', member: 'gabriel', endpoint: '/circle/gabriel/invoke' };
      break;

    case 'dazeflow':
      action = { type: 'dazeflow', endpoint: '/daze/today' };
      break;

    case 'lifeluv':
      action = { type: 'lifeluv', endpoint: '/lifeluv/checkin' };
      break;

    case 'status':
      action = { type: 'status', endpoint: '/health' };
      break;

    case 'help':
      action = {
        type: 'help',
        commands: [
          'Hey Gabriel/Shirl/Pops/etc - Talk to Circle of 8',
          'Capture my truth - DAZEFLOW entry',
          'Check in / How am I - LIFELUV',
          'System status - Health check'
        ]
      };
      break;

    default:
      // Use AI to understand the command if Anthropic is configured
      if (c.env.ANTHROPIC_API_KEY) {
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
              max_tokens: 256,
              system: 'You are a voice command processor. Analyze the command and return JSON with: intent (string), action (string), parameters (object). Keep it concise.',
              messages: [{ role: 'user', content: `Process voice command: "${text}"` }]
            })
          });

          const data = await response.json() as any;
          const aiResponse = data.content?.[0]?.text;
          
          try {
            action = JSON.parse(aiResponse);
          } catch {
            action = { type: 'ai_response', response: aiResponse };
          }
        } catch {
          action = { type: 'unknown', original: text };
        }
      } else {
        action = { type: 'unknown', original: text };
      }
  }

  return c.json({
    text: body.text,
    intent,
    action,
    timestamp: new Date().toISOString()
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// TEXT TO SPEECH (Generate speech URL)
// ═══════════════════════════════════════════════════════════════════════════════

app.post('/speak', async (c) => {
  const body = await c.req.json<{ text: string; voice?: string }>();

  if (!body.text) {
    return c.json({ error: 'text required' }, 400);
  }

  // Return a response that clients can use with Web Speech API
  // or system TTS commands
  return c.json({
    text: body.text,
    voice: body.voice || 'default',
    ssml: `<speak>${body.text}</speak>`,
    commands: {
      macos: `say "${body.text.replace(/"/g, '\\"')}"`,
      linux: `espeak "${body.text.replace(/"/g, '\\"')}"`,
      windows: `powershell -c "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('${body.text.replace(/'/g, "''")}')"`,
      web: 'Use Web Speech API speechSynthesis.speak()'
    }
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// COMMAND HISTORY
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/commands', async (c) => {
  const commands: VoiceCommand[] = [];
  
  // List recent commands from KV
  const list = await c.env.KV.list({ prefix: 'gorunfree:' });
  
  for (const key of list.keys.slice(0, 20)) {
    const data = await c.env.KV.get(key.name);
    if (data) {
      commands.push(JSON.parse(data));
    }
  }

  return c.json({
    total: commands.length,
    commands: commands.sort((a, b) => 
      new Date(b.processed_at).getTime() - new Date(a.processed_at).getTime()
    )
  });
});

export default app;
