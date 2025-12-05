"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Cache = void 0;
const enums_1 = require("./enums");
const settings_1 = require("./settings");
class CacheClass {
    static get Instance() {
        this._instance = this._instance ? this._instance : new CacheClass();
        return this._instance;
    }
    autoFold(langId) {
        return settings_1.ExtSettings.Get(enums_1.Settings.autoFold, langId);
    }
    togglePerFile(langId) {
        return settings_1.ExtSettings.Get(enums_1.Settings.togglePerFile, langId);
    }
    SetShouldFold(key, shouldToggle, langId) {
        if (this.togglePerFile(langId)) {
            this.CacheMap.set(key, shouldToggle);
        }
        else {
            this.CacheMap.set("global", shouldToggle);
        }
    }
    ShouldFold(key, langId) {
        var _a, _b;
        if (this.togglePerFile(langId)) {
            return (_a = this.CacheMap.get(key)) !== null && _a !== void 0 ? _a : this.autoFold(langId);
        }
        else {
            return (_b = this.CacheMap.get("global")) !== null && _b !== void 0 ? _b : this.autoFold(langId);
        }
    }
    ToggleShouldFold(key, langId) {
        this.SetShouldFold(key, !this.ShouldFold(key, langId), langId);
    }
    Clear() {
        this.CacheMap.clear();
    }
    constructor() {
        this.CacheMap = new Map();
    }
}
exports.Cache = CacheClass.Instance;
//# sourceMappingURL=cache.js.map