"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.saveFile = void 0;
const path_1 = require("path");
const vscode_1 = require("vscode");
const find_files_helper_1 = require("./find-files.helper");
/**
 * Writes data to the file specified in the path. If the file does not exist then the function will create it.
 *
 * @param {string} directoryPath - Relative path (from the workspace folder) where the file will be created
 * @param {string} filename - Name of the file
 * @param {string} fileContent - Data to write to the file
 * @example
 * await saveFile('src', 'file.ts', 'console.log("Hello World")');
 *
 * @returns {Promise<void>} - Confirmation of the write operation
 */
const saveFile = async (directoryPath, filename, fileContent) => {
    // Ensure there is an open workspace
    if (!vscode_1.workspace.workspaceFolders || vscode_1.workspace.workspaceFolders.length === 0) {
        const message = vscode_1.l10n.t('No workspace folders are open. Please open a workspace folder to use this extension');
        await vscode_1.window.showErrorMessage(message);
        return;
    }
    // Validate and normalize the provided directory path to avoid escaping the workspace root
    const normalizedRelativeDirectoryPath = (0, path_1.normalize)(directoryPath || '.');
    if ((0, path_1.isAbsolute)(normalizedRelativeDirectoryPath) ||
        normalizedRelativeDirectoryPath.split(/[\\\/]/).includes('..')) {
        await vscode_1.window.showErrorMessage(vscode_1.l10n.t('Invalid directory path'));
        return;
    }
    // Split into path segments in a cross-platform way and remove empty/'./' segments
    const relativePathSegments = normalizedRelativeDirectoryPath
        .split(/[\\/]+/)
        .filter((s) => s !== '' && s !== '.');
    // Disallow parent-directory traversals
    if (relativePathSegments.includes('..')) {
        await vscode_1.window.showErrorMessage(vscode_1.l10n.t('Invalid directory path'));
        return;
    }
    // Determine base folder (first workspace folder)
    const workspaceRootUri = vscode_1.workspace.workspaceFolders?.[0]?.uri;
    if (!workspaceRootUri) {
        await vscode_1.window.showErrorMessage(vscode_1.l10n.t('No workspace folders are open. Please open a workspace folder to use this extension'));
        return;
    }
    // Build directory and file URIs using segments to ensure proper joining on all platforms
    const targetDirectoryUri = relativePathSegments.length > 0
        ? vscode_1.Uri.joinPath(workspaceRootUri, ...relativePathSegments)
        : workspaceRootUri;
    const targetFileUri = vscode_1.Uri.joinPath(targetDirectoryUri, filename);
    // Track success to show notification after progress completes
    let createdFileFsPath;
    try {
        await vscode_1.window.withProgress({
            location: vscode_1.ProgressLocation.Notification,
            title: vscode_1.l10n.t('Creating file: {0}', filename),
            cancellable: true,
        }, async (_progress, cancellationToken) => {
            try {
                // If the user cancelled immediately, stop.
                if (cancellationToken.isCancellationRequested) {
                    return;
                }
                // Create the directory only if it's not the workspace root (no-op if it already exists).
                if (targetDirectoryUri.toString() !== workspaceRootUri.toString()) {
                    await vscode_1.workspace.fs.createDirectory(targetDirectoryUri);
                }
                // Check if file exists. Treat FileSystemError from stat as "not exists".
                let targetFileExists = false;
                try {
                    await vscode_1.workspace.fs.stat(targetFileUri);
                    targetFileExists = true;
                }
                catch (error) {
                    if (error instanceof vscode_1.FileSystemError) {
                        targetFileExists = false;
                    }
                    else {
                        // Unknown error - rethrow so outer catch can show it
                        throw error;
                    }
                }
                if (cancellationToken.isCancellationRequested) {
                    return;
                }
                // If file exists, offer to open it instead of overwriting
                if (targetFileExists) {
                    const openLabel = vscode_1.l10n.t('Open File');
                    const choice = await vscode_1.window.showWarningMessage(vscode_1.l10n.t('File already exists: {0}', filename), openLabel);
                    if (choice === openLabel) {
                        const textDocument = await vscode_1.workspace.openTextDocument(targetFileUri);
                        await vscode_1.window.showTextDocument(textDocument);
                    }
                    return;
                }
                // Write file contents (TextEncoder -> Uint8Array)
                const encodedFileContent = new TextEncoder().encode(fileContent);
                await vscode_1.workspace.fs.writeFile(targetFileUri, encodedFileContent);
                if (cancellationToken.isCancellationRequested) {
                    return;
                }
                // Open the created file in the editor
                const createdTextDocument = await vscode_1.workspace.openTextDocument(targetFileUri);
                await vscode_1.window.showTextDocument(createdTextDocument);
                // Mark success; show notification after progress resolves
                createdFileFsPath = targetFileUri.fsPath;
                // Clear the file cache since a new file was created
                (0, find_files_helper_1.clearCache)();
            }
            catch (error) {
                // Show a helpful error message including the underlying error if available
                await vscode_1.window.showErrorMessage(vscode_1.l10n.t('Error creating file: {0}. Please check the path and try again', error?.message ?? String(error)));
            }
        });
        // Show success notification after progress dialog closes
        if (createdFileFsPath) {
            await vscode_1.window.showInformationMessage(vscode_1.l10n.t('File created successfully: {0}', createdFileFsPath));
        }
    }
    catch (error) {
        // Catch failures from withProgress or other unexpected issues
        await vscode_1.window.showErrorMessage(vscode_1.l10n.t('Error creating file: {0}. Please check the path and try again', error?.message ?? String(error)));
    }
};
exports.saveFile = saveFile;
//# sourceMappingURL=save-file.helper.js.map