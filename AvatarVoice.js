/**
 * NOIZY.AI AVATAR VOICE SYSTEM
 * Speech synthesis with personality tuning
 * SAFE: Configured TTS, not autonomous speech
 */

class AvatarVoice {
  constructor() {
    this.synth = window.speechSynthesis;
    this.voice = null;
    this.isInitialized = false;
    
    // Voice personality settings
    this.personality = {
      rate: 0.95,        // Slightly slower for clarity
      pitch: 1.0,        // Neutral pitch
      volume: 0.9,       // Comfortable volume
      warmth: 'neutral'  // neutral, warm, professional
    };
    
    // Mode-specific voice adjustments
    this.modeSettings = {
      SAFE_AUTOPILOT: {
        rate: 0.9,
        pitch: 1.0,
        prefix: 'Noizy AI System. '
      },
      TECHNICIAN_ASSIST: {
        rate: 1.0,
        pitch: 0.95,
        prefix: ''
      },
      FULL_AUTOOPS: {
        rate: 1.1,
        pitch: 1.0,
        prefix: ''
      }
    };
  }

  async initialize() {
    if (this.isInitialized) return;

    return new Promise((resolve) => {
      const loadVoices = () => {
        const voices = this.synth.getVoices();
        
        // Prefer high-quality voices
        const preferredVoices = [
          'Samantha',           // macOS
          'Google UK English Female',
          'Microsoft Zira',
          'Alex',               // macOS fallback
        ];
        
        for (const name of preferredVoices) {
          const found = voices.find(v => v.name.includes(name));
          if (found) {
            this.voice = found;
            break;
          }
        }
        
        // Fallback to first English voice
        if (!this.voice) {
          this.voice = voices.find(v => v.lang.startsWith('en')) || voices[0];
        }
        
        this.isInitialized = true;
        console.log('[AVATAR VOICE] Initialized with voice:', this.voice?.name);
        resolve();
      };

      if (this.synth.getVoices().length > 0) {
        loadVoices();
      } else {
        this.synth.onvoiceschanged = loadVoices;
      }
    });
  }

  /**
   * Speak text with current personality settings
   */
  speak(text, mode = 'SAFE_AUTOPILOT', options = {}) {
    if (!this.isInitialized) {
      console.warn('[AVATAR VOICE] Not initialized');
      return Promise.reject('Not initialized');
    }

    return new Promise((resolve, reject) => {
      // Cancel any current speech
      this.synth.cancel();

      const settings = this.modeSettings[mode] || this.modeSettings.SAFE_AUTOPILOT;
      const fullText = settings.prefix + text;

      const utterance = new SpeechSynthesisUtterance(fullText);
      utterance.voice = this.voice;
      utterance.rate = options.rate || settings.rate;
      utterance.pitch = options.pitch || settings.pitch;
      utterance.volume = options.volume || this.personality.volume;

      utterance.onend = () => {
        resolve();
      };

      utterance.onerror = (event) => {
        reject(event.error);
      };

      this.synth.speak(utterance);
    });
  }

  /**
   * Speak with warmth adjustment
   */
  speakWarm(text, mode) {
    return this.speak(text, mode, { pitch: 1.05, rate: 0.9 });
  }

  /**
   * Speak with urgency
   */
  speakUrgent(text, mode) {
    return this.speak(text, mode, { rate: 1.2, pitch: 1.1 });
  }

  /**
   * Speak confirmation
   */
  confirm(action) {
    return this.speak(`${action} confirmed.`, 'TECHNICIAN_ASSIST', { rate: 1.1 });
  }

  /**
   * Speak error
   */
  error(message) {
    return this.speak(`Alert. ${message}`, 'SAFE_AUTOPILOT', { pitch: 0.9 });
  }

  /**
   * Speak status update
   */
  status(message) {
    return this.speak(message, 'SAFE_AUTOPILOT');
  }

  /**
   * Stop all speech
   */
  stop() {
    this.synth.cancel();
  }

  /**
   * Check if currently speaking
   */
  isSpeaking() {
    return this.synth.speaking;
  }

  /**
   * Set personality warmth
   */
  setWarmth(level) {
    this.personality.warmth = level;
    switch (level) {
      case 'warm':
        this.personality.rate = 0.9;
        this.personality.pitch = 1.05;
        break;
      case 'professional':
        this.personality.rate = 1.0;
        this.personality.pitch = 0.95;
        break;
      default:
        this.personality.rate = 0.95;
        this.personality.pitch = 1.0;
    }
  }
}

export const avatarVoice = new AvatarVoice();
export default avatarVoice;

