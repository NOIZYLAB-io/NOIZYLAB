/**
 * GABRIEL SYSTEM OMEGA - Neural Engine
 * Force-Directed Graph Visualization
 * ===================================
 * PERFORMANCE OPTIMIZED - Zero Latency Mode
 */

class NeuralEngine {
     constructor(canvasId) {
          this.canvas = document.getElementById(canvasId);
          this.ctx = this.canvas.getContext('2d', { alpha: false });

          // Graph data
          this.nodes = [];
          this.edges = [];
          this.nodeMap = new Map(); // Fast node lookup by ID

          // Physics settings
          this.physics = {
               enabled: true,
               repulsion: 5000,
               attraction: 0.01,
               damping: 0.9,
               centerGravity: 0.01,
               maxIterations: 50 // Limit physics iterations for stability
          };

          // Performance optimization
          this.frameSkip = 0;
          this.physicsUpdateRate = 2; // Update physics every N frames

          // Visual settings
          this.colors = {
               core: '#00ff41',
               system: '#00ffff',
               protocol: '#a855f7',
               module: '#ffd700',
               edge: 'rgba(0, 255, 65, 0.3)',
               edgeActive: 'rgba(0, 255, 65, 0.8)',
               text: '#ffffff',
               glow: 'rgba(0, 255, 65, 0.5)'
          };

          // Animation
          this.animationFrame = null;
          this.time = 0;

          // Interaction
          this.hoveredNode = null;
          this.selectedNode = null;
          this.isDragging = false;
          this.dragNode = null;

          this.init();
     }

     init() {
          this.resize();
          window.addEventListener('resize', () => this.resize());

          // Mouse events
          this.canvas.addEventListener('mousemove', (e) => this.onMouseMove(e));
          this.canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
          this.canvas.addEventListener('mouseup', () => this.onMouseUp());
          this.canvas.addEventListener('mouseleave', () => this.onMouseUp());
     }

     resize() {
          const rect = this.canvas.parentElement.getBoundingClientRect();
          this.canvas.width = rect.width - 40;
          this.canvas.height = 400;
          this.centerX = this.canvas.width / 2;
          this.centerY = this.canvas.height / 2;
     }

     async loadData() {
          try {
               const data = await API_BRIDGE.getMemCellGraph();
               this.setData(data.nodes, data.edges);
          } catch (error) {
               console.error('[NEURAL_ENGINE] Failed to load graph data:', error);
               this.loadDefaultData();
          }
     }

     loadDefaultData() {
          const defaultNodes = [
               { id: 'gabriel', label: 'GABRIEL', type: 'core' },
               { id: 'mc96', label: 'MC96', type: 'system' },
               { id: 'omega', label: 'OMEGA', type: 'protocol' },
               { id: 'voice', label: 'VOICE', type: 'module' },
               { id: 'vision', label: 'VISION', type: 'module' },
               { id: 'memory', label: 'MEMORY', type: 'module' },
               { id: 'shirl', label: 'SHIRL', type: 'core' },
               { id: 'deepseek', label: 'DEEPSEEK', type: 'protocol' }
          ];

          const defaultEdges = [
               { from: 'gabriel', to: 'mc96' },
               { from: 'gabriel', to: 'omega' },
               { from: 'gabriel', to: 'voice' },
               { from: 'gabriel', to: 'vision' },
               { from: 'gabriel', to: 'shirl' },
               { from: 'mc96', to: 'memory' },
               { from: 'omega', to: 'memory' },
               { from: 'omega', to: 'deepseek' },
               { from: 'shirl', to: 'voice' }
          ];

          this.setData(defaultNodes, defaultEdges);
     }

     setData(nodes, edges) {
          // Initialize nodes with random positions around center
          this.nodes = nodes.map((n, i) => ({
               ...n,
               x: this.centerX + (Math.random() - 0.5) * 200,
               y: this.centerY + (Math.random() - 0.5) * 200,
               vx: 0,
               vy: 0,
               radius: n.type === 'core' ? 35 : 25
          }));

          // Build node map for O(1) lookups
          this.nodeMap.clear();
          for (const node of this.nodes) {
               this.nodeMap.set(node.id, node);
          }

          this.edges = edges.map(e => ({
               ...e,
               pulse: Math.random() * Math.PI * 2,
               fromNode: null, // Will be resolved
               toNode: null
          }));

          // Pre-resolve edge node references for O(1) access during render
          for (const edge of this.edges) {
               edge.fromNode = this.nodeMap.get(edge.from);
               edge.toNode = this.nodeMap.get(edge.to);
          }
     }

