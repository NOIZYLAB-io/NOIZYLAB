"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.parseTsv = parseTsv;
/**
 * Parses TSV content into an array of objects.
 * Throws a formatted error if parsing fails.
 *
 * @param content The TSV string to parse.
 * @returns The parsed array of objects.
 * @throws Error if parsing fails.
 *
 * @example
 * const data = parseTsv('name\tage\nAlice\t30\nBob\t25');
 * // [{ name: 'Alice', age: '30' }, { name: 'Bob', age: '25' }]
 */
const detect_delimiter_helper_1 = require("./detect-delimiter.helper");
const error_handler_helper_1 = require("./error-handler.helper");
function parseTsv(content) {
    try {
        const rows = content
            .trim()
            .split('\n')
            .map((row) => row.replace('\r', ''));
        if (rows.length === 0) {
            return [];
        }
        // Prefer tab for TSV, but allow fallback in case of mislabeled files
        const delimiter = (0, detect_delimiter_helper_1.detectDelimiter)(content, ['\t', '|', ',', ';']);
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
        (0, error_handler_helper_1.throwError)('Failed to parse TSV', error);
    }
}
//# sourceMappingURL=tsv-parser.helper.js.map