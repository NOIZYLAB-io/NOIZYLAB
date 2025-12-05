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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.TransformController = void 0;
const json_to_ts_1 = __importDefault(require("json-to-ts"));
const json5 = __importStar(require("json5"));
const vscode_1 = require("vscode");
// Import the helper functions
const helpers_1 = require("../helpers");
/**
 * TransformController handles parsing, validation, and code generation for Angular elements.
 * All public methods are documented with JSDoc for clarity and maintainability.
 * @class TransformController
 * @module controllers/transform.controller
 */
class TransformController {
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    // Public methods
    /**
     * Converts selected JSON text to TypeScript interfaces and opens it in a new editor.
     * @returns Promise resolved with the opened TextEditor or void if cancelled.
     */
    async json2ts() {
        let editor;
        if (vscode_1.workspace.workspaceFolders) {
            editor = vscode_1.window.activeTextEditor;
        }
        else {
            const message = vscode_1.l10n.t('No text editor is active!');
            (0, helpers_1.showError)(message);
            return;
        }
        const selection = editor?.selection;
        if (selection && !selection.isEmpty) {
            const selectionRange = new vscode_1.Range(selection.start.line, selection.start.character, selection.end.line, selection.end.character);
            let text = editor?.document.getText(selectionRange) || '';
            const languageId = editor?.document.languageId || '';
            if ([
                'javascript',
                'javascriptreact',
                'typescript',
                'typescriptreact',
            ].includes(languageId)) {
                text = text
                    .replace(/'([^']+)'/g, '"$1"')
                    .replace(/(['"])?([a-zA-Z0-9_]+)(['"])?:/g, '"$2":')
                    .replace(/,*\s*\n*\]/g, ']')
                    .replace(/{\s*\n*/g, '{')
                    .replace(/,*\s*\n*};*/g, '}');
            }
            const jsonSchema = this.tryParseJSONObject(text);
            if (!jsonSchema) {
                const message = vscode_1.l10n.t('Invalid JSON Schema!');
                (0, helpers_1.showError)(message);
                return;
            }
            const tsSchema = (0, json_to_ts_1.default)(jsonSchema)
                .map((itf) => `export ${itf}\n`)
                .join('\n');
            const document = await vscode_1.workspace.openTextDocument({
                language: 'typescript',
                content: tsSchema,
            });
            return await vscode_1.window.showTextDocument(document);
        }
        const message = vscode_1.l10n.t('No text is selected!');
        (0, helpers_1.showError)(message);
        return;
    }
    // Private methods
    /**
     * Attempts to parse a string as a JSON object using JSON5.
     * @param str String to parse.
     * @returns Parsed object if valid, or false if invalid.
     */
    tryParseJSONObject(str) {
        try {
            const object = json5.parse(str);
            if (object && typeof object === 'object') {
                return object;
            }
        }
        catch (e) {
            return false;
        }
        return false;
    }
}
exports.TransformController = TransformController;
//# sourceMappingURL=transform.controller.js.map