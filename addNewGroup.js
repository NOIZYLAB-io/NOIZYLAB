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
exports.addNewGroup = void 0;
const vscode = require("vscode");
const configMgr_1 = require("../helper/configMgr");
const enum_1 = require("../enum");
const util_1 = require("../helper/util");
function addNewGroup(favoritesProvider) {
    return vscode.commands.registerCommand('favorites.group.newGroup', function (value) {
        return __awaiter(this, void 0, void 0, function* () {
            const isGitUsed = !!(0, util_1.getFirstGitRepository)();
            let branchName = 'no_git_master';
            if (isGitUsed) {
                branchName = (0, util_1.getGitBranchName)();
            }
            const previousGroups = Array.from(new Set((configMgr_1.default.get('groups') || []).concat([enum_1.DEFAULT_GROUP])));
            vscode.window
                .showQuickPick(['Input new group name'].concat(!isGitUsed ? [] : ['Create group with current branch name']))
                .then((label) => {
                if (label == 'Input new group name') {
                    vscode.window.showInputBox({ title: 'Input a name for new group' }).then((input) => {
                        if (input) {
                            addNewGroupInConfig(input, previousGroups);
                        }
                    });
                }
                else if (label == 'Create group with current branch name') {
                    addNewGroupInConfig(branchName, previousGroups);
                }
            });
        });
    });
}
exports.addNewGroup = addNewGroup;
function addNewGroupInConfig(name, previousGroups) {
    if (previousGroups.indexOf(name) === -1) {
        configMgr_1.default.save('groups', previousGroups.concat([name]));
        configMgr_1.default.save('currentGroup', name);
    }
    else {
        vscode.window.showErrorMessage(`The group "${name}" already exists.`);
    }
}

//# sourceMappingURL=addNewGroup.js.map
