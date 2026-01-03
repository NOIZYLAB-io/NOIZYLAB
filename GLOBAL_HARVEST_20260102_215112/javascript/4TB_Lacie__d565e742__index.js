import fs from 'fs';
import path from 'path';
import { promisify } from 'util';

const exists = promisify(fs.exists);
const mkdir = promisify(fs.mkdir);
const rename = promisify(fs.rename);

/**
 * GABRIEL ORGANIZER — File Organization Engine
 * 
 * Automatically organizes files into structured directories based on type.
 * 
 * @example
 * const organizer = new GabrielOrganizer('/project/path');
 * organizer.ensureStructure();
 * const result = organizer.organize(files);
 */
export class GabrielOrganizer {
  constructor(root, options = {}) {
    this.root = root || process.cwd();
    this.options = {
      structure: options.structure || {
        audio: ['audio', 'music', 'sounds'],
        code: ['code', 'src', 'scripts'],
        images: ['images', 'img', 'photos'],
        video: ['video', 'videos', 'media'],
        documents: ['documents', 'docs'],
        archives: ['archives', 'zips'],
        data: ['data', 'databases'],
        other: ['other', 'misc']
      },
      createStructure: options.createStructure !== false,
      dryRun: options.dryRun || false,
      conflictStrategy: options.conflictStrategy || 'rename', // 'rename', 'skip', 'overwrite'
      ...options
    };
    
    this.report = {
      organized: 0,
      skipped: 0,
      errors: [],
      moves: []
    };
  }

