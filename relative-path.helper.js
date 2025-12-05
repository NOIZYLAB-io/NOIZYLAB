"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.relativePath = void 0;
const fs_1 = require("fs");
const path_1 = require("path");
const vscode_1 = require("vscode");
/**
 * Generates a relative path from the workspace root to the specified path.
 * If the given path is a file, it will be resolved to the parent folder.
 * If showPath is disabled, it will return the relative path from the workspace root using
 * {@linkcode Workspace.asRelativePath}.
 * @param {Uri} [path] - The path to generate the relative path from.
 * @returns {string} The relative path.
 * @memberof TerminalController
 */
const relativePath = (path, isRootContext) => {
    // Check if the path is a file
    if (path && (0, fs_1.statSync)(path.fsPath).isFile()) {
        path = vscode_1.Uri.file((0, path_1.resolve)(path.fsPath, '..'));
    }
    let folderPath = '';
    if (isRootContext) {
        // First workspace is the root => https://code.visualstudio.com/api/references/vscode-api#workspace
        const wsFolder = vscode_1.workspace.workspaceFolders
            ? vscode_1.workspace.workspaceFolders[0]
            : '';
        if (wsFolder && path) {
            folderPath = (0, path_1.relative)(wsFolder.uri.fsPath, path.fsPath);
        }
    }
    else {
        folderPath = path ? vscode_1.workspace.asRelativePath(path.fsPath, false) : '';
    }
    return folderPath;
};
exports.relativePath = relativePath;
//# sourceMappingURL=relative-path.helper.js.map