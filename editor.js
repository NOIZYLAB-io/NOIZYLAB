"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Editor = void 0;
const vscode = require("vscode");
class Editor {
    constructor(context) {
        this.outputChannel = vscode.window.createOutputChannel('GPT Copilot');
        this.context = context;
    }
    writeToConsole(text) {
        this.outputChannel.appendLine(text);
        this.outputChannel.show();
    }
    async getUserInput(prompt, placeHolder, errorText, password = false) {
        return await vscode.window.showInputBox({
            prompt,
            placeHolder,
            password,
            ignoreFocusOut: true,
            validateInput: (value) => {
                if (value.length === 0) {
                    return errorText;
                }
                return null;
            }
        });
    }
    showErrorMessage(message) {
        void vscode.window.showErrorMessage(message);
    }
    getCurrentFileContents() {
        const editor = vscode.window.activeTextEditor;
        if (editor != null) {
            const document = editor.document;
            return document.getText();
        }
        return '';
    }
    getCurrentFileExtension() {
        const editor = vscode.window.activeTextEditor;
        if (editor != null) {
            const fileName = editor.document.fileName;
            const extension = fileName.split('.').pop();
            if (extension != null) {
                return extension;
            }
        }
        return '';
    }
    getHighlightedText() {
        const editor = vscode.window.activeTextEditor;
        if (editor != null) {
            const selection = editor.selection;
            if (!selection.isEmpty) {
                const selectionRange = new vscode.Range(selection.start.line, selection.start.character, selection.end.line, selection.end.character);
                return editor.document.getText(selectionRange);
            }
        }
        return '';
    }
    async getSecret(key) {
        return await this.context.secrets.get(key);
    }
    setSecret(key, value) {
        void this.context.secrets.store(key, value);
        void vscode.window.showInformationMessage('API Key saved');
    }
    getConfigValue(key) {
        return vscode.workspace.getConfiguration('gpt-copilot').get(key);
    }
}
exports.Editor = Editor;
//# sourceMappingURL=Editor.js.map