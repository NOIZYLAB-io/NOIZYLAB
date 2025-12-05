'use strict';
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
exports.range_uuid = exports.range_AtoX = exports.range_1toX = exports.range_0toX = exports.range_generic = exports.promptWordList = exports.promptRange = exports.range = void 0;
const vscode = require("vscode");
const utils_1 = require("./utils");
const uuid = require("uuid");
function range(rangeMethod) {
    const editor = vscode.window.activeTextEditor;
    editor.edit(editBuilder => {
        let cursors = (0, utils_1.getCursors)(editBuilder);
        let itemsToInsert;
        if (typeof rangeMethod === 'function') {
            itemsToInsert = rangeMethod(cursors.length);
        }
        else {
            itemsToInsert = rangeMethod;
        }
        cursors.forEach((selection, index) => {
            let range = new vscode.Position(selection.start.line, selection.start.character);
            editBuilder.insert(range, itemsToInsert[index]);
            editBuilder.delete(selection);
        });
    });
}
exports.range = range;
function promptRange(prompt = 'Where should the range start?') {
    return __awaiter(this, void 0, void 0, function* () {
        const result = yield vscode.window.showInputBox({ prompt });
        if (result === null || result === undefined) {
            // User cancelled
            throw new Error();
        }
        let num = +result;
        if (isNaN(num)) {
            return promptRange(`"${result}" is an invalid number. Enter a number.`);
        }
        return num;
    });
}
exports.promptRange = promptRange;
;
function promptWordList(prompt = 'List of words (space separated)') {
    return __awaiter(this, void 0, void 0, function* () {
        const result = yield vscode.window.showInputBox({ prompt });
        if (result === null || result === undefined) {
            // User cancelled
            throw new Error();
        }
        const words = result.split(/\s+/);
        return words;
    });
}
exports.promptWordList = promptWordList;
;
function range_generic(start) {
    return function (count) {
        let a = [];
        let end = count + start;
        for (let i = start; i < end; ++i) {
            a.push(String(i));
        }
        return a;
    };
}
exports.range_generic = range_generic;
function range_0toX(count) {
    return range_generic(0)(count);
}
exports.range_0toX = range_0toX;
function range_1toX(count) {
    return range_generic(1)(count);
}
exports.range_1toX = range_1toX;
function range_AtoX(count) {
    let a = [];
    let startCode = 'a'.charCodeAt(0);
    for (let i = 0; i < count; ++i) {
        const offset = i % 26; // only loop through lower case a-z
        a.push(String.fromCharCode(startCode + offset));
    }
    return a;
}
exports.range_AtoX = range_AtoX;
function range_uuid(count) {
    let a = [];
    for (let i = 0; i < count; ++i) {
        a.push(uuid.v4().toLowerCase());
    }
    return a;
}
exports.range_uuid = range_uuid;
//# sourceMappingURL=rangeMethods.js.map