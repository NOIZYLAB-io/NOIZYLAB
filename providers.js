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
exports.LanguageProviderFactory = void 0;
const vscode = __importStar(require("vscode"));
const constants_1 = require("../config/constants");
/**
 * Factory class for creating language service providers.
 */
class LanguageProviderFactory {
    keywords;
    constructor(keywords) {
        this.keywords = keywords;
    }
    /**
     * Creates and registers completion and hover providers for SAPF.
     * @returns Array of disposable providers
     */
    createProviders() {
        const completionProvider = this.createCompletionProvider();
        const hoverProvider = this.createHoverProvider();
        return [completionProvider, hoverProvider];
    }
    /**
     * Creates a completion provider for SAPF.
     * @returns Completion provider disposable
     */
    createCompletionProvider() {
        return vscode.languages.registerCompletionItemProvider('sapf', {
            provideCompletionItems: (doc, position) => {
                const config = vscode.workspace.getConfiguration('sapf');
                const completionInfo = config.get('completionInfo', 'full');
                const prefix = doc.lineAt(position).text.slice(0, position.character);
                const match = prefix.match(constants_1.wordRegex);
                const current = match?.[0] ?? '';
                const currentLower = current.toLowerCase();
                const start = position.translate(0, -current.length);
                const range = new vscode.Range(start, position);
                return [...this.keywords.values()]
                    .filter(({ keyword }) => current.length === 0 || keyword.toLowerCase().startsWith(currentLower))
                    .map(({ keyword, signature, description, category, special }) => {
                    const item = new vscode.CompletionItem(keyword, vscode.CompletionItemKind.Function);
                    item.range = range;
                    if (completionInfo === 'off') {
                        // Just provide the function name without any details
                    }
                    else if (completionInfo === 'minimum') {
                        item.detail = signature ?? '(no signature)';
                    }
                    else {
                        // 'full'
                        item.detail = signature ?? description.split('\n')[0] ?? '';
                        const md = new vscode.MarkdownString(undefined, true);
                        md.appendMarkdown(`**Category**: ${category}\n\n`);
                        md.appendCodeblock(`${keyword} ${special !== null ? `${special} ` : ''}${signature ?? '(no signature)'}`, 'sapf');
                        md.appendMarkdown(`\n\n${description}`);
                        item.documentation = md;
                    }
                    return item;
                });
            },
        }, ...constants_1.completionTriggerCharacters);
    }
    /**
     * Creates a hover provider for SAPF.
     * @returns Hover provider disposable
     */
    createHoverProvider() {
        return vscode.languages.registerHoverProvider('sapf', {
            provideHover: (doc, position) => {
                const config = vscode.workspace.getConfiguration('sapf');
                const hoverInfo = config.get('hoverInfo', 'full');
                if (hoverInfo === 'off') {
                    return undefined;
                }
                const range = doc.getWordRangeAtPosition(position);
                if (!range) {
                    return undefined;
                }
                const wordLower = doc.getText(range).toLowerCase();
                const info = this.keywords.get(wordLower);
                if (info == null) {
                    return undefined;
                }
                const md = new vscode.MarkdownString(undefined, true);
                if (hoverInfo === 'minimum') {
                    md.appendCodeblock(`${info.keyword} ${info.signature ?? '(no signature)'}`, 'sapf');
                }
                else {
                    // 'full'
                    md.appendMarkdown(`**Category**: ${info.category}\n\n`);
                    md.appendCodeblock(`${info.keyword} ${info.special !== null ? `${info.special} ` : ''}${info.signature ?? '(no signature)'}`, 'sapf');
                    md.appendMarkdown(`\n\n${info.description}`);
                }
                return new vscode.Hover(md);
            },
        });
    }
}
exports.LanguageProviderFactory = LanguageProviderFactory;
//# sourceMappingURL=providers.js.map