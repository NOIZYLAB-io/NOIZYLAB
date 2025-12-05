//
//     ,ad888ba,                              88
//    d8"'    "8b
//   d8            88,dba,,adba,   ,aPP8A.A8  88     The Cmajor Toolkit
//   Y8,           88    88    88  88     88  88
//    Y8a.   .a8P  88    88    88  88,   ,88  88     (C)2024 Cmajor Software Ltd
//     '"Y888Y"'   88    88    88  '"8bbP"Y8  88     https://cmajor.dev
//                                           ,88
//                                        888P"
//
//  The Cmajor project is subject to commercial or open-source licensing.
//  You may use it under the terms of the GPLv3 (see www.gnu.org/licenses), or
//  visit https://cmajor.dev to learn about our commercial licence options.
//
//  CMAJOR IS PROVIDED "AS IS" WITHOUT ANY WARRANTY, AND ALL WARRANTIES, WHETHER
//  EXPRESSED OR IMPLIED, INCLUDING MERCHANTABILITY AND FITNESS FOR PURPOSE, ARE
//  DISCLAIMED.

const vscode = require('vscode');
const helpers = require ("./cmaj_helpers.js");
const { spawn } = require('node:child_process');

let sharedProcess = null;
let debugOutputChannel = null;
let activePanels = new Map();

function getSharedServerProcess (commandUri, isDevMode)
{
    if (! sharedProcess)
    {
        if (! debugOutputChannel)
        {
            debugOutputChannel = vscode.window.createOutputChannel ("Cmajor");
            debugOutputChannel.show (true);
        }

        sharedProcess = new ServerProcess (commandUri, isDevMode);
    }

    return sharedProcess;
}

//==============================================================================
class ServerProcess
{
    constructor (commandUri, isDevMode)
    {
        this.commandUri = commandUri;
        this.isDevMode = isDevMode;
        this.clientPanels = [];

        this.launchProcess();
    }

    dispose()
    {
        this.killProcess();
    }

    addClientPanel (panel)
    {
        this.clientPanels.push (panel);

        if (this.serverAddress)
            panel.serverProcessReady();
    }

    removeClientPanel (panel)
    {
        const index = this.clientPanels.indexOf (panel);

        if (index >= 0)
            this.clientPanels.splice (index, 1);

        if (this.clientPanels.length == 0)
        {
            sharedProcess = null;
            this.dispose();
        }
    }

    async launchProcess()
    {
        this.killProcess();

        if (! this.commandUri)
        {
            showMissingCmajToolError();
            return false;
        }

        let timeoutMs = vscode.workspace.getConfiguration ("cmajor").get ("timeoutMs", 5000);

        let args = ["server", "--port=51020", "--timeoutMs=" + timeoutMs];

        if (module.exports.serverAssetLocation)
            args.push (module.exports.serverAssetLocation);

        this.process = spawn (this.commandUri.fsPath, args, { stdio: [ 'ignore', 'pipe', 'pipe' ] });

        this.process.stdout.on ('data', data => this.handleProcessOutput (data));
        this.process.stderr.on ('data', data => this.handleProcessOutput (data));

        this.process.on ('close', code => this.handleProcessClosed (code));

        return true;
    }

    killProcess()
    {
        this.process?.kill();
        this.process = undefined;
        this.serverAddress = undefined;
    }

    handleProcessOutput (data)
    {
        if (data)
        {
            data = data.toString();

            if (! this.serverAddress)
            {
                const addressPrefix = "Cmajor server active:";

                if (data.includes (addressPrefix))
                {
                    for (const line of data.split ("\n"))
                    {
                        if (line.startsWith (addressPrefix))
                        {
                            const address = line.replaceAll (addressPrefix, "").trim();

                            if (address.includes ("/"))
                            {
                                this.serverAddress = address;

                                for (let c of this.clientPanels)
                                    c.serverProcessReady();
                            }
                        }
                    }
                }
            }

            debugOutputChannel?.append (data);
        }
    }

    handleProcessClosed (exitCode)
    {
        sharedProcess = null;
        console.log (`Server exited, code ${exitCode}`);

        for (let c of this.clientPanels)
            c.serverProcessTerminated();
    }

    getServerURL()  { return this.serverAddress ? this.serverAddress : ""; }
}

//==============================================================================
class PatchRunnerPanel
{
    static viewType = "Cmajor";

    constructor (panelToUse, patchFileUri, commandUri, isDevMode)
    {
        this.patchFileUri = patchFileUri;
        this.commandUri = commandUri;
        this.isDevMode = isDevMode;
        this.sessionID = this.createRandomSessionID();
        this.lastServerFailureWasInfiniteLoop = false;

        activePanels.set (patchFileUri.toString(), this);

        const options = {
            retainContextWhenHidden: true,
            enableScripts: true,
            enableForms: true
        };

        if (! panelToUse)
            panelToUse = vscode.window.createWebviewPanel (PatchRunnerPanel.viewType,
                                                           "Cmajor",
                                                           {
                                                              preserveFocus: true,
                                                              viewColumn: vscode.ViewColumn.Two
                                                           },
                                                           options);
        else
            panelToUse.webview.options = options;

        this.panel = panelToUse;
        this.panel.webview.html = this.getStatusHTML ("Starting Cmajor server...");
        this.panel.webview.onDidReceiveMessage (m => this.handleMessageFromPanel (m));
        this.panel.onDidDispose (() => this.dispose());

        this.diagnostics = vscode.languages.createDiagnosticCollection ("Cmajor");

        this.launchServer();
    }

