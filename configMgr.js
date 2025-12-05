"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
const nconf = require("nconf");
const path = require("path");
const util_1 = require("./util");
class ConfigMgr {
    constructor() {
        this.eventEmitter = new vscode.EventEmitter();
    }
    get(key) {
        const config = vscode.workspace.getConfiguration('favorites');
        const useSeparate = config.get('saveSeparated');
        if ((0, util_1.isMultiRoots)() || !useSeparate) {
            return config.get(key);
        }
        nconf.file({ file: path.resolve((0, util_1.getSingleRootPath)(), '.vscfavoriterc') });
        return nconf.get(key);
    }
    save(key, value) {
        const config = vscode.workspace.getConfiguration('favorites');
        const useSeparate = config.get('saveSeparated');
        if ((0, util_1.isMultiRoots)() || !useSeparate) {
            config.update(key, value, false);
            return Promise.resolve();
        }
        nconf.file({ file: path.resolve((0, util_1.getSingleRootPath)(), '.vscfavoriterc') });
        nconf.set(key, value);
        return new Promise((resolve, reject) => {
            nconf.save((err) => {
                if (err) {
                    return reject(err);
                }
                this.eventEmitter.fire();
                resolve();
            });
        });
    }
    get onConfigChange() {
        return this.eventEmitter.event;
    }
}
exports.default = new ConfigMgr();

//# sourceMappingURL=configMgr.js.map
