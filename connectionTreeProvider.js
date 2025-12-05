"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.ConnectionItem = exports.ConnectionTreeProvider = void 0;
const vscode = __importStar(require("vscode"));
class ConnectionTreeProvider {
    constructor(sshManager, wslManager) {
        this.sshManager = sshManager;
        this.wslManager = wslManager;
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
        if (!element) {
            // Root level - show SSH and WSL categories
            return Promise.resolve([
                new ConnectionItem('SSH Connections', vscode.TreeItemCollapsibleState.Expanded, 'category'),
                new ConnectionItem('WSL Connections', vscode.TreeItemCollapsibleState.Expanded, 'category')
            ]);
        }
        if (element.label === 'SSH Connections') {
            const sshConnections = this.sshManager.listConnections();
            return Promise.resolve(sshConnections.map(conn => new ConnectionItem(conn, vscode.TreeItemCollapsibleState.None, 'ssh', {
                command: 'ssh-wsl.selectConnection',
                title: 'Select Connection',
                arguments: [conn]
            })));
        }
        if (element.label === 'WSL Connections') {
            const wslConnections = this.wslManager.listConnections();
            return Promise.resolve(wslConnections.map(conn => new ConnectionItem(conn, vscode.TreeItemCollapsibleState.None, 'wsl', {
                command: 'ssh-wsl.selectConnection',
                title: 'Select Connection',
                arguments: [conn]
            })));
        }
        return Promise.resolve([]);
    }
}
exports.ConnectionTreeProvider = ConnectionTreeProvider;
class ConnectionItem extends vscode.TreeItem {
    constructor(label, collapsibleState, type, command) {
        super(label, collapsibleState);
        this.label = label;
        this.collapsibleState = collapsibleState;
        this.type = type;
        this.command = command;
        this.tooltip = `${this.label}`;
        this.contextValue = type;
        // Set icons based on type
        switch (type) {
            case 'ssh':
                this.iconPath = new vscode.ThemeIcon('server');
                break;
            case 'wsl':
                this.iconPath = new vscode.ThemeIcon('terminal-linux');
                break;
            case 'category':
                this.iconPath = new vscode.ThemeIcon('folder');
                break;
        }
    }
}
exports.ConnectionItem = ConnectionItem;
//# sourceMappingURL=connectionTreeProvider.js.map