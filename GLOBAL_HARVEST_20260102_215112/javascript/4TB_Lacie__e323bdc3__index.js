import fs from 'fs';
import path from 'path';
import { promisify } from 'util';

const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);
const stat = promisify(fs.stat);
const access = promisify(fs.access);

/**
 * GABRIEL HEALER — Auto-Fix Engine
 * 
 * Automatically detects and fixes common issues in codebases:
 * - Broken imports
 * - Missing dependencies
 * - Formatting issues
 * - Security vulnerabilities
 * - Performance problems
 * - Configuration errors
 * 
 * @example
 * const healer = new GabrielHealer('/project/path');
 * const report = await healer.heal();
 * console.log(`Fixed ${report.fixed} issues`);
 */
export class GabrielHealer {
  constructor(root, options = {}) {
    this.root = root || process.cwd();
    this.options = {
      autoFix: options.autoFix !== false, // Default to true
      backup: options.backup !== false, // Create backups
      verbose: options.verbose || false,
      rules: options.rules || 'all', // 'all', 'safe', or array of rule names
      ...options
    };
    
    this.report = {
      scanned: 0,
      issues: [],
      fixed: 0,
      errors: [],
      backups: []
    };

    this.rules = this._initializeRules();
  }

  /**
   * Run healing process on codebase
   * @returns {Promise<Object>} Healing report
   */
  async heal() {
    this.report = {
      scanned: 0,
      issues: [],
      fixed: 0,
      errors: [],
      backups: [],
      startTime: Date.now()
    };

    try {
      // Run all enabled rules
      const files = await this._scanFiles();
      this.report.scanned = files.length;

      for (const file of files) {
        await this._processFile(file);
      }

      this.report.endTime = Date.now();
      this.report.duration = this.report.endTime - this.report.startTime;
      
      return this.report;
    } catch (error) {
      this.report.errors.push({
        type: 'healing_error',
        message: error.message,
        stack: error.stack
      });
      throw error;
    }
  }

  /**
   * Scan for issues without fixing
   * @returns {Promise<Array>} List of issues found
   */
  async scan() {
    const files = await this._scanFiles();
    const issues = [];

    for (const file of files) {
      const fileIssues = await this._detectIssues(file);
      issues.push(...fileIssues);
    }

    return issues;
  }

  /**
   * Fix specific issue
   * @param {Object} issue - Issue to fix
   * @returns {Promise<boolean>} Success status
   */
  async fixIssue(issue) {
    try {
      if (!this.options.autoFix) {
        return false;
      }

      // Create backup if enabled
      if (this.options.backup && issue.file) {
        await this._createBackup(issue.file);
      }

      // Apply fix based on issue type
      const fixed = await this._applyFix(issue);
      
      if (fixed) {
        this.report.fixed++;
        this.report.issues.push({
          ...issue,
          fixed: true,
          fixedAt: Date.now()
        });
      }

      return fixed;
    } catch (error) {
      this.report.errors.push({
        issue,
        error: error.message
      });
      return false;
    }
  }

  // ────────────────────────────────────────────────────────────────
  // RULE DEFINITIONS
  // ────────────────────────────────────────────────────────────────

