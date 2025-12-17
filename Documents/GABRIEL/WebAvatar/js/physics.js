// ============================================================================
// PHYSICS ENGINE - Hair and Cloth Dynamics Simulation
// ============================================================================

class PhysicsEngine {
    constructor(avatar) {
        this.avatar = avatar;
        this.isInitialized = false;
        
        // Physics simulation parameters
        this.gravity = new THREE.Vector3(0, -9.81, 0);
        this.windForce = new THREE.Vector3(0, 0, 0);
        this.damping = 0.98;
        
        // Physics objects
        this.hairParticles = [];
        this.clothVertices = [];
        this.constraints = [];
        
        // Simulation state
        this.timeStep = 1 / 60;
        this.substeps = 3;
    }
    
    async init() {
        // Initialize physics simulation for hair and cloth
        if (this.avatar && this.avatar.avatar) {
            this.setupHairPhysics();
            this.setupClothPhysics();
        }
        
        this.isInitialized = true;
        console.log('✅ Physics Engine initialized');
    }
    
    setupHairPhysics() {
        // Create particle system for hair simulation
        // Each hair strand is represented as a chain of particles
        
        const hairCount = 50; // Number of hair strands
        const particlesPerStrand = 8;
        
        for (let i = 0; i < hairCount; i++) {
            const strand = [];
            
            // Position hair strands around head
            const angle = (i / hairCount) * Math.PI * 2;
            const radius = 0.15;
            const startX = Math.cos(angle) * radius;
            const startZ = Math.sin(angle) * radius;
            const startY = 1.75; // Head height
            
            // Create particles for this strand
            for (let j = 0; j < particlesPerStrand; j++) {
                const particle = {
                    position: new THREE.Vector3(
                        startX,
                        startY - (j * 0.05),
                        startZ
                    ),
                    previousPosition: new THREE.Vector3(
                        startX,
                        startY - (j * 0.05),
                        startZ
                    ),
                    velocity: new THREE.Vector3(0, 0, 0),
                    mass: 0.01,
                    fixed: j === 0 // First particle is fixed to head
                };
                
                strand.push(particle);
            }
            
            this.hairParticles.push(strand);
            
            // Create constraints between particles in strand
            for (let j = 0; j < particlesPerStrand - 1; j++) {
                this.constraints.push({
                    particleA: strand[j],
                    particleB: strand[j + 1],
                    restLength: 0.05
                });
            }
        }
    }
    
    setupClothPhysics() {
        // Create grid of particles for cloth simulation (e.g., coat, cape)
        // This is a simplified version - production would use more sophisticated cloth sim
        
        const clothWidth = 10;
        const clothHeight = 10;
        const spacing = 0.05;
        
        // Create cloth vertices
        for (let y = 0; y < clothHeight; y++) {
            for (let x = 0; x < clothWidth; x++) {
                const particle = {
                    position: new THREE.Vector3(
                        (x - clothWidth / 2) * spacing,
                        1.4 - y * spacing,
                        0
                    ),
                    previousPosition: new THREE.Vector3(
                        (x - clothWidth / 2) * spacing,
                        1.4 - y * spacing,
                        0
                    ),
                    velocity: new THREE.Vector3(0, 0, 0),
                    mass: 0.02,
                    fixed: y === 0 // Top row is fixed
                };
                
                this.clothVertices.push(particle);
                
                // Create structural constraints
                if (x > 0) {
                    // Horizontal constraint
                    this.constraints.push({
                        particleA: this.clothVertices[this.clothVertices.length - 1],
                        particleB: this.clothVertices[this.clothVertices.length - 2],
                        restLength: spacing
                    });
                }
                
                if (y > 0) {
                    // Vertical constraint
                    const previousRowIndex = (y - 1) * clothWidth + x;
                    this.constraints.push({
                        particleA: this.clothVertices[this.clothVertices.length - 1],
                        particleB: this.clothVertices[previousRowIndex],
                        restLength: spacing
                    });
                }
            }
        }
    }
    
    update() {
        if (!this.isInitialized) return;
        
        // Update wind force (subtle variation)
        const time = Date.now() * 0.001;
        this.windForce.set(
            Math.sin(time * 0.5) * 0.5,
            0,
            Math.cos(time * 0.3) * 0.3
        );
        
        // Run simulation substeps for stability
        for (let i = 0; i < this.substeps; i++) {
            this.simulateStep(this.timeStep / this.substeps);
        }
        
        // Update visual representation
        this.updateVisuals();
    }
    
