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
exports.changeGroup = void 0;
const vscode = require("vscode");
const configMgr_1 = require("../helper/configMgr");
const util_1 = require("../helper/util");
const enum_1 = require("../enum");
function changeGroup(favoritesProvider) {
    return vscode.commands.registerCommand('favorites.group.changeGroup', function (value) {
        return __awaiter(this, void 0, void 0, function* () {
            const isGitUsed = !!(0, util_1.getFirstGitRepository)();
            let branchName = 'no_git_master';
            if (isGitUsed) {
                branchName = (0, util_1.getGitBranchName)();
            }
            const currentGroup = configMgr_1.default.get('currentGroup') || enum_1.DEFAULT_GROUP;
            const groups = Array.from(new Set((configMgr_1.default.get('groups') || []).concat([enum_1.DEFAULT_GROUP])));
            let doesCurrentBranchNameGroupExist;
            let isInCurrentBranchGroup;
            if (isGitUsed) {
                doesCurrentBranchNameGroupExist = groups.indexOf(branchName) !== -1;
                isInCurrentBranchGroup = currentGroup === branchName;
            }
            vscode.window
                .showQuickPick(isGitUsed && doesCurrentBranchNameGroupExist && !isInCurrentBranchGroup
                ? ['Switch to current branch group'].concat(groups.filter((item) => item !== branchName && item !== currentGroup))
                : groups.filter((item) => item !== branchName && item !== currentGroup), { title: 'Choose a group you want to switch to' })
                .then((selectedCommand) => {
                if (selectedCommand === 'Switch to current branch group') {
                    configMgr_1.default.save('currentGroup', branchName);
                }
                else if (selectedCommand != undefined) {
                    configMgr_1.default.save('currentGroup', selectedCommand);
                }
            });
        });
    });
}
exports.changeGroup = changeGroup;

//# sourceMappingURL=changeGroup.js.map