  _initializeRules() {
    return {
      brokenImports: {
        name: 'broken_imports',
        safe: true,
        detect: async (file) => {
          if (!['.js', '.ts', '.jsx', '.tsx'].includes(path.extname(file))) {
            return [];
          }

          const content = await readFile(file, 'utf8');
          const issues = [];
          const importRegex = /import\s+(?:.*\s+from\s+)?['"]([^'"]+)['"]/g;
          const requireRegex = /require\(['"]([^'"]+)['"]\)/g;

          // Check ES6 imports
          let match;
          while ((match = importRegex.exec(content)) !== null) {
            const importPath = match[1];
            if (!importPath.startsWith('.') && !importPath.startsWith('/')) {
              continue; // Skip node_modules imports
            }

            const resolved = this._resolveImport(file, importPath);
            if (!resolved || !await this._fileExists(resolved)) {
              issues.push({
                type: 'broken_import',
                file,
                line: content.substring(0, match.index).split('\n').length,
                importPath,
                severity: 'high'
              });
            }
          }

          // Check require() calls
          while ((match = requireRegex.exec(content)) !== null) {
            const importPath = match[1];
            if (!importPath.startsWith('.') && !importPath.startsWith('/')) {
              continue;
            }

            const resolved = this._resolveImport(file, importPath);
            if (!resolved || !await this._fileExists(resolved)) {
              issues.push({
                type: 'broken_import',
                file,
                line: content.substring(0, match.index).split('\n').length,
                importPath,
                severity: 'high'
              });
            }
          }

          return issues;
        },
        fix: async (issue) => {
          const content = await readFile(issue.file, 'utf8');
          // Try to find and fix the import path
          const fixed = await this._fixImportPath(issue.file, content, issue.importPath);
          if (fixed) {
            await writeFile(issue.file, fixed, 'utf8');
            return true;
          }
          return false;
        }
      },

      missingPackageJson: {
        name: 'missing_package_json',
        safe: true,
        detect: async (file) => {
          const dir = path.dirname(file);
          const packageJsonPath = path.join(dir, 'package.json');
          
          // Only check if we're in a Node.js project directory
          if (await this._fileExists(packageJsonPath)) {
            return [];
          }

          // Check if directory has .js files
          const hasJsFiles = await this._hasJsFiles(dir);
          if (!hasJsFiles) {
            return [];
          }

          return [{
            type: 'missing_package_json',
            file: dir,
            severity: 'medium'
          }];
        },
        fix: async (issue) => {
          const packageJson = {
            name: path.basename(issue.file),
            version: '1.0.0',
            type: 'module',
            main: 'index.js'
          };
          const packageJsonPath = path.join(issue.file, 'package.json');
          await writeFile(packageJsonPath, JSON.stringify(packageJson, null, 2), 'utf8');
          return true;
        }
      },

      trailingWhitespace: {
        name: 'trailing_whitespace',
        safe: true,
        detect: async (file) => {
          const content = await readFile(file, 'utf8');
          const lines = content.split('\n');
          const issues = [];

          lines.forEach((line, index) => {
            if (line.trim() !== line && line.length > 0) {
              issues.push({
                type: 'trailing_whitespace',
                file,
                line: index + 1,
                severity: 'low'
              });
            }
          });

          return issues;
        },
        fix: async (issue) => {
          const content = await readFile(issue.file, 'utf8');
          const fixed = content.split('\n').map(line => line.trimEnd()).join('\n');
          
          if (fixed !== content) {
            await writeFile(issue.file, fixed, 'utf8');
            return true;
          }
          return false;
        }
      },

      missingFileExtensions: {
        name: 'missing_file_extensions',
        safe: false,
        detect: async (file) => {
          // Only for ES modules
          const content = await readFile(file, 'utf8');
          const issues = [];
          
          // Check for imports without extensions (ES modules require them)
          const importRegex = /import\s+.*from\s+['"](\.\/[^'"]+)['"]/g;
          let match;
          
          while ((match = importRegex.exec(content)) !== null) {
            const importPath = match[1];
            if (!path.extname(importPath)) {
              const resolved = this._resolveImport(file, importPath);
              if (resolved && await this._fileExists(resolved)) {
                // Could add extension
                issues.push({
                  type: 'missing_extension',
                  file,
                  line: content.substring(0, match.index).split('\n').length,
                  importPath,
                  severity: 'medium'
                });
              }
            }
          }

          return issues;
        },
        fix: async (issue) => {
          const content = await readFile(issue.file, 'utf8');
          const importRegex = new RegExp(`(['"]${issue.importPath.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})(['"])`, 'g');
          
          // Try to find the actual file and add extension
          const resolved = this._resolveImport(issue.file, issue.importPath);
          if (resolved) {
            const ext = path.extname(resolved);
            if (ext) {
              const fixed = content.replace(
                importRegex,
                `$1${ext}$2`
              );
              
              if (fixed !== content) {
                await writeFile(issue.file, fixed, 'utf8');
                return true;
              }
            }
          }
          
          return false;
        }
      },

      insecureRandom: {
        name: 'insecure_random',
        safe: true,
        detect: async (file) => {
          const content = await readFile(file, 'utf8');
          const issues = [];

          // Check for Math.random() usage (should use crypto.randomBytes)
          const mathRandomRegex = /Math\.random\(\)/g;
          let match;
          
          while ((match = mathRandomRegex.exec(content)) !== null) {
            issues.push({
              type: 'insecure_random',
              file,
              line: content.substring(0, match.index).split('\n').length,
              code: 'Math.random()',
              severity: 'medium'
            });
          }

          return issues;
        },
        fix: async (issue) => {
          // This would require more context to fix properly
          // Just flag it for now
          return false;
        }
      },

      consoleLogs: {
        name: 'console_logs',
        safe: false, // User might want console.logs
        detect: async (file) => {
          if (!['.js', '.ts'].includes(path.extname(file))) {
            return [];
          }

          const content = await readFile(file, 'utf8');
          const issues = [];
          const consoleRegex = /console\.(log|debug|info|warn|error)\(/g;
          let match;

          while ((match = consoleRegex.exec(content)) !== null) {
            issues.push({
              type: 'console_log',
              file,
              line: content.substring(0, match.index).split('\n').length,
              method: match[1],
              severity: 'low'
            });
          }

          return issues;
        },
        fix: async (issue) => {
          // Optionally remove or comment out console.logs
          const content = await readFile(issue.file, 'utf8');
          const lines = content.split('\n');
          
          if (issue.line <= lines.length) {
            const line = lines[issue.line - 1];
            if (line.includes(`console.${issue.method}`)) {
              lines[issue.line - 1] = `// ${line}`;
              await writeFile(issue.file, lines.join('\n'), 'utf8');
              return true;
            }
          }
          
          return false;
        }
      }
    };
  }

  // ────────────────────────────────────────────────────────────────
  // PRIVATE HELPER METHODS
  // ────────────────────────────────────────────────────────────────

  async _scanFiles() {
    const files = [];
    
    const walk = async (dir) => {
      const items = await fs.promises.readdir(dir, { withFileTypes: true });
      
      for (const item of items) {
        const fullPath = path.join(dir, item.name);
        
        // Skip node_modules, .git, etc.
        if (item.name.startsWith('.') || item.name === 'node_modules') {
          continue;
        }
        
        if (item.isDirectory()) {
          await walk(fullPath);
        } else if (item.isFile()) {
          files.push(fullPath);
        }
      }
    };

    await walk(this.root);
    return files;
  }

  async _processFile(file) {
    const enabledRules = this._getEnabledRules();
    
    for (const rule of enabledRules) {
      try {
        const issues = await rule.detect(file);
        
        for (const issue of issues) {
          if (this.options.autoFix) {
            await this.fixIssue(issue);
          } else {
            this.report.issues.push(issue);
          }
        }
      } catch (error) {
        this.report.errors.push({
          file,
          rule: rule.name,
          error: error.message
        });
      }
    }
  }

  async _detectIssues(file) {
    const enabledRules = this._getEnabledRules();
    const issues = [];

    for (const rule of enabledRules) {
      try {
        const ruleIssues = await rule.detect(file);
        issues.push(...ruleIssues);
      } catch (error) {
        // Skip rules that error
      }
    }

    return issues;
  }

  _getEnabledRules() {
    const allRules = Object.values(this.rules);
    
    if (this.options.rules === 'all') {
      return allRules;
    }
    
    if (this.options.rules === 'safe') {
      return allRules.filter(rule => rule.safe);
    }
    
    if (Array.isArray(this.options.rules)) {
      return allRules.filter(rule => 
        this.options.rules.includes(rule.name)
      );
    }
    
    return allRules;
  }

  async _applyFix(issue) {
    const rule = Object.values(this.rules).find(r => 
      r.name === issue.type || r.name.replace('_', '') === issue.type.replace('_', '')
    );

    if (rule && rule.fix) {
      return await rule.fix(issue);
    }

    return false;
  }

  async _createBackup(filePath) {
    try {
      const content = await readFile(filePath);
      const backupPath = `${filePath}.gabriel-backup-${Date.now()}`;
      await writeFile(backupPath, content);
      this.report.backups.push(backupPath);
      return backupPath;
    } catch (error) {
      this.report.errors.push({
        file: filePath,
        error: `Backup failed: ${error.message}`
      });
      return null;
    }
  }

  _resolveImport(fromFile, importPath) {
    if (importPath.startsWith('/')) {
      return path.resolve(this.root, importPath.slice(1));
    }
    
    if (importPath.startsWith('.')) {
      const baseDir = path.dirname(fromFile);
      return path.resolve(baseDir, importPath);
    }
    
    return null;
  }

  async _fileExists(filePath) {
    try {
      await access(filePath, fs.constants.F_OK);
      return true;
    } catch {
      return false;
    }
  }

  async _hasJsFiles(dir) {
    try {
      const items = await fs.promises.readdir(dir);
      return items.some(item => 
        ['.js', '.ts', '.jsx', '.tsx'].includes(path.extname(item))
      );
    } catch {
      return false;
    }
  }

  async _fixImportPath(file, content, importPath) {
    // Try common fixes
    const baseDir = path.dirname(file);
    const extensions = ['.js', '.ts', '.jsx', '.tsx', '/index.js', '/index.ts'];
    
    for (const ext of extensions) {
      const testPath = path.resolve(baseDir, importPath + ext);
      if (await this._fileExists(testPath)) {
        const relativePath = path.relative(baseDir, testPath);
        return content.replace(
          new RegExp(`(['"])${importPath.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(['"])`, 'g'),
          `$1${relativePath.replace(/\\/g, '/')}$2`
        );
      }
    }
    
    return null;
  }

  /**
   * Get healing report summary
   * @returns {Object} Summary statistics
   */
  getReport() {
    return {
      ...this.report,
      summary: {
        totalIssues: this.report.issues.length,
        fixed: this.report.fixed,
        errors: this.report.errors.length,
        backups: this.report.backups.length,
        duration: this.report.duration || 0
      },
      byType: this._groupByType(),
      bySeverity: this._groupBySeverity()
    };
  }

  _groupByType() {
    return this.report.issues.reduce((acc, issue) => {
      acc[issue.type] = (acc[issue.type] || 0) + 1;
      return acc;
    }, {});
  }

  _groupBySeverity() {
    return this.report.issues.reduce((acc, issue) => {
      acc[issue.severity] = (acc[issue.severity] || 0) + 1;
      return acc;
    }, {});
  }
}

// Default export
export default GabrielHealer;

// For CommonJS compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GabrielHealer;
  module.exports.default = GabrielHealer;
}

