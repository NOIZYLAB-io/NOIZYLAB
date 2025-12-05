import * as THREE from 'three';
import { VRButton } from 'three/examples/jsm/webxr/VRButton.js';
import { XRControllerModelFactory } from 'three/examples/jsm/webxr/XRControllerModelFactory.js';

export class NoizyVerseEngine {
  constructor(container) {
    this.container = container;
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    this.controllers = [];
    this.isVR = false;
    
    this.init();
  }

  init() {
    // Renderer setup
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.setPixelRatio(window.devicePixelRatio);
    this.renderer.xr.enabled = true;
    this.container.appendChild(this.renderer.domElement);
    
    // VR Button
    this.container.appendChild(VRButton.createButton(this.renderer));
    
    // Scene background - deep space black with gold accent lighting
    this.scene.background = new THREE.Color(0x000000);
    
    // Ambient light
    const ambient = new THREE.AmbientLight(0xffffff, 0.3);
    this.scene.add(ambient);
    
    // Gold accent light
    const goldLight = new THREE.PointLight(0xf5c542, 1, 100);
    goldLight.position.set(0, 5, 0);
    this.scene.add(goldLight);
    
    // Camera position
    this.camera.position.set(0, 1.6, 3);
    
    // Controllers
    this.setupControllers();
    
    // Handle resize
    window.addEventListener('resize', () => this.onResize());
    
    // Start render loop
    this.renderer.setAnimationLoop(() => this.render());
  }

  setupControllers() {
    const controllerModelFactory = new XRControllerModelFactory();
    
    for (let i = 0; i < 2; i++) {
      const controller = this.renderer.xr.getController(i);
      controller.addEventListener('selectstart', () => this.onSelect(i));
      this.scene.add(controller);
      
      const grip = this.renderer.xr.getControllerGrip(i);
      grip.add(controllerModelFactory.createControllerModel(grip));
      this.scene.add(grip);
      
      this.controllers.push({ controller, grip });
    }
  }

  onSelect(controllerIndex) {
    console.log(`Controller ${controllerIndex} selected`);
    // Emit event for UI interaction
    window.dispatchEvent(new CustomEvent('noizyverse-select', { 
      detail: { controller: controllerIndex } 
    }));
  }

  onResize() {
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  }

  addToScene(object) {
    this.scene.add(object);
  }

  removeFromScene(object) {
    this.scene.remove(object);
  }

  render() {
    this.renderer.render(this.scene, this.camera);
  }

  dispose() {
    this.renderer.dispose();
    this.container.removeChild(this.renderer.domElement);
  }
}

export function createEngine(container) {
  return new NoizyVerseEngine(container);
}

