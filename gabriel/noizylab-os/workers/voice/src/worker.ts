// ═══════════════════════════════════════════════════════════════════════════════
// NOIZYLAB VOICE WORKER - ElevenLabs Professional TTS
// "The Voice of Repair" Edition
// ═══════════════════════════════════════════════════════════════════════════════

export interface Env {
  ELEVENLABS_API_KEY: string;
  VOICE_ID: string;  // Your cloned voice ID
  R2_AUDIO: R2Bucket;
  DB: D1Database;
}

// ═══════════════════════════════════════════════════════════════════════════════
// EMOTIONAL MODES
// ═══════════════════════════════════════════════════════════════════════════════

interface VoiceSettings {
  stability: number;
  similarity_boost: number;
  style: number;
  use_speaker_boost: boolean;
}

const EMOTIONAL_MODES: Record<string, {
  description: string;
  settings: VoiceSettings;
  prefix?: string;
  suffix?: string;
}> = {
  FOCUS: {
    description: "Calm, precise micro-soldering guidance",
    settings: {
      stability: 0.75,
      similarity_boost: 0.85,
      style: 0.3,
      use_speaker_boost: true
    },
    prefix: "Okay, let's focus here... "
  },
  ALERT: {
    description: "Warning about ESD/damage risk",
    settings: {
      stability: 0.5,
      similarity_boost: 0.9,
      style: 0.6,
      use_speaker_boost: true
    },
    prefix: "Important! "
  },
  CELEBRATE: {
    description: "Successful repair confirmation",
    settings: {
      stability: 0.4,
      similarity_boost: 0.8,
      style: 0.8,
      use_speaker_boost: true
    },
    prefix: "Excellent! ",
    suffix: " Great work!"
  },
  EMPATHY: {
    description: "Component damage acknowledgment",
    settings: {
      stability: 0.7,
      similarity_boost: 0.85,
      style: 0.4,
      use_speaker_boost: true
    },
    prefix: "I understand... "
  },
  TEACHING: {
    description: "Instructional, step-by-step guidance",
    settings: {
      stability: 0.65,
      similarity_boost: 0.9,
      style: 0.5,
      use_speaker_boost: true
    }
  },
  HYPE: {
    description: "Maximum energy for introductions",
    settings: {
      stability: 0.3,
      similarity_boost: 0.75,
      style: 0.9,
      use_speaker_boost: true
    },
    prefix: "Let's GO! "
  },
  WHISPER: {
    description: "Quiet, confidential tone",
    settings: {
      stability: 0.8,
      similarity_boost: 0.95,
      style: 0.1,
      use_speaker_boost: false
    }
  },
  NEUTRAL: {
    description: "Standard delivery",
    settings: {
      stability: 0.5,
      similarity_boost: 0.75,
      style: 0.5,
      use_speaker_boost: true
    }
  }
};

// ═══════════════════════════════════════════════════════════════════════════════
// TEXT-TO-SPEECH
// ═══════════════════════════════════════════════════════════════════════════════

async function textToSpeech(
  env: Env,
  text: string,
  mode: string = "NEUTRAL",
  voiceId?: string
): Promise<ArrayBuffer> {
  const emotion = EMOTIONAL_MODES[mode.toUpperCase()] || EMOTIONAL_MODES.NEUTRAL;
  
  // Apply emotional prefix/suffix
  let processedText = text;
  if (emotion.prefix) processedText = emotion.prefix + processedText;
  if (emotion.suffix) processedText = processedText + emotion.suffix;
  
  const response = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${voiceId || env.VOICE_ID}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "xi-api-key": env.ELEVENLABS_API_KEY
      },
      body: JSON.stringify({
        text: processedText,
        model_id: "eleven_multilingual_v2",
        voice_settings: emotion.settings
      })
    }
  );
  
  if (!response.ok) {
    const error = await response.text();
    throw new Error(`ElevenLabs API error: ${error}`);
  }
  
  return response.arrayBuffer();
}

// ═══════════════════════════════════════════════════════════════════════════════
// SPEECH-TO-SPEECH (Voice Cloning with Emotion)
// ═══════════════════════════════════════════════════════════════════════════════

