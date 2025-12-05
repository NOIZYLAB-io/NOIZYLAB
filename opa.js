"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getDataDir = getDataDir;
exports.canUseBundleFlags = canUseBundleFlags;
exports.canUseStrictFlag = canUseStrictFlag;
exports.getRoots = getRoots;
exports.getRootParams = getRootParams;
exports.getSchemaParams = getSchemaParams;
exports.refToString = refToString;
exports.parse = parse;
exports.run = run;
exports.opaIsInstalled = opaIsInstalled;
exports.runWithStatus = runWithStatus;
const cp = require("child_process");
const command_exists_1 = require("command-exists");
const fs_1 = require("fs");
const path_1 = require("path");
const vscode = require("vscode");
const github_installer_1 = require("./github-installer");
const advertise_1 = require("./ls/advertise");
const util_1 = require("./util");
const regoVarPattern = new RegExp("^[a-zA-Z_][a-zA-Z0-9_]*$");
// TODO: link to instructions that describe compiling OPA from source
const windowsArm64NotSupported = "OPA binaries are not supported for windows/arm architecture. To use the features of this plugin, compile OPA from source.";
function getDataDir(uri) {
    // NOTE(tsandall): we don't have a precise version for 3be55ed6 so
    // do our best and rely on the -dev tag.
    if (!installedOPASameOrNewerThan("0.14.0-dev")) {
        return uri.fsPath;
    }
    if (uri.scheme === "file") {
        return uri.toString();
    }
    return decodeURIComponent(uri.toString());
}
function canUseBundleFlags() {
    const bundleMode = vscode.workspace.getConfiguration("opa").get("bundleMode", true);
    return installedOPASameOrNewerThan("0.14.0-dev") && bundleMode;
}
function canUseStrictFlag() {
    const strictMode = vscode.workspace.getConfiguration("opa").get("strictMode", true);
    return strictMode && installedOPASameOrNewerThan("0.37.0");
}
function dataFlag() {
    if (canUseBundleFlags()) {
        return "--bundle";
    }
    return "--data";
}
// returns true if installed OPA is same or newer than OPA version x.
function installedOPASameOrNewerThan(x) {
    const s = getOPAVersionString(undefined);
    return opaVersionSameOrNewerThan(s, x);
}
function replacePathVariables(path) {
    let result = (0, util_1.replaceWorkspaceFolderPathVariable)(path);
    if (vscode.window.activeTextEditor !== undefined) {
        result = result.replace("${fileDirname}", (0, path_1.dirname)(vscode.window.activeTextEditor.document.fileName));
    }
    else if (path.indexOf("${fileDirname}") >= 0) {
        // Report on the original path
        vscode.window.showWarningMessage("${fileDirname} variable configured in settings, but no document is active");
    }
    return result;
}
// Returns a list of root data path URIs based on the plugin configuration.
function getRoots() {
    const roots = vscode.workspace.getConfiguration("opa").get("roots", []);
    return roots.map((root) => getDataDir(vscode.Uri.parse(replacePathVariables(root))));
}
// Returns a list of root data parameters in an array
// like ["--bundle=file:///a/b/x/", "--bundle=file:///a/b/y"] in bundle mode
// or ["--data=file:///a/b/x", "--data=file://a/b/y"] otherwise.
function getRootParams() {
    const flag = dataFlag();
    const roots = getRoots();
    return roots.map((root) => `${flag}=${root}`);
}
// Returns a list of schema parameters in an array.
// The returned array either contains a single entry; or is empty, if the 'opa.schema' setting isn't set.
function getSchemaParams() {
    let schemaPath = vscode.workspace.getConfiguration("opa").get("schema");
    if (schemaPath === undefined || schemaPath === null) {
        return [];
    }
    schemaPath = replacePathVariables(schemaPath);
    // At this stage, we don't care if the path is valid; let the OPA command return an error.
    return [`--schema=${schemaPath}`];
}
// returns true if OPA version a is same or newer than OPA version b. If either
// version is not in the expected format (i.e.,
// <major>.<minor>.<point>[-<patch>]) this function returns true. Major, minor,
// and point versions are compared numerically. Patch versions are compared
// lexicographically however an empty patch version is considered newer than a
// non-empty patch version.
function opaVersionSameOrNewerThan(a, b) {
    const aVersion = parseOPAVersion(a);
    const bVersion = parseOPAVersion(b);
    if (aVersion.length !== 4 || bVersion.length !== 4) {
        return true;
    }
    for (let i = 0; i < 3; i++) {
        if (aVersion[i] > bVersion[i]) {
            return true;
        }
        else if (bVersion[i] > aVersion[i]) {
            return false;
        }
    }
    if (aVersion[3] === "" && bVersion[3] !== "") {
        return true;
    }
    else if (aVersion[3] !== "" && bVersion[3] === "") {
        return false;
    }
    return aVersion[3] >= bVersion[3];
}
// returns array of numbers and strings representing an OPA semantic version.
function parseOPAVersion(s) {
    const parts = s.split(".", 3);
    if (parts.length < 3) {
        return [];
    }
    const major = Number(parts[0]);
    const minor = Number(parts[1]);
    const pointParts = parts[2].split("-", 2);
    const point = Number(pointParts[0]);
    let patch = "";
    if (pointParts.length >= 2) {
        patch = pointParts[1];
    }
    return [major, minor, point, patch];
}
// returns the installed OPA version as a string.
function getOPAVersionString(context) {
    const opaPath = getOpaPath(context, "opa", false);
    if (opaPath === undefined) {
        return "";
    }
    const result = cp.spawnSync(opaPath, ["version"]);
    if (result.status !== 0) {
        return "";
    }
    const lines = result.stdout.toString().split("\n");
    for (let i = 0; i < lines.length; i++) {
        const parts = lines[i].trim().split(": ", 2);
        if (parts.length < 2) {
            continue;
        }
        if (parts[0] === "Version") {
            return parts[1];
        }
    }
    return "";
}
// refToString formats a ref as a string. Strings are special-cased for
// dot-style lookup. Note: this function is currently only used for populating
// picklists based on dependencies. As such it doesn't handle all term types
// properly.
function refToString(ref) {
    let result = ref[0].value;
    for (let i = 1; i < ref.length; i++) {
        if (ref[i].type === "string") {
            if (regoVarPattern.test(ref[i].value)) {
                result += "." + ref[i].value;
                continue;
            }
        }
        result += "[" + JSON.stringify(ref[i].value) + "]";
    }
    return result;
}
/**
 * Helpers for executing OPA as a subprocess.
 */
