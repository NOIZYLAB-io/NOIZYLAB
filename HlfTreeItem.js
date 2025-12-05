"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.HlfTreeItem = void 0;
const vscode = require("vscode");
class HlfTreeItem extends vscode.TreeItem {
    constructor() {
        super(...arguments);
        this.contextValue = 'hlf-tree-item';
    }
}
exports.HlfTreeItem = HlfTreeItem;
//# sourceMappingURL=HlfTreeItem.js.map