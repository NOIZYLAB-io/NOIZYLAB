"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.createHEADFileWatcherForTestWorkspaceFolder = exports.getGitFolderPathForFolder = void 0;
const vscode = require("vscode");
const fs_1 = require("fs");
const path_1 = require("path");
const file_1 = require("./file");
const alFileHelper_1 = require("./alFileHelper");
const testController_1 = require("./testController");
function getGitFolderPathForFolder(path) {
    return getGitFolderPathForFolder2(path, 0);
}
exports.getGitFolderPathForFolder = getGitFolderPathForFolder;
function createHEADFileWatcherForTestWorkspaceFolder() {
    const testFolderPath = (0, alFileHelper_1.getTestFolderPath)();
    if (testFolderPath) {
        const gitFolder = getGitFolderPathForFolder(testFolderPath);
        if (gitFolder) {
            vscode.workspace.createFileSystemWatcher((0, path_1.join)(gitFolder, 'HEAD')).onDidChange(e => {
                (0, testController_1.discoverTests)();
            });
        }
    }
}
exports.createHEADFileWatcherForTestWorkspaceFolder = createHEADFileWatcherForTestWorkspaceFolder;
function getGitFolderPathForFolder2(path, depth) {
    while (!folderHasGitRepo(path)) {
        const currPath = path;
        path = (0, file_1.getParentFolderPathForFolder)(currPath);
        if (depth == 2) {
            return undefined;
        }
        if (currPath === path) {
            return undefined;
        }
        return getGitFolderPathForFolder2(path, depth + 1);
    }
    return (0, path_1.join)(path, '.git');
}
function folderHasGitRepo(path) {
    return (0, fs_1.existsSync)((0, path_1.join)(path, '.git'));
}
//# sourceMappingURL=git.js.map