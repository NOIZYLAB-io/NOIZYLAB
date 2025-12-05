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
exports.SoundManager = void 0;
const path = __importStar(require("path"));
const fs = __importStar(require("fs"));
const child_process_1 = require("child_process");
const util_1 = require("util");
const types_1 = require("./types");
const configManager_1 = require("./configManager");
const execAsync = (0, util_1.promisify)(child_process_1.exec);
class SoundManager {
    constructor(extensionPath) {
        this.extensionPath = extensionPath;
        this.configManager = configManager_1.ConfigManager.getInstance();
        this.defaultSounds = new Map();
        this.initializeDefaultSounds();
    }
    static getInstance(extensionPath) {
        if (!SoundManager.instance && extensionPath) {
            SoundManager.instance = new SoundManager(extensionPath);
        }
        return SoundManager.instance;
    }
    initializeDefaultSounds() {
        const soundsPath = path.join(this.extensionPath, 'sounds');
        this.defaultSounds.set(types_1.SoundEventType.SAVE, path.join(soundsPath, 'completion.wav'));
    }
    async playSound(eventType, options) {
        try {
            // Check if sounds are globally enabled
            if (!this.configManager.isEnabled()) {
                return;
            }
            // Check if this specific event is enabled
            if (!this.configManager.isEventEnabled(eventType)) {
                return;
            }
            // Determine which sound file to use
            const soundPath = this.getSoundPath(eventType, options?.customPath);
            if (!soundPath || !fs.existsSync(soundPath)) {
                console.warn(`Sound file not found: ${soundPath}`);
                return;
            }
            // Get volume setting
            const volume = options?.volume ?? this.configManager.getVolume();
            // Play the sound (non-blocking)
            this.playSoundFile(soundPath, volume).catch(error => {
                console.error('Error playing sound:', error);
            });
        }
        catch (error) {
            console.error('Error in playSound:', error);
        }
    }
    getSoundPath(eventType, customPath) {
        // Use custom path if provided and valid
        if (customPath && fs.existsSync(customPath)) {
            return customPath;
        }
        // Use configured custom sound path
        const configCustomPath = this.configManager.getCustomSoundPath(eventType);
        if (configCustomPath && fs.existsSync(configCustomPath)) {
            return configCustomPath;
        }
        // Fall back to default sound
        return this.defaultSounds.get(eventType) || '';
    }
    playSoundFile(soundPath, volume) {
        return new Promise((resolve, reject) => {
            try {
                const absolutePath = path.resolve(soundPath);
                console.log(`Playing audio file: ${absolutePath}`);
                if (process.platform === 'win32') {
                    // Use PowerShell on Windows
                    this.playWithPowerShell(absolutePath)
                        .then(() => {
                        console.log('Audio playback finished');
                        resolve();
                    })
                        .catch((error) => {
                        console.warn('PowerShell audio failed:', error.message);
                        resolve(); // Don't break extension if audio fails
                    });
                }
                else {
                    // Use alternative methods for other platforms
                    this.playWithSystemCommand(absolutePath)
                        .then(() => {
                        console.log('Audio playback finished');
                        resolve();
                    })
                        .catch((error) => {
                        console.warn('System audio failed:', error.message);
                        resolve(); // Don't break extension if audio fails
                    });
                }
            }
            catch (error) {
                console.error('Error in playSoundFile:', error);
                resolve(); // Don't break extension if audio fails
            }
        });
    }
    /**
     * Play audio using PowerShell (Windows)
     */
    async playWithPowerShell(filePath) {
        // Primary method: Use Windows Media Player COM object
        const command = `powershell -Command "& {Add-Type -AssemblyName presentationCore; $mediaPlayer = New-Object system.windows.media.mediaplayer; $mediaPlayer.open('${filePath}'); $mediaPlayer.Play(); Start-Sleep -Seconds 1; do { Start-Sleep -Milliseconds 100 } while ($mediaPlayer.Position -lt $mediaPlayer.NaturalDuration.TimeSpan); $mediaPlayer.Stop(); $mediaPlayer.Close()}"`;
        try {
            await execAsync(command);
        }
        catch (error) {
            // Fallback to simpler PowerShell method
            console.log('Trying simpler PowerShell method...');
            const simpleCommand = `powershell -c "(New-Object Media.SoundPlayer '${filePath}').PlaySync()"`;
            await execAsync(simpleCommand);
        }
    }
    /**
     * Play audio using system commands (Linux/macOS)
     */
    async playWithSystemCommand(filePath) {
        let command;
        if (process.platform === 'darwin') {
            // macOS
            command = `afplay "${filePath}"`;
        }
        else {
            // Linux - try common audio players
            command = `aplay "${filePath}" || paplay "${filePath}" || mpg123 "${filePath}" || mplayer "${filePath}"`;
        }
        await execAsync(command);
    }
    async playTestSound() {
        try {
            const testSoundPath = this.defaultSounds.get(types_1.SoundEventType.SAVE);
            if (testSoundPath && fs.existsSync(testSoundPath)) {
                await this.playSoundFile(testSoundPath, this.configManager.getVolume());
            }
            else {
                console.warn('Test sound file not found:', testSoundPath);
                throw new Error('Test sound file not found');
            }
        }
        catch (error) {
            console.error('Error in playTestSound:', error);
            throw error;
        }
    }
    validateSoundFile(filePath) {
        if (!filePath || !fs.existsSync(filePath)) {
            return false;
        }
        const allowedExtensions = ['.wav', '.mp3', '.ogg', '.m4a'];
        const fileExtension = path.extname(filePath).toLowerCase();
        return allowedExtensions.includes(fileExtension);
    }
    getDefaultSoundPath(eventType) {
        return this.defaultSounds.get(eventType) || '';
    }
}
exports.SoundManager = SoundManager;
//# sourceMappingURL=soundManager.js.map