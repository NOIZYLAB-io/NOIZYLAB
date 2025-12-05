"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.NetworkTreeProvider = void 0;
const vscode = require("vscode");
const NetworkItem_1 = require("../views/trees/NetworkItem");
const OrganizationItem_1 = require("../views/trees/OrganizationItem");
const HlfProvider_1 = require("./HlfProvider");
const Constants_1 = require("../utilities/Constants");
const OrganizationRoot_1 = require("../views/trees/OrganizationRoot");
const CaItem_1 = require("../views/trees/CaItem");
const OrdererItem_1 = require("../views/trees/OrdererItem");
const PeerItem_1 = require("../views/trees/PeerItem");
const NodeItem_1 = require("../views/trees/NodeItem");
class NetworkTreeProvider {
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
    getChildren(element) {
        const tree = [];
        //Hardcode the Fabric organization structure for now. Need to make this dynamic when we enable support for multiple organizations
        if (element) {
            if (element instanceof NetworkItem_1.NetworkItem) {
                tree.push(new OrganizationRoot_1.OrganizationRoot("Organizations", vscode.TreeItemCollapsibleState.Expanded));
            }
            else if (element instanceof OrganizationRoot_1.OrganizationRoot) {
                tree.push(new OrganizationItem_1.OrganizationItem(Constants_1.Settings.singleOrgSettings.name, vscode.TreeItemCollapsibleState.Expanded));
            }
            else if (element instanceof OrganizationItem_1.OrganizationItem) {
                tree.push(new NodeItem_1.NodeItem("ca", vscode.TreeItemCollapsibleState.Expanded));
                tree.push(new NodeItem_1.NodeItem("orderer", vscode.TreeItemCollapsibleState.Expanded));
                tree.push(new NodeItem_1.NodeItem("peer", vscode.TreeItemCollapsibleState.Expanded));
            }
            else if (element instanceof NodeItem_1.NodeItem && element.label === "ca") {
                tree.push(new CaItem_1.CaItem(Constants_1.Settings.singleOrgSettings.caDomain, vscode.TreeItemCollapsibleState.None));
            }
            else if (element instanceof NodeItem_1.NodeItem && element.label === "orderer") {
                tree.push(new OrdererItem_1.OrdererItem(Constants_1.Settings.singleOrgSettings.ordererDomain, vscode.TreeItemCollapsibleState.None));
            }
            else if (element instanceof NodeItem_1.NodeItem && element.label === "peer") {
                tree.push(new PeerItem_1.PeerItem(Constants_1.Settings.singleOrgSettings.peerDomain, vscode.TreeItemCollapsibleState.Expanded));
            }
            else if (element instanceof PeerItem_1.PeerItem) {
                tree.push(new vscode.TreeItem(Constants_1.Settings.defaultChaincodeId, vscode.TreeItemCollapsibleState.None));
            }
        }
        else {
            if (HlfProvider_1.HlfProvider.islocalNetworkStarted) {
                tree.push(new NetworkItem_1.NetworkItem("Local Fabric Network", vscode.TreeItemCollapsibleState.Expanded));
            }
            else {
                tree.push(new NetworkItem_1.NetworkItem("Local Fabric Network (Stopped)", vscode.TreeItemCollapsibleState.Collapsed));
            }
        }
        return tree;
    }
}
exports.NetworkTreeProvider = NetworkTreeProvider;
//# sourceMappingURL=NetworkTreeProvider.js.map