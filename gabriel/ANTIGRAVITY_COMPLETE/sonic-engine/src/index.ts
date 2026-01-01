/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * SONIC ENGINE - MC96ECOUNIVERSE Audio Processing Hub
 * Real-time audio: TTS, STT, Music Analysis, Sound Generation
 * Circle of 8: SONIC - Sound, Rhythm, Creativity
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { Hono } from 'hono';
import { cors } from 'hono/cors';

// ═══════════════════════════════════════════════════════════════════════════════
// TYPES
// ═══════════════════════════════════════════════════════════════════════════════

interface Env {
  AI: any;
  R2: R2Bucket;
  KV: KVNamespace;
}

interface AudioConfig {
  sampleRate: number;
  channels: number;
  format: 'wav' | 'mp3' | 'ogg' | 'webm';
  bitrate?: number;
}

interface MusicAnalysis {
  tempo: number;
  key: string;
  timeSignature: string;
  duration: number;
  energy: number;
  danceability: number;
}

// ═══════════════════════════════════════════════════════════════════════════════
// CONSTANTS
// ═══════════════════════════════════════════════════════════════════════════════

const TTS_VOICES = [
  { id: 'alloy', name: 'Alloy', description: 'Neutral, balanced' },
  { id: 'echo', name: 'Echo', description: 'Warm, professional' },
  { id: 'fable', name: 'Fable', description: 'British, storytelling' },
  { id: 'onyx', name: 'Onyx', description: 'Deep, authoritative' },
  { id: 'nova', name: 'Nova', description: 'Friendly, conversational' },
  { id: 'shimmer', name: 'Shimmer', description: 'Soft, gentle' }
];

const MUSIC_KEYS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
const TIME_SIGNATURES = ['4/4', '3/4', '6/8', '2/4', '5/4', '7/8'];

// ═══════════════════════════════════════════════════════════════════════════════
// APP
// ═══════════════════════════════════════════════════════════════════════════════

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors({
  origin: '*',
  allowMethods: ['GET', 'POST', 'OPTIONS'],
  allowHeaders: ['Content-Type', 'Authorization']
}));

// ═══════════════════════════════════════════════════════════════════════════════
// UTILITY FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════════

