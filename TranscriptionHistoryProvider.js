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
exports.TranscriptionHistoryProvider = exports.TranscriptionHistoryItem = void 0;
const vscode = __importStar(require("vscode"));
const TranscriptionHistory_1 = require("../types/TranscriptionHistory");
const CursorIntegration_1 = require("../integrations/CursorIntegration");
/**
 * Tree item for transcription history
 */
class TranscriptionHistoryItem extends vscode.TreeItem {
    label;
    collapsibleState;
    entry;
    isGroupHeader;
    constructor(label, collapsibleState, entry, isGroupHeader = false) {
        super(label, collapsibleState);
        this.label = label;
        this.collapsibleState = collapsibleState;
        this.entry = entry;
        this.isGroupHeader = isGroupHeader;
        if (entry) {
            // This is a transcription entry
            this.description = this.formatEntryDescription(entry);
            this.tooltip = this.formatEntryTooltip(entry);
            this.contextValue = 'transcriptionEntry';
            this.iconPath = new vscode.ThemeIcon('file-text');
        }
        else {
            // This is a group header
            this.iconPath = new vscode.ThemeIcon('folder');
            this.contextValue = 'transcriptionGroup';
        }
    }
    formatEntryDescription(entry) {
        const timestamp = new Date(entry.timestamp).toLocaleTimeString('ru-RU', {
            hour: '2-digit',
            minute: '2-digit'
        });
        const duration = entry.duration ? `${entry.duration.toFixed(1)}s` : '';
        const postProcessedIcon = entry.isPostProcessed ? ' ✨' : '';
        return `${timestamp} ${duration}${postProcessedIcon}`.trim();
    }
    formatEntryTooltip(entry) {
        const date = new Date(entry.timestamp).toLocaleString('ru-RU');
        const mode = entry.mode === 'insertOrClipboard' ? 'Insert/Clipboard' : 'New Chat';
        const duration = entry.duration ? `Duration: ${entry.duration.toFixed(1)}s` : '';
        const language = entry.language ? `Language: ${entry.language}` : '';
        const tooltipParts = [
            `Text: ${entry.text}`,
            `Date: ${date}`,
            `Mode: ${mode}`,
            duration,
            language
        ];
        // Add post-processing information if available
        if (entry.isPostProcessed) {
            tooltipParts.push('');
            tooltipParts.push('✨ AI Post-processed');
            if (entry.postProcessingModel) {
                tooltipParts.push(`Model: ${entry.postProcessingModel}`);
            }
            if (entry.originalText && entry.originalText !== entry.text) {
                tooltipParts.push('');
                tooltipParts.push('Original (Whisper):');
                tooltipParts.push(entry.originalText);
                tooltipParts.push('');
                tooltipParts.push('Improved (AI):');
                tooltipParts.push(entry.text);
            }
        }
        return tooltipParts.filter(Boolean).join('\n');
    }
}
exports.TranscriptionHistoryItem = TranscriptionHistoryItem;
/**
 * Data provider for transcription history
 */
