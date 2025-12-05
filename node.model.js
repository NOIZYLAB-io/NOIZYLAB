"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.NodeModel = void 0;
const vscode_1 = require("vscode");
/**
 * NodeModel represents a file or folder in the workspace tree.
 * Used for navigation, display, and file operations in the extension.
 * All properties and methods are documented with JSDoc for clarity.
 *
 * @class
 * @extends {TreeItem}
 * @export
 * @public
 * @property {Uri} [resourceUri] - The resource URI
 * @property {string} [contextValue] - The context value
 * @property {Node[]} [children] - The children
 * @example
 * const node = new Node('About Us', TreeItemCollapsibleState.None, 'about', {
 *   title: 'About Us',
 *   command: 'angular.feedback.aboutUs',
 * });
 *
 * @see https://code.visualstudio.com/api/references/vscode-api#TreeItem
 */
class NodeModel extends vscode_1.TreeItem {
    label;
    iconPath;
    command;
    resourceUri;
    contextValue;
    // -----------------------------------------------------------------
    // Properties
    // -----------------------------------------------------------------
    // Public properties
    /**
     * The children.
     * @type {NodeModel[]}
     * @public
     * @memberof NodeModel
     * @example
     * node.children = [];
     */
    children;
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * The constructor
     *
     * @constructor
     * @param {string | TreeItemLabel} label - The label
     * @param {string | Uri | { light: Uri; dark: Uri } | ThemeIcon} [iconPath] - The icon path
     * @param {Command} [command] - The command
     * @param {Uri} [resourceUri] - The resource URI
     * @param {string} [contextValue] - The context value
     * @param {NodeModel[]} [children] - The children
     * @example
     * const node = new Node('About Us', new ThemeIcon('info'), {
     *   title: 'About Us',
     *   command: 'angular.feedback.aboutUs',
     * });
     */
    constructor(label, iconPath, command, resourceUri, contextValue, children) {
        super(label, children
            ? vscode_1.TreeItemCollapsibleState.Expanded
            : vscode_1.TreeItemCollapsibleState.None);
        this.label = label;
        this.iconPath = iconPath;
        this.command = command;
        this.resourceUri = resourceUri;
        this.contextValue = contextValue;
        this.iconPath = iconPath;
        this.resourceUri = resourceUri;
        this.command = command;
        this.contextValue = contextValue;
        this.children = children;
    }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    // Public methods
    /**
     * The setChildren method
     *
     * @function setChildren
     * @param {NodeModel[]} children - The children
     * @public
     * @memberof NodeModel
     * @example
     * node.setChildren([]);
     *
     * @returns {void} The result
     */
    setChildren(children) {
        this.collapsibleState = vscode_1.TreeItemCollapsibleState.Expanded;
        this.children = children;
    }
    /**
     * The hasChildren method
     *
     * @function hasChildren
     * @public
     * @memberof NodeModel
     * @example
     * const hasChildren = node.hasChildren();
     *
     * @returns {boolean} The result
     */
    hasChildren() {
        return !!(this.children && this.children.length);
    }
}
exports.NodeModel = NodeModel;
//# sourceMappingURL=node.model.js.map