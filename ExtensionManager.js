"use strict";
/**
 * Main extension manager - orchestrates all services and components
 * @module core/ExtensionManager
 */
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
exports.ExtensionManager = void 0;
const vscode = __importStar(require("vscode"));
const ContextService_1 = require("../services/ContextService");
const ValidationService_1 = require("../services/ValidationService");
const FormattingService_1 = require("../services/FormattingService");
const Logger_1 = require("../utils/Logger");
const ExtensionError_1 = require("../errors/ExtensionError");
const constants_1 = require("../constants");
/**
 * Main extension manager class
 * Implements Singleton pattern for centralized management
 */
class ExtensionManager {
    static instance;
    log = Logger_1.logger.createChild('ExtensionManager');
    // Services
    contextService;
    validationService;
    formattingService;
    // State
    enhancementActive = true;
    statusBarItem;
    context;
    constructor() {
        this.contextService = ContextService_1.ContextService.getInstance();
        this.validationService = ValidationService_1.ValidationService.getInstance();
        this.formattingService = FormattingService_1.FormattingService.getInstance();
    }
    /**
     * Get singleton instance
     */
    static getInstance() {
        if (!ExtensionManager.instance) {
            ExtensionManager.instance = new ExtensionManager();
        }
        return ExtensionManager.instance;
    }
    /**
     * Initialize extension
     */
    async initialize(context) {
        this.log.info(`${constants_1.EXTENSION_NAME} is initializing...`);
        this.context = context;
        try {
            // Create status bar item
            this.createStatusBar(context);
            // Check for Augment extension
            await this.checkAugmentExtension();
            // Set up event listeners
            this.setupEventListeners(context);
            // Load persisted state
            this.loadPersistedState(context);
            this.log.info(`${constants_1.EXTENSION_NAME} initialized successfully`);
        }
        catch (error) {
            this.log.error('Initialization failed', error);
            ExtensionError_1.ErrorHandler.handle(error, 'Extension initialization');
        }
    }
    /**
     * Create status bar item
     */
    createStatusBar(context) {
        this.statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
        this.statusBarItem.text = constants_1.STATUS_BAR_MESSAGES.ACTIVE;
        this.statusBarItem.tooltip = 'Fix Augment is active. Click to toggle.';
        this.statusBarItem.command = constants_1.COMMANDS.TOGGLE_ENHANCEMENT;
        this.statusBarItem.show();
        context.subscriptions.push(this.statusBarItem);
    }
    /**
     * Check for Augment extension
     */
    async checkAugmentExtension() {
        const augmentExtension = vscode.extensions.getExtension(constants_1.AUGMENT_EXTENSION_ID);
        if (augmentExtension) {
            this.log.info('Augment extension found, setting up enhancements...');
            const augmentAPI = augmentExtension.exports;
            vscode.window.showInformationMessage(constants_1.NOTIFICATION_MESSAGES.ENHANCEMENT_ACTIVATED);
            return augmentAPI;
        }
        else {
            this.log.warn('Augment extension not found');
            vscode.window.showWarningMessage(constants_1.NOTIFICATION_MESSAGES.AUGMENT_NOT_FOUND);
            return undefined;
        }
    }
    /**
     * Set up event listeners
     */
    setupEventListeners(context) {
        // Listen for text document changes
        context.subscriptions.push(vscode.workspace.onDidChangeTextDocument(this.handleTextDocumentChange.bind(this)));
        // Listen for active editor changes
        context.subscriptions.push(vscode.window.onDidChangeActiveTextEditor(this.handleActiveEditorChange.bind(this)));
        // Listen for configuration changes
        context.subscriptions.push(vscode.workspace.onDidChangeConfiguration(this.handleConfigurationChange.bind(this)));
    }
    /**
     * Handle text document changes
     */
    async handleTextDocumentChange(event) {
        if (!this.enhancementActive || event.contentChanges.length === 0) {
            return;
        }
        // Debounce to avoid excessive processing
        await ExtensionError_1.ErrorHandler.wrapAsync(async () => {
            const text = event.contentChanges[0].text;
            // Check if this looks like Augment output
            if (this.isAugmentOutput(text)) {
                this.contextService.incrementExchangeCount();
                // Check context health
                if (this.contextService.shouldRefreshContext()) {
                    this.showContextRefreshSuggestion();
                }
            }
        }, 'Handle text document change');
    }
    /**
     * Check if text is Augment output
     */
    isAugmentOutput(text) {
        return (text.includes('```') ||
            text.includes('function_results') ||
            text.includes('<augment_code_snippet') ||
            text.includes('Agent:') ||
            text.includes('Next Edit:') ||
            text.includes('Instructions:') ||
            text.includes('Chat:'));
    }
    /**
     * Show context refresh suggestion
     */
    async showContextRefreshSuggestion() {
        const action = await vscode.window.showWarningMessage('Context is getting long. Consider refreshing for better results.', 'Refresh Now', 'Remind Later', 'Don\'t Show Again');
        if (action === 'Refresh Now') {
            this.contextService.resetExchangeCount();
            vscode.window.showInformationMessage(constants_1.NOTIFICATION_MESSAGES.CONTEXT_REFRESHED);
        }
    }
    /**
     * Handle active editor change
     */
    handleActiveEditorChange(editor) {
        if (editor) {
            this.log.debug('Active editor changed', {
                fileName: editor.document.fileName
            });
        }
    }
    /**
     * Handle configuration change
     */
    handleConfigurationChange(event) {
        if (event.affectsConfiguration('fixAugment')) {
            this.log.info('Configuration changed, reloading...');
            // Reload configuration-dependent components
        }
    }
    /**
     * Toggle enhancement on/off
     */
    toggleEnhancement() {
        this.enhancementActive = !this.enhancementActive;
        if (this.statusBarItem) {
            if (this.enhancementActive) {
                this.statusBarItem.text = constants_1.STATUS_BAR_MESSAGES.ACTIVE;
                this.statusBarItem.tooltip = 'Fix Augment is active. Click to toggle.';
                vscode.commands.executeCommand('setContext', 'fixAugment.enabled', true);
                vscode.window.showInformationMessage('Fix Augment is now active');
            }
            else {
                this.statusBarItem.text = constants_1.STATUS_BAR_MESSAGES.INACTIVE;
                this.statusBarItem.tooltip = 'Fix Augment is inactive. Click to toggle.';
                vscode.commands.executeCommand('setContext', 'fixAugment.enabled', false);
                vscode.window.showInformationMessage('Fix Augment is now inactive');
            }
        }
        this.log.info(`Enhancement ${this.enhancementActive ? 'activated' : 'deactivated'}`);
    }
    /**
     * Check if enhancement is active
     */
    isEnhancementActive() {
        return this.enhancementActive;
    }
    /**
     * Get services
     */
    getContextService() {
        return this.contextService;
    }
    getValidationService() {
        return this.validationService;
    }
    getFormattingService() {
        return this.formattingService;
    }
    /**
     * Load persisted state
     */
    loadPersistedState(context) {
        const sessionData = context.globalState.get('sessionData');
        if (sessionData) {
            this.contextService.importSessionData(sessionData);
            this.log.info('Persisted state loaded');
        }
    }
    /**
     * Save state for persistence
     */
    async saveState() {
        if (this.context) {
            const sessionData = this.contextService.exportSessionData();
            await this.context.globalState.update('sessionData', sessionData);
            this.log.info('State saved');
        }
    }
    /**
     * Dispose resources
     */
    dispose() {
        this.log.info('Disposing extension manager...');
        // Save state before disposing
        this.saveState();
        // Dispose status bar
        if (this.statusBarItem) {
            this.statusBarItem.dispose();
        }
        this.log.info('Extension manager disposed');
    }
}
exports.ExtensionManager = ExtensionManager;
//# sourceMappingURL=ExtensionManager.js.map