class TranscriptionHistoryProvider {
    historyManager;
    _onDidChangeTreeData = new vscode.EventEmitter();
    onDidChangeTreeData = this._onDidChangeTreeData.event;
    cursorIntegration;
    constructor(historyManager) {
        this.historyManager = historyManager;
        // Initialize CursorIntegration for chat work
        this.cursorIntegration = new CursorIntegration_1.CursorIntegration({
            primaryStrategy: CursorIntegration_1.CursorIntegrationStrategy.AICHAT_COMMAND,
            fallbackStrategies: [
                CursorIntegration_1.CursorIntegrationStrategy.CLIPBOARD,
                CursorIntegration_1.CursorIntegrationStrategy.COMMAND_PALETTE
            ],
            autoFocusChat: true,
            prefixText: '',
            suffixText: '',
            useMarkdownFormat: false,
            timeout: 5000
        });
    }
    refresh() {
        this._onDidChangeTreeData.fire();
    }
    getTreeItem(element) {
        return element;
    }
    async getChildren(element) {
        if (!element) {
            // Root elements - date groups
            return this.getDateGroups();
        }
        else if (element.isGroupHeader) {
            // Elements inside date group
            return this.getEntriesForGroup(element.label);
        }
        return [];
    }
    async getDateGroups() {
        try {
            const history = await this.historyManager.getHistory();
            if (!history) {
                return [this.createErrorItem('Failed to load transcription history')];
            }
            const entries = history.entries;
            if (entries.length === 0) {
                return [this.createEmptyItem()];
            }
            // Group entries by date categories
            const groups = this.groupEntriesByDate(entries);
            const items = [];
            for (const [category, groupEntries] of groups.entries()) {
                if (groupEntries.length > 0) {
                    const groupName = this.getGroupDisplayName(category);
                    const item = new TranscriptionHistoryItem(`${groupName} (${groupEntries.length})`, vscode.TreeItemCollapsibleState.Expanded, undefined, true);
                    items.push(item);
                }
            }
            return items;
        }
        catch (error) {
            return [this.createErrorItem(`Error loading history: ${error.message}`)];
        }
    }
    async getEntriesForGroup(groupLabel) {
        try {
            const history = await this.historyManager.getHistory();
            if (!history) {
                return [];
            }
            const entries = history.entries;
            const groups = this.groupEntriesByDate(entries);
            // Extract category from group label
            const category = this.getCategoryFromGroupLabel(groupLabel);
            const groupEntries = groups.get(category) || [];
            return groupEntries.map(entry => {
                const displayText = entry.text.length > 50 ?
                    `${entry.text.substring(0, 50)}...` :
                    entry.text;
                return new TranscriptionHistoryItem(displayText, vscode.TreeItemCollapsibleState.None, entry, false);
            });
        }
        catch (error) {
            return [this.createErrorItem(`Error loading entries: ${error.message}`)];
        }
    }
    groupEntriesByDate(entries) {
        const groups = new Map();
        const now = new Date();
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
        const yesterday = new Date(today.getTime() - 24 * 60 * 60 * 1000);
        const thisWeekStart = new Date(today.getTime() - (today.getDay() * 24 * 60 * 60 * 1000));
        // Initialize all groups
        Object.values(TranscriptionHistory_1.DateGroupCategory).forEach(category => {
            groups.set(category, []);
        });
        entries.forEach(entry => {
            const entryDate = new Date(entry.timestamp);
            const entryDay = new Date(entryDate.getFullYear(), entryDate.getMonth(), entryDate.getDate());
            let category;
            if (entryDay.getTime() === today.getTime()) {
                category = TranscriptionHistory_1.DateGroupCategory.TODAY;
            }
            else if (entryDay.getTime() === yesterday.getTime()) {
                category = TranscriptionHistory_1.DateGroupCategory.YESTERDAY;
            }
            else if (entryDay >= thisWeekStart) {
                category = TranscriptionHistory_1.DateGroupCategory.THIS_WEEK;
            }
            else {
                category = TranscriptionHistory_1.DateGroupCategory.OLDER;
            }
            groups.get(category)?.push(entry);
        });
        return groups;
    }
    getGroupDisplayName(category) {
        switch (category) {
            case TranscriptionHistory_1.DateGroupCategory.TODAY:
                return 'Today';
            case TranscriptionHistory_1.DateGroupCategory.YESTERDAY:
                return 'Yesterday';
            case TranscriptionHistory_1.DateGroupCategory.THIS_WEEK:
                return 'This Week';
            case TranscriptionHistory_1.DateGroupCategory.OLDER:
                return 'Older';
            default:
                return 'Unknown';
        }
    }
    getCategoryFromGroupLabel(groupLabel) {
        if (groupLabel.startsWith('Today')) {
            return TranscriptionHistory_1.DateGroupCategory.TODAY;
        }
        else if (groupLabel.startsWith('Yesterday')) {
            return TranscriptionHistory_1.DateGroupCategory.YESTERDAY;
        }
        else if (groupLabel.startsWith('This Week')) {
            return TranscriptionHistory_1.DateGroupCategory.THIS_WEEK;
        }
        else if (groupLabel.startsWith('Older')) {
            return TranscriptionHistory_1.DateGroupCategory.OLDER;
        }
        return TranscriptionHistory_1.DateGroupCategory.OLDER;
    }
    createErrorItem(message) {
        const item = new TranscriptionHistoryItem(`❌ ${message}`, vscode.TreeItemCollapsibleState.None, undefined, false);
        item.iconPath = new vscode.ThemeIcon('error');
        return item;
    }
    createEmptyItem() {
        const item = new TranscriptionHistoryItem('No transcriptions yet', vscode.TreeItemCollapsibleState.None, undefined, false);
        item.iconPath = new vscode.ThemeIcon('info');
        item.description = 'Start recording to see history';
        return item;
    }
    // Methods for commands
    /**
     * Copies the transcription text to the clipboard
     */
    async copyToClipboard(item) {
        if (!item.entry) {
            vscode.window.showErrorMessage('No transcription text to copy');
            return;
        }
        try {
            await vscode.env.clipboard.writeText(item.entry.text);
            vscode.window.showInformationMessage('✅ Transcription copied to clipboard');
        }
        catch (error) {
            vscode.window.showErrorMessage(`Failed to copy: ${error.message}`);
        }
    }
    /**
     * Inserts the transcription text into Cursor chat
     */
    async insertAtCursor(item) {
        if (!item.entry) {
            vscode.window.showErrorMessage('No transcription text to insert');
            return;
        }
        try {
            // Check the availability of the Cursor integration
            if (!this.cursorIntegration.isIntegrationEnabled()) {
                // If the integration is not available, use fallback
                await this.fallbackToEditor(item.entry.text);
                return;
            }
            // Show the progress indicator during insertion
            await vscode.window.withProgress({
                location: vscode.ProgressLocation.Notification,
                title: "Inserting to Cursor chat...",
                cancellable: false
            }, async (progress) => {
                progress.report({ increment: 30, message: "Preparing chat..." });
                // Use the verified CursorIntegration
                const result = await this.cursorIntegration.sendToChat(item.entry.text);
                progress.report({ increment: 70, message: "Text sent!" });
                if (result.success) {
                    const strategyMessage = result.strategy === CursorIntegration_1.CursorIntegrationStrategy.AICHAT_COMMAND ?
                        'direct chat' : `${result.strategy} strategy`;
                    vscode.window.showInformationMessage(`✅ Transcription sent to Cursor chat via ${strategyMessage}`);
                }
                else {
                    throw new Error(result.error || 'Unknown error occurred');
                }
            });
        }
        catch (error) {
            // If the insertion into the chat fails, try to insert into the active editor as fallback
            console.warn('Failed to insert to Cursor chat, trying fallback:', error);
            try {
                await this.fallbackToEditor(item.entry.text);
            }
            catch (fallbackError) {
                vscode.window.showErrorMessage(`Failed to insert text: ${error.message}`);
            }
        }
    }
    /**
     * Fallback method for inserting into the active editor
     */
    async fallbackToEditor(text) {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('Failed to insert to Cursor chat and no active editor available');
            return;
        }
        const position = editor.selection.active;
        await editor.edit(editBuilder => {
            editBuilder.insert(position, text);
        });
        vscode.window.showInformationMessage('✅ Transcription inserted at cursor (fallback mode)');
    }
    /**
     * Shows the diff between original and post-processed text
     */
    async showDiff(item) {
        if (!item.entry) {
            vscode.window.showErrorMessage('No transcription entry to show diff for');
            return;
        }
        const entry = item.entry;
        if (!entry.isPostProcessed || !entry.originalText) {
            vscode.window.showInformationMessage('This transcription was not post-processed or original text is not available');
            return;
        }
        try {
            // Create temporary documents for diff view
            const originalUri = vscode.Uri.parse(`untitled:Original (Whisper)`);
            const processedUri = vscode.Uri.parse(`untitled:Improved (${entry.postProcessingModel || 'AI'})`);
            // Open both documents
            const originalDocument = await vscode.workspace.openTextDocument(originalUri);
            const processedDocument = await vscode.workspace.openTextDocument(processedUri);
            // Edit the documents with content
            const originalEditor = await vscode.window.showTextDocument(originalDocument, { preview: false });
            await originalEditor.edit(editBuilder => {
                editBuilder.insert(new vscode.Position(0, 0), entry.originalText);
            });
            const processedEditor = await vscode.window.showTextDocument(processedDocument, { preview: false });
            await processedEditor.edit(editBuilder => {
                editBuilder.insert(new vscode.Position(0, 0), entry.text);
            });
            // Close the editors and show diff
            await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
            await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
            // Show diff view
            await vscode.commands.executeCommand('vscode.diff', originalUri, processedUri, `Transcription Comparison`);
        }
        catch (error) {
            vscode.window.showErrorMessage(`Failed to show diff: ${error.message}`);
        }
    }
    /**
     * Deletes the entry from the history
     */
    async deleteEntry(item) {
        if (!item.entry) {
            vscode.window.showErrorMessage('No transcription entry to delete');
            return;
        }
        try {
            const confirmResult = await vscode.window.showWarningMessage('Are you sure you want to delete this transcription?', { modal: true }, 'Delete');
            if (confirmResult === 'Delete') {
                const result = await this.historyManager.removeEntry(item.entry.id);
                if (result.success) {
                    this.refresh();
                    vscode.window.showInformationMessage('✅ Transcription deleted');
                }
                else {
                    vscode.window.showErrorMessage(`Failed to delete: ${result.error}`);
                }
            }
        }
        catch (error) {
            vscode.window.showErrorMessage(`Failed to delete: ${error.message}`);
        }
    }
    /**
     * Clears the entire transcription history
     */
    async clearHistory() {
        try {
            const confirmResult = await vscode.window.showWarningMessage('Are you sure you want to clear all transcription history? This action cannot be undone.', { modal: true }, 'Clear All');
            if (confirmResult === 'Clear All') {
                const result = await this.historyManager.clearHistory();
                if (result.success) {
                    this.refresh();
                    vscode.window.showInformationMessage('✅ Transcription history cleared');
                }
                else {
                    vscode.window.showErrorMessage(`Failed to clear history: ${result.error}`);
                }
            }
        }
        catch (error) {
            vscode.window.showErrorMessage(`Failed to clear history: ${error.message}`);
        }
    }
    /**
     * Cleaning up resources
     */
    dispose() {
        if (this.cursorIntegration) {
            this.cursorIntegration.dispose();
        }
    }
}
exports.TranscriptionHistoryProvider = TranscriptionHistoryProvider;
//# sourceMappingURL=TranscriptionHistoryProvider.js.map