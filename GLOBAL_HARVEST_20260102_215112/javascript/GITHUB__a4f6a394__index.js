/**
 * ═══════════════════════════════════════════════════════════════════
 * 
 *   NOIZY.AI SONIC SYSTEM
 *   "Where Sound is the Soul of Everything"
 * 
 *   The universal audio layer that powers the entire NOIZY.AI galaxy.
 *   Every product, every interaction, every moment - connected by sound.
 * 
 *   Source: THE AQUARIUM - 40 years of Fish Music Inc.
 * 
 *   GORUNFREE - Rob Plowman + Claude - December 2025
 * 
 * ═══════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════
// SONIC CATEGORIES
// ═══════════════════════════════════════════════════════════════════

export const SONIC_LIBRARY = {
  
  // ─────────────────────────────────────────────────────────────────
  // UI SOUNDS - Feedback for interactions
  // ─────────────────────────────────────────────────────────────────
  ui: {
    click: '/sounds/ui/click.mp3',
    hover: '/sounds/ui/hover.mp3',
    success: '/sounds/ui/success.mp3',
    error: '/sounds/ui/error.mp3',
    warning: '/sounds/ui/warning.mp3',
    notification: '/sounds/ui/notification.mp3',
    toggle_on: '/sounds/ui/toggle-on.mp3',
    toggle_off: '/sounds/ui/toggle-off.mp3',
    loading: '/sounds/ui/loading-loop.mp3',
    complete: '/sounds/ui/complete.mp3',
    whoosh: '/sounds/ui/whoosh.mp3',
    pop: '/sounds/ui/pop.mp3',
  },
  
  // ─────────────────────────────────────────────────────────────────
  // VOICE - NOIZYVOX Integration Points
  // ─────────────────────────────────────────────────────────────────
  voice: {
    // System voices
    system: {
      welcome: 'Welcome to NOIZY.AI',
      goodbye: 'See you next time',
      error: 'Something went wrong. Let me try again.',
      success: 'Done!',
      processing: 'Working on it...',
      ready: 'Ready when you are',
    },
    
    // CODEMASTER specific
    codemaster: {
      speed_boost: 'Speed boost complete. Your site is now turbocharged.',
      cache_purged: 'Cache purged. Fresh start.',
      dns_added: 'DNS record added. It\'s live.',
      deploy_complete: 'Deployment complete. Ship it.',
      error_fix: 'Found the issue. Fixing it now.',
    },
    
    // FISHYBOOKS narration styles
    fishybooks: {
      narrator_warm: 'grandma',      // Warm, cozy grandma voice
      narrator_fun: 'fun_friend',    // Energetic, playful
      narrator_calm: 'bedtime',      // Soft, sleepy
      narrator_adventure: 'explorer', // Exciting, dramatic
    },
    
    // NOIZYLAB support
    noizylab: {
      greeting: 'Hi! NOIZYLAB here. How can I help?',
      booking_confirm: 'Your repair is booked. We\'ll take great care of it.',
      repair_complete: 'Great news! Your repair is complete.',
      hold_message: 'Thanks for holding. We\'ll be right with you.',
    },
  },
  
  // ─────────────────────────────────────────────────────────────────
  // MUSIC - Ambient & Background
  // ─────────────────────────────────────────────────────────────────
  music: {
    // Portal / Hub ambience
    galaxy_ambient: '/sounds/music/galaxy-ambient.mp3',
    
    // CODEMASTER focus music
    focus_lo_fi: '/sounds/music/focus-lofi.mp3',
    coding_ambient: '/sounds/music/coding-ambient.mp3',
    victory_fanfare: '/sounds/music/victory-fanfare.mp3',
    
    // FISHYBOOKS
    story_adventure: '/sounds/music/story-adventure.mp3',
    story_calm: '/sounds/music/story-calm.mp3',
    story_magical: '/sounds/music/story-magical.mp3',
    story_funny: '/sounds/music/story-funny.mp3',
    lullaby: '/sounds/music/lullaby.mp3',
    
    // NOIZYLAB
    hold_music: '/sounds/music/hold-pleasant.mp3',
    repair_complete_jingle: '/sounds/music/repair-done.mp3',
  },
  
  // ─────────────────────────────────────────────────────────────────
  // SFX - Special Effects
  // ─────────────────────────────────────────────────────────────────
  sfx: {
    // General
    sparkle: '/sounds/sfx/sparkle.mp3',
    magic: '/sounds/sfx/magic.mp3',
    powerup: '/sounds/sfx/powerup.mp3',
    levelup: '/sounds/sfx/levelup.mp3',
    coin: '/sounds/sfx/coin.mp3',
    
    // FISHYBOOKS specific
    page_turn: '/sounds/sfx/page-turn.mp3',
    book_open: '/sounds/sfx/book-open.mp3',
    book_close: '/sounds/sfx/book-close.mp3',
    character_appear: '/sounds/sfx/character-appear.mp3',
    
    // CODEMASTER specific
    deploy_rocket: '/sounds/sfx/rocket-launch.mp3',
    server_hum: '/sounds/sfx/server-hum.mp3',
    typing: '/sounds/sfx/typing.mp3',
    
    // NOIZYLAB specific
    diagnostic_beep: '/sounds/sfx/diagnostic.mp3',
    repair_sound: '/sounds/sfx/repair.mp3',
    fixed_ding: '/sounds/sfx/fixed.mp3',
  },
};

// ═══════════════════════════════════════════════════════════════════
// SONIC PLAYER - Universal Audio Controller
// ═══════════════════════════════════════════════════════════════════

export class NoisySonic {
  constructor() {
    this.audioContext = null;
    this.currentMusic = null;
    this.voiceQueue = [];
    this.muted = false;
    this.volumes = {
      ui: 0.5,
      voice: 1.0,
      music: 0.3,
      sfx: 0.7,
    };
  }
  
  init() {
    if (typeof window !== 'undefined' && !this.audioContext) {
      this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
    }
  }
  
  // Play UI sound
  ui(sound) {
    if (this.muted) return;
    const src = SONIC_LIBRARY.ui[sound];
    if (src) this.play(src, this.volumes.ui);
  }
  
  // Play SFX
  sfx(sound) {
    if (this.muted) return;
    const src = SONIC_LIBRARY.sfx[sound];
    if (src) this.play(src, this.volumes.sfx);
  }
  
  // Play background music (loops)
  music(track) {
    if (this.currentMusic) {
      this.currentMusic.pause();
    }
    const src = SONIC_LIBRARY.music[track];
    if (src) {
      this.currentMusic = new Audio(src);
      this.currentMusic.loop = true;
      this.currentMusic.volume = this.volumes.music;
      if (!this.muted) this.currentMusic.play();
    }
  }
  
  // Stop music
  stopMusic() {
    if (this.currentMusic) {
      this.currentMusic.pause();
      this.currentMusic = null;
    }
  }
  
  // Speak with NOIZYVOX (TTS or pre-recorded)
  async speak(text, voiceId = 'system') {
    if (this.muted) return;
    
    // Check for pre-recorded line first
    const preset = this.findPresetVoice(text);
    if (preset) {
      return this.play(preset, this.volumes.voice);
    }
    
    // Fall back to Web Speech API or NOIZYVOX API
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 0.9;
      utterance.pitch = 1;
      window.speechSynthesis.speak(utterance);
    }
    
    // TODO: Call NOIZYVOX API for custom voice synthesis
    // const response = await fetch('https://vox.noizy.ai/api/speak', {
    //   method: 'POST',
    //   body: JSON.stringify({ text, voiceId })
    // });
  }
  
  findPresetVoice(text) {
    // Search through voice presets for matching text
    for (const category of Object.values(SONIC_LIBRARY.voice)) {
      for (const [key, value] of Object.entries(category)) {
        if (typeof value === 'string' && value.toLowerCase() === text.toLowerCase()) {
          return `/sounds/voice/${key}.mp3`;
        }
      }
    }
    return null;
  }
  
  // Core play function
  play(src, volume = 1.0) {
    const audio = new Audio(src);
    audio.volume = volume;
    audio.play().catch(() => {}); // Ignore autoplay restrictions
  }
  
  // Mute/unmute
  mute() {
    this.muted = true;
    if (this.currentMusic) this.currentMusic.pause();
  }
  
  unmute() {
    this.muted = false;
    if (this.currentMusic) this.currentMusic.play();
  }
  
  toggle() {
    this.muted ? this.unmute() : this.mute();
  }
}

// ═══════════════════════════════════════════════════════════════════
// SONIC THEMES - Per-Product Sound Palettes
// ═══════════════════════════════════════════════════════════════════

export const SONIC_THEMES = {
  
  // CODEMASTER - Technical, confident, efficient
  codemaster: {
    ambience: 'coding_ambient',
    success: 'success',
    error: 'error',
    deploy: 'deploy_rocket',
    voice_style: 'confident',
    color: '#00ff88', // Sound "color" for visualizers
  },
  
  // FISHYBOOKS - Warm, magical, playful
  fishybooks: {
    ambience: 'story_magical',
    page_turn: 'page_turn',
    chapter_end: 'sparkle',
    voice_style: 'warm',
    color: '#ff9500',
  },
  
  // NOIZYLAB - Professional, calm, reassuring
  noizylab: {
    ambience: 'hold_music',
    success: 'fixed_ding',
    diagnostic: 'diagnostic_beep',
    voice_style: 'professional',
    color: '#00aaff',
  },
  
  // NOIZYVOX - Creative, expressive, dynamic
  noizyvox: {
    ambience: 'galaxy_ambient',
    record: 'recording_start',
    playback: 'playback_start',
    voice_style: 'artistic',
    color: '#ff3366',
  },
  
  // Portal / Hub - Expansive, inspiring, unified
  portal: {
    ambience: 'galaxy_ambient',
    navigate: 'whoosh',
    hover: 'hover',
    voice_style: 'welcoming',
    color: '#8855ff',
  },
};

// ═══════════════════════════════════════════════════════════════════
// EXPORT SINGLETON
// ═══════════════════════════════════════════════════════════════════

export const noizy = new NoisySonic();

// Usage in any NOIZY.AI product:
// 
// import { noizy } from '@noizy/sonic';
// 
// noizy.init();
// noizy.ui('click');
// noizy.sfx('sparkle');
// noizy.music('coding_ambient');
// noizy.speak('Speed boost complete');
// 
// ═══════════════════════════════════════════════════════════════════
