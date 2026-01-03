import fs from 'fs';
import path from 'path';
import { promisify } from 'util';

const readdir = promisify(fs.readdir);
const statAsync = promisify(fs.stat);

/**
 * GABRIEL SCANNER — File Crawler + Classifier
 * 
 * Comprehensive file system scanner with intelligent classification
 * Supports both Node.js and Cloudflare Workers (limited)
 * 
 * @example
 * const scanner = new GabrielScanner('/path/to/scan');
 * const index = await scanner.scan();
 */
export class GabrielScanner {
  constructor(root, options = {}) {
    this.root = root || process.cwd();
    this.index = [];
    this.options = {
      maxDepth: options.maxDepth || Infinity,
      includeHidden: options.includeHidden || false,
      excludePatterns: options.excludePatterns || [
        'node_modules',
        '.git',
        '.DS_Store',
        'dist',
        'build'
      ],
      includePatterns: options.includePatterns || null,
      ...options
    };
    this.stats = {
      files: 0,
      directories: 0,
      errors: 0,
      startTime: null,
      endTime: null
    };
  }

  /**
   * Scan the root directory and build index
   * @returns {Promise<Array>} Array of indexed file/directory entries
   */
  async scan() {
    this.index = [];
    this.stats.files = 0;
    this.stats.directories = 0;
    this.stats.errors = 0;
    this.stats.startTime = Date.now();

    try {
      await this.walk(this.root, 0);
      this.stats.endTime = Date.now();
      return this.index;
    } catch (error) {
      console.error('Scan error:', error);
      this.stats.errors++;
      throw error;
    }
  }

  /**
   * Recursively walk directory tree
   * @private
   */
  async walk(dir, depth = 0) {
    // Check depth limit
    if (depth > this.options.maxDepth) {
      return;
    }

    // Check if directory should be excluded
    const dirName = path.basename(dir);
    if (!this.options.includeHidden && dirName.startsWith('.')) {
      return;
    }

    if (this.options.excludePatterns.some(pattern => {
      if (typeof pattern === 'string') {
        return dir.includes(pattern) || dirName === pattern;
      }
      if (pattern instanceof RegExp) {
        return pattern.test(dir);
      }
      return false;
    })) {
      return;
    }

    try {
      const items = await readdir(dir);

      for (const item of items) {
        const fullPath = path.join(dir, item);

        // Skip hidden files if not including them
        if (!this.options.includeHidden && item.startsWith('.')) {
          continue;
        }

        try {
          const stat = await statAsync(fullPath);

          if (stat.isDirectory()) {
            this.stats.directories++;
            
            // Add directory to index
            this.index.push({
              path: fullPath,
              type: 'directory',
              size: 0,
              extension: null,
              mtime: stat.mtime,
              ctime: stat.ctime,
              depth
            });

            // Recursively walk subdirectory
            await this.walk(fullPath, depth + 1);
          } else if (stat.isFile()) {
            this.stats.files++;
            
            const ext = path.extname(item).toLowerCase();
            const classification = this.classify(fullPath, ext);

            this.index.push({
              path: fullPath,
              type: 'file',
              size: stat.size,
              extension: ext || null,
              classification,
              mtime: stat.mtime,
              ctime: stat.ctime,
              depth,
              name: item
            });
          } else if (stat.isSymbolicLink()) {
            // Handle symlinks
            this.index.push({
              path: fullPath,
              type: 'symlink',
              size: 0,
              extension: null,
              mtime: stat.mtime,
              depth
            });
          }
        } catch (error) {
          // Handle permission errors or broken symlinks
          this.stats.errors++;
          if (this.options.onError) {
            this.options.onError(fullPath, error);
          }
        }
      }
    } catch (error) {
      this.stats.errors++;
      if (this.options.onError) {
        this.options.onError(dir, error);
      }
    }
  }

