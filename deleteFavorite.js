"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deleteFavorite = void 0;
const vscode = require("vscode");
const configMgr_1 = require("../helper/configMgr");
const util_1 = require("../helper/util");
function deleteFavorite() {
    return vscode.commands.registerCommand('favorites.deleteFavorite', (value) => {
        if (!value) {
            if (!vscode.window.activeTextEditor) {
                return vscode.window.showWarningMessage('You have to choose a resource first');
            }
            value = vscode.window.activeTextEditor.document.uri;
        }
        const previousResources = (0, util_1.getCurrentResources)();
        const uri = value.resourceUri || value;
        if (uri.scheme === 'file') {
            const fsPath = value.value || value.fsPath;
            const currentGroup = configMgr_1.default.get('currentGroup');
            configMgr_1.default
                .save('resources', previousResources.filter((r) => {
                if ((r.filePath !== fsPath && (0, util_1.pathResolve)(r.filePath) !== fsPath) || r.group !== currentGroup) {
                    return true;
                }
                return false;
            }))
                .catch(console.warn);
        }
        else {
            // Not a file, so remove the stringified uri
            configMgr_1.default
                .save('resources', previousResources.filter((r) => {
                if (r.filePath !== uri.toString()) {
                    return true;
                }
                return false;
            }))
                .catch(console.warn);
        }
    });
}
exports.deleteFavorite = deleteFavorite;

//# sourceMappingURL=deleteFavorite.js.map
