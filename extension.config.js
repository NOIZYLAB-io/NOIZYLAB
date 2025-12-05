"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ExtensionConfig = void 0;
const constants_config_1 = require("./constants.config");
/**
 * The Config class.
 *
 * @class
 * @classdesc The class that represents the configuration of the extension.
 * @export
 * @public
 * @property {WorkspaceConfiguration} config - The workspace configuration
 * @property {boolean} enable - The flag to enable the extension
 * @property {string} defaultLanguage - The default language
 * @property {boolean} disableRecursiveBarrelling - The flag to disable recursive barrelling
 * @property {string[]} includeExtensionOnExport - The extensions to include in the export
 * @property {string[]} ignoreFilePathPatternOnExport - The file path patterns to ignore on export
 * @property {number} maxSearchRecursionDepth - The maximum search recursion depth
 * @property {boolean} supportsHiddenFiles - The flag to allow hidden files
 * @property {boolean} preserveGitignoreSettings - The flag to respect the .gitignore file
 * @property {boolean} keepExtensionOnExport - The flag to keep the extension on export
 * @property {boolean} detectExportsInFiles - The flag to detect exports in files
 * @property {string} useNamedExports - The filename to export the default export
 * @property {boolean} exportDefaultFilename - The filename to export the default export
 * @property {string} configuredDefaultFilename - The configured default filename
 * @property {string[]} headerCommentTemplate - The header comment template
 * @property {boolean} excludeSemiColonAtEndOfLine - The flag to exclude a semicolon at the end of a line
 * @property {boolean} useSingleQuotes - The flag to use single quotes
 * @property {string} endOfLine - The end of line character
 * @property {boolean} insertFinalNewline - The flag to insert a final newline
 * @example
 * const config = new Config(workspace.getConfiguration());
 * console.log(config.includeExtensionOnExport);
 * console.log(config.exclude);
 */
class ExtensionConfig {
    // -----------------------------------------------------------------
    // Constructor
    // -----------------------------------------------------------------
    /**
     * Constructor for the Config class.
     *
     * @constructor
     * @param {WorkspaceConfiguration} config - The workspace configuration
     * @public
     * @memberof Config
     */
    constructor(config) {
        this.config = config;
        this.enable = config.get('enable', true);
        this.defaultLanguage = config.get('language.defaultLanguage', constants_config_1.DEFAULT_LANGUAGE);
        this.disableRecursiveBarrelling = config.get('files.disableRecursiveBarrelling', constants_config_1.DISABLE_RECURSIVE);
        this.includeExtensionOnExport = config.get('files.includeExtensionOnExport', constants_config_1.INCLUDE_EXTENSIONS);
        this.ignoreFilePathPatternOnExport = config.get('files.ignoreFilePathPatternOnExport', constants_config_1.EXCLUDE_PATTERNS);
        this.maxSearchRecursionDepth = config.get('files.maxSearchRecursionDepth', constants_config_1.RECURSION_DEPTH);
        this.supportsHiddenFiles = config.get('files.supportsHiddenFiles', constants_config_1.SUPPORTS_HIDDEN);
        this.preserveGitignoreSettings = config.get('files.preserveGitignoreSettings', constants_config_1.PRESERVE_GITIGNORE);
        this.keepExtensionOnExport = config.get('files.keepExtensionOnExport', constants_config_1.KEEP_EXTENSION);
        this.detectExportsInFiles = config.get('files.detectExportsInFiles', constants_config_1.DETECT_EXPORTS);
        this.useNamedExports = config.get('files.useNamedExports', constants_config_1.USE_NAMED_EXPORTS);
        this.exportDefaultFilename = config.get('files.exportDefaultFilename', constants_config_1.EXPORT_FILENAME);
        this.configuredDefaultFilename = config.get('files.configuredDefaultFilename', constants_config_1.DEFAULT_FILENAME);
        this.headerCommentTemplate = config.get('formatting.headerCommentTemplate', constants_config_1.HEADER_COMMENT_TEMPLATE);
        this.excludeSemiColonAtEndOfLine = config.get('formatting.excludeSemiColonAtEndOfLine', constants_config_1.EXCLUDE_SEMICOLON);
        this.useSingleQuotes = config.get('formatting.useSingleQuotes', constants_config_1.USE_SINGLE_QUOTES);
        this.endOfLine = config.get('formatting.endOfLine', constants_config_1.END_OF_LINE);
        this.insertFinalNewline = config.get('formatting.insertFinalNewline', constants_config_1.INSERT_FINAL_NEWLINE);
    }
    // -----------------------------------------------------------------
    // Methods
    // -----------------------------------------------------------------
    // Public methods
    /**
     * The update method.
     *
     * @function update
     * @param {WorkspaceConfiguration} config - The workspace configuration
     * @public
     * @memberof Config
     * @example
     * const config = new Config(workspace.getConfiguration());
     * config.update(workspace.getConfiguration());
     */
    update(config) {
        this.enable = config.get('enable', this.enable);
        this.defaultLanguage = config.get('language.defaultLanguage', this.defaultLanguage);
        this.disableRecursiveBarrelling = config.get('files.disableRecursiveBarrelling', this.disableRecursiveBarrelling);
        this.includeExtensionOnExport = config.get('files.includeExtensionOnExport', this.includeExtensionOnExport);
        this.ignoreFilePathPatternOnExport = config.get('files.ignoreFilePathPatternOnExport', this.ignoreFilePathPatternOnExport);
        this.maxSearchRecursionDepth = config.get('files.maxSearchRecursionDepth', this.maxSearchRecursionDepth);
        this.supportsHiddenFiles = config.get('files.supportsHiddenFiles', this.supportsHiddenFiles);
        this.preserveGitignoreSettings = config.get('files.preserveGitignoreSettings', this.preserveGitignoreSettings);
        this.keepExtensionOnExport = config.get('files.keepExtensionOnExport', this.keepExtensionOnExport);
        this.detectExportsInFiles = config.get('files.detectExportsInFiles', this.detectExportsInFiles);
        this.useNamedExports = config.get('files.useNamedExports', this.useNamedExports);
        this.exportDefaultFilename = config.get('files.exportDefaultFilename', this.exportDefaultFilename);
        this.configuredDefaultFilename = config.get('files.configuredDefaultFilename', this.configuredDefaultFilename);
        this.headerCommentTemplate = config.get('formatting.headerCommentTemplate', this.headerCommentTemplate);
        this.excludeSemiColonAtEndOfLine = config.get('formatting.excludeSemiColonAtEndOfLine', this.excludeSemiColonAtEndOfLine);
        this.useSingleQuotes = config.get('formatting.useSingleQuotes', this.useSingleQuotes);
        this.endOfLine = config.get('formatting.endOfLine', this.endOfLine);
        this.insertFinalNewline = config.get('formatting.insertFinalNewline', this.insertFinalNewline);
    }
}
exports.ExtensionConfig = ExtensionConfig;
//# sourceMappingURL=extension.config.js.map