"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ListFilesProvider = void 0;
const vscode_1 = require("vscode");
const controllers_1 = require("../controllers");
const helpers_1 = require("../helpers");
const models_1 = require("../models");
/**
 * The ListFilesProvider class
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
 * const provider = new ListFilesProvider();
 *
 * @see https://code.visualstudio.com/api/references/vscode-api#TreeDataProvider
 */
class ListFilesProvider {
    // -----------------------------------------------------------------
    // Properties
    // -----------------------------------------------------------------
    // Private properties
    /**
     * The onDidChangeTreeData event emitter.
     * @type {EventEmitter<NodeModel | undefined | null | void>}
     * @private
     * @memberof ListFilesProvider
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
     * @memberof ListFilesProvider
     * @example
     * this._isDisposed = false;
     */
    _isDisposed = false;
    /**
     * The cached nodes.
     * @type {NodeModel[] | undefined}
     * @private
     * @memberof ListFilesProvider
     * @example
     * this._cachedNodes = undefined;
     */
    _cachedNodes = undefined;
    /**
     * The cache promise.
     * @type {Promise<NodeModel[] | undefined> | undefined}
     * @private
     * @memberof ListFilesProvider
     * @example
     * this._cachePromise = undefined;
     */
    _cachePromise = undefined;
    // Public properties
    /**
     * The onDidChangeTreeData event.
     * @type {Event<NodeModel | undefined | null | void>}
     * @public
     * @memberof ListFilesProvider
     * @example
     * readonly onDidChangeTreeData: Event<Node | undefined | null | void>;
     * this.onDidChangeTreeData = this._onDidChangeTreeData.event;
     *
     * @see https://code.visualstudio.com/api/references/vscode-api#Event
     */
    onDidChangeTreeData;
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Constructor for the ListFilesProvider class
     *
     * @constructor
     * @public
     * @memberof ListFilesProvider
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
     * Returns the tree item for the supplied element.
     *
     * @function getTreeItem
     * @param {NodeModel} element - The element
     * @public
     * @memberof ListFilesProvider
     * @example
     * const treeItem = provider.getTreeItem(element);
     *
     * @returns {TreeItem | Thenable<TreeItem>} - The tree item
     *
     * @see https://code.visualstudio.com/api/references/vscode-api#TreeDataProvider
     */
    getTreeItem(element) {
        return element;
    }
    /**
     * Returns the children for the supplied element.
     *
     * @function getChildren
     * @param {NodeModel} [element] - The element
     * @public
     * @memberof ListFilesProvider
     * @example
     * const children = provider.getChildren(element);
     *
     * @returns {ProviderResult<NodeModel[]>} - The children
     *
     * @see https://code.visualstudio.com/api/references/vscode-api#TreeDataProvider
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
        this._cachePromise = this.getListFiles().then((nodes) => {
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
     * @memberof ListFilesProvider
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
     * @memberof ListFilesProvider
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
     * Gets the list of files.
     *
     * @function getListFiles
     * @private
     * @memberof ListFilesProvider
     * @example
     * const files = provider.getListFiles();
     *
     * @returns {Promise<NodeModel[] | undefined>} - The list of files
     */
    async getListFiles() {
        const files = await controllers_1.ListFilesController.getFiles();
        if (!files) {
            return [];
        }
        const fileTypes = controllers_1.ListFilesController.config.watch;
        const { default: pLimit } = await import('p-limit');
        const limit = pLimit(2);
        const groups = await Promise.all(fileTypes.map((type) => limit(async () => {
            const suffix = `${(0, helpers_1.singularize)(type)}.ts`;
            const children = files.filter((file) => file.label.toString().includes(suffix));
            if (children.length === 0) {
                return;
            }
            return new models_1.NodeModel(`${(0, helpers_1.titleize)(type)}: ${children.length}`, new vscode_1.ThemeIcon('folder-opened'), undefined, undefined, type, children);
        })));
        return groups.filter((node) => node !== undefined);
    }
}
exports.ListFilesProvider = ListFilesProvider;
//# sourceMappingURL=list-files.provider.js.map