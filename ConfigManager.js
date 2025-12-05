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
exports.ConfigManager = void 0;
const vscode = __importStar(require("vscode"));
const types_1 = require("./types");
class ConfigManager {
    constructor() {
        this.configuration = vscode.workspace.getConfiguration('soundNotification');
        this.setupConfigurationWatcher();
    }
    static getInstance() {
        if (!ConfigManager.instance) {
            ConfigManager.instance = new ConfigManager();
        }
        return ConfigManager.instance;
    }
    setupConfigurationWatcher() {
        vscode.workspace.onDidChangeConfiguration((event) => {
            if (event.affectsConfiguration('soundNotification')) {
                this.configuration = vscode.workspace.getConfiguration('soundNotification');
            }
        });
    }
    getConfiguration() {
        return {
            enabled: this.configuration.get('enabled', true),
            volume: this.configuration.get('volume', 0.5),
            events: {
                onSave: this.configuration.get('events.onSave', true),
            },
            customSounds: {
                save: this.configuration.get('customSounds.save', ''),
            }
        };
    }
    isEnabled() {
        return this.configuration.get('enabled', true);
    }
    getVolume() {
        return this.configuration.get('volume', 0.5);
    }
    isEventEnabled(eventType) {
        const config = this.getConfiguration();
        switch (eventType) {
            case types_1.SoundEventType.SAVE:
                return config.events.onSave;
            default:
                return false;
        }
    }
    getCustomSoundPath(eventType) {
        const config = this.getConfiguration();
        switch (eventType) {
            case types_1.SoundEventType.SAVE:
                return config.customSounds.save;
            default:
                return '';
        }
    }
    async toggleSounds() {
        const currentState = this.isEnabled();
        await this.configuration.update('enabled', !currentState, vscode.ConfigurationTarget.Global);
    }
    async setVolume(volume) {
        const clampedVolume = Math.max(0, Math.min(1, volume));
        await this.configuration.update('volume', clampedVolume, vscode.ConfigurationTarget.Global);
    }
    openSettings() {
        vscode.commands.executeCommand('workbench.action.openSettings', 'soundNotification');
    }
}
exports.ConfigManager = ConfigManager;
//# sourceMappingURL=configManager.js.map