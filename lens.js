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
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.CodeLensProvider = void 0;
const vscode = __importStar(require("vscode"));
const path_1 = __importDefault(require("path"));
const lens_1 = require("../@types/lens");
const cmd_1 = require("../@types/cmd");
const logger_1 = require("../util/logger");
class CodeLensProvider {
    constructor(disposable, keploy) {
        this.keploy = keploy;
        const languages = [
            lens_1.Language.JAVASCRIPT,
            lens_1.Language.TYPESCRIPT,
            lens_1.Language.JSX,
            lens_1.Language.TSX,
            lens_1.Language.PYTHON,
            lens_1.Language.GO,
            lens_1.Language.JAVA,
        ];
        // Register CodeLens provider for each language
        languages.forEach((language) => {
            const providerDisposable = vscode.languages.registerCodeLensProvider({ language, scheme: 'file' }, this);
            disposable.push(providerDisposable);
        });
    }
    provideCodeLenses(document) {
        return __awaiter(this, void 0, void 0, function* () {
            const fileName = document.uri.fsPath;
            // Skip test files
            if (fileName.endsWith('.test.js') ||
                fileName.endsWith('.test.ts') ||
                fileName.endsWith('Tests.java') ||
                fileName.endsWith('Test.java') ||
                fileName.includes('/Test') ||
                fileName.includes('/test/') ||
                fileName.endsWith('_test.go') ||
                fileName.includes('test_')) {
                return [];
            }
            logger_1.Logger.info('fileName in codeLens:', fileName);
            const fileExtension = path_1.default.extname(fileName);
            const codeLenses = [];
            try {
                const functionNames = yield this.keploy.GetAllFunctionsInFile(fileName, fileExtension);
                functionNames.forEach((functionInfo) => {
                    const range = new vscode.Range(functionInfo.line, 0, functionInfo.line, 0);
                    const conf = {
                        filePath: document.uri.fsPath,
                        functionName: functionInfo.name,
                        singleUtgTest: false, // Default value
                        additional_prompts: "",
                    };
                    codeLenses.push(new vscode.CodeLens(range, {
                        title: `🐰 Generate unit test for this function`,
                        command: cmd_1.KeployCommand.RUN_UTG,
                        arguments: [Object.assign(Object.assign({}, conf), { singleUtgTest: true })],
                    }));
                    codeLenses.push(new vscode.CodeLens(range, {
                        title: `🐰 Generate unit test for entire file`,
                        command: cmd_1.KeployCommand.RUN_UTG,
                        arguments: [Object.assign(Object.assign({}, conf), { singleUtgTest: false })],
                    }));
                });
            }
            catch (error) {
                logger_1.Logger.error('Error while processing functions:', error);
            }
            return codeLenses;
        });
    }
}
exports.CodeLensProvider = CodeLensProvider;
//# sourceMappingURL=lens.js.map