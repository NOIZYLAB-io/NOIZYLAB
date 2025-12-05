"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.JsonController = void 0;
const vscode_1 = require("vscode");
const configs_1 = require("../configs");
const helpers_1 = require("../helpers");
const normalize_helper_1 = require("../helpers/normalize.helper");
const providers_1 = require("../providers");
/**
 * Controls JSON preview and parsing actions for the VSCode JSON Flow extension.
 * Handles showing JSON previews, parsing, and error handling in the editor.
 */
class JsonController {
    context;
    config;
    // -----------------------------------------------------------------
    // Properties
    // -----------------------------------------------------------------
    /**
     * Delay in milliseconds for initializing the JSON preview panel (to ensure webview is ready).
     */
    _processingDelay = 1000;
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Creates a new JsonController.
     * @param context The VSCode extension context.
     * @param config The extension configuration instance.
     */
    constructor(context, config) {
        this.context = context;
        this.config = config;
    }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    /**
     * Displays a JSON preview for the given file URI in a webview panel.
     * Shows error messages for invalid files or parsing errors.
     * @param uri The file URI to preview.
     */
    async showPreview(uri, column = vscode_1.ViewColumn.One) {
        try {
            const document = await vscode_1.workspace.openTextDocument(uri.fsPath);
            const { graphLayoutOrientation } = this.config;
            // Get the language ID and file name
            const { languageId, fileName } = document;
            // Determine the file type, defaulting to 'json' if unsupported
            let fileType = languageId;
            if (!(0, helpers_1.isFileTypeSupported)(fileType)) {
                const baseName = fileName.split(/[\\\/]/).pop() ?? fileName;
                if (/^\.env(\..*)?$/i.test(baseName)) {
                    fileType = 'env';
                }
                else {
                    const fileExtension = fileName.split('.').pop();
                    fileType = (0, helpers_1.isFileTypeSupported)(fileExtension)
                        ? fileExtension
                        : 'json';
                }
            }
            // Parse JSON content
            const parsedJsonData = (0, helpers_1.parseJSONContent)(document.getText(), fileType);
            // Check if the JSON content is null
            if (parsedJsonData === null) {
                vscode_1.window.showErrorMessage(vscode_1.l10n.t('Could not parse JSON for preview'));
                return;
            }
            this.showJsonPanel(parsedJsonData, fileName, graphLayoutOrientation, uri.fsPath, column);
        }
        catch (error) {
            const errorMessage = error instanceof Error ? error.message : String(error);
            console.error('Error opening JSON preview:', errorMessage);
            vscode_1.window.showErrorMessage(vscode_1.l10n.t('Failed to open JSON preview: {0}', errorMessage));
        }
    }
    /**
     * Displays a JSON preview for the currently selected text in the active editor.
     * Shows error messages if there is no selection or if parsing fails.
     */
    showPartialPreview() {
        const { graphLayoutOrientation } = this.config;
        // Get the active text editor
        const editor = vscode_1.window.activeTextEditor;
        // Check if there is an active editor
        if (!editor) {
            vscode_1.window.showErrorMessage(vscode_1.l10n.t('No active editor!'));
            return;
        }
        // Check if there is a selection
        const selection = editor.selection;
        if (selection.isEmpty) {
            vscode_1.window.showErrorMessage(vscode_1.l10n.t('No selection!'));
            return;
        }
        // Get the selection range
        const selectionRange = new vscode_1.Range(selection.start.line, selection.start.character, selection.end.line, selection.end.character);
        // Get the language ID and file name
        const { languageId, fileName, uri } = editor.document;
        let fileType = languageId;
        let text = editor.document.getText(selectionRange);
        // Normalize JSON string and detect type
        const { normalized, detectedType } = (0, normalize_helper_1.normalizeToJsonString)(text, fileType);
        fileType = detectedType;
        text = normalized;
        if (!(0, helpers_1.isFileTypeSupported)(fileType)) {
            const baseName = fileName.split(/[\\\/]/).pop() ?? fileName;
            if (/^\.env(\..*)?$/i.test(baseName)) {
                fileType = 'env';
            }
            else {
                const fileExtension = fileName.split('.').pop();
                fileType = (0, helpers_1.isFileTypeSupported)(fileExtension) ? fileExtension : 'jsonc';
            }
        }
        // Parse JSON content
        const parsedJsonData = (0, helpers_1.parseJSONContent)(text, fileType);
        // Check if the JSON content is null
        if (parsedJsonData === null) {
            vscode_1.window.showErrorMessage(vscode_1.l10n.t('Could not parse selected JSON'));
            return;
        }
        this.showJsonPanel(parsedJsonData, fileName, graphLayoutOrientation, uri.fsPath);
    }
    /**
     * Fetches JSON data from a REST API and displays it in a webview panel.
     * Prompts the user for the API URL and handles errors during fetching.
     */
    async fetchJsonData() {
        const url = await vscode_1.window.showInputBox({
            prompt: 'Enter the REST API URL (GET)',
            placeHolder: 'https://api.example.com/data',
            validateInput: (text) => {
                if (!text.trim()) {
                    return 'URL cannot be empty';
                }
                try {
                    new URL(text);
                    return null;
                }
                catch {
                    return 'Invalid URL format';
                }
            },
        });
        if (!url) {
            vscode_1.window.showWarningMessage(vscode_1.l10n.t('Operation cancelled: No URL provided'));
            return;
        }
        await vscode_1.window.withProgress({
            location: vscode_1.ProgressLocation.Notification,
            title: 'Fetching JSON...',
            cancellable: false,
        }, async () => {
            const controller = new AbortController();
            const timeout = setTimeout(() => controller.abort(), 10_000);
            try {
                const response = await fetch(url, {
                    method: 'GET',
                    headers: { accept: 'application/json' },
                    signal: controller.signal,
                });
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status} ${response.statusText}`);
                }
                const contentType = response.headers.get('Content-Type') || '';
                const data = contentType.includes('application/json')
                    ? await response.json()
                    : await response.text();
                const parsedJsonData = (0, helpers_1.parseJSONContent)(typeof data === 'string' ? data : JSON.stringify(data), 'json');
                // Check if the JSON content is null
                if (parsedJsonData === null) {
                    vscode_1.window.showErrorMessage(vscode_1.l10n.t('Could not parse fetched JSON'));
                    return;
                }
                // Use a generic file name and orientation for the panel
                this.showJsonPanel(parsedJsonData, 'Fetched Data', this.config.graphLayoutOrientation);
            }
            catch (err) {
                const msg = err instanceof Error ? err.message : String(err);
                vscode_1.window.showErrorMessage(vscode_1.l10n.t('Error fetching JSON: {0}', [msg]));
            }
            finally {
                clearTimeout(timeout);
            }
        });
    }
    /**
     * Helper to create and update the JSON preview panel in a modular way.
     * @param data The parsed JSON data to display.
     * @param fileName The name of the file for panel title.
     * @param orientation The orientation for the graph layout.
     * @param path The file path (optional).
     */
    showJsonPanel(data, fileName, orientation, path, column = vscode_1.ViewColumn.One) {
        const displayName = fileName.split(/[\\/]/).pop() || configs_1.EXTENSION_DISPLAY_NAME;
        const panel = providers_1.JSONProvider.createPanel(this.context.extensionUri, column);
        panel.title = displayName;
        setTimeout(() => {
            panel.webview.postMessage({
                command: 'update',
                data,
                orientation,
                path,
                fileName,
            });
        }, this._processingDelay);
    }
}
exports.JsonController = JsonController;
//# sourceMappingURL=json.controller.js.map