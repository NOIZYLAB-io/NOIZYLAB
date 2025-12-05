"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.OrganizationItem = void 0;
const path = require("path");
const HlfTreeItem_1 = require("./HlfTreeItem");
class OrganizationItem extends HlfTreeItem_1.HlfTreeItem {
    constructor() {
        super(...arguments);
        this.iconPath = {
            light: path.join(__filename, '..', '..', '..', '..', 'media', 'organizations-black.png'),
            dark: path.join(__filename, '..', '..', '..', '..', 'media', 'organizations-white.png')
        };
        this.contextValue = 'organization';
    }
}
exports.OrganizationItem = OrganizationItem;
//# sourceMappingURL=OrganizationItem.js.map