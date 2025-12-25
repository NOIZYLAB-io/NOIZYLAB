/**
 * GABRIEL SYSTEM OMEGA - Main Application
 * Mission Control Portal Core Logic
 * ====================================
 */

class GabrielPortal {
     // Configuration constants
     static PARTICLE_CONNECTION_DISTANCE_SQ = 100 * 100; // 10000 (squared for perf)

     constructor() {
          this.neuralEngine = null;
          this.feedMessages = [];
          this.updateInterval = null;
          this.bgCanvas = null;
          this.bgCtx = null;
          this.particles = [];
          // Cached DOM elements for performance (avoid repeated getElementById calls)
          this.cachedElements = {};
     }

     async init() {
          this.log('[INIT] Gabriel Enablement Portal booting...');

          // Initialize background
          this.initBackground();

          // Cache frequently accessed DOM elements (performance optimization)
          this.cacheElements();

          // Initialize API
          await API_BRIDGE.init();
          const connected = API_BRIDGE.state.connected;
          this.log(`[API] Connection status: ${connected ? 'ONLINE' : 'OFFLINE (Mock Mode)'}`);

          // Initialize Neural Engine
          this.neuralEngine = new NeuralEngine('neural-graph');
          this.neuralEngine.start();
          this.log('[NEURAL] Neural visualization engine started');

          // Setup UI handlers
          this.setupEventListeners();

          // Start status updates
          this.startStatusUpdates();

          // Update timestamp
          this.updateTimestamp();
          setInterval(() => this.updateTimestamp(), 1000);

          this.log('[READY] Gabriel System Omega is ONLINE');
          this.log('[PROTOCOL] GORUNFREE enabled');

          // Play startup sound (visual only for now)
          this.flashStatus();
     }

     cacheElements() {
          // Cache DOM elements to avoid repeated getElementById calls
          this.cachedElements = {
               latency: document.getElementById('latency-value'),
               agents: document.getElementById('agents-value'),
               memcell: document.getElementById('memcell-value'),
               uptime: document.getElementById('uptime-value'),
               statusBadge: document.getElementById('system-status'),
               timestamp: document.getElementById('timestamp'),
               feed: document.getElementById('live-feed')
          };
     }

     initBackground() {
          this.bgCanvas = document.getElementById('neural-bg');
          this.bgCtx = this.bgCanvas.getContext('2d');

          const resize = () => {
               this.bgCanvas.width = window.innerWidth;
               this.bgCanvas.height = window.innerHeight;
          };

          resize();
          window.addEventListener('resize', resize);

          // Create particles
          for (let i = 0; i < 100; i++) {
               this.particles.push({
                    x: Math.random() * window.innerWidth,
                    y: Math.random() * window.innerHeight,
                    vx: (Math.random() - 0.5) * 0.5,
                    vy: (Math.random() - 0.5) * 0.5,
                    size: Math.random() * 2 + 1
               });
          }

          this.animateBackground();
     }

     animateBackground() {
          const ctx = this.bgCtx;
          ctx.clearRect(0, 0, this.bgCanvas.width, this.bgCanvas.height);

          // Update and draw particles
          for (const p of this.particles) {
               p.x += p.vx;
               p.y += p.vy;

               // Wrap around
               if (p.x < 0) p.x = this.bgCanvas.width;
               if (p.x > this.bgCanvas.width) p.x = 0;
               if (p.y < 0) p.y = this.bgCanvas.height;
               if (p.y > this.bgCanvas.height) p.y = 0;

               ctx.beginPath();
               ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
               ctx.fillStyle = 'rgba(0, 255, 65, 0.5)';
               ctx.fill();
          }

          // Draw connections between nearby particles
          // OPTIMIZATION: Use squared distance to avoid expensive Math.sqrt()
          // OPTIMIZATION: Batch path operations with single beginPath/stroke
          ctx.strokeStyle = 'rgba(0, 255, 65, 0.1)';
          ctx.lineWidth = 1;
          ctx.beginPath(); // Single beginPath for all connection lines
          for (let i = 0; i < this.particles.length; i++) {
               const p1 = this.particles[i];
               for (let j = i + 1; j < this.particles.length; j++) {
                    const p2 = this.particles[j];
                    const dx = p2.x - p1.x;
                    const dy = p2.y - p1.y;
                    const distSq = dx * dx + dy * dy;

                    if (distSq < GabrielPortal.PARTICLE_CONNECTION_DISTANCE_SQ) {
                         ctx.moveTo(p1.x, p1.y);
                         ctx.lineTo(p2.x, p2.y);
                    }
               }
          }
          ctx.stroke(); // Single stroke call for all lines

          requestAnimationFrame(() => this.animateBackground());
     }

