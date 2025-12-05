"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CodelensProvider = void 0;
const vscode = require("vscode");
const alFileHelper_1 = require("./alFileHelper");
class CodelensProvider {
    constructor() {
        this.codeLenses = [];
    }
    provideCodeLenses(document, token) {
        this.codeLenses = [];
        if (!((0, alFileHelper_1.documentIsTestCodeunit)(document))) {
            return this.codeLenses;
        }
        const config = vscode.workspace.getConfiguration('al-test-runner');
        if (config.enableCodeLens) {
            const testMethodRanges = (0, alFileHelper_1.getTestMethodRangesFromDocument)(document);
            testMethodRanges.forEach(testMethodRange => {
                this.codeLenses.push(new vscode.CodeLens(testMethodRange.range, { title: "Run Test", command: "altestrunner.runTest", arguments: [document.fileName, testMethodRange.range.start.line], tooltip: "Run this test with AL Test Runner" }));
                this.codeLenses.push(new vscode.CodeLens(testMethodRange.range, { title: "Debug Test", command: "altestrunner.debugTest", arguments: [document.fileName, testMethodRange.range.start.line], tooltip: "Debug this test with AL Test Runner" }));
            });
            if (this.codeLenses.push.length > 0) {
                this.codeLenses.push(new vscode.CodeLens(new vscode.Range(0, 0, 0, 0), { title: "Run Tests", command: "altestrunner.runTestsCodeunit", arguments: [document.fileName], tooltip: "Run all tests in this codeunit with AL Test Runner" }));
                this.codeLenses.push(new vscode.CodeLens(new vscode.Range(0, 0, 0, 0), { title: "Debug Tests", command: "altestrunner.debugTestsCodeunit", arguments: [document.fileName], tooltip: "Run all tests in this codeunit with AL Test Runner" }));
            }
        }
        return this.codeLenses;
    }
}
exports.CodelensProvider = CodelensProvider;
//# sourceMappingURL=CodelensProvider.js.map