function parse(context, opaPath, path, cb, onerror) {
    run(context, opaPath, ["parse", path, "--format", "json"], "", (_, result) => {
        const pkg = (0, util_1.getPackage)(result);
        const imports = (0, util_1.getImports)(result);
        cb(pkg, imports);
    }, onerror);
}
function run(context, path, args, stdin, onSuccess, onFailure) {
    runWithStatus(context, path, args, stdin, (code, stderr, stdout) => {
        if (code === 0) {
            onSuccess(stderr, JSON.parse(stdout));
        }
        else if (stdout !== "") {
            onFailure(stdout);
        }
        else {
            onFailure(stderr);
        }
    });
}
function opaIsInstalled(context) {
    return getOpaPath(context, "opa", false) !== undefined;
}
function getOpaPath(context, path, shouldPromptForInstall) {
    let opaPath = vscode.workspace.getConfiguration("opa.dependency_paths").get("opa");
    // if not set, check the deprecated setting location
    if (opaPath === undefined || opaPath === null) {
        opaPath = vscode.workspace.getConfiguration("opa").get("path");
    }
    if (opaPath !== undefined && opaPath !== null) {
        opaPath = (0, util_1.replaceWorkspaceFolderPathVariable)(opaPath);
    }
    if (opaPath !== undefined && opaPath !== null && opaPath.length > 0) {
        if (opaPath.startsWith("file://")) {
            opaPath = opaPath.substring(7);
        }
        if ((0, fs_1.existsSync)(opaPath)) {
            return opaPath;
        }
        console.warn("'opa.path' setting configured with invalid path:", opaPath);
    }
    if ((0, command_exists_1.sync)(path)) {
        return path;
    }
    if (shouldPromptForInstall) {
        // this is used to track if the user has been offered to install OPA,
        // this can later be used to allow other prompts to be shown
        if (context) {
            const globalStateKey = "opa.prompts.install.opa";
            context.globalState.update(globalStateKey, true);
        }
        (0, github_installer_1.promptForInstall)("opa", "open-policy-agent/opa", "OPA is either not installed or is missing from your path, would you like to install it?", (release) => {
            // release.assets.name contains {'darwin', 'linux', 'windows'} and {'arm64', 'amd64'}
            // in the format `opa_$OS_$ARCH...` so we can use that to search for the appropriate asset
            const assets = release.assets || [];
            const os = process.platform;
            // node can return many values for process.arch but OPA only supports arm64 and amd64
            const arch = process.arch.indexOf("arm") !== -1 ? "arm64" : "amd64";
            let targetAsset;
            switch (os) {
                case "darwin":
                    targetAsset = assets.filter((asset) => asset.name.indexOf(`darwin_${arch}`) !== -1)[0];
                    break;
                case "linux":
                    targetAsset = assets.filter((asset) => asset.name.indexOf(`linux_${arch}`) !== -1)[0];
                    break;
                case "win32":
                    // arm is not supported officially for windows, so prompt the user
                    // to build from source and provide an empty url from the default case
                    if (arch === "arm64") {
                        throw windowsArm64NotSupported;
                    }
                    else {
                        targetAsset = assets.filter((asset) => asset.name.indexOf(`windows`) !== -1)[0];
                        break;
                    }
                default:
                    targetAsset = { browser_download_url: "" };
            }
            return targetAsset.browser_download_url;
        }, () => {
            const os = process.platform;
            switch (os) {
                case "darwin":
                case "linux":
                    return "opa";
                case "win32":
                    return "opa.exe";
                default:
                    return "opa";
            }
        }, () => {
            context && (0, advertise_1.advertiseLanguageServers)(context);
        });
    }
}
function getOpaEnv() {
    const env = vscode.workspace.getConfiguration("opa").get("env", {});
    return Object.fromEntries(Object.entries(env).map(([k, v]) => [k, replacePathVariables(v)]));
}
// runWithStatus executes the OPA binary at path with args and stdin. The
// callback is invoked with the exit status, stderr, and stdout buffers.
function runWithStatus(context, path, args, stdin, cb) {
    const opaPath = getOpaPath(context, path, true);
    if (opaPath === undefined) {
        return;
    }
    console.log("spawn:", opaPath, "args:", args.toString());
    const proc = cp.spawn(opaPath, args, { env: { ...process.env, ...getOpaEnv() } });
    proc.stdin.write(stdin);
    proc.stdin.end();
    let stdout = "";
    let stderr = "";
    proc.stdout.on("data", (data) => {
        stdout += data;
    });
    proc.stderr.on("data", (data) => {
        stderr += data;
    });
    proc.on("exit", (code) => {
        console.log("code:", code);
        console.log("stdout:", stdout);
        console.log("stderr:", stderr);
        cb(code || 0, stderr, stdout);
    });
}
//# sourceMappingURL=opa.js.map