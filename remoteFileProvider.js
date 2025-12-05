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
exports.FileItem = exports.RemoteFileProvider = void 0;
const vscode = __importStar(require("vscode"));
class RemoteFileProvider {
    constructor(sshManager, wslManager) {
        this.sshManager = sshManager;
        this.wslManager = wslManager;
        this._onDidChangeTreeData = new vscode.EventEmitter();
        this.onDidChangeTreeData = this._onDidChangeTreeData.event;
        this.currentPath = '/';
        this.activeConnection = null;
        this.connectionType = null;
    }
    refresh() {
        this._onDidChangeTreeData.fire();
    }
    setActiveConnection(connectionId, type) {
        this.activeConnection = connectionId;
        this.connectionType = type;
        this.currentPath = '/';
        this.refresh();
    }
    navigateToPath(path) {
        this.currentPath = path;
        this.refresh();
    }
    getTreeItem(element) {
        return element;
    }
    async getChildren(element) {
        if (!this.activeConnection || !this.connectionType) {
            return [new FileItem('No active connection', vscode.TreeItemCollapsibleState.None, 'info')];
        }
        const targetPath = element ? element.path : this.currentPath;
        try {
            if (this.connectionType === 'ssh') {
                // For SSH, we would need to implement directory listing
                // This is a simplified version
                return [
                    new FileItem('home', vscode.TreeItemCollapsibleState.Collapsed, 'directory', '/home'),
                    new FileItem('etc', vscode.TreeItemCollapsibleState.Collapsed, 'directory', '/etc'),
                    new FileItem('var', vscode.TreeItemCollapsibleState.Collapsed, 'directory', '/var')
                ];
            }
            else if (this.connectionType === 'wsl' && targetPath) {
                const result = await this.wslManager.executeCommand(`ls -la "${targetPath}"`);
                return this.parseDirectoryListing(result, targetPath);
            }
        }
        catch (error) {
            return [new FileItem(`Error: ${error}`, vscode.TreeItemCollapsibleState.None, 'error')];
        }
        return [];
    }
    parseDirectoryListing(output, basePath) {
        const lines = output.split('\n').filter(line => line.trim());
        const items = [];
        for (const line of lines) {
            const parts = line.trim().split(/\s+/);
            if (parts.length >= 9 && !line.startsWith('total')) {
                const permissions = parts[0];
                const name = parts.slice(8).join(' ');
                if (name === '.' || name === '..')
                    continue;
                const isDirectory = permissions.startsWith('d');
                const fullPath = basePath.endsWith('/') ? `${basePath}${name}` : `${basePath}/${name}`;
                items.push(new FileItem(name, isDirectory ? vscode.TreeItemCollapsibleState.Collapsed : vscode.TreeItemCollapsibleState.None, isDirectory ? 'directory' : 'file', fullPath));
            }
        }
        return items;
    }
}
exports.RemoteFileProvider = RemoteFileProvider;
class FileItem extends vscode.TreeItem {
    constructor(label, collapsibleState, type, path) {
        super(label, collapsibleState);
        this.label = label;
        this.collapsibleState = collapsibleState;
        this.type = type;
        this.path = path;
        this.tooltip = this.path || this.label;
        this.contextValue = type;
        // Set icons and commands based on type
        switch (type) {
            case 'file':
                this.iconPath = new vscode.ThemeIcon('file');
                this.command = {
                    command: 'ssh-wsl.openRemoteFile',
                    title: 'Open File',
                    arguments: [this.path]
                };
                break;
            case 'directory':
                this.iconPath = new vscode.ThemeIcon('folder');
                break;
            case 'info':
                this.iconPath = new vscode.ThemeIcon('info');
                break;
            case 'error':
                this.iconPath = new vscode.ThemeIcon('error');
                break;
        }
    }
}
exports.FileItem = FileItem;
//# sourceMappingURL=remoteFileProvider.js.map