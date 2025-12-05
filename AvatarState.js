/**
 * NOIZY.AI AVATAR STATE MANAGER
 * Tracks current visual state of the holographic interface
 * SAFE: State vectors, not consciousness
 */

import { getModeColor, getLoadColor } from './AvatarModeColors.js';

class AvatarStateManager {
  constructor() {
    this.state = {
      // Operational mode
      mode: 'SAFE_AUTOPILOT',
      
      // System metrics (0-100)
      cpuLoad: 0,
      gpuLoad: 0,
      networkLoad: 0,
      
      // Expression state
      expression: 'idle',
      
      // Activity flags
      isThinking: false,
      isProcessing: false,
      isTalking: false,
      hasError: false,
      
      // Animation state
      pulseRate: 1.0,
      glowIntensity: 0.6,
      geometryScale: 1.0,
      
      // VR state
      isVisible: true,
      lookTarget: null,
      gestureActive: null
    };
    
    this.listeners = [];
  }

  subscribe(callback) {
    this.listeners.push(callback);
    return () => {
      this.listeners = this.listeners.filter(l => l !== callback);
    };
  }

  notify() {
    this.listeners.forEach(cb => cb(this.state));
  }

  setMode(mode) {
    this.state.mode = mode;
    const colors = getModeColor(mode);
    this.state.glowIntensity = colors.intensity;
    this.notify();
  }

  setExpression(expression) {
    this.state.expression = expression;
    this.notify();
  }

  setSystemMetrics({ cpu, gpu, network }) {
    if (cpu !== undefined) this.state.cpuLoad = cpu;
    if (gpu !== undefined) this.state.gpuLoad = gpu;
    if (network !== undefined) this.state.networkLoad = network;
    
    // Adjust geometry based on load
    const avgLoad = (this.state.cpuLoad + this.state.gpuLoad) / 2;
    this.state.geometryScale = 1.0 + (avgLoad / 200); // Subtle swelling
    
    this.notify();
  }

  setThinking(isThinking) {
    this.state.isThinking = isThinking;
    this.state.expression = isThinking ? 'thinking' : 'idle';
    this.notify();
  }

  setProcessing(isProcessing) {
    this.state.isProcessing = isProcessing;
    this.state.expression = isProcessing ? 'processing' : 'idle';
    this.notify();
  }

  setTalking(isTalking) {
    this.state.isTalking = isTalking;
    this.state.expression = isTalking ? 'talking' : 'idle';
    this.notify();
  }

  setError(hasError) {
    this.state.hasError = hasError;
    this.state.expression = hasError ? 'error' : 'idle';
    this.notify();
  }

  setSuccess() {
    this.state.expression = 'success';
    this.notify();
    // Auto-reset after pulse
    setTimeout(() => {
      this.state.expression = 'idle';
      this.notify();
    }, 1500);
  }

  setLookTarget(target) {
    this.state.lookTarget = target;
    this.notify();
  }

  setGesture(gesture) {
    this.state.gestureActive = gesture;
    this.notify();
  }

  getState() {
    return { ...this.state };
  }

  getColors() {
    return {
      mode: getModeColor(this.state.mode),
      cpu: getLoadColor('cpu', this.state.cpuLoad),
      gpu: getLoadColor('gpu', this.state.gpuLoad),
      network: getLoadColor('network', this.state.networkLoad)
    };
  }
}

export const avatarState = new AvatarStateManager();
export default avatarState;

