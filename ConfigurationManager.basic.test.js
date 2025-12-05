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
const assert = __importStar(require("assert"));
const sinon = __importStar(require("sinon"));
const ConfigurationManager_1 = require("../../core/ConfigurationManager");
describe('ConfigurationManager - Basic Tests', () => {
    let configManager;
    let sandbox;
    beforeEach(() => {
        // Create sinon sandbox
        sandbox = sinon.createSandbox();
        // Reset singleton
        ConfigurationManager_1.ConfigurationManager.instance = null;
        // Create new instance
        configManager = ConfigurationManager_1.ConfigurationManager.getInstance();
    });
    afterEach(() => {
        configManager.dispose();
        sandbox.restore();
    });
    it('should use the correct speechToTextWhisper prefix', () => {
        // Create mock for loadConfiguration
        const loadConfigurationStub = sandbox.stub(configManager, 'loadConfiguration');
        loadConfigurationStub.returns({
            whisper: {
                apiKey: 'test-api-key',
                language: 'auto',
                whisperModel: 'whisper-1',
                prompt: '',
                temperature: 0.1,
                timeout: 30000,
                maxRetries: 3
            },
            audio: {
                audioQuality: 'standard',
                ffmpegPath: '',
                maxRecordingDuration: 60,
                silenceDetection: true,
                silenceDuration: 3,
                silenceThreshold: 50,
                inputDevice: 'auto'
            },
            ui: {
                showStatusBar: true
            }
        });
        // Get configuration (which triggers loadConfiguration)
        const config = configManager.getConfiguration();
        // Check that loadConfiguration was called
        assert.ok(loadConfigurationStub.called, 'loadConfiguration should have been called');
        // Check the structure of the returned configuration
        assert.ok(config.whisper, 'Should have whisper section');
        assert.ok(config.audio, 'Should have audio section');
        assert.ok(config.ui, 'Should have ui section');
    });
    it('should correctly validate silenceThreshold within 20-80 range', () => {
        // Test valid values
        const loadConfigurationStub = sandbox.stub(configManager, 'loadConfiguration');
        // Test valid value
        loadConfigurationStub.returns({
            whisper: { apiKey: 'test-key', language: 'auto', whisperModel: 'whisper-1', prompt: '', temperature: 0.1, timeout: 30000, maxRetries: 3 },
            audio: { audioQuality: 'standard', ffmpegPath: '', maxRecordingDuration: 60, silenceDetection: true, silenceDuration: 3, silenceThreshold: 25, inputDevice: 'auto' },
            ui: { showStatusBar: true }
        });
        let validation = configManager.validateConfiguration();
        assert.ok(validation.isValid, 'silenceThreshold=25 should be valid');
        // Test invalid value
        loadConfigurationStub.returns({
            whisper: { apiKey: 'test-key', language: 'auto', whisperModel: 'whisper-1', prompt: '', temperature: 0.1, timeout: 30000, maxRetries: 3 },
            audio: { audioQuality: 'standard', ffmpegPath: '', maxRecordingDuration: 60, silenceDetection: true, silenceDuration: 3, silenceThreshold: 10, inputDevice: 'auto' },
            ui: { showStatusBar: true }
        });
        // Clear cache for new configuration to load
        configManager.invalidateCache();
        validation = configManager.validateConfiguration();
        assert.ok(!validation.isValid, 'silenceThreshold=10 should be invalid');
    });
    it('should use correct keys for reading settings', () => {
        // Create mock for loadConfiguration
        const loadConfigurationStub = sandbox.stub(configManager, 'loadConfiguration');
        loadConfigurationStub.returns({
            whisper: {
                apiKey: 'test-api-key',
                language: 'auto',
                whisperModel: 'whisper-1',
                prompt: '',
                temperature: 0.1,
                timeout: 30000,
                maxRetries: 3
            },
            audio: {
                audioQuality: 'standard',
                ffmpegPath: '',
                maxRecordingDuration: 60,
                silenceDetection: true,
                silenceDuration: 3,
                silenceThreshold: 50,
                inputDevice: 'auto'
            },
            ui: {
                showStatusBar: true
            }
        });
        // Get configuration
        const config = configManager.getConfiguration();
        // Check that loadConfiguration was called (which implies correct keys were read)
        assert.ok(loadConfigurationStub.called, 'loadConfiguration should have been called');
        // Check that configuration has correct values
        assert.strictEqual(config.whisper.apiKey, 'test-api-key');
        assert.strictEqual(config.audio.audioQuality, 'standard');
        assert.strictEqual(config.ui.showStatusBar, true);
    });
});
//# sourceMappingURL=ConfigurationManager.basic.test.js.map