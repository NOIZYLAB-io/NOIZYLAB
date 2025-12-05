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
exports.ContextManager = exports.ContextType = exports.IDEType = void 0;
const vscode = __importStar(require("vscode"));
/**
 * IDE types supported by SpeechToTextWhisper
 */
var IDEType;
(function (IDEType) {
    IDEType["VSCODE"] = "vscode";
    IDEType["CURSOR"] = "cursor";
    IDEType["UNKNOWN"] = "unknown";
})(IDEType || (exports.IDEType = IDEType = {}));
/**
 * Types of active context in IDE
 */
var ContextType;
(function (ContextType) {
    ContextType["EDITOR"] = "editor";
    ContextType["TERMINAL"] = "terminal";
    ContextType["CHAT"] = "chat";
    ContextType["OUTPUT"] = "output";
    ContextType["DEBUGGER"] = "debugger";
    ContextType["SEARCH"] = "search";
    ContextType["EXPLORER"] = "explorer";
    ContextType["UNKNOWN"] = "unknown"; // Unknown context
})(ContextType || (exports.ContextType = ContextType = {}));
/**
 * IDE context manager for adapting SpeechToTextWhisper behavior
 */
class ContextManager {
    ideType = IDEType.UNKNOWN;
    currentContext;
    events;
    disposables = [];
    lastEditorActiveTime = 0;
    // Language settings cache
    languageCache = new Map();
    constructor(events = {}) {
        this.events = events;
        // Initialize the base context
        this.currentContext = {
            ideType: IDEType.UNKNOWN,
            contextType: ContextType.UNKNOWN
        };
        // Determine the IDE type during initialization
        this.detectIDEType();
        // Get the current context
        this.updateContext();
        // Subscribe to context change events
        this.setupEventListeners();
    }
    /**
     * Determine the IDE type
     */
    detectIDEType() {
        try {
            const appName = vscode.env.appName.toLowerCase();
            const uriScheme = vscode.env.uriScheme;
            // Determine the IDE type by application name
            if (appName.includes('cursor')) {
                this.ideType = IDEType.CURSOR;
            }
            else if (appName.includes('visual studio code') || appName.includes('vscode')) {
                this.ideType = IDEType.VSCODE;
            }
            else {
                // Additional check by URI scheme
                if (uriScheme === 'cursor') {
                    this.ideType = IDEType.CURSOR;
                }
                else if (uriScheme === 'vscode' || uriScheme === 'vscode-insiders') {
                    this.ideType = IDEType.VSCODE;
                }
                else {
                    this.ideType = IDEType.UNKNOWN;
                }
            }
            // Notify about the IDE type detection
            if (this.events.onIDETypeDetected) {
                this.events.onIDETypeDetected(this.ideType);
            }
        }
        catch (error) {
            console.error('❌ Failed to detect IDE type:', error);
            this.ideType = IDEType.UNKNOWN;
        }
    }
    /**
     * Setup event listeners
     */
    setupEventListeners() {
        // Listen to changes in the active editor
        this.disposables.push(vscode.window.onDidChangeActiveTextEditor((editor) => {
            if (editor) {
                this.lastEditorActiveTime = Date.now();
            }
            this.updateContext();
        }));
        // Listen to changes in the editor selection
        this.disposables.push(vscode.window.onDidChangeTextEditorSelection((event) => {
            this.updateContext();
        }));
        // Listen to changes in the active terminal
        this.disposables.push(vscode.window.onDidChangeActiveTerminal((terminal) => {
            this.updateContext();
        }));
        // Listen to changes in the debugger state
        this.disposables.push(vscode.debug.onDidStartDebugSession((session) => {
            this.updateContext();
        }));
        this.disposables.push(vscode.debug.onDidTerminateDebugSession((session) => {
            this.updateContext();
        }));
        // Listen to changes in the workspace
        this.disposables.push(vscode.workspace.onDidChangeWorkspaceFolders(() => {
            this.updateContext();
        }));
    }
    /**
     * Update the current context
     */
    updateContext() {
        const previousContext = { ...this.currentContext };
        try {
            // Determine the context type
            const contextType = this.detectContextType();
            // Collect information about the active editor
            const activeEditor = this.getActiveEditorInfo();
            // Information about the terminal
            const terminal = this.getTerminalInfo();
            // Information about the debugger
            const debuggerInfo = this.getDebuggerInfo();
            // Information about the workspace
            const workspace = this.getWorkspaceInfo();
            // Update the context
            this.currentContext = {
                ideType: this.ideType,
                contextType,
                activeEditor,
                terminal,
                debugger: debuggerInfo,
                workspace
            };
            // Check for changes and notify
            if (this.hasContextChanged(previousContext, this.currentContext)) {
                if (this.events.onContextChange) {
                    this.events.onContextChange(this.currentContext);
                }
                // If the language changed
                if (activeEditor &&
                    (!previousContext.activeEditor ||
                        previousContext.activeEditor.language.id !== activeEditor.language.id)) {
                    if (this.events.onLanguageChange) {
                        this.events.onLanguageChange(activeEditor.language);
                    }
                }
            }
        }
        catch (error) {
            console.error('❌ Failed to update context:', error);
        }
    }
    /**
     * Determine the context type
     */
    detectContextType() {
        // Check if the debugger is active
        if (vscode.debug.activeDebugSession) {
            return ContextType.DEBUGGER;
        }
        // Check if the active terminal is active
        if (vscode.window.activeTerminal) {
            return ContextType.TERMINAL;
        }
        // Check if the active editor is active
        if (vscode.window.activeTextEditor) {
            return ContextType.EDITOR;
        }
        // For Cursor - improved AI chat detection
        if (this.ideType === IDEType.CURSOR) {
            // Check if the IDE is focused
            if (vscode.window.state.focused) {
                // Check if there are open editors
                const hasOpenEditors = vscode.window.visibleTextEditors.length > 0;
                // MAIN LOGIC: If there are no open editors and no active terminal - likely chat
                if (!hasOpenEditors && !vscode.window.activeTerminal && !vscode.debug.activeDebugSession) {
                    return ContextType.CHAT;
                }
                // ADDITIONAL LOGIC: If there are editors, but none are active for more than 3 seconds
                const timeSinceLastEditor = Date.now() - (this.lastEditorActiveTime || 0);
                if (hasOpenEditors && timeSinceLastEditor > 3000) { // 3 seconds without active editor
                    return ContextType.CHAT;
                }
                // NEW LOGIC: If the IDE is focused, but there is no active UI element - chat
                if (!vscode.window.activeTextEditor && !vscode.window.activeTerminal && !vscode.debug.activeDebugSession) {
                    return ContextType.CHAT;
                }
            }
        }
        return ContextType.UNKNOWN;
    }
    /**
     * Get information about the active editor
     */
    getActiveEditorInfo() {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            return undefined;
        }
        const language = this.getLanguageInfo(editor.document.languageId);
        return {
            fileName: editor.document.fileName,
            language,
            selection: editor.selection,
            lineNumber: editor.selection.active.line + 1,
            columnNumber: editor.selection.active.character + 1
        };
    }
    /**
     * Get information about the programming language
     */
    getLanguageInfo(languageId) {
        // Check the cache
        if (this.languageCache.has(languageId)) {
            return this.languageCache.get(languageId);
        }
        // Determine the language information
        const languageInfo = this.createLanguageInfo(languageId);
        // Cache the result
        this.languageCache.set(languageId, languageInfo);
        return languageInfo;
    }
    /**
     * Create information about the programming language
     */
    createLanguageInfo(languageId) {
        const languageMap = {
            'javascript': { name: 'JavaScript', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'typescript': { name: 'TypeScript', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'html': { name: 'HTML', commentStyle: 'block', blockComment: { start: '<!--', end: '-->' } },
            'css': { name: 'CSS', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'scss': { name: 'SCSS', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'less': { name: 'Less', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            // System languages
            'c': { name: 'C', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'cpp': { name: 'C++', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'csharp': { name: 'C#', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'java': { name: 'Java', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'rust': { name: 'Rust', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'go': { name: 'Go', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            // Scripting languages
            'python': { name: 'Python', commentStyle: 'line', lineComment: '#' },
            'ruby': { name: 'Ruby', commentStyle: 'line', lineComment: '#' },
            'php': { name: 'PHP', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'perl': { name: 'Perl', commentStyle: 'line', lineComment: '#' },
            'bash': { name: 'Bash', commentStyle: 'line', lineComment: '#' },
            'powershell': { name: 'PowerShell', commentStyle: 'both', lineComment: '#', blockComment: { start: '<#', end: '#>' } },
            // Functional languages
            'haskell': { name: 'Haskell', commentStyle: 'both', lineComment: '--', blockComment: { start: '{-', end: '-}' } },
            'scala': { name: 'Scala', commentStyle: 'both', lineComment: '//', blockComment: { start: '/*', end: '*/' } },
            'clojure': { name: 'Clojure', commentStyle: 'line', lineComment: ';' },
            // Configuration files
            'json': { name: 'JSON', commentStyle: 'line', lineComment: '//' },
            'yaml': { name: 'YAML', commentStyle: 'line', lineComment: '#' },
            'toml': { name: 'TOML', commentStyle: 'line', lineComment: '#' },
            'xml': { name: 'XML', commentStyle: 'block', blockComment: { start: '<!--', end: '-->' } },
            // Markup and documentation
            'markdown': { name: 'Markdown', commentStyle: 'block', blockComment: { start: '<!--', end: '-->' } },
            'latex': { name: 'LaTeX', commentStyle: 'line', lineComment: '%' },
            // Databases
            'sql': { name: 'SQL', commentStyle: 'both', lineComment: '--', blockComment: { start: '/*', end: '*/' } },
            // Other
            'plaintext': { name: 'Plain Text', commentStyle: 'line', lineComment: '#' }
        };
        const langConfig = languageMap[languageId] || {};
        return {
            id: languageId,
            name: langConfig.name || languageId.toUpperCase(),
            commentStyle: langConfig.commentStyle || 'line',
            lineComment: langConfig.lineComment,
            blockComment: langConfig.blockComment,
            ...langConfig
        };
    }
    /**
     * Get information about the terminal
     */
    getTerminalInfo() {
        const activeTerminal = vscode.window.activeTerminal;
        if (!activeTerminal) {
            return undefined;
        }
        return {
            isActive: true,
            name: activeTerminal.name
        };
    }
    /**
     * Get information about the debugger
     */
    getDebuggerInfo() {
        const activeSession = vscode.debug.activeDebugSession;
        return {
            isActive: !!activeSession,
            sessionName: activeSession?.name
        };
    }
    /**
     * Get information about the workspace
     */
    getWorkspaceInfo() {
        const workspaceFolders = vscode.workspace.workspaceFolders;
        const workspaceName = vscode.workspace.name;
        return {
            name: workspaceName || 'Untitled',
            folders: workspaceFolders?.map(folder => folder.uri.fsPath) || []
        };
    }
    /**
     * Check for context changes
     */
    hasContextChanged(previous, current) {
        return (previous.contextType !== current.contextType ||
            previous.activeEditor?.fileName !== current.activeEditor?.fileName ||
            previous.activeEditor?.language.id !== current.activeEditor?.language.id ||
            previous.terminal?.isActive !== current.terminal?.isActive ||
            previous.debugger?.isActive !== current.debugger?.isActive);
    }
    /**
     * Public methods for getting information about the context
     */
    /**
     * Get the current context
     */
    getContext() {
        return { ...this.currentContext };
    }
    /**
     * Get the IDE type
     */
    getIDEType() {
        return this.ideType;
    }
    /**
     * Get the type of the current context
     */
    getContextType() {
        return this.currentContext.contextType;
    }
    /**
     * Check if the IDE is of type Cursor
     */
    isCursor() {
        return this.ideType === IDEType.CURSOR;
    }
    /**
     * Check if the IDE is of type VS Code
     */
    isVSCode() {
        return this.ideType === IDEType.VSCODE;
    }
    /**
     * Check if the editor is active
     */
    isEditorActive() {
        return this.currentContext.contextType === ContextType.EDITOR;
    }
    /**
     * Check if the terminal is active
     */
    isTerminalActive() {
        return this.currentContext.contextType === ContextType.TERMINAL;
    }
    /**
     * Check if the chat is active (for Cursor)
     */
    isChatActive() {
        return this.currentContext.contextType === ContextType.CHAT;
    }
    /**
     * Get information about the language of the current file
     */
    getCurrentLanguage() {
        return this.currentContext.activeEditor?.language || null;
    }
    /**
     * Check if the support of a certain type of comments
     */
    supportsComments(type) {
        const language = this.getCurrentLanguage();
        if (!language) {
            return false;
        }
        return language.commentStyle === 'both' || language.commentStyle === type;
    }
    /**
     * Get the appropriate comment style for the current language
     */
    getPreferredCommentStyle() {
        const language = this.getCurrentLanguage();
        if (!language) {
            return null;
        }
        if (language.commentStyle === 'both') {
            return 'line'; // We prefer line comments
        }
        return language.commentStyle === 'line' || language.commentStyle === 'block'
            ? language.commentStyle
            : null;
    }
    /**
     * Force update the context
     */
    refreshContext() {
        this.updateContext();
    }
    /**
     * Release resources
     */
    dispose() {
        this.disposables.forEach(disposable => {
            try {
                disposable.dispose();
            }
            catch (error) {
                console.error('❌ Error disposing context manager resource:', error);
            }
        });
        this.disposables = [];
        this.languageCache.clear();
    }
}
exports.ContextManager = ContextManager;
//# sourceMappingURL=ContextManager.js.map