"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.generateLanguageDefinitions = generateLanguageDefinitions;
exports.parseSapfHelpOutput = parseSapfHelpOutput;
const fs = __importStar(require("fs"));
const child_process_1 = require("child_process");
/**
 * Generate function definitions from SAPF helpall output
 */
async function generateLanguageDefinitions(sapfPath, preludePath) {
    try {
        // Build command arguments
        const args = [];
        if (preludePath != null && preludePath.trim() !== '' && fs.existsSync(preludePath)) {
            args.push('-p', preludePath);
        }
        else if (preludePath != null && preludePath.trim() !== '') {
            throw new Error(`Prelude file not found: ${preludePath}`);
        }
        // Generate helpall output using spawn
        const output = await new Promise((resolve, reject) => {
            const child = (0, child_process_1.spawn)(sapfPath, args, {
                stdio: ['pipe', 'pipe', 'pipe'],
                env: process.env,
            });
            let stdout = '';
            let stderr = '';
            child.stdout.on('data', (data) => {
                stdout += data.toString();
            });
            child.stderr.on('data', (data) => {
                stderr += data.toString();
            });
            child.on('close', (code) => {
                if (code === 0) {
                    resolve(stdout);
                }
                else {
                    reject(new Error(`Process exited with code ${code}. stderr: ${stderr}`));
                }
            });
            child.on('error', (err) => {
                reject(err);
            });
            // Send helpall command and quit
            child.stdin.write('helpall\n');
            child.stdin.write('quit\n');
            child.stdin.end();
        });
        // Parse the output
        return parseSapfHelpOutput(output);
    }
    catch (error) {
        throw new Error(`Failed to generate function definitions: ${error}`);
    }
}
/**
 * Parse SAPF helpall output into structured function definitions
 */
function parseSapfHelpOutput(output) {
    const lines = output.split('\n');
    const result = {};
    let currentCategory = null;
    let inFunctionSection = false;
    for (const line of lines) {
        // Skip header lines until we reach "BUILT IN FUNCTIONS"
        if (line.includes('BUILT IN FUNCTIONS')) {
            inFunctionSection = true;
            continue;
        }
        if (!inFunctionSection) {
            continue;
        }
        // Detect category headers: *** category name ***
        const categoryMatch = line.match(/^\*\*\* (.+) \*\*\*$/);
        if (categoryMatch) {
            const [, categoryName] = categoryMatch;
            currentCategory = categoryName;
            // Only create new category if it doesn't exist, otherwise merge
            result[currentCategory] ??= { items: {} };
            continue;
        }
        // Parse function definitions
        if (currentCategory != null && line.trim() && !line.startsWith(' Argument Automapping')) {
            // Try main pattern: function with signature and description
            const functionMatch = line.match(/^ ([^\s]+) (\([^)]*\)|@\w+\s*\([^)]*\)) (.+)$/);
            if (functionMatch) {
                const [, functionName, signature, description] = functionMatch;
                // Handle special annotations like @k, @kk, @ak
                let special = null;
                let cleanSignature = signature;
                const specialMatch = signature.match(/^@(\w+)\s*(.+)$/);
                if (specialMatch) {
                    const [, specialType, sigContent] = specialMatch;
                    special = specialType;
                    cleanSignature = sigContent;
                }
                // Build description with special annotation if present
                let fullDescription = description;
                if (special != null) {
                    fullDescription = `@${special} ${cleanSignature} ${description}`;
                }
                else {
                    fullDescription = `${cleanSignature} ${description}`;
                }
                result[currentCategory].items[functionName] = fullDescription;
            }
            // Try pattern for operator variants with extra indentation (op/, op\, etc.)
            else if (line.match(/^\s{6,}/)) {
                const opMatch = line.match(/^\s+([^\s]+)\s+(\([^)]*\))\s+(.+)$/);
                if (opMatch) {
                    const [, functionName, signature, description] = opMatch;
                    result[currentCategory].items[functionName] = `${signature} ${description}`;
                }
            }
            // Try pattern for functions with signature but no description (or just whitespace)
            else {
                const sigOnlyMatch = line.match(/^ ([^\s]+) (\([^)]*\)|@\w+\s*\([^)]*\))\s*$/);
                if (sigOnlyMatch) {
                    const [, functionName, signature] = sigOnlyMatch;
                    result[currentCategory].items[functionName] = signature;
                }
                // Try pattern for functions without signature (name - description)
                else {
                    const noSigMatch = line.match(/^ ([^\s]+) - (.+)$/);
                    if (noSigMatch) {
                        const [, functionName, description] = noSigMatch;
                        result[currentCategory].items[functionName] = description;
                    }
                }
            }
        }
    }
    return result;
}
//# sourceMappingURL=generator.js.map