async function speechToSpeech(
  env: Env,
  audioBytes: ArrayBuffer,
  mode: string = "NEUTRAL",
  voiceId?: string
): Promise<ArrayBuffer> {
  const emotion = EMOTIONAL_MODES[mode.toUpperCase()] || EMOTIONAL_MODES.NEUTRAL;
  
  const formData = new FormData();
  formData.append("audio", new Blob([audioBytes], { type: "audio/mpeg" }));
  formData.append("model_id", "eleven_english_sts_v2");
  formData.append("voice_settings", JSON.stringify(emotion.settings));
  
  const response = await fetch(
    `https://api.elevenlabs.io/v1/speech-to-speech/${voiceId || env.VOICE_ID}`,
    {
      method: "POST",
      headers: {
        "xi-api-key": env.ELEVENLABS_API_KEY
      },
      body: formData
    }
  );
  
  if (!response.ok) {
    const error = await response.text();
    throw new Error(`ElevenLabs STS error: ${error}`);
  }
  
  return response.arrayBuffer();
}

// ═══════════════════════════════════════════════════════════════════════════════
// CALM MODE SCRIPT GENERATOR
// ═══════════════════════════════════════════════════════════════════════════════

interface CalmModeScript {
  id: string;
  type: "intro" | "step" | "warning" | "success" | "encouragement";
  text: string;
  mode: string;
  duration_estimate_ms: number;
}

function generateCalmModeScript(
  stepNumber: number,
  stepTitle: string,
  stepDetail: string,
  isWarning: boolean = false
): CalmModeScript[] {
  const scripts: CalmModeScript[] = [];
  
  // Step announcement
  scripts.push({
    id: `step-${stepNumber}-announce`,
    type: "step",
    text: `Step ${stepNumber}: ${stepTitle}`,
    mode: "TEACHING",
    duration_estimate_ms: 3000
  });
  
  // Warning if needed
  if (isWarning) {
    scripts.push({
      id: `step-${stepNumber}-warning`,
      type: "warning",
      text: "Be careful here. This is a sensitive component.",
      mode: "ALERT",
      duration_estimate_ms: 3500
    });
  }
  
  // Detail
  scripts.push({
    id: `step-${stepNumber}-detail`,
    type: "step",
    text: stepDetail,
    mode: "FOCUS",
    duration_estimate_ms: Math.max(4000, stepDetail.length * 50)
  });
  
  // Encouragement
  if (stepNumber % 3 === 0) {
    scripts.push({
      id: `step-${stepNumber}-encourage`,
      type: "encouragement",
      text: "You're doing great. Take your time.",
      mode: "EMPATHY",
      duration_estimate_ms: 2500
    });
  }
  
  return scripts;
}

// ═══════════════════════════════════════════════════════════════════════════════
// REPAIR GUIDE NARRATOR
// ═══════════════════════════════════════════════════════════════════════════════

interface RepairStep {
  title: string;
  detail: string;
  warnings?: string[];
  tools?: string[];
}

async function generateRepairAudio(
  env: Env,
  repairName: string,
  steps: RepairStep[]
): Promise<{ audioKey: string; scripts: CalmModeScript[] }> {
  const allScripts: CalmModeScript[] = [];
  const audioChunks: ArrayBuffer[] = [];
  
  // Intro
  const introScript: CalmModeScript = {
    id: "intro",
    type: "intro",
    text: `Welcome to the ${repairName} repair guide. Let's get started.`,
    mode: "TEACHING",
    duration_estimate_ms: 4000
  };
  allScripts.push(introScript);
  audioChunks.push(await textToSpeech(env, introScript.text, introScript.mode));
  
  // Steps
  for (let i = 0; i < steps.length; i++) {
    const step = steps[i];
    const hasWarning = step.warnings && step.warnings.length > 0;
    
    const stepScripts = generateCalmModeScript(i + 1, step.title, step.detail, hasWarning);
    
    for (const script of stepScripts) {
      allScripts.push(script);
      audioChunks.push(await textToSpeech(env, script.text, script.mode));
      
      // Rate limit
      await new Promise(r => setTimeout(r, 200));
    }
  }
  
  // Success outro
  const outroScript: CalmModeScript = {
    id: "outro",
    type: "success",
    text: `Congratulations! You've completed the ${repairName} repair. Power on and test your device.`,
    mode: "CELEBRATE",
    duration_estimate_ms: 5000
  };
  allScripts.push(outroScript);
  audioChunks.push(await textToSpeech(env, outroScript.text, outroScript.mode));
  
  // Combine audio
  const totalLength = audioChunks.reduce((sum, chunk) => sum + chunk.byteLength, 0);
  const combined = new Uint8Array(totalLength);
  let offset = 0;
  for (const chunk of audioChunks) {
    combined.set(new Uint8Array(chunk), offset);
    offset += chunk.byteLength;
  }
  
  // Store in R2
  const audioKey = `repairs/${repairName.replace(/\s+/g, "-").toLowerCase()}-${Date.now()}.mp3`;
  await env.R2_AUDIO.put(audioKey, combined.buffer, {
    httpMetadata: { contentType: "audio/mpeg" }
  });
  
  return { audioKey, scripts: allScripts };
}

