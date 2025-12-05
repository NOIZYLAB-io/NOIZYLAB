"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ResourceItem = void 0;
const vscode = require("vscode");
const HlfTreeItem_1 = require("./HlfTreeItem");
class ResourceItem extends HlfTreeItem_1.HlfTreeItem {
    constructor(message, description, icon, link) {
        super(message, vscode.TreeItemCollapsibleState.None);
        this.message = message;
        this.description = description;
        this.icon = icon;
        this.link = link;
        this.contextValue = 'resource';
    }
    getTreeItem() {
        const item = new vscode.TreeItem(this.message, vscode.TreeItemCollapsibleState.None);
        item.tooltip = this.message;
        item.description = this.description;
        item.resourceUri = vscode.Uri.parse(this.link);
        item.iconPath = this.icon;
        item.command = {
            command: "hlf.link.open",
            title: '',
            arguments: [item.resourceUri, this.message],
        };
        return item;
    }
}
exports.ResourceItem = ResourceItem;
//# sourceMappingURL=ResourceItem.js.map