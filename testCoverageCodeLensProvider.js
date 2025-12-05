"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.TestCoverageCodeLensProvider = void 0;
const vscode = require("vscode");
const alFileHelper_1 = require("./alFileHelper");
const config_1 = require("./config");
const testCoverage_1 = require("./testCoverage");
class TestCoverageCodeLensProvider {
    constructor() {
        this.codeLenses = [];
    }
    provideCodeLenses(document, token) {
        this.codeLenses = [];
        if (!(document.fileName.endsWith('.al'))) {
            return this.codeLenses;
        }
        if ((0, alFileHelper_1.documentIsTestCodeunit)(document)) {
            return this.codeLenses;
        }
        const objectName = (0, alFileHelper_1.getDocumentName)(document);
        if ((0, config_1.getCurrentWorkspaceConfig)().enableCodeLens) {
            (0, alFileHelper_1.getMethodRangesFromDocument)(document).forEach(methodRange => {
                const method = { objectName: objectName, methodName: methodRange.name };
                const testCount = (0, testCoverage_1.getTestCoverageForMethod)(method).length;
                if (testCount > 0) {
                    let title = `${testCount} test`;
                    if (testCount != 1) {
                        title = title + 's';
                    }
                    ;
                    this.codeLenses.push(new vscode.CodeLens(methodRange.range, { title: `Run ${title}`, command: "altestrunner.runRelatedTests", arguments: [method] }));
                    this.codeLenses.push(new vscode.CodeLens(methodRange.range, { title: `Show ${title}`, command: "altestrunner.showRelatedTests", arguments: [method] }));
                }
            });
        }
        return this.codeLenses;
    }
}
exports.TestCoverageCodeLensProvider = TestCoverageCodeLensProvider;
//# sourceMappingURL=testCoverageCodeLensProvider.js.map