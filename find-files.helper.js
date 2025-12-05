"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.findFiles = exports.getCacheStats = exports.clearCache = void 0;
const fast_glob_1 = __importDefault(require("fast-glob"));
const ignore_1 = __importDefault(require("ignore"));
const path_1 = require("path");
const vscode_1 = require("vscode");
// Shared cache for all file operations across the extension
const findFilesCache = new Map();
const findFilesCacheTTL = 5 * 60 * 1000; // 5 minutes
const findFilesInFlight = new Map();
const MAX_FILES_TO_INDEX_LIMIT = 5000;
const MAX_CACHE_SIZE = 100;
const toPosix = (filePath) => filePath.replace(/\\/g, '/');
const getIgnoreMatcher = async (options) => {
    const { baseDirectoryPath, excludedPatterns, enableGitignoreDetection } = options;
    const ignoreMatcher = (0, ignore_1.default)();
    if (excludedPatterns.length) {
        ignoreMatcher.add(excludedPatterns.map(toPosix));
    }
    if (enableGitignoreDetection) {
        try {
            const gitignoreUri = vscode_1.Uri.joinPath(vscode_1.Uri.file(baseDirectoryPath), '.gitignore');
            await vscode_1.workspace.fs.stat(gitignoreUri);
            const data = await vscode_1.workspace.fs.readFile(gitignoreUri);
            const content = new TextDecoder('utf-8').decode(data);
            ignoreMatcher.add(content);
        }
        catch {
            // no .gitignore or not accessible - ignore
        }
    }
    return ignoreMatcher;
};
const findFilesRemote = async (options, workspaceFolder, ignoreMatcher) => {
    const { includeFilePatterns, excludedPatterns = [] } = options;
    const seen = new Set();
    const aggregated = [];
    const posixExcluded = excludedPatterns.map(toPosix);
    const combinedExclude = posixExcluded.length > 0 ? `{${posixExcluded.join(',')}}` : undefined;
    let total = 0;
    for (const includePatternGlob of includeFilePatterns) {
        if (total >= MAX_FILES_TO_INDEX_LIMIT) {
            break;
        }
        const relativePattern = new vscode_1.RelativePattern(workspaceFolder, includePatternGlob);
        const found = await vscode_1.workspace.findFiles(relativePattern, combinedExclude, MAX_FILES_TO_INDEX_LIMIT - total);
        for (const fileUri of found) {
            if (seen.has(fileUri.fsPath)) {
                continue;
            }
            seen.add(fileUri.fsPath);
            aggregated.push(fileUri);
            total++;
            if (total >= MAX_FILES_TO_INDEX_LIMIT) {
                break;
            }
        }
    }
    const basePosix = toPosix(options.baseDirectoryPath).replace(/\/$/, '');
    const filterByDepth = (candidateUri) => {
        if (options.disableRecursive) {
            const rel = toPosix(candidateUri.fsPath).slice(basePosix.length + 1);
            return !rel.includes('/');
        }
        if (!options.maxRecursionDepth || options.maxRecursionDepth <= 0) {
            return true;
        }
        const relativeFilePath = toPosix(candidateUri.fsPath).slice(basePosix.length + 1);
        const segments = relativeFilePath.split('/');
        const folderDepth = Math.max(0, segments.length - 1);
        return folderDepth <= options.maxRecursionDepth;
    };
    const filterDotfiles = (candidateUri) => {
        if (options.includeDotfiles) {
            return true;
        }
        const relative = vscode_1.workspace.asRelativePath(candidateUri, false);
        return !relative.split(/[\\\/]/).some((s) => s.startsWith('.'));
    };
    const filterIgnored = (candidateUri) => {
        if (!ignoreMatcher) {
            return true;
        }
        const filePosix = toPosix(candidateUri.fsPath);
        const relativeFilePath = path_1.posix.relative(basePosix, filePosix);
        return !ignoreMatcher.ignores(relativeFilePath);
    };
    return aggregated
        .filter(filterByDepth)
        .filter(filterDotfiles)
        .filter(filterIgnored)
        .sort((a, b) => a.fsPath.localeCompare(b.fsPath))
        .slice(0, MAX_FILES_TO_INDEX_LIMIT);
};
const findFilesLocal = async (options, ignoreMatcher) => {
    const { baseDirectoryPath, includeFilePatterns, excludedPatterns = [], } = options;
    const includeGlobs = includeFilePatterns.map(toPosix);
    const aggregatedUris = [];
    const seenPaths = new Set();
    let totalCollected = 0;
    const stream = fast_glob_1.default.stream(includeGlobs, {
        cwd: baseDirectoryPath,
        dot: options.includeDotfiles,
        ignore: excludedPatterns.map(toPosix),
        onlyFiles: true,
        unique: true,
        followSymbolicLinks: true,
        absolute: true,
    });
    try {
        for await (const matchedPath of stream) {
            if (!matchedPath) {
                continue;
            }
            const absolutePosixPath = toPosix(matchedPath);
            if (seenPaths.has(absolutePosixPath)) {
                continue;
            }
            const candidateUri = vscode_1.Uri.file(matchedPath);
            const basePosix = toPosix(baseDirectoryPath).replace(/\/$/, '');
            const relPath = absolutePosixPath.startsWith(`${basePosix}/`)
                ? absolutePosixPath.slice(basePosix.length + 1)
                : absolutePosixPath;
            if (options.disableRecursive && relPath.includes('/')) {
                continue;
            }
            if (!options.disableRecursive &&
                options.maxRecursionDepth &&
                options.maxRecursionDepth > 0) {
                const segments = relPath.split('/');
                const folderDepth = Math.max(0, segments.length - 1);
                if (folderDepth > options.maxRecursionDepth) {
                    continue;
                }
            }
            if (!options.includeDotfiles) {
                const relativeForDot = vscode_1.workspace.asRelativePath(candidateUri, false);
                if (relativeForDot.split(/[\\\/]/).some((seg) => seg.startsWith('.'))) {
                    continue;
                }
            }
            if (ignoreMatcher) {
                const relativePathForIgnore = path_1.posix.relative(basePosix, absolutePosixPath);
                if (ignoreMatcher.ignores(relativePathForIgnore)) {
                    continue;
                }
            }
            seenPaths.add(absolutePosixPath);
            aggregatedUris.push(candidateUri);
            totalCollected++;
            if (totalCollected >= MAX_FILES_TO_INDEX_LIMIT) {
                if (typeof stream.destroy === 'function') {
                    try {
                        stream.destroy();
                    }
                    catch {
                        // ignore
                    }
                }
                break;
            }
        }
    }
    catch (streamErr) {
        try {
            if (typeof stream.destroy === 'function') {
                stream.destroy();
            }
        }
        catch {
            // ignore
        }
        throw streamErr;
    }
    return aggregatedUris
        .sort((a, b) => a.fsPath.localeCompare(b.fsPath))
        .slice(0, MAX_FILES_TO_INDEX_LIMIT);
};
const updateCache = (cacheKey, files) => {
    const now = Date.now();
    // Evict old entries
    for (const [key, cachedEntry] of findFilesCache.entries()) {
        if (now - cachedEntry.timestamp >= findFilesCacheTTL) {
            findFilesCache.delete(key);
        }
    }
    // Evict oldest if cache is full
    if (findFilesCache.size >= MAX_CACHE_SIZE) {
        const entriesByAge = Array.from(findFilesCache.entries()).sort((a, b) => a[1].timestamp - b[1].timestamp);
        const excess = findFilesCache.size - MAX_CACHE_SIZE + 1;
        for (let i = 0; i < excess; i++) {
            findFilesCache.delete(entriesByAge[i][0]);
        }
    }
    findFilesCache.set(cacheKey, { files, timestamp: now });
};
/**
 * Clears the shared cache for file operations.
 * Useful when files have been created, deleted, or modified.
 *
 * @function clearCache
 * @public
 * @example
 * clearCache();
 *
 * @returns {void} - No return value
 */
