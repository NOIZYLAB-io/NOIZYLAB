"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.NodeItem = void 0;
const vscode_1 = require("vscode");
const HlfTreeItem_1 = require("./HlfTreeItem");
class NodeItem extends HlfTreeItem_1.HlfTreeItem {
    constructor() {
        super(...arguments);
        this.iconPath = new vscode_1.ThemeIcon("file-directory");
        this.contextValue = 'node';
    }
}
exports.NodeItem = NodeItem;
//# sourceMappingURL=NodeItem.js.map