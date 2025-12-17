// ============================================================================
// AVATAR CONTROLLER - 3D Model Loading and Animation
// ============================================================================

class AvatarController {
    constructor() {
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.controls = null;
        this.avatar = null;
        this.mixer = null;
        this.clock = new THREE.Clock();
        
        this.morphTargets = {};
        this.currentAnimation = null;
        this.emotionBlends = {
            calm: { smile: 0, frown: 0, eyebrowUp: 0, eyebrowDown: 0 },
            happy: { smile: 1.0, frown: 0, eyebrowUp: 0.3, eyebrowDown: 0 },
            excited: { smile: 0.9, frown: 0, eyebrowUp: 0.8, eyebrowDown: 0 },
            thinking: { smile: 0.2, frown: 0, eyebrowUp: 0.5, eyebrowDown: 0 },
            concerned: { smile: 0, frown: 0.6, eyebrowUp: 0, eyebrowDown: 0.7 }
        };
    }
    
    async init() {
        // Create scene
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x1a1a2e);
        this.scene.fog = new THREE.Fog(0x1a1a2e, 10, 50);
        
        // Create camera
        this.camera = new THREE.PerspectiveCamera(
            45,
            window.innerWidth / window.innerHeight,
            0.1,
            1000
        );
        this.camera.position.set(0, 1.6, 3);
        
        // Create renderer
        this.renderer = new THREE.WebGLRenderer({
            antialias: true,
            alpha: true,
            powerPreference: 'high-performance'
        });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        this.renderer.outputEncoding = THREE.sRGBEncoding;
        this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
        this.renderer.toneMappingExposure = 1.2;
        
        // Add renderer to DOM
        const container = document.getElementById('canvas-container');
        container.appendChild(this.renderer.domElement);
        
        // Add orbit controls
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.05;
        this.controls.minDistance = 1.5;
        this.controls.maxDistance = 8;
        this.controls.maxPolarAngle = Math.PI / 2;
        this.controls.target.set(0, 1.4, 0);
        
        // Setup lighting
        this.setupLighting();
        
        // Load avatar
        await this.loadAvatar();
        
        // Setup environment
        this.setupEnvironment();
        
