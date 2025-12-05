"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseJson = parseJson;
/**
 * Parses JSON, JSONC, or JSON5 content using the json5 library.
 * Throws a formatted error if parsing fails.
 *
 * @param content The JSON string to parse.
 * @returns The parsed object.
 * @throws Error if parsing fails.
 *
 * @example
 * const obj = parseJson('{ "foo": 123 }');
 * // { foo: 123 }
 */
const json5_1 = __importDefault(require("json5"));
const error_handler_helper_1 = require("./error-handler.helper");
function parseJson(content) {
    try {
        return json5_1.default.parse(content);
    }
    catch (error) {
        (0, error_handler_helper_1.throwError)('Failed to parse JSON', error);
    }
}
//# sourceMappingURL=json-parser.helper.js.map