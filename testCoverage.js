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
exports.runRelatedTests = exports.showRelatedTests = exports.getTestCoverageForMethod = exports.buildTestCoverage = exports.readTestCoverage = exports.buildTestCoverageFromTestItem = exports.testCoverage = void 0;
const vscode = require("vscode");
const alFileHelper_1 = require("./alFileHelper");
const coverage_1 = require("./coverage");
const extension_1 = require("./extension");
const path_1 = require("path");
const fs_1 = require("fs");
const output_1 = require("./output");
const testController_1 = require("./testController");
const telemetry_1 = require("./telemetry");
exports.testCoverage = [];
readTestCoverage();
function buildTestCoverageFromTestItem(testItem) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const testMethod = { objectName: testItem.parent.label, methodName: testItem.label };
            const codeCoverage = yield (0, coverage_1.readCodeCoverage)();
            buildTestCoverage(codeCoverage, testMethod).then(newCoverage => {
                writeTestCoverage(testMethod, newCoverage);
            });
            resolve();
        }));
    });
}
exports.buildTestCoverageFromTestItem = buildTestCoverageFromTestItem;
function writeTestCoverage(testMethod, newCoverage) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const path = yield getTestCoveragePath();
            let existingCoverage = excludeCoverageForMethod(testMethod);
            const mergedCoverage = addNewCoverage(existingCoverage, newCoverage);
            (0, fs_1.writeFileSync)(path, JSON.stringify(mergedCoverage, null, 2));
            exports.testCoverage = mergedCoverage;
            resolve();
        }));
    });
}
function excludeCoverageForMethod(method) {
    return exports.testCoverage.filter(test => {
        return (test.testMethod.objectName !== method.objectName || test.testMethod.methodName !== method.methodName);
    });
}
function addNewCoverage(existingCoverage, newCoverage) {
    newCoverage.forEach(element => {
        existingCoverage.push(element);
    });
    return existingCoverage;
}
function readTestCoverage() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const path = yield getTestCoveragePath();
            if ((0, fs_1.existsSync)(path)) {
                const text = (0, fs_1.readFileSync)(path, { encoding: 'utf-8' });
                exports.testCoverage = JSON.parse(text);
            }
            else {
                exports.testCoverage = [];
            }
            resolve();
        }));
    });
}
exports.readTestCoverage = readTestCoverage;
function getTestCoveragePath() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const codeCoveragePath = yield (0, coverage_1.getCodeCoveragePath)();
            if (codeCoveragePath) {
                resolve((0, path_1.join)((0, path_1.dirname)(codeCoveragePath), 'testCoverage.json'));
            }
        }));
    });
}
function buildTestCoverage(codeCoverage, testMethod) {
    return new Promise(resolve => {
        let thisCoverage = [];
        let methodIncluded = false;
        codeCoverage.forEach((line, index) => __awaiter(this, void 0, void 0, function* () {
            if (!methodIncluded) {
                if (parseInt(line.NoOfHits) != 0) {
                    const methodLine = getPreviousMethodLine(codeCoverage, index);
                    if (methodLine) {
                        methodIncluded = true;
                        const alFile = getALFileForCodeCoverageLine(line);
                        if (alFile) {
                            if (!alFile.excludeFromCodeCoverage) {
                                const document = yield vscode.workspace.openTextDocument(alFile.path);
                                const methodName = yield (0, alFileHelper_1.getMethodNameFromDocumentAndLine)(document, parseInt(methodLine.LineNo));
                                const test = {
                                    method: { objectName: alFile.object.name, methodName: methodName, object: alFile.object },
                                    testMethod: testMethod
                                };
                                thisCoverage.push(test);
                            }
                        }
                    }
                }
            }
            if (line.LineType == 'Trigger/Function') {
                methodIncluded = false;
            }
            if (index == codeCoverage.length - 1) {
                resolve(thisCoverage);
            }
        }));
    });
}
exports.buildTestCoverage = buildTestCoverage;
function getALFileForCodeCoverageLine(codeCoverageLine) {
    const matchingFiles = extension_1.alFiles.filter(file => {
        if (file.object) {
            return (file.object.id == parseInt(codeCoverageLine.ObjectID) && file.object.type == codeCoverageLine.ObjectType.toLowerCase());
        }
    });
    if (matchingFiles) {
        return matchingFiles[0];
    }
}
function getPreviousMethodLine(codeCoverage, index) {
    for (let i = index - 1; i >= 0; i--) {
        if (codeCoverage[i].LineType === 'Trigger/Function') {
            return codeCoverage[i];
        }
    }
}
function getTestCoverageForMethod(method) {
    return exports.testCoverage.filter(element => {
        return (element.method.objectName == method.objectName && element.method.methodName == method.methodName);
    });
}
exports.getTestCoverageForMethod = getTestCoverageForMethod;
function showRelatedTests(method) {
    return __awaiter(this, void 0, void 0, function* () {
        if (!method) {
            return;
        }
        (0, telemetry_1.sendShowRelatedTestsEvent)();
        const relatedTestMethods = yield getRelatedTests(method);
        (0, output_1.writeTable)(extension_1.channelWriter, relatedTestMethods, ["objectName", "methodName", "path"], true, true, `${method.objectName}.${method.methodName} tested by:`, ["Codeunit", "Test", "Path"]);
        extension_1.channelWriter.write(' ');
        extension_1.channelWriter.write(`${relatedTestMethods.length} test(s) call ${method.methodName}.`);
        extension_1.channelWriter.write('The test coverage map is updated when single tests are run and when code coverage is enabled. For more information see https://jimmymcp.github.io/al-test-runner-docs/articles/test-coverage.html');
        extension_1.channelWriter.show();
    });
}
exports.showRelatedTests = showRelatedTests;
function runRelatedTests(method) {
    return __awaiter(this, void 0, void 0, function* () {
        if (!method) {
            return;
        }
        let testItems = [];
        const relatedTests = yield getRelatedTests(method);
        relatedTests.forEach(test => {
            const testItem = (0, testController_1.getTestItemForMethod)(test);
            if (testItem) {
                testItems.push(testItem);
            }
        });
        if (testItems.length > 0) {
            vscode.window.showInformationMessage(`Running ${testItems.length} test(s) related to ${method.methodName}`);
            const request = new vscode.TestRunRequest(testItems);
            (0, testController_1.runTestHandler)(request);
        }
    });
}
exports.runRelatedTests = runRelatedTests;
function getRelatedTests(method) {
    return __awaiter(this, void 0, void 0, function* () {
        const files = yield (0, alFileHelper_1.getALFilesInWorkspace)();
        return new Promise(resolve => {
            let relatedTestMethods = [];
            const testCoverages = getTestCoverageForMethod(method);
            testCoverages.forEach((testCoverage, index) => __awaiter(this, void 0, void 0, function* () {
                const path = yield (0, alFileHelper_1.getFilePathOfObject)({ type: 'codeunit', id: 0, name: testCoverage.testMethod.objectName }, testCoverage.testMethod.methodName, files);
                relatedTestMethods.push({ objectName: testCoverage.testMethod.objectName, methodName: testCoverage.testMethod.methodName, path: path });
                if (index == testCoverages.length - 1) {
                    resolve(relatedTestMethods);
                }
            }));
        });
    });
}
//# sourceMappingURL=testCoverage.js.map