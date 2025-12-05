"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CatCodingPanel = void 0;
const vscode = require("vscode");
const path = require("path");
const avffmpeg_1 = require("./avffmpeg");
/**
 * Manages cat coding webview panels
 */
class CatCodingPanel {
    static createOrShow(context) {
        const extensionUri = context.extensionUri;
        const column = vscode.window.activeTextEditor
            ? vscode.window.activeTextEditor.viewColumn
            : undefined;
        // If we already have a panel, show it.
        if (CatCodingPanel.currentPanel) {
            CatCodingPanel.currentPanel._panel.reveal(column);
            return;
        }
        // Otherwise, create a new panel.
        const panel = vscode.window.createWebviewPanel(CatCodingPanel.viewType, 'Cat Coding', column || vscode.ViewColumn.One, {});
        CatCodingPanel.currentPanel = new CatCodingPanel(context, panel, extensionUri);
    }
    // public static revive(panel: vscode.WebviewPanel, extensionUri: vscode.Uri) {
    // 	CatCodingPanel.currentPanel = new CatCodingPanel(panel, extensionUri);
    // }
    constructor(context, panel, extensionUri) {
        this._disposables = [];
        this._context = context;
        this._panel = panel;
        this._extensionUri = extensionUri;
        // Setup initial content for the webview
        panel.webview.options = {
            enableScripts: true,
            localResourceRoots: [
                vscode.Uri.file(path.join(this._context.extensionPath, 'vue-dist-codec', 'assets')),
            ],
        };
        this._panel.webview.onDidReceiveMessage(e => this.onMessage(e, panel));
        this._panel.title = "Codecs supported by FFmpeg";
        this._panel.webview.html = this._getHtmlForWebview(this._panel.webview, panel);
        // Listen for when the panel is disposed
        // This happens when the user closes the panel or when the panel is closed programmatically
        this._panel.onDidDispose(() => this.dispose(), null, this._disposables);
        // // Update the content based on view changes
        // this._panel.onDidChangeViewState(
        // 	e => {
        // 		if (this._panel.visible) {
        // 			// this._update();
        // 		}
        // 	},
        // 	null,
        // 	this._disposables
        // );
        // Handle messages from the webview
        // this._panel.webview.onDidReceiveMessage(
        // 	message => {
        // 		switch (message.command) {
        // 			case 'alert':
        // 				vscode.window.showErrorMessage(message.text);
        // 				return;
        // 		}
        // 	},
        // 	null,
        // 	this._disposables
        // );
    }
    dispose() {
        CatCodingPanel.currentPanel = undefined;
        // Clean up our resources
        this._panel.dispose();
        while (this._disposables.length) {
            const x = this._disposables.pop();
            if (x) {
                x.dispose();
            }
        }
    }
    _getHtmlForWebview(webview, webviewPanel) {
        const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._context.extensionUri, 'media', 'vscode.css'));
        const dependencyNameList = [
            'index.css',
            'index.js',
        ];
        const dependencyList = dependencyNameList.map((item) => webviewPanel.webview.asWebviewUri(vscode.Uri.file(path.join(this._context.extensionPath, 'vue-dist-codec', 'assets', item))));
        // Use a nonce to only allow specific scripts to be run
        const nonce = getNonce();
        return /* html */ `
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta name="viewport" content="width=device-width, initial-scale=1">
				<title>AVProbe extension</title>
				<style>
					body {
						padding: 8px;
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
    postMessage(panel, type, body) {
        panel.webview.postMessage({ type, body });
    }
    onMessage(message, webviewPanel) {
        console.log('codec onMessage: ', message);
        switch (message.type) {
            case 'ready': {
                this.postMessage(webviewPanel, 'init', null);
                return;
            }
            case 'show_decoders': {
                avffmpeg_1.FFmpeg.execFFmpegCmd(['-decoders'])
                    .then((info) => {
                    console.log('showDecodersInfo: ', info);
                    this.postMessage(webviewPanel, 'show_decoders', info);
                })
                    .catch((err) => {
                    console.log('showDecodersInfo error: ', err);
                });
                return;
            }
            case 'show_encoders': {
                avffmpeg_1.FFmpeg.execFFmpegCmd(['-encoders'])
                    .then((info) => {
                    console.log('showEncodersInfo: ', info);
                    this.postMessage(webviewPanel, 'show_encoders', info);
                })
                    .catch((err) => {
                    console.log('showEncodersInfo error: ', err);
                });
                return;
            }
            case 'show_decoder_info': {
                const decoderName = message.decoderName;
                if (decoderName) {
                    avffmpeg_1.FFmpeg.execFFmpegCmd(['-help', 'decoder', decoderName])
                        .then((info) => {
                        console.log('showDecoderInfo: ', info);
                        this.postMessage(webviewPanel, 'show_decoder_info', info);
                    })
                        .catch((err) => {
                        console.log('showDecoderInfo error: ', err);
                    });
                }
                return;
            }
        }
    }
}
exports.CatCodingPanel = CatCodingPanel;
CatCodingPanel.viewType = 'catCoding';
function getNonce() {
    let text = '';
    const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 32; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}
//# sourceMappingURL=codec.js.map