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
exports.DeviceManagerProvider = void 0;
const vscode = __importStar(require("vscode"));
const FFmpegAudioRecorder_1 = require("../core/FFmpegAudioRecorder");
/**
 * Data provider for managing audio devices
 */
class DeviceManagerProvider {
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
            return this.getAudioDevices();
        }
        return [];
    }
    async getAudioDevices() {
        const config = vscode.workspace.getConfiguration('speechToTextWhisper');
        const selectedDeviceId = config.get('inputDevice') || 'auto';
        try {
            const devices = await FFmpegAudioRecorder_1.FFmpegAudioRecorder.detectInputDevices();
            const items = [];
            devices.forEach((device, index) => {
                const isSelected = selectedDeviceId === device.id || (selectedDeviceId === 'auto' && device.isDefault);
                const statusText = isSelected ? '✅ Selected' : (device.isDefault ? '⭐ Default' : '');
                const deviceItem = new DeviceItem(device.name, statusText, vscode.TreeItemCollapsibleState.None);
                deviceItem.iconPath = new vscode.ThemeIcon(isSelected ? 'check' : 'device-microphone');
                deviceItem.contextValue = 'audioDevice';
                deviceItem.command = {
                    command: 'speechToTextWhisper.audioSettings.selectDevice',
                    title: 'Select Device',
                    arguments: [device.id]
                };
                deviceItem.tooltip = `${device.name} (ID: ${device.id})${device.isDefault ? ' - Default' : ''}`;
                items.push(deviceItem);
            });
            return items;
        }
        catch (error) {
            const errorItem = new DeviceItem('❌ Device Detection Failed', error.message, vscode.TreeItemCollapsibleState.None);
            errorItem.iconPath = new vscode.ThemeIcon('error');
            return [errorItem];
        }
    }
    async selectDevice(deviceId) {
        try {
            const config = vscode.workspace.getConfiguration('speechToTextWhisper');
            await config.update('inputDevice', deviceId, vscode.ConfigurationTarget.Global);
            const devices = await FFmpegAudioRecorder_1.FFmpegAudioRecorder.detectInputDevices();
            const selectedDevice = devices.find(device => device.id === deviceId);
            const deviceName = selectedDevice?.name || deviceId;
            this.refresh();
            vscode.window.showInformationMessage(`✅ Selected audio device: ${deviceName}`);
        }
        catch (error) {
            vscode.window.showErrorMessage(`Failed to select device: ${error.message}`);
        }
    }
    async testDevice(deviceId) {
        try {
            const devices = await FFmpegAudioRecorder_1.FFmpegAudioRecorder.detectInputDevices();
            const device = devices.find(d => d.id === deviceId);
            const deviceName = device?.name || deviceId;
            vscode.window.showInformationMessage(`🎤 Testing device: ${deviceName}...`);
            if (device) {
                vscode.window.showInformationMessage(`✅ Device "${deviceName}" is available`);
            }
            else {
                vscode.window.showWarningMessage(`⚠️ Device "${deviceName}" not found`);
            }
        }
        catch (error) {
            vscode.window.showErrorMessage(`❌ Device test failed: ${error.message}`);
        }
    }
}
exports.DeviceManagerProvider = DeviceManagerProvider;
class DeviceItem extends vscode.TreeItem {
    label;
    description;
    collapsibleState;
    constructor(label, description, collapsibleState) {
        super(label, collapsibleState);
        this.label = label;
        this.description = description;
        this.collapsibleState = collapsibleState;
        this.description = description;
        this.tooltip = `${label}: ${description}`;
    }
}
//# sourceMappingURL=DeviceManagerProvider.js.map