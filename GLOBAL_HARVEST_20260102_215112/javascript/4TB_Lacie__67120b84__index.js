/**
 * 🟣 GABRIEL OS v1.0 — Main Entry Point
 * 
 * Complete OS foundation for NOIZYLAB infrastructure.
 * Integrates all GABRIEL subsystems into unified interface.
 * 
 * @example
 * import Gabriel from './gabriel/index.js';
 * 
 * // Quick start
 * const gabriel = new Gabriel('/project/path', {
 *   kv: 'https://kv-endpoint.com'
 * });
 * 
 * // Run daemon
 * gabriel.start();
 * 
 * // Or use individual modules
 * const files = await gabriel.scan();
 * await gabriel.heal();
 * gabriel.organize(files);
 */
import { GabrielScanner } from './scanner/index.js';
import { GabrielSync, GabrielSyncEngine } from './sync/index.js';
import { GabrielHealer } from './healer/index.js';
import { GabrielOrganizer } from './organizer/index.js';
import { GabrielDaemon } from './daemon/index.js';
import { GabrielPipeline } from './pipeline/index.js';
import { GabrielCodeProcessor } from './code-processor/index.js';
import { GabrielCleanup } from './cleanup/index.js';

export class Gabriel {
  constructor(root, options = {}) {
    // Default to NOIZYLAB root for local operations
    this.root = root || '/Users/m2ultra/NOIZYLAB';
    this.options = {
      ...options,
      // Local-first: no Cloudflare endpoints required
      endpoints: options.endpoints || {}
    };
    
    // Initialize all subsystems
    this.scanner = new GabrielScanner(this.root, options.scanner || {});
    this.sync = new GabrielSync(this.root, options.endpoints || {});
    this.syncEngine = new GabrielSyncEngine({
      r2: options.endpoints?.r2 || null,
      kv: options.endpoints?.kv || null,
      d1: options.endpoints?.d1 || null,
      ...options.syncEngine
    });
    this.healer = new GabrielHealer(this.root, options.healer || {});
    this.organizer = new GabrielOrganizer(this.root, options.organizer || {});
    this.daemon = new GabrielDaemon(this.root, options.endpoints || {});
    this.pipeline = new GabrielPipeline(options.endpoints || {});
    this.codeProcessor = new GabrielCodeProcessor(this.root, options.codeProcessor || {});
    this.cleanup = new GabrielCleanup(this.root, options.cleanup || {});
  }

  // ────────────────────────────────────────────────────────────────
  // SCANNER METHODS
  // ────────────────────────────────────────────────────────────────

  /**
   * Scan directory for files
   * @returns {Promise<Array>} Scanned files
   */
  async scan() {
    return await this.scanner.scan();
  }

  /**
   * Get scan statistics
   * @returns {Object} Scan statistics
   */
  getScanStats() {
    return this.scanner.getStats();
  }

  /**
   * Filter scanned files by classification
   * @param {string} classification - Classification type
   * @returns {Array} Filtered files
   */
  filterByType(classification) {
    return this.scanner.filterByClassification(classification);
  }

  // ────────────────────────────────────────────────────────────────
  // SYNC METHODS
  // ────────────────────────────────────────────────────────────────

  /**
   * Sync to Cloudflare
   * @returns {Promise<Array>} Synced files
   */
  async sync() {
    return await this.sync.sync();
  }

  /**
   * Sync to specific endpoint
   * @param {string} endpoint - Endpoint name
   * @param {Object} options - Sync options
   */
  async syncTo(endpoint, options = {}) {
    return await this.sync.syncTo(endpoint, options);
  }

  /**
   * Sync from endpoint
   * @param {string} endpoint - Endpoint name
   * @param {Object} options - Sync options
   */
  async syncFrom(endpoint, options = {}) {
    return await this.sync.syncFrom(endpoint, options);
  }

