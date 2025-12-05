"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.WorkspaceLibraryExecutionManager = exports.resetWorkspaceTrustCommand = exports.manageWorkspaceTrustCommand = void 0;
const vscode = require("vscode");
exports.manageWorkspaceTrustCommand = 'tslint.manageWorkspaceLibraryExecution';
exports.resetWorkspaceTrustCommand = 'tslint.resetWorkspaceLibraryExecution';
class WorkspaceLibraryExecutionManager {
    constructor(context) {
        this.isTrustedWorkspaceKey = 'tslint.isTrustedWorkspace';
        this.isTrustedGloballyKey = 'tslint.allowGlobalLibraryExecution';
        this._disposables = [];
        this._onDidChange = new vscode.EventEmitter();
        this.onDidChange = this._onDidChange.event;
        this.globalMemento = context.globalState;
        this.workspaceMemento = context.workspaceState;
        this._disposables.push(vscode.commands.registerCommand(exports.manageWorkspaceTrustCommand, () => {
            this.showTrustUi();
        }));
        this._disposables.push(vscode.commands.registerCommand(exports.resetWorkspaceTrustCommand, () => {
            this.reset();
        }));
    }
    dispose() {
        for (const disposable of this._disposables) {
            disposable.dispose();
        }
        this._disposables = [];
    }
    allowWorkspaceLibraryExecution() {
        const global = this.globalMemento.get(this.isTrustedGloballyKey);
        if (global) {
            return true;
        }
        return this.workspaceMemento.get(this.isTrustedWorkspaceKey);
    }
    showTrustUi() {
        return __awaiter(this, void 0, void 0, function* () {
            const currentIsTrustedWorkspaceValue = this.workspaceMemento.get(this.isTrustedWorkspaceKey);
            const trustItem = {
                label: "Enable workspace library execution",
                description: currentIsTrustedWorkspaceValue === true ? "(currently active)" : undefined,
                detail: "Enable loading TSLint and linting rules from the current workspace.",
            };
            const untrustItem = {
                label: "Disable workspace library execution",
                description: currentIsTrustedWorkspaceValue === false ? "(currently active)" : undefined,
                detail: "Blocks loading TSLint from the current workspace. The global TSLint can still be used.",
            };
            const trustGloballyItem = {
                label: "Always enable workspace library execution",
                description: this.globalMemento.get(this.isTrustedGloballyKey) ? "(enabled)" : undefined,
                detail: "Enables loading TSLint in all workspaces without prompting.",
            };
            const helpItem = {
                label: "Help",
            };
            const result = yield vscode.window.showQuickPick([
                trustItem,
                untrustItem,
                trustGloballyItem,
                helpItem
            ], {
                placeHolder: "Configure workspace library execution"
            });
            switch (result) {
                case trustItem:
                    yield this.workspaceMemento.update(this.isTrustedWorkspaceKey, true);
                    this._onDidChange.fire();
                    break;
                case untrustItem:
                    yield this.workspaceMemento.update(this.isTrustedWorkspaceKey, false);
                    this._onDidChange.fire();
                    break;
                case trustGloballyItem:
                    yield this.globalMemento.update(this.isTrustedGloballyKey, true);
                    this._onDidChange.fire();
                    break;
                case helpItem:
                    yield vscode.env.openExternal(vscode.Uri.parse('https://github.com/microsoft/typescript-tslint-plugin#readme'));
                    break;
            }
        });
    }
    reset() {
        this.globalMemento.update(this.isTrustedGloballyKey, undefined);
        this.workspaceMemento.update(this.isTrustedWorkspaceKey, undefined);
        this._onDidChange.fire();
    }
}
exports.WorkspaceLibraryExecutionManager = WorkspaceLibraryExecutionManager;
//# sourceMappingURL=workspaceTrustManager.js.map