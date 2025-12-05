"use strict";
/**
 * Context management service
 * @module services/ContextService
 */
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.ContextService = void 0;
const vscode = __importStar(require("vscode"));
const constants_1 = require("../constants");
const Logger_1 = require("../utils/Logger");
/**
 * Service for managing conversation context and health
 */
class ContextService {
    static instance;
    log = Logger_1.logger.createChild('ContextService');
    contextExchangeCount = 0;
    sessionStartTime = Date.now();
    lastContextRefresh = Date.now();
    filesProcessed = 0;
    constructor() { }
    /**
     * Get singleton instance
     */
    static getInstance() {
        if (!ContextService.instance) {
            ContextService.instance = new ContextService();
        }
        return ContextService.instance;
    }
    /**
     * Get current exchange count
     */
    getExchangeCount() {
        return this.contextExchangeCount;
    }
    /**
     * Increment exchange count
     */
    incrementExchangeCount() {
        this.contextExchangeCount++;
        this.log.debug(`Context exchange count: ${this.contextExchangeCount}`);
    }
    /**
     * Reset exchange count
     */
    resetExchangeCount() {
        this.contextExchangeCount = 0;
        this.lastContextRefresh = Date.now();
        this.log.info('Context exchange count reset');
    }
    /**
     * Get context health status
     */
    getContextHealth() {
        const config = vscode.workspace.getConfiguration();
        const threshold = config.get('fixAugment.contextRefreshThreshold', constants_1.DEFAULT_CONFIG.CONTEXT_REFRESH_THRESHOLD);
        const count = this.contextExchangeCount;
        const warningThreshold = Math.floor(threshold * 0.7);
        if (count >= threshold) {
            return {
                status: 'red',
                text: `Context refresh needed (${count} exchanges)`
            };
        }
        else if (count >= warningThreshold) {
            return {
                status: 'yellow',
                text: `Context getting long (${count} exchanges)`
            };
        }
        else {
            return {
                status: 'green',
                text: `Context healthy (${count} exchanges)`
            };
        }
    }
    /**
     * Check if context should be refreshed
     */
    shouldRefreshContext() {
        const config = vscode.workspace.getConfiguration();
        const threshold = config.get('fixAugment.contextRefreshThreshold', constants_1.DEFAULT_CONFIG.CONTEXT_REFRESH_THRESHOLD);
        return this.contextExchangeCount >= threshold;
    }
    /**
     * Get session start time
     */
    getSessionStartTime() {
        return this.sessionStartTime;
    }
    /**
     * Get last context refresh time
     */
    getLastContextRefresh() {
        return this.lastContextRefresh;
    }
    /**
     * Get files processed count
     */
    getFilesProcessed() {
        return this.filesProcessed;
    }
    /**
     * Increment files processed
     */
    incrementFilesProcessed() {
        this.filesProcessed++;
        this.log.debug(`Files processed: ${this.filesProcessed}`);
    }
    /**
     * Get session duration in milliseconds
     */
    getSessionDuration() {
        return Date.now() - this.sessionStartTime;
    }
    /**
     * Get time since last refresh in milliseconds
     */
    getTimeSinceRefresh() {
        return Date.now() - this.lastContextRefresh;
    }
    /**
     * Format duration for display
     */
    formatDuration(ms) {
        const seconds = Math.floor(ms / 1000);
        const minutes = Math.floor(seconds / 60);
        const hours = Math.floor(minutes / 60);
        const days = Math.floor(hours / 24);
        if (days > 0) {
            return `${days}d ${hours % 24}h`;
        }
        else if (hours > 0) {
            return `${hours}h ${minutes % 60}m`;
        }
        else if (minutes > 0) {
            return `${minutes}m`;
        }
        else {
            return `${seconds}s`;
        }
    }
    /**
     * Format time ago for display
     */
    formatTimeAgo(timestamp) {
        const now = Date.now();
        const diff = now - timestamp;
        const minutes = Math.floor(diff / 60000);
        if (minutes < 1) {
            return 'Just now';
        }
        else if (minutes < 60) {
            return `${minutes}m ago`;
        }
        else {
            const hours = Math.floor(minutes / 60);
            if (hours < 24) {
                return `${hours}h ago`;
            }
            else {
                const days = Math.floor(hours / 24);
                return `${days}d ago`;
            }
        }
    }
    /**
     * Get session statistics
     */
    getSessionStats() {
        return {
            duration: this.formatDuration(this.getSessionDuration()),
            exchanges: this.contextExchangeCount,
            filesProcessed: this.filesProcessed,
            lastRefresh: this.formatTimeAgo(this.lastContextRefresh)
        };
    }
    /**
     * Reset session
     */
    resetSession() {
        this.contextExchangeCount = 0;
        this.sessionStartTime = Date.now();
        this.lastContextRefresh = Date.now();
        this.filesProcessed = 0;
        this.log.info('Session reset');
    }
    /**
     * Export session data for persistence
     */
    exportSessionData() {
        return {
            contextExchangeCount: this.contextExchangeCount,
            sessionStartTime: this.sessionStartTime,
            lastContextRefresh: this.lastContextRefresh,
            filesProcessed: this.filesProcessed
        };
    }
    /**
     * Import session data from persistence
     */
    importSessionData(data) {
        if (data.contextExchangeCount !== undefined) {
            this.contextExchangeCount = data.contextExchangeCount;
        }
        if (data.sessionStartTime !== undefined) {
            this.sessionStartTime = data.sessionStartTime;
        }
        if (data.lastContextRefresh !== undefined) {
            this.lastContextRefresh = data.lastContextRefresh;
        }
        if (data.filesProcessed !== undefined) {
            this.filesProcessed = data.filesProcessed;
        }
        this.log.info('Session data imported');
    }
}
exports.ContextService = ContextService;
//# sourceMappingURL=ContextService.js.map