     start() {
          if (this.animationFrame) return;
          this.loadData();
          this.animate();
     }

     stop() {
          if (this.animationFrame) {
               cancelAnimationFrame(this.animationFrame);
               this.animationFrame = null;
          }
     }

     animate() {
          this.time += 0.016; // ~60fps
          this.frameSkip++;

          // Update physics at reduced rate for performance
          if (this.physics.enabled && !this.isDragging && this.frameSkip % this.physicsUpdateRate === 0) {
               this.updatePhysics();
          }

          this.render();
          this.animationFrame = requestAnimationFrame(() => this.animate());
     }

     updatePhysics() {
          const nodes = this.nodes;
          const nodeCount = nodes.length;

          // Node repulsion - optimized loop
          for (let i = 0; i < nodeCount; i++) {
               const nodeI = nodes[i];
               for (let j = i + 1; j < nodeCount; j++) {
                    const nodeJ = nodes[j];
                    const dx = nodeJ.x - nodeI.x;
                    const dy = nodeJ.y - nodeI.y;
                    const distSq = dx * dx + dy * dy;
                    const dist = Math.sqrt(distSq) || 1;
                    const force = this.physics.repulsion / (dist * dist);

                    const fx = (dx / dist) * force;
                    const fy = (dy / dist) * force;

                    nodeI.vx -= fx;
                    nodeI.vy -= fy;
                    nodeJ.vx += fx;
                    nodeJ.vy += fy;
               }
          }

          // Edge attraction - use pre-resolved references
          for (const edge of this.edges) {
               const from = edge.fromNode;
               const to = edge.toNode;
               if (!from || !to) continue;

               const dx = to.x - from.x;
               const dy = to.y - from.y;
               const dist = Math.sqrt(dx * dx + dy * dy) || 1;
               const force = dist * this.physics.attraction;

               const fx = (dx / dist) * force;
               const fy = (dy / dist) * force;

               from.vx += fx;
               from.vy += fy;
               to.vx -= fx;
               to.vy -= fy;
          }

          // Center gravity & velocity application - combined loop
          const damping = this.physics.damping;
          const centerGravity = this.physics.centerGravity;
          const width = this.canvas.width;
          const height = this.canvas.height;

          for (const node of nodes) {
               node.vx += (this.centerX - node.x) * centerGravity;
               node.vy += (this.centerY - node.y) * centerGravity;
               node.vx *= damping;
               node.vy *= damping;
               node.x += node.vx;
               node.y += node.vy;

               // Bounds check
               const r = node.radius;
               if (node.x < r) node.x = r;
               else if (node.x > width - r) node.x = width - r;
               if (node.y < r) node.y = r;
               else if (node.y > height - r) node.y = height - r;
          }
     }

