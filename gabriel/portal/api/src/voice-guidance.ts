/**
 * Voice Guidance System for NoizyLab
 * 
 * Integrates with ElevenLabs for natural voice synthesis
 * Provides hands-free repair guidance during PCB work
 */

interface VoiceConfig {
  voiceId: string;
  stability: number;
  similarityBoost: number;
  speakingRate: number;
}

interface RepairStep {
  order: number;
  action: string;
  tools: string[];
  technique: string;
  warnings: string[];
}

// Default voice configuration
const DEFAULT_VOICE_CONFIG: VoiceConfig = {
  voiceId: 'EXAVITQu4vr4xnSDxMaL', // Sarah - clear, professional
  stability: 0.7,
  similarityBoost: 0.8,
  speakingRate: 1.0
};

// Available voices
const VOICES = {
  sarah: { id: 'EXAVITQu4vr4xnSDxMaL', name: 'Sarah', description: 'Clear, professional' },
  josh: { id: 'TxGEqnHWrfWFTfGW9XjX', name: 'Josh', description: 'Deep, authoritative' },
  bella: { id: 'EXAVITQu4vr4xnSDxMaL', name: 'Bella', description: 'Warm, friendly' },
  adam: { id: 'pNInz6obpgDQGcFmaJgB', name: 'Adam', description: 'Calm, measured' }
};

/**
 * Generate speech for a repair step
 */
export async function speakRepairStep(
  step: RepairStep,
  config: VoiceConfig = DEFAULT_VOICE_CONFIG,
  env: Env
): Promise<ArrayBuffer> {
  // Build natural-sounding script
  const script = buildStepScript(step);
  
  return synthesizeSpeech(script, config, env);
}

/**
 * Build natural script from repair step
 */
function buildStepScript(step: RepairStep): string {
  let script = `Step ${step.order}: ${step.action}. `;
  
  if (step.technique) {
    script += `${step.technique} `;
  }
  
  if (step.tools.length > 0) {
    script += `You'll need: ${step.tools.join(', ')}. `;
  }
  
  if (step.warnings.length > 0) {
    script += `Warning: ${step.warnings[0]}. `;
  }
  
  return script;
}

/**
 * Generate introduction speech
 */
export async function speakIntroduction(
  diagnosis: string,
  difficulty: string,
  estimatedTime: string,
  config: VoiceConfig = DEFAULT_VOICE_CONFIG,
  env: Env
): Promise<ArrayBuffer> {
  const script = `
    Let's get started with your repair. 
    ${diagnosis}. 
    This is rated ${difficulty} difficulty and should take about ${estimatedTime}. 
    Make sure you have good lighting and a stable workspace. 
    Say "next" when you're ready for the first step.
  `.trim().replace(/\s+/g, ' ');
  
  return synthesizeSpeech(script, config, env);
}

/**
 * Generate completion speech
 */
export async function speakCompletion(
  success: boolean,
  config: VoiceConfig = DEFAULT_VOICE_CONFIG,
  env: Env
): Promise<ArrayBuffer> {
  const script = success
    ? "Excellent work! All repairs have been completed. Your board should now be functional. Consider running another scan to verify the fixes."
    : "The guided repair session has ended. Some steps may require professional assistance. Please review the report for next steps.";
  
  return synthesizeSpeech(script, config, env);
}

/**
 * Generate warning speech
 */
export async function speakWarning(
  warning: string,
  config: VoiceConfig = DEFAULT_VOICE_CONFIG,
  env: Env
): Promise<ArrayBuffer> {
  const script = `Attention! ${warning}. Please proceed with caution.`;
  return synthesizeSpeech(script, config, env);
}

/**
 * Synthesize speech using ElevenLabs API
 */
async function synthesizeSpeech(
  text: string,
  config: VoiceConfig,
  env: Env
): Promise<ArrayBuffer> {
  const response = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${config.voiceId}`,
    {
      method: 'POST',
      headers: {
        'xi-api-key': env.ELEVENLABS_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text,
        model_id: 'eleven_turbo_v2',
        voice_settings: {
          stability: config.stability,
          similarity_boost: config.similarityBoost,
          speaking_rate: config.speakingRate
        }
      })
    }
  );
  
  if (!response.ok) {
    throw new Error(`ElevenLabs API error: ${response.status}`);
  }
  
  return response.arrayBuffer();
}

/**
 * Stream speech for real-time playback
 */
export async function streamSpeech(
  text: string,
  config: VoiceConfig = DEFAULT_VOICE_CONFIG,
  env: Env
): Promise<ReadableStream> {
  const response = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${config.voiceId}/stream`,
    {
      method: 'POST',
      headers: {
        'xi-api-key': env.ELEVENLABS_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text,
        model_id: 'eleven_turbo_v2',
        voice_settings: {
          stability: config.stability,
          similarity_boost: config.similarityBoost
        }
      })
    }
  );
  
  if (!response.ok || !response.body) {
    throw new Error(`ElevenLabs streaming error: ${response.status}`);
  }
  
  return response.body;
}

