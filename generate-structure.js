"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.generateStructure = generateStructure;
const fs_1 = require("fs");
const path_1 = require("path");
const find_files_1 = require("./find-files");
const get_prefix_1 = require("./get-prefix");
async function generateStructure(folderPath, excludePatterns, style, allowRecursion = true, // Toggle recursive search
respectGitignore = false // Toggle .gitignore usage
) {
    let structure = '';
    // Retrieve the sorted items using the optimized findFiles function.
    const items = await (0, find_files_1.findFiles)(folderPath, // Base directory
    ['**/*'], // Include all files and directories
    excludePatterns, // Exclude patterns
    allowRecursion, // Recursive search
    respectGitignore // Respect .gitignore if enabled
    );
    // Iterate over each sorted item to build the structure.
    for (const [index, item] of items.entries()) {
        const fullPath = (0, path_1.resolve)(item); // Ensure full path
        const isFolder = (0, fs_1.statSync)(fullPath).isDirectory();
        const isLastItem = index === items.length - 1;
        // Calculate the depth (number of subdirectories) based on the relative path.
        const currentDepth = fullPath.split(path_1.sep).length - folderPath.split(path_1.sep).length;
        // Get the prefix for the current item based on its depth, style, if it's the last item, and if it's a file.
        const prefix = (0, get_prefix_1.getPrefix)(currentDepth, style, isLastItem, !isFolder);
        // Append the item (using its basename) to the structure.
        structure += `${prefix}${(0, path_1.basename)(item)}\n`;
    }
    return structure;
}
//# sourceMappingURL=generate-structure.js.map