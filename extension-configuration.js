"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ExtensionConfiguration = exports.DEFAULT_CODE_COVERAGE_THRESHOLD = exports.DEFAULT_SEARCH_CRITERIA = exports.CONFIG_OPTION_SHOW_DECORATIONS = exports.CONFIG_OPTION_COVERAGE_THRESHOLD = exports.CONFIG_OPTION_SEARCH_CRITERIA = exports.CONFIG_OPTION_ENABLE_ON_STARTUP = exports.CONFIG_SECTION_NAME = void 0;
const vscode_1 = require("vscode");
exports.CONFIG_SECTION_NAME = "markiscodecoverage";
exports.CONFIG_OPTION_ENABLE_ON_STARTUP = "enableOnStartup";
exports.CONFIG_OPTION_SEARCH_CRITERIA = "searchCriteria";
exports.CONFIG_OPTION_COVERAGE_THRESHOLD = "coverageThreshold";
exports.CONFIG_OPTION_SHOW_DECORATIONS = "enableDecorations";
exports.DEFAULT_SEARCH_CRITERIA = "coverage/lcov*.info";
exports.DEFAULT_CODE_COVERAGE_THRESHOLD = 80;
class ExtensionConfiguration extends vscode_1.Disposable {
    constructor(config) {
        var _a, _b;
        // use dummy function for callOnDispose since dispose() will be overrided
        super(() => true);
        this._onConfigOptionUpdated = new vscode_1.EventEmitter();
        this._isDisposed = false;
        this._showCoverage = true;
        this._searchCriteria = "";
        this._coverageThreshold = 0;
        this._showDecorations = false;
        this.showCoverage =
            !config.has(exports.CONFIG_OPTION_ENABLE_ON_STARTUP) ||
                ((_a = config.get(exports.CONFIG_OPTION_ENABLE_ON_STARTUP)) !== null && _a !== void 0 ? _a : true);
        const configSearchCriteria = config.has(exports.CONFIG_OPTION_SEARCH_CRITERIA) &&
            config.get(exports.CONFIG_OPTION_SEARCH_CRITERIA);
        this.searchCriteria =
            configSearchCriteria && typeof configSearchCriteria === "string"
                ? configSearchCriteria
                : exports.DEFAULT_SEARCH_CRITERIA;
        this.coverageThreshold =
            (_b = config.get(exports.CONFIG_OPTION_COVERAGE_THRESHOLD)) !== null && _b !== void 0 ? _b : exports.DEFAULT_CODE_COVERAGE_THRESHOLD;
        this.showDecorations = config.get(exports.CONFIG_OPTION_SHOW_DECORATIONS, false);
    }
    dispose() {
        if (!this._isDisposed) {
            this._onConfigOptionUpdated.dispose();
            this._isDisposed = true;
        }
    }
    onConfigOptionUpdated(listener) {
        this._checkDisposed();
        return this._onConfigOptionUpdated.event(listener);
    }
    get showCoverage() {
        this._checkDisposed();
        return this._showCoverage;
    }
    set showCoverage(value) {
        this._checkDisposed();
        this._showCoverage = value;
    }
    get showDecorations() {
        this._checkDisposed();
        return this._showDecorations;
    }
    set showDecorations(value) {
        this._checkDisposed();
        this._showDecorations = value;
    }
    get searchCriteria() {
        this._checkDisposed();
        return this._searchCriteria;
    }
    set searchCriteria(value) {
        this._checkDisposed();
        this._searchCriteria = value;
    }
    get coverageThreshold() {
        this._checkDisposed();
        return this._coverageThreshold;
    }
    set coverageThreshold(value) {
        this._checkDisposed();
        this._coverageThreshold = value;
    }
    dispatchConfigUpdate(evtSrc, latestSnapshot) {
        var _a;
        this._checkDisposed();
        if (this._hasBeenUpdated(evtSrc, exports.CONFIG_OPTION_SEARCH_CRITERIA)) {
            const configSearchCriteria = latestSnapshot.has(exports.CONFIG_OPTION_SEARCH_CRITERIA) &&
                latestSnapshot.get(exports.CONFIG_OPTION_SEARCH_CRITERIA);
            this.searchCriteria =
                configSearchCriteria && typeof configSearchCriteria === "string"
                    ? configSearchCriteria
                    : this.searchCriteria;
            this._onConfigOptionUpdated.fire(exports.CONFIG_OPTION_SEARCH_CRITERIA);
        }
        else if (this._hasBeenUpdated(evtSrc, exports.CONFIG_OPTION_COVERAGE_THRESHOLD)) {
            this.coverageThreshold =
                (_a = latestSnapshot.get(exports.CONFIG_OPTION_COVERAGE_THRESHOLD)) !== null && _a !== void 0 ? _a : this.coverageThreshold;
            this._onConfigOptionUpdated.fire(exports.CONFIG_OPTION_COVERAGE_THRESHOLD);
        }
        else if (this._hasBeenUpdated(evtSrc, exports.CONFIG_OPTION_SHOW_DECORATIONS)) {
            this.showDecorations = latestSnapshot.get(exports.CONFIG_OPTION_SHOW_DECORATIONS, this.showDecorations);
            this._onConfigOptionUpdated.fire(exports.CONFIG_OPTION_SHOW_DECORATIONS);
        }
    }
    _hasBeenUpdated(evtSrc, optionName) {
        return evtSrc.affectsConfiguration(`${exports.CONFIG_SECTION_NAME}.${optionName}`);
    }
    _checkDisposed() {
        if (this._isDisposed) {
            throw new Error("illegal state - object is disposed");
        }
    }
}
exports.ExtensionConfiguration = ExtensionConfiguration;
//# sourceMappingURL=extension-configuration.js.map