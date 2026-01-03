// ============================================================================
// WEBXR CONTROLLER - VR/AR Support
// ============================================================================

class WebXRController {
    constructor(avatar) {
        this.avatar = avatar;
        this.isVRSupported = false;
        this.session = null;
        this.referenceSpace = null;
        
        // VR Controllers
        this.controller1 = null;
        this.controller2 = null;
        this.controllerGrip1 = null;
        this.controllerGrip2 = null;
        
        this.init();
    }
    
    init() {
        // Check WebXR support
        if ('xr' in navigator) {
            navigator.xr.isSessionSupported('immersive-vr').then((supported) => {
                this.isVRSupported = supported;
                
                if (supported) {
                    console.log('✅ WebXR VR supported');
                    this.setupVRButton();
                } else {
                    console.log('⚠️ WebXR VR not supported');
                    document.getElementById('vr-btn').style.display = 'none';
                }
            });
        } else {
            console.log('⚠️ WebXR not available');
            document.getElementById('vr-btn').style.display = 'none';
        }
    }
    
    setupVRButton() {
        const vrButton = document.getElementById('vr-btn');
        
        vrButton.addEventListener('click', () => {
            if (!this.session) {
                this.enterVR();
            } else {
                this.exitVR();
            }
        });
    }
    
    async enterVR() {
        if (!this.isVRSupported) {
            alert('VR not supported on this device');
            return;
        }
        
        try {
            // Request VR session
            this.session = await navigator.xr.requestSession('immersive-vr', {
                optionalFeatures: ['local-floor', 'bounded-floor', 'hand-tracking']
            });
            
            console.log('✅ VR session started');
            
            // Setup session
            await this.onSessionStarted(this.session);
            
            // Update UI
            document.getElementById('vr-btn').textContent = '🥽 Exit VR';
            
        } catch (error) {
            console.error('Failed to enter VR:', error);
            alert('Failed to start VR session: ' + error.message);
        }
    }
    
    async onSessionStarted(session) {
        this.session = session;
        
        // Handle session end
        session.addEventListener('end', () => {
            this.onSessionEnded();
        });
        
        // Get renderer from avatar
        const renderer = this.avatar.getRenderer();
        
        // Enable XR on renderer
        renderer.xr.enabled = true;
        renderer.xr.setSession(session);
        
        // Get reference space
        this.referenceSpace = await session.requestReferenceSpace('local-floor');
        
        // Setup VR controllers
        this.setupControllers(renderer);
        
        // Update camera for VR
        this.avatar.getCamera().position.set(0, 1.6, 3);
        
        console.log('✅ VR session configured');
    }
    
    setupControllers(renderer) {
        const scene = this.avatar.getScene();
        
        // Controller 1
        this.controller1 = renderer.xr.getController(0);
        this.controller1.addEventListener('selectstart', this.onSelectStart.bind(this));
        this.controller1.addEventListener('selectend', this.onSelectEnd.bind(this));
        scene.add(this.controller1);
        
        // Controller 2
        this.controller2 = renderer.xr.getController(1);
        this.controller2.addEventListener('selectstart', this.onSelectStart.bind(this));
        this.controller2.addEventListener('selectend', this.onSelectEnd.bind(this));
        scene.add(this.controller2);
        
        // Controller grips (for showing controller models)
        this.controllerGrip1 = renderer.xr.getControllerGrip(0);
        this.addControllerModel(this.controllerGrip1);
        scene.add(this.controllerGrip1);
        
        this.controllerGrip2 = renderer.xr.getControllerGrip(1);
        this.addControllerModel(this.controllerGrip2);
        scene.add(this.controllerGrip2);
        
        // Add ray visualizers
        this.addControllerRay(this.controller1);
        this.addControllerRay(this.controller2);
    }
    
    addControllerModel(grip) {
        // Add simple controller representation
        const geometry = new THREE.BoxGeometry(0.05, 0.05, 0.2);
        const material = new THREE.MeshStandardMaterial({ 
            color: 0x4facfe,
            emissive: 0x4facfe,
            emissiveIntensity: 0.5
        });
        const controller = new THREE.Mesh(geometry, material);
        grip.add(controller);
    }
    
