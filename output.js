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
exports.getMaxLengthOfPropertyFromArray = exports.padString = exports.writeTable = exports.getOutputWriter = void 0;
const extension_1 = require("./extension");
const vscode = require("vscode");
const types_1 = require("./types");
function getOutputWriter(outputType) {
    switch (outputType) {
        case types_1.OutputType.Editor:
            return new OutputEditor;
        default:
            return new OutputChannel;
    }
}
exports.getOutputWriter = getOutputWriter;
class OutputChannel {
    constructor() {
        this.content = "";
    }
    write(contentLine) {
        extension_1.outputChannel.appendLine(contentLine);
    }
    clear() {
        extension_1.outputChannel.clear();
    }
    show() {
        extension_1.outputChannel.show(true);
    }
}
class OutputEditor {
    constructor() {
        this.content = "";
    }
    write(contentLine) {
        this.content += contentLine + "\n";
    }
    clear() {
        this.content = "";
    }
    show() {
        return __awaiter(this, void 0, void 0, function* () {
            this.document = yield vscode.workspace.openTextDocument({ content: this.content });
            vscode.window.showTextDocument(this.document);
        });
    }
}
function writeTable(writer, contentArray, properties, clearFirst, showHeadings, title, headings) {
    if (clearFirst) {
        writer.clear();
    }
    else {
        writer.write(' ');
    }
    if (title) {
        writer.write(title);
        writer.write(' ');
    }
    let maxLengths = getMaxColumnLengths(contentArray, properties);
    if (showHeadings) {
        let headingLine = '';
        properties.forEach((property, index) => {
            if (headingLine !== '') {
                headingLine += ' | ';
            }
            if (headings) {
                headingLine += padString(headings[index], maxLengths[index]);
            }
            else {
                headingLine += padString(property, maxLengths[index]);
            }
        });
        writer.write(headingLine);
        writer.write(padString('', headingLine.length, '-'));
    }
    contentArray.forEach(content => {
        let line = '';
        properties.forEach((property, index) => {
            if (line !== '') {
                line += ' | ';
            }
            line += padString(content[property], maxLengths[index]);
        });
        writer.write(line);
    });
}
exports.writeTable = writeTable;
function padString(string, length, padWith = ' ') {
    let result = string;
    for (let i = result.length; i < length; i++) {
        result += padWith;
    }
    return result;
}
exports.padString = padString;
function getMaxColumnLengths(contentArray, properties, headings) {
    let maxLengths = [];
    properties === null || properties === void 0 ? void 0 : properties.forEach((property, index) => {
        if (headings) {
            maxLengths.push(getMaxLengthOfPropertyFromArray(contentArray, property, headings[index]));
        }
        else {
            maxLengths.push(getMaxLengthOfPropertyFromArray(contentArray, property));
        }
    });
    return maxLengths;
}
function getMaxLengthOfPropertyFromArray(contentArray, property, heading) {
    let maxLength = 0;
    contentArray.forEach(element => {
        let propertyValue;
        if (property) {
            if (typeof (element[property]) == "string") {
                propertyValue = element[property];
            }
            else {
                propertyValue = element[property].toString();
            }
        }
        else {
            propertyValue = element;
        }
        if (propertyValue.length > maxLength) {
            maxLength = propertyValue.length;
        }
    });
    if (property) {
        if (property.length > maxLength) {
            maxLength = property.length;
        }
    }
    if (heading) {
        if (heading.length > maxLength) {
            maxLength = heading.length;
        }
    }
    return maxLength;
}
exports.getMaxLengthOfPropertyFromArray = getMaxLengthOfPropertyFromArray;
//# sourceMappingURL=output.js.map