    simulateStep(dt) {
        // Integrate forces (Verlet integration)
        this.integrateParticles(dt);
        
        // Satisfy constraints
        for (let i = 0; i < 3; i++) { // Multiple iterations for stability
            this.satisfyConstraints();
        }
    }
    
    integrateParticles(dt) {
        // Update all hair particles
        this.hairParticles.forEach(strand => {
            strand.forEach(particle => {
                if (particle.fixed) return;
                
                // Calculate forces
                const force = new THREE.Vector3();
                force.add(this.gravity.clone().multiplyScalar(particle.mass));
                force.add(this.windForce);
                
                // Verlet integration
                const acceleration = force.divideScalar(particle.mass);
                const temp = particle.position.clone();
                
                particle.position
                    .sub(particle.previousPosition)
                    .multiplyScalar(this.damping)
                    .add(acceleration.multiplyScalar(dt * dt))
                    .add(particle.position);
                
                particle.previousPosition.copy(temp);
            });
        });
        
        // Update cloth particles
        this.clothVertices.forEach(particle => {
            if (particle.fixed) return;
            
            const force = new THREE.Vector3();
            force.add(this.gravity.clone().multiplyScalar(particle.mass));
            force.add(this.windForce);
            
            const acceleration = force.divideScalar(particle.mass);
            const temp = particle.position.clone();
            
            particle.position
                .sub(particle.previousPosition)
                .multiplyScalar(this.damping)
                .add(acceleration.multiplyScalar(dt * dt))
                .add(particle.position);
            
            particle.previousPosition.copy(temp);
        });
    }
    
    satisfyConstraints() {
        // Enforce distance constraints
        this.constraints.forEach(constraint => {
            const delta = new THREE.Vector3();
            delta.subVectors(constraint.particleB.position, constraint.particleA.position);
            
            const currentLength = delta.length();
            if (currentLength === 0) return;
            
            const diff = (currentLength - constraint.restLength) / currentLength;
            const correction = delta.multiplyScalar(diff * 0.5);
            
            if (!constraint.particleA.fixed) {
                constraint.particleA.position.add(correction);
            }
            
            if (!constraint.particleB.fixed) {
                constraint.particleB.position.sub(correction);
            }
        });
    }
    
    updateVisuals() {
        // Update Three.js meshes to match physics simulation
        // This would modify the actual avatar geometry in production
        
        // For now, we can visualize with debug lines
        if (window.DEBUG_PHYSICS) {
            this.debugDraw();
        }
    }
    
    debugDraw() {
        // Draw hair strands as lines for debugging
        this.hairParticles.forEach(strand => {
            const points = strand.map(p => p.position);
            const geometry = new THREE.BufferGeometry().setFromPoints(points);
            const material = new THREE.LineBasicMaterial({ color: 0x888888 });
            const line = new THREE.Line(geometry, material);
            
            // Add to scene temporarily
            if (this.avatar && this.avatar.scene) {
                this.avatar.scene.add(line);
                
                // Remove after one frame
                setTimeout(() => {
                    this.avatar.scene.remove(line);
                    geometry.dispose();
                    material.dispose();
                }, 16);
            }
        });
    }
    
    setWind(x, y, z) {
        this.windForce.set(x, y, z);
    }
    
    setGravity(x, y, z) {
        this.gravity.set(x, y, z);
    }
    
    reset() {
        // Reset all particles to initial positions
        this.hairParticles.forEach(strand => {
            strand.forEach(particle => {
                particle.previousPosition.copy(particle.position);
                particle.velocity.set(0, 0, 0);
            });
        });
        
        this.clothVertices.forEach(particle => {
            particle.previousPosition.copy(particle.position);
            particle.velocity.set(0, 0, 0);
        });
    }
    
    // Advanced: Collision detection with avatar body
    checkCollisions() {
        // Check if particles collide with avatar mesh
        if (!this.avatar || !this.avatar.avatar) return;
        
        const headPosition = new THREE.Vector3(0, 1.6, 0);
        const headRadius = 0.15;
        
        // Check hair collisions with head
        this.hairParticles.forEach(strand => {
            strand.forEach(particle => {
                if (particle.fixed) return;
                
                const distance = particle.position.distanceTo(headPosition);
                
                if (distance < headRadius) {
                    // Push particle out of collision
                    const direction = new THREE.Vector3();
                    direction.subVectors(particle.position, headPosition).normalize();
                    particle.position.copy(headPosition).add(direction.multiplyScalar(headRadius));
                }
            });
        });
    }
}
