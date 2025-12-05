"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
const path = require("path");
class Importer {
    constructor(importer) {
        this.importer = importer;
        this.loadConfig();
    }
    loadConfig() {
        this.spacesBetweenBraces = this.importer.conf('spaceBetweenBraces', true);
        this.doubleQuotes = this.importer.conf('doubleQuotes', false);
        this.preferRelative = this.importer.conf('preferRelative', false);
    }
    importSymbol(document, symbol) {
        let module = this.resolveModule(document, symbol);
        var importRegExp = /\bimport\s+(?:({?)\s*(.+?)\s*}?\s+from\s+)?[\'"]([^"\']+)["\']\s*;?/g;
        let currentDoc = document.getText();
        var matches;
        var lastImport = null;
        let edit;
        while ((matches = importRegExp.exec(currentDoc))) {
            lastImport = document.positionAt(currentDoc.indexOf(matches[0]));
            var isDefault = matches[1] != "{";
            if (matches[3] == module && symbol.isDefault == isDefault) {
                let symbols = matches[2].split(/\s*,\s*/g);
                let symbolName = symbol.asDefinition ? symbol.asDefinition : symbol.name;
                if (symbols.indexOf(symbolName) < 0)
                    symbols.push(symbolName);
                if ((symbol.isDefault || isDefault) && symbols.length > 1)
                    continue;
                edit = new vscode.WorkspaceEdit();
                edit.replace(document.uri, new vscode.Range(lastImport.line, lastImport.character, lastImport.line, lastImport.character + matches[0].length), this.createImportStatement(this.createImportDefinition(symbols.join(', '), isDefault), module, false));
                break;
            }
        }
        if (!edit) {
            edit = new vscode.WorkspaceEdit();
            edit.insert(document.uri, new vscode.Position(lastImport ? lastImport.line + 1 : 0, 0), this.createImportStatement(this.createImportDefinition(symbol.asDefinition ? symbol.asDefinition : symbol.name, symbol.isDefault), module, true));
        }
        vscode.workspace.applyEdit(edit);
    }
    createImportDefinition(definitions, skipBrakets = false) {
        var definition = skipBrakets ? '' : '{';
        if (this.spacesBetweenBraces && skipBrakets == false)
            definition += ' ';
        definition += definitions;
        if (this.spacesBetweenBraces && skipBrakets == false)
            definition += ' ';
        definition += skipBrakets ? '' : '}';
        return definition;
    }
    createImportStatement(definition, module, endline = false) {
        let q = this.doubleQuotes ? '"' : "'";
        let NL = endline ? '\n' : '';
        let importStatement = 'import ' + definition + ' from ' + q + module + q + (this.importer.emitSemicolon ? ";" : "") + NL;
        return importStatement;
    }
    resolveModule(document, symbol) {
        if (symbol.module) {
            if (this.preferRelative) {
                let rel = this.resolveRelativeModule(document, symbol);
                if (rel.length <= symbol.module.length)
                    return rel;
            }
            return symbol.module;
        }
        else
            return this.resolveRelativeModule(document, symbol);
    }
    resolveRelativeModule(document, symbol) {
        var moduleParts = path.relative(path.dirname(document.fileName), symbol.path).split(/[\\/]/);
        if (moduleParts[0] !== '.' && moduleParts[0] !== '..')
            moduleParts.splice(0, 0, '.');
        var fileIdx = moduleParts.length - 1;
        moduleParts[fileIdx] = this.importer.removeFileExtension(moduleParts[fileIdx]);
        return moduleParts.join("/");
    }
}
exports.Importer = Importer;
//# sourceMappingURL=Importer.js.map