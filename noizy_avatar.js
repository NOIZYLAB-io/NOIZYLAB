import * as THREE from 'three';

/**
 * Noizy.AI Avatar
 * A visual AI companion in 3D space
 */

export class NoizyAvatar {
  constructor(scene) {
    this.scene = scene;
    this.group = new THREE.Group();
    this.state = 'idle'; // idle, thinking, speaking, listening
    this.emotionColor = 0xf5c542; // gold default
  }

  build() {
    // Main body - geometric orb
    this.createCore();
    
    // Eye/sensor ring
    this.createEyeRing();
    
    // Floating accent elements
    this.createAccents();
    
    // Audio visualizer ring
    this.createAudioRing();

    this.group.position.set(0, 1.5, -1);
    this.scene.add(this.group);
  }

  createCore() {
    // Inner core
    const coreGeometry = new THREE.IcosahedronGeometry(0.2, 2);
    const coreMaterial = new THREE.MeshStandardMaterial({
      color: 0x111111,
      roughness: 0.2,
      metalness: 0.9
    });
    this.core = new THREE.Mesh(coreGeometry, coreMaterial);
    this.group.add(this.core);

    // Outer shell (transparent)
    const shellGeometry = new THREE.IcosahedronGeometry(0.25, 1);
    const shellMaterial = new THREE.MeshBasicMaterial({
      color: this.emotionColor,
      transparent: true,
      opacity: 0.2,
      wireframe: true
    });
    this.shell = new THREE.Mesh(shellGeometry, shellMaterial);
    this.group.add(this.shell);
  }

  createEyeRing() {
    const ringGeometry = new THREE.TorusGeometry(0.15, 0.02, 8, 32);
    const ringMaterial = new THREE.MeshBasicMaterial({
      color: this.emotionColor
    });
    this.eyeRing = new THREE.Mesh(ringGeometry, ringMaterial);
    this.eyeRing.position.z = 0.15;
    this.group.add(this.eyeRing);

    // Eye dot
    const dotGeometry = new THREE.SphereGeometry(0.03);
    const dotMaterial = new THREE.MeshBasicMaterial({ color: 0xffffff });
    this.eyeDot = new THREE.Mesh(dotGeometry, dotMaterial);
    this.eyeDot.position.z = 0.18;
    this.group.add(this.eyeDot);
  }

  createAccents() {
    this.accents = [];
    const accentCount = 6;

    for (let i = 0; i < accentCount; i++) {
      const geometry = new THREE.TetrahedronGeometry(0.03);
      const material = new THREE.MeshBasicMaterial({
        color: this.emotionColor,
        transparent: true,
        opacity: 0.8
      });
      const accent = new THREE.Mesh(geometry, material);
      
      const angle = (i / accentCount) * Math.PI * 2;
      accent.position.x = Math.cos(angle) * 0.35;
      accent.position.y = Math.sin(angle) * 0.35;
      
      this.accents.push(accent);
      this.group.add(accent);
    }
  }

  createAudioRing() {
    const segments = 32;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(segments * 3);
    
    for (let i = 0; i < segments; i++) {
      const angle = (i / segments) * Math.PI * 2;
      positions[i * 3] = Math.cos(angle) * 0.3;
      positions[i * 3 + 1] = Math.sin(angle) * 0.3;
      positions[i * 3 + 2] = 0;
    }
    
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    
    const material = new THREE.LineBasicMaterial({
      color: this.emotionColor,
      transparent: true,
      opacity: 0.5
    });
    
    this.audioRing = new THREE.LineLoop(geometry, material);
    this.group.add(this.audioRing);
  }

  setState(state) {
    this.state = state;
  }

  setEmotion(emotion) {
    const colors = {
      neutral: 0xf5c542,   // gold
      happy: 0x00ff88,     // green
      calm: 0x00e5ff,      // cyan
      alert: 0xff3747,     // red
      thinking: 0x9966ff   // purple
    };
    
    this.emotionColor = colors[emotion] || colors.neutral;
    
    // Update materials
    if (this.shell) this.shell.material.color.setHex(this.emotionColor);
    if (this.eyeRing) this.eyeRing.material.color.setHex(this.emotionColor);
    this.accents.forEach(a => a.material.color.setHex(this.emotionColor));
    if (this.audioRing) this.audioRing.material.color.setHex(this.emotionColor);
  }

  speak(text) {
    this.setState('speaking');
    // Trigger speaking animation
    console.log(`Noizy.AI: ${text}`);
  }

  update(delta) {
    // Core rotation
    if (this.core) {
      this.core.rotation.y += delta * 0.5;
      this.core.rotation.x += delta * 0.2;
    }

    // Shell counter-rotation
    if (this.shell) {
      this.shell.rotation.y -= delta * 0.3;
    }

    // Accent orbit
    this.accents.forEach((accent, i) => {
      const time = Date.now() * 0.001;
      const angle = time + (i / this.accents.length) * Math.PI * 2;
      accent.position.x = Math.cos(angle) * 0.35;
      accent.position.y = Math.sin(angle) * 0.35;
      accent.rotation.x += delta * 2;
      accent.rotation.y += delta * 3;
    });

    // State-based animations
    if (this.state === 'thinking') {
      this.group.position.y = 1.5 + Math.sin(Date.now() * 0.003) * 0.05;
    } else if (this.state === 'speaking') {
      const scale = 1 + Math.sin(Date.now() * 0.01) * 0.1;
      this.audioRing.scale.set(scale, scale, 1);
    }

    // Eye tracking (look at camera)
    // This would track the camera position in a real implementation
  }

  lookAt(target) {
    this.group.lookAt(target);
  }

  dispose() {
    this.scene.remove(this.group);
  }
}

