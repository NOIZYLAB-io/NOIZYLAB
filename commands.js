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
exports.registerCommands = void 0;
const vscode = require("vscode");
const testController_1 = require("./testController");
const config_1 = require("./config");
const fs_1 = require("fs");
const extension_1 = require("./extension");
const coverage_1 = require("./coverage");
const showTableData_1 = require("./showTableData");
const testCoverage_1 = require("./testCoverage");
const alFileHelper_1 = require("./alFileHelper");
const performance_1 = require("./performance");
const pageScripting_1 = require("./pageScripting");
const devOpsTestSteps_1 = require("./devOpsTestSteps");
function registerCommands(context) {
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.runAllTests', (extensionId, extensionName) => __awaiter(this, void 0, void 0, function* () {
        (0, testController_1.runTestHandler)(new vscode.TestRunRequest());
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.runTestsCodeunit', (filename, extensionId, extensionName) => __awaiter(this, void 0, void 0, function* () {
        const testItem = yield (0, testController_1.getTestItemFromFileNameAndSelection)(filename, 0);
        if (testItem) {
            const request = new vscode.TestRunRequest([testItem]);
            (0, testController_1.runTestHandler)(request);
        }
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.runTest', (filename, selectionStart, extensionId, extensionName) => __awaiter(this, void 0, void 0, function* () {
        const testItem = yield (0, testController_1.getTestItemFromFileNameAndSelection)(filename, selectionStart);
        if (testItem) {
            const request = new vscode.TestRunRequest([testItem]);
            (0, testController_1.runTestHandler)(request);
        }
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.debugTest', (filename, selectionStart) => __awaiter(this, void 0, void 0, function* () {
        const testItem = yield (0, testController_1.getTestItemFromFileNameAndSelection)(filename, selectionStart);
        if (testItem) {
            const request = new vscode.TestRunRequest([testItem]);
            (0, testController_1.debugTestHandler)(request);
        }
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.debugTestsCodeunit', (filename) => __awaiter(this, void 0, void 0, function* () {
        const testItem = yield (0, testController_1.getTestItemFromFileNameAndSelection)(filename, 0);
        if (testItem) {
            const request = new vscode.TestRunRequest([testItem]);
            (0, testController_1.debugTestHandler)(request);
        }
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.clearTestResults', () => __awaiter(this, void 0, void 0, function* () {
        const resultsPath = (0, config_1.getALTestRunnerPath)() + '\\Results';
        if ((0, fs_1.existsSync)(resultsPath)) {
            (0, fs_1.readdirSync)(resultsPath).forEach(e => (0, fs_1.unlinkSync)(resultsPath + '\\' + e));
        }
        (0, extension_1.triggerUpdateDecorations)();
        vscode.window.showInformationMessage('AL Test Runner results cleared');
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.clearCredentials', () => __awaiter(this, void 0, void 0, function* () {
        (0, config_1.setALTestRunnerConfig)('userName', '');
        (0, config_1.setALTestRunnerConfig)('securePassword', '');
        vscode.window.showInformationMessage('AL Test Runner credentials cleared');
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.setContainerCredential', () => {
        (0, config_1.setALTestRunnerConfig)('userName', '');
        (0, config_1.setALTestRunnerConfig)('securePassword', '');
        let terminal = (0, extension_1.getALTestRunnerTerminal)((0, extension_1.getTerminalName)());
        terminal.show(false);
        terminal.sendText(' ');
        terminal.sendText('Set-ALTestRunnerCredential -Credential (Get-Credential)');
    }));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.setVMCredential', () => {
        (0, config_1.setALTestRunnerConfig)('vmUserName', '');
        (0, config_1.setALTestRunnerConfig)('vmSecurePassword', '');
        let terminal = (0, extension_1.getALTestRunnerTerminal)((0, extension_1.getTerminalName)());
        terminal.sendText(' ');
        terminal.sendText('Get-ALTestRunnerCredential -VM');
    }));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.openConfigFile', () => __awaiter(this, void 0, void 0, function* () {
        (0, config_1.getALTestRunnerConfig)();
        vscode.window.showTextDocument(yield vscode.workspace.openTextDocument((0, config_1.getALTestRunnerConfigPath)()));
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.installTestRunnerService', () => __awaiter(this, void 0, void 0, function* () {
        let terminal = (0, extension_1.getALTestRunnerTerminal)((0, extension_1.getTerminalName)());
        terminal.show(true);
        terminal.sendText(`Install-TestRunnerService -LaunchConfig '${(0, config_1.getLaunchConfiguration)((0, config_1.getALTestRunnerConfig)().launchConfigName)}'`);
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.toggleCodeCoverage', (newCodeCoverageDisplay) => __awaiter(this, void 0, void 0, function* () {
        (0, coverage_1.toggleCodeCoverageDisplay)(newCodeCoverageDisplay);
    })));
    vscode.commands.registerCommand('altestrunner.showTableData', () => __awaiter(this, void 0, void 0, function* () {
        (0, showTableData_1.showTableData)();
    }));
    vscode.commands.registerCommand('altestrunner.showRelatedTests', method => {
        (0, testCoverage_1.showRelatedTests)(method);
    });
    vscode.commands.registerCommand('altestrunner.runRelatedTests', method => {
        (0, testCoverage_1.runRelatedTests)(method);
    });
    vscode.commands.registerCommand('altestrunner.viewPageScriptingReport', () => {
        (0, pageScripting_1.viewPageScriptingReport)();
    });
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.listALFiles', () => __awaiter(this, void 0, void 0, function* () {
        yield (0, alFileHelper_1.listALFiles)();
    })));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.showPerformanceProfile', () => {
        (0, performance_1.showPerformanceProfile)();
    }));
    context.subscriptions.push(vscode.commands.registerCommand('altestrunner.exportTestItemsToCsv', (testItem) => __awaiter(this, void 0, void 0, function* () {
        (0, devOpsTestSteps_1.exportTestItemsToCsv)(testItem);
    })));
}
exports.registerCommands = registerCommands;
//# sourceMappingURL=commands.js.map