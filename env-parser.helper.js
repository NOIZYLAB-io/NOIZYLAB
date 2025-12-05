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
exports.parseEnv = parseEnv;
/**
 * Parses .env content using the dotenv library.
 * Throws a formatted error if parsing fails.
 *
 * @param content The ENV string to parse.
 * @returns The parsed object.
 * @throws Error if parsing fails.
 *
 * @example
 * const obj = parseEnv('FOO=bar\nBAZ=qux');
 * // { FOO: 'bar', BAZ: 'qux' }
 */
const dotenv = __importStar(require("dotenv"));
const error_handler_helper_1 = require("./error-handler.helper");
function parseEnv(content) {
    try {
        return dotenv.parse(content);
    }
    catch (error) {
        (0, error_handler_helper_1.throwError)('Failed to parse ENV', error);
    }
}
//# sourceMappingURL=env-parser.helper.js.map