  // ────────────────────────────────────────────────────────────────
  // HEALER METHODS
  // ────────────────────────────────────────────────────────────────

  /**
   * Scan for issues
   * @returns {Promise<Array>} Issues found
   */
  async scanIssues() {
    return await this.healer.scan();
  }

  /**
   * Heal codebase issues
   * @returns {Promise<Object>} Healing report
   */
  async heal() {
    return await this.healer.heal();
  }

  /**
   * Fix specific issue
   * @param {Object} issue - Issue to fix
   * @returns {Promise<boolean>} Success status
   */
  async fixIssue(issue) {
    return await this.healer.fixIssue(issue);
  }

  /**
   * Get healing report
   * @returns {Object} Healing report
   */
  getHealReport() {
    return this.healer.getReport();
  }

  // ────────────────────────────────────────────────────────────────
  // ORGANIZER METHODS
  // ────────────────────────────────────────────────────────────────

  /**
   * Organize files
   * @param {Array} files - Files to organize
   * @returns {Array} Organization results
   */
  organize(files) {
    return this.organizer.organize(files);
  }

  /**
   * Ensure directory structure
   */
  ensureStructure() {
    this.organizer.ensureStructure();
  }

  /**
   * Get organization report
   * @returns {Object} Organization report
   */
  getOrgReport() {
    return this.organizer.getReport();
  }

  // ────────────────────────────────────────────────────────────────
  // DAEMON METHODS
  // ────────────────────────────────────────────────────────────────

  /**
   * Start daemon
   * @param {number} intervalMs - Interval in milliseconds
   */
  start(intervalMs = 60000) {
    this.daemon.start(intervalMs);
  }

  /**
   * Stop daemon
   */
  stop() {
    this.daemon.stop();
  }

  /**
   * Run single cycle
   * @returns {Promise<Object>} Cycle results
   */
  async cycle() {
    return await this.daemon.cycle();
  }

  /**
   * Get daemon status
   * @returns {Object} Status information
   */
  getStatus() {
    return this.daemon.getStatus();
  }

  // ────────────────────────────────────────────────────────────────
  // PIPELINE METHODS
  // ────────────────────────────────────────────────────────────────

  /**
   * Run event through pipeline
   * @param {Object} event - Event to process
   * @param {Object} options - Pipeline options
   * @returns {Promise<Object>} Pipeline result
   */
  async runEvent(event, options = {}) {
    return await this.pipeline.runEvent(event, options);
  }

  /**
   * Run specific pipeline stage
   * @param {string} stage - Stage name
   * @param {Object} event - Event data
   * @returns {Promise<Object>} Stage result
   */
  async runStage(stage, event) {
    return await this.pipeline.runStage(stage, event);
  }

  /**
   * Get pipeline statistics
   * @returns {Object} Pipeline stats
   */
  getPipelineStats() {
    return this.pipeline.getStats();
  }

  // ────────────────────────────────────────────────────────────────
  // COMPOSITE OPERATIONS
  // ────────────────────────────────────────────────────────────────

  /**
   * Complete workflow: scan → heal → organize → sync
   * @returns {Promise<Object>} Complete workflow results
   */
  async workflow() {
    console.log('🟣 GABRIEL OS - Complete Workflow');
    console.log('='.repeat(60));

    const results = {
      scan: null,
      heal: null,
      organize: null,
      sync: null
    };

    try {
      // 1. Scan
      console.log('📂 Step 1: Scanning files...');
      results.scan = await this.scan();
      console.log(`   ✓ Found ${results.scan.length} files`);

      // 2. Heal
      console.log('\n🔧 Step 2: Healing issues...');
      results.heal = await this.heal();
      console.log(`   ✓ Fixed ${results.heal.fixed || 0} issues`);

      // 3. Organize
      console.log('\n📁 Step 3: Organizing files...');
      results.organize = this.organize(results.scan);
      const organizedCount = results.organize.filter(r => r.success).length;
      console.log(`   ✓ Organized ${organizedCount} files`);

      // 4. Sync
      console.log('\n☁️  Step 4: Syncing to Cloudflare...');
      results.sync = await this.sync();
      console.log('   ✓ Sync complete');

      console.log('\n✅ Workflow complete!');
      return results;
    } catch (error) {
      console.error('\n❌ Workflow error:', error.message);
      throw error;
    }
  }

