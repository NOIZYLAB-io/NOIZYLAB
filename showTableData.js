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
exports.showTableData = void 0;
const vscode = require("vscode");
const config_1 = require("./config");
const extension_1 = require("./extension");
const telemetry_1 = require("./telemetry");
const alFileHelper_1 = require("./alFileHelper");
function showTableData() {
    return __awaiter(this, void 0, void 0, function* () {
        (0, telemetry_1.sendShowTableDataEvent)();
        let wordAtCursor = getWordAtCursor();
        let recordName = findRecordNameForVariable(wordAtCursor);
        if (recordName !== '') {
            vscode.window.showInformationMessage(`Opening browser to table ${recordName}...`);
            let showTableDataTerminal = (0, extension_1.getALTestRunnerTerminal)('al-test-runner-2');
            showTableDataTerminal.sendText(`cd "${(0, alFileHelper_1.getTestFolderPath)()}"`);
            showTableDataTerminal.sendText(`Show-TableData '${recordName}' -LaunchConfig '${(0, config_1.getLaunchConfiguration)((0, config_1.getALTestRunnerConfig)().launchConfigName)}'`);
        }
        else {
            vscode.window.showErrorMessage(`Could not find a record variable matching the name ${wordAtCursor}`);
        }
    });
}
exports.showTableData = showTableData;
function getWordAtCursor() {
    let rangeOfWord = extension_1.activeEditor.document.getWordRangeAtPosition(extension_1.activeEditor.selection.active);
    return extension_1.activeEditor.document.getText(rangeOfWord);
}
function findRecordNameForVariable(variableName) {
    let documentText = extension_1.activeEditor.document.getText();
    let regex = String.raw `${variableName} *: *Record *"*[^;\)"]+`;
    let matches = documentText.match(regex);
    if (matches) {
        let recordDefinition = matches.shift();
        if (recordDefinition.indexOf('"') > 0) {
            return recordDefinition.substring(recordDefinition.lastIndexOf('"') + 1);
        }
        else {
            return recordDefinition.substring(recordDefinition.lastIndexOf(' ') + 1);
        }
    }
    return '';
}
//# sourceMappingURL=showTableData.js.map