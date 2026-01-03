import fs from 'fs';
import path from 'path';
import { promisify } from 'util';

const readdir = promisify(fs.readdir);
const stat = promisify(fs.stat);
const rmdir = promisify(fs.rmdir);
const unlink = promisify(fs.unlink);

/**
 * GABRIEL CLEANUP — Delete Empty Folders
 * 
 * Recursively finds and deletes empty directories
 * 
 * @example
 * const cleanup = new GabrielCleanup('/Users/m2ultra/NOIZYLAB');
 * const deleted = await cleanup.deleteEmptyFolders();
 */
export class GabrielCleanup {
  constructor(root = '/Users/m2ultra/NOIZYLAB', options = {}) {
    this.root = root;
    this.options = {
      dryRun: options.dryRun || false,
      excludePatterns: options.excludePatterns || [
        'node_modules',
        '.git',
        '.DS_Store',
        'dist',
        'build'
      ],
      includeHidden: options.includeHidden || false,
      ...options
    };
    
    this.report = {
      scanned: 0,
      empty: [],
      deleted: [],
      errors: []
    };
  }

  /**
   * Delete all empty folders
   * @returns {Promise<Object>} Cleanup report
   */
  async deleteEmptyFolders() {
    this.report = {
      scanned: 0,
      empty: [],
      deleted: [],
      errors: []
    };

    console.log('🧹 GABRIEL CLEANUP - Deleting Empty Folders');
    console.log('='.repeat(60));
    console.log(`📂 Root: ${this.root}`);
    console.log(`🔍 Mode: ${this.options.dryRun ? 'DRY RUN' : 'LIVE'}\n`);

    await this._scanAndDelete(this.root);

    console.log(`\n✅ Cleanup Complete!`);
    console.log(`   Scanned: ${this.report.scanned} directories`);
    console.log(`   Empty found: ${this.report.empty.length}`);
    console.log(`   Deleted: ${this.report.deleted.length}`);
    console.log(`   Errors: ${this.report.errors.length}`);

    return this.report;
  }

  /**
   * Recursively scan and delete empty folders
   * @private
   */
  async _scanAndDelete(dir, depth = 0) {
    // Skip excluded patterns
    const dirName = path.basename(dir);
    
    if (!this.options.includeHidden && dirName.startsWith('.')) {
      return;
    }

    if (this.options.excludePatterns.some(pattern => {
      if (typeof pattern === 'string') {
        return dir.includes(pattern) || dirName === pattern;
      }
      return false;
    })) {
      return;
    }

    try {
      const items = await readdir(dir);
      
      // Recursively process subdirectories first
      for (const item of items) {
        const fullPath = path.join(dir, item);
        
        try {
          const stat = await fs.promises.stat(fullPath);
          
          if (stat.isDirectory()) {
            await this._scanAndDelete(fullPath, depth + 1);
          }
        } catch (error) {
          // Skip items we can't stat
        }
      }

      // Check if directory is now empty
      this.report.scanned++;
      const currentItems = await readdir(dir);
      
      if (currentItems.length === 0) {
        this.report.empty.push(dir);
        
        // Don't delete root directory
        if (dir === this.root) {
          return;
        }

        if (!this.options.dryRun) {
          try {
            await rmdir(dir);
            this.report.deleted.push(dir);
            console.log(`🗑️  Deleted: ${dir}`);
          } catch (error) {
            this.report.errors.push({
              path: dir,
              error: error.message
            });
          }
        } else {
          console.log(`🔍 Would delete: ${dir}`);
        }
      }
    } catch (error) {
      // Directory might have been deleted already, or permission error
      this.report.errors.push({
        path: dir,
        error: error.message
      });
    }
  }

  /**
   * Find all empty folders without deleting
   * @returns {Promise<Array>} List of empty folder paths
   */
  async findEmptyFolders() {
    const tempOptions = { ...this.options, dryRun: true };
    const tempCleanup = new GabrielCleanup(this.root, tempOptions);
    await tempCleanup.deleteEmptyFolders();
    return tempCleanup.report.empty;
  }

  /**
   * Get cleanup report
   * @returns {Object} Report
   */
  getReport() {
    return this.report;
  }
}

// Default export
export default GabrielCleanup;

// For CommonJS compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GabrielCleanup;
  module.exports.default = GabrielCleanup;
}

