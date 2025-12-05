"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FilesController = void 0;
const fastGlob = require("fast-glob");
const fs_1 = require("fs");
const ignore_1 = require("ignore");
const path_1 = require("path");
const vscode_1 = require("vscode");
/**
 * The FilesController class.
 *
 * @class
 * @classdesc The class that represents the list files controller.
 * @export
 * @public
 * @property {ExtensionConfig} config - The configuration object
 * @example
 * const controller = new FilesController(config);
 */
class FilesController {
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Constructor for the FilesController class
     *
     * @constructor
     * @param {ExtensionConfig} config - The configuration object
     * @public
     * @memberof FilesController
     */
    constructor(config) {
        this.config = config;
    }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    // Public methods
    /**
     * The createBarrel method.
     *
     * @function createBarrel
     * @param {Uri} [folderPath] - The path to the folder
     * @public
     * @async
     * @memberof FilesController
     * @example
     * controller.createBarrel();
     *
     * @returns {Promise<void>} - The promise with no return value
     */
    async createBarrel(folderPath) {
        const { defaultLanguage, configuredDefaultFilename } = this.config;
        // If the folder is not valid, return
        if (!folderPath) {
            const message = vscode_1.l10n.t('The folder is not valid!');
            vscode_1.window.showErrorMessage(message);
            return;
        }
        const workspaceFolder = vscode_1.workspace.getWorkspaceFolder(folderPath);
        // If the folder is not in the workspace, return
        if (!workspaceFolder) {
            const message = vscode_1.l10n.t('The folder is not in the workspace!');
            vscode_1.window.showErrorMessage(message);
            return;
        }
        const content = await this.getContent(folderPath.fsPath);
        const fileExtension = defaultLanguage === 'TypeScript' ? 'ts' : 'js';
        const outputFileName = `${configuredDefaultFilename}.${fileExtension}`;
        if (content) {
            this.saveFile(folderPath.fsPath, outputFileName, content);
        }
    }
    /**
     * The updateBarrelInFolder method.
     *
     * @function updateBarrelInFolder
     * @param {Uri} [folderPath] - The path to the folder
     * @public
     * @async
     * @memberof FilesController
     * @example
     * controller.updateBarrelInFolder();
     *
     * @returns {Promise<void>} - The promise with no return value
     */
    async updateBarrelInFolder(folderPath) {
        const { defaultLanguage, configuredDefaultFilename } = this.config;
        // If the folder is not valid, return
        if (!folderPath) {
            const message = vscode_1.l10n.t('The folder is not valid!');
            vscode_1.window.showErrorMessage(message);
            return;
        }
        const workspaceFolder = vscode_1.workspace.getWorkspaceFolder(folderPath);
        // If the folder is not in the workspace, return
        if (!workspaceFolder) {
            const message = vscode_1.l10n.t('The folder is not in the workspace!');
            vscode_1.window.showErrorMessage(message);
            return;
        }
        const fileExtension = defaultLanguage === 'TypeScript' ? 'ts' : 'js';
        const outputFileName = `${configuredDefaultFilename}.${fileExtension}`;
        const filename = (0, path_1.join)(folderPath.fsPath, outputFileName);
        if (!(0, fs_1.existsSync)(filename)) {
            const message = vscode_1.l10n.t('The file does not exist!');
            vscode_1.window.showErrorMessage(message);
            return;
        }
        const openPath = vscode_1.Uri.file(filename);
        this.updateBarrel(openPath);
    }
    /**
     * The updateBarrel method.
     *
     * @function updateBarrel
     * @param {Uri} [folderPath] - The path to the folder
     * @public
     * @async
     * @memberof FilesController
     * @example
     * controller.updateBarrel();
     *
     * @returns {Promise<void>} - The promise with no return value
     */
    async updateBarrel(folderPath) {
        // If the folder is not valid, return
        if (!folderPath) {
            const message = vscode_1.l10n.t('The folder is not valid!');
            vscode_1.window.showErrorMessage(message);
            return;
        }
        const workspaceFolder = vscode_1.workspace.getWorkspaceFolder(folderPath);
        // If the folder is not in the workspace, return
        if (!workspaceFolder) {
            const message = vscode_1.l10n.t('The folder is not in the workspace!');
            vscode_1.window.showErrorMessage(message);
            return;
        }
        const baseDir = (0, path_1.dirname)(folderPath.fsPath);
        const content = await this.getContent(baseDir);
        if (content) {
            const document = await vscode_1.workspace.openTextDocument(folderPath);
            const edit = new vscode_1.WorkspaceEdit();
            const start = new vscode_1.Position(0, 0);
            const end = new vscode_1.Position(document.lineCount, 0);
            const range = new vscode_1.Range(start, end);
            edit.replace(document.uri, range, content);
            await vscode_1.workspace.applyEdit(edit);
            await vscode_1.commands.executeCommand('workbench.action.files.saveAll');
            await vscode_1.window.showTextDocument(document);
            const message = vscode_1.l10n.t('File successfully updated!');
            vscode_1.window.showInformationMessage(message);
        }
    }
    // Private methods
    /**
     * The getContent method.
     *
     * @function getContent
     * @param {string} folderPath - The folder path
     * @private
     * @async
     * @memberof FilesController
     * @example
     * controller.getContent();
     *
     * @returns {Promise<string | undefined>} - The promise with the content
     */
    async getContent(folderPath) {
        // Get the configuration values
        const { disableRecursiveBarrelling, includeExtensionOnExport, ignoreFilePathPatternOnExport, maxSearchRecursionDepth, supportsHiddenFiles, preserveGitignoreSettings, useSingleQuotes, excludeSemiColonAtEndOfLine, keepExtensionOnExport, endOfLine, detectExportsInFiles, useNamedExports, exportDefaultFilename, headerCommentTemplate, insertFinalNewline, } = this.config;
        const quote = useSingleQuotes ? "'" : '"';
        const semi = excludeSemiColonAtEndOfLine ? '' : ';';
        const newline = endOfLine === 'crlf' ? '\r\n' : '\n';
        const include = includeExtensionOnExport.length === 1
            ? `**/*.${includeExtensionOnExport[0]}`
            : `**/*.{${includeExtensionOnExport.join(',')}}`;
        // Retrieve matching files
        const files = await this.findFiles(folderPath, [include], ignoreFilePathPatternOnExport, disableRecursiveBarrelling, maxSearchRecursionDepth, supportsHiddenFiles, preserveGitignoreSettings);
        // If no files are found, return
        if (files.length === 0) {
            const relativePath = vscode_1.workspace.asRelativePath(folderPath);
            const allFilesInFolder = await vscode_1.workspace.findFiles(`${relativePath}/**/*`);
            if (allFilesInFolder.length === 0) {
                const message = vscode_1.l10n.t('The {0} folder is empty!', [relativePath]);
                vscode_1.window.showWarningMessage(message);
            }
            else {
                const message = vscode_1.l10n.t('No files found matching the specified patterns in the {0} folder! Please check the include and exclude files in the settings', [relativePath]);
                vscode_1.window.showWarningMessage(message);
            }
            return;
        }
        let content = '';
        if (headerCommentTemplate.length > 0) {
            content += headerCommentTemplate.join(newline) + newline + newline;
        }
        const exports = [];
        for (const file of files) {
            let relativePath = (0, path_1.relative)(folderPath, file.fsPath).replace(/\\/g, '/');
            if (!keepExtensionOnExport) {
                relativePath = relativePath.replace(/\.[^/.]+$/, '');
            }
            if (detectExportsInFiles) {
                // Get formatted filename
                const baseName = (0, path_1.basename)(file.path).replace(/\.[^/.]+$/, '');
                const formattedFileName = this.formatFileName(baseName, exportDefaultFilename);
                const document = await vscode_1.workspace.openTextDocument(file.path);
                const text = document.getText();
                // Check if the file has a default export
                const defaultExportRegex = /\bexport\s*(?:async|function|const|let|var)?\s*default\s+/g;
                // Check if the file has exported members
                const exportedMembersRegex = /\bexport\s*\{\s*[^}]*\s*\}/g;
                // Check if the file has a named export
                const namedExportRegex = /\bexport\s+(?:(async|abstract|declare|const|let|var)\s*)?(enum|function|class|type|interface|const|let|var)\s+(\w+)\b/g;
                if (text.match(defaultExportRegex)) {
                    exports.push(`export { default as ${formattedFileName} } from ${quote}./${relativePath}${quote}${semi}`);
                    continue;
                }
                if (text.match(exportedMembersRegex)) {
                    if (useNamedExports) {
                        const fileMembers = [];
                        for (const [, members] of text.matchAll(exportedMembersRegex)) {
                            for (const member of members.split(',')) {
                                const name = member.trim();
                                fileMembers.push(name);
                            }
                        }
                        if (fileMembers.length > 0) {
                            const exportName = fileMembers.join(', ');
                            exports.push(`export { ${exportName} } from ${quote}./${relativePath}${quote}${semi}`);
                        }
                    }
                    else {
                        exports.push(`export * as ${formattedFileName} from ${quote}./${relativePath}${quote}${semi}`);
                    }
                    continue;
                }
                if (text.match(namedExportRegex)) {
                    if (useNamedExports) {
                        const fileTypeExports = [];
                        const fileExports = [];
                        for (const [, , type, name] of text.matchAll(namedExportRegex)) {
                            (type === 'interface' || type === 'type'
                                ? fileTypeExports
                                : fileExports).push(name);
                        }
                        if (fileTypeExports.length > 0 || fileExports.length > 0) {
                            if (!fileExports.length) {
                                // Only type exports exist
                                const typeExports = fileTypeExports.join(', ');
                                exports.push(`export type { ${typeExports} } from ${quote}./${relativePath}${quote}${semi}`);
                            }
                            else if (!fileTypeExports.length) {
                                // Only value exports exist
                                const valueExports = fileExports.join(', ');
                                exports.push(`export { ${valueExports} } from ${quote}./${relativePath}${quote}${semi}`);
                            }
                            else {
                                // Both type and value exports exist
                                const combinedExports = [
                                    ...fileTypeExports.map((name) => `type ${name}`),
                                    ...fileExports,
                                ].join(', ');
                                exports.push(`export { ${combinedExports} } from ${quote}./${relativePath}${quote}${semi}`);
                            }
                        }
                    }
                    else {
                        exports.push(`export * as ${formattedFileName} from ${quote}./${relativePath}${quote}${semi}`);
                    }
                    continue;
                }
            }
            else {
                exports.push(`export * from ${quote}./${relativePath}${quote}${semi}`);
            }
        }
        content += exports.join(newline);
        // Add a final newline
        if (insertFinalNewline) {
            content += newline;
        }
        return content;
    }
    /**
     * The formatFileName method.
     *
     * @function formatFileName
     * @param {string} fileName - The file name
     * @param {string} style - The style
     * @private
     * @memberof FilesController
     * @example
     * controller.formatFileName('fileName', 'style');
     *
     * @returns {string} - The formatted file name
     */
    formatFileName(fileName, style) {
        switch (style) {
            case 'camelCase':
                fileName = fileName.replace(/[-.](.)/g, (_, c) => c.toUpperCase());
                break;
            case 'pascalCase':
                fileName = fileName
                    .replace(/[-.]\w/g, (match) => match.charAt(1).toUpperCase())
                    .replace(/^./, (match) => match.toUpperCase());
                break;
            case 'kebabCase':
                fileName = fileName.replace(/[-.](.)/g, (_, c) => `-${c}`);
                break;
            case 'snakeCase':
                fileName = fileName.replace(/[-.](.)/g, (_, c) => `_${c}`);
                break;
        }
        return fileName;
    }
    /**
     * The saveFile method.
     *
     * @function saveFile
     * @param {string} path - The path
     * @param {string} filename - The filename
     * @param {string} data - The data
     * @private
     * @async
     * @memberof FilesController
     * @example
     * controller.saveFile('path', 'filename', 'data');
     *
     * @returns {Promise<void>} - The promise with no return value
     */
    async saveFile(path, filename, data) {
        const file = (0, path_1.join)(path, filename);
        if (!(0, fs_1.existsSync)((0, path_1.dirname)(file))) {
            (0, fs_1.mkdirSync)((0, path_1.dirname)(file), { recursive: true });
        }
        (0, fs_1.access)(file, (err) => {
            if (err) {
                (0, fs_1.open)(file, 'w+', (err, fd) => {
                    if (err) {
                        const message = vscode_1.l10n.t('The file has not been created!');
                        vscode_1.window.showErrorMessage(message);
                        return;
                    }
                    (0, fs_1.writeFile)(fd, data, 'utf8', (err) => {
                        if (err) {
                            const message = vscode_1.l10n.t('The file has not been created!');
                            vscode_1.window.showErrorMessage(message);
                            return;
                        }
                        const openPath = vscode_1.Uri.file(file);
                        vscode_1.workspace.openTextDocument(openPath).then(async (filename) => {
                            await vscode_1.commands.executeCommand('workbench.action.files.saveAll');
                            await vscode_1.window.showTextDocument(filename);
                        });
                    });
                });
                const message = vscode_1.l10n.t('File created successfully!');
                vscode_1.window.showInformationMessage(message);
            }
            else {
                const message = vscode_1.l10n.t('The file name already exists!');
                vscode_1.window.showWarningMessage(message);
            }
        });
    }
    /**
     * The findFiles method.
     *
     * @function findFiles
     * @param {string} baseDir - The base directory
     * @param {string[]} includeFilePatterns - The include pattern
     * @param {string[]} excludedPatterns - The exclude pattern
     * @param {boolean} includeOnlyFiles - The flag to include only files
     * @param {boolean} disableRecursive - The flag to disable recursive searching
     * @param {number} deep - The recursion depth
     * @param {boolean} includeDotfiles - The flag to include dotfiles
     * @param {boolean} enableGitignoreDetection - The flag to enable .gitignore detection
     * @private
     * @async
     * @memberof FilesController
     * @example
     * controller.findFiles('baseDir', ['include'], ['exclude']);
     *
     * @returns {Promise<Uri[]>} - The promise with the files
     */
    async findFiles(baseDir, includeFilePatterns, excludedPatterns, disableRecursive = false, deep = 0, includeDotfiles = false, enableGitignoreDetection = false) {
        // If we need to respect .gitignore, we need to load it
        let gitignore;
        if (enableGitignoreDetection) {
            const gitignorePath = (0, path_1.join)(baseDir, '.gitignore');
            // Load .gitignore if it exists
            if ((0, fs_1.existsSync)(gitignorePath)) {
                gitignore = (0, ignore_1.default)().add((0, fs_1.readFileSync)(gitignorePath, 'utf8'));
            }
        }
        // Configure fast-glob options
        const options = {
            cwd: baseDir, // Set the base directory for searching
            absolute: true, // Return absolute paths for files found
            onlyFiles: true, // Match only files, not directories
            dot: includeDotfiles, // Include the files and directories starting with a dot
            deep: disableRecursive ? 1 : deep === 0 ? undefined : deep, // Set the recursion depth
            ignore: excludedPatterns, // Set the patterns to ignore files and directories
        };
        try {
            // Use fast-glob to find matching files
            let foundFilePaths = await fastGlob(includeFilePatterns, options);
            if (gitignore) {
                // Filter out files that are ignored by .gitignore
                foundFilePaths = foundFilePaths.filter((filePath) => {
                    const relativePath = (0, path_1.relative)(baseDir, filePath); // Convert to relative paths
                    return !gitignore.ignores(relativePath);
                });
            }
            // Convert file paths to VS Code Uri objects
            return foundFilePaths.sort().map((filePath) => vscode_1.Uri.file(filePath));
        }
        catch (error) {
            const message = vscode_1.l10n.t('Error while finding files: {0}', [error]);
            vscode_1.window.showErrorMessage(message);
            return [];
        }
    }
}
exports.FilesController = FilesController;
//# sourceMappingURL=files.controller.js.map