        console.log('✅ Avatar Controller initialized');
    }
    
    setupLighting() {
        // Ambient light
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
        this.scene.add(ambientLight);
        
        // Main directional light (key light)
        const keyLight = new THREE.DirectionalLight(0xffffff, 0.8);
        keyLight.position.set(5, 10, 7.5);
        keyLight.castShadow = true;
        keyLight.shadow.mapSize.width = 2048;
        keyLight.shadow.mapSize.height = 2048;
        keyLight.shadow.camera.near = 0.5;
        keyLight.shadow.camera.far = 50;
        keyLight.shadow.camera.left = -10;
        keyLight.shadow.camera.right = 10;
        keyLight.shadow.camera.top = 10;
        keyLight.shadow.camera.bottom = -10;
        this.scene.add(keyLight);
        
        // Fill light
        const fillLight = new THREE.DirectionalLight(0x4facfe, 0.3);
        fillLight.position.set(-5, 5, -5);
        this.scene.add(fillLight);
        
        // Rim light
        const rimLight = new THREE.DirectionalLight(0x00f2fe, 0.4);
        rimLight.position.set(0, 5, -10);
        this.scene.add(rimLight);
        
        // Hemisphere light for natural ambient
        const hemiLight = new THREE.HemisphereLight(0xffffff, 0x444444, 0.3);
        this.scene.add(hemiLight);
    }
    
    async loadAvatar() {
        return new Promise((resolve, reject) => {
            const loader = new THREE.GLTFLoader();
            
            // Try to load avatar.glb - if it doesn't exist, create a placeholder
            loader.load(
                'models/avatar.glb',
                (gltf) => {
                    this.avatar = gltf.scene;
                    this.scene.add(this.avatar);
                    
                    // Configure avatar
                    this.avatar.position.set(0, 0, 0);
                    this.avatar.scale.set(1, 1, 1);
                    
                    // Enable shadows
                    this.avatar.traverse((node) => {
                        if (node.isMesh) {
                            node.castShadow = true;
                            node.receiveShadow = true;
                            
                            // Store morph targets for facial animation
                            if (node.morphTargetDictionary) {
                                this.morphTargets[node.name] = node;
                            }
                        }
                    });
                    
                    // Setup animation mixer
                    if (gltf.animations && gltf.animations.length > 0) {
                        this.mixer = new THREE.AnimationMixer(this.avatar);
                        gltf.animations.forEach((clip) => {
                            const action = this.mixer.clipAction(clip);
                            if (clip.name === 'Idle') {
                                action.play();
                            }
                        });
                    }
                    
                    console.log('✅ Avatar loaded successfully');
                    resolve();
                },
                (progress) => {
                    const percent = (progress.loaded / progress.total * 100).toFixed(0);
                    console.log(`Loading avatar: ${percent}%`);
                },
                (error) => {
                    console.warn('Avatar model not found, creating placeholder...');
                    this.createPlaceholderAvatar();
                    resolve();
                }
            );
        });
    }
    
    createPlaceholderAvatar() {
        // Create a simple humanoid figure as placeholder
        const group = new THREE.Group();
        
        // Head
        const headGeometry = new THREE.SphereGeometry(0.15, 32, 32);
        const headMaterial = new THREE.MeshStandardMaterial({
            color: 0xffdbac,
            roughness: 0.7,
            metalness: 0.1
        });
        const head = new THREE.Mesh(headGeometry, headMaterial);
        head.position.y = 1.6;
        head.castShadow = true;
        group.add(head);
        
        // Body
        const bodyGeometry = new THREE.CylinderGeometry(0.2, 0.25, 0.8, 32);
        const bodyMaterial = new THREE.MeshStandardMaterial({
            color: 0x2c3e50,
            roughness: 0.6,
            metalness: 0.2
        });
        const body = new THREE.Mesh(bodyGeometry, bodyMaterial);
        body.position.y = 1.0;
        body.castShadow = true;
        group.add(body);
        
        // Arms
        const armGeometry = new THREE.CylinderGeometry(0.05, 0.05, 0.6, 16);
        const leftArm = new THREE.Mesh(armGeometry, bodyMaterial);
        leftArm.position.set(-0.3, 1.0, 0);
        leftArm.rotation.z = Math.PI / 6;
        leftArm.castShadow = true;
        group.add(leftArm);
        
        const rightArm = new THREE.Mesh(armGeometry, bodyMaterial);
        rightArm.position.set(0.3, 1.0, 0);
        rightArm.rotation.z = -Math.PI / 6;
        rightArm.castShadow = true;
        group.add(rightArm);
        
        // Legs
        const legGeometry = new THREE.CylinderGeometry(0.08, 0.08, 0.8, 16);
        const leftLeg = new THREE.Mesh(legGeometry, bodyMaterial);
        leftLeg.position.set(-0.1, 0.2, 0);
        leftLeg.castShadow = true;
        group.add(leftLeg);
        
        const rightLeg = new THREE.Mesh(legGeometry, bodyMaterial);
        rightLeg.position.set(0.1, 0.2, 0);
        rightLeg.castShadow = true;
        group.add(rightLeg);
        
        this.avatar = group;
        this.scene.add(this.avatar);
        
        console.log('✅ Placeholder avatar created');
    }
    
    setupEnvironment() {
        // Ground plane
        const groundGeometry = new THREE.PlaneGeometry(20, 20);
        const groundMaterial = new THREE.MeshStandardMaterial({
            color: 0x16213e,
            roughness: 0.8,
            metalness: 0.2
        });
        const ground = new THREE.Mesh(groundGeometry, groundMaterial);
        ground.rotation.x = -Math.PI / 2;
        ground.receiveShadow = true;
        this.scene.add(ground);
        
        // Add some atmospheric particles
        this.addParticles();
    }
    
    addParticles() {
        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 1000;
        const positions = new Float32Array(particlesCount * 3);
        
        for (let i = 0; i < particlesCount * 3; i++) {
            positions[i] = (Math.random() - 0.5) * 20;
        }
        
        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        
        const particlesMaterial = new THREE.PointsMaterial({
            color: 0x4facfe,
            size: 0.02,
            transparent: true,
            opacity: 0.6,
            blending: THREE.AdditiveBlending
        });
        
        const particles = new THREE.Points(particlesGeometry, particlesMaterial);
        this.scene.add(particles);
        
        // Animate particles
        const animateParticles = () => {
            const positions = particles.geometry.attributes.position.array;
            for (let i = 1; i < positions.length; i += 3) {
                positions[i] += 0.001;
                if (positions[i] > 10) positions[i] = -10;
            }
            particles.geometry.attributes.position.needsUpdate = true;
            requestAnimationFrame(animateParticles);
        };
        animateParticles();
    }
    
    setEmotion(emotion) {
        const blends = this.emotionBlends[emotion];
        if (!blends) return;
        
        // Apply blend shapes to all mesh objects with morph targets
        Object.values(this.morphTargets).forEach((mesh) => {
            if (!mesh.morphTargetInfluences) return;
            
            const dict = mesh.morphTargetDictionary;
            
            // Smoothly transition to target values
            Object.keys(blends).forEach((key) => {
                if (dict[key] !== undefined) {
                    const targetValue = blends[key];
                    const currentValue = mesh.morphTargetInfluences[dict[key]];
                    mesh.morphTargetInfluences[dict[key]] = THREE.MathUtils.lerp(
                        currentValue,
                        targetValue,
                        0.1
                    );
                }
            });
        });
    }
    
    applyBlendShape(shapeName, value) {
        Object.values(this.morphTargets).forEach((mesh) => {
            if (!mesh.morphTargetInfluences || !mesh.morphTargetDictionary) return;
            
            const index = mesh.morphTargetDictionary[shapeName];
            if (index !== undefined) {
                mesh.morphTargetInfluences[index] = value;
            }
        });
    }
    
    resetBlendShapes() {
        Object.values(this.morphTargets).forEach((mesh) => {
            if (mesh.morphTargetInfluences) {
                mesh.morphTargetInfluences.fill(0);
            }
        });
    }
    
    update() {
        const delta = this.clock.getDelta();
        
        // Update animation mixer
        if (this.mixer) {
            this.mixer.update(delta);
        }
        
        // Update controls
        if (this.controls) {
            this.controls.update();
        }
        
        // Idle breathing animation
        if (this.avatar) {
            const time = this.clock.getElapsedTime();
            this.avatar.position.y = Math.sin(time * 2) * 0.01;
        }
    }
    
    render() {
        this.renderer.render(this.scene, this.camera);
    }
    
    handleResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
    
    getScene() {
        return this.scene;
    }
    
    getCamera() {
        return this.camera;
    }
    
    getRenderer() {
        return this.renderer;
    }
}
