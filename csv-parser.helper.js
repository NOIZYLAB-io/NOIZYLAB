"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseCsv = parseCsv;
/**
 * Parses CSV content into an array of objects.
 * Throws a formatted error if parsing fails.
 *
 * @param content The CSV string to parse.
 * @returns The parsed array of objects.
 * @throws Error if parsing fails.
 *
 * @example
 * const data = parseCsv('name,age\nAlice,30\nBob,25');
 * // [{ name: 'Alice', age: '30' }, { name: 'Bob', age: '25' }]
 */
const detect_delimiter_helper_1 = require("./detect-delimiter.helper");
const error_handler_helper_1 = require("./error-handler.helper");
function parseCsv(content) {
    try {
        const rows = content
            .trim()
            .split('\n')
            .map((r) => r.replace('\r', ''));
        if (rows.length === 0) {
            return [];
        }
        // Prefer common CSV delimiters; include tab/pipe to be robust with mislabeled files
        const delimiter = (0, detect_delimiter_helper_1.detectDelimiter)(content, [',', ';', '|', '\t']);
        const headers = rows[0].split(delimiter);
        return rows.slice(1).map((row) => {
            const values = row.split(delimiter);
            return headers.reduce((acc, header, index) => {
                acc[header] = values[index];
                return acc;
            }, {});
        });
    }
    catch (error) {
        (0, error_handler_helper_1.throwError)('Failed to parse CSV', error);
    }
}
//# sourceMappingURL=csv-parser.helper.js.map