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
exports.DiagnosticsProvider = void 0;
const vscode = __importStar(require("vscode"));
const FFmpegAudioRecorder_1 = require("../core/FFmpegAudioRecorder");
/**
 * Data provider for diagnostics
 */
class DiagnosticsProvider {
    _onDidChangeTreeData = new vscode.EventEmitter();
    onDidChangeTreeData = this._onDidChangeTreeData.event;
    constructor() { }
    refresh() {
        this._onDidChangeTreeData.fire();
    }
    getTreeItem(element) {
        return element;
    }
    async getChildren(element) {
        if (!element) {
            return this.getDiagnostics();
        }
        return [];
    }
    async getDiagnostics() {
        const items = [];
        // FFmpeg check
        const ffmpegCheck = await FFmpegAudioRecorder_1.FFmpegAudioRecorder.checkFFmpegAvailability();
        const ffmpegItem = new DiagnosticItem('FFmpeg', ffmpegCheck.available ? '✅ Available' : '❌ Not Found', ffmpegCheck.version || ffmpegCheck.error || 'Unknown status');
        ffmpegItem.iconPath = new vscode.ThemeIcon(ffmpegCheck.available ? 'check' : 'error');
        items.push(ffmpegItem);
        // Audio devices
        try {
            const devices = await FFmpegAudioRecorder_1.FFmpegAudioRecorder.detectInputDevices();
            const deviceNames = devices.map(device => device.name);
            const devicesItem = new DiagnosticItem('Audio Devices', devices.length > 0 ? `✅ ${devices.length} Found` : '❌ None Found', devices.length > 0 ? deviceNames.slice(0, 2).join(', ') + (devices.length > 2 ? '...' : '') : 'No devices detected');
            devicesItem.iconPath = new vscode.ThemeIcon(devices.length > 0 ? 'check' : 'error');
            items.push(devicesItem);
        }
        catch (error) {
            const devicesItem = new DiagnosticItem('Audio Devices', '⚠️ Check Failed', error.message);
            devicesItem.iconPath = new vscode.ThemeIcon('warning');
            items.push(devicesItem);
        }
        // API key
        const config = vscode.workspace.getConfiguration('speechToTextWhisper');
        const apiKey = config.get('apiKey');
        const apiItem = new DiagnosticItem('OpenAI API Key', apiKey && apiKey.trim() ? '✅ Configured' : '❌ Missing', apiKey && apiKey.trim() ? 'API key is set' : 'Please configure your OpenAI API key');
        apiItem.iconPath = new vscode.ThemeIcon(apiKey && apiKey.trim() ? 'check' : 'error');
        items.push(apiItem);
        return items;
    }
    async runAllDiagnostics() {
        vscode.window.showInformationMessage('🔧 Running diagnostics...');
        this.refresh();
        vscode.window.showInformationMessage('✅ Diagnostics completed. Check the panel for results.');
    }
}
exports.DiagnosticsProvider = DiagnosticsProvider;
class DiagnosticItem extends vscode.TreeItem {
    label;
    description;
    tooltip;
    constructor(label, description, tooltip) {
        super(label, vscode.TreeItemCollapsibleState.None);
        this.label = label;
        this.description = description;
        this.tooltip = tooltip;
        this.description = description;
        this.tooltip = tooltip;
    }
}
//# sourceMappingURL=DiagnosticsProvider.js.map