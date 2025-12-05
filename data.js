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
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.updateData = exports.getPath = void 0;
const vscode_1 = __importDefault(require("vscode"));
const fs = __importStar(require("node:fs"));
const path = __importStar(require("node:path"));
const utils_1 = require("./utils");
const fetch_1 = require("./fetch");
let data = null;
async function getPath(context, word) {
    let path = "about:blank";
    if (data === null) {
        data = await initData(context);
    }
    const filtered = data
        .filter((i) => i.name.includes(word))
        .sort((a, b) => a.name.length - b.name.length);
    if (filtered.length == 1) {
        path = filtered[0].link;
    }
    else {
        const result = await vscode_1.default.window.showQuickPick([
            ...filtered.map((e, i) => ({
                label: `$(${(0, utils_1.getIcon)(e)}) ${e.name}`,
                description: "note" in e ? e.note : undefined,
                detail: (0, utils_1.getDescription)(e),
                index: i,
            })),
            {
                label: "$(globe) More results provided by search engine...",
                index: null,
            },
        ], {
            canPickMany: false,
        });
        if (typeof result === "undefined")
            throw new utils_1.UserCancelledError();
        if (result.index !== null)
            path = filtered[result.index].link;
        else
            path = null;
    }
    return path;
}
exports.getPath = getPath;
function getStoragePath(context) {
    return vscode_1.default.Uri.joinPath(context.globalStorageUri, "linkmap.json");
}
const textDecoder = new TextDecoder();
async function updateData(context) {
    const content = await (0, fetch_1.fetch)(`https://cdn.jsdelivr.net/npm/@gytx/cppreference-index/dist/generated.json`).then((r) => r.arrayBuffer());
    const storagePath = getStoragePath(context);
    await vscode_1.default.workspace.fs.writeFile(storagePath, new Uint8Array(content));
    data = JSON.parse(textDecoder.decode(content));
}
exports.updateData = updateData;
async function initData(context) {
    await vscode_1.default.workspace.fs.createDirectory(context.globalStorageUri);
    const storagePath = getStoragePath(context);
    if (!fs.existsSync(storagePath.fsPath)) {
        const bundled = vscode_1.default.Uri.file(path.join(__dirname, "./generated.json"));
        vscode_1.default.workspace.fs.copy(bundled, storagePath);
    }
    const content = await vscode_1.default.workspace.fs.readFile(storagePath);
    return JSON.parse(textDecoder.decode(content));
}
//# sourceMappingURL=data.js.map