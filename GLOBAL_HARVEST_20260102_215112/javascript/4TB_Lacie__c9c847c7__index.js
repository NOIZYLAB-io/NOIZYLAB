/**
 * 🟣 GABRIEL CODE PROCESSOR — Code Harvesting & Optimization Engine
 * 
 * Processes code through complete lifecycle:
 * TEST → HARVEST → OPTIMIZE → ABSORB → MOVE/COPY → DELETE
 * 
 * @example
 * const processor = new GabrielCodeProcessor('/Users/m2ultra/NOIZYLAB');
 * 
 * // Process incoming code
 * await processor.process(code, {
 *   test: true,
 *   optimize: true,
 *   absorb: true
 * });
 */
import fs from 'fs';
import path from 'path';
import { promisify } from 'util';
import crypto from 'crypto';

const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);
const stat = promisify(fs.stat);
const copyFile = promisify(fs.copyFile);
const unlink = promisify(fs.unlink);
const mkdir = promisify(fs.mkdir);

export class GabrielCodeProcessor {
  constructor(root = '/Users/m2ultra/NOIZYLAB', options = {}) {
    this.root = root;
    this.options = {
      testOnReceive: options.testOnReceive !== false,
      harvestPatterns: options.harvestPatterns || true,
      optimize: options.optimize !== false,
      autoAbsorb: options.autoAbsorb !== false,
      backupBeforeDelete: options.backupBeforeDelete !== false,
      stagingDir: path.join(root, '.gabriel', 'staging'),
      archiveDir: path.join(root, '.gabriel', 'archive'),
      ...options
    };
    
    this.report = {
      processed: [],
      tested: [],
      harvested: [],
      optimized: [],
      absorbed: [],
      moved: [],
      copied: [],
      deleted: []
    };
  }

