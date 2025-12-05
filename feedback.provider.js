"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FeedbackProvider = void 0;
const vscode_1 = require("vscode");
const configs_1 = require("../configs");
const models_1 = require("../models");
/**
 * The FeedbackProvider class
 *
 * @class
 * @classdesc The class that represents the feedback provider.
 * @export
 * @public
 * @implements {TreeDataProvider<NodeModel>}
 * @property {EventEmitter<NodeModel | undefined | null | void>} _onDidChangeTreeData - The onDidChangeTreeData event emitter
 * @property {Event<NodeModel | undefined | null | void>} onDidChangeTreeData - The onDidChangeTreeData event
 * @property {FeedbackController} controller - The feedback controller
 * @example
 * const provider = new FeedbackProvider();
 *
 * @see https://code.visualstudio.com/api/references/vscode-api#TreeDataProvider
 */
class FeedbackProvider {
    controller;
    // -----------------------------------------------------------------
    // Properties
    // -----------------------------------------------------------------
    // Private properties
    /**
     * The onDidChangeTreeData event emitter.
     * @type {EventEmitter<NodeModel | undefined | null | void>}
     * @private
     * @memberof FeedbackProvider
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
     * @memberof FeedbackProvider
     * @example
     * this._isDisposed = false;
     */
    _isDisposed = false;
    // Public properties
    /**
     * The onDidChangeTreeData event.
     * @type {Event<NodeModel | undefined | null | void>}
     * @public
     * @memberof FeedbackProvider
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
     * Constructor for the FeedbackProvider class
     *
     * @constructor
     * @param {FeedbackController} controller - The feedback controller
     * @public
     * @memberof FeedbackProvider
     */
    constructor(controller) {
        this.controller = controller;
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
     * @memberof FeedbackProvider
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
     * @param {NodeModel} [element] - The element.
     * @returns {ProviderResult<NodeModel[]>} - The children.
     */
    getChildren(element) {
        if (element) {
            return element.children;
        }
        return this.getFeedbacks();
    }
    /**
     * Refreshes the tree data.
     *
     * @function refresh
     * @public
     * @memberof FeedbackProvider
     * @example
     * provider.refresh();
     *
     * @returns {void} - No return value
     */
    refresh() {
        this._onDidChangeTreeData.fire();
    }
    /**
     * Disposes the provider.
     *
     * @function dispose
     * @public
     * @memberof FeedbackProvider
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
     * Returns the feedbacks.
     *
     * @function getFeedbacks
     * @private
     * @memberof FeedbackProvider
     * @example
     * const feedbacks = this.getFeedbacks();
     *
     * @returns {NodeModel[]} - The feedbacks
     */
    getFeedbacks() {
        return [
            new models_1.NodeModel(vscode_1.l10n.t('About Us'), new vscode_1.ThemeIcon('info'), {
                title: 'About Us',
                command: `${configs_1.EXTENSION_ID}.feedback.aboutUs`,
            }),
            new models_1.NodeModel(vscode_1.l10n.t('Report an Issue'), new vscode_1.ThemeIcon('bug'), {
                title: 'Report an Issue',
                command: `${configs_1.EXTENSION_ID}.feedback.reportIssues`,
            }),
            new models_1.NodeModel(vscode_1.l10n.t('Rate Us'), new vscode_1.ThemeIcon('star'), {
                title: 'Rate Us',
                command: `${configs_1.EXTENSION_ID}.feedback.rateUs`,
            }),
            new models_1.NodeModel(vscode_1.l10n.t('Support Us'), new vscode_1.ThemeIcon('heart'), {
                title: 'Support Us',
                command: `${configs_1.EXTENSION_ID}.feedback.supportUs`,
            }),
        ];
    }
}
exports.FeedbackProvider = FeedbackProvider;
//# sourceMappingURL=feedback.provider.js.map