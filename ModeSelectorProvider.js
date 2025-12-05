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
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.ModeSelectorProvider = void 0;
const vscode = __importStar(require("vscode"));
/**
 * Data provider for switching recording modes
 */
class ModeSelectorProvider {
    _onDidChangeTreeData = new vscode.EventEmitter();
    onDidChangeTreeData = this._onDidChangeTreeData.event;
    currentMode = 'insert';
    constructor() { }
    refresh() {
        this._onDidChangeTreeData.fire();
    }
    getTreeItem(element) {
        return element;
    }
    async getChildren(element) {
        if (!element) {
            return this.getModeItems();
        }
        return [];
    }
    async getModeItems() {
        const items = [];
        // Option for the "Insert Text" mode with a checkmark
        const insertModeItem = new ModeItem('Insert Text', 'Insert transcribed text at cursor position', vscode.TreeItemCollapsibleState.None);
        insertModeItem.iconPath = this.currentMode === 'insert' ? new vscode.ThemeIcon('check') : undefined;
        insertModeItem.command = {
            command: 'speechToTextWhisper.setMode',
            title: 'Set Insert Mode',
            arguments: ['insert']
        };
        items.push(insertModeItem);
        // Option for the "Copy to Clipboard" mode with a checkmark
        const clipboardModeItem = new ModeItem('Copy to Clipboard', 'Copy transcribed text to clipboard', vscode.TreeItemCollapsibleState.None);
        clipboardModeItem.iconPath = this.currentMode === 'clipboard' ? new vscode.ThemeIcon('check') : undefined;
        clipboardModeItem.command = {
            command: 'speechToTextWhisper.setMode',
            title: 'Set Clipboard Mode',
            arguments: ['clipboard']
        };
        items.push(clipboardModeItem);
        return items;
    }
    getCurrentMode() {
        return this.currentMode;
    }
    toggleMode() {
        const oldMode = this.currentMode;
        this.currentMode = this.currentMode === 'insert' ? 'clipboard' : 'insert';
        this.refresh();
        // Show a notification about the mode change
        const modeText = this.currentMode === 'insert' ? 'Insert Text' : 'Copy to Clipboard';
        vscode.window.showInformationMessage(`🔄 Mode switched to: ${modeText}`);
    }
    setMode(mode) {
        if (this.currentMode !== mode) {
            const oldMode = this.currentMode;
            this.currentMode = mode;
            this.refresh();
            // Show a notification about the mode change
            const modeText = mode === 'insert' ? 'Insert Text' : 'Copy to Clipboard';
            vscode.window.showInformationMessage(`✓ Mode set to: ${modeText}`);
        }
    }
}
exports.ModeSelectorProvider = ModeSelectorProvider;
class ModeItem extends vscode.TreeItem {
    label;
    tooltip;
    collapsibleState;
    constructor(label, tooltip, collapsibleState) {
        super(label, collapsibleState);
        this.label = label;
        this.tooltip = tooltip;
        this.collapsibleState = collapsibleState;
        this.tooltip = tooltip;
    }
}
//# sourceMappingURL=ModeSelectorProvider.js.map