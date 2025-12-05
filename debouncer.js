"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FileChangeDebouncer = void 0;
class FileChangeDebouncer {
    constructor(debounceTime, callback) {
        this.debounceTime = debounceTime;
        this.callback = callback;
        this.changedTestFiles = [];
        this.nonTestFilesChanged = false;
    }
    fileChanged(testFile) {
        if (testFile) {
            this.changedTestFiles.push(testFile);
        }
        else {
            this.nonTestFilesChanged = true;
        }
        if (this.timeout) {
            clearTimeout(this.timeout);
        }
        this.timeout = setTimeout(() => {
            this.callback(this.changedTestFiles.length > 0, this.nonTestFilesChanged ? undefined : this.changedTestFiles);
            this.changedTestFiles = [];
            this.nonTestFilesChanged = false;
        }, this.debounceTime);
    }
    reset() {
        if (this.timeout) {
            clearTimeout(this.timeout);
            this.timeout = undefined;
            this.changedTestFiles = [];
            this.nonTestFilesChanged = false;
        }
    }
    dispose() {
        if (this.timeout) {
            this.callback(this.changedTestFiles.length > 0, this.nonTestFilesChanged ? undefined : this.changedTestFiles);
            this.timeout = undefined;
            this.changedTestFiles = [];
            this.nonTestFilesChanged = false;
        }
    }
}
exports.FileChangeDebouncer = FileChangeDebouncer;
//# sourceMappingURL=debouncer.js.map