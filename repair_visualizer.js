import * as THREE from 'three';

/**
 * VR Repair Visualizer
 * Shows 3D representations of device components and issues
 */

export class RepairVisualizer {
  constructor(scene) {
    this.scene = scene;
    this.components = new Map();
    this.issues = [];
    this.group = new THREE.Group();
    this.scene.add(this.group);
  }

  /**
   * Create a 3D device model
   */
  createDevice(type = 'laptop') {
    const device = new THREE.Group();

    if (type === 'laptop') {
      // Base
      const baseGeometry = new THREE.BoxGeometry(0.35, 0.02, 0.25);
      const baseMaterial = new THREE.MeshStandardMaterial({
        color: 0x2a2a2a,
        roughness: 0.3,
        metalness: 0.7
      });
      const base = new THREE.Mesh(baseGeometry, baseMaterial);
      device.add(base);

      // Screen
      const screenGeometry = new THREE.BoxGeometry(0.34, 0.22, 0.01);
      const screenMaterial = new THREE.MeshStandardMaterial({
        color: 0x1a1a1a,
        roughness: 0.1,
        metalness: 0.5
      });
      const screen = new THREE.Mesh(screenGeometry, screenMaterial);
      screen.position.set(0, 0.12, -0.12);
      screen.rotation.x = -0.3;
      device.add(screen);

      // Screen display
      const displayGeometry = new THREE.PlaneGeometry(0.3, 0.18);
      const displayMaterial = new THREE.MeshBasicMaterial({
        color: 0x111111
      });
      const display = new THREE.Mesh(displayGeometry, displayMaterial);
      display.position.set(0, 0.12, -0.115);
      display.rotation.x = -0.3;
      device.add(display);
      this.display = display;

      // Add internal components (visible in exploded view)
      this.addComponent(device, 'cpu', [0, 0.02, 0], 0xff6b6b);
      this.addComponent(device, 'ram', [0.08, 0.02, 0], 0x4ecdc4);
      this.addComponent(device, 'ssd', [-0.08, 0.02, 0], 0x45b7d1);
      this.addComponent(device, 'fan', [0.12, 0.02, 0.05], 0xf7dc6f);
      this.addComponent(device, 'battery', [0, 0.02, 0.08], 0x82e0aa);
    }

    device.position.set(0, 1, 0);
    this.group.add(device);
    this.device = device;

    return device;
  }

  addComponent(parent, name, position, color) {
    const geometry = new THREE.BoxGeometry(0.04, 0.01, 0.03);
    const material = new THREE.MeshStandardMaterial({
      color: color,
      roughness: 0.5,
      metalness: 0.3,
      transparent: true,
      opacity: 0.8
    });
    const component = new THREE.Mesh(geometry, material);
    component.position.set(...position);
    component.userData = { name, originalPosition: [...position] };
    parent.add(component);
    this.components.set(name, component);
  }

  /**
   * Highlight a component with an issue
   */
  highlightIssue(componentName, severity = 'warning') {
    const component = this.components.get(componentName);
    if (!component) return;

    const colors = {
      critical: 0xff0000,
      warning: 0xffaa00,
      info: 0x00aaff
    };

    // Create pulsing ring around component
    const ringGeometry = new THREE.TorusGeometry(0.04, 0.005, 8, 32);
    const ringMaterial = new THREE.MeshBasicMaterial({
      color: colors[severity] || colors.warning,
      transparent: true,
      opacity: 0.8
    });
    const ring = new THREE.Mesh(ringGeometry, ringMaterial);
    ring.rotation.x = Math.PI / 2;
    ring.position.copy(component.position);
    ring.position.y += 0.02;
    
    this.device.add(ring);
    this.issues.push({ component: componentName, ring, severity });

    // Animate ring
    const animate = () => {
      ring.scale.x = 1 + Math.sin(Date.now() * 0.005) * 0.2;
      ring.scale.y = 1 + Math.sin(Date.now() * 0.005) * 0.2;
      ring.material.opacity = 0.5 + Math.sin(Date.now() * 0.005) * 0.3;
    };

    return { ring, animate };
  }

