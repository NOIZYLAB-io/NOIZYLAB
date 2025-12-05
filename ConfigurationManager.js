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
exports.configurationManager = exports.ConfigurationManager = void 0;
const vscode = __importStar(require("vscode"));
/**
 * Centralized manager for managing extension settings
 * Uses singleton pattern to ensure a single source of truth
 */
class ConfigurationManager {
    static instance;
    cachedConfig = null;
    changeListeners = [];
    disposables = [];
    constructor() {
        // Subscribe to VS Code configuration changes
        const configChangeDisposable = vscode.workspace.onDidChangeConfiguration((event) => {
            if (event.affectsConfiguration('speechToTextWhisper')) {
                this.invalidateCache();
                this.notifyListeners();
            }
        });
        this.disposables.push(configChangeDisposable);
    }
    /**
     * Get the single instance of ConfigurationManager
     */
    static getInstance() {
        if (!ConfigurationManager.instance) {
            ConfigurationManager.instance = new ConfigurationManager();
        }
        return ConfigurationManager.instance;
    }
    /**
     * Get the full configuration
     */
    getConfiguration() {
        if (!this.cachedConfig) {
            this.cachedConfig = this.loadConfiguration();
        }
        return this.cachedConfig;
    }
    /**
     * Get the Whisper configuration
     */
    getWhisperConfiguration() {
        return this.getConfiguration().whisper;
    }
    /**
     * Get the audio configuration
     */
    getAudioConfiguration() {
        return this.getConfiguration().audio;
    }
    /**
     * Get the UI configuration
     */
    getUIConfiguration() {
        return this.getConfiguration().ui;
    }
    /**
     * Get the post-processing configuration
     */
    getPostProcessingConfiguration() {
        return this.getConfiguration().postProcessing;
    }
    /**
     * Set the configuration value
     */
    async setConfigurationValue(section, value) {
        const config = vscode.workspace.getConfiguration('speechToTextWhisper');
        await config.update(section, value, vscode.ConfigurationTarget.Global);
        this.invalidateCache();
    }
    /**
     * Add a configuration change listener
     */
    addChangeListener(listener) {
        this.changeListeners.push(listener);
    }
    /**
     * Remove a configuration change listener
     */
    removeChangeListener(listener) {
        const index = this.changeListeners.indexOf(listener);
        if (index > -1) {
            this.changeListeners.splice(index, 1);
        }
    }
    /**
     * Validate the configuration
     */
    validateConfiguration() {
        const config = this.getConfiguration();
        const errors = [];
        // Validate the Whisper configuration
        if (!config.whisper.apiKey || config.whisper.apiKey.trim() === '') {
            errors.push('Whisper API key is required');
        }
        if (config.whisper.temperature < 0 || config.whisper.temperature > 1) {
            errors.push('Temperature must be between 0 and 1');
        }
        if (config.whisper.timeout <= 0) {
            errors.push('Timeout must be greater than 0');
        }
        if (config.whisper.maxRetries < 0) {
            errors.push('Max retries must be non-negative');
        }
        // Validate the audio configuration
        if (config.audio.maxRecordingDuration <= 0) {
            errors.push('Max recording duration must be greater than 0');
        }
        if (config.audio.silenceDuration <= 0) {
            errors.push('Silence duration must be greater than 0');
        }
        if (config.audio.silenceThreshold < 20 || config.audio.silenceThreshold > 80) {
            errors.push('Silence threshold must be between 20 and 80');
        }
        // Validate the post-processing configuration
        if (config.postProcessing) {
            const validModels = [
                'Without post-processing',
                // GPT-4.1 series (April 2025)
                'gpt-4.1',
                'gpt-4.1-mini',
                'gpt-4.1-nano',
                // GPT-4o series
                'gpt-4o',
                'gpt-4o-mini',
                'gpt-4o-2024-11-20',
                'gpt-4o-2024-08-06',
                'gpt-4o-2024-05-13',
                // GPT-4.5 series
                'gpt-4.5-preview',
                // GPT-4 Turbo
                'gpt-4-turbo',
                'gpt-4-turbo-2024-04-09',
                // o-series models
                'o1',
                'o1-preview',
                'o1-mini',
                'o3',
                'o3-mini',
                'o4-mini',
                // Legacy models
                'gpt-3.5-turbo',
                'gpt-3.5-turbo-0125',
                'gpt-3.5-turbo-1106',
                // Special models
                'chatgpt-4o-latest'
            ];
            if (!validModels.includes(config.postProcessing.model)) {
                errors.push(`Invalid model selection: ${config.postProcessing.model}`);
            }
        }
        if (config.postProcessing) {
            if (config.postProcessing.minTextLength < 0) {
                errors.push('Minimum text length must be non-negative');
            }
            if (config.postProcessing.timeout <= 0) {
                errors.push('Post-processing timeout must be greater than 0');
            }
        }
        return {
            isValid: errors.length === 0,
            errors
        };
    }
    /**
     * Get the default configuration value
     */
    getDefaultConfiguration() {
        return {
            whisper: {
                apiKey: '',
                language: 'auto',
                whisperModel: 'whisper-1',
                prompt: "This is a technical instruction about programming in Visual Studio Code IDE. The speaker provides step-by-step coding instructions related to features, extensions, debugging, and software development workflows. Output should be formatted in markdown with proper code blocks and structure.",
                temperature: 0.1,
                timeout: 30000,
                maxRetries: 3
            },
            audio: {
                audioQuality: 'standard',
                ffmpegPath: '',
                maxRecordingDuration: 3600,
                silenceDetection: true,
                silenceDuration: 3,
                silenceThreshold: 20,
                inputDevice: 'auto'
            },
            ui: {
                showStatusBar: true
            },
            postProcessing: {
                model: 'gpt-4.1-mini',
                prompt: 'Please improve this transcribed text by:\n1. Adding proper punctuation and capitalization\n2. Removing filler words (um, uh, like, you know)\n3. Structuring sentences for better readability\n4. Maintaining the original meaning and technical terms\n\nOriginal text:',
                minTextLength: 50,
                timeout: 30000
            }
        };
    }
    /**
     * Reset the configuration to default values
     */
    async resetToDefaults() {
        const defaultConfig = this.getDefaultConfiguration();
        const config = vscode.workspace.getConfiguration('speechToTextWhisper');
        // Reset Whisper settings
        await config.update('language', defaultConfig.whisper.language, vscode.ConfigurationTarget.Global);
        await config.update('whisperModel', defaultConfig.whisper.whisperModel, vscode.ConfigurationTarget.Global);
        await config.update('prompt', defaultConfig.whisper.prompt, vscode.ConfigurationTarget.Global);
        await config.update('temperature', defaultConfig.whisper.temperature, vscode.ConfigurationTarget.Global);
        await config.update('timeout', defaultConfig.whisper.timeout, vscode.ConfigurationTarget.Global);
        await config.update('maxRetries', defaultConfig.whisper.maxRetries, vscode.ConfigurationTarget.Global);
        // Reset audio settings
        await config.update('audioQuality', defaultConfig.audio.audioQuality, vscode.ConfigurationTarget.Global);
        await config.update('ffmpegPath', defaultConfig.audio.ffmpegPath, vscode.ConfigurationTarget.Global);
        await config.update('maxRecordingDuration', defaultConfig.audio.maxRecordingDuration, vscode.ConfigurationTarget.Global);
        await config.update('silenceDetection', defaultConfig.audio.silenceDetection, vscode.ConfigurationTarget.Global);
        await config.update('silenceDuration', defaultConfig.audio.silenceDuration, vscode.ConfigurationTarget.Global);
        await config.update('silenceThreshold', defaultConfig.audio.silenceThreshold, vscode.ConfigurationTarget.Global);
        await config.update('inputDevice', defaultConfig.audio.inputDevice, vscode.ConfigurationTarget.Global);
        // Reset UI settings
        await config.update('showStatusBar', defaultConfig.ui.showStatusBar, vscode.ConfigurationTarget.Global);
        // Reset post-processing settings
        await config.update('postProcessing.model', defaultConfig.postProcessing.model, vscode.ConfigurationTarget.Global);
        await config.update('postProcessing.prompt', defaultConfig.postProcessing.prompt, vscode.ConfigurationTarget.Global);
        await config.update('postProcessing.minTextLength', defaultConfig.postProcessing.minTextLength, vscode.ConfigurationTarget.Global);
        await config.update('postProcessing.timeout', defaultConfig.postProcessing.timeout, vscode.ConfigurationTarget.Global);
        this.invalidateCache();
    }
    /**
     * Release resources
     */
    dispose() {
        this.disposables.forEach(disposable => disposable.dispose());
        this.disposables = [];
        this.changeListeners = [];
        this.cachedConfig = null;
    }
    /**
     * Load the configuration from VS Code settings
     */
    loadConfiguration() {
        const config = vscode.workspace.getConfiguration('speechToTextWhisper');
        const defaultConfig = this.getDefaultConfiguration();
        return {
            whisper: {
                apiKey: config.get('apiKey', defaultConfig.whisper.apiKey),
                language: config.get('language', defaultConfig.whisper.language),
                whisperModel: config.get('whisperModel', defaultConfig.whisper.whisperModel),
                prompt: config.get('prompt', defaultConfig.whisper.prompt),
                temperature: config.get('temperature', defaultConfig.whisper.temperature),
                timeout: config.get('timeout', defaultConfig.whisper.timeout),
                maxRetries: config.get('maxRetries', defaultConfig.whisper.maxRetries)
            },
            audio: {
                audioQuality: config.get('audioQuality', defaultConfig.audio.audioQuality),
                ffmpegPath: config.get('ffmpegPath', defaultConfig.audio.ffmpegPath),
                maxRecordingDuration: config.get('maxRecordingDuration', defaultConfig.audio.maxRecordingDuration),
                silenceDetection: config.get('silenceDetection', defaultConfig.audio.silenceDetection),
                silenceDuration: config.get('silenceDuration', defaultConfig.audio.silenceDuration),
                silenceThreshold: config.get('silenceThreshold', defaultConfig.audio.silenceThreshold),
                inputDevice: config.get('inputDevice', defaultConfig.audio.inputDevice)
            },
            ui: {
                showStatusBar: config.get('showStatusBar', defaultConfig.ui.showStatusBar)
            },
            postProcessing: {
                model: config.get('postProcessing.model', defaultConfig.postProcessing.model),
                prompt: config.get('postProcessing.prompt', defaultConfig.postProcessing.prompt),
                minTextLength: config.get('postProcessing.minTextLength', defaultConfig.postProcessing.minTextLength),
                timeout: config.get('postProcessing.timeout', defaultConfig.postProcessing.timeout)
            }
        };
    }
    /**
     * Clear the configuration cache
     */
    invalidateCache() {
        this.cachedConfig = null;
    }
    /**
     * Notify all listeners about configuration changes
     */
    notifyListeners() {
        const config = this.getConfiguration();
        this.changeListeners.forEach(listener => {
            try {
                listener(config);
            }
            catch (error) {
                console.error('Error in configuration change listener:', error);
            }
        });
    }
}
exports.ConfigurationManager = ConfigurationManager;
// Export the single instance for convenience
exports.configurationManager = ConfigurationManager.getInstance();
//# sourceMappingURL=ConfigurationManager.js.map