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
exports.revealInSideBar = void 0;
const vscode = require("vscode");
function revealInSideBar() {
    return vscode.commands.registerCommand('favorites.revealInSideBar', function (value) {
        return __awaiter(this, void 0, void 0, function* () {
            if (!value && !vscode.window.activeTextEditor) {
                return vscode.window.showWarningMessage('You have to choose a resource first');
            }
            if (value.uri) {
                yield vscode.commands.executeCommand('revealInExplorer', value.uri);
            }
        });
    });
}
exports.revealInSideBar = revealInSideBar;

//# sourceMappingURL=revealInSideBar.js.map