// ═══════════════════════════════════════════════════════════════════════════════
// WORKER
// ═══════════════════════════════════════════════════════════════════════════════

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json"
    };

    if (method === "OPTIONS") {
      return new Response(null, {
        headers: {
          ...corsHeaders,
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type"
        }
      });
    }

    try {
      // Health
      if (path === "/health") {
        return Response.json({ ok: true, service: "voice" }, { headers: corsHeaders });
      }

      // List emotional modes
      if (path === "/modes") {
        const modes = Object.entries(EMOTIONAL_MODES).map(([name, config]) => ({
          name,
          description: config.description
        }));
        return Response.json({ ok: true, modes }, { headers: corsHeaders });
      }

      // Text-to-Speech
      if (path === "/tts" && method === "POST") {
        const body = await request.json() as any;
        const { text, mode, voice_id } = body;
        
        if (!text) {
          return Response.json({ ok: false, error: "Missing text" }, { status: 400, headers: corsHeaders });
        }
        
        const audio = await textToSpeech(env, text, mode || "NEUTRAL", voice_id);
        
        return new Response(audio, {
          headers: {
            "Content-Type": "audio/mpeg",
            "Access-Control-Allow-Origin": "*"
          }
        });
      }

      // Speech-to-Speech
      if (path === "/sts" && method === "POST") {
        const formData = await request.formData();
        const audioFile = formData.get("audio") as File;
        const mode = formData.get("mode") as string || "NEUTRAL";
        
        if (!audioFile) {
          return Response.json({ ok: false, error: "Missing audio" }, { status: 400, headers: corsHeaders });
        }
        
        const audioBytes = await audioFile.arrayBuffer();
        const result = await speechToSpeech(env, audioBytes, mode);
        
        return new Response(result, {
          headers: {
            "Content-Type": "audio/mpeg",
            "Access-Control-Allow-Origin": "*"
          }
        });
      }

      // Generate repair guide audio
      if (path === "/repair-guide" && method === "POST") {
        const body = await request.json() as any;
        const { name, steps } = body;
        
        if (!name || !steps || !Array.isArray(steps)) {
          return Response.json(
            { ok: false, error: "Missing name or steps" },
            { status: 400, headers: corsHeaders }
          );
        }
        
        const result = await generateRepairAudio(env, name, steps);
        
        // Generate signed URL for audio
        // In production, you'd use a signed URL
        const audioUrl = `https://your-r2-domain/${result.audioKey}`;
        
        return Response.json({
          ok: true,
          audioKey: result.audioKey,
          audioUrl,
          scripts: result.scripts,
          totalDuration: result.scripts.reduce((sum, s) => sum + s.duration_estimate_ms, 0)
        }, { headers: corsHeaders });
      }

      // Get stored audio
      if (path.startsWith("/audio/") && method === "GET") {
        const key = path.replace("/audio/", "");
        const object = await env.R2_AUDIO.get(key);
        
        if (!object) {
          return Response.json({ ok: false, error: "Not found" }, { status: 404, headers: corsHeaders });
        }
        
        return new Response(object.body, {
          headers: {
            "Content-Type": "audio/mpeg",
            "Access-Control-Allow-Origin": "*",
            "Cache-Control": "public, max-age=86400"
          }
        });
      }

      return Response.json({ ok: false, error: "Not found" }, { status: 404, headers: corsHeaders });

    } catch (err: any) {
      console.error("Voice worker error:", err);
      return Response.json(
        { ok: false, error: err.message || "Internal error" },
        { status: 500, headers: corsHeaders }
      );
    }
  }
};
