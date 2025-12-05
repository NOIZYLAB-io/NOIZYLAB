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
exports.getCommentLinesForTestItem = exports.pasalCaseToSentenceCase = exports.getDevOpsTestStepsForTestItems = exports.exportTestItemsToCsv = void 0;
const vscode = require("vscode");
const config_1 = require("./config");
function exportTestItemsToCsv(testItem) {
    return __awaiter(this, void 0, void 0, function* () {
        const testSteps = yield getDevOpsTestStepsForTestItems(testItem);
        const csv = convertTestStepsToCsv(testSteps);
        saveCsvToFile(csv, testItem.label);
    });
}
exports.exportTestItemsToCsv = exportTestItemsToCsv;
function getDevOpsTestStepsForTestItems(testItem) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            if (testItem == undefined) {
                resolve([]);
                return;
            }
            let testSteps = [];
            if (testItem.children.size > 0) {
                let children = [];
                testItem.children.forEach(child => {
                    children.push(child);
                });
                // for...of loop forces the code to wait for the promise to resolve before continuing
                for (let child of children) {
                    const childTestSteps = yield getDevOpsTestStepsForTestItems(child);
                    testSteps = testSteps.concat(childTestSteps);
                }
                resolve(testSteps);
                return;
            }
            testSteps.push({
                ID: '',
                "Work Item Type": 'Test Case',
                Title: pasalCaseToSentenceCase(testItem.label),
                "Test Step": '',
                "Step Action": '',
                "Step Expected": '',
            });
            let testStepNumber = 0;
            const commentLines = yield getCommentLinesForTestItem(testItem);
            commentLines.forEach(commentLine => {
                testStepNumber++;
                if (commentLine.startsWith('//[GIVEN]') || commentLine.startsWith('//[WHEN]')) {
                    const lineType = capitaliseFirstCharacter(commentLine.substring(3, commentLine.indexOf(']')).toLowerCase());
                    const stepAction = `${lineType} ${commentLine.substring(commentLine.indexOf(']') + 1).trim()}`;
                    testSteps.push({
                        ID: '',
                        "Work Item Type": '',
                        Title: '',
                        "Test Step": testStepNumber.toString(),
                        "Step Action": stepAction,
                        "Step Expected": '',
                    });
                }
                else {
                    const stepExpected = commentLine.substring(commentLine.indexOf(']') + 1).trim();
                    let testStep = testSteps[testSteps.length - 1];
                    if (testStep['Step Expected'] != '') {
                        testStep['Step Expected'] += '\n';
                    }
                    testStep['Step Expected'] += `Then ${stepExpected}`;
                    testSteps[testSteps.length - 1] = testStep;
                }
            });
            resolve(testSteps);
        }));
    });
}
exports.getDevOpsTestStepsForTestItems = getDevOpsTestStepsForTestItems;
function capitaliseFirstCharacter(text) {
    return text.charAt(0).toUpperCase() + text.slice(1);
}
function pasalCaseToSentenceCase(pascalCase, acronymsToKeep) {
    let sentenceCase = pascalCase.replace(/([A-Z])/g, ' $1').trim();
    if (!acronymsToKeep) {
        acronymsToKeep = (0, config_1.getCurrentWorkspaceConfig)().testNameAcronyms;
    }
    if (acronymsToKeep) {
        acronymsToKeep.forEach(acronym => {
            if (pascalCase.includes(acronym)) {
                let splitAcronym = acronym.replace(/([A-Z])/g, ' $1').trim();
                sentenceCase = sentenceCase.replace(splitAcronym, acronym);
            }
        });
    }
    return sentenceCase;
}
exports.pasalCaseToSentenceCase = pasalCaseToSentenceCase;
function getCommentLinesForTestItem(testItem) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            let commentLines = [];
            const testText = yield getTextOfTestItem(testItem);
            //find the lines that start with '//'
            testText.forEach(line => {
                if (line.trimStart().startsWith('//')) {
                    commentLines.push(line.trimStart());
                }
            });
            resolve(commentLines);
        }));
    });
}
exports.getCommentLinesForTestItem = getCommentLinesForTestItem;
function getTextOfTestItem(testItem) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise(resolve => {
            vscode.workspace.openTextDocument(testItem.uri).then((document) => __awaiter(this, void 0, void 0, function* () {
                //get a range which starts at the testitem range and ends at the end of the document
                const range = new vscode.Range(testItem.range.start, document.lineAt(document.lineCount - 1).range.end);
                const documentText = yield document.getText(range);
                //find the next occurence of "    end;"
                const regEx = /\n    end;/;
                const match = regEx.exec(documentText);
                if (match) {
                    resolve(documentText.substring(0, match.index).split('\n'));
                }
                else {
                    resolve([]);
                }
            }));
        });
    });
}
function convertTestStepsToCsv(testSteps) {
    let csv = 'ID,Work Item Type,Title,Test Step,Step Action,Step Expected\n';
    testSteps.forEach(testStep => {
        csv += `"${testStep.ID}","${testStep["Work Item Type"]}","${testStep.Title}","${testStep["Test Step"]}","${testStep["Step Action"]}","${testStep["Step Expected"]}"\n`;
    });
    return csv;
}
function saveCsvToFile(csv, filename) {
    vscode.window.showSaveDialog({
        defaultUri: vscode.Uri.file(filename + '.csv'),
        filters: {
            'CSV Files': ['csv']
        }
    }).then(fileUri => {
        if (fileUri) {
            vscode.workspace.fs.writeFile(fileUri, Buffer.from(csv));
        }
    });
}
//# sourceMappingURL=devOpsTestSteps.js.map