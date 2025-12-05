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
exports.getCoverageEnabledForTestRunRequest = exports.getStatementCoverage = exports.getFileCoverage = exports.getALFilesInCoverage = exports.toggleCodeCoverageDisplay = exports.createCodeCoverageStatusBarItem = exports.getCodeCoveragePercentage = exports.filterCodeCoverageByLineNoRange = exports.filterCodeCoverageByObject = exports.saveTestRunCoverage = exports.saveAllTestsCodeCoverage = exports.getCodeCoveragePath = exports.readCodeCoverage = exports.updateCodeCoverageDecoration = void 0;
const vscode = require("vscode");
const alFileHelper_1 = require("./alFileHelper");
const fs_1 = require("fs");
const types_1 = require("./types");
const extension_1 = require("./extension");
const path_1 = require("path");
const config_1 = require("./config");
const pageScripting_1 = require("./pageScripting");
let codeCoverageStatusBarItem;
let codeCoverageDisplay = types_1.CodeCoverageDisplay.Off;
function updateCodeCoverageDecoration() {
    return __awaiter(this, void 0, void 0, function* () {
        if (!extension_1.activeEditor) {
            return;
        }
        const document = extension_1.activeEditor.document;
        let alObject = (0, alFileHelper_1.getALObjectOfDocument)(document);
        if (!alObject) {
            return;
        }
        let testedRanges = [];
        if (codeCoverageDisplay != types_1.CodeCoverageDisplay.Off) {
            let codeCoverage = yield readCodeCoverage(codeCoverageDisplay);
            codeCoverage = filterCodeCoverageByObject(codeCoverage, alObject);
            codeCoverage.forEach(element => {
                testedRanges.push(document.lineAt(parseInt(element.LineNo) - 1).range);
            });
        }
        extension_1.activeEditor.setDecorations(extension_1.passingTestDecorationType, testedRanges);
    });
}
exports.updateCodeCoverageDecoration = updateCodeCoverageDecoration;
function readCodeCoverage(codeCoverageDisplay, testRun) {
    return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
        let codeCoverage = [];
        let codeCoveragePath;
        if (testRun) {
            codeCoveragePath = getCoveragePathForTestRun(testRun);
        }
        else {
            codeCoveragePath = yield getCodeCoveragePath(codeCoverageDisplay);
        }
        if (codeCoveragePath) {
            if ((0, fs_1.existsSync)(codeCoveragePath)) {
                codeCoverage = JSON.parse((0, fs_1.readFileSync)(codeCoveragePath, { encoding: 'utf-8' }));
            }
        }
        resolve(codeCoverage);
    }));
}
exports.readCodeCoverage = readCodeCoverage;
function getCodeCoveragePath(codeCoverageType) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            if (codeCoverageType == types_1.CodeCoverageDisplay.All) {
                const path = yield getCodeCoveragePath(types_1.CodeCoverageDisplay.Previous);
                if (path) {
                    resolve((0, path_1.join)((0, path_1.dirname)(path), 'codeCoverageAll.json'));
                }
            }
            let config = vscode.workspace.getConfiguration('al-test-runner');
            if (config.codeCoveragePath) {
                const testFolderName = (0, alFileHelper_1.getTestFolderPath)();
                if (testFolderName) {
                    resolve((0, path_1.join)(testFolderName, config.codeCoveragePath));
                }
            }
            else {
                let discoveredPath = yield discoverCodeCoveragePath();
                resolve(discoveredPath);
            }
        }));
    });
}
exports.getCodeCoveragePath = getCodeCoveragePath;
function saveAllTestsCodeCoverage() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise(() => __awaiter(this, void 0, void 0, function* () {
            const path = yield getCodeCoveragePath(types_1.CodeCoverageDisplay.Previous);
            if (path) {
                const allTestsPath = yield getCodeCoveragePath(types_1.CodeCoverageDisplay.All);
                if (allTestsPath) {
                    (0, fs_1.copyFileSync)(path, allTestsPath);
                }
            }
        }));
    });
}
exports.saveAllTestsCodeCoverage = saveAllTestsCodeCoverage;
function saveTestRunCoverage(testRun) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const path = yield getCodeCoveragePath(types_1.CodeCoverageDisplay.Previous);
            if (path) {
                let testRunCoveragePath = getCoveragePathForTestRun(testRun);
                (0, fs_1.copyFileSync)(path, testRunCoveragePath);
            }
            resolve();
        }));
    });
}
exports.saveTestRunCoverage = saveTestRunCoverage;
function getCoveragePathForTestRun(testRun) {
    return (0, path_1.join)(require('os').tmpdir(), `codeCoverage${testRun.name}.json`);
}
function discoverCodeCoveragePath() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve, reject) => __awaiter(this, void 0, void 0, function* () {
            let codeCoverageFiles = yield vscode.workspace.findFiles(`**/**${getCodeCoverageFileName()}`);
            if (codeCoverageFiles.length > 0) {
                let codeCoveragePath = codeCoverageFiles.shift().fsPath;
                resolve(codeCoveragePath);
            }
            else {
                resolve(null);
            }
        }));
    });
}
function getCodeCoverageFileName() {
    try {
        let config = (0, config_1.getALTestRunnerConfig)();
        return (0, path_1.basename)(config.codeCoveragePath);
    }
    catch (_a) {
        return '';
    }
}
function filterCodeCoverageByObject(codeCoverage, alObject, includeZeroHits = false) {
    return codeCoverage.filter((element) => {
        return ((element.ObjectType.toLowerCase() === alObject.type.toLowerCase()) &&
            (parseInt(element.ObjectID) === alObject.id) &&
            ((parseInt(element.NoOfHits) !== 0) || includeZeroHits) &&
            (parseInt(element.LineNo) !== 0) &&
            (element.LineType === "Code"));
    });
}
exports.filterCodeCoverageByObject = filterCodeCoverageByObject;
function filterCodeCoverageByLineNoRange(codeCoverage, startLineNumber, endLineNumber, includeZeroHits = false) {
    return codeCoverage.filter(element => {
        const lineNumber = parseInt(element.LineNo);
        return (lineNumber >= startLineNumber && lineNumber <= endLineNumber &&
            (parseInt(element.NoOfHits) !== 0 || includeZeroHits) &&
            (element.LineType === "Code"));
    });
}
exports.filterCodeCoverageByLineNoRange = filterCodeCoverageByLineNoRange;
function getCoverageObjectFromCodeCoverage(codeCoverage, alFile) {
    let objectCoverage = filterCodeCoverageByObject(codeCoverage, alFile.object, true);
    let coverageObject = {
        file: alFile,
        noOfLines: objectCoverage.length,
        noOfHitLines: filterCodeCoverageByObject(objectCoverage, alFile.object, false).length
    };
    coverageObject.coverage = getCodeCoveragePercentageForCoverageObject(coverageObject);
    return coverageObject;
}
function getALObjectsFromCodeCoverage(codeCoverage) {
    let alObjects = [];
    let currentObject;
    let lastObject;
    codeCoverage.forEach(element => {
        currentObject = getALObjectFromCodeCoverageLine(element);
        if (JSON.stringify(currentObject) != JSON.stringify(lastObject)) {
            lastObject = getALObjectFromCodeCoverageLine(element);
            alObjects.push(lastObject);
        }
    });
    return alObjects;
}
function getALObjectFromCodeCoverageLine(codeCoverageLine) {
    return { id: parseInt(codeCoverageLine.ObjectID), type: codeCoverageLine.ObjectType };
}
function getCodeCoveragePercentageForCoverageObject(coverageObject) {
    return getCodeCoveragePercentage(coverageObject.noOfHitLines, coverageObject.noOfLines);
}
function getCodeCoveragePercentage(hitLines, totalLines) {
    if (totalLines == 0) {
        return 0;
    }
    else {
        return Math.round(hitLines / totalLines * 100);
    }
}
exports.getCodeCoveragePercentage = getCodeCoveragePercentage;
function createCodeCoverageStatusBarItem() {
    codeCoverageStatusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right);
    codeCoverageStatusBarItem.command = { command: 'altestrunner.toggleCodeCoverage', title: 'Toggle Code Coverage' };
    updateCodeCoverageStatusBarItemText(codeCoverageStatusBarItem);
    return codeCoverageStatusBarItem;
}
exports.createCodeCoverageStatusBarItem = createCodeCoverageStatusBarItem;
function updateCodeCoverageStatusBarItemText(statusBarItem) {
    statusBarItem.text = `Code Coverage: ${codeCoverageDisplay}`;
    if (codeCoverageDisplay == types_1.CodeCoverageDisplay.Off) {
        statusBarItem.backgroundColor = undefined;
    }
    else {
        statusBarItem.backgroundColor = new vscode.ThemeColor('statusBarItem.warningBackground');
    }
    statusBarItem.show();
}
function toggleCodeCoverageDisplay(newCodeCoverageDisplay) {
    if (newCodeCoverageDisplay) {
        if (codeCoverageDisplay == newCodeCoverageDisplay) {
            //so the user can click the coverage % code lens a second time to turn the coverage off
            codeCoverageDisplay = types_1.CodeCoverageDisplay.Off;
        }
        else {
            codeCoverageDisplay = newCodeCoverageDisplay;
        }
    }
    else {
        switch (codeCoverageDisplay) {
            case types_1.CodeCoverageDisplay.Off:
                codeCoverageDisplay = types_1.CodeCoverageDisplay.Previous;
                break;
            case types_1.CodeCoverageDisplay.Previous:
                codeCoverageDisplay = types_1.CodeCoverageDisplay.All;
                break;
            default:
                codeCoverageDisplay = types_1.CodeCoverageDisplay.Off;
                break;
        }
    }
    updateCodeCoverageStatusBarItemText(codeCoverageStatusBarItem);
    updateCodeCoverageDecoration();
}
exports.toggleCodeCoverageDisplay = toggleCodeCoverageDisplay;
function getALFilesInCoverage(codeCoverage) {
    if (!(codeCoverage)) {
        return [];
    }
    let alFiles = [];
    let alObjects = getALObjectsFromCodeCoverage(codeCoverage);
    alObjects.forEach(alObject => {
        let alFile = (0, alFileHelper_1.getALFileForALObject)(alObject);
        if (alFile) {
            alFiles.push(alFile);
        }
    });
    return alFiles;
}
exports.getALFilesInCoverage = getALFilesInCoverage;
function getFileCoverage(codeCoverage, alFile) {
    let coverageObject = getCoverageObjectFromCodeCoverage(codeCoverage, alFile);
    return new vscode.FileCoverage(vscode.Uri.file(alFile.path), new vscode.TestCoverageCount(coverageObject.noOfHitLines, coverageObject.noOfLines));
}
exports.getFileCoverage = getFileCoverage;
function getStatementCoverage(codeCoverage, alFile) {
    let statementCoverage = [];
    if (alFile.object) {
        filterCodeCoverageByObject(codeCoverage, alFile.object, false).forEach(codeCoverageLine => {
            statementCoverage.push(new vscode.StatementCoverage(parseInt(codeCoverageLine.NoOfHits), new vscode.Range(parseInt(codeCoverageLine.LineNo) - 1, 0, parseInt(codeCoverageLine.LineNo) - 1, 0)));
        });
    }
    return statementCoverage;
}
exports.getStatementCoverage = getStatementCoverage;
function getCoverageEnabledForTestRunRequest(request) {
    const codeCoverage = (0, config_1.getCurrentWorkspaceConfig)().enableCodeCoverage;
    if (request.include === undefined) { //all tests
        return codeCoverage == types_1.enableCodeCoverage.Always || codeCoverage == types_1.enableCodeCoverage['When running all tests'];
    }
    else {
        const testItem = request.include[0];
        if ((0, pageScripting_1.testItemIsPageScript)(testItem)) {
            return false;
        }
        else { //selection of one or more tests
            return codeCoverage == types_1.enableCodeCoverage.Always.toString();
        }
    }
}
exports.getCoverageEnabledForTestRunRequest = getCoverageEnabledForTestRunRequest;
//# sourceMappingURL=coverage.js.map