"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseJSONContent = exports.isFileTypeSupported = void 0;
const vscode_1 = require("vscode");
const _1 = require(".");
/**
 * Checks if a value is a supported FileType.
 *
 * @param value The value to check.
 * @returns True if the value is a supported FileType, false otherwise.
 *
 * @example
 * isFileTypeSupported('json'); // true
 * isFileTypeSupported('unsupported'); // false
 */
const isFileTypeSupported = (value) => {
    const validFileTypes = [
        'csv',
        'dockercompose',
        'env',
        'hcl',
        'ini',
        'json',
        'json5',
        'jsonc',
        'properties',
        'toml',
        'tsv',
        'xml',
        'yaml',
        'yml',
    ];
    return validFileTypes.includes(value);
};
exports.isFileTypeSupported = isFileTypeSupported;
/**
 * Parses the given string content using the specified file type parser.
 * Returns an object representation or null if parsing fails.
 *
 * @param content The string content to parse.
 * @param type The type of file format to parse as.
 * @returns The parsed object or null if parsing fails.
 *
 * @remarks
 * Delegates parsing to modular helpers. Centralizes error handling for consistency.
 *
 * @example
 * const obj = parseJSONContent('{ "foo": 1 }', 'json');
 * if (obj) { console.log(obj.foo); }
 */
const parseJSONContent = (content, type) => {
    try {
        // Delegates parsing based on file type to modular helpers.
        switch (type) {
            case 'json':
            case 'jsonc':
            case 'json5':
                return (0, _1.parseJson)(content);
            case 'dockercompose':
            case 'yaml':
            case 'yml':
                return (0, _1.parseYaml)(content);
            case 'toml':
                return (0, _1.parseToml)(content);
            case 'ini':
            case 'properties':
                return (0, _1.parseIni)(content);
            case 'env':
                return (0, _1.parseEnv)(content);
            case 'xml':
                return (0, _1.parseXml)(content);
            case 'hcl':
                return (0, _1.parseHcl)(content);
            case 'csv':
                return (0, _1.parseCsv)(content);
            case 'tsv':
                return (0, _1.parseTsv)(content);
            default: {
                // Show a localized error for unsupported file types
                const message = vscode_1.l10n.t('Invalid file type!');
                vscode_1.window.showErrorMessage(message);
                return null;
            }
        }
    }
    catch (error) {
        const message = vscode_1.l10n.t('Error parsing {0}: {1}', [
            type.toUpperCase(),
            error.message,
        ]);
        vscode_1.window.showErrorMessage(message);
        return null;
    }
};
exports.parseJSONContent = parseJSONContent;
//# sourceMappingURL=json.helper.js.map