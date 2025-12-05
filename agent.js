"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ItemType = exports.ARCH = exports.OS = exports.PLAY = exports.Status = exports.KEPLOY_APP_URI = exports.API_SERVER_URI = exports.SERVER_LOG_FILE = exports.EXTENSION_ID = void 0;
exports.EXTENSION_ID = "keploy.keployio";
exports.SERVER_LOG_FILE = "keploy-server.log";
exports.API_SERVER_URI = "https://api.keploy.io";
exports.KEPLOY_APP_URI = "https://app.keploy.io";
var Status;
(function (Status) {
    Status["ACTIVE"] = "active";
    Status["INACTIVE"] = "inactive";
    Status["INSTALLING"] = "installing";
    Status["DOWNLOADING"] = "downloading";
    Status["COMPLETE"] = "complete";
    Status["ERROR"] = "error";
})(Status || (exports.Status = Status = {}));
var PLAY;
(function (PLAY) {
    PLAY["FILE"] = "file";
    PLAY["FUNCTION"] = "function";
    PLAY["ADDITIONAL_PROMPTS"] = "additionalprompts";
})(PLAY || (exports.PLAY = PLAY = {}));
var OS;
(function (OS) {
    OS["WINDOWS"] = "win32";
    OS["LINUX"] = "linux";
    OS["MAC"] = "darwin";
})(OS || (exports.OS = OS = {}));
var ARCH;
(function (ARCH) {
    ARCH["AMD64"] = "amd64";
    ARCH["ARM64"] = "arm64";
})(ARCH || (exports.ARCH = ARCH = {}));
var ItemType;
(function (ItemType) {
    ItemType["Folder"] = "folder";
    ItemType["File"] = "file";
    ItemType["Class"] = "class";
    ItemType["Function"] = "function";
    ItemType["Test"] = "test";
    ItemType["TestFunction"] = "testFunction";
})(ItemType || (exports.ItemType = ItemType = {}));
//# sourceMappingURL=agent.js.map