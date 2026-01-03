import { GabrielScanner } from '../scanner/index.js';
import { GabrielSync } from '../sync/index.js';
import { GabrielHealer } from '../healer/index.js';
import { GabrielOrganizer } from '../organizer/index.js';

/**
 * GABRIEL DAEMON — Always-On Runner
 * 
 * Continuous monitoring and processing daemon that runs:
 * - File scanning
 * - Auto-healing
 * - File organization
 * - Cloudflare synchronization
 * 
 * @example
 * const daemon = new GabrielDaemon('/project/path', {
 *   kv: 'https://kv-endpoint.com'
 * });
 * 
 * daemon.start(60000); // Run every 60 seconds
 */
export class GabrielDaemon {
  constructor(root, endpoints = {}) {
    // Default to NOIZYLAB root for local operations
    this.root = root || '/Users/m2ultra/NOIZYLAB';
    this.endpoints = endpoints || {}; // Optional - works without endpoints
    
    // Initialize subsystems
    this.scan = new GabrielScanner(this.root);
    this.sync = new GabrielSync(this.root, endpoints);
    this.heal = new GabrielHealer(this.root);
    this.org = new GabrielOrganizer(this.root);
    
    this.running = false;
    this.intervalId = null;
    this.cycleCount = 0;
    this.stats = {
      cycles: 0,
      errors: 0,
      startTime: null,
      lastCycleTime: null
    };
  }

  /**
   * Run a single cycle of operations
   * @returns {Promise<Object>} Cycle results
   */
  async cycle() {
    const cycleStart = Date.now();
    this.cycleCount++;

    try {
      // 1. Scan files
      const files = await this.scan.scan();

      // 2. Heal issues
      const healed = await this.heal.heal();

      // 3. Organize files
      const organized = this.org.organize(files);

      // 4. Sync to Cloudflare
      const synced = await this.sync.sync();

      this.stats.lastCycleTime = Date.now() - cycleStart;
      this.stats.cycles++;

      return {
        cycle: this.cycleCount,
        files: files.length,
        healed: healed.fixed || 0,
        organized: organized.filter(r => r.success).length,
        synced: synced ? 'success' : 'failed',
        duration: this.stats.lastCycleTime
      };
    } catch (error) {
      this.stats.errors++;
      console.error(`Cycle ${this.cycleCount} error:`, error);
      
      return {
        cycle: this.cycleCount,
        error: error.message,
        duration: Date.now() - cycleStart
      };
    }
  }

  /**
   * Start daemon with specified interval
   * @param {number} intervalMs - Interval in milliseconds (default: 60000 = 1 minute)
   */
  start(intervalMs = 60000) {
    if (this.running) {
      console.log('GABRIEL DAEMON already running');
      return;
    }

    this.running = true;
    this.stats.startTime = Date.now();
    
    console.log('🟣 GABRIEL DAEMON ACTIVE');
    console.log(`   Root: ${this.root}`);
    console.log(`   Interval: ${intervalMs}ms (${intervalMs / 1000}s)`);
    console.log('   Starting initial cycle...\n');

    // Run initial cycle immediately
    this.cycle().then(result => {
      console.log(`✅ Cycle ${result.cycle} complete:`, {
        files: result.files,
        healed: result.healed,
        organized: result.organized,
        synced: result.synced,
        duration: `${result.duration}ms`
      });
    }).catch(error => {
      console.error('❌ Initial cycle failed:', error);
    });

    // Set up interval for subsequent cycles
    this.intervalId = setInterval(() => {
      this.cycle().then(result => {
        if (result.error) {
          console.error(`❌ Cycle ${result.cycle} error:`, result.error);
        } else {
          console.log(`✅ Cycle ${result.cycle} complete:`, {
            files: result.files,
            healed: result.healed,
            organized: result.organized,
            synced: result.synced,
            duration: `${result.duration}ms`
          });
        }
      }).catch(error => {
        console.error(`❌ Cycle ${this.cycleCount} exception:`, error);
      });
    }, intervalMs);
  }

  /**
   * Stop daemon
   */
  stop() {
    if (!this.running) {
      return;
    }

    this.running = false;
    
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }

    const uptime = Date.now() - this.stats.startTime;
    console.log('\n🟣 GABRIEL DAEMON STOPPED');
    console.log(`   Uptime: ${Math.floor(uptime / 1000)}s`);
    console.log(`   Cycles: ${this.stats.cycles}`);
    console.log(`   Errors: ${this.stats.errors}`);
  }

  /**
   * Get daemon status
   * @returns {Object} Status information
   */
  getStatus() {
    const uptime = this.stats.startTime 
      ? Date.now() - this.stats.startTime 
      : 0;

    return {
      running: this.running,
      cycleCount: this.cycleCount,
      uptime,
      stats: {
        ...this.stats,
        uptime
      }
    };
  }

  /**
   * Run single cycle (alias for cycle())
   * @returns {Promise<Object>} Cycle results
   */
  async run() {
    return await this.cycle();
  }
}

// Default export
export default GabrielDaemon;

// For CommonJS compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GabrielDaemon;
  module.exports.default = GabrielDaemon;
}

