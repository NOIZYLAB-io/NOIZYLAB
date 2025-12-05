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
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const keywordsData = __importStar(require("./language.json")); // Relative path to the JSON file
let sapfTerminal;
const sapfKeywords = new Map();
function parseAndPopulateKeywords(categories) {
    try {
        for (const categoryName in categories) {
            if (Object.prototype.hasOwnProperty.call(categories, categoryName)) {
                const category = categories[categoryName];
                const items = category.items;
                for (const keyword in items) {
                    if (Object.prototype.hasOwnProperty.call(items, keyword)) {
                        let description = items[keyword];
                        let signature = null;
                        let special = null;
                        // Regex to find:
                        // 1. Optional special annotation like @zzz, @kkk (group 1)
                        // 2. The signature like (a b --> c) (group 2)
                        // 3. The remaining description (group 3)
                        const regex = /^(?:(@[a-z]+)\s*)?(\([^)]*?\s*-->\s*[^)]*?\))?\s*(.*)$/;
                        const match = description.match(regex);
                        if (match) {
                            special = match[1] || null;
                            signature = match[2] || null;
                            description = match[3] || description; // Use remaining part or original if no match
                        }
                        sapfKeywords.set(keyword, {
                            keyword: keyword,
                            signature: signature,
                            description: description.trim(), // Trim leading/trailing whitespace
                            category: categoryName,
                            special: special
                        });
                    }
                }
            }
        }
        console.log(`Loaded ${sapfKeywords.size} SAPF keywords.`);
    }
    catch (e) {
        console.error("Failed to parse SAPF keywords JSON:", e);
    }
}
function getBlockOrLine(editor) {
    const text = editor.document.getText();
    const cursorOffset = editor.document.offsetAt(editor.selection.active);
    // Find block enclosed in ( ... ) that contains the cursor
    let start = -1, end = -1, balance = 0;
    for (let i = cursorOffset - 1; i >= 0; i--) {
        const c = text[i];
        if (c === ')')
            balance++;
        else if (c === '(') {
            if (balance === 0) {
                start = i;
                break;
            }
            balance--;
        }
    }
    balance = 0;
    for (let i = cursorOffset; i < text.length; i++) {
        const c = text[i];
        if (c === '(')
            balance++;
        else if (c === ')') {
            if (balance === 0) {
                end = i;
                break;
            }
            balance--;
        }
    }
    if (start !== -1 && end !== -1) {
        const block = text.slice(start + 1, end);
        const lines = block.split(/\r?\n/).map(line => line.trim());
        return lines.join('\n');
    }
    // Fallback to current line
    return editor.document.lineAt(editor.selection.active.line).text.trim();
}
function activate(context) {
    parseAndPopulateKeywords(keywordsData);
    const completionProvider = vscode.languages.registerCompletionItemProvider("sapf", {
        provideCompletionItems(document, position) {
            const linePrefix = document.lineAt(position).text.substring(0, position.character);
            // Simple word regex to find the current word being typed
            const wordMatch = linePrefix.match(/[\w\-\?]+$/);
            const currentWord = wordMatch ? wordMatch[0] : '';
            if (!currentWord) {
                return undefined;
            }
            const completionItems = [];
            for (const [keywordName, keywordInfo] of sapfKeywords.entries()) {
                if (keywordName.startsWith(currentWord)) {
                    const item = new vscode.CompletionItem(keywordName, vscode.CompletionItemKind.Function);
                    // Use signature for detail or first line of description
                    item.detail = keywordInfo.signature || keywordInfo.description.split('\n')[0];
                    // Create Markdown documentation
                    const docs = new vscode.MarkdownString();
                    docs.appendMarkdown(`**Category**: ${keywordInfo.category}\n\n`);
                    docs.appendCodeblock(`${keywordName} ${keywordInfo.special ? keywordInfo.special + ' ' : ''}${keywordInfo.signature || '(no signature)'}`, "sapf");
                    docs.appendMarkdown(`\n\n${keywordInfo.description}`);
                    item.documentation = docs;
                    completionItems.push(item);
                }
            }
            return completionItems;
        }
    });
    context.subscriptions.push(completionProvider);
    const hoverProvider = vscode.languages.registerHoverProvider("sapf", {
        provideHover(document, position) {
            const range = document.getWordRangeAtPosition(position);
            if (!range) {
                return undefined;
            }
            const word = document.getText(range);
            const keywordInfo = sapfKeywords.get(word);
            if (keywordInfo) {
                const docs = new vscode.MarkdownString();
                docs.appendMarkdown(`**Category**: ${keywordInfo.category}\n\n`);
                docs.appendCodeblock(`${keywordInfo.keyword} ${keywordInfo.special ? keywordInfo.special + ' ' : ''}${keywordInfo.signature || '(no signature)'}`, "sapf");
                docs.appendMarkdown(`\n\n${keywordInfo.description}`);
                return new vscode.Hover(docs);
            }
            return undefined;
        }
    });
    context.subscriptions.push(hoverProvider);
    const evalLineCommand = vscode.commands.registerCommand('vsapf.evalLine', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            return;
        }
        const line = getBlockOrLine(editor);
        const binaryPath = vscode.workspace.getConfiguration().get('vsapf.binaryPath') || '';
        const binaryArgs = vscode.workspace.getConfiguration().get('vsapf.binaryArgs') || [];
        // Create terminal if not exists
        if (!sapfTerminal) {
            sapfTerminal = vscode.window.createTerminal({
                name: 'SAPF REPL',
                shellPath: binaryPath,
                shellArgs: binaryArgs
            });
            sapfTerminal.show(true);
        }
        // Send current line to terminal
        sapfTerminal.sendText(line, true);
    });
    context.subscriptions.push(evalLineCommand);
    context.subscriptions.push(vscode.commands.registerCommand('vsapf.stop', () => {
        if (sapfTerminal) {
            sapfTerminal.sendText("stop", true);
        }
    }));
    context.subscriptions.push(vscode.window.onDidCloseTerminal(async (terminal) => {
        if (terminal === sapfTerminal) {
            const pid = await sapfTerminal.processId;
            if (pid) {
                console.log(`Terminal process ID: ${pid}. Attempting to terminate.`);
                try {
                    process.kill(pid, 'SIGKILL');
                    console.log(`Sent SIGKILL to PID ${pid}`);
                }
                catch (e) {
                    if (e.code === 'ESRCH') {
                        console.log(`Process ${pid} not found (already exited).`);
                    }
                    else {
                        console.warn(`Error sending signal to PID ${pid}:`, e);
                    }
                }
            }
            sapfTerminal = undefined;
        }
    }));
}
async function deactivate() {
    if (sapfTerminal) {
        sapfTerminal.dispose();
        sapfTerminal = undefined;
    }
}
//# sourceMappingURL=extension%20copy.js.map