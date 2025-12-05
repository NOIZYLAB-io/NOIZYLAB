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
exports.moveToBottom = void 0;
const vscode = require("vscode");
const configMgr_1 = require("../helper/configMgr");
const util_1 = require("../helper/util");
function moveToBottom(favoritesProvider) {
    return vscode.commands.registerCommand('favorites.moveToBottom', function (value) {
        return __awaiter(this, void 0, void 0, function* () {
            const config = vscode.workspace.getConfiguration('favorites');
            const currentGroup = configMgr_1.default.get('currentGroup');
            const items = yield (0, util_1.getCurrentResources)();
            const filteredArray = [];
            items.forEach((value, index) => {
                if (value.group == currentGroup) {
                    filteredArray.push({ filePath: value.filePath, group: value.group, previousIndex: index });
                }
            });
            const currentIndex = filteredArray.find((i) => i.filePath === value.value).previousIndex;
            if (currentIndex === filteredArray[filteredArray.length - 1].previousIndex) {
                return;
            }
            items.push(items[currentIndex]);
            items.splice(currentIndex, 1);
            config.update('sortOrder', 'MANUAL', false);
            configMgr_1.default.save('resources', items).catch(console.warn);
        });
    });
}
exports.moveToBottom = moveToBottom;

//# sourceMappingURL=moveToBottom.js.map
