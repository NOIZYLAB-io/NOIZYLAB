"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.HlfCodeLensProvider = void 0;
const vscode = require("vscode");
class HlfCodeLensProvider {
    constructor() {
        this.lineSplit = /\r?\n/g;
    }
    //Get the code areas corresponding to the various request sections
    provideCodeLenses(document) {
        //var startTime = process.hrtime();
        //const telemetryLogger = TelemetryLogger.instance();
        const codeLenses = [];
        const lines = document.getText().split(this.lineSplit);
        let startline = 0, startIndex = 0, codeStartline = 0, codeStartIndex = 0;
        let lineIndex = 0;
        let lineMatches = 0;
        let lastOpenBracketLine = 0, lastOpenBracketIndex = 0;
        let lastCloseBracketLine = 0, lastCloseBracketIndex = 0;
        for (let line of lines) {
            const matchedIndex = line.search(/("invoke"|"query") *:/gi);
            if (matchedIndex === -1) {
                if (line.lastIndexOf("{") > -1) {
                    lastOpenBracketLine = lineIndex;
                    lastOpenBracketIndex = line.lastIndexOf("{");
                }
                if (line.lastIndexOf("}") > -1) {
                    lastCloseBracketLine = lineIndex;
                    lastCloseBracketIndex = line.lastIndexOf("}");
                }
            }
            else {
                const preTransactionLine = line.substring(0, matchedIndex);
                if (preTransactionLine.lastIndexOf("{") > -1) {
                    lastOpenBracketLine = lineIndex;
                    lastOpenBracketIndex = preTransactionLine.lastIndexOf("{");
                }
                if (preTransactionLine.lastIndexOf("}") > -1) {
                    lastCloseBracketLine = lineIndex;
                    lastCloseBracketIndex = preTransactionLine.lastIndexOf("}");
                }
                if (lineMatches > 0) {
                    const range = new vscode.Range(startline, startIndex, lineIndex - 1, 0);
                    const codeRange = new vscode.Range(codeStartline, codeStartIndex, lastCloseBracketLine, lastCloseBracketIndex + 1);
                    const cmd = {
                        arguments: [codeRange],
                        title: 'Send Request',
                        command: 'hlf.fabric.request'
                    };
                    codeLenses.push(new vscode.CodeLens(range, cmd));
                }
                if (line.lastIndexOf("}") > -1) {
                    lastCloseBracketLine = lineIndex;
                    lastCloseBracketIndex = line.lastIndexOf("}");
                }
                lineMatches++;
                startline = lineIndex;
                startIndex = matchedIndex;
                codeStartline = lastOpenBracketLine;
                codeStartIndex = lastOpenBracketIndex;
            }
            lineIndex++;
        }
        if (lineMatches > 0) {
            const range = new vscode.Range(startline, startIndex, lineIndex, 0);
            const codeRange = new vscode.Range(codeStartline, codeStartIndex, lastCloseBracketLine, lastCloseBracketIndex + 1);
            const cmd = {
                arguments: [codeRange],
                title: 'Send Request',
                command: 'hlf.fabric.request'
            };
            codeLenses.push(new vscode.CodeLens(range, cmd));
        }
        //const elapsedTime = telemetryLogger.parseHrtimeToMs(process.hrtime(startTime));
        //telemetryLogger.sendTelemetryEvent('CodeLens', null, {'codeLensDuration': elapsedTime});
        return codeLenses;
    }
}
exports.HlfCodeLensProvider = HlfCodeLensProvider;
//# sourceMappingURL=HlfCodeLensProvider.js.map