    dispose()
    {
        activePanels.delete (this.patchFileUri.toString());
        this.closeServer();
        this.diagnostics?.dispose();
    }

    serverProcessReady()
    {
        this.panel.webview.html = this.getFullHTML();
        this.panel.webview.postMessage ({ loadPatch: this.patchFileUri.fsPath });
    }

    serverProcessTerminated()
    {
        const problem = this.lastServerFailureWasInfiniteLoop
                            ? "Server process terminated due to an infinite loop in the process!"
                            : "Lost connection to the Cmajor server process!";

        this.panel.webview.html = this.getStatusHTML (`${problem}</p>
            <p><button style="margin: 8px; padding: 5px; background-color: red; outline: none; border: none;" onclick="relaunchServer()">Relaunch</button>
        `);
    }

    launchServer()
    {
        this.lastServerFailureWasInfiniteLoop = false;
        this.serverProcess = getSharedServerProcess (this.commandUri, this.isDevMode);
        this.serverProcess.addClientPanel (this);
    }

    closeServer()
    {
        this.serverProcess?.removeClientPanel (this);
        this.serverProcess = undefined;
    }

    handleMessageFromPanel (message)
    {
        if (message?.newServerStatus)
        {
            const status = message.newServerStatus;
            let newTitle = "Cmajor";

            if (status.manifest && status.manifest.name)
                newTitle = "Cmajor: " + status.manifest.name;
            else if (status.error)
                newTitle = "Cmajor: Build Error";

            this.refreshDiagnostics (status.error);
            this.panel.title = newTitle;
        }
        else if (message?.readClipboard)
        {
            vscode.env.clipboard.readText()
                .then (text => this.sendMessageToPanel ({ clipboardText: text }));
        }
        else if (message?.writeClipboard)
        {
            vscode.env.clipboard.writeText (message.writeClipboard);
        }
        else if (message?.showSourceFile)
        {
            this.showSourceFile (message.showSourceFile.toString());
        }
        else if (message?.openURLInNewWindow)
        {
            vscode.env.openExternal (vscode.Uri.parse (message.openURLInNewWindow));
        }
        else if (message?.showErrorAlert)
        {
            vscode.window.showErrorMessage (message.showErrorAlert);
        }
        else if (message?.openTextDocument)
        {
            vscode.workspace.openTextDocument ({ content: message.openTextDocument,
                                                 language: message.language })
                .then (doc => this.showTextDocumentInOtherColumn (doc));
        }
        else if (message?.serverFailedWithInfiniteLoop)
        {
            this.lastServerFailureWasInfiniteLoop = true;
        }
        else if (message?.reloading)
        {
            // when the panel reloads, we need to send a message so it can reattach its event target
            setTimeout (() => this.sendMessageToPanel ({ reloaded: true }), 500);
        }
        else if (message?.relaunchServer)
        {
            this.closeServer();
            this.launchServer();
        }
    }

    sendMessageToPanel (message)
    {
        this.panel?.webview?.postMessage ({ messageFromVScode: message });
    }

    refreshDiagnostics (errorText)
    {
        this.diagnostics.clear();

        if (errorText)
        {
            const lines = errorText.split ("\n");
            const fileAndPositionMatcher = /^(.*)(:(\d+):(\d+):)\s+(warning|error|note):\s+(.*)$/;
            const fileOnlyMatcher = /^(.*):\s+(warning|error|note):\s+(.*)$/;
            let perFileDiagnosticLists = new Map();

            function addDiagnostic (file, line, column, type, message, code)
            {
                const range = new vscode.Range (line, column, line, column);
                type = type.toString().trim();

                const severity = (type == "warning" ? vscode.DiagnosticSeverity.Warning
                                                    : (type == "note" ? vscode.DiagnosticSeverity.Information
                                                                      : vscode.DiagnosticSeverity.Error));

                const diagnostic = new vscode.Diagnostic (range, message.toString().trim(), severity);

                const filename = file.toString();
                const existingList = perFileDiagnosticLists.get (filename);

                if (! existingList)
                    perFileDiagnosticLists.set (filename, { file: file, list: [diagnostic] });
                else
                    existingList.list.push (diagnostic);
            }

            for (let i = 0; i < lines.length; ++i)
            {
                let matches = lines[i].match (fileAndPositionMatcher);

                if (matches && matches.length == 7)
                {
                    const file = vscode.Uri.file (matches[1]);

                    if (file)
                    {
                        const line    = matches[3] - 1;
                        const column  = matches[4] - 1;
                        const type    = matches[5].toString().trim();
                        const message = matches[6].toString().trim();

                        addDiagnostic (file, line, column, type, message);
                    }
                }
                else
                {
                    matches = lines[i].match (fileOnlyMatcher);

                    if (matches && matches.length == 4)
                    {
                        const file = vscode.Uri.file (matches[1]);

                        if (file)
                        {
                            const type    = matches[2].toString().trim();
                            const message = matches[3].toString().trim();

                            addDiagnostic (file, 0, 0, type, message);
                        }
                    }
                }
            }

            perFileDiagnosticLists.forEach ((list, file) => this.diagnostics.set (list.file, list.list));
        }
    }