    addControllerRay(controller) {
        // Add ray pointer
        const geometry = new THREE.BufferGeometry();
        geometry.setAttribute('position', new THREE.Float32BufferAttribute([0, 0, 0, 0, 0, -1], 3));
        
        const material = new THREE.LineBasicMaterial({
            color: 0x4facfe,
            linewidth: 2
        });
        
        const line = new THREE.Line(geometry, material);
        line.scale.z = 5;
        controller.add(line);
    }
    
    onSelectStart(event) {
        console.log('Controller select start');
        
        // Highlight controller
        const controller = event.target;
        controller.children[0].scale.z = 10;
        
        // Trigger interaction with avatar
        this.interactWithAvatar(controller);
    }
    
    onSelectEnd(event) {
        console.log('Controller select end');
        
        // Reset controller
        const controller = event.target;
        controller.children[0].scale.z = 5;
    }
    
    interactWithAvatar(controller) {
        // Raycast from controller to avatar
        const raycaster = new THREE.Raycaster();
        const tempMatrix = new THREE.Matrix4();
        
        tempMatrix.identity().extractRotation(controller.matrixWorld);
        
        raycaster.ray.origin.setFromMatrixPosition(controller.matrixWorld);
        raycaster.ray.direction.set(0, 0, -1).applyMatrix4(tempMatrix);
        
        if (this.avatar && this.avatar.avatar) {
            const intersects = raycaster.intersectObject(this.avatar.avatar, true);
            
            if (intersects.length > 0) {
                console.log('Avatar interaction!');
                
                // Trigger avatar response
                if (window.gabrielApp) {
                    window.gabrielApp.speak("You've touched me in VR! This is quite immersive.");
                }
            }
        }
    }
    
    exitVR() {
        if (this.session) {
            this.session.end();
        }
    }
    
    onSessionEnded() {
        this.session = null;
        
        // Reset renderer
        const renderer = this.avatar.getRenderer();
        renderer.xr.enabled = false;
        
        // Update UI
        document.getElementById('vr-btn').textContent = '🥽 Enter VR';
        
        console.log('✅ VR session ended');
    }
    
    // Hand tracking support (experimental)
    async enableHandTracking() {
        if (!this.session) return;
        
        try {
            const inputSources = this.session.inputSources;
            
            for (const inputSource of inputSources) {
                if (inputSource.hand) {
                    console.log('Hand tracking available');
                    this.setupHandTracking(inputSource);
                }
            }
        } catch (error) {
            console.error('Hand tracking error:', error);
        }
    }
    
    setupHandTracking(inputSource) {
        // Setup hand tracking visualization
        const hand = inputSource.hand;
        
        // Create joint spheres
        const joints = [];
        
        for (const joint of hand.values()) {
            const geometry = new THREE.SphereGeometry(0.01);
            const material = new THREE.MeshBasicMaterial({ color: 0x00f2fe });
            const sphere = new THREE.Mesh(geometry, material);
            
            this.avatar.getScene().add(sphere);
            joints.push({ joint, sphere });
        }
        
        // Update joint positions in animation loop
        const updateHands = () => {
            if (!this.session) return;
            
            joints.forEach(({ joint, sphere }) => {
                const pose = joint.getPose(this.referenceSpace);
                if (pose) {
                    sphere.position.copy(pose.transform.position);
                    sphere.quaternion.copy(pose.transform.orientation);
                }
            });
            
            requestAnimationFrame(updateHands);
        };
        
        updateHands();
    }
    
    // AR mode (experimental)
    async enterAR() {
        try {
            const session = await navigator.xr.requestSession('immersive-ar', {
                requiredFeatures: ['hit-test'],
                optionalFeatures: ['dom-overlay'],
                domOverlay: { root: document.body }
            });
            
            console.log('✅ AR session started');
            await this.onSessionStarted(session);
            
        } catch (error) {
            console.error('Failed to enter AR:', error);
            alert('AR not supported on this device');
        }
    }
}
