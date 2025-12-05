"use strict";
// AudioQualityManager.ts - Audio quality settings manager
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
exports.AudioQualityManager = void 0;
const vscode = __importStar(require("vscode"));
const GlobalOutput_1 = require("./GlobalOutput");
/**
 * Audio quality settings manager for SpeechToTextWhisper
 */
class AudioQualityManager {
    static QUALITY_PRESETS = [
        {
            name: 'standard',
            description: 'Standard quality (16kHz, 64kbps)',
            settings: {
                quality: 'standard',
                sampleRate: 16000,
                channelCount: 1,
                audioFormat: 'webm'
            },
            recommendedFor: ['general use', 'quick notes', 'basic transcription']
        },
        {
            name: 'high',
            description: 'High quality (44.1kHz, 128kbps)',
            settings: {
                quality: 'high',
                sampleRate: 44100,
                channelCount: 1,
                audioFormat: 'wav'
            },
            recommendedFor: ['meetings', 'interviews', 'important content']
        },
        {
            name: 'ultra',
            description: 'Maximum quality (48kHz, 256kbps)',
            settings: {
                quality: 'ultra',
                sampleRate: 48000,
                channelCount: 1,
                audioFormat: 'wav'
            },
            recommendedFor: ['critical recordings', 'noisy environments', 'technical dictation']
        }
    ];
    /**
     * Gets the current audio quality settings from the VS Code configuration
     */
    static getCurrentSettings() {
        const config = vscode.workspace.getConfiguration('speechToTextWhisper');
        return {
            quality: config.get('audioQuality', 'standard'),
            audioFormat: config.get('audioFormat', 'wav'),
            sampleRate: config.get('sampleRate'),
            channelCount: config.get('channels'),
            echoCancellation: config.get('echoCancellation', true),
            noiseSuppression: config.get('noiseSuppression', true),
            autoGainControl: config.get('autoGain', true),
            silenceDetection: config.get('silenceDetection', true),
            silenceThreshold: config.get('silenceThreshold', 2.0)
        };
    }
    /**
     * Applies the quality preset to the VS Code settings
     */
    static async applyQualityPreset(presetName) {
        const preset = this.QUALITY_PRESETS.find(p => p.name === presetName);
        if (!preset) {
            throw new Error(`Quality preset '${presetName}' not found`);
        }
        const config = vscode.workspace.getConfiguration('speechToTextWhisper');
        // Mapping keys between the internal interface and VSCode settings
        const keyMapping = {
            'quality': 'audioQuality',
            'channelCount': 'channels',
            'autoGainControl': 'autoGain'
        };
        // Apply settings from the preset
        for (const [key, value] of Object.entries(preset.settings)) {
            if (value !== undefined) {
                const configKey = keyMapping[key] || key;
                await config.update(configKey, value, vscode.ConfigurationTarget.Global);
            }
        }
        GlobalOutput_1.AudioQualityManagerLog.info(`Applied audio quality preset: ${preset.name}`);
    }
    /**
     * Gets the list of available quality presets
     */
    static getAvailablePresets() {
        return [...this.QUALITY_PRESETS];
    }
    /**
     * Optimizes the quality settings based on the usage context
     */
    static getOptimizedSettings(context) {
        const baseSettings = this.getCurrentSettings();
        switch (context) {
            case 'meeting':
                return {
                    ...baseSettings,
                    quality: 'high',
                    echoCancellation: true,
                    noiseSuppression: true,
                    silenceDetection: false // Don't interrupt on pauses in conversation
                };
            case 'dictation':
                return {
                    ...baseSettings,
                    quality: 'high',
                    echoCancellation: true,
                    noiseSuppression: true,
                    silenceDetection: true,
                    silenceThreshold: 3.0 // Wait longer before stopping
                };
            case 'quick_notes':
                return {
                    ...baseSettings,
                    quality: 'standard',
                    silenceDetection: true,
                    silenceThreshold: 1.5 // Fast stop
                };
            case 'noisy_environment':
                return {
                    ...baseSettings,
                    quality: 'ultra',
                    echoCancellation: true,
                    noiseSuppression: true,
                    autoGainControl: true,
                    silenceThreshold: 4.0 // More time for noise filtering
                };
            default:
                return baseSettings;
        }
    }
    /**
     * Validates the quality settings for compatibility with the browser
     */
    static validateSettings(settings) {
        const warnings = [];
        const suggestions = [];
        let isValid = true;
        // Check support for high sample rate
        if (settings.sampleRate && settings.sampleRate > 48000) {
            warnings.push('Sample rate above 48kHz may not be supported by all browsers');
            suggestions.push('Consider using 48kHz for maximum compatibility');
        }
        // Check the combination of format and quality
        if (settings.quality === 'ultra' && settings.audioFormat === 'mp3') {
            warnings.push('MP3 format may not provide maximum quality for ultra mode');
            suggestions.push('Use WAV format for ultra quality');
        }
        // Check the silence detection settings
        if (settings.silenceDetection && settings.silenceThreshold < 0.5) {
            warnings.push('Too low silence threshold may lead to premature stop of recording');
            suggestions.push('Recommended silence threshold is at least 1 second');
        }
        return { isValid, warnings, suggestions };
    }
    /**
     * Returns recommendations for performance optimization
     */
    static getPerformanceRecommendations(settings) {
        const recommendations = [];
        if (settings.quality === 'ultra') {
            recommendations.push('Ultra quality consumes more resources. Use for critical recordings.');
        }
        if (settings.audioFormat === 'wav' && settings.quality === 'standard') {
            recommendations.push('WAV format with standard quality may be excessive. Consider WebM for better compression.');
        }
        if (!settings.echoCancellation && !settings.noiseSuppression) {
            recommendations.push('Disabling echo cancellation and noise suppression may degrade quality in noisy environments.');
        }
        if (settings.silenceDetection && settings.silenceThreshold > 5.0) {
            recommendations.push('High silence threshold may miss short pauses in speech.');
        }
        return recommendations;
    }
    /**
     * Exports the current settings to JSON
     */
    static exportSettings() {
        const settings = this.getCurrentSettings();
        return JSON.stringify(settings, null, 2);
    }
    /**
     * Imports settings from JSON
     */
    static async importSettings(settingsJson) {
        try {
            const settings = JSON.parse(settingsJson);
            const validation = this.validateSettings(settings);
            if (!validation.isValid) {
                throw new Error(`Invalid settings: ${validation.warnings.join(', ')}`);
            }
            const config = vscode.workspace.getConfiguration('speechToTextWhisper');
            // Mapping keys between the internal interface and VSCode settings
            const keyMapping = {
                'quality': 'audioQuality',
                'channelCount': 'channels',
                'autoGainControl': 'autoGain'
            };
            // Apply settings
            for (const [key, value] of Object.entries(settings)) {
                if (value !== undefined) {
                    const configKey = keyMapping[key] || key;
                    await config.update(configKey, value, vscode.ConfigurationTarget.Global);
                }
            }
            GlobalOutput_1.AudioQualityManagerLog.info('Audio quality settings imported successfully');
        }
        catch (error) {
            throw new Error(`Failed to import settings: ${error.message}`);
        }
    }
}
exports.AudioQualityManager = AudioQualityManager;
//# sourceMappingURL=AudioQualityManager.js.map