    showSourceFile (file)
    {
        file = file.trim();

        if (file.endsWith (":"))
            file = file.substring (0, file.length - 1);

        let selection = null;

        let matches = file.match (/^(.*):(\d+):(\d+)$/);

        if (matches?.length == 4 && matches[1])
        {
            file = matches[1];
            const line    = matches[2] - 1;
            const column  = matches[3] - 1;
            const start = new vscode.Position (line, column);
            selection = new vscode.Range (start, start);
        }
        else
        {
            matches = file.match (/^(.*):(\d+)$/);

            if (matches?.length == 3 && matches[1])
            {
                file = matches[1];
                const line = matches[2] - 1;
                const start = new vscode.Position (line, 0);
                selection = new vscode.Range (start, start);
            }
        }

        vscode.workspace.openTextDocument (vscode.Uri.file (file))
           .then (doc => this.showTextDocumentInOtherColumn (doc, selection));
    }

    showTextDocumentInOtherColumn (document, selection)
    {
        let viewColumn = null;

        if (this.panel?.viewColumn == vscode.ViewColumn.Two
             || this.panel?.viewColumn == vscode.ViewColumn.Three)
            viewColumn = vscode.ViewColumn.One;

        vscode.window.showTextDocument (document,
                                        {
                                            preserveFocus: false,
                                            preview: true,
                                            selection: selection,
                                            viewColumn: viewColumn
                                        });
    }

    getIndexURL()
    {
        return this.serverProcess.getServerURL() + "/session_" + this.sessionID + "/cmaj-patch-runner.html";
    }

    createRandomSessionID()
    {
        let sessionID = "";

        for (let i = 0; i < 10; ++i)
            sessionID += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[Math.floor (Math.random() * 25)];

        return sessionID;
    }

    getHTML (body)
    {
        return `
<!DOCTYPE html>
<html><head><meta charset="utf-8"/><title>Cmajor Patch Runner</title></head>
<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

.cmaj-body {
    padding: 0;
}

iframe {
    width: 100%;
    height: 100%;
    position: absolute;
    border: none;
    margin: 0;
    padding: 0;
  }
</style>

<script>
 const vscode = acquireVsCodeApi();
 function relaunchServer() { vscode.postMessage ({ relaunchServer: true }); }
</script>

${body}
</html>`;
    }

    getStatusHTML (message)
    {
        return this.getHTML (`<body><p>${message}</p></body>`);
    }

    getFullHTML()
    {
        return this.getHTML (`
<body class="cmaj-body">
  <iframe id="cmaj-panel-content"></iframe>
</body>

<script type="module">

const iframe = document.getElementById ("cmaj-panel-content");

function loadPatch (file)
{
    vscode.setState ({ file: file });
    iframe.contentWindow.postMessage ({ messageFromVScode: { patchToLoad: file } }, "*");
}

iframe.onload = () =>
{
    const state = vscode.getState();

    if (state?.file)
        loadPatch (state.file);

    iframe.onload = undefined;
}

window.addEventListener ("message", event =>
{
    if (event?.data?.loadPatch)
        loadPatch (event.data.loadPatch);
    else if (event?.data?.messageFromVScode)
        iframe.contentWindow.postMessage (event.data, "*");
    else if (event?.data?.messageToVScode)
        vscode.postMessage (event.data.messageToVScode);
});

iframe.src = "${this.getIndexURL()}";

</script>`);
    }
}

async function showPanel (patchFileUri, extensionUri, isDevMode)
{
    const existing = activePanels.get (patchFileUri.toString());

    if (existing && existing.panel)
    {
        existing.panel.reveal();
        return;
    }

    const commandUri = await helpers.findCmajTool (extensionUri);

    if (! commandUri)
    {
        helpers.showMissingCmajToolError();
        return;
    }

    new PatchRunnerPanel (null, patchFileUri, commandUri, isDevMode);
}

function registerSerialiser (extensionUri, isDevMode)
{
    if (vscode.window.registerWebviewPanelSerializer)
    {
        vscode.window.registerWebviewPanelSerializer (PatchRunnerPanel.viewType,
        {
            async deserializeWebviewPanel (webviewPanel, state)
            {
                const commandUri = await helpers.findCmajTool (extensionUri);

                if (state.file)
                    new PatchRunnerPanel (webviewPanel, state.file, commandUri, isDevMode);
            }
        });
    }
}

module.exports = {
    showPanel,
    registerSerialiser
}
