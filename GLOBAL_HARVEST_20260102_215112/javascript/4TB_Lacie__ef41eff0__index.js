import fs from 'fs';
import path from 'path';
import { promisify } from 'util';
import crypto from 'crypto';

// Dynamic import for GabrielScanner to avoid circular dependencies
let GabrielScanner;

const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);
const stat = promisify(fs.stat);
const mkdir = promisify(fs.mkdir);

/**
 * GABRIEL SYNC ENGINE — Local ⇆ Cloudflare Bridge
 * 
 * Bidirectional synchronization between local filesystem and Cloudflare services:
 * - R2 (Object Storage)
 * - KV (Key-Value Store)
 * - D1 (SQLite Database)
 * 
 * @example
 * const sync = new GabrielSyncEngine({
 *   r2: env.MY_BUCKET,
 *   kv: env.MY_KV,
 *   d1: env.MY_DB
 * });
 * 
 * // Sync local directory to R2
 * await sync.syncToCloudflare('/local/path', 'r2-prefix/');
 * 
 * // Sync from Cloudflare to local
 * await sync.syncFromCloudflare('r2-prefix/', '/local/path');
 */
export class GabrielSyncEngine {
  constructor(options = {}) {
    this.r2 = options.r2 || null;
    this.kv = options.kv || null;
    this.d1 = options.d1 || null;
    this.options = {
      concurrency: options.concurrency || 5,
      chunkSize: options.chunkSize || 1024 * 1024 * 5, // 5MB
      retryAttempts: options.retryAttempts || 3,
      retryDelay: options.retryDelay || 1000,
      conflictStrategy: options.conflictStrategy || 'newer', // 'newer', 'local', 'remote', 'manual'
      ...options
    };
    
    this.syncState = {
      localToRemote: new Map(),
      remoteToLocal: new Map(),
      conflicts: [],
      errors: []
    };
  }

  /**
   * Sync local directory to Cloudflare R2
   * @param {string} localPath - Local directory path
   * @param {string} r2Prefix - R2 key prefix
   * @param {Object} options - Sync options
   */
  async syncToCloudflare(localPath, r2Prefix = '', options = {}) {
    if (!this.r2) {
      throw new Error('R2 binding not configured');
    }

    const opts = { ...this.options, ...options };
    const files = await this.getLocalFiles(localPath);
    
    const results = [];
    const queue = [...files];
    const workers = [];

    // Process files with concurrency limit
    for (let i = 0; i < Math.min(opts.concurrency, queue.length); i++) {
      workers.push(this.processUploadQueue(queue, localPath, r2Prefix, opts, results));
    }

    await Promise.all(workers);

    return {
      synced: results.filter(r => r.success).length,
      failed: results.filter(r => !r.success).length,
      results,
      conflicts: this.syncState.conflicts
    };
  }

  /**
   * Sync from Cloudflare R2 to local directory
   * @param {string} r2Prefix - R2 key prefix
   * @param {string} localPath - Local directory path
   * @param {Object} options - Sync options
   */
  async syncFromCloudflare(r2Prefix, localPath, options = {}) {
    if (!this.r2) {
      throw new Error('R2 binding not configured');
    }

    const opts = { ...this.options, ...options };
    const remoteFiles = await this.listR2Objects(r2Prefix);
    
    // Ensure local directory exists
    await this.ensureDirectory(localPath);

    const results = [];
    const queue = [...remoteFiles];
    const workers = [];

    for (let i = 0; i < Math.min(opts.concurrency, queue.length); i++) {
      workers.push(this.processDownloadQueue(queue, r2Prefix, localPath, opts, results));
    }

    await Promise.all(workers);

    return {
      synced: results.filter(r => r.success).length,
      failed: results.filter(r => !r.success).length,
      results,
      conflicts: this.syncState.conflicts
    };
  }

