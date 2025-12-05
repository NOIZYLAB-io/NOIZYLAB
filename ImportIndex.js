"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fs = require("fs");
var MatchMode;
(function (MatchMode) {
    MatchMode[MatchMode["EXACT"] = 0] = "EXACT";
    MatchMode[MatchMode["START"] = 1] = "START";
    MatchMode[MatchMode["END"] = 2] = "END";
    MatchMode[MatchMode["ANY"] = 3] = "ANY";
})(MatchMode = exports.MatchMode || (exports.MatchMode = {}));
function matches(value, test, ignoreCase, mode) {
    value = value || '';
    test = test || '';
    if (ignoreCase) {
        value = value.toLocaleLowerCase();
        test = test.toLocaleLowerCase();
    }
    var valid = false;
    valid = valid || (mode == MatchMode.EXACT && value == test);
    valid = valid || (mode == MatchMode.START && value.startsWith(test));
    valid = valid || (mode == MatchMode.ANY && value.indexOf(test) >= 0);
    valid = valid || (mode == MatchMode.END && value.endsWith(test));
    return valid;
}
function exists(path) {
    try {
        return !!fs.statSync(path);
    }
    catch (e) {
        return false;
    }
}
class ImportIndex {
    constructor() {
        this.resetIndex();
    }
    resetIndex() {
        this.knownSymbols = {};
    }
    get symbolCount() {
        var c = 0;
        for (var k in this.knownSymbols)
            c += this.knownSymbols[k].length;
        return c;
    }
    getSymbols(name, ignoreCase = false, mode = MatchMode.EXACT) {
        if (mode == MatchMode.EXACT && !ignoreCase) {
            return this.knownSymbols[name] || [];
        }
        var result = [];
        for (var k in this.knownSymbols) {
            if (matches(k, name, ignoreCase, mode))
                result.push.apply(result, this.knownSymbols[k]);
        }
        return result;
    }
    getModules(name, ignoreCase = false, mode = MatchMode.EXACT) {
        var modules = [];
        for (var k in this.knownSymbols) {
            var imports = this.knownSymbols[k];
            for (var i = 0; i < imports.length; i++) {
                var imp = imports[i];
                if (matches(imp.module, name, ignoreCase, mode) && modules.indexOf(imp.module) < 0)
                    modules.push(imp.module);
            }
        }
        modules.sort();
        return modules;
    }
    deleteByPath(fsPath) {
        var toDelete = [];
        for (var name in this.knownSymbols) {
            let symbols = this.knownSymbols[name];
            for (let i = 0; i < symbols.length; i++)
                if (symbols[i].path == fsPath)
                    toDelete.push(symbols[i]);
        }
        for (let i = 0; i < toDelete.length; i++)
            this.delete(toDelete[i]);
    }
    delete(obj) {
        var current = this.getSymbols(obj.name, false, MatchMode.EXACT);
        var updated = [];
        for (var i = 0; i < current.length; i++) {
            var c = current[i];
            if (obj.module == c.module)
                continue;
            if (!c.path || exists(c.path))
                updated.push(c);
        }
        if (updated.length)
            this.knownSymbols[obj.name] = updated;
        else
            delete this.knownSymbols[obj.name];
    }
    addSymbol(name, module, path, type, isDefault, asDefinition) {
        name = name.trim();
        if (name.length == 0)
            return null;
        let obj = {
            name,
            module,
            path,
            type,
            isDefault,
            asDefinition
        };
        var updated = [obj];
        var current = this.getSymbols(obj.name, false, MatchMode.EXACT);
        var updated = [obj];
        for (var i = 0; i < current.length; i++) {
            var c = current[i];
            if (obj.module == c.module) {
                obj.path = obj.path || c.path;
                obj.type = obj.type || c.type;
                obj.isDefault = obj.isDefault || c.isDefault;
                obj.asDefinition = obj.asDefinition || c.asDefinition;
                continue;
            }
            if (!c.path || exists(c.path))
                updated.push(c);
        }
        this.knownSymbols[obj.name] = updated;
    }
}
exports.ImportIndex = ImportIndex;
//# sourceMappingURL=ImportIndex.js.map