  /**
   * Get complete system status
   * @returns {Object} System status
   */
  getSystemStatus() {
    return {
      root: this.root,
      daemon: this.daemon.getStatus(),
      pipeline: this.pipeline.getStats(),
      codeProcessor: this.codeProcessor.getReport(),
      timestamp: Date.now()
    };
  }

  // ────────────────────────────────────────────────────────────────
  // CODE PROCESSOR METHODS
  // ────────────────────────────────────────────────────────────────

  /**
   * Process code through complete lifecycle
   * @param {string|Object} code - Code to process
   * @param {Object} options - Processing options
   * @returns {Promise<Object>} Processing result
   */
  async processCode(code, options = {}) {
    return await this.codeProcessor.process(code, options);
  }

  /**
   * Test code
   * @param {Object} entry - Code entry
   * @returns {Promise<Object>} Test results
   */
  async testCode(entry) {
    return await this.codeProcessor.test(entry);
  }

  /**
   * Harvest patterns from code
   * @param {Object} entry - Code entry
   * @returns {Promise<Object>} Harvested data
   */
  async harvestCode(entry) {
    return await this.codeProcessor.harvest(entry);
  }

  /**
   * Optimize code
   * @param {Object} entry - Code entry
   * @param {Object} harvested - Harvested data
   * @returns {Promise<Object>} Optimized code
   */
  async optimizeCode(entry, harvested) {
    return await this.codeProcessor.optimize(entry, harvested);
  }

  /**
   * Get code processor report
   * @returns {Object} Processing report
   */
  getCodeReport() {
    return this.codeProcessor.getReport();
  }

  // ────────────────────────────────────────────────────────────────
  // CLEANUP METHODS
  // ────────────────────────────────────────────────────────────────

  /**
   * Delete empty folders
   * @param {boolean} dryRun - Dry run mode
   * @returns {Promise<Object>} Cleanup report
   */
  async cleanup(dryRun = false) {
    const cleanup = new (await import('./cleanup/index.js')).GabrielCleanup(
      this.root,
      { ...this.options.cleanup, dryRun }
    );
    return await cleanup.deleteEmptyFolders();
  }

  /**
   * Find empty folders without deleting
   * @returns {Promise<Array>} List of empty folders
   */
  async findEmptyFolders() {
    const cleanup = new (await import('./cleanup/index.js')).GabrielCleanup(
      this.root,
      { ...this.options.cleanup, dryRun: true }
    );
    return await cleanup.findEmptyFolders();
  }
}

// Export all modules
export {
  GabrielScanner,
  GabrielSync,
  GabrielSyncEngine,
  GabrielHealer,
  GabrielOrganizer,
  GabrielDaemon,
  GabrielPipeline,
  GabrielCodeProcessor,
  GabrielCleanup
};

// Default export
export default Gabriel;

// For CommonJS compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = Gabriel;
  module.exports.default = Gabriel;
  module.exports.GabrielScanner = GabrielScanner;
  module.exports.GabrielSync = GabrielSync;
  module.exports.GabrielSyncEngine = GabrielSyncEngine;
  module.exports.GabrielHealer = GabrielHealer;
  module.exports.GabrielOrganizer = GabrielOrganizer;
  module.exports.GabrielDaemon = GabrielDaemon;
  module.exports.GabrielPipeline = GabrielPipeline;
  module.exports.GabrielCodeProcessor = GabrielCodeProcessor;
  module.exports.GabrielCleanup = GabrielCleanup;
}

