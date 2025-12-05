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
exports.listALFiles = exports.getTestMethodRangesFromDocument = exports.getMethodRangesFromDocument = exports.getMethodNameFromDocumentAndLine = exports.activeEditorIsOpenToTestAppJson = exports.getTestFolderPath = exports.openEditorToTestFileIfNotAlready = exports.getALFileForALObject = exports.getALFilesInWorkspace = exports.getFilePathOfObject = exports.getDocumentName = exports.getDocumentIdAndName = exports.documentIsTestCodeunit = exports.getALObjectOfDocument = exports.getALObjectFromPath = void 0;
const vscode = require("vscode");
const types_1 = require("./types");
const extension_1 = require("./extension");
const fs_1 = require("fs");
const config_1 = require("./config");
const path_1 = require("path");
const constants_1 = require("./constants");
const telemetry_1 = require("./telemetry");
const output_1 = require("./output");
function getALObjectFromPath(path) {
    const text = (0, fs_1.readFileSync)(path, { encoding: 'utf-8' });
    const objectDeclaration = getObjectDeclarationFromText(text);
    if (objectDeclaration) {
        let alObject = getALObjectFromDeclaration(objectDeclaration);
        return alObject;
    }
    return { id: 0, name: '', type: '' };
}
exports.getALObjectFromPath = getALObjectFromPath;
function getALObjectOfDocument(document) {
    const objectDeclaration = getObjectDeclarationFromDocument(document);
    if (objectDeclaration) {
        return getALObjectFromDeclaration(objectDeclaration);
    }
    return undefined;
}
exports.getALObjectOfDocument = getALObjectOfDocument;
function documentIsTestCodeunit(document) {
    if (document.fileName.substring(document.fileName.lastIndexOf('.')) !== '.al') {
        return false;
    }
    const text = document.getText();
    return (text.match('Sub(t|T)ype *= *(t|T)est;') !== null);
}
exports.documentIsTestCodeunit = documentIsTestCodeunit;
function getDocumentIdAndName(document) {
    const objectDeclaration = getObjectDeclarationFromDocument(document);
    if (objectDeclaration) {
        return getIdAndNameFromObjectDeclaration(objectDeclaration);
    }
    return '';
}
exports.getDocumentIdAndName = getDocumentIdAndName;
function getIdAndNameFromObjectDeclaration(declaration) {
    let matches = declaration.match('\\d+ .*');
    if (matches) {
        return matches.shift().replace(/"/g, '');
    }
    return '';
}
function getObjectDeclarationFromDocument(document) {
    const documentText = document.getText();
    return getObjectDeclarationFromText(documentText);
}
function getObjectDeclarationFromText(text) {
    let matches = text.match(new RegExp(constants_1.objectDeclarationRegEx, 'i'));
    if (matches) {
        return matches.shift();
    }
}
function getALObjectFromDeclaration(declaration) {
    let ALObject = {
        type: declaration.substr(0, declaration.indexOf(' ')),
        id: parseInt(declaration.substring(declaration.indexOf(' ') + 1)),
        name: getObjectNameFromText(declaration)
    };
    return ALObject;
}
function getDocumentName(document) {
    const idAndName = getDocumentIdAndName(document);
    return idAndName.substr(idAndName.indexOf(' ') + 1);
}
exports.getDocumentName = getDocumentName;
function getObjectNameFromText(declaration) {
    const idAndName = getIdAndNameFromObjectDeclaration(declaration);
    return idAndName.substr(idAndName.indexOf(' ') + 1);
}
function getFilePathOfObject(object, method, files) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const alFile = getALFileForALObject(object, files);
            if (alFile) {
                const text = (0, fs_1.readFileSync)(alFile.path, { encoding: 'utf-8' });
                const matches = text.match(`procedure.*${method}`);
                if (matches) {
                    const document = yield vscode.workspace.openTextDocument(alFile.path);
                    const lineNo = document.positionAt(matches.index).line + 1;
                    resolve(`${alFile.path}:${lineNo}`);
                }
            }
        }));
    });
}
exports.getFilePathOfObject = getFilePathOfObject;
function getALFilesInWorkspace(excludePattern, glob) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            (0, telemetry_1.sendDebugEvent)('getALFilesInWorkspace-start');
            let alFiles = [];
            let files;
            if (glob) {
                files = yield vscode.workspace.findFiles(glob);
            }
            else {
                files = yield vscode.workspace.findFiles('**/*.al');
            }
            for (let file of files) {
                (0, telemetry_1.sendDebugEvent)('getALFilesInWorkspace-openTextDocument', { "path": file.fsPath });
                const document = yield vscode.workspace.openTextDocument(file);
                const alObject = getALObjectOfDocument(document);
                if (alObject) {
                    alFiles.push({ object: alObject, path: file.fsPath, excludeFromCodeCoverage: excludePath(file.fsPath, excludePattern) });
                }
                else {
                    (0, telemetry_1.sendDebugEvent)('getALFilesInWorkspace-alObjectUndefined', { "path": file.fsPath });
                }
            }
            ;
            resolve(alFiles);
        }));
    });
}
exports.getALFilesInWorkspace = getALFilesInWorkspace;
function excludePath(path, excludePattern) {
    if (!excludePattern) {
        return false;
    }
    if (path.match(excludePattern)) {
        return true;
    }
    return false;
}
function getALFileForALObject(object, files) {
    if (!files) {
        files = extension_1.alFiles;
    }
    const filteredFiles = files.filter(file => {
        if (file.object) {
            if (object.name) {
                return file.object.type.toLowerCase() === object.type.toLowerCase() &&
                    file.object.name === object.name;
            }
            else {
                return file.object.type.toLowerCase() === object.type.toLowerCase() &&
                    file.object.id === object.id;
            }
        }
    });
    if (filteredFiles.length > 0) {
        return (filteredFiles.shift());
    }
    else {
        return undefined;
    }
}
exports.getALFileForALObject = getALFileForALObject;
function openEditorToTestFileIfNotAlready() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            (0, telemetry_1.sendDebugEvent)('openEditorToTestFileIfNotAlready-start');
            if (!activeEditorOpenToTestFile()) {
                if (yield openTestAppJson()) {
                    resolve(true);
                }
                else {
                    resolve(false);
                }
            }
            else {
                resolve(false);
            }
        }));
    });
}
exports.openEditorToTestFileIfNotAlready = openEditorToTestFileIfNotAlready;
function activeEditorOpenToTestFile() {
    if (!extension_1.activeEditor) {
        return false;
    }
    const testFolderPath = getTestFolderPath();
    if (testFolderPath) {
        return extension_1.activeEditor.document.uri.fsPath.includes(testFolderPath);
    }
    else {
        return false;
    }
}
function openTestAppJson() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => __awaiter(this, void 0, void 0, function* () {
            const appJsonPath = getPathOfTestAppJson();
            if (appJsonPath) {
                vscode.commands.executeCommand('workbench.action.keepEditor');
                resolve(yield vscode.window.showTextDocument(yield vscode.workspace.openTextDocument(appJsonPath)));
            }
            else {
                resolve(undefined);
            }
        }));
    });
}
function getPathOfTestAppJson() {
    const testFolderPath = getTestFolderPath();
    if (testFolderPath) {
        return (0, path_1.join)(testFolderPath, 'app.json');
    }
}
function getTestFolderPath() {
    const config = (0, config_1.getCurrentWorkspaceConfig)(false);
    const testFolderFromConfig = (0, config_1.getTestFolderFromConfig)(config);
    if (testFolderFromConfig) {
        return testFolderFromConfig;
    }
    const workspaceFolder = (0, config_1.getWorkspaceFolder)();
    if (workspaceFolder) {
        return workspaceFolder;
    }
    vscode.window.showErrorMessage(`Could not find a test workspace folder with name "${config.testFolderName}". Please check the Test Folder Name setting.`, 'Open Settings').then(button => {
        if (button == 'Open Settings') {
            vscode.commands.executeCommand('workbench.action.openSettings2');
        }
    });
    return undefined;
}
exports.getTestFolderPath = getTestFolderPath;
function activeEditorIsOpenToTestAppJson() {
    if (!extension_1.activeEditor) {
        return false;
    }
    return extension_1.activeEditor.document.uri.fsPath === getPathOfTestAppJson();
}
exports.activeEditorIsOpenToTestAppJson = activeEditorIsOpenToTestAppJson;
function getMethodNameFromDocumentAndLine(document, lineNumber) {
    const line = document.lineAt(lineNumber - 1);
    return line.text.substring(line.text.indexOf('procedure ') + 'procedure '.length, line.text.indexOf('('));
}
exports.getMethodNameFromDocumentAndLine = getMethodNameFromDocumentAndLine;
function getMethodRangesFromDocument(document) {
    let alMethodRanges = [];
    const regEx = /(?:procedure )(\w*)(?:\()/gi;
    const text = document.getText();
    let match;
    while (match = regEx.exec(text)) {
        if (!documentLineIsCommentedOut(document, text, match.index)) {
            const alMethodRange = {
                name: match[1],
                range: new vscode.Range(document.positionAt(match.index), document.positionAt(match.index + match[1].length))
            };
            alMethodRanges.push(alMethodRange);
        }
    }
    return alMethodRanges;
}
exports.getMethodRangesFromDocument = getMethodRangesFromDocument;
function getTestMethodRangesFromDocument(document) {
    const documentText = document.getText();
    const regEx = /\[Test\]/gi;
    let testMethods = [];
    let match;
    while (match = regEx.exec(documentText)) {
        let subDocumentText = '';
        if (match.index + 1000 > documentText.length) {
            subDocumentText = documentText.substring(match.index);
        }
        else {
            subDocumentText = documentText.substring(match.index, match.index + 1000);
        }
        let methodMatch = subDocumentText.match('(?<=procedure ).*\\(');
        if (methodMatch !== undefined) {
            const startPos = document.positionAt(match.index + methodMatch.index);
            const endPos = document.positionAt(match.index + methodMatch.index + methodMatch[0].length - 1);
            if (!documentLineIsCommentedOut(document, documentText, match.index)) {
                const testMethod = {
                    name: subDocumentText.substring(methodMatch.index, methodMatch.index + methodMatch[0].length - 1),
                    range: new vscode.Range(startPos, endPos)
                };
                testMethods.push(testMethod);
            }
        }
    }
    return testMethods;
}
exports.getTestMethodRangesFromDocument = getTestMethodRangesFromDocument;
function documentLineIsCommentedOut(document, text, index) {
    //if the line startsWith (excluding whitespace at the beginning of the line) // then it has been commented out
    const textLine = document.lineAt(document.positionAt(index).line);
    if (textLine.text.substring(textLine.firstNonWhitespaceCharacterIndex).startsWith('//')) {
        return true;
    }
    //if there is a match on /* before the line and not a */ after that match then the line has been block commented out
    const lastIndexBlockCommentStart = text.substring(0, index).lastIndexOf('/*');
    if (lastIndexBlockCommentStart > -1) {
        const lastIndexBlockCommentEnd = text.substring(lastIndexBlockCommentStart, index).lastIndexOf('*/');
        if (lastIndexBlockCommentEnd == -1) {
            return true;
        }
    }
    return false;
}
function listALFiles() {
    return __awaiter(this, void 0, void 0, function* () {
        vscode.window.showInformationMessage('Reading AL files in workspace...');
        const outputEditor = (0, output_1.getOutputWriter)(types_1.OutputType.Editor);
        const startTime = new Date();
        let results = [];
        const files = yield getALFilesInWorkspace();
        files.forEach(file => {
            let result;
            if (file.object) {
                result = { path: file.path, type: file.object.type, id: file.object.id, name: file.object.name };
            }
            else {
                result = { path: file.path, type: 'undefined', id: 'undefined', name: 'undefined' };
            }
            results.push(result);
        });
        (0, output_1.writeTable)(outputEditor, results, ['path', 'type', 'id', 'name'], true, true);
        const endTime = new Date();
        outputEditor.write(`Started at: ${startTime.toTimeString()}`);
        outputEditor.write(`Ended at  : ${endTime.toTimeString()}`);
        outputEditor.show();
    });
}
exports.listALFiles = listALFiles;
//# sourceMappingURL=alFileHelper.js.map