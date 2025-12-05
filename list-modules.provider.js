"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ListModulesProvider = void 0;
const vscode_1 = require("vscode");
const configs_1 = require("../configs");
const controllers_1 = require("../controllers");
const models_1 = require("../models");
/**
 * The ListModulesProvider class
 *
 * @class
 * @classdesc The class that represents the list of files provider.
 * @export
 * @public
 * @implements {TreeDataProvider<NodeModel>}
 * @property {EventEmitter<NodeModel | undefined | null | void>} _onDidChangeTreeData - The onDidChangeTreeData event emitter
 * @property {Event<NodeModel | undefined | null | void>} onDidChangeTreeData - The onDidChangeTreeData event
 * @property {ListFilesController} controller - The list of files controller
 * @example
 * const provider = new ListModulesProvider();
 *
 * @see https://code.visualstudio.com/api/references/vscode-api#TreeDataProvider
 */
class ListModulesProvider {
    // -----------------------------------------------------------------
    // Properties
    // -----------------------------------------------------------------
    // Private properties
    /**
     * The onDidChangeTreeData event emitter.
     * @type {EventEmitter<NodeModel | undefined | null | void>}
     * @private
     * @memberof ListModulesProvider
     * @example
     * this._onDidChangeTreeData = new EventEmitter<Node | undefined | null | void>();
     * this.onDidChangeTreeData = this._onDidChangeTreeData.event;
     *
     * @see https://code.visualstudio.com/api/references/vscode-api#EventEmitter
     */
    _onDidChangeTreeData;
    /**
     * Indicates whether the provider has been disposed.
     * @type {boolean}
     * @private
     * @memberof ListModulesProvider
     * @example
     * this._isDisposed = false;
     */
    _isDisposed = false;
    /**
     * The cached nodes.
     * @type {NodeModel[] | undefined}
     * @private
     * @memberof ListModulesProvider
     * @example
     * this._cachedNodes = undefined;
     */
    _cachedNodes = undefined;
    /**
     * The cache promise.
     * @type {Promise<NodeModel[] | undefined> | undefined}
     * @private
     * @memberof ListModulesProvider
     * @example
     * this._cachePromise = undefined;
     */
    _cachePromise = undefined;
    // Public properties
    /**
     * Event that signals when the module tree data has changed.
     * Used by VSCode to refresh the explorer view when modules are added, removed, or updated.
     *
     * @public
     * @readonly
     * @type {Event<NodeModel | undefined | null | void>}
     * @see https://code.visualstudio.com/api/references/vscode-api#Event
     */
    onDidChangeTreeData;
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Creates an instance of ListModulesProvider for the VSCode explorer tree.
     * Associates the provider with a ListFilesController to manage file discovery and navigation.
     *
     * @param {ListFilesController} controller - The controller responsible for listing files in the workspace.
     * @public
     */
    constructor() {
        this._onDidChangeTreeData = new vscode_1.EventEmitter();
        this.onDidChangeTreeData = this._onDidChangeTreeData.event;
    }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    // Public methods
    /**
     * Returns the TreeItem representation for a given NodeModel element.
     * Used by VSCode to render nodes in the explorer tree.
     *
     * @param {NodeModel} element - The node model representing a file or section.
     * @returns {TreeItem} The corresponding TreeItem for the VSCode explorer.
     * @public
     */
    getTreeItem(element) {
        return element;
    }
    /**
     * Returns the child nodes for a given module node or root.
     * If no element is provided, returns the top-level module nodes; otherwise, returns children for the given node.
     *
     * @param {NodeModel} [element] - The parent node to retrieve children for.
     * @returns {ProviderResult<NodeModel[]>} Array of child NodeModel elements or undefined if none.
     * @public
     */
    getChildren(element) {
        if (element) {
            return element.children;
        }
        if (this._cachedNodes) {
            return this._cachedNodes;
        }
        if (this._cachePromise) {
            return this._cachePromise;
        }
        this._cachePromise = this.getListModules().then((nodes) => {
            this._cachedNodes = nodes;
            this._cachePromise = undefined;
            return nodes;
        });
        return this._cachePromise;
    }
    /**
     * Refreshes the tree data by firing the event.
     *
     * @function refresh
     * @public
     * @memberof ListModulesProvider
     * @example
     * provider.refresh();
     *
     * @returns {void} - No return value
     */
    refresh() {
        this._cachedNodes = undefined;
        this._cachePromise = undefined;
        this._onDidChangeTreeData.fire();
    }
    /**
     * Disposes the provider.
     *
     * @function dispose
     * @public
     * @memberof ListModulesProvider
     * @example
     * provider.dispose();
     *
     * @returns {void} - No return value
     */
    dispose() {
        this._onDidChangeTreeData.dispose();
        if (this._isDisposed) {
            return;
        }
        this._isDisposed = true;
        if (this._onDidChangeTreeData) {
            this._onDidChangeTreeData.dispose();
        }
    }
    // Private methods
    /**
     * Retrieves all Angular module files in the workspace and parses their structure.
     * Filters files ending with 'module.ts' and scans for key sections (declarations, exports, imports, bootstrap, providers).
     *
     * @private
     * @returns {Promise<NodeModel[]>} Array of NodeModel representing Angular module sections, or undefined if none found.
     * @example
     * const modules = await provider.getListModules();
     */
    async getListModules() {
        const files = await controllers_1.ListFilesController.getFiles();
        if (!files) {
            return [];
        }
        const nodes = files.filter((file) => file.label.toString().includes('module.ts'));
        const ngModuleDeclarationRegex = /^\s*(declarations|exports|imports|bootstrap|providers)\s*:\s*\[/i;
        const { default: pLimit } = await import('p-limit');
        const limit = pLimit(2);
        await Promise.all(nodes.map((file) => limit(async () => {
            if (!file.resourceUri) {
                return file.setChildren([]);
            }
            try {
                const document = await vscode_1.workspace.openTextDocument(file.resourceUri);
                const children = [];
                for (let i = 0; i < document.lineCount; i++) {
                    const text = document.lineAt(i).text;
                    const match = ngModuleDeclarationRegex.exec(text);
                    if (match) {
                        const propertyName = match[1]; // 'declarations', 'imports', etc.
                        const label = `${propertyName}: [`;
                        children.push(new models_1.NodeModel(label, new vscode_1.ThemeIcon('symbol-module'), {
                            command: `${configs_1.EXTENSION_ID}.list.gotoLine`,
                            title: text.trim(),
                            arguments: [file.resourceUri, i],
                        }));
                    }
                }
                file.setChildren(children);
            }
            catch (err) {
                console.error(`Error reading file ${file.resourceUri?.fsPath}:`, err instanceof Error ? err.message : String(err));
                file.setChildren([]);
            }
        })));
        return nodes.filter((file) => file.children && file.children.length !== 0);
    }
}
exports.ListModulesProvider = ListModulesProvider;
//# sourceMappingURL=list-modules.provider.js.map