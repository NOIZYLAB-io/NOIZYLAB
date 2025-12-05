"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getComponentMetadata = void 0;
const vscode = require("vscode");
const scule_1 = require("scule");
const logger_1 = require("./logger");
let metadataCache = null;
let lastSuccessfulFile = null;
let lastFetch = 0;
const DEFAULT_CACHE_TTL_MINUTES = 30; // 30 minutes
/**
 * Fetches metadata from a specified URL with optional force parameter.
 *
 * @param {string} url - The URL endpoint to fetch metadata from
 * @param {boolean} force - When true, displays VS Code information messages during fetch process. Defaults to false.
 * @returns A Promise that resolves to the fetched metadata object, or null if the fetch fails
 * @throws Will throw an error if the fetch response is not ok
 */
function fetchRemoteComponentMetadata(url, force = false) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            (0, logger_1.logger)(`Fetching MDC component metadata from: ${url}`);
            vscode.window.showInformationMessage(`MDC: Fetching component metadata from: ${url}`);
            const response = yield fetch(url);
            if (!response.ok) {
                throw new Error(`Failed to fetch MDC component metadata: ${response.statusText}`);
            }
            // Convert response to Uint8Array for consistency with file processing
            const data = new Uint8Array(yield response.arrayBuffer());
            const metadata = processMetadataFile({
                metadataContent: data,
                filePath: url,
                force,
                source: 'remote'
            });
            if (metadata) {
                const message = `MDC: Component metadata fetched successfully (${metadata.length} components found).`;
                vscode.window.showInformationMessage(message);
                const config = vscode.workspace.getConfiguration('mdc');
                if (config.get('debug')) {
                    (0, logger_1.logger)(message);
                }
            }
            return metadata;
        }
        catch (error) {
            const errorMessage = `MDC: ${error.message}`;
            (0, logger_1.logger)(errorMessage, 'error');
            vscode.window.showErrorMessage(errorMessage);
            return null;
        }
    });
}
/**
 * Processes a metadata file containing MDC component information.
 *
 * @param {ProcessMetadataOptions} options - Configuration options for processing metadata
 * @returns {MDCComponentData[]} An array of MDCComponentData objects sorted by component name, or null if processing fails.
 *
 * @description
 * This function performs the following steps:
 * 1. Decodes the file content from Uint8Array to text
 * 2. Extracts the default export object using regex
 * 3. Parses the JSON content
 * 4. Creates a map of component metadata, converting component names to kebab-case
 * 5. Sorts the components by name
 */
const processMetadataFile = ({ metadataContent, filePath, source = 'local', force = false }) => {
    const config = vscode.workspace.getConfiguration('mdc');
    const textContent = new TextDecoder().decode(metadataContent);
    (0, logger_1.logger)(`Processing ${source} metadata from: ${filePath}`);
    // Try parsing as direct JSON first
    try {
        const directContent = JSON.parse(textContent);
        if (Array.isArray(directContent) &&
            directContent.length > 0 &&
            'mdc_name' in directContent[0] &&
            'component_meta' in directContent[0] &&
            'meta' in directContent[0].component_meta) {
            const config = vscode.workspace.getConfiguration('mdc');
            if (config.get('debug')) {
                (0, logger_1.logger)(`${directContent.length} components found (no data transformation needed).`);
            }
            return directContent;
        }
        // If we got here, the JSON was valid but needs transformation
        (0, logger_1.logger)('Valid JSON found, attempting data transformation...');
        // Try transforming the JSON content
        const componentsMap = new Map();
        Object.values(directContent).forEach((componentMeta) => {
            const kebabCaseName = (0, scule_1.kebabCase)(componentMeta.kebabName || componentMeta.pascalName);
            if (!componentsMap.has(kebabCaseName)) {
                componentsMap.set(kebabCaseName, {
                    mdc_name: kebabCaseName,
                    component_meta: componentMeta
                });
            }
        });
        // Sort the array of component metadata entries based on mdc_name.
        const metadata = Array.from(componentsMap.values()).sort((a, b) => a.mdc_name.localeCompare(b.mdc_name));
        if (config.get('debug')) {
            (0, logger_1.logger)(`${metadata === null || metadata === void 0 ? void 0 : metadata.length} components found (transformed data format).`);
        }
        return metadata;
    }
    catch (error) {
        // JSON parse failed, if this is a local file, try export pattern
        if (source === 'local') {
            (0, logger_1.logger)('Direct JSON parse failed, checking for export pattern...');
            const match = textContent.match(/export\s+default\s+([{[][\s\S]*?\n[}\]])/m);
            if (match === null || match === void 0 ? void 0 : match[1]) {
                try {
                    return processMetadataFile({
                        metadataContent: new TextEncoder().encode(match[1]),
                        filePath,
                        force,
                        source: 'remote' // Treat exported content as if it were remote JSON
                    });
                }
                catch (exportError) {
                    (0, logger_1.logger)('Export pattern processing failed.', 'error');
                }
            }
        }
    }
    (0, logger_1.logger)(`Unable to process ${source} metadata content from: ${filePath}`, 'error');
    return null;
};
/**
 * Attempts to find and load local component metadata from `.nuxt/component-meta.mjs` files in the current workspace or its subdirectories.
 */
