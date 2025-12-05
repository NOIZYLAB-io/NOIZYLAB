"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.getBlockOrLine = getBlockOrLine;
exports.findInnerBlock = findInnerBlock;
const vscode = __importStar(require("vscode"));
const constants_1 = require("../config/constants");
const utils_1 = require("./utils");
/**
 * Returns the smallest enclosing bracket block or a single line if none.
 * @param editor The active text editor
 * @returns Block information containing text and range
 */
function getBlockOrLine(editor) {
    const selText = editor.document.getText(editor.selection);
    if (selText) {
        return { text: selText, range: editor.selection };
    }
    const text = editor.document.getText();
    const cursor = editor.document.offsetAt(editor.selection.active);
    let bracketKind = vscode.workspace
        .getConfiguration('sapf')
        .get('codeBlockBrackets', constants_1.defaultBracketType);
    // Validate bracket configuration
    if (constants_1.brackets[bracketKind] === undefined) {
        vscode.window.showWarningMessage(`Invalid bracket type: ${bracketKind}, using '${constants_1.defaultBracketType}'`);
        bracketKind = constants_1.defaultBracketType;
    }
    const stack = [];
    let start = -1;
    let end = -1;
    const [openBracket, closeBracket] = constants_1.brackets[bracketKind];
    for (let i = 0; i < text.length; i++) {
        const currentChar = text[i];
        if (currentChar === openBracket) {
            stack.push(i);
        }
        else if (currentChar === closeBracket && stack.length) {
            const openIndex = stack.pop();
            if (openIndex == null) {
                continue;
            }
            if (openIndex < cursor && i > cursor && (start === -1 || openIndex < start)) {
                start = openIndex;
                end = i;
            }
        }
    }
    if (start !== -1 && end !== -1) {
        const range = new vscode.Range(editor.document.positionAt(start), editor.document.positionAt(end));
        const block = text.slice(start + 1, end);
        return { text: block, range };
    }
    return (0, utils_1.getLine)(editor);
}
/**
 * Finds the innermost block containing the cursor position.
 * @param editor The active text editor
 * @param bracketType The type of brackets to search for
 * @returns Block information or null if no block found
 */
function findInnerBlock(editor, bracketType) {
    const text = editor.document.getText();
    const cursor = editor.document.offsetAt(editor.selection.active);
    if (constants_1.brackets[bracketType] === undefined) {
        return null;
    }
    const [openBracket, closeBracket] = constants_1.brackets[bracketType];
    const stack = [];
    let bestMatch = null;
    for (let i = 0; i < text.length; i++) {
        const currentChar = text[i];
        if (currentChar === openBracket) {
            stack.push({ index: i, depth: stack.length });
        }
        else if (currentChar === closeBracket && stack.length > 0) {
            const openInfo = stack.pop();
            if (openInfo && openInfo.index < cursor && i > cursor) {
                if (!bestMatch || openInfo.depth > bestMatch.depth) {
                    bestMatch = { start: openInfo.index, end: i, depth: openInfo.depth };
                }
            }
        }
    }
    if (bestMatch) {
        const range = new vscode.Range(editor.document.positionAt(bestMatch.start), editor.document.positionAt(bestMatch.end));
        const blockText = text.slice(bestMatch.start + 1, bestMatch.end);
        return { text: blockText, range };
    }
    return null;
}
//# sourceMappingURL=block-finder.js.map