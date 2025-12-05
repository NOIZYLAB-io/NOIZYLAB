"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.generateGrammar = generateGrammar;
/**
 * Generates a TextMate grammar file from keyword definitions
 * @param keywords Map of keywords to their information
 * @returns TextMate grammar object
 */
function generateGrammar(keywords) {
    const builtinFunctions = Array.from(keywords.keys());
    // Group functions by length to create more manageable patterns
    const functionGroups = {};
    builtinFunctions.forEach(name => {
        const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const length = name.length;
        const groupKey = length > 10 ? 'long' : length > 5 ? 'medium' : 'short';
        if (!functionGroups[groupKey]) {
            functionGroups[groupKey] = [];
        }
        functionGroups[groupKey].push(escaped);
    });
    // Create patterns for each group (longest first to avoid partial matches)
    const patterns = [];
    if (functionGroups.long) {
        patterns.push({
            "name": "keyword.builtin.sapf",
            "match": `\\b(${functionGroups.long.sort((a, b) => b.length - a.length).join('|')})\\b`
        });
    }
    if (functionGroups.medium) {
        patterns.push({
            "name": "keyword.builtin.sapf",
            "match": `\\b(${functionGroups.medium.sort((a, b) => b.length - a.length).join('|')})\\b`
        });
    }
    if (functionGroups.short) {
        patterns.push({
            "name": "keyword.builtin.sapf",
            "match": `\\b(${functionGroups.short.sort((a, b) => b.length - a.length).join('|')})\\b`
        });
    }
    return {
        "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
        "name": "SAPF",
        "scopeName": "source.sapf",
        "patterns": [
            { "include": "#comments" },
            { "include": "#builtin-functions" },
            { "include": "#user-variables" }
        ],
        "repository": {
            "comments": {
                "patterns": [{
                        "name": "comment.line.semicolon.sapf",
                        "match": ";.*$"
                    }]
            },
            "builtin-functions": {
                "patterns": patterns
            },
            "user-variables": {
                "patterns": [{
                        "name": "variable.other.sapf",
                        "match": "\\b[a-zA-Z][a-zA-Z0-9_]*\\b"
                    }]
            }
        }
    };
}
//# sourceMappingURL=grammar.js.map