"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fs = require("fs");
const vscode = require("vscode");
const path = require("path");
const ImportIndex_1 = require("./ImportIndex");
const BATCH_SIZE = 50;
function toGlob(p) {
    return p.length == 1 ? p[0] : ("{" + p.join(",") + "}");
}
function toSA(value) {
    if (value === void 0)
        return [];
    else if (typeof value === 'string')
        return [value];
    else
        return value;
}
class ImportIndexer {
    constructor(importer) {
        this.importer = importer;
        this.reset();
    }
    reset() {
        this.index = new ImportIndex_1.ImportIndex();
        this.filesToScan = toSA(this.importer.conf('filesToScan'));
        this.filesToExclude = toSA(this.importer.conf('filesToExclude'));
        var tsconfig;
        try {
            tsconfig = JSON.parse(fs.readFileSync(vscode.workspace.rootPath + "/" + this.importer.conf('tsconfigName', 'tsconfig.json')).toString());
        }
        catch (e) {
            tsconfig = undefined;
        }
        if (tsconfig && tsconfig.compilerOptions) {
            this.paths = tsconfig.compilerOptions.paths ? tsconfig.compilerOptions.paths["*"] : undefined;
            if (this.paths) {
                for (let i = 0; i < this.paths.length; i++) {
                    let p = path.resolve(vscode.workspace.rootPath, this.paths[i]).split(/[\/\\]/);
                    p[p.length - 1] = "";
                    this.paths[i] = p.join("/");
                }
            }
            else
                this.paths = [];
        }
        else
            this.paths = [];
    }
    attachFileWatcher() {
        if (this.fileWatcher) {
            this.fileWatcher.dispose();
            this.fileWatcher = undefined;
        }
        let watcher = this.fileWatcher = vscode.workspace.createFileSystemWatcher(toGlob(this.filesToScan));
        var batch = [];
        var batchTimeout = undefined;
        var batchHandler = () => {
            batchTimeout = undefined;
            //this.processWorkspaceFiles( batch.splice( 0, batch.length ), false, true );
            vscode.workspace
                .findFiles(toGlob(this.filesToScan), toGlob(['**/node_modules/**'].concat(this.filesToExclude)), 99999)
                .then((files) => {
                var b = batch.splice(0, batch.length);
                if (b.length)
                    this.processWorkspaceFiles(files.filter(f => b.indexOf(f.fsPath) >= 0), false, true);
            });
        };
        var addBatch = (file) => {
            batch.push(file.fsPath);
            if (batchTimeout) {
                clearTimeout(batchTimeout);
                batchTimeout = undefined;
            }
            batchTimeout = setTimeout(batchHandler, 250);
        };
        watcher.onDidChange((file) => {
            addBatch(file);
        });
        watcher.onDidCreate((file) => {
            addBatch(file);
        });
        watcher.onDidDelete((file) => {
            this.fileDeleted(file);
        });
    }
    scanAll(showNotifications) {
        this.scanStarted = new Date();
        vscode.workspace
            .findFiles(toGlob(this.filesToScan), toGlob(['**/node_modules/**'].concat(this.filesToExclude)), 99999)
            .then((files) => this.processWorkspaceFiles(files, showNotifications, false));
    }
    fileDeleted(file) {
        this.index.deleteByPath(file.fsPath);
        this.printSummary();
    }
    printSummary() {
        this.importer.setStatusBar("Symbols: " + this.index.symbolCount);
    }
    processWorkspaceFiles(files, showNotifications, deleteByFile) {
        files = files.filter((f) => {
            return f.fsPath.indexOf('typings') === -1 &&
                f.fsPath.indexOf('node_modules') === -1 &&
                f.fsPath.indexOf('jspm_packages') === -1;
        });
        console.log("processWorkspaceFiles", files, showNotifications, deleteByFile);
        var fi = 0;
        var next = () => {
            for (var x = 0; x < BATCH_SIZE && fi < files.length; x++) {
                this.importer.setStatusBar("processing " + fi + "/" + files.length);
                var file = files[fi++];
                try {
                    var data = fs.readFileSync(file.fsPath, 'utf8');
                    this.processFile(data, file, deleteByFile);
                }
                catch (err) {
                    console.log("Failed to loadFile", err);
                }
            }
            if (fi == files.length) {
                this.scanEnded = new Date();
                this.printSummary();
                if (showNotifications)
                    this.importer.showNotificationMessage(`cache creation complete - (${Math.abs(this.scanStarted - this.scanEnded)}ms)`);
                return;
            }
            //loop async
            setTimeout(next, 0);
        };
        next();
    }
    processFile(data, file, deleteByFile) {
        if (deleteByFile)
            this.index.deleteByPath(file.fsPath);
        var fsPath = file.fsPath.replace(/[\/\\]/g, "/");
        fsPath = this.importer.removeFileExtension(fsPath);
        var path = file.fsPath;
        var module = undefined;
        for (var i = 0; i < this.paths.length; i++) {
            var p = this.paths[i];
            if (fsPath.substr(0, p.length) == p) {
                module = fsPath.substr(p.length);
                break;
            }
        }
        var typesRegEx = /(export\s+?(default\s+?)?(?:((?:(?:abstract\s+)?class)|(?:type)|(?:interface)|(?:function(?:\s*\*)?)|(?:let)|(?:var)|(?:const)|(?:enum))\s+)?)([a-zA-z]\w*)/g;
        var typeMatches;
        while ((typeMatches = typesRegEx.exec(data))) {
            let isDefault = typeMatches[2];
            let symbolType = typeMatches[3];
            let symbolName = typeMatches[4];
            this.index.addSymbol(symbolName, module, path, symbolType, !!isDefault, undefined);
        }
        var importRegEx = /\bimport\s+(?:({?)\s*(.+?)\s*}?\s+from\s+)?[\'"]([^"\']+)["\']/g;
        var imports;
        while (imports = importRegEx.exec(data)) {
            if (!imports[2])
                continue;
            let importModule = imports[3];
            if (importModule.indexOf('./') < 0 && importModule.indexOf('!') < 0) {
                let symbols = imports[2].split(/\s*,\s*/g);
                for (var s = 0; s < symbols.length; s++) {
                    let symbolName = symbols[s];
                    let asStmtMatch = /\*\s+as\s+(.*)/.exec(symbolName);
                    let asStmt = undefined;
                    if (asStmtMatch) {
                        asStmt = symbolName;
                        symbolName = asStmtMatch[1];
                    }
                    this.index.addSymbol(symbolName, importModule, undefined, undefined, imports[1] != "{", asStmt);
                }
            }
        }
    }
}
exports.ImportIndexer = ImportIndexer;
//# sourceMappingURL=ImportIndexer.js.map