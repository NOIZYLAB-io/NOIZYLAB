"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getFileNameFromPath = exports.storeJsonData = exports.setJsonItem = exports.getJsonItem = void 0;
const Util_1 = require("../Util");
const DeviceManager_1 = require("./DeviceManager");
const LocalStorageManager_1 = require("./LocalStorageManager");
const fs = require("fs");
let storageMgr = undefined;
function getStorageManager() {
    if (!storageMgr) {
        storageMgr = LocalStorageManager_1.LocalStorageManager.getCachedStorageManager();
    }
    return storageMgr;
}
function getJsonItem(file, key, defaultValue = '') {
    var _a;
    return ((_a = getStorageManager()) === null || _a === void 0 ? void 0 : _a.getValue(`${getFileNameFromPath(file)}_${key}`)) || defaultValue;
}
exports.getJsonItem = getJsonItem;
function setJsonItem(file, key, value) {
    var _a;
    (_a = getStorageManager()) === null || _a === void 0 ? void 0 : _a.setValue(`${getFileNameFromPath(file)}_${key}`, value);
}
exports.setJsonItem = setJsonItem;
function storeJsonData(fileName, json) {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const content = JSON.stringify(json);
            fs.writeFileSync(fileName, content, 'utf8');
        }
        catch (e) {
            (0, Util_1.logIt)(`Unable to write ${fileName} info: ${e.message}`, true);
        }
    });
}
exports.storeJsonData = storeJsonData;
function getFileNameFromPath(filePath) {
    const parts = (0, DeviceManager_1.isWindows)() ? filePath.split('\\') : filePath.split('/');
    return parts[parts.length - 1].split('.')[0];
}
exports.getFileNameFromPath = getFileNameFromPath;
//# sourceMappingURL=FileManager.js.map