  /**
   * Classify file by extension and path patterns
   * @private
   */
  classify(filePath, ext) {
    const fileName = path.basename(filePath).toLowerCase();
    const dirName = path.dirname(filePath).toLowerCase();

    // Audio files
    const audioExts = ['.wav', '.aiff', '.aif', '.mp3', '.flac', '.ogg', '.m4a', '.aac', '.wma', '.opus'];
    if (audioExts.includes(ext)) return 'audio';

    // Video files
    const videoExts = ['.mov', '.mp4', '.avi', '.mkv', '.webm', '.flv', '.wmv', '.m4v', '.3gp', '.mpg', '.mpeg'];
    if (videoExts.includes(ext)) return 'video';

    // Image files
    const imageExts = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.tiff', '.ico', '.heic', '.heif'];
    if (imageExts.includes(ext)) return 'image';

    // Code files
    const codeExts = [
      '.js', '.ts', '.jsx', '.tsx', '.py', '.java', '.cpp', '.c', '.h', '.hpp',
      '.cs', '.go', '.rs', '.rb', '.php', '.swift', '.kt', '.scala', '.clj',
      '.json', '.yaml', '.yml', '.xml', '.html', '.css', '.scss', '.sass',
      '.sh', '.bash', '.zsh', '.fish', '.ps1', '.bat', '.cmd',
      '.sql', '.r', '.m', '.matlab', '.lua', '.vim', '.vimrc'
    ];
    if (codeExts.includes(ext)) return 'code';

    // Documentation
    const docExts = ['.md', '.txt', '.rtf', '.doc', '.docx', '.pdf', '.pages'];
    if (docExts.includes(ext)) return 'document';

    // Archive/Compressed
    const archiveExts = ['.zip', '.tar', '.gz', '.bz2', '.xz', '.7z', '.rar', '.dmg', '.iso'];
    if (archiveExts.includes(ext)) return 'archive';

    // Data files
    const dataExts = ['.csv', '.tsv', '.db', '.sqlite', '.sqlite3', '.xls', '.xlsx'];
    if (dataExts.includes(ext)) return 'data';

    // Fonts
    const fontExts = ['.ttf', '.otf', '.woff', '.woff2', '.eot'];
    if (fontExts.includes(ext)) return 'font';

    // Configuration
    const configExts = ['.config', '.conf', '.ini', '.cfg', '.toml', '.env'];
    if (configExts.includes(ext) || fileName.match(/^\.(config|conf|env|gitconfig|npmrc)/)) {
      return 'config';
    }

    // Project files
    if (fileName.match(/^(package\.json|composer\.json|pom\.xml|build\.gradle|requirements\.txt|Gemfile|Cargo\.toml)$/)) {
      return 'project';
    }

    // By directory patterns
    if (dirName.includes('/node_modules') || dirName.includes('\\node_modules')) return 'dependency';
    if (dirName.includes('/.git') || dirName.includes('\\.git')) return 'git';
    if (dirName.includes('/dist') || dirName.includes('\\dist')) return 'build';
    if (dirName.includes('/build') || dirName.includes('\\build')) return 'build';
    if (dirName.includes('/test') || dirName.includes('\\test')) return 'test';
    if (dirName.includes('/tests') || dirName.includes('\\tests')) return 'test';

    return 'other';
  }

  /**
   * Get scan statistics
   * @returns {Object} Statistics about the scan
   */
  getStats() {
    const duration = this.stats.endTime && this.stats.startTime 
      ? this.stats.endTime - this.stats.startTime 
      : null;

    return {
      ...this.stats,
      duration,
      indexed: this.index.length,
      byType: this.groupByType(),
      byClassification: this.groupByClassification()
    };
  }

  /**
   * Group files by type (file/directory)
   * @private
   */
  groupByType() {
    return this.index.reduce((acc, item) => {
      acc[item.type] = (acc[item.type] || 0) + 1;
      return acc;
    }, {});
  }

  /**
   * Group files by classification
   * @private
   */
  groupByClassification() {
    return this.index
      .filter(item => item.classification)
      .reduce((acc, item) => {
        acc[item.classification] = (acc[item.classification] || 0) + 1;
        return acc;
      }, {});
  }

  /**
   * Filter index by classification
   * @param {string} classification - Classification to filter by
   * @returns {Array} Filtered entries
   */
  filterByClassification(classification) {
    return this.index.filter(item => item.classification === classification);
  }

  /**
   * Filter index by type
   * @param {string} type - Type to filter by (file/directory)
   * @returns {Array} Filtered entries
   */
  filterByType(type) {
    return this.index.filter(item => item.type === type);
  }

  /**
   * Find files by extension
   * @param {string|Array} extensions - Extension(s) to find
   * @returns {Array} Matching entries
   */
  findByExtension(extensions) {
    const exts = Array.isArray(extensions) ? extensions : [extensions];
    return this.index.filter(item => 
      item.extension && exts.includes(item.extension.toLowerCase())
    );
  }

  /**
   * Search by path pattern (regex or string)
   * @param {string|RegExp} pattern - Pattern to match
   * @returns {Array} Matching entries
   */
  search(pattern) {
    const regex = typeof pattern === 'string' 
      ? new RegExp(pattern, 'i') 
      : pattern;
    
    return this.index.filter(item => regex.test(item.path));
  }

  /**
   * Export index to JSON
   * @returns {string} JSON string
   */
  toJSON() {
    return JSON.stringify({
      root: this.root,
      scanned: new Date().toISOString(),
      stats: this.getStats(),
      index: this.index
    }, null, 2);
  }
}

// Default export
export default GabrielScanner;

// For CommonJS compatibility (if needed)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GabrielScanner;
  module.exports.default = GabrielScanner;
}

