"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.findFiles = findFiles;
const fastGlob = require("fast-glob");
const fs_1 = require("fs");
const ignore_1 = require("ignore");
const path_1 = require("path");
async function findFiles(baseDir, include, // Include patterns
exclude, // Exclude patterns
allowRecursion = true, // Toggle recursive search
respectGitignore = false // Toggle .gitignore usage
) {
    // Load .gitignore if needed
    let gitignore;
    if (respectGitignore) {
        const gitignorePath = (0, path_1.join)(baseDir, '.gitignore');
        if ((0, fs_1.existsSync)(gitignorePath)) {
            gitignore = (0, ignore_1.default)().add((0, fs_1.readFileSync)(gitignorePath, "utf8"));
        }
    }
    // Configure fast-glob options
    const options = {
        cwd: baseDir, // Base directory
        absolute: true, // Return absolute paths
        onlyFiles: false, // Return files and directories
        dot: true, // Include dotfiles
        deep: allowRecursion ? Infinity : 1, // Recursive or not
        ignore: exclude, // Exclude patterns
    };
    try {
        // Retrieve matching paths using fast-glob
        const filePaths = await fastGlob(include, options);
        // Filter out paths that match .gitignore patterns, if enabled
        let filteredPaths = gitignore
            ? filePaths.filter((filePath) => {
                const relativePath = (0, path_1.relative)(baseDir, filePath);
                return !gitignore.ignores(relativePath);
            })
            : filePaths;
        // Custom sorting: for each directory level, ensure directories come before files.
        filteredPaths.sort((a, b) => {
            // Get the paths relative to the base directory.
            const aRel = (0, path_1.relative)(baseDir, a);
            const bRel = (0, path_1.relative)(baseDir, b);
            // Split the relative paths into segments.
            const aParts = aRel.split(path_1.sep);
            const bParts = bRel.split(path_1.sep);
            const minLen = Math.min(aParts.length, bParts.length);
            // Compare each segment.
            for (let i = 0; i < minLen; i++) {
                if (aParts[i] !== bParts[i]) {
                    // Build the partial paths up to the current segment.
                    const aSegmentPath = (0, path_1.join)(baseDir, ...aParts.slice(0, i + 1));
                    const bSegmentPath = (0, path_1.join)(baseDir, ...bParts.slice(0, i + 1));
                    // Determine if the segment represents a directory.
                    const aIsDir = (0, fs_1.statSync)(aSegmentPath).isDirectory();
                    const bIsDir = (0, fs_1.statSync)(bSegmentPath).isDirectory();
                    // If one segment is a directory and the other is not, order the directory first.
                    if (aIsDir && !bIsDir) {
                        return -1;
                    }
                    if (!aIsDir && bIsDir) {
                        return 1;
                    }
                    // If both segments are of the same type, sort alphabetically.
                    return aParts[i].localeCompare(bParts[i]);
                }
            }
            // If all segments compared are equal, the path with fewer segments (i.e. the parent) comes first.
            return aParts.length - bParts.length;
        });
        return filteredPaths;
    }
    catch (error) {
        console.error('Error while finding files:', error);
        throw error;
    }
}
//# sourceMappingURL=find-files.js.map