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
exports.testItemIsPageScript = exports.runPageScript = exports.discoverPageScripts = exports.viewPageScriptingReport = void 0;
const vscode = require("vscode");
const path = require("path");
const fs_1 = require("fs");
const child_process_1 = require("child_process");
const config_1 = require("./config");
const path_1 = require("path");
const xml2js = require("xml2js");
const extension_1 = require("./extension");
function viewPageScriptingReport() {
    return __awaiter(this, void 0, void 0, function* () {
        let terminal = (0, extension_1.getALTestRunnerTerminal)();
        terminal.show(true);
        terminal.sendText(`cd "${(0, config_1.getALTestRunnerPath)()}"`);
        terminal.sendText('npx playwright show-report');
    });
}
exports.viewPageScriptingReport = viewPageScriptingReport;
function discoverPageScripts(testController) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            let testItems = [];
            const scriptFiles = yield vscode.workspace.findFiles('**/*.yml', '**/.altestrunner/**');
            scriptFiles.forEach(scriptFile => {
                if (uriIsPageScript(scriptFile)) {
                    const name = path.parse(scriptFile.fsPath).name;
                    testItems.push(testController.createTestItem(name, name, scriptFile));
                }
            });
            resolve(testItems);
        }));
    });
}
exports.discoverPageScripts = discoverPageScripts;
function runPageScript(testItem) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve, reject) => __awaiter(this, void 0, void 0, function* () {
            if (!((0, fs_1.existsSync)(`${(0, config_1.getALTestRunnerPath)()}/node_modules/@microsoft/bc-replay`))) {
                vscode.window.showInformationMessage('Installing bc-replay package. This may take a few minutes.');
                yield execCommand('npm install @microsoft/bc-replay', { cwd: (0, config_1.getALTestRunnerPath)() });
            }
            const launchConfig = yield (0, config_1.getALTestRunnerLaunchConfig)();
            let containerPassword;
            try {
                containerPassword = yield (0, config_1.getContainerPasswordFromALTestRunnerConfig)();
            }
            catch (error) {
                resolve([]);
                return;
            }
            const env = Object.assign(Object.assign({}, process.env), { pageScriptingUser: (0, config_1.getALTestRunnerConfig)().userName, pageScriptingPassword: containerPassword });
            const options = {
                env,
                cwd: (0, config_1.getALTestRunnerPath)()
            };
            let server = `${launchConfig.server}/${launchConfig.serverInstance}`;
            if (launchConfig.tenant) {
                server += `?tenant=${launchConfig.tenant}`;
            }
            let pageScripts = [];
            injectRandomValues(testItem, pageScripts);
            let testsPath = '';
            if (testItem.parent) {
                testsPath = testItem.uri.fsPath;
                vscode.window.showInformationMessage(`Running test: ${testItem.label} on ${server}`);
            }
            else {
                testItem.children.forEach(child => {
                    testsPath = (0, path_1.join)(path.dirname(child.uri.fsPath), '/**/*.yml');
                });
                vscode.window.showInformationMessage(`Running all page scripts on ${server}`);
            }
            let command = `npx replay -Tests "${testsPath}" -Authentication UserPassword -StartAddress "${server}" -UserNameKey pageScriptingUser -PasswordKey pageScriptingPassword -ResultDir "${(0, config_1.getALTestRunnerPath)()}"`;
            if ((0, config_1.getCurrentWorkspaceConfig)().runPageScriptsHeaded) {
                command += ' -Headed';
            }
            //replace double slashes with single slashes
            command = command.replace(/\\/g, '/');
            try {
                yield execCommand(command, options);
            }
            catch (error) {
                if (!(error.message.includes('One or more test recordings failed'))) {
                    vscode.window.showErrorMessage(`Error executing command: ${error.message}`);
                    reject(error);
                    return;
                }
            }
            resolve(yield getResults());
            restorePageScriptContent(pageScripts);
        }));
    });
}
exports.runPageScript = runPageScript;
function execCommand(command, options) {
    return new Promise((resolve, reject) => {
        (0, child_process_1.exec)(command, options, (error, stdout, stderr) => {
            if (error) {
                reject(error);
                return;
            }
            resolve();
        });
    });
}
function testItemIsPageScript(testItem) {
    var _a;
    return (((_a = testItem.parent) === null || _a === void 0 ? void 0 : _a.label) === 'Page Scripts') || (testItem.label == 'Page Scripts');
}
exports.testItemIsPageScript = testItemIsPageScript;
function uriIsPageScript(uri) {
    return (0, fs_1.readFileSync)(uri.fsPath, { encoding: 'utf-8' }).includes('page:');
}
function getResults() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const resultPath = path.join((0, config_1.getALTestRunnerPath)(), 'results.xml');
            if (!(0, fs_1.existsSync)(resultPath)) {
                resolve([]);
                return;
            }
            const xmlParser = new xml2js.Parser();
            const resultXml = (0, fs_1.readFileSync)(resultPath, { encoding: 'utf-8' });
            const resultObj = yield xmlParser.parseStringPromise(resultXml);
            let results = [];
            let collections = [];
            resultObj.testsuites.testsuite.forEach((suite) => {
                let collection;
                let tests = [];
                suite.testcase.forEach((test) => {
                    let testName = test.$.name;
                    testName = testName.trim();
                    if (testName.startsWith('(')) {
                        testName = testName.substring(1);
                    }
                    if (testName.endsWith(')')) {
                        testName = testName.substring(0, testName.length - 1);
                    }
                    testName = path.parse(testName).name;
                    tests.push({
                        $: {
                            name: testName,
                            method: testName,
                            result: test.failure ? 'Fail' : 'Pass',
                            time: test.$.time
                        },
                        failure: [{
                                "stack-trace": test.failure ? test.failure[0]._ : '',
                                message: test.failure ? test.failure[0]._ : ''
                            }]
                    });
                });
                collection = {
                    $: {
                        name: suite.$.name,
                        failed: suite.$.failures,
                        skipped: suite.$.skipped,
                        time: suite.$.time,
                        passed: (parseInt(suite.$.tests) - parseInt(suite.$.failures) - parseInt(suite.$.skipped)).toString(),
                        total: suite.$.tests
                    },
                    test: tests
                };
                collections.push(collection);
            });
            results.push({
                $: {
                    "run-date": `${new Date().getFullYear()}-${new Date().getMonth() + 1}-${new Date().getDate()}`,
                    "run-time": `${new Date().toTimeString()}`,
                    "test-framework": "Page Scripting",
                    name: 'Page Scripts',
                    failed: resultObj.testsuites.$.failures,
                    skipped: resultObj.testsuites.$.skipped,
                    time: resultObj.testsuites.$.time,
                    passed: (parseInt(resultObj.testsuites.$.tests) - parseInt(resultObj.testsuites.$.failures) - parseInt(resultObj.testsuites.$.skipped)).toString(),
                    total: resultObj.testsuites.$.tests
                },
                collection: collections
            });
            resolve(results);
        }));
    });
}
// prior to running the test look for random placeholders in the test item and replace them with random values
function injectRandomValues(testItem, pageScripts) {
    testItem.children.forEach(child => {
        injectRandomValues(child, pageScripts);
    });
    if (!testItem.uri || !(0, fs_1.existsSync)(testItem.uri.fsPath)) {
        return;
    }
    let content = (0, fs_1.readFileSync)(testItem.uri.fsPath, { encoding: 'utf-8' });
    const originalContent = content;
    // Replace all RandText(x) with random strings of length x
    content = content.replace(/RandText\((\d+)\)/g, (_, len) => {
        const length = parseInt(len, 10);
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let result = '';
        for (let i = 0; i < length; i++) {
            result += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        return result;
    });
    (0, fs_1.writeFileSync)(testItem.uri.fsPath, content, { encoding: 'utf-8' });
    pageScripts.push({ testItem: testItem, content: originalContent });
}
function restorePageScriptContent(pageScripts) {
    pageScripts.forEach(pageScript => {
        (0, fs_1.writeFileSync)(pageScript.testItem.uri.fsPath, pageScript.content, { encoding: 'utf-8' });
    });
}
//# sourceMappingURL=pageScripting.js.map