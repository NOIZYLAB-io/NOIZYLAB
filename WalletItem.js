"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WalletItem = void 0;
const path = require("path");
const HlfTreeItem_1 = require("./HlfTreeItem");
class WalletItem extends HlfTreeItem_1.HlfTreeItem {
    constructor(label, collapsibleState, context = 'wallet') {
        super(label, collapsibleState);
        this.iconPath = {
            light: path.join(__filename, '..', '..', '..', '..', 'media', 'wallet-black.png'),
            dark: path.join(__filename, '..', '..', '..', '..', 'media', 'wallet-white.png')
        };
        this.contextValue = context;
    }
}
exports.WalletItem = WalletItem;
//# sourceMappingURL=WalletItem.js.map