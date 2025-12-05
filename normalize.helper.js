"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.normalizeToJsonString = normalizeToJsonString;
/**
 * Helper to normalize text to a JSON string format.
 * Converts JavaScript/TypeScript-like syntax to valid JSON.
 */
function normalizeToJsonString(text, fileType) {
    let normalized = text;
    let detectedType = fileType;
    if (['javascript', 'javascriptreact', 'typescript', 'typescriptreact'].includes(fileType)) {
        detectedType = 'jsonc';
        normalized = text
            .replace(/'([^']+)'/g, '"$1"')
            .replace(/(["'])?([a-zA-Z0-9_]+)(["'])?:/g, '"$2":')
            .replace(/,*\s*\n*\]/g, ']')
            .replace(/{\s*\n*/g, '{')
            .replace(/,*\s*\n*};*/g, '}');
    }
    return { normalized, detectedType };
}
//# sourceMappingURL=normalize.helper.js.map