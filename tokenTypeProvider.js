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
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getTokenTypeAtCursorStart = getTokenTypeAtCursorStart;
exports.getTokenTypeAtCursorHover = getTokenTypeAtCursorHover;
exports.clearTokenCache = clearTokenCache;
const vscode = __importStar(require("vscode"));
const tokenCache = {};
function getTokenTypeAtCursorStart(editor) {
    return getTokenTypeAtCursor(editor, true);
}
function getTokenTypeAtCursorHover(editor) {
    return getTokenTypeAtCursor(editor, false);
}
async function getTokenTypeAtCursor(editor, atBegin) {
    const position = editor.selection.active;
    const document = editor.document;
    if (!document) {
        return undefined;
    }
    const cacheKey = document.uri.toString();
    let semanticTokens = getCachedTokens(cacheKey);
    if (!semanticTokens) {
        semanticTokens = await getSemanticTokens(document);
        if (!semanticTokens) {
            return undefined;
        }
        tokenCache[cacheKey] = semanticTokens;
    }
    const tokens = semanticTokens.data;
    let currentLine = 0;
    let currentStartCharacter = 0;
    for (let i = 0; i < tokens.length; i += 5) {
        const deltaLine = tokens[i];
        const deltaStartCharacter = tokens[i + 1];
        const length = tokens[i + 2];
        const tokenType = tokens[i + 3];
        // const tokenModifiers = tokens[i + 4];
        currentLine += deltaLine;
        currentStartCharacter =
            deltaLine === 0
                ? currentStartCharacter + deltaStartCharacter
                : deltaStartCharacter;
        const isAtCursor = atBegin
            ? position.line === currentLine &&
                position.character === currentStartCharacter
            : position.line === currentLine &&
                position.character >= currentStartCharacter &&
                position.character <= currentStartCharacter + length - 1;
        if (isAtCursor) {
            return getTokenTypeName(document.uri, tokenType);
        }
    }
    return null;
}
async function getTokenTypeName(uri, tokenType) {
    const semanticTokensLegend = await vscode.commands.executeCommand("vscode.provideDocumentSemanticTokensLegend", uri);
    return semanticTokensLegend?.tokenTypes[tokenType] || "unknown";
}
async function getSemanticTokens(document) {
    let semanticTokens = null;
    try {
        const cancelToken = new vscode.CancellationTokenSource();
        semanticTokens = await vscode.commands.executeCommand("vscode.provideDocumentSemanticTokens", document.uri, cancelToken);
    }
    catch (error) {
        vscode.window.showWarningMessage(`Error getting document semantic tokens. ${error}`);
        return undefined;
    }
    if (!semanticTokens) {
        return undefined;
    }
    return semanticTokens;
}
function getCachedTokens(uri) {
    return tokenCache[uri];
}
function clearTokenCache(uri) {
    delete tokenCache[uri];
}
//# sourceMappingURL=tokenTypeProvider.js.map