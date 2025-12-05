"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CodeCoverageCodeLensProvider = void 0;
const vscode = require("vscode");
const alFileHelper_1 = require("./alFileHelper");
const coverage_1 = require("./coverage");
const config_1 = require("./config");
const types_1 = require("./types");
class CodeCoverageCodeLensProvider {
    constructor() {
        this.codeLenses = [];
    }
    provideCodeLenses(document, token) {
        this.codeLenses = [];
        return new Promise(resolve => {
            if (!document.fileName.endsWith('.al')) {
                resolve(this.codeLenses);
            }
            if ((0, alFileHelper_1.documentIsTestCodeunit)(document)) {
                resolve(this.codeLenses);
            }
            if ((0, config_1.getCurrentWorkspaceConfig)().enableCodeLens) {
                const alObject = (0, alFileHelper_1.getALObjectOfDocument)(document);
                if (alObject) {
                    (0, coverage_1.readCodeCoverage)(types_1.CodeCoverageDisplay.All).then(allCodeCoverage => {
                        const objectCodeCoverage = (0, coverage_1.filterCodeCoverageByObject)(allCodeCoverage, alObject, true);
                        const methodRanges = (0, alFileHelper_1.getMethodRangesFromDocument)(document);
                        methodRanges.forEach((methodRange, index) => {
                            let endLineNumber;
                            if (index == methodRanges.length - 1) {
                                endLineNumber = 99999;
                            }
                            else {
                                endLineNumber = methodRanges[index + 1].range.start.line - 1;
                            }
                            const startLineNumber = methodRange.range.start.line;
                            const totalLines = (0, coverage_1.filterCodeCoverageByLineNoRange)(objectCodeCoverage, startLineNumber, endLineNumber, true).length;
                            const hitLines = (0, coverage_1.filterCodeCoverageByLineNoRange)(objectCodeCoverage, startLineNumber, endLineNumber, false).length;
                            this.codeLenses.push(new vscode.CodeLens(methodRange.range, { title: `${(0, coverage_1.getCodeCoveragePercentage)(hitLines, totalLines)}% Coverage`, command: 'altestrunner.toggleCodeCoverage', arguments: [types_1.CodeCoverageDisplay.All] }));
                            if (index == methodRanges.length - 1) {
                                resolve(this.codeLenses);
                            }
                        });
                    });
                }
            }
        });
    }
}
exports.CodeCoverageCodeLensProvider = CodeCoverageCodeLensProvider;
//# sourceMappingURL=codeCoverageCodeLensProvider.js.map