/**
 * Voice guidance session manager (client-side)
 */
export class VoiceGuidanceSession {
  private audioContext: AudioContext;
  private currentAudio: AudioBufferSourceNode | null = null;
  private queue: ArrayBuffer[] = [];
  private isPlaying = false;
  private onStepComplete?: () => void;
  
  constructor() {
    this.audioContext = new AudioContext();
  }
  
  /**
   * Play audio buffer
   */
  async play(audioData: ArrayBuffer): Promise<void> {
    const audioBuffer = await this.audioContext.decodeAudioData(audioData.slice(0));
    
    return new Promise((resolve) => {
      this.currentAudio = this.audioContext.createBufferSource();
      this.currentAudio.buffer = audioBuffer;
      this.currentAudio.connect(this.audioContext.destination);
      
      this.currentAudio.onended = () => {
        this.isPlaying = false;
        this.playNext();
        resolve();
      };
      
      this.isPlaying = true;
      this.currentAudio.start();
    });
  }
  
  /**
   * Add audio to queue
   */
  enqueue(audioData: ArrayBuffer): void {
    this.queue.push(audioData);
    if (!this.isPlaying) {
      this.playNext();
    }
  }
  
  /**
   * Play next item in queue
   */
  private async playNext(): Promise<void> {
    if (this.queue.length > 0) {
      const next = this.queue.shift();
      if (next) {
        await this.play(next);
      }
    }
  }
  
  /**
   * Stop current playback
   */
  stop(): void {
    if (this.currentAudio) {
      this.currentAudio.stop();
      this.currentAudio = null;
    }
    this.queue = [];
    this.isPlaying = false;
  }
  
  /**
   * Pause playback
   */
  pause(): void {
    if (this.audioContext.state === 'running') {
      this.audioContext.suspend();
    }
  }
  
  /**
   * Resume playback
   */
  resume(): void {
    if (this.audioContext.state === 'suspended') {
      this.audioContext.resume();
    }
  }
  
  /**
   * Set callback for step completion
   */
  setOnStepComplete(callback: () => void): void {
    this.onStepComplete = callback;
  }
  
  /**
   * Clean up resources
   */
  destroy(): void {
    this.stop();
    this.audioContext.close();
  }
}

/**
 * Voice command recognition (client-side)
 */
export class VoiceCommandRecognizer {
  private recognition: SpeechRecognition | null = null;
  private commands: Map<string, () => void> = new Map();
  
  constructor() {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
      this.recognition = new SpeechRecognition();
      this.recognition.continuous = true;
      this.recognition.interimResults = false;
      
      this.recognition.onresult = (event: SpeechRecognitionEvent) => {
        const transcript = event.results[event.results.length - 1][0].transcript.toLowerCase().trim();
        this.handleCommand(transcript);
      };
    }
  }
  
  /**
   * Register a voice command
   */
  registerCommand(phrase: string, callback: () => void): void {
    this.commands.set(phrase.toLowerCase(), callback);
  }
  
  /**
   * Handle recognized command
   */
  private handleCommand(transcript: string): void {
    for (const [phrase, callback] of this.commands) {
      if (transcript.includes(phrase)) {
        callback();
        break;
      }
    }
  }
  
  /**
   * Start listening
   */
  start(): void {
    this.recognition?.start();
  }
  
  /**
   * Stop listening
   */
  stop(): void {
    this.recognition?.stop();
  }
}

// Default voice commands
export const DEFAULT_COMMANDS = {
  'next': 'Go to next step',
  'repeat': 'Repeat current step',
  'pause': 'Pause guidance',
  'resume': 'Resume guidance',
  'stop': 'End session',
  'help': 'Get help'
};

interface Env {
  ELEVENLABS_API_KEY: string;
}

export { VOICES, DEFAULT_VOICE_CONFIG };
export type { VoiceConfig, RepairStep };
