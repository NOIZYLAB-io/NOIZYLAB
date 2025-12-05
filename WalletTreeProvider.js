"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WalletTreeProvider = void 0;
const vscode = require("vscode");
const NetworkItem_1 = require("../views/trees/NetworkItem");
const OrganizationItem_1 = require("../views/trees/OrganizationItem");
const WalletItem_1 = require("../views/trees/WalletItem");
const HlfProvider_1 = require("./HlfProvider");
const WalletIdentityProvider_1 = require("./WalletIdentityProvider");
const Constants_1 = require("../utilities/Constants");
class WalletTreeProvider {
    constructor() {
        this._onDidChangeTreeData = new vscode.EventEmitter();
        this.onDidChangeTreeData = this._onDidChangeTreeData.event;
    }
    refresh() {
        this._onDidChangeTreeData.fire();
    }
    getTreeItem(element) {
        return element;
    }
    async getChildren(element) {
        const tree = [];
        if (HlfProvider_1.HlfProvider.islocalNetworkStarted) {
            if (element) {
                if (element instanceof NetworkItem_1.NetworkItem) {
                    tree.push(new OrganizationItem_1.OrganizationItem(Constants_1.Settings.singleOrgSettings.name, vscode.TreeItemCollapsibleState.Expanded));
                }
                if (element instanceof OrganizationItem_1.OrganizationItem) {
                    const wallets = await WalletIdentityProvider_1.WalletIdentityProvider.getwallets();
                    wallets.forEach(user => {
                        if (user.toLowerCase() === Constants_1.Settings.singleOrgSettings.adminUser.toLowerCase()) {
                            //Do not allow the default org admin user to be removed.
                            //For this, set the context to some value other than 'wallet'
                            tree.push(new WalletItem_1.WalletItem(user, vscode.TreeItemCollapsibleState.None, user));
                        }
                        else {
                            tree.push(new WalletItem_1.WalletItem(user, vscode.TreeItemCollapsibleState.None));
                        }
                    });
                }
            }
            else {
                tree.push(new NetworkItem_1.NetworkItem("Local Fabric Network", vscode.TreeItemCollapsibleState.Expanded));
            }
        }
        return Promise.resolve(tree);
    }
}
exports.WalletTreeProvider = WalletTreeProvider;
//# sourceMappingURL=WalletTreeProvider.js.map