  /**
   * Bidirectional sync (compare and sync both ways)
   * @param {string} localPath - Local directory path
   * @param {string} r2Prefix - R2 key prefix
   * @param {Object} options - Sync options
   */
  async syncBidirectional(localPath, r2Prefix = '', options = {}) {
    const localFiles = await this.getLocalFiles(localPath);
    const remoteFiles = await this.listR2Objects(r2Prefix);

    const localMap = new Map(localFiles.map(f => [f.relative, f]));
    const remoteMap = new Map(remoteFiles.map(f => [f.key.replace(r2Prefix, ''), f]));

    const toUpload = [];
    const toDownload = [];
    const conflicts = [];

    // Find files to upload (local-only or newer)
    for (const [relPath, localFile] of localMap) {
      const remoteFile = remoteMap.get(relPath);
      
      if (!remoteFile) {
        toUpload.push(localFile);
      } else {
        const localHash = await this.getFileHash(localFile.path);
        const remoteHash = remoteFile.etag || '';
        
        if (localHash !== remoteHash) {
          const localTime = localFile.mtime;
          const remoteTime = new Date(remoteFile.uploaded || 0);
          
          if (localTime > remoteTime) {
            toUpload.push(localFile);
          } else if (localTime < remoteTime) {
            toDownload.push(remoteFile);
          } else {
            // Same time but different hash - conflict
            conflicts.push({
              path: relPath,
              local: localFile,
              remote: remoteFile,
              reason: 'hash_mismatch'
            });
          }
        }
      }
    }

    // Find files to download (remote-only)
    for (const [relPath, remoteFile] of remoteMap) {
      if (!localMap.has(relPath)) {
        toDownload.push(remoteFile);
      }
    }

    // Handle conflicts
    for (const conflict of conflicts) {
      const strategy = this.options.conflictStrategy;
      
      if (strategy === 'newer') {
        const localTime = conflict.local.mtime;
        const remoteTime = new Date(conflict.remote.uploaded || 0);
        
        if (localTime > remoteTime) {
          toUpload.push(conflict.local);
        } else {
          toDownload.push(conflict.remote);
        }
      } else if (strategy === 'local') {
        toUpload.push(conflict.local);
      } else if (strategy === 'remote') {
        toDownload.push(conflict.remote);
      } else {
        // Manual - add to conflicts list
        this.syncState.conflicts.push(conflict);
      }
    }

    // Perform syncs
    const uploadResults = await this.syncToCloudflare(localPath, r2Prefix);
    const downloadResults = await this.syncFromCloudflare(r2Prefix, localPath);

    return {
      uploaded: uploadResults.synced,
      downloaded: downloadResults.synced,
      conflicts: conflicts.length,
      conflictsList: conflicts
    };
  }

  /**
   * Sync data to KV store
   * @param {string} key - KV key
   * @param {any} value - Value to store (will be JSON stringified)
   */
  async syncToKV(key, value) {
    if (!this.kv) {
      throw new Error('KV binding not configured');
    }

    const serialized = typeof value === 'string' ? value : JSON.stringify(value);
    await this.kv.put(key, serialized);
    return { key, success: true };
  }

  /**
   * Sync data from KV store
   * @param {string} key - KV key
   * @returns {Promise<any>} Parsed value
   */
  async syncFromKV(key) {
    if (!this.kv) {
      throw new Error('KV binding not configured');
    }

    const value = await this.kv.get(key);
    if (!value) return null;

    try {
      return JSON.parse(value);
    } catch {
      return value;
    }
  }

  /**
   * Batch sync to KV
   * @param {Map|Object} data - Key-value pairs to sync
   */
  async syncBatchToKV(data) {
    const entries = data instanceof Map ? Array.from(data.entries()) : Object.entries(data);
    const results = [];

    for (const [key, value] of entries) {
      try {
        await this.syncToKV(key, value);
        results.push({ key, success: true });
      } catch (error) {
        results.push({ key, success: false, error: error.message });
      }
    }

    return results;
  }

  /**
   * Sync to D1 database
   * @param {string} table - Table name
   * @param {Object|Array} data - Data to insert/update
   */
  async syncToD1(table, data) {
    if (!this.d1) {
      throw new Error('D1 binding not configured');
    }

    const items = Array.isArray(data) ? data : [data];
    const results = [];

    for (const item of items) {
      try {
        // Simple insert or replace
        const keys = Object.keys(item);
        const values = Object.values(item);
        const placeholders = keys.map(() => '?').join(', ');
        
        const sql = `
          INSERT INTO ${table} (${keys.join(', ')})
          VALUES (${placeholders})
          ON CONFLICT DO UPDATE SET
          ${keys.map(k => `${k} = excluded.${k}`).join(', ')}
        `;

        await this.d1.prepare(sql).bind(...values).run();
        results.push({ item, success: true });
      } catch (error) {
        results.push({ item, success: false, error: error.message });
      }
    }

    return results;
  }

