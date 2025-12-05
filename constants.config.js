"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.INSERT_FINAL_NEWLINE = exports.END_OF_LINE = exports.USE_SINGLE_QUOTES = exports.EXCLUDE_SEMICOLON = exports.HEADER_COMMENT_TEMPLATE = exports.DEFAULT_FILENAME = exports.EXPORT_FILENAME = exports.USE_NAMED_EXPORTS = exports.DETECT_EXPORTS = exports.KEEP_EXTENSION = exports.PRESERVE_GITIGNORE = exports.SUPPORTS_HIDDEN = exports.RECURSION_DEPTH = exports.EXCLUDE_PATTERNS = exports.INCLUDE_EXTENSIONS = exports.DISABLE_RECURSIVE = exports.DEFAULT_LANGUAGE = exports.REPOSITORY_URL = exports.USER_PUBLISHER = exports.USER_NAME = exports.EXTENSION_DISPLAY_NAME = exports.EXTENSION_NAME = exports.EXTENSION_ID = void 0;
/**
 * EXTENSION_ID: The unique identifier of the extension.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(EXTENSION_ID);
 *
 * @returns {string} - The unique identifier of the extension
 */
exports.EXTENSION_ID = 'autoBarrel';
/**
 * EXTENSION_NAME: The repository ID of the extension.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(EXTENSION_NAME);
 *
 * @returns {string} - The repository ID of the extension
 */
exports.EXTENSION_NAME = 'vscode-auto-barrel';
/**
 * EXTENSION_DISPLAY_NAME: The name of the extension.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(EXTENSION_DISPLAY_NAME);
 *
 * @returns {string} - The name of the extension
 */
exports.EXTENSION_DISPLAY_NAME = 'Auto Barrel';
/**
 * USER_NAME: The ManuelGil of the extension.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(USER_NAME);
 *
 * @returns {string} - The ManuelGil of the extension
 */
exports.USER_NAME = 'ManuelGil';
/**
 * USER_PUBLISHER: The publisher of the extension.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(USER_PUBLISHER);
 *
 * @returns {string} - The publisher of the extension
 */
exports.USER_PUBLISHER = 'imgildev';
/**
 * REPOSITORY_URL: The documentation URL of the extension.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(REPOSITORY_URL);
 *
 * @returns {string} - The documentation URL of the extension
 */
exports.REPOSITORY_URL = `https://github.com/${exports.USER_NAME}/${exports.EXTENSION_NAME}`;
/**
 * DEFAULT_LANGUAGE: The default language.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(DEFAULT_LANGUAGE);
 *
 * @returns {string} - The default language
 */
exports.DEFAULT_LANGUAGE = 'TypeScript';
/**
 * RECURSIVE_BARRELLING: The flag to recursively barrel.
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(RECURSIVE_BARRELLING);
 *
 * @returns {boolean} - The flag to recursively barrel
 */
exports.DISABLE_RECURSIVE = false;
/**
 * INCLUDE: The files to include.
 * @type {string[]}
 * @public
 * @memberof Constants
 * @example
 * console.log(INCLUDE);
 *
 * @returns {string[]} - The files to include
 */
exports.INCLUDE_EXTENSIONS = ['ts', 'tsx', 'vue'];
/**
 * EXCLUDE: The files to exclude.
 * @type {string[]}
 * @public
 * @memberof Constants
 * @example
 * console.log(EXCLUDE);
 *
 * @returns {string[]} - The files to exclude
 */
exports.EXCLUDE_PATTERNS = [
    '**/*.spec.*',
    '**/*.test.*',
    '**/*.e2e.*',
    '**/index.ts',
    '**/index.js',
];
/**
 * RECURSION_DEPTH: The recursion depth.
 * @type {number}
 * @public
 * @memberof Constants
 * @example
 * console.log(RECURSION_DEPTH);
 *
 * @returns {number} - The recursion depth
 */
exports.RECURSION_DEPTH = 0;
/**
 * SUPPORTS_HIDDEN: The flag to support hidden files and directories (files that start with a dot).
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(SUPPORTS_HIDDEN);
 *
 * @returns {boolean} - The flag to support hidden files and directories
 */
exports.SUPPORTS_HIDDEN = true;
/**
 * PRESERVE_GITIGNORE: The flag to preserve the .gitignore file.
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(PRESERVE_GITIGNORE);
 *
 * @returns {boolean} - The flag to preserve the .gitignore file
 */
exports.PRESERVE_GITIGNORE = false;
/**
 * KEEP_EXTENSION: The flag to keep the extension on export.
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(KEEP_EXTENSION);
 *
 * @returns {boolean} - The flag to keep the extension on export
 */
exports.KEEP_EXTENSION = false;
/**
 * DETECT_EXPORTS: The flag to detect exports.
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(DETECT_EXPORTS);
 *
 * @returns {boolean} - The flag to detect exports
 */
exports.DETECT_EXPORTS = false;
/**
 * USE_NAMED_EXPORTS: The flag to use named exports.
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(USE_NAMED_EXPORTS);
 *
 * @returns {boolean} - The flag to use named exports
 */
exports.USE_NAMED_EXPORTS = false;
/**
 * EXPORT_FILENAME: The filename to export the default export.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(EXPORT_FILENAME);
 *
 * @returns {string} - The filename to export the default export
 */
exports.EXPORT_FILENAME = 'filename';
/**
 * DEFAULT_FILENAME: The default filename.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(DEFAULT_FILENAME);
 *
 * @returns {string} - The default filename
 */
exports.DEFAULT_FILENAME = 'index';
/**
 * HEADER_COMMENT_TEMPLATE: The default header comment template.
 * @type {string[]}
 * @public
 * @memberof Constants
 * @example
 * console.log(HEADER_COMMENT_TEMPLATE);
 *
 * @returns {string[]} - The default header comment template
 */
exports.HEADER_COMMENT_TEMPLATE = [];
/**
 * EXCLUDE_SEMICOLON: The flag to exclude a semicolon at the end of a line.
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(EXCLUDE_SEMICOLON);
 *
 * @returns {boolean} - The flag to exclude a semicolon at the end of a line
 */
exports.EXCLUDE_SEMICOLON = false;
/**
 * USE_SINGLE_QUOTES: The flag to use single quotes.
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(USE_SINGLE_QUOTES);
 *
 * @returns {boolean} - The flag to use single quotes
 */
exports.USE_SINGLE_QUOTES = true;
/**
 * END_OF_LINE: The end of line character.
 * @type {string}
 * @public
 * @memberof Constants
 * @example
 * console.log(END_OF_LINE);
 *
 * @returns {string} - The end of line character
 */
exports.END_OF_LINE = 'lf';
/**
 * INSERT_FINAL_NEWLINE: The flag to insert a final newline.
 * @type {boolean}
 * @public
 * @memberof Constants
 * @example
 * console.log(INSERT_FINAL_NEWLINE);
 *
 * @returns {boolean} - The flag to insert a final newline
 */
exports.INSERT_FINAL_NEWLINE = true;
//# sourceMappingURL=constants.config.js.map