"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AVProbeEditorProvider = void 0;
const path = require("path");
const vscode = require("vscode");
const avffmpeg_1 = require("./avffmpeg");
const dispose_1 = require("./dispose");
const util_1 = require("./util");
const extension_options_1 = require("./extension_options");
/**
 * Define the document (the data model) used for media files.
 */
class AVFileDocument extends dispose_1.Disposable {
    static async create(uri, backupId, delegate) {
        // If we have a backup, read that. Otherwise read the resource from the
        // workspace
        const dataFile = typeof backupId === 'string' ? vscode.Uri.parse(backupId) : uri;
        const fileData = new Uint8Array();
        // don't read file directly, use delegate
        return new AVFileDocument(uri, fileData, delegate);
    }
    constructor(uri, initialContent, delegate) {
        super();
        this._onDidDispose = this._register(new vscode.EventEmitter());
        /**
         * Fired when the document is disposed of.
         */
        this.onDidDispose = this._onDidDispose.event;
        this._onDidChangeDocument = this._register(new vscode.EventEmitter());
        /**
         * Fired to notify webviews that the document has changed.
         */
        this.onDidChangeContent = this._onDidChangeDocument.event;
        this._onDidChange = this._register(new vscode.EventEmitter());
        /**
         * Fired to tell VS Code that an edit has occurred in the document.
         *
         * This updates the document's dirty indicator.
         */
        this.onDidChange = this._onDidChange.event;
        this._uri = uri;
        this._documentData = initialContent;
        this._delegate = delegate;
    }
    get uri() {
        return this._uri;
    }
    get documentData() {
        return this._documentData;
    }
    /**
     * Called by VS Code when there are no more references to the document.
     *
     * This happens when all editors for it have been closed.
     */
    dispose() {
        this._onDidDispose.fire();
        super.dispose();
    }
}
class AVProbeEditorProvider {
    static register(context) {
        return vscode.window.registerCustomEditorProvider(AVProbeEditorProvider.viewType, new AVProbeEditorProvider(context), {
            // For this demo extension, we enable `retainContextWhenHidden` which
            // keeps the webview alive even when it is not visible. You should
            // avoid using this setting unless is absolutely required as it does
            // have memory overhead.
            webviewOptions: {
                retainContextWhenHidden: true,
            },
            supportsMultipleEditorsPerDocument: false,
        });
    }
    constructor(_context) {
        this._context = _context;
        /**
         * Tracks all known webviews
         */
        this.webviews = new WebviewCollection();
        this._requestId = 1;
        this._callbacks = new Map();
    }
    //#region CustomEditorProvider
    async openCustomDocument(uri, openContext, _token) {
        const document = await AVFileDocument.create(uri, openContext.backupId, {
            getFileData: async () => {
                const webviewsForDocument = Array.from(this.webviews.get(document.uri));
                if (!webviewsForDocument.length) {
                    throw new Error('Could not find webview to save for');
                }
                const panel = webviewsForDocument[0];
                const response = await this.postMessageWithResponse(panel, 'getFileData', {});
                return new Uint8Array(response);
            }
        });
        console.log('openCustomDocument: ' + uri.path);
        const listeners = [];
        listeners.push(document.onDidChange(e => {
            // Tell VS Code that the document has been edited by the use.
            /* 			this._onDidChangeCustomDocument.fire({
                                            document,
                                            ...e,
                                    });
             */
        }));
        document.onDidDispose(() => (0, dispose_1.disposeAll)(listeners));
        return document;
    }
    async resolveCustomEditor(document, webviewPanel, _token) {
        // Add the webview to our internal set of active webviews
        this.webviews.add(document.uri, webviewPanel);
        // Setup initial content for the webview
        webviewPanel.webview.options = {
            enableScripts: true,
            localResourceRoots: [
                vscode.Uri.file(path.join(this._context.extensionPath, 'vue-dist-avprobe', 'assets')),
            ],
        };
        webviewPanel.webview.html =
            this.getHtmlForWebview(webviewPanel.webview, webviewPanel, document);
        webviewPanel.webview.onDidReceiveMessage(e => this.onMessage(document, e, webviewPanel));
    }
    /**
     * Get the static HTML used for in our editor's webviews.
     */
    getHtmlForWebview(webview, webviewPanel, document) {
        // Local path to script and css for the webview
        const scriptUri = webview.asWebviewUri(vscode.Uri.joinPath(this._context.extensionUri, 'media', 'avprobe.js'));
        const scriptJsonViewUri = webview.asWebviewUri(vscode.Uri.joinPath(this._context.extensionUri, 'media', '3rd_party/json_view/jsonview.js'));
        const styleResetUri = webview.asWebviewUri(vscode.Uri.joinPath(this._context.extensionUri, 'media', 'reset.css'));
        const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._context.extensionUri, 'media', 'vscode.css'));
        const styleTableUri = webview.asWebviewUri(vscode.Uri.joinPath(this._context.extensionUri, 'media', 'table.css'));
        //const filePath = document.uri.path;
        const dependencyNameList = [
            'index.css',
            'index.js',
        ];
        const dependencyList = dependencyNameList.map((item) => webviewPanel.webview.asWebviewUri(vscode.Uri.file(path.join(this._context.extensionPath, 'vue-dist-avprobe', 'assets', item))));
        // Use a nonce to whitelist which scripts can be run
        const nonce = (0, util_1.getNonce)();
        // <link href="${styleResetUri}" rel="stylesheet" />
        // <link href="${styleVSCodeUri}" rel="stylesheet" />
        // <link href="${styleTableUri}" rel="stylesheet" />
        // <script nonce="${nonce}" src="${scriptJsonViewUri}"></script>
        return /* html */ `
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta name="viewport" content="width=device-width, initial-scale=1">
				<title>AVProbe extension</title>
				<style>
					body {
						padding: 20px;
					}
				</style>
				<script>
					const vscode = acquireVsCodeApi();
				</script>
				<link href="${styleVSCodeUri}" rel="stylesheet" />
				<script type="module" crossorigin src="${dependencyList[1]}"></script>
				<link rel="stylesheet" href="${dependencyList[0]}" />
			</head>
			<body>
				<div id="app"></div>
			</body>
		</html>
			`;
    }
    postMessageWithResponse(panel, type, body) {
        const requestId = this._requestId++;
        const p = new Promise(resolve => this._callbacks.set(requestId, resolve));
        panel.webview.postMessage({ type, requestId, body });
        return p;
    }
    postMessage(panel, type, body) {
        panel.webview.postMessage({ type, body });
    }
    onMessage(document, message, webviewPanel) {
        // get file size of the media file
        const filePath = document.uri.fsPath;
        switch (message.type) {
            case 'ready': {
                vscode.workspace.fs.stat(document.uri).then((stat) => {
                    const fileSize = stat.size;
                    console.log('fileSize: ', fileSize);
                    if (document.uri.scheme === 'untitled') {
                        this.postMessage(webviewPanel, 'init', {
                            untitled: true,
                            editable: true,
                            filePath: '',
                            fileSize: 0,
                        });
                    }
                    else {
                        const editable = vscode.workspace.fs.isWritableFileSystem(document.uri.scheme);
                        this.postMessage(webviewPanel, 'init', {
                            value: document.documentData,
                            editable,
                            filePath,
                            fileSize,
                        });
                    }
                });
                return;
            }
            case 'probe': {
                avffmpeg_1.FFProbe.probeMediaInfo(filePath)
                    .then((info) => {
                    console.log('probeMediaInfo: ', info);
                    this.postMessage(webviewPanel, 'media_info', JSON.stringify(info));
                })
                    .catch((err) => {
                    console.log('probeMediaInfo error: ', err);
                });
                return;
            }
            case 'show_packets': {
                const streamIndex = message.streamIndex;
                let args = '-v quiet -hide_banner -print_format json -show_packets';
                if (streamIndex !== undefined && Number(streamIndex) >= 0) {
                    args += ' -select_streams ' + streamIndex;
                }
                else {
                    // nop, select all streams for default
                }
                avffmpeg_1.FFProbe.probeMediaInfoWithCustomArgs(filePath, args)
                    .then((info) => {
                    console.log('probeMediaInfo: ', info);
                    this.postMessage(webviewPanel, 'packets', JSON.stringify(info));
                })
                    .catch((err) => {
                    console.log('probeMediaInfo error: ', err);
                });
                return;
            }
            case 'show_frame': {
                const framePtsString = message.framePts;
                avffmpeg_1.FFmpeg.extractFrameAsBmp(filePath, framePtsString).then((info) => {
                    console.log("extractFrameAsBmp: ", info);
                    this.postMessage(webviewPanel, 'bmp_frame', info);
                }).catch((error) => {
                    console.error("extractFrameAsBmp error: ", error);
                });
                return;
            }
            case "get_extension_options": {
                console.log("options: ", message);
                this.postMessage(webviewPanel, 'extension_options', {
                    "ffmpegPath": extension_options_1.ExtensionOptions.getFFmpegPath(),
                    "ffprobePath": extension_options_1.ExtensionOptions.getFFprobePath(),
                    "tablePageSize": extension_options_1.ExtensionOptions.getTablePageSize(),
                });
                return;
            }
        }
    }
}
exports.AVProbeEditorProvider = AVProbeEditorProvider;
AVProbeEditorProvider.viewType = 'xueshi.io.avprobe';
/**
 * Tracks all webviews.
 */
class WebviewCollection {
    constructor() {
        this._webviews = new Set();
    }
    /**
     * Get all known webviews for a given uri.
     */
    *get(uri) {
        const key = uri.toString();
        for (const entry of this._webviews) {
            if (entry.resource === key) {
                yield entry.webviewPanel;
            }
        }
    }
    /**
     * Add a new webview to the collection.
     */
    add(uri, webviewPanel) {
        const entry = { resource: uri.toString(), webviewPanel };
        this._webviews.add(entry);
        webviewPanel.onDidDispose(() => {
            this._webviews.delete(entry);
        });
    }
}
//# sourceMappingURL=avprobeEditor.js.map