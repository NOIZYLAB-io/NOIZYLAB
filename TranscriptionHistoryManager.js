"use strict";
/**
 * Transcription history manager
 * Manages saving, loading, and migrating transcription history data
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.TranscriptionHistoryManager = void 0;
const TranscriptionHistory_1 = require("../types/TranscriptionHistory");
const GlobalOutput_1 = require("../utils/GlobalOutput");
const ErrorHandler_1 = require("../utils/ErrorHandler");
/**
 * Class for managing transcription history
 */
class TranscriptionHistoryManager {
    context;
    errorHandler;
    _history = null;
    constructor(context, errorHandler) {
        this.context = context;
        this.errorHandler = errorHandler;
    }
    /**
     * Initialization of the manager - loading history from storage
     */
    async initialize() {
        try {
            const result = await this.loadHistory();
            return result;
        }
        catch (error) {
            const errorMsg = `Failed to initialize TranscriptionHistoryManager: ${error instanceof Error ? error.message : String(error)}`;
            GlobalOutput_1.ExtensionLog.error(errorMsg);
            // Create a new empty history on initialization error
            this._history = this.createEmptyHistory();
            return {
                success: false,
                error: errorMsg,
                data: { fallbackUsed: true }
            };
        }
    }
    /**
     * Adding a new entry to the history
     */
    async addEntry(options) {
        try {
            if (!this._history) {
                await this.initialize();
            }
            // Create a new entry
            const entry = {
                id: this.generateEntryId(),
                text: options.text.trim(),
                timestamp: options.timestamp || new Date().toISOString(),
                duration: options.duration,
                language: options.language,
                mode: options.mode,
                // Post-processing fields
                originalText: options.originalText?.trim(),
                isPostProcessed: options.isPostProcessed || false,
                postProcessingModel: options.postProcessingModel
            };
            // Add to the beginning of the array (new entries on top)
            this._history.entries.unshift(entry);
            // Apply the limit on the number of entries
            this.enforceMaxEntries();
            // Update the time of the last change
            this._history.lastUpdated = new Date().toISOString();
            // Save to storage
            const saveResult = await this.saveHistory();
            if (saveResult.success) {
                return {
                    success: true,
                    data: { entry, totalEntries: this._history.entries.length }
                };
            }
            return saveResult;
        }
        catch (error) {
            const errorContext = {
                operation: 'addEntry',
                timestamp: new Date(),
                additionalData: { optionsReceived: !!options }
            };
            return this.handleError(error, errorContext);
        }
    }
    /**
     * Deleting an entry by ID
     */
    async removeEntry(entryId) {
        try {
            if (!this._history) {
                await this.initialize();
            }
            const initialCount = this._history.entries.length;
            this._history.entries = this._history.entries.filter(entry => entry.id !== entryId);
            const removed = this._history.entries.length < initialCount;
            if (removed) {
                this._history.lastUpdated = new Date().toISOString();
                const saveResult = await this.saveHistory();
                if (saveResult.success) {
                    return {
                        success: true,
                        data: { entryId, remainingEntries: this._history.entries.length }
                    };
                }
                return saveResult;
            }
            return {
                success: false,
                error: `Entry with ID ${entryId} not found`
            };
        }
        catch (error) {
            const errorContext = {
                operation: 'removeEntry',
                timestamp: new Date(),
                additionalData: { entryId }
            };
            return this.handleError(error, errorContext);
        }
    }
    /**
     * Clearing all history
     */
    async clearHistory() {
        try {
            this._history = this.createEmptyHistory();
            const saveResult = await this.saveHistory();
            return saveResult;
        }
        catch (error) {
            const errorContext = {
                operation: 'clearHistory',
                timestamp: new Date()
            };
            return this.handleError(error, errorContext);
        }
    }
    /**
     * Getting all history
     */
    async getHistory() {
        if (!this._history) {
            await this.initialize();
        }
        return this._history || this.createEmptyHistory();
    }
    /**
     * Getting an entry by ID
     */
    async getEntry(entryId) {
        const history = await this.getHistory();
        return history.entries.find(entry => entry.id === entryId) || null;
    }
    /**
     * Getting the number of entries
     */
    async getEntriesCount() {
        const history = await this.getHistory();
        return history.entries.length;
    }
    /**
     * Loading history from VS Code storage
     */
    async loadHistory() {
        try {
            const savedData = this.context.globalState.get(TranscriptionHistory_1.TRANSCRIPTION_HISTORY_CONSTANTS.STORAGE_KEY);
            if (!savedData) {
                this._history = this.createEmptyHistory();
                return { success: true, data: { newHistory: true } };
            }
            // Attempt to migrate data if necessary
            const migrationResult = this.migrateData(savedData);
            this._history = migrationResult.data;
            return {
                success: true,
                data: {
                    entriesLoaded: this._history.entries.length,
                    migrated: migrationResult.migrated
                }
            };
        }
        catch (error) {
            const errorMsg = `Failed to load history: ${error instanceof Error ? error.message : String(error)}`;
            GlobalOutput_1.ExtensionLog.error(errorMsg);
            // Fallback to an empty history
            this._history = this.createEmptyHistory();
            return {
                success: false,
                error: errorMsg,
                data: { fallbackUsed: true }
            };
        }
    }
    /**
     * Saving history to VS Code storage
     */
    async saveHistory() {
        try {
            if (!this._history) {
                return { success: false, error: 'No history to save' };
            }
            await this.context.globalState.update(TranscriptionHistory_1.TRANSCRIPTION_HISTORY_CONSTANTS.STORAGE_KEY, this._history);
            return { success: true };
        }
        catch (error) {
            const errorMsg = `Failed to save history: ${error instanceof Error ? error.message : String(error)}`;
            GlobalOutput_1.ExtensionLog.error(errorMsg);
            return {
                success: false,
                error: errorMsg
            };
        }
    }
    /**
     * Migration of data from old formats
     */
    migrateData(savedData) {
        // If the data is already in the current format
        if (savedData.version === TranscriptionHistory_1.TRANSCRIPTION_HISTORY_CONSTANTS.CURRENT_VERSION) {
            return { data: savedData, migrated: false };
        }
        // Migration from the old format (if there is just an array of entries)
        if (Array.isArray(savedData)) {
            const migratedHistory = {
                version: TranscriptionHistory_1.TRANSCRIPTION_HISTORY_CONSTANTS.CURRENT_VERSION,
                entries: savedData.map((entry, index) => ({
                    id: entry.id || `migrated_${Date.now()}_${index}`,
                    text: entry.text || '',
                    timestamp: entry.timestamp || new Date().toISOString(),
                    duration: entry.duration || 0,
                    language: entry.language || 'auto',
                    mode: entry.mode || TranscriptionHistory_1.RecordingMode.INSERT_OR_CLIPBOARD
                })),
                lastUpdated: new Date().toISOString()
            };
            return { data: migratedHistory, migrated: true };
        }
        // Migration from the format without a version
        if (savedData.entries && !savedData.version) {
            const migratedHistory = {
                version: TranscriptionHistory_1.TRANSCRIPTION_HISTORY_CONSTANTS.CURRENT_VERSION,
                entries: savedData.entries.map((entry, index) => ({
                    id: entry.id || `migrated_${Date.now()}_${index}`,
                    text: entry.text || '',
                    timestamp: entry.timestamp || new Date().toISOString(),
                    duration: entry.duration || 0,
                    language: entry.language || 'auto',
                    mode: entry.mode || TranscriptionHistory_1.RecordingMode.INSERT_OR_CLIPBOARD
                })),
                lastUpdated: savedData.lastUpdated || new Date().toISOString()
            };
            return { data: migratedHistory, migrated: true };
        }
        // If the format is unknown, create an empty history
        GlobalOutput_1.ExtensionLog.warn('Unknown data format during migration, creating empty history');
        return { data: this.createEmptyHistory(), migrated: true };
    }
    /**
     * Creating an empty history
     */
    createEmptyHistory() {
        return {
            version: TranscriptionHistory_1.TRANSCRIPTION_HISTORY_CONSTANTS.CURRENT_VERSION,
            entries: [],
            lastUpdated: new Date().toISOString()
        };
    }
    /**
     * Applying the limit on the maximum number of entries
     */
    enforceMaxEntries() {
        if (!this._history) {
            return;
        }
        const maxEntries = TranscriptionHistory_1.TRANSCRIPTION_HISTORY_CONSTANTS.MAX_ENTRIES;
        if (this._history.entries.length > maxEntries) {
            const removedCount = this._history.entries.length - maxEntries;
            this._history.entries = this._history.entries.slice(0, maxEntries);
        }
    }
    /**
     * Generating a unique ID for an entry
     */
    generateEntryId() {
        return `entry_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }
    /**
     * Handling errors
     */
    handleError(error, context) {
        const errorMsg = error instanceof Error ? error.message : String(error);
        this.errorHandler.handleError(ErrorHandler_1.ErrorType.UNKNOWN_ERROR, context, error instanceof Error ? error : new Error(errorMsg));
        return {
            success: false,
            error: errorMsg
        };
    }
}
exports.TranscriptionHistoryManager = TranscriptionHistoryManager;
//# sourceMappingURL=TranscriptionHistoryManager.js.map