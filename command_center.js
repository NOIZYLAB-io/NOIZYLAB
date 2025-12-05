import * as THREE from 'three';

/**
 * NoizyVerse Command Center
 * The main holographic dashboard environment
 */

export class CommandCenter {
  constructor(scene) {
    this.scene = scene;
    this.objects = [];
    this.panels = [];
  }

  build() {
    // Circular platform
    this.createPlatform();
    
    // Holographic panels in a semicircle
    this.createHoloPanels();
    
    // Central AI orb
    this.createAIOrb();
    
    // Ambient effects
    this.createAmbientEffects();
  }

  createPlatform() {
    const platformGeometry = new THREE.CylinderGeometry(4, 4.2, 0.2, 64);
    const platformMaterial = new THREE.MeshStandardMaterial({
      color: 0x0a0a0a,
      roughness: 0.3,
      metalness: 0.8
    });
    const platform = new THREE.Mesh(platformGeometry, platformMaterial);
    platform.position.y = -0.1;
    this.scene.add(platform);
    this.objects.push(platform);

    // Edge glow ring
    const ringGeometry = new THREE.TorusGeometry(4.1, 0.03, 16, 100);
    const ringMaterial = new THREE.MeshBasicMaterial({
      color: 0xf5c542,
      transparent: true,
      opacity: 0.8
    });
    const ring = new THREE.Mesh(ringGeometry, ringMaterial);
    ring.rotation.x = Math.PI / 2;
    ring.position.y = 0;
    this.scene.add(ring);
    this.objects.push(ring);
  }

  createHoloPanels() {
    const panelCount = 5;
    const radius = 3;
    const panelData = [
      { title: 'DEVICES', color: 0xf5c542 },
      { title: 'DIAGNOSTICS', color: 0x00e5ff },
      { title: 'AI STATUS', color: 0xf5c542 },
      { title: 'NETWORK', color: 0x00ff88 },
      { title: 'ALERTS', color: 0xff3747 }
    ];

    for (let i = 0; i < panelCount; i++) {
      const angle = (Math.PI / 4) + (i * Math.PI / 4);
      const x = Math.sin(angle) * radius;
      const z = -Math.cos(angle) * radius;

      const panel = this.createPanel(panelData[i]);
      panel.position.set(x, 1.5, z);
      panel.lookAt(0, 1.5, 0);
      
      this.scene.add(panel);
      this.panels.push(panel);
      this.objects.push(panel);
    }
  }

  createPanel(data) {
    const group = new THREE.Group();

    // Panel background
    const panelGeometry = new THREE.PlaneGeometry(1.2, 0.8);
    const panelMaterial = new THREE.MeshBasicMaterial({
      color: 0x000000,
      transparent: true,
      opacity: 0.7,
      side: THREE.DoubleSide
    });
    const panel = new THREE.Mesh(panelGeometry, panelMaterial);
    group.add(panel);

    // Border
    const borderGeometry = new THREE.EdgesGeometry(panelGeometry);
    const borderMaterial = new THREE.LineBasicMaterial({ color: data.color });
    const border = new THREE.LineSegments(borderGeometry, borderMaterial);
    group.add(border);

    // Title bar
    const titleGeometry = new THREE.PlaneGeometry(1.2, 0.1);
    const titleMaterial = new THREE.MeshBasicMaterial({
      color: data.color,
      transparent: true,
      opacity: 0.3
    });
    const titleBar = new THREE.Mesh(titleGeometry, titleMaterial);
    titleBar.position.y = 0.35;
    group.add(titleBar);

    // Store panel data
    group.userData = { ...data, interactive: true };

    return group;
  }

  createAIOrb() {
    // Core orb
    const orbGeometry = new THREE.SphereGeometry(0.3, 32, 32);
    const orbMaterial = new THREE.MeshBasicMaterial({
      color: 0xf5c542,
      transparent: true,
      opacity: 0.8
    });
    const orb = new THREE.Mesh(orbGeometry, orbMaterial);
    orb.position.set(0, 1.2, 0);
    this.scene.add(orb);
    this.objects.push(orb);
    this.aiOrb = orb;

    // Outer glow
    const glowGeometry = new THREE.SphereGeometry(0.35, 32, 32);
    const glowMaterial = new THREE.MeshBasicMaterial({
      color: 0xffd95c,
      transparent: true,
      opacity: 0.2
    });
    const glow = new THREE.Mesh(glowGeometry, glowMaterial);
    orb.add(glow);

    // Orbiting rings
    for (let i = 0; i < 3; i++) {
      const ringGeometry = new THREE.TorusGeometry(0.4 + i * 0.1, 0.01, 8, 50);
      const ringMaterial = new THREE.MeshBasicMaterial({
        color: 0xf5c542,
        transparent: true,
        opacity: 0.4 - i * 0.1
      });
      const ring = new THREE.Mesh(ringGeometry, ringMaterial);
      ring.rotation.x = Math.random() * Math.PI;
      ring.rotation.y = Math.random() * Math.PI;
      orb.add(ring);
    }
  }

  createAmbientEffects() {
    // Floating data particles
    const particleCount = 200;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);

    const goldColor = new THREE.Color(0xf5c542);
    const cyanColor = new THREE.Color(0x00e5ff);

    for (let i = 0; i < particleCount * 3; i += 3) {
      const angle = Math.random() * Math.PI * 2;
      const radius = 2 + Math.random() * 2;
      positions[i] = Math.sin(angle) * radius;
      positions[i + 1] = 0.5 + Math.random() * 2;
      positions[i + 2] = Math.cos(angle) * radius;

      const color = Math.random() > 0.5 ? goldColor : cyanColor;
      colors[i] = color.r;
      colors[i + 1] = color.g;
      colors[i + 2] = color.b;
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    const material = new THREE.PointsMaterial({
      size: 0.03,
      vertexColors: true,
      transparent: true,
      opacity: 0.8
    });

    const particles = new THREE.Points(geometry, material);
    this.scene.add(particles);
    this.objects.push(particles);
    this.dataParticles = particles;
  }

  update(delta) {
    // Rotate AI orb rings
    if (this.aiOrb) {
      this.aiOrb.children.forEach((child, i) => {
        if (child.type === 'Mesh') {
          child.rotation.x += delta * (0.2 + i * 0.1);
          child.rotation.y += delta * (0.1 + i * 0.05);
        }
      });
    }

    // Animate data particles
    if (this.dataParticles) {
      this.dataParticles.rotation.y += delta * 0.05;
    }

    // Pulse panels
    this.panels.forEach((panel, i) => {
      const pulse = Math.sin(Date.now() * 0.002 + i) * 0.02;
      panel.scale.set(1 + pulse, 1 + pulse, 1);
    });
  }

  dispose() {
    this.objects.forEach(obj => {
      this.scene.remove(obj);
      if (obj.geometry) obj.geometry.dispose();
      if (obj.material) obj.material.dispose();
    });
  }
}