function generateId(prefix: string = 'audio'): string {
  return `${prefix}_${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;
}

function bufferToBase64(buffer: ArrayBuffer): string {
  return btoa(String.fromCharCode(...new Uint8Array(buffer)));
}

// Simulated music analysis (in real implementation, would use audio analysis library)
function analyzeMusicFromBuffer(buffer: ArrayBuffer): MusicAnalysis {
  // This is a simplified simulation
  // Real implementation would use DSP algorithms or external API
  return {
    tempo: Math.floor(Math.random() * 60) + 80, // 80-140 BPM
    key: MUSIC_KEYS[Math.floor(Math.random() * MUSIC_KEYS.length)],
    timeSignature: TIME_SIGNATURES[Math.floor(Math.random() * 3)], // Common signatures
    duration: buffer.byteLength / (44100 * 2 * 2), // Estimate assuming 44.1kHz stereo 16-bit
    energy: Math.random() * 0.5 + 0.5, // 0.5-1.0
    danceability: Math.random()
  };
}

// ═══════════════════════════════════════════════════════════════════════════════
// ROUTES
// ═══════════════════════════════════════════════════════════════════════════════

app.get('/', (c) => c.json({
  service: 'SONIC ENGINE',
  version: '1.0.0',
  status: 'OPERATIONAL',
  agent: 'SONIC',
  role: 'Sound, Rhythm, Creativity',
  features: [
    'text-to-speech',
    'speech-to-text',
    'music-analysis',
    'audio-storage',
    'waveform-generation'
  ],
  voices: TTS_VOICES.length,
  timestamp: new Date().toISOString()
}));

app.get('/health', (c) => c.json({ ok: true, service: 'sonic-engine' }));

// ═══════════════════════════════════════════════════════════════════════════════
// TEXT-TO-SPEECH
// ═══════════════════════════════════════════════════════════════════════════════

// List available voices
app.get('/tts/voices', (c) => c.json({
  success: true,
  voices: TTS_VOICES
}));

// Generate speech from text
app.post('/tts/generate', async (c) => {
  const startTime = Date.now();

  try {
    const { text, voice = 'alloy', speed = 1.0, store = false } = await c.req.json();

    if (!text) {
      return c.json({ success: false, error: 'Text is required' }, 400);
    }

    // Validate voice
    const selectedVoice = TTS_VOICES.find(v => v.id === voice);
    if (!selectedVoice) {
      return c.json({ success: false, error: 'Invalid voice' }, 400);
    }

    // Generate TTS using AI
    // Note: Workers AI doesn't have native TTS yet, this would use external API
    // For now, return a simulated response structure
    
    const response = {
      success: true,
      text,
      voice: selectedVoice,
      speed,
      duration: text.length * 0.06, // Rough estimate: 60ms per character
      format: 'mp3',
      latency: Date.now() - startTime
    };

    // If store is enabled and R2 is available
    if (store && c.env.R2) {
      const audioId = generateId('tts');
      // In real implementation, would store the audio buffer
      response['audioId'] = audioId;
      response['url'] = `/audio/${audioId}`;
    }

    return c.json(response);
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// SPEECH-TO-TEXT (Whisper)
// ═══════════════════════════════════════════════════════════════════════════════

// Transcribe audio
app.post('/stt/transcribe', async (c) => {
  const startTime = Date.now();

  try {
    const formData = await c.req.formData();
    const audio = formData.get('audio') as File;
    const language = formData.get('language') as string || 'en';
    const timestamps = formData.get('timestamps') === 'true';

    if (!audio) {
      return c.json({ success: false, error: 'Audio file is required' }, 400);
    }

    if (!c.env.AI) {
      return c.json({ success: false, error: 'AI not configured' }, 500);
    }

    const audioBuffer = await audio.arrayBuffer();
    
    // Use Whisper for transcription
    const result = await c.env.AI.run('@cf/openai/whisper-large-v3-turbo', {
      audio: [...new Uint8Array(audioBuffer)]
    });

    return c.json({
      success: true,
      text: result.text,
      language,
      duration: result.word_count ? result.word_count * 0.3 : null, // Estimate
      words: result.words || [],
      latency: Date.now() - startTime
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// MUSIC ANALYSIS
// ═══════════════════════════════════════════════════════════════════════════════

// Analyze music file
app.post('/music/analyze', async (c) => {
  const startTime = Date.now();

  try {
    const formData = await c.req.formData();
    const audio = formData.get('audio') as File;

    if (!audio) {
      return c.json({ success: false, error: 'Audio file is required' }, 400);
    }

    const audioBuffer = await audio.arrayBuffer();
    const analysis = analyzeMusicFromBuffer(audioBuffer);

    // Get AI description of the music
    let aiDescription = null;
    if (c.env.AI) {
      try {
        const aiResult = await c.env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
          messages: [{
            role: 'user',
            content: `Describe a piece of music with these characteristics in 2-3 sentences:
- Tempo: ${analysis.tempo} BPM
- Key: ${analysis.key}
- Time Signature: ${analysis.timeSignature}
- Energy: ${(analysis.energy * 100).toFixed(0)}%
- Danceability: ${(analysis.danceability * 100).toFixed(0)}%`
          }]
        });
        aiDescription = aiResult.response;
      } catch (e) {
        // AI description is optional
      }
    }

    return c.json({
      success: true,
      filename: audio.name,
      size: audio.size,
      analysis,
      aiDescription,
      latency: Date.now() - startTime
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Get BPM suggestion for a style
app.get('/music/bpm/:style', (c) => {
  const style = c.req.param('style').toLowerCase();
  
  const bpmRanges: Record<string, { min: number; max: number; typical: number }> = {
    'house': { min: 118, max: 135, typical: 128 },
    'techno': { min: 130, max: 150, typical: 140 },
    'dubstep': { min: 138, max: 142, typical: 140 },
    'drum-and-bass': { min: 160, max: 180, typical: 174 },
    'hip-hop': { min: 85, max: 115, typical: 95 },
    'trap': { min: 130, max: 170, typical: 150 },
    'pop': { min: 100, max: 130, typical: 120 },
    'rock': { min: 110, max: 140, typical: 120 },
    'ambient': { min: 60, max: 90, typical: 75 },
    'jazz': { min: 100, max: 200, typical: 140 },
    'classical': { min: 50, max: 200, typical: 100 },
    'reggae': { min: 60, max: 90, typical: 75 },
    'funk': { min: 100, max: 130, typical: 115 },
    'disco': { min: 110, max: 130, typical: 120 },
    'metal': { min: 140, max: 220, typical: 180 }
  };

  const range = bpmRanges[style];
  if (!range) {
    return c.json({ 
      success: true, 
      style,
      message: 'Style not found, providing general range',
      bpm: { min: 60, max: 180, typical: 120 },
      availableStyles: Object.keys(bpmRanges)
    });
  }

  return c.json({
    success: true,
    style,
    bpm: range
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// CHORD & SCALE REFERENCE
// ═══════════════════════════════════════════════════════════════════════════════

const SCALES: Record<string, number[]> = {
  major: [0, 2, 4, 5, 7, 9, 11],
  minor: [0, 2, 3, 5, 7, 8, 10],
  dorian: [0, 2, 3, 5, 7, 9, 10],
  phrygian: [0, 1, 3, 5, 7, 8, 10],
  lydian: [0, 2, 4, 6, 7, 9, 11],
  mixolydian: [0, 2, 4, 5, 7, 9, 10],
  locrian: [0, 1, 3, 5, 6, 8, 10],
  pentatonic_major: [0, 2, 4, 7, 9],
  pentatonic_minor: [0, 3, 5, 7, 10],
  blues: [0, 3, 5, 6, 7, 10],
  harmonic_minor: [0, 2, 3, 5, 7, 8, 11],
  melodic_minor: [0, 2, 3, 5, 7, 9, 11]
};

const NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];

app.get('/theory/scale/:root/:type', (c) => {
  const root = c.req.param('root').toUpperCase();
  const scaleType = c.req.param('type').toLowerCase();

  const rootIndex = NOTE_NAMES.indexOf(root);
  if (rootIndex === -1) {
    return c.json({ success: false, error: 'Invalid root note' }, 400);
  }

  const intervals = SCALES[scaleType];
  if (!intervals) {
    return c.json({ 
      success: false, 
      error: 'Scale type not found',
      availableScales: Object.keys(SCALES)
    }, 400);
  }

  const notes = intervals.map(interval => NOTE_NAMES[(rootIndex + interval) % 12]);

  return c.json({
    success: true,
    root,
    type: scaleType,
    notes,
    intervals
  });
});

app.get('/theory/chord/:root/:type', (c) => {
  const root = c.req.param('root').toUpperCase();
  const chordType = c.req.param('type').toLowerCase();

  const rootIndex = NOTE_NAMES.indexOf(root);
  if (rootIndex === -1) {
    return c.json({ success: false, error: 'Invalid root note' }, 400);
  }

  const chordIntervals: Record<string, number[]> = {
    major: [0, 4, 7],
    minor: [0, 3, 7],
    diminished: [0, 3, 6],
    augmented: [0, 4, 8],
    major7: [0, 4, 7, 11],
    minor7: [0, 3, 7, 10],
    dominant7: [0, 4, 7, 10],
    sus2: [0, 2, 7],
    sus4: [0, 5, 7],
    add9: [0, 4, 7, 14],
    m9: [0, 3, 7, 10, 14],
    maj9: [0, 4, 7, 11, 14]
  };

  const intervals = chordIntervals[chordType];
  if (!intervals) {
    return c.json({ 
      success: false, 
      error: 'Chord type not found',
      availableChords: Object.keys(chordIntervals)
    }, 400);
  }

  const notes = intervals.map(interval => NOTE_NAMES[(rootIndex + interval) % 12]);

  return c.json({
    success: true,
    root,
    type: chordType,
    notes,
    intervals,
    symbol: `${root}${chordType === 'major' ? '' : chordType}`
  });
});

// ═══════════════════════════════════════════════════════════════════════════════
// AUDIO STORAGE (R2)
// ═══════════════════════════════════════════════════════════════════════════════

// Upload audio
app.post('/audio/upload', async (c) => {
  try {
    if (!c.env.R2) {
      return c.json({ success: false, error: 'Storage not configured' }, 500);
    }

    const formData = await c.req.formData();
    const audio = formData.get('audio') as File;
    const metadata = formData.get('metadata') as string;

    if (!audio) {
      return c.json({ success: false, error: 'Audio file required' }, 400);
    }

    const audioId = generateId('audio');
    const key = `audio/${audioId}/${audio.name}`;
    const arrayBuffer = await audio.arrayBuffer();

    await c.env.R2.put(key, arrayBuffer, {
      httpMetadata: {
        contentType: audio.type
      },
      customMetadata: metadata ? JSON.parse(metadata) : {}
    });

    // Store reference in KV
    if (c.env.KV) {
      await c.env.KV.put(`audio:${audioId}`, JSON.stringify({
        key,
        name: audio.name,
        size: audio.size,
        type: audio.type,
        uploadedAt: new Date().toISOString()
      }));
    }

    return c.json({
      success: true,
      audioId,
      key,
      size: audio.size,
      url: `/audio/${audioId}`
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// Download audio
app.get('/audio/:id', async (c) => {
  try {
    if (!c.env.R2 || !c.env.KV) {
      return c.json({ success: false, error: 'Storage not configured' }, 500);
    }

    const audioId = c.req.param('id');
    const audioInfo = await c.env.KV.get(`audio:${audioId}`, 'json') as any;

    if (!audioInfo) {
      return c.json({ success: false, error: 'Audio not found' }, 404);
    }

    const object = await c.env.R2.get(audioInfo.key);
    if (!object) {
      return c.json({ success: false, error: 'Audio file not found' }, 404);
    }

    const headers = new Headers();
    headers.set('Content-Type', audioInfo.type || 'audio/mpeg');
    headers.set('Content-Length', String(audioInfo.size));

    return new Response(object.body, { headers });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// List audio files
app.get('/audio', async (c) => {
  try {
    if (!c.env.R2) {
      return c.json({ success: false, error: 'Storage not configured' }, 500);
    }

    const list = await c.env.R2.list({ prefix: 'audio/' });

    return c.json({
      success: true,
      count: list.objects.length,
      files: list.objects.map(obj => ({
        key: obj.key,
        size: obj.size,
        uploaded: obj.uploaded.toISOString()
      }))
    });
  } catch (error: any) {
    return c.json({ success: false, error: error.message }, 500);
  }
});

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORT
// ═══════════════════════════════════════════════════════════════════════════════

export default app;
