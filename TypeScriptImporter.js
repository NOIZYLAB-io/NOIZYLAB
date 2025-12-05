"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
const ImportIndexer_1 = require("./ImportIndexer");
const ImportIndex_1 = require("./ImportIndex");
const Importer_1 = require("./Importer");
function activate(context) {
    let importer = new TypeScriptImporter(context);
    if (importer.disabled)
        return;
    importer.start();
}
exports.activate = activate;
function deactivate() {
}
exports.deactivate = deactivate;
class SymbolCompletionItem extends vscode.CompletionItem {
    constructor(doc, m, lowImportance) {
        super(m.name);
        this.m = m;
        if (!m.type)
            this.kind = vscode.CompletionItemKind.File;
        else if (m.type.indexOf("class") >= 0)
            this.kind = vscode.CompletionItemKind.Class;
        else if (m.type.indexOf("interface") >= 0)
            this.kind = vscode.CompletionItemKind.Interface;
        else if (m.type.indexOf("function") >= 0)
            this.kind = vscode.CompletionItemKind.Function;
        else
            this.kind = vscode.CompletionItemKind.Variable;
        this.description = this.documentation = m.module || m.path;
        if (lowImportance) {
            this.sortText = "zzzzzzzzzz" + m.name;
            this.label = m.name;
            this.insertText = m.name;
        }
        if (doc)
            this.command = {
                title: "import",
                command: 'tsimporter.importSymbol',
                arguments: [doc, m]
            };
    }
}
function getSelectedWord() {
    if (!vscode.window.activeTextEditor)
        return "";
    let document = vscode.window.activeTextEditor.document;
    if (!document)
        return "";
    let word = "";
    let selection = vscode.window.activeTextEditor.selection;
    if (selection) {
        let w = selection;
        if (selection.isEmpty)
            w = document.getWordRangeAtPosition(selection.active);
        if (w && w.isSingleLine) {
            word = document.getText(w);
        }
    }
    return word;
}
class TypeScriptImporter {
    constructor(context) {
        this.context = context;
        this.disabled = false;
        this.noStatusBar = false;
        this.lowImportance = false;
        this.emitSemicolon = true;
        this.status = "Initializing";
        if (vscode.workspace.rootPath === undefined)
            this.disabled = true;
        else
            this.disabled = this.conf("disabled");
        this.loadConfig();
    }
    conf(property, defaultValue) {
        return vscode.workspace.getConfiguration('tsimporter').get(property, defaultValue);
    }
    loadConfig() {
        this.showNotifications = this.conf('showNotifications');
        this.removeFileExtensions = this.conf('removeFileExtensions', '.d.ts,.ts,.tsx').trim().split(/\s*,\s*/);
        this.lowImportance = this.conf('lowImportance', false);
        this.emitSemicolon = this.conf('emitSemicolon', true);
        this.noStatusBar = this.conf('noStatusBar', false);
    }
    start() {
        this.indexer = new ImportIndexer_1.ImportIndexer(this);
        this.indexer.attachFileWatcher();
        this.codeCompletionIndexer = new ImportIndexer_1.ImportIndexer(this);
        this.importer = new Importer_1.Importer(this);
        let codeActionFixer = vscode.languages.registerCodeActionsProvider('typescript', this);
        let completionItem = vscode.languages.registerCompletionItemProvider('typescript', this);
        let codeActionFixerReact = vscode.languages.registerCodeActionsProvider('typescriptreact', this);
        let completionItemReact = vscode.languages.registerCompletionItemProvider('typescriptreact', this);
        let codeActionFixerVue = vscode.languages.registerCodeActionsProvider('vue', this);
        let completionItemVue = vscode.languages.registerCompletionItemProvider('vue', this);
        let reindexCommand = vscode.commands.registerCommand('tsimporter.reindex', () => {
            this.loadConfig();
            this.indexer.reset();
            this.indexer.attachFileWatcher();
            this.indexer.scanAll(true);
        });
        let addImport = vscode.commands.registerCommand('tsimporter.addImport', () => {
            if (!vscode.window.activeTextEditor)
                return;
            let document = vscode.window.activeTextEditor.document;
            let word = getSelectedWord();
            this.codeCompletionIndexer.index.resetIndex();
            this.codeCompletionIndexer.processFile(document.getText(), document.uri, false);
            var definitions = [];
            this.indexer.index.getSymbols(word, true, ImportIndex_1.MatchMode.ANY).forEach(m => {
                if (this.codeCompletionIndexer.index.getSymbols(m.name, false, ImportIndex_1.MatchMode.EXACT).length == 0) {
                    var ci = new SymbolCompletionItem(document, m, this.lowImportance);
                    definitions.push(ci);
                }
            });
            let importItem = item => {
                if (item)
                    vscode.commands.executeCommand(item.command.command, item.command.arguments[0], item.command.arguments[1]);
            };
            if (definitions.length == 0) {
                vscode.window.showInformationMessage("no importable symbols found!");
            }
            else if (definitions.length == 1) {
                importItem(definitions[0]);
            }
            else {
                vscode.window.showQuickPick(definitions).then(importItem);
            }
        });
        let openSymbol = vscode.commands.registerCommand('tsimporter.openSymbol', () => {
            let word = getSelectedWord();
            var definitions = [];
            this.indexer.index.getSymbols(word, true, ImportIndex_1.MatchMode.ANY).forEach(m => {
                if (m.path) {
                    var ci = new SymbolCompletionItem(null, m, this.lowImportance);
                    definitions.push(ci);
                }
            });
            let openItem = item => {
                if (item) {
                    let uri = vscode.Uri.file(item.m.path);
                    console.log(uri);
                    vscode.workspace.openTextDocument(uri).then(r => {
                        vscode.window.showTextDocument(r);
                    }, f => {
                        console.error("fault", f);
                    });
                }
            };
            if (definitions.length == 0) {
                vscode.window.showInformationMessage("no importable symbols found!");
            }
            else if (definitions.length == 1) {
                openItem(definitions[0]);
            }
            else {
                vscode.window.showQuickPick(definitions).then(openItem);
            }
        });
        let dumpSymbolsCommand = vscode.commands.registerCommand('tsimporter.dumpIndex', () => {
            let change = vscode.window.onDidChangeActiveTextEditor(e => {
                change.dispose();
                let edit = new vscode.WorkspaceEdit();
                edit.insert(e.document.uri, new vscode.Position(0, 0), JSON.stringify(this.indexer.index, null, "\t"));
                vscode.workspace.applyEdit(edit);
            });
            vscode.commands.executeCommand("workbench.action.files.newUntitledFile");
        });
        let importCommand = vscode.commands.registerCommand('tsimporter.importSymbol', (document, symbol) => {
            this.importer.importSymbol(document, symbol);
        });
        this.statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 1);
        this.setStatusBar("initializing");
        this.statusBar.command = 'tsimporter.dumpIndex';
        if (this.noStatusBar)
            this.statusBar.hide();
        else
            this.statusBar.show();
        this.context.subscriptions.push(codeActionFixer, completionItem, codeActionFixerReact, completionItemReact, codeActionFixerVue, completionItemVue, importCommand, dumpSymbolsCommand, this.statusBar);
        vscode.commands.executeCommand('tsimporter.reindex', { showOutput: true });
    }
    removeFileExtension(fileName) {
        for (var i = 0; i < this.removeFileExtensions.length; i++) {
            var e = this.removeFileExtensions[i];
            if (fileName.endsWith(e))
                return fileName.substring(0, fileName.length - e.length);
        }
        return fileName;
    }
    showNotificationMessage(message) {
        if (this.showNotifications)
            vscode.window.showInformationMessage('[TypeScript Importer] ' + message);
    }
    setStatusBar(status) {
        this.status = status;
        if (this.statusBar)
            this.statusBar.text = "[TypeScript Importer]: " + this.status;
    }
    /**
     * Provide completion items for the given position and document.
     *
     * @param document The document in which the command was invoked.
     * @param position The position at which the command was invoked.
     * @param token A cancellation token.
     * @return An array of completions, a [completion list](#CompletionList), or a thenable that resolves to either.
     * The lack of a result can be signaled by returning `undefined`, `null`, or an empty array.
     */
    provideCompletionItems(document, position, token) {
        var line = document.lineAt(position.line);
        var lineText = line.text;
        if (lineText) {
            var docText = document.getText();
            var len = document.offsetAt(position);
            let idx = 0;
            let MODE;
            (function (MODE) {
                MODE[MODE["Code"] = 0] = "Code";
                MODE[MODE["MultiLineComment"] = 1] = "MultiLineComment";
                MODE[MODE["LineComment"] = 2] = "LineComment";
                MODE[MODE["SingleQuoteString"] = 3] = "SingleQuoteString";
                MODE[MODE["DoubleQuoteString"] = 4] = "DoubleQuoteString";
                MODE[MODE["MultiLineString"] = 5] = "MultiLineString";
            })(MODE || (MODE = {}));
            let mode = MODE.Code;
            while (idx < len) {
                let next = docText.substr(idx, 1);
                let next2 = docText.substr(idx, 2);
                switch (mode) {
                    case MODE.Code:
                        {
                            if (next2 == "/*") {
                                mode = MODE.MultiLineComment;
                                idx++;
                            }
                            else if (next2 == "//") {
                                mode = MODE.LineComment;
                                idx++;
                            }
                            else if (next == "'")
                                mode = MODE.SingleQuoteString;
                            else if (next == '"')
                                mode = MODE.DoubleQuoteString;
                            else if (next == '`')
                                mode = MODE.MultiLineString;
                        }
                        break;
                    case MODE.MultiLineComment:
                        {
                            if (next2 == "*/") {
                                mode = MODE.Code;
                                idx++;
                            }
                        }
                        break;
                    case MODE.LineComment:
                        {
                            if (next == "\n") {
                                mode = MODE.Code;
                            }
                        }
                        break;
                    case MODE.SingleQuoteString:
                        {
                            if (next == "'" || next == "\n")
                                mode = MODE.Code;
                        }
                        break;
                    case MODE.DoubleQuoteString:
                        {
                            if (next == '"' || next == "\n")
                                mode = MODE.Code;
                        }
                        break;
                    case MODE.MultiLineString:
                        {
                            if (next == '`')
                                mode = MODE.Code;
                        }
                        break;
                }
                idx++;
            }
            //console.log( "parsed mode is", mode );
            if (mode != MODE.Code)
                return;
        }
        if (lineText && lineText.indexOf("import") >= 0 && lineText.indexOf("from") >= 0) {
            var delims = ["'", '"'];
            var end = position.character;
            var start = end - 1;
            while (delims.indexOf(lineText.charAt(start)) < 0 && start > 0)
                start--;
            if (start > 0) {
                var moduleText = lineText.substring(start + 1, end);
                return this.provideModuleCompletionItems(moduleText, new vscode.Range(new vscode.Position(position.line, start + 1), new vscode.Position(position.line, position.character)));
            }
            else {
                return [];
            }
        }
        else // if( range )
         {
            let s = new Date().getTime();
            let range = null; //document.getWordRangeAtPosition( position );
            let word = "";
            if (range && range.isSingleLine && !range.isEmpty)
                word = document.getText(range).trim();
            this.codeCompletionIndexer.index.resetIndex();
            this.codeCompletionIndexer.processFile(document.getText(), document.uri, false);
            var definitions = [];
            this.indexer.index.getSymbols(word, true, ImportIndex_1.MatchMode.ANY).forEach(m => {
                if (this.codeCompletionIndexer.index.getSymbols(m.name, false, ImportIndex_1.MatchMode.EXACT).length == 0) {
                    var ci = new SymbolCompletionItem(document, m, this.lowImportance);
                    definitions.push(ci);
                }
            });
            //console.log( "provided", definitions.length, "within", (new Date().getTime() - s), "ms" );
            return definitions;
        }
    }
    provideModuleCompletionItems(searchText, replaceRange) {
        var modules = [];
        this.indexer.index.getModules(searchText, true, ImportIndex_1.MatchMode.ANY).forEach(m => {
            var ci = new vscode.CompletionItem(m);
            ci.kind = vscode.CompletionItemKind.File;
            ci.textEdit = new vscode.TextEdit(replaceRange, m);
            modules.push(ci);
        });
        return modules;
    }
    /**
     * Given a completion item fill in more data, like [doc-comment](#CompletionItem.documentation)
     * or [details](#CompletionItem.detail).
     *
     * The editor will only resolve a completion item once.
     *
     * @param item A completion item currently active in the UI.
     * @param token A cancellation token.
     * @return The resolved completion item or a thenable that resolves to of such. It is OK to return the given
     * `item`. When no result is returned, the given `item` will be used.
     */
    resolveCompletionItem(item, token) {
        return item;
    }
    /**
     * Provide commands for the given document and range.
     *
     * @param document The document in which the command was invoked.
     * @param range The range for which the command was invoked.
     * @param context Context carrying additional information.
     * @param token A cancellation token.
     * @return An array of commands or a thenable of such. The lack of a result can be
     * signaled by returning `undefined`, `null`, or an empty array.
     */
    provideCodeActions(document, range, context, token) {
        if (context && context.diagnostics) {
            for (var i = 0; i < context.diagnostics.length; i++) {
                var symbols = this.getSymbolsForDiagnostic(context.diagnostics[i].message);
                if (symbols.length) {
                    let handlers = [];
                    for (var s = 0; s < symbols.length; s++) {
                        var symbol = symbols[s];
                        handlers.push({
                            title: this.importer.createImportStatement(this.importer.createImportDefinition(symbol.name), this.importer.resolveModule(document, symbol)),
                            command: 'tsimporter.importSymbol',
                            arguments: [document, symbol]
                        });
                    }
                    ;
                    return handlers;
                }
            }
        }
        return [];
    }
    getSymbolsForDiagnostic(message) {
        var test = /Cannot find name ['"](.*?)['"]\./;
        var match;
        if (message && (match = test.exec(message))) {
            let missing = match[1];
            return this.indexer.index.getSymbols(missing, false, ImportIndex_1.MatchMode.EXACT);
        }
        else
            return [];
    }
}
exports.TypeScriptImporter = TypeScriptImporter;
//# sourceMappingURL=TypeScriptImporter.js.map