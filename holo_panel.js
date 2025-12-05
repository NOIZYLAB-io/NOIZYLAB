import * as THREE from 'three';

/**
 * Holographic Panel System
 * Floating 3D UI panels for VR/AR
 */

export class HoloPanel {
  constructor(options = {}) {
    this.width = options.width || 1;
    this.height = options.height || 0.6;
    this.title = options.title || 'Panel';
    this.color = options.color || 0xf5c542;
    this.interactive = options.interactive !== false;
    
    this.group = new THREE.Group();
    this.isHovered = false;
    this.isSelected = false;
    
    this.build();
  }

  build() {
    // Background plane
    const bgGeometry = new THREE.PlaneGeometry(this.width, this.height);
    const bgMaterial = new THREE.MeshBasicMaterial({
      color: 0x000000,
      transparent: true,
      opacity: 0.85,
      side: THREE.DoubleSide
    });
    this.background = new THREE.Mesh(bgGeometry, bgMaterial);
    this.group.add(this.background);

    // Border frame
    this.createBorder();

    // Title bar
    this.createTitleBar();

    // Corner accents
    this.createCorners();

    // Glow effect (for hover)
    this.createGlow();
  }

  createBorder() {
    const shape = new THREE.Shape();
    const w = this.width / 2;
    const h = this.height / 2;
    
    shape.moveTo(-w, -h);
    shape.lineTo(w, -h);
    shape.lineTo(w, h);
    shape.lineTo(-w, h);
    shape.lineTo(-w, -h);

    const points = shape.getPoints();
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    
    const material = new THREE.LineBasicMaterial({
      color: this.color,
      linewidth: 2
    });
    
    this.border = new THREE.Line(geometry, material);
    this.border.position.z = 0.001;
    this.group.add(this.border);
  }

  createTitleBar() {
    const barGeometry = new THREE.PlaneGeometry(this.width, 0.06);
    const barMaterial = new THREE.MeshBasicMaterial({
      color: this.color,
      transparent: true,
      opacity: 0.3
    });
    this.titleBar = new THREE.Mesh(barGeometry, barMaterial);
    this.titleBar.position.y = this.height / 2 - 0.03;
    this.titleBar.position.z = 0.002;
    this.group.add(this.titleBar);
  }

  createCorners() {
    const cornerSize = 0.05;
    const cornerGeometry = new THREE.PlaneGeometry(cornerSize, cornerSize);
    const cornerMaterial = new THREE.MeshBasicMaterial({
      color: this.color
    });

    const positions = [
      [-this.width / 2 + cornerSize / 2, this.height / 2 - cornerSize / 2],
      [this.width / 2 - cornerSize / 2, this.height / 2 - cornerSize / 2],
      [-this.width / 2 + cornerSize / 2, -this.height / 2 + cornerSize / 2],
      [this.width / 2 - cornerSize / 2, -this.height / 2 + cornerSize / 2]
    ];

    this.corners = positions.map(pos => {
      const corner = new THREE.Mesh(cornerGeometry, cornerMaterial);
      corner.position.set(pos[0], pos[1], 0.003);
      this.group.add(corner);
      return corner;
    });
  }

  createGlow() {
    const glowGeometry = new THREE.PlaneGeometry(this.width + 0.1, this.height + 0.1);
    const glowMaterial = new THREE.MeshBasicMaterial({
      color: this.color,
      transparent: true,
      opacity: 0
    });
    this.glow = new THREE.Mesh(glowGeometry, glowMaterial);
    this.glow.position.z = -0.01;
    this.group.add(this.glow);
  }

  setHovered(hovered) {
    this.isHovered = hovered;
    this.glow.material.opacity = hovered ? 0.15 : 0;
    
    const scale = hovered ? 1.02 : 1;
    this.group.scale.set(scale, scale, scale);
  }

  setSelected(selected) {
    this.isSelected = selected;
    this.border.material.color.setHex(selected ? 0xffffff : this.color);
  }

  setContent(content) {
    // In a real implementation, this would render text/graphics
    // For now, store content data
    this.content = content;
  }

  update(delta) {
    // Subtle floating animation
    this.group.position.y += Math.sin(Date.now() * 0.002) * 0.0002;
    
    // Corner pulse when hovered
    if (this.isHovered) {
      const pulse = 0.8 + Math.sin(Date.now() * 0.005) * 0.2;
      this.corners.forEach(c => c.material.opacity = pulse);
    }
  }

  getObject() {
    return this.group;
  }

  dispose() {
    this.group.traverse(obj => {
      if (obj.geometry) obj.geometry.dispose();
      if (obj.material) obj.material.dispose();
    });
  }
}

/**
 * Panel Manager - handles multiple panels
 */
export class HoloPanelManager {
  constructor(scene) {
    this.scene = scene;
    this.panels = new Map();
  }

  createPanel(id, options) {
    const panel = new HoloPanel(options);
    this.panels.set(id, panel);
    this.scene.add(panel.getObject());
    return panel;
  }

  getPanel(id) {
    return this.panels.get(id);
  }

  removePanel(id) {
    const panel = this.panels.get(id);
    if (panel) {
      this.scene.remove(panel.getObject());
      panel.dispose();
      this.panels.delete(id);
    }
  }

  update(delta) {
    this.panels.forEach(panel => panel.update(delta));
  }

  dispose() {
    this.panels.forEach(panel => {
      this.scene.remove(panel.getObject());
      panel.dispose();
    });
    this.panels.clear();
  }
}

