import * as THREE from 'three';

/**
 * NoizyVerse Repair Room
 * A 3D environment for visualizing device repairs
 */

export class RepairRoom {
  constructor(scene) {
    this.scene = scene;
    this.objects = [];
    this.device = null;
    this.diagnosticPanels = [];
  }

  build() {
    // Floor - carbon fiber texture
    const floorGeometry = new THREE.PlaneGeometry(20, 20);
    const floorMaterial = new THREE.MeshStandardMaterial({
      color: 0x111111,
      roughness: 0.8,
      metalness: 0.2
    });
    const floor = new THREE.Mesh(floorGeometry, floorMaterial);
    floor.rotation.x = -Math.PI / 2;
    floor.receiveShadow = true;
    this.scene.add(floor);
    this.objects.push(floor);

    // Grid overlay
    const gridHelper = new THREE.GridHelper(20, 40, 0xf5c542, 0x333333);
    gridHelper.position.y = 0.01;
    this.scene.add(gridHelper);
    this.objects.push(gridHelper);

    // Workbench
    this.createWorkbench();

    // Ambient particles (gold dust effect)
    this.createParticles();

    // Holographic ring
    this.createHoloRing();
  }

  createWorkbench() {
    const benchGeometry = new THREE.BoxGeometry(2, 0.1, 1);
    const benchMaterial = new THREE.MeshStandardMaterial({
      color: 0x1a1a1a,
      roughness: 0.3,
      metalness: 0.7
    });
    const bench = new THREE.Mesh(benchGeometry, benchMaterial);
    bench.position.set(0, 0.9, 0);
    bench.castShadow = true;
    this.scene.add(bench);
    this.objects.push(bench);

    // Bench legs
    const legGeometry = new THREE.CylinderGeometry(0.05, 0.05, 0.9);
    const legMaterial = new THREE.MeshStandardMaterial({ color: 0x333333 });
    const legPositions = [
      [-0.9, 0.45, -0.4],
      [0.9, 0.45, -0.4],
      [-0.9, 0.45, 0.4],
      [0.9, 0.45, 0.4]
    ];

    legPositions.forEach(pos => {
      const leg = new THREE.Mesh(legGeometry, legMaterial);
      leg.position.set(...pos);
      this.scene.add(leg);
      this.objects.push(leg);
    });
  }

  createParticles() {
    const particleCount = 500;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 20;
      positions[i + 1] = Math.random() * 5;
      positions[i + 2] = (Math.random() - 0.5) * 20;
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const material = new THREE.PointsMaterial({
      color: 0xf5c542,
      size: 0.02,
      transparent: true,
      opacity: 0.6
    });

    const particles = new THREE.Points(geometry, material);
    this.scene.add(particles);
    this.objects.push(particles);
    this.particles = particles;
  }

  createHoloRing() {
    const ringGeometry = new THREE.TorusGeometry(1.5, 0.02, 16, 100);
    const ringMaterial = new THREE.MeshBasicMaterial({
      color: 0xf5c542,
      transparent: true,
      opacity: 0.5
    });
    const ring = new THREE.Mesh(ringGeometry, ringMaterial);
    ring.position.set(0, 1.5, 0);
    ring.rotation.x = Math.PI / 2;
    this.scene.add(ring);
    this.objects.push(ring);
    this.holoRing = ring;
  }

  placeDevice(deviceType = 'laptop') {
    // Remove existing device
    if (this.device) {
      this.scene.remove(this.device);
    }

    let geometry;
    if (deviceType === 'laptop') {
      geometry = new THREE.BoxGeometry(0.6, 0.02, 0.4);
    } else if (deviceType === 'desktop') {
      geometry = new THREE.BoxGeometry(0.4, 0.5, 0.4);
    } else if (deviceType === 'phone') {
      geometry = new THREE.BoxGeometry(0.08, 0.16, 0.01);
    }

    const material = new THREE.MeshStandardMaterial({
      color: 0x2a2a2a,
      roughness: 0.2,
      metalness: 0.8
    });

    this.device = new THREE.Mesh(geometry, material);
    this.device.position.set(0, 1, 0);
    this.scene.add(this.device);
  }

  highlightComponent(componentName, color = 0xff0000) {
    // Create a glowing highlight around a component
    const highlightGeometry = new THREE.SphereGeometry(0.1);
    const highlightMaterial = new THREE.MeshBasicMaterial({
      color: color,
      transparent: true,
      opacity: 0.5
    });
    const highlight = new THREE.Mesh(highlightGeometry, highlightMaterial);
    
    // Position based on component
    const positions = {
      'cpu': [0, 1.05, 0],
      'ram': [0.1, 1.05, 0],
      'ssd': [-0.1, 1.05, 0],
      'fan': [0.2, 1.05, 0]
    };

    const pos = positions[componentName] || [0, 1.1, 0];
    highlight.position.set(...pos);
    this.scene.add(highlight);
    
    return highlight;
  }

  update(delta) {
    // Animate particles
    if (this.particles) {
      this.particles.rotation.y += delta * 0.05;
    }

    // Animate holo ring
    if (this.holoRing) {
      this.holoRing.rotation.z += delta * 0.2;
    }
  }

  dispose() {
    this.objects.forEach(obj => {
      this.scene.remove(obj);
      if (obj.geometry) obj.geometry.dispose();
      if (obj.material) obj.material.dispose();
    });
  }
}

