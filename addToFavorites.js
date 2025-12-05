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
exports.addToFavorites = void 0;
const vscode = require("vscode");
const util_1 = require("../helper/util");
const configMgr_1 = require("../helper/configMgr");
const enum_1 = require("../enum");
function addToFavorites() {
    return vscode.commands.registerCommand('favorites.addToFavorites', (fileUri) => __awaiter(this, void 0, void 0, function* () {
        if (!fileUri) {
            if (!vscode.window.activeTextEditor) {
                return vscode.window.showWarningMessage('You have to choose a resource first');
            }
            fileUri = vscode.window.activeTextEditor.document.uri;
        }
        const fileName = fileUri.fsPath;
        const previousResources = (0, util_1.getCurrentResources)();
        // Store the stringified uri for any resource that isn't a file
        const newResource = fileUri.scheme !== 'file'
            ? fileUri.toString()
            : (0, util_1.isMultiRoots)()
                ? fileName
                : fileName.substr((0, util_1.getSingleRootPath)().length + 1);
        const currentGroup = configMgr_1.default.get('currentGroup') || enum_1.DEFAULT_GROUP;
        if (previousResources.some((r) => r.filePath === newResource && r.group === currentGroup)) {
            return;
        }
        yield configMgr_1.default
            .save('resources', previousResources.concat([
            { filePath: newResource, group: currentGroup },
        ]))
            .catch(console.warn);
        if (configMgr_1.default.get('groups') == undefined || configMgr_1.default.get('groups').length == 0) {
            configMgr_1.default.save('groups', [enum_1.DEFAULT_GROUP]).catch(console.warn);
        }
    }));
}
exports.addToFavorites = addToFavorites;

//# sourceMappingURL=addToFavorites.js.map