function fetchLocalComponentMetadata(force = false) {
    return __awaiter(this, void 0, void 0, function* () {
        const config = vscode.workspace.getConfiguration('mdc');
        const metadataFilePattern = config.get('componentMetadataLocalFilePattern', '**/.nuxt/component-meta.mjs');
        const metadataExcludeDirectoriesPattern = config.get('componentMetadataLocalExcludePattern', '{**/node_modules/**,**/dist/**,**/.output/**,**/.cache/**,**/.playground/**}');
        try {
            const workspaceFolders = vscode.workspace.workspaceFolders;
            if (!(workspaceFolders === null || workspaceFolders === void 0 ? void 0 : workspaceFolders.length)) {
                (0, logger_1.logger)('No workspace folders found.');
                return null;
            }
            // If we have a cached file path and this isn't a force refresh, try it first
            if (!force && lastSuccessfulFile) {
                try {
                    const fileContent = yield vscode.workspace.fs.readFile(vscode.Uri.file(lastSuccessfulFile));
                    const metadata = processMetadataFile({
                        metadataContent: fileContent,
                        filePath: lastSuccessfulFile,
                        force,
                        source: 'local'
                    });
                    if (metadata) {
                        return metadata;
                    }
                    // If processing failed, clear the cache and continue with full search
                    lastSuccessfulFile = null;
                }
                catch (error) {
                    (0, logger_1.logger)(`Cached file no longer accessible: ${error.message}`);
                    lastSuccessfulFile = null;
                }
            }
            // Full file search if needed
            const sourceFilePattern = new vscode.RelativePattern(workspaceFolders[0], metadataFilePattern);
            // Find files, excluding the provided directory patterns
            const files = yield vscode.workspace.findFiles(sourceFilePattern, metadataExcludeDirectoriesPattern);
            if (!files.length) {
                (0, logger_1.logger)('No files found.');
                return null;
            }
            // Try each file until we find valid metadata
            for (const file of files) {
                (0, logger_1.logger)(`Attempting to read metadata file: ${file.fsPath}`);
                try {
                    const fileContent = yield vscode.workspace.fs.readFile(file);
                    const metadata = processMetadataFile({
                        metadataContent: fileContent,
                        filePath: file.fsPath,
                        force,
                        source: 'local'
                    });
                    if (metadata) {
                        lastSuccessfulFile = file.fsPath;
                        return metadata;
                    }
                }
                catch (parseError) {
                    (0, logger_1.logger)(`Error parsing metadata from ${file.fsPath}: ${parseError}`, 'error');
                    continue;
                }
            }
            (0, logger_1.logger)('No valid metadata found in available sources.');
            return null;
        }
        catch (error) {
            (0, logger_1.logger)(`Error loading local metadata: ${error.message}`, 'error');
            return null;
        }
    });
}
/**
 * Retrieves metadata from a configured URL with caching support.
 * @param {boolean} force - When true, bypasses cache and forces a new fetch. Defaults to false.
 * @returns {Promise<MDCComponentData[]>} Promise resolving to metadata object, or null if URL is not configured or fetch fails
 * @throws {Error} Potentially throws if network request fails
 *
 * The function will:
 * - Check configuration for metadata URL and cache TTL
 * - Show warning if force=true but URL not configured
 * - Return cached data if within TTL period
 * - Fetch new data if cache expired or force=true
 * - Update cache with new data if fetch successful
 */
function getComponentMetadata(force = false) {
    return __awaiter(this, void 0, void 0, function* () {
        const config = vscode.workspace.getConfiguration('mdc');
        const componentCompletionsEnabled = config.get('enableComponentMetadataCompletions', false);
        const componentMetadataCacheTTL = 60 * 1000 * Number(config.get('componentMetadataCacheTTL') || DEFAULT_CACHE_TTL_MINUTES);
        const now = Date.now();
        // Check if we should skip fetching (not forced and within TTL)
        if (!force && lastFetch > 0 && (now - lastFetch) < componentMetadataCacheTTL) {
            if (metadataCache) {
                return metadataCache;
            }
            return null;
        }
        // If completions are disabled, update lastFetch and return
        if (!componentCompletionsEnabled) {
            const message = 'MDC: Component metadata suggestions are not enabled.';
            (0, logger_1.logger)(message);
            vscode.window.showInformationMessage(message);
            lastFetch = now; // Remember this check even if disabled
            return null;
        }
        // Clear cache if forcing refresh
        if (force) {
            (0, logger_1.logger)('Fetching MDC component metadata and clearing cache...');
            metadataCache = null;
            lastFetch = 0;
        }
        let metadata = null;
        const componentMetadataURL = config.get('componentMetadataURL');
        // If URL is configured, only use remote metadata
        if (componentMetadataURL) {
            (0, logger_1.logger)('Attempting to fetch remote metadata...');
            metadata = yield fetchRemoteComponentMetadata(componentMetadataURL, force);
        }
        else {
            // Only try local metadata if no URL is configured
            metadata = yield fetchLocalComponentMetadata(force);
        }
        // Always update lastFetch after any attempt
        lastFetch = now;
        if (metadata) {
            (0, logger_1.logger)('Metadata fetch successful, updating cache.');
            metadataCache = metadata;
            return metadata;
        }
        return null;
    });
}
exports.getComponentMetadata = getComponentMetadata;
//# sourceMappingURL=component-metadata.js.map