"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FileCoverageInfoProvider = void 0;
const vscode_1 = require("vscode");
const extension_configuration_1 = require("./extension-configuration");
const FILE_DECORATION_BADGE = "<%";
const FILE_DECORATION_TOOLTIP_PRELUDE = "Insufficent Code Coverage:";
/**
 * @param lines The coverage data for a file
 * @returns The coverage percentage
 * @description This method calculates the coverage percentage based on the number of lines hit and the number of lines found.
 */
function calculateCoveragePercent(coverage) {
    const { hit, found } = coverage.lines;
    const result = Math.floor((hit / found) * 100);
    if (isNaN(result) || !isFinite(result) || result < 0) {
        return 0;
    }
    else if (result > 100) {
        return 100;
    }
    return result;
}
/**
 * This class provides file decorations for the Explore View based on code coverage.
 * It listens for changes to the coverage threshold and regenerates the file decorations when it changes.
 */
class FileCoverageInfoProvider extends vscode_1.Disposable {
    constructor(_configuration, _coverageByFile, _showFileDecorations = _configuration.showDecorations, _coverageThreshold = _configuration.coverageThreshold, _isDisposing = false, _fileDecorationsEmitter = new vscode_1.EventEmitter(), onDidChangeFileDecorations = _fileDecorationsEmitter.event, _listeners = [_fileDecorationsEmitter]) {
        super(() => {
            this._isDisposing = true;
            for (const listener of _listeners)
                listener.dispose();
            delete this._fileDecorationsEmitter;
        });
        this._configuration = _configuration;
        this._coverageByFile = _coverageByFile;
        this._showFileDecorations = _showFileDecorations;
        this._coverageThreshold = _coverageThreshold;
        this._isDisposing = _isDisposing;
        this._fileDecorationsEmitter = _fileDecorationsEmitter;
        this.onDidChangeFileDecorations = onDidChangeFileDecorations;
        // Watch for updates to coverage threshold and regenerate when its updated
        _listeners.push(_configuration.onConfigOptionUpdated(this.handleConfigUpdate.bind(this)));
    }
    /**
     * @description This method shows the file decorations for the Explore View.
     */
    showCoverage() {
        this._showFileDecorations = true;
        this.updateFileDecorations();
    }
    /**
     * @description This method hides the file decorations for the Explore View.
     */
    hideCoverage() {
        this._showFileDecorations = false;
        this.updateFileDecorations();
    }
    /**
     * @param fsPaths The file(s) to decorate
     * @description This method is called by the extension to fire the onDidChangeFileDecorations event for the specified file(s).
     */
    updateFileDecorations() {
        if (this._isDisposing || !this._fileDecorationsEmitter)
            return;
        const uris = Array.from(this._coverageByFile.keys()).map((path) => vscode_1.Uri.file(path));
        this._fileDecorationsEmitter.fire(uris);
    }
    /**
     * @param uri The file to decorate
     * @param _token
     * @returns The decoration to apply to the file
     * @description This method is called by VSCode to decorate a file in the Explore View.
     */
    provideFileDecoration(uri, _token) {
        if (this._isDisposing || !this._showFileDecorations)
            return;
        const coverage = this._coverageByFile.get(uri.fsPath);
        if (coverage) {
            const percentCovered = calculateCoveragePercent(coverage);
            if (percentCovered < this._coverageThreshold) {
                return new vscode_1.FileDecoration(FILE_DECORATION_BADGE, `${FILE_DECORATION_TOOLTIP_PRELUDE} ${percentCovered}% vs. ${this._coverageThreshold}%.`, new vscode_1.ThemeColor("markiscodecoverage.insufficientCoverageForeground"));
            }
        }
    }
    /**
     * @param e The configuration option that was updated
     * @description This method is called when a configuration option is updated.
     * It checks if the coverage threshold was updated and updates the coverage threshold if it was.
     * It then regenerates the file decorations.
     */
    handleConfigUpdate(e) {
        if (this._isDisposing ||
            e !== extension_configuration_1.CONFIG_OPTION_COVERAGE_THRESHOLD ||
            this._coverageThreshold === this._configuration.coverageThreshold) {
            return;
        }
        this._coverageThreshold = this._configuration.coverageThreshold;
        this.updateFileDecorations();
    }
}
exports.FileCoverageInfoProvider = FileCoverageInfoProvider;
//# sourceMappingURL=file-coverage-info-provider.js.map