     setupEventListeners() {
          // Quick action buttons
          document.querySelectorAll('.action-card').forEach(card => {
               card.addEventListener('click', (e) => {
                    const action = card.dataset.action;
                    this.handleAction(action);
               });
          });

          // Neural controls
          document.getElementById('reset-graph')?.addEventListener('click', () => {
               this.neuralEngine.resetView();
               this.log('[NEURAL] Graph view reset');
          });

          document.getElementById('toggle-physics')?.addEventListener('click', () => {
               const enabled = this.neuralEngine.togglePhysics();
               this.log(`[NEURAL] Physics ${enabled ? 'enabled' : 'disabled'}`);
          });

          document.getElementById('export-graph')?.addEventListener('click', () => {
               this.neuralEngine.exportGraph();
               this.log('[NEURAL] Graph exported to JSON');
          });

          // Keyboard shortcuts
          document.addEventListener('keydown', (e) => {
               if (e.key === 'Escape') this.neuralEngine.selectedNode = null;
               if (e.key === 'r' && e.ctrlKey) {
                    e.preventDefault();
                    this.neuralEngine.resetView();
               }
          });
     }

     handleAction(action) {
          this.log(`[CMD] Executing: ${action.toUpperCase()}`);

          switch (action) {
               case 'mission-control':
                    this.log('[NAV] Opening Mission Control Dashboard...');
                    window.open('mini_dashboard.html', '_blank');
                    break;

               case 'memcell':
                    this.log('[MEMCELL] Accessing MemCell Brain interface...');
                    this.neuralEngine.resetView();
                    document.querySelector('.neural-section')?.scrollIntoView({ behavior: 'smooth' });
                    break;

               case 'knowledge-graph':
                    this.log('[QUERY] Knowledge Graph explorer launching...');
                    this.showNotification('Knowledge Graph - Opening Explorer');
                    break;

               case 'voice-forge':
                    this.log('[AUDIO] Voice Forge TTS engine ready');
                    this.testVoice();
                    break;

               case 'sonic-templator':
                    this.log('[SONIC] SONIC-TEMPLATOR scaffolding tool');
                    this.showNotification('SONIC-TEMPLATOR - Ready for project creation');
                    break;

               case 'deepseek':
                    this.log('[R1] DeepSeek R1 reasoning engine connecting...');
                    window.open('https://chat.deepseek.com/', '_blank');
                    break;

               default:
                    this.log(`[WARN] Unknown action: ${action}`);
          }
     }

     testVoice() {
          // Use Web Speech API if available
          if ('speechSynthesis' in window) {
               const utterance = new SpeechSynthesisUtterance('Gabriel System Omega online. All systems nominal.');
               utterance.rate = 0.9;
               utterance.pitch = 0.8;
               speechSynthesis.speak(utterance);
               this.log('[VOICE] Audio test complete');
          } else {
               this.log('[VOICE] Web Speech API not available');
          }
     }

     async startStatusUpdates() {
          const update = async () => {
               try {
                    const status = await API_BRIDGE.getStatus();
                    this.updateMetrics(status);
               } catch (e) {
                    console.warn('Status update failed:', e);
               }
          };

          update();
          this.updateInterval = setInterval(update, 5000);
     }

     updateMetrics(status) {
          // Use cached DOM elements for better performance
          const { latency, agents, memcell, uptime, statusBadge } = this.cachedElements;

          if (latency) latency.textContent = status.latency || '<7ms';
          if (agents) agents.textContent = status.agents_active || '3';
          if (memcell) memcell.textContent = status.memcell_nodes || '∞';
          if (uptime) uptime.textContent = status.uptime || '99.9%';

          // Update connection status
          if (statusBadge) {
               const statusText = statusBadge.querySelector('.status-text');
               if (statusText) {
                    statusText.textContent = status.status || 'ONLINE';
               }
          }
     }

     updateTimestamp() {
          const el = this.cachedElements.timestamp;
          if (el) {
               const now = new Date();
               el.textContent = `SYNC: ${now.toISOString()}`;
          }
     }

     log(message) {
          const feed = this.cachedElements.feed;
          if (!feed) return;

          const time = new Date().toLocaleTimeString('en-US', { hour12: false });
          const line = document.createElement('div');
          line.className = 'feed-line';
          line.textContent = `[${time}] ${message}`;

          feed.appendChild(line);
          feed.scrollTop = feed.scrollHeight;

          // Keep only last 50 messages
          while (feed.children.length > 50) {
               feed.removeChild(feed.firstChild);
          }

          console.log(`[GABRIEL] ${message}`);
     }

     flashStatus() {
          const badge = this.cachedElements.statusBadge;
          if (badge) {
               badge.style.animation = 'none';
               badge.offsetHeight; // Trigger reflow
               badge.style.animation = 'pulse-glow 0.5s ease-in-out 3';
          }
     }

     showNotification(message) {
          // Create toast notification
          const toast = document.createElement('div');
          toast.style.cssText = `
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: rgba(0, 255, 65, 0.1);
            border: 1px solid #00ff41;
            color: #00ff41;
            padding: 15px 25px;
            border-radius: 8px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 14px;
            z-index: 9999;
            animation: slideIn 0.3s ease;
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.3);
        `;
          toast.textContent = message;

          document.body.appendChild(toast);

          setTimeout(() => {
               toast.style.animation = 'slideOut 0.3s ease forwards';
               setTimeout(() => toast.remove(), 300);
          }, 3000);
     }
}

// Add animation styles
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100px); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
     window.portal = new GabrielPortal();
     window.portal.init();
});