  /**
   * Exploded view - separate components for inspection
   */
  explodedView(expand = true) {
    const offset = expand ? 0.15 : 0;
    
    this.components.forEach((component, name) => {
      const original = component.userData.originalPosition;
      const direction = new THREE.Vector3(
        original[0] * 2,
        expand ? 0.1 : 0,
        original[2] * 2
      ).normalize();

      const target = expand
        ? new THREE.Vector3(
            original[0] + direction.x * offset,
            original[1] + offset,
            original[2] + direction.z * offset
          )
        : new THREE.Vector3(...original);

      // Animate to position
      this.animateComponent(component, target);
    });
  }

  animateComponent(component, target) {
    const start = component.position.clone();
    const duration = 500;
    const startTime = Date.now();

    const animate = () => {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease out cubic

      component.position.lerpVectors(start, target, eased);

      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    };

    animate();
  }

  /**
   * Show repair step visualization
   */
  showRepairStep(step) {
    const steps = {
      'remove_battery': () => {
        const battery = this.components.get('battery');
        if (battery) {
          this.animateComponent(battery, new THREE.Vector3(0, 1.3, 0.3));
        }
      },
      'replace_ram': () => {
        const ram = this.components.get('ram');
        if (ram) {
          // Fade out old RAM
          ram.material.opacity = 0.3;
          // Show new RAM coming in
          this.showNewComponent('ram', [0.08, 1.3, -0.2], [0.08, 0.02, 0]);
        }
      },
      'clean_fan': () => {
        const fan = this.components.get('fan');
        if (fan) {
          // Spin animation
          const spin = () => {
            fan.rotation.y += 0.1;
            if (fan.rotation.y < Math.PI * 4) {
              requestAnimationFrame(spin);
            }
          };
          spin();
        }
      }
    };

    if (steps[step]) {
      steps[step]();
    }
  }

  showNewComponent(name, startPos, endPos) {
    const geometry = new THREE.BoxGeometry(0.04, 0.01, 0.03);
    const material = new THREE.MeshStandardMaterial({
      color: 0x00ff00,
      roughness: 0.5,
      metalness: 0.3,
      transparent: true,
      opacity: 0.8
    });
    const newComponent = new THREE.Mesh(geometry, material);
    newComponent.position.set(...startPos);
    this.device.add(newComponent);

    this.animateComponent(newComponent, new THREE.Vector3(...endPos));
  }

  /**
   * Show diagnostic scan effect
   */
  scanEffect() {
    const scanGeometry = new THREE.PlaneGeometry(0.5, 0.01);
    const scanMaterial = new THREE.MeshBasicMaterial({
      color: 0x00ff00,
      transparent: true,
      opacity: 0.5
    });
    const scanLine = new THREE.Mesh(scanGeometry, scanMaterial);
    scanLine.rotation.x = -Math.PI / 2;
    scanLine.position.set(0, 1.15, 0);
    this.group.add(scanLine);

    // Animate scan
    let scanY = 1.15;
    const animate = () => {
      scanY -= 0.005;
      scanLine.position.y = scanY;
      
      if (scanY > 0.85) {
        requestAnimationFrame(animate);
      } else {
        this.group.remove(scanLine);
        scanLine.geometry.dispose();
        scanLine.material.dispose();
      }
    };
    animate();
  }

  update(delta) {
    // Update issue animations
    this.issues.forEach(issue => {
      if (issue.animate) issue.animate();
    });
  }

  dispose() {
    this.scene.remove(this.group);
    this.group.traverse(obj => {
      if (obj.geometry) obj.geometry.dispose();
      if (obj.material) obj.material.dispose();
    });
  }
}

