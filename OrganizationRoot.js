"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.OrganizationRoot = void 0;
const path = require("path");
const HlfTreeItem_1 = require("./HlfTreeItem");
class OrganizationRoot extends HlfTreeItem_1.HlfTreeItem {
    constructor() {
        super(...arguments);
        this.iconPath = {
            light: path.join(__filename, '..', '..', '..', '..', 'media', 'organizations-black.png'),
            dark: path.join(__filename, '..', '..', '..', '..', 'media', 'organizations-white.png')
        };
        this.contextValue = 'organizationRoot';
    }
}
exports.OrganizationRoot = OrganizationRoot;
//# sourceMappingURL=OrganizationRoot.js.map