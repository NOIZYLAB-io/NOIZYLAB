"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FilesProvider = void 0;
const promise_pool_1 = require("@supercharge/promise-pool");
const vscode_1 = require("vscode");
const models_1 = require("../models");
/**
 * FilesProvider supplies the file tree for the VSCode JSON Flow extension.
 * Manages and groups file nodes for display in the explorer view.
 * Follows SOLID principles for maintainability and extensibility.
 *
 * @example
 * const provider = new FilesProvider(controller);
 */
class FilesProvider {
    controller;
    // -----------------------------------------------------------------
    // Properties
    // -----------------------------------------------------------------
    /**
     * Event fired when the file tree data changes.
     */
    onDidChangeTreeData;
    /**
     * Internal event emitter for file tree data changes. Used to signal the view to update.
     */
    _onDidChangeTreeData;
    /**
     * Tracks whether the provider has been disposed to prevent redundant disposal.
     */
    _isDisposed = false;
    /**
     * Cache compiled regex by file type to avoid re-allocations across runs.
     */
    _regexCache = new Map();
    /**
     * Debounce timer for refresh calls.
     */
    _refreshTimer = null;
    /**
     * Debounce interval in milliseconds for refresh events.
     */
    _refreshDebounceMs = 200;
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Constructs a FilesProvider responsible for managing and grouping file nodes in the explorer view.
     * @param controller FilesController instance providing file data and configuration.
     */
    constructor(controller) {
        this.controller = controller;
        this._onDidChangeTreeData = new vscode_1.EventEmitter();
        this.onDidChangeTreeData = this._onDidChangeTreeData.event;
    }
    /**
     * Disposes internal resources and event listeners to prevent memory leaks.
     * This method is idempotent and safe to call multiple times.
     *
     * @remarks
     * Always call this method when the provider is no longer needed to avoid resource leaks.
     */
    dispose() {
        if (this._isDisposed) {
            return;
        }
        this._isDisposed = true;
        if (this._refreshTimer) {
            clearTimeout(this._refreshTimer);
            this._refreshTimer = null;
        }
        if (this._onDidChangeTreeData) {
            this._onDidChangeTreeData.dispose();
        }
        this._onDidChangeTreeData = undefined;
    }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    /**
     * Internal cache for grouped file nodes.
     */
    _cachedNodes = undefined;
    _cachePromise = undefined;
    /**
     * Returns the tree item representation for the given file node.
     * @param element The node for which to return the tree item.
     */
    getTreeItem(element) {
        return element;
    }
    /**
     * Returns the child nodes for the given file node, or the root file groups if no node is provided.
     * @param element The parent node, or undefined for root nodes.
     */
    async getChildren(element) {
        if (element) {
            return element.children;
        }
        if (this._cachedNodes) {
            return this._cachedNodes;
        }
        if (this._cachePromise) {
            return this._cachePromise;
        }
        this._cachePromise = this.getListFilesInternal().then((nodes) => {
            this._cachedNodes = nodes;
            this._cachePromise = undefined;
            return nodes;
        });
        return this._cachePromise;
    }
    /**
     * Refreshes the file tree view, causing it to be re-rendered in the explorer.
     */
    refresh() {
        this._cachedNodes = undefined;
        this._cachePromise = undefined;
        if (this._refreshTimer) {
            clearTimeout(this._refreshTimer);
            this._refreshTimer = null;
        }
        this._refreshTimer = setTimeout(() => {
            this._onDidChangeTreeData.fire();
            this._refreshTimer = null;
        }, this._refreshDebounceMs);
    }
    /**
     * Retrieves and groups files by type, constructing NodeModel nodes for the tree view.
     * Only NodeModel instances are used to ensure type consistency.
     * @returns Promise resolving to an array of grouped NodeModel nodes or undefined if none.
     */
    async getListFilesInternal() {
        const { includedFilePatterns } = this.controller.config;
        const files = await this.controller.getFiles();
        if (!files) {
            return [];
        }
        const { results, errors } = await promise_pool_1.PromisePool.for(includedFilePatterns)
            .withConcurrency(3)
            .process(async (fileType) => {
            const children = files.filter((file) => {
                const fsPath = file.resourceUri?.fsPath ?? '';
                const baseName = fsPath.split(/[\\\/]/).pop() ?? file.label.toString();
                if (fileType === 'env') {
                    // Match .env and .env.* (but not .envrc)
                    return /^\.env(\..*)?$/i.test(baseName);
                }
                // Strict extension match: ends with .<fileType>
                let extRegex = this._regexCache.get(fileType);
                if (!extRegex) {
                    extRegex = new RegExp(`\\.${fileType}$`, 'i');
                    this._regexCache.set(fileType, extRegex);
                }
                return extRegex.test(baseName);
            });
            if (children.length === 0) {
                return undefined;
            }
            const node = new models_1.NodeModel(`${fileType}: ${children.length}`, new vscode_1.ThemeIcon('folder-opened'), undefined, undefined, fileType, children);
            node.tooltip = vscode_1.l10n.t('Group: {0}\nFiles: {1}\nHint: Click to expand', [
                fileType,
                children.length,
            ]);
            return node;
        });
        if (errors.length > 0) {
            console.error('Errors processing file types:', errors);
        }
        const nodes = results.filter((node) => node !== undefined);
        // Order groups by size (descending) for usability
        nodes.sort((a, b) => (b.children?.length ?? 0) - (a.children?.length ?? 0));
        return nodes;
    }
}
exports.FilesProvider = FilesProvider;
//# sourceMappingURL=files.providers.js.map