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
exports.getTestItemForMethod = exports.getTestItemsIncludedInRequest = exports.getTestCodeunitsIncludedInRequest = exports.getDisabledTestsForRequest = exports.deleteTestItemForFilename = exports.getTestItemFromFileNameAndSelection = exports.debugTest = exports.debugTestHandler = exports.runSelectedTests = exports.runAllTests = exports.runTest = exports.readyToRunTests = exports.runTestHandler = exports.discoverTestsInDocument = exports.discoverTestsInFileName = exports.discoverTests = exports.createTestController = exports.numberOfTests = void 0;
const vscode = require("vscode");
const alFileHelper_1 = require("./alFileHelper");
const config_1 = require("./config");
const extension_1 = require("./extension");
const types_1 = require("./types");
const path = require("path");
const telemetry_1 = require("./telemetry");
const testCoverage_1 = require("./testCoverage");
const coverage_1 = require("./coverage");
const debug_1 = require("./debug");
const pageScripting_1 = require("./pageScripting");
function createTestController(controllerId = 'alTestController') {
    const alTestController = vscode.tests.createTestController(controllerId, 'AL Tests');
    const profile = alTestController.createRunProfile('Run', vscode.TestRunProfileKind.Run, request => {
        runTestHandler(request);
    });
    profile.loadDetailedCoverage = (testRun, fileCoverage, token) => __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            let alFile = {
                path: fileCoverage.uri.fsPath,
                object: (0, alFileHelper_1.getALObjectFromPath)(fileCoverage.uri.fsPath),
                excludeFromCodeCoverage: false
            };
            resolve((0, coverage_1.getStatementCoverage)(yield (0, coverage_1.readCodeCoverage)(types_1.CodeCoverageDisplay.All, testRun), alFile));
        }));
    });
    alTestController.createRunProfile('Debug', vscode.TestRunProfileKind.Debug, request => {
        debugTestHandler(request);
    });
    alTestController.refreshHandler = () => __awaiter(this, void 0, void 0, function* () { discoverTests(); });
    return alTestController;
}
exports.createTestController = createTestController;
function discoverTests() {
    return __awaiter(this, void 0, void 0, function* () {
        exports.numberOfTests = 0;
        const alFiles = yield (0, alFileHelper_1.getALFilesInWorkspace)();
        alFiles.forEach((alFile) => __awaiter(this, void 0, void 0, function* () {
            const document = yield vscode.workspace.openTextDocument(alFile.path);
            discoverTestsInDocument(document);
        }));
        const pageScripts = yield (0, pageScripting_1.discoverPageScripts)(extension_1.alTestController);
        const pageScriptsItem = extension_1.alTestController.createTestItem('Page Scripts', 'Page Scripts');
        pageScripts.forEach(pageScript => {
            pageScriptsItem.children.add(pageScript);
        });
        extension_1.alTestController.items.add(pageScriptsItem);
    });
}
exports.discoverTests = discoverTests;
function discoverTestsInFileName(fileName) {
    return __awaiter(this, void 0, void 0, function* () {
        const document = yield vscode.workspace.openTextDocument(fileName);
        discoverTestsInDocument(document);
    });
}
exports.discoverTestsInFileName = discoverTestsInFileName;
function discoverTestsInDocument(document) {
    return __awaiter(this, void 0, void 0, function* () {
        if ((0, alFileHelper_1.documentIsTestCodeunit)(document)) {
            const alFiles = yield (0, alFileHelper_1.getALFilesInWorkspace)('', `**/${path.basename(document.uri.fsPath)}`);
            let alFile;
            if (alFiles) {
                alFile = alFiles.shift();
                let codeunitItem = yield getTestItemFromFileNameAndSelection(document.uri.fsPath, 0);
                if (codeunitItem === undefined) {
                    codeunitItem = extension_1.alTestController.createTestItem(alFile.object.name, alFile.object.name, document.uri);
                }
                codeunitItem.children.forEach(test => {
                    codeunitItem.children.delete(test.id);
                    exports.numberOfTests -= 1;
                });
                (0, alFileHelper_1.getTestMethodRangesFromDocument)(document).forEach(testRange => {
                    const testItem = extension_1.alTestController.createTestItem(testRange.name, testRange.name, document.uri);
                    testItem.range = testRange.range;
                    codeunitItem.children.add(testItem);
                    exports.numberOfTests += 1;
                });
                extension_1.alTestController.items.add(codeunitItem);
            }
        }
    });
}
exports.discoverTestsInDocument = discoverTestsInDocument;
function runTestHandler(request) {
    return __awaiter(this, void 0, void 0, function* () {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const run = extension_1.alTestController.createTestRun(request, timestamp);
        (0, telemetry_1.sendTestRunStartEvent)(request);
        let results;
        if (request.include === undefined) {
            results = yield runAllTests(request);
            (0, coverage_1.saveAllTestsCodeCoverage)();
        }
        else if (request.include.length > 1) {
            results = yield runSelectedTests(request);
        }
        else {
            const testItem = request.include[0];
            if ((0, pageScripting_1.testItemIsPageScript)(testItem)) {
                results = yield (0, pageScripting_1.runPageScript)(testItem);
            }
            else {
                let lineNumber = 0;
                let filename;
                if (testItem.parent) {
                    lineNumber = testItem.range.start.line;
                    filename = testItem.parent.uri.fsPath;
                }
                else {
                    filename = testItem.uri.fsPath;
                }
                results = yield runTest(request, filename, lineNumber);
                (0, testCoverage_1.buildTestCoverageFromTestItem)(testItem);
            }
        }
        setResultsForTestItems(results, request, run);
        if ((0, coverage_1.getCoverageEnabledForTestRunRequest)(request)) {
            yield (0, coverage_1.saveTestRunCoverage)(run);
            const codeCoverage = yield (0, coverage_1.readCodeCoverage)(types_1.CodeCoverageDisplay.All, run);
            (0, coverage_1.getALFilesInCoverage)(codeCoverage).forEach(alFile => {
                run.addCoverage((0, coverage_1.getFileCoverage)(codeCoverage, alFile));
            });
        }
        run.end();
        (0, telemetry_1.sendTestRunFinishedEvent)(request);
        if (results.length > 0) {
            outputTestResults(results);
        }
    });
}
exports.runTestHandler = runTestHandler;
function setResultsForTestItems(results, request, run) {
    if (results.length == 0) {
        return;
    }
    let testItems = [];
    if (request.include) {
        request.include.forEach(testItem => {
            testItems.push(testItem);
        });
    }
    else {
        extension_1.alTestController.items.forEach(testCodeunit => {
            if (!(0, pageScripting_1.testItemIsPageScript)(testCodeunit)) {
                testItems.push(testCodeunit);
            }
        });
    }
    testItems.forEach(testItem => {
        if (testItem.parent) {
            const result = getResultForTestItem(results, testItem, testItem.parent);
            setResultForTestItem(result, testItem, run);
        }
        else {
            testItem.children.forEach(test => {
                const result = getResultForTestItem(results, test, testItem);
                setResultForTestItem(result, test, run);
            });
        }
    });
}
function readyToRunTests() {
    return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
        (0, telemetry_1.sendDebugEvent)('readyToRunTests-start');
        if ((0, config_1.launchConfigIsValid)() == types_1.launchConfigValidity.Invalid) {
            (0, telemetry_1.sendDebugEvent)('readyToRunTests-launchConfigNotValid');
            //clear the credentials and company name if the launch config is not valid
            (0, config_1.setALTestRunnerConfig)('userName', '');
            (0, config_1.setALTestRunnerConfig)('securePassword', '');
            (0, config_1.setALTestRunnerConfig)('companyName', '');
            (0, config_1.setALTestRunnerConfig)('testRunnerServiceUrl', '');
            yield (0, config_1.selectLaunchConfig)();
        }
        if ((0, config_1.launchConfigIsValid)() == types_1.launchConfigValidity.Valid) {
            (0, telemetry_1.sendDebugEvent)('readyToRunTests-launchConfigIsValid');
            resolve(true);
        }
        else {
            resolve(false);
        }
    }));
}
exports.readyToRunTests = readyToRunTests;
function runTest(request, filename, selectionStart, extensionId, extensionName) {
    return __awaiter(this, void 0, void 0, function* () {
        (0, telemetry_1.sendDebugEvent)('runTest-start', { filename: filename ? filename : 'undefined', selectionStart: selectionStart ? selectionStart.toString() : '0', extensionId: extensionId ? extensionId : 'undefined', extensionName: extensionName ? extensionName : 'undefined' });
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            yield readyToRunTests().then((ready) => __awaiter(this, void 0, void 0, function* () {
                if (ready) {
                    if (filename === undefined) {
                        filename = vscode.window.activeTextEditor.document.fileName;
                    }
                    if (selectionStart === undefined) {
                        selectionStart = vscode.window.activeTextEditor.selection.start.line;
                    }
                    if (extensionId === undefined) {
                        extensionId = (0, extension_1.getAppJsonKey)('id');
                    }
                    if (extensionName === undefined) {
                        extensionName = (0, extension_1.getAppJsonKey)('name');
                    }
                    (0, telemetry_1.sendDebugEvent)('runTest-ready', { filename: filename, selectionStart: selectionStart.toString(), extensionId: extensionId, extensionName: extensionName });
                    let command = `Invoke-ALTestRunner -Tests Test -ExtensionId "${extensionId}" -ExtensionName "${extensionName}" -FileName "${filename}" -SelectionStart ${selectionStart} -LaunchConfig '${(0, config_1.getLaunchConfiguration)((0, config_1.getALTestRunnerConfig)().launchConfigName)}'`;
                    command = addOptionalRunTestParameters(command);
                    const codeCoverageEnabled = (0, coverage_1.getCoverageEnabledForTestRunRequest)(request);
                    const results = yield (0, extension_1.invokeTestRunner)(command, { enableCodeCoverage: codeCoverageEnabled });
                    resolve(results);
                }
                else {
                    resolve([]);
                }
            }));
        }));
    });
}
exports.runTest = runTest;
;
function runAllTests(request, extensionId, extensionName) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            yield readyToRunTests().then((ready) => __awaiter(this, void 0, void 0, function* () {
                if (ready) {
                    if (extensionId === undefined) {
                        extensionId = (0, extension_1.getAppJsonKey)('id');
                    }
                    if (extensionName === undefined) {
                        extensionName = (0, extension_1.getAppJsonKey)('name');
                    }
                    (0, telemetry_1.sendDebugEvent)('runAllTests-ready');
                    let command = `Invoke-ALTestRunner -Tests All -ExtensionId "${extensionId}" -ExtensionName "${extensionName}" -LaunchConfig '${(0, config_1.getLaunchConfiguration)((0, config_1.getALTestRunnerConfig)().launchConfigName)}'`;
                    command = addOptionalRunTestParameters(command);
                    const codeCoverageEnabled = (0, coverage_1.getCoverageEnabledForTestRunRequest)(request);
                    const results = yield (0, extension_1.invokeTestRunner)(command, { enableCodeCoverage: codeCoverageEnabled });
                    resolve(results);
                }
                else {
                    resolve([]);
                }
            }));
        }));
    });
}
exports.runAllTests = runAllTests;
function runSelectedTests(request, extensionId, extensionName) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            yield readyToRunTests().then((ready) => __awaiter(this, void 0, void 0, function* () {
                if (ready) {
                    if (extensionId === undefined) {
                        extensionId = (0, extension_1.getAppJsonKey)('id');
                    }
                    if (extensionName === undefined) {
                        extensionName = (0, extension_1.getAppJsonKey)('name');
                    }
                    (0, telemetry_1.sendDebugEvent)('runSelectedTests-ready');
                    const disabledTests = getDisabledTestsForRequest(request);
                    const disabledTestsJson = JSON.stringify(disabledTests);
                    let command = `Invoke-ALTestRunner -Tests All -ExtensionId "${extensionId}" -ExtensionName "${extensionName}" -DisabledTests ('${disabledTestsJson}' | ConvertFrom-Json) -LaunchConfig '${(0, config_1.getLaunchConfiguration)((0, config_1.getALTestRunnerConfig)().launchConfigName)}'`;
                    command = addOptionalRunTestParameters(command);
                    const codeCoverageEnabled = (0, coverage_1.getCoverageEnabledForTestRunRequest)(request);
                    const results = yield (0, extension_1.invokeTestRunner)(command, { enableCodeCoverage: codeCoverageEnabled });
                    resolve(results);
                }
                else {
                    resolve([]);
                }
            }));
        }));
    });
}
exports.runSelectedTests = runSelectedTests;
function addOptionalRunTestParameters(command) {
    if ((0, config_1.getCurrentWorkspaceConfig)().runTestsViaUrl) {
        command += ' -RunViaURL';
    }
    return command;
}
function debugTestHandler(request) {
    return __awaiter(this, void 0, void 0, function* () {
        if (request.include) {
            const testItem = request.include[0];
            let filename;
            let lineNumber;
            if (testItem.parent) {
                filename = testItem.parent.uri.fsPath;
                lineNumber = testItem.range.start.line;
            }
            else {
                filename = testItem.uri.fsPath;
                lineNumber = 0;
            }
            (0, telemetry_1.sendTestDebugStartEvent)(request);
            debugTest(filename, lineNumber);
        }
        else {
            debugTest('', 0);
        }
    });
}
exports.debugTestHandler = debugTestHandler;
function debugTest(filename, selectionStart) {
    return __awaiter(this, void 0, void 0, function* () {
        if (filename === undefined) {
            filename = vscode.window.activeTextEditor.document.fileName;
        }
        if (selectionStart === undefined) {
            selectionStart = vscode.window.activeTextEditor.selection.start.line;
        }
        const ready = yield (0, debug_1.readyToDebug)();
        if (!ready) {
            vscode.window.showErrorMessage('AL Test Runner is not ready to debug. Please check that the Test Runner Service app is installed and the testRunnerServiceUrl in config.json is correct.');
        }
        yield (0, extension_1.attachDebugger)();
        (0, extension_1.invokeDebugTest)(filename, selectionStart);
    });
}
exports.debugTest = debugTest;
function setResultForTestItem(result, testItem, run) {
    if (result.$.result == 'Pass') {
        run.passed(testItem);
    }
    else {
        run.failed(testItem, new vscode.TestMessage(`${result.failure[0].message[0]}\n\n${result.failure[0]["stack-trace"][0]}`));
    }
}
function getResultForTestItem(results, testItem, parent) {
    const assemblyName = parent.label.substring(1, parent.label.length - 1);
    let returnResult = { $: { method: testItem.label, name: testItem.label, result: 'none', time: '0' }, failure: [{ message: '', 'stack-trace': '' }] };
    ;
    results.forEach(assembly => {
        if (assembly.$.name.includes(assemblyName)) {
            assembly.collection.forEach(collection => {
                collection.test.forEach(result => {
                    if (result.$.method === testItem.label) {
                        returnResult = result;
                    }
                });
            });
        }
    });
    return returnResult;
}
function getTestItemFromFileNameAndSelection(filename, selectionStart) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            if (filename === undefined) {
                filename = vscode.window.activeTextEditor.document.fileName;
            }
            if (selectionStart === undefined) {
                selectionStart = vscode.window.activeTextEditor.selection.start.line;
            }
            const document = yield vscode.workspace.openTextDocument(filename);
            const object = (0, alFileHelper_1.getALObjectOfDocument)(document);
            if (object) {
                const codeunitItem = extension_1.alTestController.items.get(object.name);
                if (selectionStart === 0) {
                    resolve(codeunitItem);
                    return;
                }
                let testMethodRanges = (0, alFileHelper_1.getTestMethodRangesFromDocument)(document);
                testMethodRanges = testMethodRanges.filter(range => {
                    if (range.range.start.line <= selectionStart) {
                        return true;
                    }
                });
                if (testMethodRanges.length > 0) {
                    const testMethod = testMethodRanges.pop();
                    const testItem = codeunitItem.children.get(testMethod.name);
                    resolve(testItem);
                }
            }
            else {
                resolve(undefined);
            }
        }));
    });
}
exports.getTestItemFromFileNameAndSelection = getTestItemFromFileNameAndSelection;
function deleteTestItemForFilename(filename) {
    return __awaiter(this, void 0, void 0, function* () {
        const testItem = yield getTestItemFromFileNameAndSelection(filename, 0);
        if (testItem) {
            extension_1.alTestController.items.delete(testItem.id);
        }
    });
}
exports.deleteTestItemForFilename = deleteTestItemForFilename;
function getDisabledTestsForRequest(request, testContoller) {
    let disabledTests = [];
    let testCodeunitsToRun = getTestCodeunitsIncludedInRequest(request);
    let controller;
    if (testContoller) {
        controller = testContoller;
    }
    else {
        controller = extension_1.alTestController;
    }
    if (!controller) {
        return disabledTests;
    }
    if (!controller.items) {
        return disabledTests;
    }
    //tests which are in codeunits where some tests are included, but the tests themselves are not included
    testCodeunitsToRun.forEach(testCodeunit => {
        var _a;
        //unless the codeunit itself is included, then iterate over its children to test which ones need to be disabled
        if (((_a = request.include) === null || _a === void 0 ? void 0 : _a.indexOf(testCodeunit)) == -1) {
            testCodeunit.children.forEach(testItem => {
                var _a;
                if (((_a = request.include) === null || _a === void 0 ? void 0 : _a.indexOf(testItem)) == -1) {
                    disabledTests.push({ codeunitName: testCodeunit.label, method: testItem.label });
                }
            });
        }
    });
    //test codeunits where none of their tests are included
    controller.items.forEach(testCodeunit => {
        if (testCodeunitsToRun.indexOf(testCodeunit) == -1) {
            disabledTests.push({ codeunitName: testCodeunit.label, method: '*' });
        }
    });
    return disabledTests;
}
exports.getDisabledTestsForRequest = getDisabledTestsForRequest;
function getTestCodeunitsIncludedInRequest(request) {
    let testCodeunits = [];
    if (request.include) {
        request.include.forEach(testItem => {
            if (testItem.children.size > 0) {
                testCodeunits.push(testItem);
            }
            if (testItem.parent) {
                if (testCodeunits.indexOf(testItem.parent) == -1) {
                    testCodeunits.push(testItem.parent);
                }
            }
        });
    }
    return testCodeunits;
}
exports.getTestCodeunitsIncludedInRequest = getTestCodeunitsIncludedInRequest;
function getTestItemsIncludedInRequest(request) {
    let testItems = [];
    if (request.include) {
        //iterate through the test items with children (i.e. the test codeunits) first
        //add all the children of each included codeunit
        request.include.filter(testItem => {
            return !testItem.parent;
        }).forEach(testCodeunit => {
            if (testCodeunit.children) {
                testCodeunit.children.forEach(testItem => {
                    testItems.push(testItem);
                });
            }
        });
        //then add any included children as long as they are not already in the collection
        request.include.filter(testItem => {
            return testItem.parent;
        }).forEach(testItem => {
            if (testItems.indexOf(testItem) == -1) {
                testItems.push(testItem);
            }
        });
    }
    return testItems;
}
exports.getTestItemsIncludedInRequest = getTestItemsIncludedInRequest;
function getTestItemForMethod(method) {
    let testCodeunit = extension_1.alTestController.items.get(method.objectName);
    if (testCodeunit) {
        return testCodeunit.children.get(method.methodName);
    }
}
exports.getTestItemForMethod = getTestItemForMethod;
function outputTestResults(assemblies) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            let noOfTests = 0;
            let noOfFailures = 0;
            let noOfSkips = 0;
            let totalTime = 0;
            if (assemblies.length > 0) {
                extension_1.outputWriter.clear();
            }
            for (let assembly of assemblies) {
                noOfTests += parseInt(assembly.$.total);
                const assemblyTime = parseFloat(assembly.$.time);
                totalTime += assemblyTime;
                const failed = parseInt(assembly.$.failed);
                noOfFailures += failed;
                const skipped = parseInt(assembly.$.skipped);
                noOfSkips += skipped;
                if (failed > 0) {
                    extension_1.outputWriter.write('❌ ' + assembly.$.name + '\t' + assemblyTime.toFixed(2) + 's');
                }
                else {
                    extension_1.outputWriter.write('✅ ' + assembly.$.name + '\t' + assemblyTime.toFixed(2) + 's');
                }
                for (let test of assembly.collection[0].test) {
                    const testTime = parseFloat(test.$.time);
                    let filePath = '';
                    const codeunitName = assembly.$.name.substring(assembly.$.name.indexOf(' ') + 1);
                    switch (test.$.result) {
                        case 'Pass':
                            extension_1.outputWriter.write('\t✅ ' + test.$.method + '\t' + testTime.toFixed(2) + 's');
                            break;
                        case 'Skip':
                            filePath = assembly.$.name == 'Page Scripts' ? '' : yield (0, alFileHelper_1.getFilePathOfObject)({ type: 'codeunit', id: 0, name: codeunitName }, test.$.method);
                            extension_1.outputWriter.write('\t❓ ' + test.$.method + '\t' + testTime.toFixed(2) + 's ' + filePath);
                            break;
                        case 'Fail':
                            filePath = assembly.$.name == 'Page Scripts' ? '' : yield (0, alFileHelper_1.getFilePathOfObject)({ type: 'codeunit', id: 0, name: codeunitName }, test.$.method);
                            extension_1.outputWriter.write('\t❌ ' + test.$.method + '\t' + testTime.toFixed(2) + "s " + filePath);
                            extension_1.outputWriter.write('\t\t' + test.failure[0].message);
                            break;
                        default:
                            break;
                    }
                }
            }
            let statusBarItem = vscode.window.createStatusBarItem('altestrunner.summary', vscode.StatusBarAlignment.Right);
            let summaryText, backgroundColor;
            if ((noOfFailures + noOfSkips) === 0) {
                summaryText = `✅ ${noOfTests} test(s) ran in ${totalTime.toFixed(2)}s at ${assemblies[0].$["run-time"]}`;
                backgroundColor = 'statusBarItem.prominentBackground';
            }
            else {
                summaryText = `❌ ${noOfTests} test(s) ran in ${totalTime.toFixed(2)}s - ${noOfFailures + noOfSkips} test(s) failed/skipped at ${assemblies[0].$["run-time"]}`;
                backgroundColor = 'statusBarItem.errorBackground';
            }
            extension_1.outputWriter.write(summaryText);
            statusBarItem.text = summaryText;
            statusBarItem.backgroundColor = new vscode.ThemeColor(backgroundColor);
            statusBarItem.command = 'workbench.view.testing.focus';
            statusBarItem.show();
            setTimeout(() => {
                statusBarItem.dispose();
            }, 10000);
            extension_1.outputWriter.show();
            resolve(true);
        }));
    });
}
//# sourceMappingURL=testController.js.map