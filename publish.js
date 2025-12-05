"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.displayPublishTerminal = exports.onChangeAppFile = exports.publishAppFile = exports.publishApp = void 0;
const fs_1 = require("fs");
const path_1 = require("path");
const vscode = require("vscode");
const alFileHelper_1 = require("./alFileHelper");
const config_1 = require("./config");
const constants_1 = require("./constants");
const extension_1 = require("./extension");
const file_1 = require("./file");
const telemetry_1 = require("./telemetry");
const types_1 = require("./types");
let shouldPublishApp = false;
function publishApp(publishType) {
    return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
        (0, telemetry_1.sendDebugEvent)('publishApp-start', { publishType: publishType.toString() });
        let success = false;
        let message = '';
        if (publishType === types_1.PublishType.None) {
            resolve({ success: true, message: '' });
            return;
        }
        const closeEditor = yield (0, alFileHelper_1.openEditorToTestFileIfNotAlready)();
        let command = '';
        if ((0, config_1.getCurrentWorkspaceConfig)().enablePublishingFromPowerShell) {
            (0, telemetry_1.sendDebugEvent)('publishApp-publishFromPowerShell');
            shouldPublishApp = true;
            if ((0, fs_1.existsSync)(getPublishCompletionPath())) {
                (0, fs_1.unlinkSync)(getPublishCompletionPath());
            }
            yield vscode.commands.executeCommand('al.package');
            const resultExists = yield (0, file_1.awaitFileExistence)(getPublishCompletionPath(), (0, config_1.getCurrentWorkspaceConfig)().publishTimeout);
            if (resultExists) {
                const content = (0, fs_1.readFileSync)(getPublishCompletionPath(), { encoding: 'utf-8' });
                success = content.trim() === '1';
                if (!success) {
                    message = content;
                    (0, telemetry_1.sendFailedToPublishError)(content);
                }
            }
            else {
                success = false;
                (0, telemetry_1.sendFailedToPublishError)();
            }
        }
        else {
            (0, telemetry_1.sendDebugEvent)('publishApp-publishWithALCommand');
            switch (publishType) {
                case types_1.PublishType.Publish:
                    command = 'al.publishNoDebug';
                    break;
                case types_1.PublishType.Rapid:
                    command = 'al.incrementalPublishNoDebug';
                    break;
            }
            yield vscode.commands.executeCommand(command);
            success = true;
        }
        if (closeEditor) {
            if ((0, alFileHelper_1.activeEditorIsOpenToTestAppJson)()) {
                yield vscode.commands.executeCommand('workbench.action.closeActiveEditor');
            }
        }
        resolve({ success: success, message: message });
    }));
}
exports.publishApp = publishApp;
function publishAppFile(uri) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            shouldPublishApp = false;
            const terminal = (0, extension_1.getALTestRunnerTerminal)(getTerminalName());
            terminal.show(true);
            terminal.sendText(' ');
            terminal.sendText(`Publish-App -AppFile "${uri.fsPath}" -CompletionPath "${getPublishCompletionPath()}" -LaunchConfig '${(0, config_1.getLaunchConfiguration)((0, config_1.getALTestRunnerConfig)().launchConfigName)}'`);
            const resultExists = yield (0, file_1.awaitFileExistence)(getPublishCompletionPath(), (0, config_1.getCurrentWorkspaceConfig)().publishTimeout);
            if (resultExists) {
                const content = (0, fs_1.readFileSync)(getPublishCompletionPath(), { encoding: 'utf-8' });
                const success = content.trim() === '1';
                let message = '';
                if (!success) {
                    message = content.trim();
                }
                resolve({ success: success, message: message });
            }
            else {
                resolve({ success: false, message: constants_1.failedToPublishMessage });
            }
        }));
    });
}
exports.publishAppFile = publishAppFile;
function onChangeAppFile(uri) {
    return __awaiter(this, void 0, void 0, function* () {
        if ((!shouldPublishApp) && (!(0, config_1.getCurrentWorkspaceConfig)().automaticPublishing)) {
            return;
        }
        if ((uri.fsPath.indexOf('dep.app') > 0) || (uri.fsPath.indexOf('.alpackages') > 0)) {
            return;
        }
        yield publishAppFile(uri);
    });
}
exports.onChangeAppFile = onChangeAppFile;
function getTerminalName() {
    return 'al-test-runner';
}
function getPublishCompletionPath() {
    return (0, path_1.join)((0, config_1.getALTestRunnerPath)(), "publish.txt");
}
function displayPublishTerminal() {
    const terminal = (0, extension_1.getALTestRunnerTerminal)(getTerminalName());
    terminal.show(false);
}
exports.displayPublishTerminal = displayPublishTerminal;
//# sourceMappingURL=publish.js.map