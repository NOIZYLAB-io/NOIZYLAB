"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ListFilesController = void 0;
const vscode_1 = require("vscode");
const configs_1 = require("../configs");
const helpers_1 = require("../helpers");
const models_1 = require("../models");
/**
 * Controller for listing and navigating Angular files in the workspace.
 * ListFilesController manages navigation and display of files and folders in the workspace.
 * All public methods and properties are documented with JSDoc for clarity and maintainability.
 *
 * @class ListFilesController
 * @module controllers/list-files.controller
 */
class ListFilesController {
    // -----------------------------------------------------------------
    // Properties
    // -----------------------------------------------------------------
    // Public properties
    /**
     * The static config property.
     *
     * @static
     * @property
     * @public
     * @type {Config}
     * @memberof ListFilesController
     */
    static config;
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Constructor for the ListFilesController class
     *
     * @constructor
     * @param {Config} config - The configuration object
     * @public
     * @memberof ListFilesController
     */
    constructor(config) {
        ListFilesController.config = config;
    }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    // Public methods
    /**
     * Returns a list of files in the workspace as NodeModel objects.
     * @param maxResults Maximum number of results to return.
     * @returns Promise resolved with an array of NodeModel or void if none found.
     */
    static async getFiles() {
        if (!vscode_1.workspace.workspaceFolders) {
            vscode_1.window.showErrorMessage(vscode_1.l10n.t('Operation cancelled!'));
            return;
        }
        const folders = vscode_1.workspace.workspaceFolders.map((folder) => folder.uri.fsPath);
        const allFiles = [];
        const { include, exclude } = this.config;
        const includePatterns = include
            .map((pattern) => pattern?.trim())
            .filter((pattern) => !!pattern && pattern.length > 0)
            .map((pattern) => {
            const hasGlob = /[\*?\[\]\{\}\(\)!]/.test(pattern);
            const hasSep = /[\\/]/.test(pattern);
            if (hasGlob || hasSep) {
                return pattern;
            }
            const ext = pattern.startsWith('.') ? pattern.slice(1) : pattern;
            return `**/*.${ext}`;
        });
        for (const folder of folders) {
            const result = await (0, helpers_1.findFiles)({
                baseDirectoryPath: folder,
                includeFilePatterns: includePatterns,
                excludedPatterns: exclude,
                includeDotfiles: false,
                enableGitignoreDetection: true,
            });
            allFiles.push(...result);
        }
        if (allFiles.length === 0) {
            return;
        }
        const uniqueFiles = Array.from(new Set(allFiles.map((f) => f.fsPath))).map((path) => vscode_1.Uri.file(path));
        uniqueFiles.sort((a, b) => a.path.localeCompare(b.path));
        const nodes = uniqueFiles.map((file) => {
            const path = vscode_1.workspace.asRelativePath(file);
            const filename = path.split('/').pop();
            let label = filename ?? vscode_1.l10n.t('Untitled');
            if (filename && this.config.showPath) {
                const folder = path.split('/').slice(0, -1).join('/');
                label += folder ? vscode_1.l10n.t(' ({0})', folder) : ` ${vscode_1.l10n.t('(root)')}`;
            }
            const node = new models_1.NodeModel(label, new vscode_1.ThemeIcon('file'), {
                command: `${configs_1.EXTENSION_ID}.list.openFile`,
                title: vscode_1.l10n.t('Open File'),
                arguments: [file],
            }, file, file.fsPath);
            node.tooltip = file.fsPath;
            return node;
        });
        return nodes;
    }
    /**
     * Opens the specified file in the VSCode editor.
     * @param uri File Uri to open.
     */
    openFile(uri) {
        vscode_1.workspace.openTextDocument(uri).then((filename) => {
            vscode_1.window.showTextDocument(filename);
        });
    }
    /**
     * Opens the specified file and moves the cursor to the given line.
     * @param uri File Uri to open.
     * @param line Line number to navigate to.
     */
    gotoLine(uri, line) {
        vscode_1.workspace.openTextDocument(uri).then((document) => {
            vscode_1.window.showTextDocument(document).then((editor) => {
                const pos = new vscode_1.Position(line, 0);
                editor.revealRange(new vscode_1.Range(pos, pos), vscode_1.TextEditorRevealType.InCenterIfOutsideViewport);
                editor.selection = new vscode_1.Selection(pos, pos);
            });
        });
    }
}
exports.ListFilesController = ListFilesController;
//# sourceMappingURL=list-files.controller.js.map