     render() {
          const ctx = this.ctx;
          const width = this.canvas.width;
          const height = this.canvas.height;
          
          // Clear with solid color (faster than clearRect with transparency)
          ctx.fillStyle = 'rgb(10, 10, 15)';
          ctx.fillRect(0, 0, width, height);

          // Draw edges with pre-resolved references
          ctx.lineWidth = 2;
          for (const edge of this.edges) {
               const from = edge.fromNode;
               const to = edge.toNode;
               if (!from || !to) continue;

               // Animated pulse along edge
               edge.pulse += 0.02;
               const pulsePos = (Math.sin(edge.pulse) + 1) * 0.5;

               ctx.beginPath();
               ctx.moveTo(from.x, from.y);
               ctx.lineTo(to.x, to.y);
               ctx.strokeStyle = this.colors.edge;
               ctx.stroke();

               // Draw pulse
               const px = from.x + (to.x - from.x) * pulsePos;
               const py = from.y + (to.y - from.y) * pulsePos;
               ctx.beginPath();
               ctx.arc(px, py, 4, 0, Math.PI * 2);
               ctx.fillStyle = this.colors.core;
               ctx.fill();
          }

          // Draw nodes
          for (const node of this.nodes) {
               const isHovered = node === this.hoveredNode;
               const isSelected = node === this.selectedNode;
               const color = this.colors[node.type] || this.colors.module;
               const radius = node.radius + (isHovered ? 5 : 0);

               // Glow effect
               if (isHovered || isSelected || node.type === 'core') {
                    ctx.beginPath();
                    ctx.arc(node.x, node.y, radius + 10, 0, Math.PI * 2);
                    const gradient = ctx.createRadialGradient(
                         node.x, node.y, radius,
                         node.x, node.y, radius + 20
                    );
                    gradient.addColorStop(0, color.replace(')', ', 0.3)').replace('rgb', 'rgba'));
                    gradient.addColorStop(1, 'transparent');
                    ctx.fillStyle = gradient;
                    ctx.fill();
               }

               // Node circle
               ctx.beginPath();
               ctx.arc(node.x, node.y, radius, 0, Math.PI * 2);
               ctx.fillStyle = 'rgba(0, 0, 0, 0.8)';
               ctx.fill();
               ctx.strokeStyle = color;
               ctx.lineWidth = isHovered ? 3 : 2;
               ctx.stroke();

               // Rotating ring for core nodes
               if (node.type === 'core') {
                    ctx.save();
                    ctx.translate(node.x, node.y);
                    ctx.rotate(this.time);
                    ctx.beginPath();
                    ctx.arc(0, 0, radius + 8, 0, Math.PI * 0.5);
                    ctx.strokeStyle = color;
                    ctx.lineWidth = 2;
                    ctx.stroke();
                    ctx.restore();
               }

               // Label
               ctx.font = `bold ${node.type === 'core' ? 11 : 9}px 'Orbitron', sans-serif`;
               ctx.fillStyle = this.colors.text;
               ctx.textAlign = 'center';
               ctx.textBaseline = 'middle';
               ctx.fillText(node.label, node.x, node.y);
          }

          // Draw tooltip for hovered node
          if (this.hoveredNode) {
               const node = this.hoveredNode;
               const tooltipText = `${node.label} // ${node.type.toUpperCase()}`;
               ctx.font = '12px JetBrains Mono';
               const textWidth = ctx.measureText(tooltipText).width;

               ctx.fillStyle = 'rgba(0, 0, 0, 0.9)';
               ctx.fillRect(node.x - textWidth / 2 - 10, node.y - node.radius - 35, textWidth + 20, 25);
               ctx.strokeStyle = this.colors[node.type] || this.colors.module;
               ctx.strokeRect(node.x - textWidth / 2 - 10, node.y - node.radius - 35, textWidth + 20, 25);

               ctx.fillStyle = '#fff';
               ctx.textAlign = 'center';
               ctx.fillText(tooltipText, node.x, node.y - node.radius - 22);
          }
     }

     getNodeAtPosition(x, y) {
          for (const node of this.nodes) {
               const dx = x - node.x;
               const dy = y - node.y;
               if (dx * dx + dy * dy < node.radius * node.radius) {
                    return node;
               }
          }
          return null;
     }

     onMouseMove(e) {
          const rect = this.canvas.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;

          if (this.isDragging && this.dragNode) {
               this.dragNode.x = x;
               this.dragNode.y = y;
               this.dragNode.vx = 0;
               this.dragNode.vy = 0;
          } else {
               this.hoveredNode = this.getNodeAtPosition(x, y);
               this.canvas.style.cursor = this.hoveredNode ? 'pointer' : 'default';
          }
     }

     onMouseDown(e) {
          const rect = this.canvas.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;

          const node = this.getNodeAtPosition(x, y);
          if (node) {
               this.isDragging = true;
               this.dragNode = node;
               this.selectedNode = node;
          }
     }

     onMouseUp() {
          this.isDragging = false;
          this.dragNode = null;
     }

     resetView() {
          this.loadData();
     }

     togglePhysics() {
          this.physics.enabled = !this.physics.enabled;
          return this.physics.enabled;
     }

     exportGraph() {
          const data = {
               nodes: this.nodes.map(n => ({ id: n.id, label: n.label, type: n.type, x: n.x, y: n.y })),
               edges: this.edges.map(e => ({ from: e.from, to: e.to }))
          };
          const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = 'gabriel_neural_graph.json';
          a.click();
          URL.revokeObjectURL(url);
     }
}

// Export
window.NeuralEngine = NeuralEngine;