const clearCache = () => {
    findFilesCache.clear();
    findFilesInFlight.clear();
};
exports.clearCache = clearCache;
/**
 * Gets cache statistics for monitoring and debugging.
 *
 * @function getCacheStats
 * @public
 * @example
 * const stats = getCacheStats();
 *
 * @returns {{ size: number; maxSize: number; ttl: number }} - Cache statistics
 */
const getCacheStats = () => {
    return {
        size: findFilesCache.size,
        maxSize: MAX_CACHE_SIZE,
        ttl: findFilesCacheTTL,
    };
};
exports.getCacheStats = getCacheStats;
/**
 * Searches for files in a directory that match specified patterns, with optimized performance.
 * Uses fast-glob for discovery and applies post-filters for recursion depth, dotfiles, and optional .gitignore rules.
 * Includes shared caching and optimizations for large projects with many files.
 *
 * @param {FindFilesOptions} options - The options for the file search.
 * @returns {Promise<Uri[]>} Array of VS Code Uri objects for the found files.
 * @throws {Error} If an error occurs during file search, it is caught and a message is displayed.
 */
const findFiles = async (options) => {
    const { baseDirectoryPath, includeFilePatterns, excludedPatterns = [], disableRecursive = false, maxRecursionDepth = 0, includeDotfiles = false, enableGitignoreDetection = false, } = options;
    try {
        if (!includeFilePatterns.length) {
            return [];
        }
        const cacheKey = JSON.stringify({
            baseDir: baseDirectoryPath,
            include: [...includeFilePatterns].map(toPosix).sort(),
            exclude: [...excludedPatterns].map(toPosix).sort(),
            disableRecursive,
            maxRecursionDepth,
            includeDotfiles,
            enableGitignoreDetection,
        });
        const ongoing = findFilesInFlight.get(cacheKey);
        if (ongoing) {
            return ongoing;
        }
        const work = (async () => {
            const cached = findFilesCache.get(cacheKey);
            if (cached && Date.now() - cached.timestamp < findFilesCacheTTL) {
                return cached.files;
            }
            const ignoreMatcher = await getIgnoreMatcher({
                baseDirectoryPath,
                excludedPatterns,
                enableGitignoreDetection,
            });
            const baseUri = vscode_1.Uri.file(baseDirectoryPath);
            const workspaceFolder = vscode_1.workspace.getWorkspaceFolder(baseUri);
            const isRemoteWorkspace = !!workspaceFolder?.uri.scheme && workspaceFolder.uri.scheme !== 'file';
            let results;
            if (isRemoteWorkspace) {
                results = await findFilesRemote(options, workspaceFolder, ignoreMatcher);
            }
            else {
                results = await findFilesLocal(options, ignoreMatcher);
            }
            updateCache(cacheKey, results);
            return results;
        })();
        findFilesInFlight.set(cacheKey, work);
        try {
            return await work;
        }
        finally {
            findFilesInFlight.delete(cacheKey);
        }
    }
    catch (error) {
        const errorInstance = error instanceof Error ? error : new Error(String(error));
        console.error('findFiles error', errorInstance);
        try {
            const errorMessage = errorInstance?.message ?? String(errorInstance);
            vscode_1.window.showErrorMessage(errorMessage);
        }
        catch {
            // ignore UI errors
        }
        return [];
    }
};
exports.findFiles = findFiles;
//# sourceMappingURL=find-files.helper.js.map