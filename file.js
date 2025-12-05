"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getParentFolderPathForFolder = exports.awaitFileExistence = void 0;
const vscode = require("vscode");
const fs_1 = require("fs");
const path_1 = require("path");
function awaitFileExistence(path, timeout) {
    return new Promise(resolve => {
        let timer = setTimeout(() => {
            if (timeout > 0) {
                watcher.dispose();
                resolve(false);
            }
        }, timeout);
        if ((0, fs_1.existsSync)(path)) {
            clearTimeout(timer);
            resolve(true);
        }
        const watcher = vscode.workspace.createFileSystemWatcher(path);
        watcher.onDidCreate(e => {
            callResolve();
        });
        watcher.onDidChange(e => {
            callResolve();
        });
        function callResolve() {
            watcher.dispose();
            clearTimeout(timer);
            resolve(true);
        }
    });
}
exports.awaitFileExistence = awaitFileExistence;
function getParentFolderPathForFolder(path) {
    path = removeTrailingSlahesFromPath(path);
    return removeTrailingSlahesFromPath(path.substring(0, path.length - (0, path_1.basename)(path).length));
}
exports.getParentFolderPathForFolder = getParentFolderPathForFolder;
function removeTrailingSlahesFromPath(path) {
    return path.replace(/\/*$/, '').replace(/\\*$/, ''); //remove trailing forward and back slashes from the path
}
//# sourceMappingURL=file.js.map