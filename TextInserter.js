"use strict";
// TextInserter.ts - component for inserting transcribed text into the editor
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
exports.TextInserter = void 0;
const vscode = __importStar(require("vscode"));
const GlobalOutput_1 = require("../utils/GlobalOutput");
/**
 * Component for inserting transcribed text into the VS Code editor
 */
class TextInserter {
    // Extended language map
    languageMap = {
        // Web Technologies
        'javascript': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.js', '.mjs', '.jsx'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'typescript': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.ts', '.tsx'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'html': {
            singleLineComment: '<!--',
            multiLineCommentStart: '<!--',
            multiLineCommentEnd: '-->',
            fileExtensions: ['.html', '.htm'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'css': {
            singleLineComment: '/*',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.css'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'scss': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.scss'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'sass': {
            singleLineComment: '//',
            fileExtensions: ['.sass'],
            indentationChar: ' ',
            hasBlockComments: false
        },
        'less': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.less'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        // System Languages
        'c': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.c', '.h'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'cpp': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.cpp', '.cxx', '.cc', '.hpp'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'csharp': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.cs'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'rust': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.rs'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'go': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.go'],
            indentationChar: '\t',
            hasBlockComments: true
        },
        // JVM Languages
        'java': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.java'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'kotlin': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.kt', '.kts'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'scala': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.scala', '.sc'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        // Scripting Languages
        'python': {
            singleLineComment: '#',
            multiLineCommentStart: '"""',
            multiLineCommentEnd: '"""',
            fileExtensions: ['.py', '.pyw'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'ruby': {
            singleLineComment: '#',
            multiLineCommentStart: '=begin',
            multiLineCommentEnd: '=end',
            fileExtensions: ['.rb', '.erb'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'php': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.php', '.phtml'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'perl': {
            singleLineComment: '#',
            multiLineCommentStart: '=pod',
            multiLineCommentEnd: '=cut',
            fileExtensions: ['.pl', '.pm'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        // Shell Scripts
        'bash': {
            singleLineComment: '#',
            fileExtensions: ['.sh', '.bash'],
            indentationChar: ' ',
            hasBlockComments: false
        },
        'zsh': {
            singleLineComment: '#',
            fileExtensions: ['.zsh'],
            indentationChar: ' ',
            hasBlockComments: false
        },
        'fish': {
            singleLineComment: '#',
            fileExtensions: ['.fish'],
            indentationChar: ' ',
            hasBlockComments: false
        },
        'powershell': {
            singleLineComment: '#',
            multiLineCommentStart: '<#',
            multiLineCommentEnd: '#>',
            fileExtensions: ['.ps1', '.psm1'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        // Mobile
        'swift': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.swift'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'dart': {
            singleLineComment: '//',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.dart'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        // Data & Config
        'sql': {
            singleLineComment: '--',
            multiLineCommentStart: '/*',
            multiLineCommentEnd: '*/',
            fileExtensions: ['.sql'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'yaml': {
            singleLineComment: '#',
            fileExtensions: ['.yml', '.yaml'],
            indentationChar: ' ',
            hasBlockComments: false
        },
        'toml': {
            singleLineComment: '#',
            fileExtensions: ['.toml'],
            indentationChar: ' ',
            hasBlockComments: false
        },
        'ini': {
            singleLineComment: ';',
            fileExtensions: ['.ini', '.cfg'],
            indentationChar: ' ',
            hasBlockComments: false
        },
        // Other Languages
        'lua': {
            singleLineComment: '--',
            multiLineCommentStart: '--[[',
            multiLineCommentEnd: ']]',
            fileExtensions: ['.lua'],
            indentationChar: ' ',
            hasBlockComments: true
        },
        'r': {
            singleLineComment: '#',
            fileExtensions: ['.r', '.R'],
            indentationChar: ' ',
            hasBlockComments: false
        },
        'matlab': {
            singleLineComment: '%',
            multiLineCommentStart: '%{',
            multiLineCommentEnd: '%}',
            fileExtensions: ['.m'],
            indentationChar: ' ',
            hasBlockComments: true
        }
    };
    /**
     * Inserts text at the cursor position
     */
    async insertAtCursor(text, options = {}) {
        const editor = this.getActiveEditor();
        const formattedText = this.formatText(text, options);
        const position = editor.selection.active;
        const indentedText = options.indentToSelection
            ? this.addIndentation(formattedText, editor, position)
            : formattedText;
        await editor.edit(editBuilder => {
            editBuilder.insert(position, indentedText);
        });
        // Move the cursor to the end of the inserted text
        const newPosition = position.translate(0, indentedText.length);
        editor.selection = new vscode.Selection(newPosition, newPosition);
    }
    /**
     * Inserts text as a comment
     */
    async insertAsComment(text, options = {}) {
        const editor = this.getActiveEditor();
        const languageInfo = this.getLanguageInfo(editor.document.languageId);
        let commentedText;
        if (this.shouldUseMultilineComment(text, options, languageInfo)) {
            commentedText = this.createMultilineComment(text, languageInfo);
        }
        else {
            commentedText = this.createSingleLineComment(text, languageInfo);
        }
        const finalText = options.addNewLine !== false ? commentedText + '\n' : commentedText;
        await this.insertAtCursor(finalText, {
            ...options,
            formatText: false, // Already formatted as a comment
            addNewLine: false // Already added a new line if needed
        });
    }
    /**
     * Replaces the selected text
     */
    async replaceSelection(text, options = {}) {
        const editor = this.getActiveEditor();
        const selection = editor.selection;
        if (selection.isEmpty) {
            throw this.createError('No selected text to replace', 'NO_SELECTION', 'replace');
        }
        const formattedText = this.formatText(text, options);
        await editor.edit(editBuilder => {
            editBuilder.replace(selection, formattedText);
        });
    }
    /**
     * Inserts text on a new line
     */
    async insertOnNewLine(text, options = {}) {
        const editor = this.getActiveEditor();
        const position = editor.selection.active;
        // Move to the end of the current line
        const lineEndPosition = new vscode.Position(position.line, editor.document.lineAt(position.line).text.length);
        const newLineText = '\n' + this.formatText(text, options);
        await editor.edit(editBuilder => {
            editBuilder.insert(lineEndPosition, newLineText);
        });
    }
    /**
     * Copies text to the clipboard
     */
    async copyToClipboard(text, options = {}) {
        const formattedText = this.formatText(text, options);
        await vscode.env.clipboard.writeText(formattedText);
        vscode.window.showInformationMessage(`Copied to clipboard: "${formattedText.substring(0, 50)}${formattedText.length > 50 ? '...' : ''}"`);
    }
    /**
     * Universal method for inserting text
     */
    async insertText(text, options = {}) {
        const mode = options.mode || 'cursor';
        switch (mode) {
            case 'cursor':
                try {
                    await this.insertAtCursor(text, options);
                }
                catch (error) {
                    // If no active editor, fallback to clipboard
                    if (error.code === 'NO_ACTIVE_EDITOR') {
                        GlobalOutput_1.ExtensionLog.warn(`⚠️ [TextInserter] No active editor, falling back to clipboard`);
                        await this.copyToClipboard(text, options);
                        vscode.window.showWarningMessage(`No active editor. Text copied to clipboard instead.`);
                    }
                    else {
                        throw error;
                    }
                }
                break;
            case 'clipboard':
                await this.copyToClipboard(text, options);
                break;
            default:
                GlobalOutput_1.ExtensionLog.error(`❌ [TextInserter] Unknown mode: ${mode}`);
                throw this.createError(`Unsupported insertion mode: ${mode}`, 'INVALID_MODE', mode);
        }
    }
    /**
     * Gets information about the current context
     */
    getActiveContext() {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            // Check the active terminal
            const terminal = vscode.window.activeTerminal;
            return {
                type: terminal ? 'terminal' : 'unknown',
                hasSelection: false
            };
        }
        const selection = editor.selection;
        const hasSelection = !selection.isEmpty;
        return {
            type: 'editor',
            language: editor.document.languageId,
            hasSelection,
            selectionText: hasSelection ? editor.document.getText(selection) : undefined,
            cursorPosition: editor.selection.active
        };
    }
    /**
     * Gets information about the programming language
     */
    getLanguageInfo(languageId) {
        return this.languageMap[languageId] || {
            singleLineComment: '//',
            fileExtensions: [],
            indentationChar: ' ',
            hasBlockComments: false
        };
    }
    /**
     * Determines if a multiline comment is needed
     */
    shouldUseMultilineComment(text, options, languageInfo) {
        if (options.forceMultilineComment) {
            return languageInfo.hasBlockComments;
        }
        // Use a multiline comment for text with line breaks
        return text.includes('\n') && languageInfo.hasBlockComments;
    }
    /**
     * Creates a single line comment
     */
    createSingleLineComment(text, languageInfo) {
        const lines = text.split('\n');
        const commentPrefix = languageInfo.singleLineComment;
        return lines
            .map(line => line.trim() ? `${commentPrefix} ${line}` : commentPrefix)
            .join('\n');
    }
    /**
     * Creates a multiline comment
     */
    createMultilineComment(text, languageInfo) {
        if (!languageInfo.multiLineCommentStart || !languageInfo.multiLineCommentEnd) {
            return this.createSingleLineComment(text, languageInfo);
        }
        const start = languageInfo.multiLineCommentStart;
        const end = languageInfo.multiLineCommentEnd;
        // Special handling for HTML/XML comments
        if (start === '<!--') {
            return `${start} ${text} ${end}`;
        }
        // For languages with /* */ style
        if (start === '/*') {
            return `${start}\n${text}\n${end}`;
        }
        // For languages with specific block comments (Python, Ruby)
        return `${start}\n${text}\n${end}`;
    }
    /**
     * Formats text according to the options
     */
    formatText(text, options) {
        if (!options.formatText) {
            return text;
        }
        // Basic formatting
        let formatted = text.trim();
        // Add a new line at the end if needed
        if (options.addNewLine) {
            formatted += '\n';
        }
        return formatted;
    }
    /**
     * Adds indentation to the text according to the current cursor position
     */
    addIndentation(text, editor, position) {
        const currentLine = editor.document.lineAt(position.line);
        const indentation = currentLine.text.substring(0, currentLine.firstNonWhitespaceCharacterIndex);
        const lines = text.split('\n');
        return lines
            .map((line, index) => index === 0 ? line : indentation + line)
            .join('\n');
    }
    /**
     * Gets the active editor or throws an error
     */
    getActiveEditor() {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            throw this.createError('No active editor. Open a file for editing.', 'NO_ACTIVE_EDITOR', 'editor');
        }
        return editor;
    }
    /**
     * Creates a typed error
     */
    createError(message, code, context) {
        const error = new Error(message);
        error.code = code;
        error.context = context;
        return error;
    }
    /**
     * Gets supported languages
     */
    static getSupportedLanguages() {
        return Object.keys(new TextInserter().languageMap);
    }
    /**
     * Checks if the language is supported
     */
    static isLanguageSupported(languageId) {
        return languageId in new TextInserter().languageMap;
    }
}
exports.TextInserter = TextInserter;
//# sourceMappingURL=TextInserter.js.map