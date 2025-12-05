"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseHcl = parseHcl;
/**
 * Parses HCL content using the hcl-parser library.
 * Throws a formatted error if parsing fails.
 *
 * @param content The HCL string to parse.
 * @returns The parsed object.
 * @throws Error if parsing fails.
 *
 * @example
 * const obj = parseHcl('variable \"foo\" { default = \"bar\" }');
 * // { variable: { foo: { default: "bar" } } }
 */
const hcl_parser_1 = __importDefault(require("hcl-parser"));
const error_handler_helper_1 = require("./error-handler.helper");
function parseHcl(content) {
    try {
        return hcl_parser_1.default.parse(content);
    }
    catch (error) {
        (0, error_handler_helper_1.throwError)('Failed to parse HCL', error);
    }
}
//# sourceMappingURL=hcl-parser.helper.js.map