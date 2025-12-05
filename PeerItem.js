"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PeerItem = void 0;
const HlfTreeItem_1 = require("./HlfTreeItem");
class PeerItem extends HlfTreeItem_1.HlfTreeItem {
    constructor() {
        super(...arguments);
        this.contextValue = 'peer';
    }
}
exports.PeerItem = PeerItem;
//# sourceMappingURL=PeerItem.js.map