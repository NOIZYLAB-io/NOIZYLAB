/**
 * NOIZY.AI AVATAR SIGNALS
 * Receives system state signals and translates to visual effects
 * SAFE: Data translation layer only
 */

import avatarState from './AvatarState.js';

class AvatarSignalReceiver {
  constructor() {
    this.websocket = null;
    this.pollInterval = null;
    this.isConnected = false;
  }

  // Connect to backend state router
  async connect(endpoint = 'ws://localhost:8000/ws/avatar') {
    try {
      this.websocket = new WebSocket(endpoint);
      
      this.websocket.onopen = () => {
        this.isConnected = true;
        console.log('[AVATAR] Signal connection established');
      };

      this.websocket.onmessage = (event) => {
        this.handleSignal(JSON.parse(event.data));
      };

      this.websocket.onclose = () => {
        this.isConnected = false;
        console.log('[AVATAR] Signal connection closed');
        // Auto-reconnect after 3 seconds
        setTimeout(() => this.connect(endpoint), 3000);
      };

      this.websocket.onerror = (error) => {
        console.error('[AVATAR] Signal error:', error);
      };

    } catch (error) {
      console.error('[AVATAR] Failed to connect:', error);
      // Fallback to polling
      this.startPolling();
    }
  }

  // Fallback polling mode
  startPolling(endpoint = '/api/avatar/state', interval = 500) {
    this.pollInterval = setInterval(async () => {
      try {
        const response = await fetch(endpoint);
        const data = await response.json();
        this.handleSignal(data);
      } catch (error) {
        // Silent fail during polling
      }
    }, interval);
  }

  stopPolling() {
    if (this.pollInterval) {
      clearInterval(this.pollInterval);
      this.pollInterval = null;
    }
  }

  // Process incoming signal
  handleSignal(signal) {
    // Mode changes
    if (signal.current_mode) {
      const modeMap = {
        'Safe Autopilot': 'SAFE_AUTOPILOT',
        'Technician Assist': 'TECHNICIAN_ASSIST',
        'Full AutoOps': 'FULL_AUTOOPS'
      };
      avatarState.setMode(modeMap[signal.current_mode] || 'SAFE_AUTOPILOT');
    }

    // System metrics
    if (signal.cpu_load !== undefined || signal.gpu_load !== undefined || signal.network_load !== undefined) {
      avatarState.setSystemMetrics({
        cpu: signal.cpu_load,
        gpu: signal.gpu_load,
        network: signal.network_load
      });
    }

    // Activity states
    if (signal.intent_in_progress !== undefined) {
      avatarState.setThinking(signal.intent_in_progress);
    }

    if (signal.diagnostics_running !== undefined) {
      avatarState.setProcessing(signal.diagnostics_running);
    }

    if (signal.is_speaking !== undefined) {
      avatarState.setTalking(signal.is_speaking);
    }

    // Error states
    if (signal.has_error !== undefined) {
      avatarState.setError(signal.has_error);
    }

    // Success events
    if (signal.task_completed) {
      avatarState.setSuccess();
    }

    // VR-specific
    if (signal.look_target) {
      avatarState.setLookTarget(signal.look_target);
    }

    if (signal.gesture) {
      avatarState.setGesture(signal.gesture);
    }
  }

  // Manual signal injection (for testing)
  inject(signal) {
    this.handleSignal(signal);
  }

  disconnect() {
    if (this.websocket) {
      this.websocket.close();
      this.websocket = null;
    }
    this.stopPolling();
    this.isConnected = false;
  }
}

export const avatarSignals = new AvatarSignalReceiver();
export default avatarSignals;