  /**
   * Sync from D1 database
   * @param {string} table - Table name
   * @param {Object} query - Query conditions
   */
  async syncFromD1(table, query = {}) {
    if (!this.d1) {
      throw new Error('D1 binding not configured');
    }

    let sql = `SELECT * FROM ${table}`;
    const bindings = [];

    if (Object.keys(query).length > 0) {
      const conditions = Object.entries(query).map(([key, value], i) => {
        bindings.push(value);
        return `${key} = ?`;
      });
      sql += ` WHERE ${conditions.join(' AND ')}`;
    }

    const result = await this.d1.prepare(sql).bind(...bindings).all();
    return result.results || [];
  }

  // ────────────────────────────────────────────────────────────────
  // PRIVATE HELPER METHODS
  // ────────────────────────────────────────────────────────────────

  async getLocalFiles(dir, baseDir = null) {
    if (!baseDir) baseDir = dir;
    
    const files = [];
    const items = await fs.promises.readdir(dir);

    for (const item of items) {
      const fullPath = path.join(dir, item);
      const stat = await fs.promises.stat(fullPath);

      if (stat.isDirectory()) {
        const subFiles = await this.getLocalFiles(fullPath, baseDir);
        files.push(...subFiles);
      } else {
        files.push({
          path: fullPath,
          relative: path.relative(baseDir, fullPath),
          size: stat.size,
          mtime: stat.mtime,
          mode: stat.mode
        });
      }
    }

    return files;
  }

  async listR2Objects(prefix = '') {
    if (!this.r2) return [];

    const objects = [];
    let cursor = undefined;

    do {
      const list = await this.r2.list({ prefix, cursor });
      objects.push(...list.objects);
      cursor = list.cursor;
    } while (cursor);

    return objects.map(obj => ({
      key: obj.key,
      size: obj.size,
      etag: obj.etag,
      uploaded: obj.uploaded,
      httpEtag: obj.httpEtag
    }));
  }

  async processUploadQueue(queue, localPath, r2Prefix, options, results) {
    while (queue.length > 0) {
      const file = queue.shift();
      if (!file) break;

      for (let attempt = 0; attempt < options.retryAttempts; attempt++) {
        try {
          const content = await readFile(file.path);
          const r2Key = path.join(r2Prefix, file.relative).replace(/\\/g, '/');

          await this.r2.put(r2Key, content, {
            httpMetadata: {
              contentType: this.getContentType(file.path),
              cacheControl: 'public, max-age=3600'
            },
            customMetadata: {
              originalPath: file.path,
              size: file.size.toString(),
              mtime: file.mtime.toISOString()
            }
          });

          results.push({ path: file.path, key: r2Key, success: true });
          break;
        } catch (error) {
          if (attempt === options.retryAttempts - 1) {
            results.push({ 
              path: file.path, 
              success: false, 
              error: error.message 
            });
          } else {
            await this.delay(options.retryDelay * (attempt + 1));
          }
        }
      }
    }
  }

