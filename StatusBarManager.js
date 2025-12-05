"use strict";
// StatusBarManager.ts - managing the interface elements in the VS Code status bar
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
exports.StatusBarManager = void 0;
const vscode = __importStar(require("vscode"));
/**
 * Managing the interface elements in the VS Code status bar
 * Provides visual feedback on the recording and speech processing state
 */
class StatusBarManager {
    events;
    statusBarItem;
    currentState = 'idle';
    isRecording = false;
    lastError = null;
    successTimer = null;
    errorTimer = null;
    progressInterval = null;
    progressStep = 0;
    config;
    // Configuration for different states
    stateConfig = {
        idle: {
            text: '$(mic)',
            tooltip: 'Click to start voice recording',
            icon: 'mic',
            command: 'speechToTextWhisper.recordAndInsertOrClipboard'
        },
        recording: {
            text: '$(sync~spin)',
            tooltip: 'Recording... Click to stop',
            icon: 'sync',
            backgroundColor: new vscode.ThemeColor('statusBarItem.warningBackground'),
            color: new vscode.ThemeColor('statusBarItem.warningForeground'),
            command: 'speechToTextWhisper.recordAndInsertOrClipboard'
        },
        processing: {
            text: '$(loading~spin)',
            tooltip: 'Processing audio data...',
            icon: 'loading',
            backgroundColor: new vscode.ThemeColor('statusBarItem.prominentBackground')
        },
        transcribing: {
            text: '$(sync~spin)',
            tooltip: 'Transcribing speech to text...',
            icon: 'sync',
            backgroundColor: new vscode.ThemeColor('statusBarItem.warningBackground'),
            color: new vscode.ThemeColor('statusBarItem.warningForeground')
        },
        'post-processing': {
            text: '$(sparkle~spin)',
            tooltip: 'Improving text quality with AI...',
            icon: 'sparkle',
            backgroundColor: new vscode.ThemeColor('statusBarItem.prominentBackground'),
            color: new vscode.ThemeColor('statusBarItem.prominentForeground')
        },
        inserting: {
            text: '$(edit)',
            tooltip: 'Inserting transcribed text...',
            icon: 'edit',
            backgroundColor: new vscode.ThemeColor('statusBarItem.prominentBackground')
        },
        success: {
            text: '$(check)',
            tooltip: 'Text successfully inserted!',
            icon: 'check',
            backgroundColor: new vscode.ThemeColor('statusBarItem.prominentBackground'),
            color: new vscode.ThemeColor('statusBarItem.prominentForeground')
        },
        error: {
            text: '$(error)',
            tooltip: 'Voice recording error occurred',
            icon: 'error',
            backgroundColor: new vscode.ThemeColor('statusBarItem.errorBackground'),
            color: new vscode.ThemeColor('statusBarItem.errorForeground')
        },
        warning: {
            text: '$(warning)',
            tooltip: 'Voice recording warning',
            icon: 'warning',
            backgroundColor: new vscode.ThemeColor('statusBarItem.warningBackground'),
            color: new vscode.ThemeColor('statusBarItem.warningForeground')
        }
    };
    constructor(events, config = {}) {
        this.events = events;
        this.config = {
            position: config.position || 'right',
            priority: config.priority || 100,
            showTooltips: config.showTooltips !== false,
            autoHideOnSuccess: config.autoHideOnSuccess !== false,
            successDisplayDuration: config.successDisplayDuration || 2000,
            errorDisplayDuration: config.errorDisplayDuration || 3000,
            enableAnimations: config.enableAnimations !== false,
            showProgress: config.showProgress !== false
        };
        this.createStatusBarItem();
        this.updateUI();
        this.show();
    }
    /**
     * Creates a status bar item
     */
    createStatusBarItem() {
        const alignment = this.config.position === 'left'
            ? vscode.StatusBarAlignment.Left
            : vscode.StatusBarAlignment.Right;
        this.statusBarItem = vscode.window.createStatusBarItem(alignment, this.config.priority);
    }
    /**
     * Updates the recording state
     */
    updateRecordingState(isRecording) {
        this.isRecording = isRecording;
        if (isRecording) {
            this.setState('recording');
            this.startProgressAnimation(); // Start the animation for recording
        }
        else {
            this.clearProgressAnimation(); // Stop the animation when recording is stopped
            this.setState('idle');
        }
    }
    /**
     * Shows the processing state of audio
     */
    showProcessing() {
        this.setState('processing');
        this.startProgressAnimation();
    }
    /**
     * Shows the transcription state
     */
    showTranscribing() {
        this.setState('transcribing');
        this.startProgressAnimation();
    }
    /**
     * Shows the post-processing state
     */
    showPostProcessing() {
        this.setState('post-processing');
        this.startProgressAnimation();
    }
    /**
     * Shows the inserting state of text
     */
    showInserting() {
        this.setState('inserting');
    }
    /**
     * Shows the success state
     */
    showSuccess(message) {
        this.clearTimers();
        this.setState('success');
        if (message) {
            this.updateTooltip(`Success: ${message}`);
        }
        if (this.config.autoHideOnSuccess) {
            this.successTimer = setTimeout(() => {
                this.setState('idle');
            }, this.config.successDisplayDuration);
        }
    }
    /**
     * Shows the error state
     */
    showError(message, severity = 'error') {
        this.clearTimers();
        this.lastError = message;
        const state = severity === 'warning' ? 'warning' : 'error';
        this.setState(state);
        this.updateTooltip(`${this.capitalizeFirst(severity)}: ${message}`);
        this.errorTimer = setTimeout(() => {
            this.setState('idle');
            this.lastError = null;
        }, this.config.errorDisplayDuration);
    }
    /**
     * Shows the warning state
     */
    showWarning(message) {
        this.showError(message, 'warning');
    }
    /**
     * Updates the progress of the operation
     */
    updateProgress(percentage, message) {
        if (!this.config.showProgress) {
            return;
        }
        const progressBar = this.createProgressBar(percentage);
        const currentConfig = this.stateConfig[this.currentState];
        this.statusBarItem.text = `${currentConfig.icon} ${progressBar}`;
        if (message && this.config.showTooltips) {
            this.updateTooltip(`${currentConfig.tooltip} (${Math.round(percentage)}%) - ${message}`);
        }
    }
    /**
     * Gets the information about the current state
     */
    getStatus() {
        return {
            state: this.currentState,
            isRecording: this.isRecording,
            isVisible: this.statusBarItem ? true : false,
            lastError: this.lastError,
            configuration: this.config
        };
    }
    /**
     * Updates the configuration
     */
    updateConfiguration(newConfig) {
        Object.assign(this.config, newConfig);
        // Recreate the element if the position has changed
        if (newConfig.position || newConfig.priority !== undefined) {
            const wasVisible = this.statusBarItem ? true : false;
            this.dispose();
            this.createStatusBarItem();
            if (wasVisible) {
                this.show();
            }
        }
        this.updateUI();
    }
    /**
     * Shows the status bar item
     */
    show() {
        if (this.statusBarItem) {
            this.statusBarItem.show();
        }
    }
    /**
     * Hides the status bar item
     */
    hide() {
        if (this.statusBarItem) {
            this.statusBarItem.hide();
        }
    }
    /**
     * Toggles the visibility of the item
     */
    toggle() {
        // VS Code API does not provide a direct way to check visibility
        // So we track the state ourselves
        if (this.statusBarItem) {
            // Simple implementation: always show
            this.show();
        }
    }
    /**
     * Sets a new state
     */
    setState(newState) {
        if (this.currentState === newState) {
            return;
        }
        this.currentState = newState;
        this.updateUI();
    }
    /**
     * Updates the UI of the item
     */
    updateUI() {
        if (!this.statusBarItem) {
            return;
        }
        const config = this.stateConfig[this.currentState];
        // Update the text with animation if enabled
        if (this.config.enableAnimations && this.isAnimatedState()) {
            this.statusBarItem.text = this.getAnimatedText(config);
        }
        else {
            this.statusBarItem.text = config.text;
        }
        // Update the tooltip if enabled
        if (this.config.showTooltips) {
            this.statusBarItem.tooltip = this.buildTooltip(config);
        }
        // Update the colors
        this.statusBarItem.backgroundColor = config.backgroundColor;
        this.statusBarItem.color = config.color;
        // Update the command
        this.statusBarItem.command = config.command;
    }
    /**
     * Updates the tooltip
     */
    updateTooltip(tooltip) {
        if (this.config.showTooltips && this.statusBarItem) {
            this.statusBarItem.tooltip = tooltip;
        }
    }
    /**
     * Creates a progress bar
     */
    createProgressBar(percentage) {
        const totalBlocks = 10;
        const filledBlocks = Math.round((percentage / 100) * totalBlocks);
        const emptyBlocks = totalBlocks - filledBlocks;
        return '█'.repeat(filledBlocks) + '░'.repeat(emptyBlocks);
    }
    /**
     * Checks if the state is animated
     */
    isAnimatedState() {
        return ['recording', 'processing', 'transcribing'].includes(this.currentState);
    }
    /**
     * Gets the animated text
     */
    getAnimatedText(config) {
        if (this.currentState === 'recording') {
            return `$(sync~spin) Recording`;
        }
        if (this.currentState === 'transcribing') {
            return `$(sync~spin) Transcribing`;
        }
        return config.text;
    }
    /**
     * Builds the full tooltip
     */
    buildTooltip(config) {
        let tooltip = config.tooltip;
        // Add additional information for different states
        switch (this.currentState) {
            case 'idle':
                tooltip += '\n\nHotkey: Ctrl+Shift+N (hold to record)';
                tooltip += '\nRight-click for settings';
                break;
            case 'recording':
                tooltip += '\n\nHotkey: Ctrl+Shift+N (release to stop)';
                break;
            case 'error':
                if (this.lastError) {
                    tooltip += `\n\nLast error: ${this.lastError}`;
                }
                tooltip += '\n\nClick to retry';
                break;
        }
        return tooltip;
    }
    /**
     * Starts the progress animation
     */
    startProgressAnimation() {
        if (!this.config.enableAnimations) {
            return;
        }
        this.clearProgressAnimation();
        this.progressStep = 0;
        this.progressInterval = setInterval(() => {
            this.progressStep++;
            this.updateUI();
        }, 500);
    }
    /**
     * Stops the progress animation
     */
    clearProgressAnimation() {
        if (this.progressInterval) {
            clearInterval(this.progressInterval);
            this.progressInterval = null;
        }
    }
    /**
     * Clears all timers
     */
    clearTimers() {
        if (this.successTimer) {
            clearTimeout(this.successTimer);
            this.successTimer = null;
        }
        if (this.errorTimer) {
            clearTimeout(this.errorTimer);
            this.errorTimer = null;
        }
        this.clearProgressAnimation();
    }
    /**
     * Makes the first letter uppercase
     */
    capitalizeFirst(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
    /**
     * Releases resources
     */
    dispose() {
        this.clearTimers();
        if (this.statusBarItem) {
            this.statusBarItem.dispose();
        }
    }
    /**
     * Static methods for creating standard configurations
     */
    /**
     * Creates a minimal configuration
     */
    static createMinimalConfig() {
        return {
            showTooltips: false,
            enableAnimations: false,
            showProgress: false
        };
    }
    /**
     * Creates a full configuration
     */
    static createFullConfig() {
        return {
            position: 'right',
            priority: 100,
            showTooltips: true,
            autoHideOnSuccess: true,
            successDisplayDuration: 2000,
            errorDisplayDuration: 5000,
            enableAnimations: true,
            showProgress: true
        };
    }
    /**
     * Creates a configuration for development
     */
    static createDebugConfig() {
        return {
            position: 'left',
            priority: 1000,
            showTooltips: true,
            autoHideOnSuccess: false,
            successDisplayDuration: 5000,
            errorDisplayDuration: 10000,
            enableAnimations: true,
            showProgress: true
        };
    }
}
exports.StatusBarManager = StatusBarManager;
//# sourceMappingURL=StatusBarManager.js.map