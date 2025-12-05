"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseXml = parseXml;
/**
 * Parses XML content using the fast-xml-parser library.
 * Throws a formatted error if parsing fails.
 *
 * @param content The XML string to parse.
 * @returns The parsed object.
 * @throws Error if parsing fails.
 *
 * @example
 * const obj = parseXml('<foo><bar>baz</bar></foo>');
 * // { foo: { bar: 'baz' } }
 */
const fast_xml_parser_1 = require("fast-xml-parser");
const error_handler_helper_1 = require("./error-handler.helper");
function parseXml(content) {
    try {
        const parser = new fast_xml_parser_1.XMLParser();
        return parser.parse(content);
    }
    catch (error) {
        (0, error_handler_helper_1.throwError)('Failed to parse XML', error);
    }
}
//# sourceMappingURL=xml-parser.helper.js.map