  /**
   * Ensure directory structure exists (synchronous)
   */
  ensureStructure() {
    if (!this.options.createStructure) {
      return;
    }

    const folders = Object.keys(this.options.structure);
    
    folders.forEach((folder) => {
      const folderPath = path.join(this.root, folder);
      if (!fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath, { recursive: true });
      }
    });
  }

  /**
   * Move file to appropriate folder based on type
   * @param {string} file - File path
   * @param {string} type - File type/classification
   * @returns {Promise<string|null>} New file path or null if skipped
   */
  async moveFile(file, type) {
    if (this.options.dryRun) {
      const newPath = this._getDestinationPath(file, type);
      return newPath;
    }

    try {
      const newPath = await this._moveFileSafe(file, type);
      this.report.organized++;
      this.report.moves.push({
        from: file,
        to: newPath,
        type
      });
      return newPath;
    } catch (error) {
      this.report.errors.push({
        file,
        type,
        error: error.message
      });
      this.report.skipped++;
      return null;
    }
  }

  /**
   * Move file (synchronous version)
   * @param {string} file - File path
   * @param {string} type - File type/classification
   * @returns {string} New file path
   */
  moveFile(file, type) {
    const newPath = path.join(this.root, type, path.basename(file));
    
    try {
      fs.renameSync(file, newPath);
      return newPath;
    } catch (error) {
      // Handle case where destination exists
      if (error.code === 'EEXIST' || error.code === 'ENOENT') {
        const resolvedPath = this._resolveConflict(file, newPath);
        if (resolvedPath) {
          fs.renameSync(file, resolvedPath);
          return resolvedPath;
        }
      }
      throw error;
    }
  }

  /**
   * Organize array of files
   * @param {Array} files - Array of file objects with {path, type} or {path, classification}
   * @returns {Promise<Array>} Array of move operations
   */
  async organize(files) {
    this.report = {
      organized: 0,
      skipped: 0,
      errors: [],
      moves: []
    };

    await this.ensureStructure();

    const results = [];

    for (const file of files) {
      const filePath = file.path || file;
      const fileType = file.type || file.classification || 'other';
      
      // Map classification to folder name
      const folder = this._mapTypeToFolder(fileType);
      
      const newPath = await this.moveFile(filePath, folder);
      
      results.push({
        from: filePath,
        to: newPath,
        type: fileType,
        folder,
        success: newPath !== null
      });
    }

    return results;
  }

  /**
   * Organize files (synchronous version)
   * @param {Array} files - Array of file objects
   * @returns {Array} Array of move operations
   */
  organize(files) {
    this.ensureStructure();

    return files.map((file) => {
      const filePath = file.path || file;
      const fileType = file.type || file.classification || 'other';
      const folder = this._mapTypeToFolder(fileType);
      
      try {
        const newPath = this.moveFile(filePath, folder);
        return {
          from: filePath,
          to: newPath,
          type: fileType,
          folder,
          success: true
        };
      } catch (error) {
        return {
          from: filePath,
          to: null,
          type: fileType,
          folder,
          success: false,
          error: error.message
        };
      }
    });
  }

  /**
   * Organize by file extension
   * @param {Array} files - Array of file paths
   */
  async organizeByExtension(files) {
    const classified = files.map(file => {
      const ext = path.extname(file).toLowerCase();
      const type = this._classifyByExtension(ext);
      return { path: file, type };
    });

    return await this.organize(classified);
  }

  /**
   * Get organization report
   * @returns {Object} Report of organization operations
   */
  getReport() {
    return {
      ...this.report,
      summary: {
        total: this.report.organized + this.report.skipped,
        organized: this.report.organized,
        skipped: this.report.skipped,
        errors: this.report.errors.length
      }
    };
  }

  // ────────────────────────────────────────────────────────────────
  // PRIVATE HELPER METHODS
  // ────────────────────────────────────────────────────────────────

  _mapTypeToFolder(type) {
    // Map classification types to folder names
    const typeMap = {
      audio: 'audio',
      music: 'audio',
      sound: 'audio',
      video: 'video',
      movie: 'video',
      image: 'images',
      photo: 'images',
      picture: 'images',
      code: 'code',
      script: 'code',
      document: 'documents',
      doc: 'documents',
      pdf: 'documents',
      archive: 'archives',
      zip: 'archives',
      data: 'data',
      database: 'data',
      csv: 'data',
      json: 'data'
    };

    return typeMap[type.toLowerCase()] || 'other';
  }

  _classifyByExtension(ext) {
    const extMap = {
      '.mp3': 'audio',
      '.wav': 'audio',
      '.flac': 'audio',
      '.mp4': 'video',
      '.mov': 'video',
      '.png': 'images',
      '.jpg': 'images',
      '.pdf': 'documents',
      '.zip': 'archives',
      '.js': 'code',
      '.ts': 'code',
      '.py': 'code'
    };

    return extMap[ext] || 'other';
  }

  _getDestinationPath(file, type) {
    const folder = this._mapTypeToFolder(type);
    return path.join(this.root, folder, path.basename(file));
  }

  async _moveFileSafe(file, type) {
    const folder = this._mapTypeToFolder(type);
    const destination = path.join(this.root, folder, path.basename(file));

    // Check if destination exists
    if (await exists(destination)) {
      const resolved = this._resolveConflict(file, destination);
      if (!resolved) {
        throw new Error(`Destination exists and conflict strategy is skip: ${destination}`);
      }
      await rename(file, resolved);
      return resolved;
    }

    await rename(file, destination);
    return destination;
  }

  _resolveConflict(source, destination) {
    const strategy = this.options.conflictStrategy;

    if (strategy === 'skip') {
      return null;
    }

    if (strategy === 'overwrite') {
      // Delete destination and use it
      try {
        fs.unlinkSync(destination);
      } catch {
        // Ignore if doesn't exist
      }
      return destination;
    }

    if (strategy === 'rename') {
      // Add timestamp or counter to filename
      const dir = path.dirname(destination);
      const ext = path.extname(destination);
      const base = path.basename(destination, ext);
      const timestamp = Date.now();
      return path.join(dir, `${base}-${timestamp}${ext}`);
    }

    return null;
  }
}

// Default export
export default GabrielOrganizer;

// For CommonJS compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GabrielOrganizer;
  module.exports.default = GabrielOrganizer;
}

