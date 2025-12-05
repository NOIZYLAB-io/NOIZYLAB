/**
 * NOIZY.AI AVATAR BRIDGE
 * Connects frontend avatar to backend Orchestra Engine
 * SAFE: Pure data relay, no decision-making
 */

import avatarState from './AvatarState.js';
import avatarSignals from './AvatarSignals.js';

class AvatarBridge {
  constructor() {
    this.isInitialized = false;
    this.backendUrl = 'http://localhost:8000';
    this.wsUrl = 'ws://localhost:8000/ws/avatar';
  }

  async initialize() {
    if (this.isInitialized) return;

    try {
      // Connect signal receiver
      await avatarSignals.connect(this.wsUrl);
      
      // Fetch initial state
      await this.syncInitialState();
      
      this.isInitialized = true;
      console.log('[AVATAR BRIDGE] Initialized successfully');
      
    } catch (error) {
      console.error('[AVATAR BRIDGE] Initialization failed:', error);
      // Start in safe fallback mode
      avatarState.setMode('SAFE_AUTOPILOT');
      avatarState.setExpression('idle');
    }
  }

  async syncInitialState() {
    try {
      const response = await fetch(`${this.backendUrl}/api/system/state`);
      const data = await response.json();
      
      // Sync mode
      if (data.mode) {
        const modeMap = {
          'Safe Autopilot': 'SAFE_AUTOPILOT',
          'Technician Assist': 'TECHNICIAN_ASSIST',
          'Full AutoOps': 'FULL_AUTOOPS'
        };
        avatarState.setMode(modeMap[data.mode] || 'SAFE_AUTOPILOT');
      }

      // Sync metrics
      if (data.metrics) {
        avatarState.setSystemMetrics({
          cpu: data.metrics.cpu || 0,
          gpu: data.metrics.gpu || 0,
          network: data.metrics.network || 0
        });
      }

    } catch (error) {
      console.warn('[AVATAR BRIDGE] Could not fetch initial state:', error);
    }
  }

  // Send command to backend
  async sendCommand(command, params = {}) {
    try {
      const response = await fetch(`${this.backendUrl}/api/avatar/command`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command, params })
      });
      return await response.json();
    } catch (error) {
      console.error('[AVATAR BRIDGE] Command failed:', error);
      return { success: false, error: error.message };
    }
  }

  // Request mode change
  async requestModeChange(newMode) {
    avatarState.setThinking(true);
    const result = await this.sendCommand('set_mode', { mode: newMode });
    avatarState.setThinking(false);
    
    if (result.success) {
      avatarState.setSuccess();
    } else {
      avatarState.setError(true);
      setTimeout(() => avatarState.setError(false), 2000);
    }
    
    return result;
  }

  // Report VR interaction
  async reportInteraction(interactionType, data = {}) {
    return this.sendCommand('vr_interaction', {
      type: interactionType,
      ...data,
      timestamp: Date.now()
    });
  }

  // Report voice command
  async reportVoiceCommand(transcript) {
    avatarState.setExpression('attention');
    const result = await this.sendCommand('voice_command', { transcript });
    avatarState.setExpression('idle');
    return result;
  }

  // Get current avatar state for rendering
  getRenderState() {
    return {
      state: avatarState.getState(),
      colors: avatarState.getColors()
    };
  }

  // Subscribe to state changes
  onStateChange(callback) {
    return avatarState.subscribe(callback);
  }

  disconnect() {
    avatarSignals.disconnect();
    this.isInitialized = false;
  }
}

export const avatarBridge = new AvatarBridge();
export default avatarBridge;

