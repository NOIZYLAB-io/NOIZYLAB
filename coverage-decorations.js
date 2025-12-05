"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CoverageDecorations = exports.mapDecorationOptions = exports.UNCOVERED_LINE_MESSAGE = void 0;
const vscode_1 = require("vscode");
const extension_configuration_1 = require("./extension-configuration");
const utils_1 = require("./utils");
exports.UNCOVERED_LINE_MESSAGE = "This line is missing code coverage.";
/**
 * @param coverage The coverage information to map to decoration options
 * @returns The decoration options for the uncovered lines in the coverage information
 * @description This method maps the coverage information to decoration options for the uncovered lines.
 * exported for testing purposes
 */
function mapDecorationOptions(coverage) {
    var _a, _b;
    if (!((_a = coverage === null || coverage === void 0 ? void 0 : coverage.lines) === null || _a === void 0 ? void 0 : _a.details) || !((_b = coverage === null || coverage === void 0 ? void 0 : coverage.lines) === null || _b === void 0 ? void 0 : _b.found))
        return [];
    return (coverage.lines.details
        // Filter out lines that are covered
        .filter((line) => line.hit === 0)
        // Convert LineCoverageInfo to line numbers
        .map((line) => line.line - 1)
        // Sort the line numbers
        .sort((a, b) => a - b)
        // Convert line numbers to ranges
        .reduce((result, num) => {
        // Convert a list of numbers to a list of ranges
        // e.g. [1,2,3,5,6,7,9] => [[1,3],[5,7],[9,9]]
        const lastGroup = result[result.length - 1];
        if (!lastGroup) {
            result.push([num, num]);
        }
        else if (num === lastGroup[1] + 1) {
            lastGroup[1] = num;
        }
        else {
            result.push([num, num]);
        }
        return result;
    }, [])
        // Convert ranges to decoration options
        .map(([start, end]) => ({
        hoverMessage: new vscode_1.MarkdownString(exports.UNCOVERED_LINE_MESSAGE),
        range: new vscode_1.Range(start, 1, end, 1),
    })));
}
exports.mapDecorationOptions = mapDecorationOptions;
/**
 * @returns A new TextEditorDecorationType
 * @description Creates a new TextEditorDecorationType for uncovered lines
 * in the coverage information.
 */
function createDecorationType() {
    return vscode_1.window.createTextEditorDecorationType({
        isWholeLine: true,
        overviewRulerLane: vscode_1.OverviewRulerLane.Full,
        overviewRulerColor: { id: "markiscodecoverage.colorUncoveredLineRuler" },
        backgroundColor: { id: "markiscodecoverage.colorUncoveredLineText" },
    });
}
class CoverageDecorations extends vscode_1.Disposable {
    constructor(_config, _coverageByFile, _isDisposing = false, _decorationType = createDecorationType(), _fileCoverageDecorations = new Map(), _listeners = []) {
        super(() => {
            this._isDisposing = true;
            _fileCoverageDecorations.clear();
            _decorationType.dispose();
            for (const listener of _listeners)
                listener.dispose();
        });
        this._config = _config;
        this._coverageByFile = _coverageByFile;
        this._isDisposing = _isDisposing;
        this._decorationType = _decorationType;
        this._fileCoverageDecorations = _fileCoverageDecorations;
        const [debouncedFunc, debounceDispose] = (0, utils_1.debounce)(this.displayCoverageDecorations.bind(this), 100);
        this.displayCoverageDecorations = debouncedFunc;
        _listeners.push(this._config.onConfigOptionUpdated(this.onConfigOptionUpdated.bind(this)), debounceDispose);
    }
    /**
     * @param coverage The coverage information to display decorations for
     * @description Displays decorations for the uncovered lines in the coverage information.
     * This method is debounced to prevent flickering when the file is loading.
     * Debouncing is done by the constructor.
     */
    displayCoverageDecorations(coverage) {
        if (this._isDisposing || !this._config.showDecorations)
            return;
        const activeTextEditor = vscode_1.window.activeTextEditor;
        if (!activeTextEditor)
            return;
        const file = activeTextEditor.document.uri.fsPath;
        let decorations = this._fileCoverageDecorations.get(file);
        if (!coverage) {
            coverage = this._coverageByFile.get(file);
        }
        if (!decorations && coverage) {
            decorations = mapDecorationOptions(coverage);
            this._fileCoverageDecorations.set(file, decorations);
        }
        if (decorations) {
            activeTextEditor.setDecorations(this._decorationType, decorations);
        }
    }
    /**
     * @param file The file to add decorations for
     * @param coverage The coverage information to add decorations for
     * @returns The decoration options for the uncovered lines in the coverage information
     * @description Adds decorations for the specified file based on the coverage information.
     */
    addDecorationsForFile(file, coverage) {
        if (this._isDisposing || !this._config.showDecorations)
            return undefined;
        const decorations = mapDecorationOptions(coverage);
        this._fileCoverageDecorations.set(file, decorations);
        return decorations;
    }
    /**
     * @param file The file to remove decorations for
     * @description Removes the decorations for the specified file.
     */
    removeDecorationsForFile(file) {
        if (this._isDisposing)
            return undefined;
        this._fileCoverageDecorations.delete(file.fsPath);
    }
    /**
     * @description Clears all decorations from all files.
     */
    clearAllDecorations() {
        var _a;
        if (this._isDisposing)
            return undefined;
        this._fileCoverageDecorations.clear();
        (_a = vscode_1.window.activeTextEditor) === null || _a === void 0 ? void 0 : _a.setDecorations(this._decorationType, []);
        vscode_1.window.visibleTextEditors.forEach((editor) => {
            editor.setDecorations(this._decorationType, []);
        });
    }
    /**
     * @description Event is fired when the user changes the active text editor.
     */
    onFileChange() {
        this.displayCoverageDecorations();
    }
    /**
     * @description Handle configuration option updated event.
     * @param configOption The configuration option that was updated
     */
    onConfigOptionUpdated(configOption) {
        if (configOption === extension_configuration_1.CONFIG_OPTION_SHOW_DECORATIONS &&
            vscode_1.window.activeTextEditor) {
            const activeFile = vscode_1.window.activeTextEditor.document.uri.fsPath;
            const coverage = this._coverageByFile.get(activeFile);
            coverage && this._config.showDecorations
                ? this.displayCoverageDecorations(coverage)
                : this.clearAllDecorations();
        }
    }
}
exports.CoverageDecorations = CoverageDecorations;
//# sourceMappingURL=coverage-decorations.js.map