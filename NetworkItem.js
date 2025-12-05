"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.NetworkItem = void 0;
const path = require("path");
const HlfTreeItem_1 = require("./HlfTreeItem");
class NetworkItem extends HlfTreeItem_1.HlfTreeItem {
    constructor() {
        super(...arguments);
        this.iconPath = {
            light: path.join(__filename, '..', '..', '..', '..', 'media', 'network-black.png'),
            dark: path.join(__filename, '..', '..', '..', '..', 'media', 'network-white.png')
        };
        this.contextValue = 'network';
    }
}
exports.NetworkItem = NetworkItem;
//# sourceMappingURL=NetworkItem.js.map