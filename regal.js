"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.promptForInstallRegal = promptForInstallRegal;
exports.isInstalledRegal = isInstalledRegal;
exports.promptForUpdateRegal = promptForUpdateRegal;
exports.regalPath = regalPath;
exports.activateRegal = activateRegal;
exports.deactivateRegal = deactivateRegal;
const child_process_1 = require("child_process");
const command_exists_1 = require("command-exists");
const fs_1 = require("fs");
const path_1 = require("path");
const semver = require("semver");
const vscode_1 = require("vscode");
const vscode = require("vscode");
const node_1 = require("vscode-languageclient/node");
const extension_1 = require("../../extension");
const github_installer_1 = require("../../github-installer");
const util_1 = require("../../util");
let client;
let clientLock = false;
let outChan;
let activeDebugSessions = new Map();
const minimumSupportedRegalVersion = "0.18.0";
function promptForInstallRegal(message) {
    const dlOpts = downloadOptionsRegal();
    (0, github_installer_1.promptForInstall)("regal", dlOpts.repo, message, dlOpts.determineBinaryURLFromRelease, dlOpts.determineExecutableName);
}
function isInstalledRegal() {
    if ((0, command_exists_1.sync)(regalPath())) {
        return true;
    }
    return false;
}
function promptForUpdateRegal(minVer = minimumSupportedRegalVersion) {
    const version = regalVersion();
    if (version === "missing") {
        promptForInstallRegal("Regal is needed but not installed. Would you like to install it?");
        return;
    }
    // assumption here that it's a dev version or something, and ignore
    if (!semver.valid(version)) {
        return;
    }
    if (semver.gte(version, minVer)) {
        return;
    }
    const path = regalPath();
    let message = "The version of Regal that the OPA extension is using is out of date. Click \"Install\" to update it to a new one.";
    // if the path is not the path where VS Code manages Regal,
    // then we show another message
    if (path === "regal") {
        message = "Installed Regal version " + version + " is out of date and is not supported. Please update Regal to "
            + minVer
            + " using your preferred method. Or click \"Install\" to use a version managed by the OPA extension.";
    }
    promptForInstallRegal(message);
    return;
}
function regalVersion() {
    let version = "missing";
    if (isInstalledRegal()) {
        const versionJSON = (0, child_process_1.execSync)(regalPath() + " version --format=json").toString().trim();
        const versionObj = JSON.parse(versionJSON);
        version = versionObj.version || "unknown";
    }
    return version;
}
function regalPath() {
    let path = vscode.workspace.getConfiguration("opa.dependency_paths").get("regal");
    if (path !== undefined && path !== null) {
        path = (0, util_1.replaceWorkspaceFolderPathVariable)(path);
    }
    if (path !== undefined && path !== null && path.length > 0) {
        if (path.startsWith("file://")) {
            path = path.substring(7);
        }
        if ((0, fs_1.existsSync)(path)) {
            return path;
        }
    }
    // default case, attempt to find in path
    return "regal";
}
class debuggableMessageStrategy {
    handleMessage(message, next) {
        // If the VSCODE_DEBUG_MODE environment variable is set to true, then
        // we can log the messages to the console for debugging purposes.
        if (process.env.VSCODE_DEBUG_MODE === "true") {
            const messageData = JSON.parse(JSON.stringify(message));
            const method = messageData.method || "response";
            console.log(method, JSON.stringify(messageData));
        }
        return next(message);
    }
}
function activateRegal(_context) {
    if (!outChan) {
        outChan = vscode_1.window.createOutputChannel("Regal");
    }
    // activateRegal is run when the config changes, but this happens a few times
    // at startup. We use clientLock to prevent the activation of multiple instances.
    if (clientLock) {
        return;
    }
    clientLock = true;
    promptForUpdateRegal();
    const version = regalVersion();
    if (version === "missing") {
        extension_1.opaOutputChannel.appendLine("Regal LS could not be started because the \"regal\" executable is not available.");
        return;
    }
    // assumption here that it's a dev version or something, and ignore.
    // if the version is invalid, then continue as assuming a dev build or similar
    if (semver.valid(version)) {
        if (semver.lt(version, minimumSupportedRegalVersion)) {
            extension_1.opaOutputChannel.appendLine("Regal LS could not be started because the version of \"regal\" is less than the minimum supported version.");
            return;
        }
    }
    const serverOptions = {
        command: regalPath(),
        args: ["language-server"],
    };
    const clientOptions = {
        documentSelector: [{ scheme: "file", language: "rego" }],
        outputChannel: outChan,
        traceOutputChannel: outChan,
        revealOutputChannelOn: 0,
        connectionOptions: {
            messageStrategy: new debuggableMessageStrategy(),
        },
        errorHandler: {
            error: (error, message, _count) => {
                console.error(error);
                console.error(message);
                return {
                    action: node_1.ErrorAction.Continue,
                };
            },
            closed: () => {
                console.error("client closed");
                return {
                    action: node_1.CloseAction.DoNotRestart,
                };
            },
        },
        synchronize: {
            fileEvents: [
                vscode_1.workspace.createFileSystemWatcher("**/*.rego"),
                vscode_1.workspace.createFileSystemWatcher("**/.regal/config.yaml"),
            ],
        },
        diagnosticPullOptions: {
            onChange: true,
            onSave: true,
        },
        initializationOptions: {
            formatter: vscode.workspace.getConfiguration("opa").get("formatter", "opa-fmt"),
            // These options are passed to the Regal language server to signal the
            // capabilities of the client. Since VSCode and vscode-opa supports both
            // inline evaluation results and live debugging, both are enabled and are
            // not configurable.
            evalCodelensDisplayInline: true,
            enableDebugCodelens: true,
        },
    };
    client = new node_1.LanguageClient("regal", "Regal LSP client", serverOptions, clientOptions);
    client.onRequest("regal/showEvalResult", handleRegalShowEvalResult);
    client.onRequest("regal/startDebugging", handleDebug);
    vscode.debug.onDidTerminateDebugSession((session) => {
        activeDebugSessions.delete(session.name);
    });
    client.start();
}
function deactivateRegal() {
    clientLock = false;
    if (!client) {
        return undefined;
    }
    return client.stop();
}
function downloadOptionsRegal() {
    return {
        repo: "open-polict-agent/regal",
        determineBinaryURLFromRelease: (release) => {
            // release.assets.name contains {'darwin', 'linux', 'windows'}
            const assets = release.assets || [];
            const os = process.platform;
            let targetAsset;
            switch (os) {
                case "darwin":
                    targetAsset = assets.filter((asset) => asset.name.indexOf("Darwin") !== -1)[0];
                    break;
                case "linux":
                    targetAsset = assets.filter((asset) => asset.name.indexOf("Linux") !== -1)[0];
                    break;
                case "win32":
                    targetAsset = assets.filter((asset) => asset.name.indexOf("Windows") !== -1)[0];
                    break;
                default:
                    targetAsset = { browser_download_url: "" };
            }
            return targetAsset.browser_download_url;
        },
        determineExecutableName: () => {
            const os = process.platform;
            switch (os) {
                case "darwin":
                case "linux":
                    return "regal";
                case "win32":
                    return "regal.exe";
                default:
                    return "regal";
            }
        },
    };
}
function handleDebug(params) {
    const activeEditor = vscode.window.activeTextEditor;
    if (!activeEditor) {
        return;
    }
    if (activeDebugSessions.has(params.name)) {
        vscode.window.showErrorMessage("Debug session for '" + params.name + "' already active");
        return;
    }
    vscode.debug.startDebugging(undefined, params).then((success) => {
        if (success) {
            activeDebugSessions.set(params.name, undefined);
        }
    });
}
function handleRegalShowEvalResult(params) {
    const activeEditor = vscode.window.activeTextEditor;
    if (!activeEditor)
        return;
    // Before setting a new decoration, remove all previous decorations
    (0, extension_1.removeDecorations)();
    const { attachmentMessage, hoverMessage } = createMessages(params);
    const decorationOptions = [];
    const targetDecorationOptions = [];
    const truncateThreshold = 100;
    if (params.target === "package") {
        handlePackageDecoration(params, activeEditor, decorationOptions, targetDecorationOptions, attachmentMessage, hoverMessage, truncateThreshold);
    }
    else if (params.rule_head_locations.length > 0) {
        handleRuleHeadsDecoration(params, activeEditor, decorationOptions, targetDecorationOptions, attachmentMessage, hoverMessage, truncateThreshold);
    }
    handlePrintOutputDecoration(params, activeEditor, decorationOptions, truncateThreshold);
    const wf = vscode.workspace.getWorkspaceFolder(activeEditor.document.uri);
    for (const [uri, items] of Object.entries(params.result.printOutput)) {
        let path;
        if (wf) {
            path = (0, path_1.relative)(wf.uri.fsPath, vscode.Uri.parse(uri).fsPath);
        }
        else {
            path = vscode.Uri.parse(uri).fsPath;
        }
        Object.keys(items).map(Number).forEach((line) => {
            outChan.appendLine(`🖨️ ${path}:${line} => ${items[line].join(" => ")}`);
        });
    }
    // Always set the base decoration, containing the result message and after text
    activeEditor.setDecorations(extension_1.evalResultDecorationType, decorationOptions);
    // Set decoration type based on whether the result is undefined
    const targetDecorationType = params.result.isUndefined
        ? extension_1.evalResultTargetUndefinedDecorationType
        : extension_1.evalResultTargetSuccessDecorationType;
    activeEditor.setDecorations(targetDecorationType, targetDecorationOptions);
}
function createMessages(params) {
    let attachmentMessage = params.result.value;
    let hoverMessage = params.result.value;
    const hoverTitle = "### Evaluation Result\n\n";
    if (params.result.isUndefined) {
        // Handle rule result
        attachmentMessage = "undefined";
        hoverMessage = hoverTitle + makeCode("text", attachmentMessage);
    }
    else if (typeof params.result.value === "object") {
        // Handle objects (including arrays)
        const formattedValue = JSON.stringify(params.result.value, null, 2);
        attachmentMessage = formattedValue.replace(/\n\s*/g, " ")
            .replace(/(\{|\[)\s/g, "$1")
            .replace(/\s(\}|\])/g, "$1");
        const code = makeCode("json", formattedValue);
        hoverMessage = hoverTitle + (code.length > 100000 ? formattedValue : code);
    }
    else {
        // Handle strings and other types simple types
        if (typeof params.result.value === "string") {
            attachmentMessage = `"${params.result.value.replace(/ /g, "\u00a0")}"`;
        }
        hoverMessage = hoverTitle + makeCode("json", attachmentMessage);
    }
    return { attachmentMessage, hoverMessage };
}
function handlePackageDecoration(params, activeEditor, decorationOptions, targetDecorationOptions, attachmentMessage, hoverMessage, truncateThreshold) {
    const line = params.line - 1;
    const documentLine = activeEditor.document.lineAt(line);
    const lineLength = documentLine.text.length;
    // To avoid horizontal scroll for large outputs, we ask users to hover for the full result
    if (lineLength + attachmentMessage.length > truncateThreshold) {
        const suffix = "... (hover for result)";
        attachmentMessage = attachmentMessage.substring(0, truncateThreshold - lineLength - suffix.length) + suffix;
    }
    decorationOptions.push(createDecoration(line, lineLength, hoverMessage, attachmentMessage));
    const packageIndex = documentLine.text.indexOf(params.package);
    const startChar = packageIndex > 0 ? packageIndex : 0;
    const endChar = packageIndex > 0 ? packageIndex + params.package.length : lineLength;
    // Highlight only the target name with a color, displayed in addition to the whole line decoration
    targetDecorationOptions.push({
        range: new vscode.Range(new vscode.Position(line, startChar), new vscode.Position(line, endChar)),
    });
}
function handleRuleHeadsDecoration(params, activeEditor, decorationOptions, targetDecorationOptions, attachmentMessage, hoverMessage, truncateThreshold) {
    params.rule_head_locations.forEach((location) => {
        const line = location.row - 1;
        const documentLine = activeEditor.document.lineAt(line);
        const lineLength = documentLine.text.length;
        // To avoid horizontal scroll for large outputs, we ask users to hover for the full result
        if (lineLength + attachmentMessage.length > truncateThreshold) {
            const suffix = "... (hover for result)";
            attachmentMessage = attachmentMessage.substring(0, truncateThreshold - lineLength - suffix.length) + suffix;
        }
        decorationOptions.push(createDecoration(line, lineLength, hoverMessage, attachmentMessage));
        const startChar = location.col - 1;
        const endChar = documentLine.text.includes(params.target)
            ? startChar + params.target.length
            : findEndChar(documentLine.text, lineLength);
        // Highlight only the target name with a color, displayed in addition to the whole line decoration
        targetDecorationOptions.push({
            range: new vscode.Range(new vscode.Position(line, startChar), new vscode.Position(line, endChar)),
        });
    });
}
function handlePrintOutputDecoration(params, activeEditor, decorationOptions, truncateThreshold) {
    // TODO: display print output in any file from the params map!
    // Currently only print output in the current editor is shown
    const printOutput = params.result.printOutput[activeEditor.document.uri.toString()];
    if (!printOutput) {
        return;
    }
    Object.keys(printOutput).map(Number).forEach((line) => {
        const lineLength = activeEditor.document.lineAt(line).text.length;
        const joinedLines = printOutput[line].join("\n");
        // Pre-block formatting fails if there are over 100k chars
        const hoverText = joinedLines.length < 100000 ? makeCode("text", joinedLines) : joinedLines;
        const hoverMessage = "### Print Output\n\n" + hoverText;
        let attachmentMessage = ` 🖨️ => ${printOutput[line].join(" => ")}`;
        if (lineLength + attachmentMessage.length > truncateThreshold) {
            const suffix = "... (hover for result)";
            attachmentMessage = attachmentMessage.substring(0, truncateThreshold - lineLength - suffix.length) + suffix;
        }
        decorationOptions.push({
            range: new vscode.Range(new vscode.Position(line - 1, 0), new vscode.Position(line - 1, lineLength)),
            hoverMessage: hoverMessage,
            renderOptions: {
                after: {
                    contentText: attachmentMessage,
                    color: new vscode.ThemeColor("editorLineNumber.foreground"),
                },
            },
        });
    });
}
function createDecoration(line, lineLength, hoverMessage, attachmentMessage) {
    // Create base decoration options for a line
    return {
        range: new vscode.Range(new vscode.Position(line, 0), new vscode.Position(line, lineLength)),
        hoverMessage: hoverMessage,
        renderOptions: {
            after: {
                contentText: ` => ${attachmentMessage}`,
                color: new vscode.ThemeColor("editorLineNumber.foreground"),
            },
        },
    };
}
function findEndChar(text, lineLength) {
    // Find the end character position, stopping at the first [ or . character as a fallback
    for (let i = 0; i < lineLength; i++) {
        if (text[i] === "[" || text[i] === ".") {
            return i;
        }
    }
    return lineLength;
}
// makeCode returns a markdown code block with the given language and code
function makeCode(lang, code) {
    return "```" + lang + "\n" + code + "\n```";
}
//# sourceMappingURL=regal.js.map