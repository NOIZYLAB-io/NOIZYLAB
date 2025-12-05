"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.OrdererItem = void 0;
const HlfTreeItem_1 = require("./HlfTreeItem");
class OrdererItem extends HlfTreeItem_1.HlfTreeItem {
    constructor() {
        super(...arguments);
        this.contextValue = 'orderer';
    }
}
exports.OrdererItem = OrdererItem;
//# sourceMappingURL=OrdererItem.js.map