  async processDownloadQueue(queue, r2Prefix, localPath, options, results) {
    while (queue.length > 0) {
      const remoteFile = queue.shift();
      if (!remoteFile) break;

      for (let attempt = 0; attempt < options.retryAttempts; attempt++) {
        try {
          const r2Key = remoteFile.key;
          const relativePath = r2Key.replace(r2Prefix, '').replace(/^\//, '');
          const localFilePath = path.join(localPath, relativePath);

          await this.ensureDirectory(path.dirname(localFilePath));

          const object = await this.r2.get(r2Key);
          if (!object) {
            results.push({ key: r2Key, success: false, error: 'Object not found' });
            break;
          }

          const arrayBuffer = await object.arrayBuffer();
          await writeFile(localFilePath, Buffer.from(arrayBuffer));

          results.push({ key: r2Key, path: localFilePath, success: true });
          break;
        } catch (error) {
          if (attempt === options.retryAttempts - 1) {
            results.push({ 
              key: remoteFile.key, 
              success: false, 
              error: error.message 
            });
          } else {
            await this.delay(options.retryDelay * (attempt + 1));
          }
        }
      }
    }
  }

  async getFileHash(filePath) {
    const content = await readFile(filePath);
    return crypto.createHash('md5').update(content).digest('hex');
  }

  getContentType(filePath) {
    const ext = path.extname(filePath).toLowerCase();
    const types = {
      '.js': 'application/javascript',
      '.ts': 'application/typescript',
      '.json': 'application/json',
      '.html': 'text/html',
      '.css': 'text/css',
      '.png': 'image/png',
      '.jpg': 'image/jpeg',
      '.jpeg': 'image/jpeg',
      '.gif': 'image/gif',
      '.svg': 'image/svg+xml',
      '.mp4': 'video/mp4',
      '.mp3': 'audio/mpeg',
      '.pdf': 'application/pdf'
    };
    return types[ext] || 'application/octet-stream';
  }

  async ensureDirectory(dirPath) {
    try {
      await mkdir(dirPath, { recursive: true });
    } catch (error) {
      if (error.code !== 'EEXIST') {
        throw error;
      }
    }
  }

  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

/**
 * GABRIEL SYNC — Simplified Sync Interface
 * 
 * Simple wrapper around GabrielSyncEngine that integrates with GabrielScanner
 * 
 * @example
 * const sync = new GabrielSync('/local/path', {
 *   kv: 'https://kv-endpoint.com',
 *   r2: env.MY_BUCKET
 * });
 * const files = await sync.sync();
 */
export class GabrielSync {
  constructor(root, endpoints = {}) {
    this.root = root;
    this.endpoints = endpoints;
    // Lazy load scanner to avoid circular dependencies
    this._scanner = null;
    this.engine = new GabrielSyncEngine({
      r2: endpoints.r2 || null,
      kv: endpoints.kv || null,
      d1: endpoints.d1 || null
    });
  }

  get scan() {
    if (!this._scanner) {
      // Dynamic import for ES modules
      import('../scanner/index.js').then(module => {
        const GabrielScanner = module.GabrielScanner || module.default;
        this._scanner = new GabrielScanner(this.root);
      }).catch(() => {
        // Fallback: create placeholder scanner
        this._scanner = {
          scan: async () => {
            throw new Error('Scanner not loaded. Ensure gabriel/scanner/index.js exists.');
          }
        };
      });
    }
    return this._scanner;
  }

  async _ensureScanner() {
    if (!this._scanner) {
      const module = await import('../scanner/index.js');
      const GabrielScanner = module.GabrielScanner || module.default;
      this._scanner = new GabrielScanner(this.root);
    }
    return this._scanner;
  }

  /**
   * Scan and sync files to endpoints
   * @returns {Promise<Array>} Scanned files
   */
  async sync() {
    const scanner = await this._ensureScanner();
    const files = await scanner.scan();

    // Sync manifest to KV endpoint if provided
    if (this.endpoints.kv) {
      await fetch(this.endpoints.kv, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type: 'sync_manifest', files })
      });
    }

    return files;
  }

  /**
   * Sync to specific endpoint
   * @param {string} endpoint - Endpoint name ('kv', 'r2', 'd1')
   * @param {Object} options - Sync options
   */
  async syncTo(endpoint, options = {}) {
    switch (endpoint) {
      case 'r2':
        return await this.engine.syncToCloudflare(this.root, options.prefix || '', options);
      
      case 'kv':
        await this._ensureScanner();
        const files = await this.scan.scan();
        if (typeof this.endpoints.kv === 'string' && this.endpoints.kv.startsWith('http')) {
          await fetch(this.endpoints.kv, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ type: 'sync_manifest', files })
          });
        } else {
          await this.engine.syncToKV('sync_manifest', { type: 'sync_manifest', files });
        }
        return files;
      
      case 'd1':
        if (!this.endpoints.d1) throw new Error('D1 endpoint not configured');
        await this._ensureScanner();
        const scannedFiles = await this.scan.scan();
        return await this.engine.syncToD1(options.table || 'files', scannedFiles);
      
      default:
        throw new Error(`Unknown endpoint: ${endpoint}`);
    }
  }

  /**
   * Sync from endpoint
   * @param {string} endpoint - Endpoint name ('kv', 'r2', 'd1')
   * @param {Object} options - Sync options
   */
  async syncFrom(endpoint, options = {}) {
    switch (endpoint) {
      case 'r2':
        return await this.engine.syncFromCloudflare(options.prefix || '', this.root, options);
      
      case 'kv':
        if (typeof this.endpoints.kv === 'string' && this.endpoints.kv.startsWith('http')) {
          const response = await fetch(this.endpoints.kv);
          const data = await response.json();
          return data.files || [];
        } else {
          const manifest = await this.engine.syncFromKV('sync_manifest');
          return manifest?.files || [];
        }
      
      case 'd1':
        if (!this.endpoints.d1) throw new Error('D1 endpoint not configured');
        return await this.engine.syncFromD1(options.table || 'files', options.query || {});
      
      default:
        throw new Error(`Unknown endpoint: ${endpoint}`);
    }
  }
}

// Default export
export default GabrielSyncEngine;

// Named exports
export { GabrielSync };

// For CommonJS compatibility
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GabrielSyncEngine;
  module.exports.default = GabrielSyncEngine;
  module.exports.GabrielSync = GabrielSync;
}

