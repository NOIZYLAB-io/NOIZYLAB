/**
 * NoizyVerse XR Session Manager
 * Handles VR/AR session lifecycle
 */

export class XRSessionManager {
  constructor(renderer) {
    this.renderer = renderer;
    this.session = null;
    this.isImmersive = false;
    this.mode = null; // 'vr' | 'ar' | 'inline'
  }

  async checkSupport() {
    const support = {
      vr: false,
      ar: false
    };

    if (navigator.xr) {
      support.vr = await navigator.xr.isSessionSupported('immersive-vr');
      support.ar = await navigator.xr.isSessionSupported('immersive-ar');
    }

    return support;
  }

  async startVR() {
    if (!navigator.xr) {
      throw new Error('WebXR not supported');
    }

    this.session = await navigator.xr.requestSession('immersive-vr', {
      optionalFeatures: ['local-floor', 'bounded-floor', 'hand-tracking']
    });

    this.renderer.xr.setSession(this.session);
    this.isImmersive = true;
    this.mode = 'vr';

    this.session.addEventListener('end', () => this.onSessionEnd());

    return this.session;
  }

  async startAR() {
    if (!navigator.xr) {
      throw new Error('WebXR not supported');
    }

    this.session = await navigator.xr.requestSession('immersive-ar', {
      optionalFeatures: ['local-floor', 'hit-test', 'hand-tracking']
    });

    this.renderer.xr.setSession(this.session);
    this.isImmersive = true;
    this.mode = 'ar';

    this.session.addEventListener('end', () => this.onSessionEnd());

    return this.session;
  }

  async endSession() {
    if (this.session) {
      await this.session.end();
    }
  }

  onSessionEnd() {
    this.session = null;
    this.isImmersive = false;
    this.mode = null;
    window.dispatchEvent(new CustomEvent('noizyverse-session-end'));
  }

  getMode() {
    return this.mode;
  }

  isActive() {
    return this.isImmersive;
  }
}