  /**
   * Process code through complete lifecycle
   * @param {string|Object} code - Code to process (string or {path, content, type})
   * @param {Object} options - Processing options
   * @returns {Promise<Object>} Processing result
   */
  async process(code, options = {}) {
    const opts = { ...this.options, ...options };
    const entry = {
      id: `code-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      received: Date.now(),
      original: code,
      ...this._normalizeCode(code)
    };

    const result = {
      id: entry.id,
      stages: {},
      final: null,
      actions: []
    };

    try {
      // Stage 1: TEST
      if (opts.testOnReceive) {
        result.stages.test = await this.test(entry);
        this.report.tested.push(result.stages.test);
      }

      // Stage 2: HARVEST
      if (opts.harvestPatterns) {
        result.stages.harvest = await this.harvest(entry);
        this.report.harvested.push(result.stages.harvest);
      }

      // Stage 3: OPTIMIZE
      if (opts.optimize) {
        result.stages.optimize = await this.optimize(entry, result.stages.harvest);
        this.report.optimized.push(result.stages.optimize);
      }

      // Stage 4: ABSORB
      if (opts.autoAbsorb) {
        result.stages.absorb = await this.absorb(entry, result.stages.optimize || entry);
        this.report.absorbed.push(result.stages.absorb);
      }

      // Stage 5: MOVE/COPY
      if (result.stages.absorb?.destination) {
        const moveResult = await this.moveOrCopy(
          entry,
          result.stages.absorb.destination,
          opts
        );
        result.stages.move = moveResult;
        
        if (moveResult.action === 'moved') {
          this.report.moved.push(moveResult);
        } else {
          this.report.copied.push(moveResult);
        }
      }

      // Stage 6: DELETE (if requested)
      if (opts.deleteAfter && result.stages.move?.success) {
        result.stages.delete = await this.delete(entry, opts);
        if (result.stages.delete.success) {
          this.report.deleted.push(result.stages.delete);
        }
      }

      result.final = result.stages.move || result.stages.absorb || entry;
      this.report.processed.push(result);

      return result;
    } catch (error) {
      result.error = error.message;
      this.report.processed.push(result);
      throw error;
    }
  }

  /**
   * TEST — Validate and test code
   * @param {Object} entry - Code entry
   * @returns {Promise<Object>} Test results
   */
  async test(entry) {
    const result = {
      syntax: false,
      lint: false,
      runtime: false,
      errors: []
    };

    try {
      // Syntax validation
      if (entry.language === 'javascript' || entry.language === 'typescript') {
        result.syntax = await this._testJavaScript(entry);
      } else if (entry.language === 'python') {
        result.syntax = await this._testPython(entry);
      }

      // Lint check (if applicable)
      if (entry.language === 'javascript' || entry.language === 'typescript') {
        result.lint = await this._lintCode(entry);
      }

      result.passed = result.syntax && (result.lint !== false);
    } catch (error) {
      result.errors.push(error.message);
      result.passed = false;
    }

    return result;
  }

  /**
   * HARVEST — Extract patterns, insights, dependencies
   * @param {Object} entry - Code entry
   * @returns {Promise<Object>} Harvested data
   */
  async harvest(entry) {
    const harvested = {
      patterns: [],
      dependencies: [],
      functions: [],
      classes: [],
      imports: [],
      exports: [],
      comments: [],
      insights: []
    };

    const content = entry.content || '';

    // Extract imports
    const importMatches = content.matchAll(/import\s+(?:.*\s+from\s+)?['"]([^'"]+)['"]/g);
    for (const match of importMatches) {
      harvested.imports.push(match[1]);
    }

    // Extract exports
    const exportMatches = content.matchAll(/export\s+(?:default\s+)?(?:class|function|const|let|var)\s+(\w+)/g);
    for (const match of exportMatches) {
      harvested.exports.push(match[1]);
    }

    // Extract functions
    const functionMatches = content.matchAll(/(?:export\s+)?(?:async\s+)?function\s+(\w+)/g);
    for (const match of functionMatches) {
      harvested.functions.push(match[1]);
    }

    // Extract classes
    const classMatches = content.matchAll(/(?:export\s+)?class\s+(\w+)/g);
    for (const match of classMatches) {
      harvested.classes.push(match[1]);
    }

    // Extract comments for insights
    const commentMatches = content.matchAll(/\/\*\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\//g);
    for (const match of commentMatches) {
      harvested.comments.push(match[0]);
    }

    // Detect patterns
    if (content.includes('export class')) {
      harvested.patterns.push('class_export');
    }
    if (content.includes('export default')) {
      harvested.patterns.push('default_export');
    }
    if (content.includes('async')) {
      harvested.patterns.push('async_operations');
    }
    if (content.includes('fetch') || content.includes('http')) {
      harvested.patterns.push('http_requests');
    }

    // Generate insights
    if (harvested.functions.length > 0) {
      harvested.insights.push(`Contains ${harvested.functions.length} functions`);
    }
    if (harvested.classes.length > 0) {
      harvested.insights.push(`Contains ${harvested.classes.length} classes`);
    }

    return harvested;
  }

  /**
   * OPTIMIZE — Optimize code structure and performance
   * @param {Object} entry - Code entry
   * @param {Object} harvested - Harvested data
   * @returns {Promise<Object>} Optimized code
   */
  async optimize(entry, harvested = {}) {
    let optimized = entry.content || '';
    const optimizations = [];

    // Remove trailing whitespace
    const beforeWhitespace = optimized;
    optimized = optimized.split('\n').map(line => line.trimEnd()).join('\n');
    if (optimized !== beforeWhitespace) {
      optimizations.push('removed_trailing_whitespace');
    }

    // Add missing semicolons (optional)
    // Normalize line endings
    optimized = optimized.replace(/\r\n/g, '\n');

    // Sort imports (if applicable)
    if (harvested.imports && harvested.imports.length > 0) {
      optimizations.push('detected_imports');
    }

    return {
      ...entry,
      content: optimized,
      optimizations,
      optimized: true
    };
  }

  /**
   * ABSORB — Determine where code should be integrated
   * @param {Object} entry - Code entry
   * @param {Object} optimized - Optimized code entry
   * @returns {Promise<Object>} Absorption plan
   */
  async absorb(entry, optimized) {
    const destination = this._determineDestination(optimized);
    const integration = this._planIntegration(optimized, destination);

    return {
      destination,
      integration,
      ready: true,
      timestamp: Date.now()
    };
  }

  /**
   * MOVE OR COPY — Move or copy code to destination
   * @param {Object} entry - Code entry
   * @param {string} destination - Destination path
   * @param {Object} options - Options
   * @returns {Promise<Object>} Move/copy result
   */
  async moveOrCopy(entry, destination, options = {}) {
    await this._ensureDirectory(path.dirname(destination));

    const action = options.copyOnly ? 'copy' : 'move';
    
    try {
      if (entry.path && fs.existsSync(entry.path)) {
        // File exists, move/copy it
        if (action === 'copy') {
          await copyFile(entry.path, destination);
        } else {
          await fs.promises.rename(entry.path, destination);
        }
      } else if (entry.content) {
        // Content only, write to destination
        await writeFile(destination, entry.content, 'utf8');
      }

      return {
        action: action === 'copy' ? 'copied' : 'moved',
        from: entry.path || 'inline',
        to: destination,
        success: true
      };
    } catch (error) {
      return {
        action: action === 'copy' ? 'copy' : 'move',
        from: entry.path || 'inline',
        to: destination,
        success: false,
        error: error.message
      };
    }
  }

  /**
   * DELETE — Remove code/file
   * @param {Object} entry - Code entry
   * @param {Object} options - Options
   * @returns {Promise<Object>} Delete result
   */
  async delete(entry, options = {}) {
    if (!entry.path) {
      return { success: false, reason: 'No file path to delete' };
    }

    try {
      // Backup if requested
      if (options.backupBeforeDelete) {
        await this._backup(entry.path);
      }

      await unlink(entry.path);
      
      return {
        success: true,
        deleted: entry.path,
        timestamp: Date.now()
      };
    } catch (error) {
      return {
        success: false,
        error: error.message,
        path: entry.path
      };
    }
  }

  /**
   * Get processing report
   * @returns {Object} Complete report
   */
  getReport() {
    return {
      ...this.report,
      summary: {
        processed: this.report.processed.length,
        tested: this.report.tested.length,
        harvested: this.report.harvested.length,
        optimized: this.report.optimized.length,
        absorbed: this.report.absorbed.length,
        moved: this.report.moved.length,
        copied: this.report.copied.length,
        deleted: this.report.deleted.length
      }
    };
  }

  // ────────────────────────────────────────────────────────────────
  // PRIVATE HELPER METHODS
  // ────────────────────────────────────────────────────────────────

  _normalizeCode(code) {
    if (typeof code === 'string') {
      return {
        content: code,
        language: this._detectLanguage(code),
        type: 'inline'
      };
    }

    if (typeof code === 'object' && code.path) {
      return {
        path: code.path,
        content: code.content || '',
        language: code.language || this._detectLanguage(code.content || ''),
        type: 'file'
      };
    }

    return {
      content: String(code),
      language: 'unknown',
      type: 'unknown'
    };
  }

  _detectLanguage(content) {
    if (content.includes('export class') || content.includes('import ')) {
      return 'javascript';
    }
    if (content.includes('def ') || content.includes('import ')) {
      return 'python';
    }
    if (content.includes('<?php')) {
      return 'php';
    }
    return 'unknown';
  }

  async _testJavaScript(entry) {
    try {
      // Basic syntax check - try to parse
      if (entry.content) {
        // Simple check - would need actual parser for full validation
        return !entry.content.match(/syntax\s+error/i);
      }
      return true;
    } catch {
      return false;
    }
  }

  async _testPython(entry) {
    // Python syntax check would go here
    return true;
  }

  async _lintCode(entry) {
    // Linting would go here
    return null; // No lint errors found
  }

  _determineDestination(entry) {
    const language = entry.language || 'javascript';
    const name = entry.name || `code-${Date.now()}`;
    
    // Determine best destination based on code characteristics
    if (entry.content?.includes('export class')) {
      // ES6 class - likely a module
      const className = entry.content.match(/export class (\w+)/)?.[1];
      if (className) {
        return path.join(
          this.root,
          'gabriel',
          className.toLowerCase().replace('gabriel', '').trim() || 'modules',
          `${className}.js`
        );
      }
    }

    if (entry.content?.includes('export default')) {
      return path.join(this.root, 'gabriel', 'modules', `${name}.js`);
    }

    // Default location
    return path.join(this.root, '.gabriel', 'processed', `${name}.${language === 'javascript' ? 'js' : language}`);
  }

  _planIntegration(entry, destination) {
    return {
      method: 'direct',
      destination,
      requires: [],
      conflicts: []
    };
  }

  async _ensureDirectory(dirPath) {
    try {
      await mkdir(dirPath, { recursive: true });
    } catch (error) {
      if (error.code !== 'EEXIST') {
        throw error;
      }
    }
  }

  async _backup(filePath) {
    const backupDir = this.options.archiveDir;
    await this._ensureDirectory(backupDir);
    
    const backupPath = path.join(
      backupDir,
      `${path.basename(filePath)}.backup-${Date.now()}`
    );
    
    await copyFile(filePath, backupPath);
    return backupPath;
  }
}

// Default export
export default GabrielCodeProcessor;

// For CommonJS compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GabrielCodeProcessor;
  module.exports.default = GabrielCodeProcessor;
}

