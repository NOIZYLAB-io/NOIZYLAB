"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Auth = void 0;
const axios_1 = __importStar(require("axios"));
const vscode = __importStar(require("vscode"));
const fs = __importStar(require("fs"));
const os_1 = __importDefault(require("os"));
const child_process_1 = require("child_process");
const agent_1 = require("../../@types/agent");
const cmd_1 = require("../../@types/cmd");
const auth_1 = require("../../@types/auth");
const logger_1 = require("../../util/logger");
const winreg_1 = __importDefault(require("winreg"));
class Auth {
    constructor(disposable, keploy) {
        this.dbusPath = "/var/lib/dbus/machine-id";
        // dbusPathEtc is the default path for dbus machine id located in /etc.
        // Some systems (like Fedora 20) only know this path.
        // Sometimes it's the other way round.
        this.dbusPathEtc = "/etc/machine-id";
        this.keploy = keploy;
        // register uri handler
        const uri_disposable = vscode.window.registerUriHandler({
            handleUri: (uri) => this.handleKeployUri(uri),
        });
        disposable.push(uri_disposable);
    }
    handleKeployUri(uri) {
        return __awaiter(this, void 0, void 0, function* () {
            var _a;
            logger_1.Logger.info('Handling URI', uri);
            // Extract the token from the URI query parameters
            const token = (_a = uri.query.split('token=')[1]) === null || _a === void 0 ? void 0 : _a.split('&')[0];
            if (!token) {
                logger_1.Logger.info('No token found in the URI');
                this.silentSignOut();
                return;
            }
            try {
                logger_1.Logger.info("Received token:", token);
                const response = yield this.validateLogin(token);
                if (!response) {
                    vscode.window.showErrorMessage('(Keploy) Token validation failed!');
                    this.silentSignOut();
                    return;
                }
                const authState = {
                    accessToken: undefined,
                    jwtToken: token,
                    signedIn: true,
                    authType: auth_1.AuthType.OTHERS,
                };
                // set the Auth state
                this.keploy.SetAuthState(authState);
                vscode.commands.executeCommand('setContext', cmd_1.KeployContextKeys.SIGNED_IN, true);
                vscode.commands.executeCommand('setContext', cmd_1.KeployContextKeys.SIGNED_OUT, false);
            }
            catch (error) {
                logger_1.Logger.error('Failed to validate token:', error, token);
                vscode.window.showErrorMessage(`(Keploy) Error during login ${error}`);
                this.silentSignOut();
                return;
            }
            this.keploy.SendAuthStateToView(auth_1.AUTH_STATUS.SIGNED_IN);
            vscode.window.showInformationMessage('(Keploy) You are now logged in!');
            // setup keploy because login was successful
            yield this.keploy.SetupKeploy();
        });
    }
    signInViaKeploy() {
        logger_1.Logger.info("Signing in via Keploy");
        const state = this.generateRandomState(); // Generate a secure random state
        const authUrl = `${agent_1.KEPLOY_APP_URI}/signin?vscode=true&state=${state}`;
        vscode.env.openExternal(vscode.Uri.parse(authUrl));
    }
    validateLogin(jwtToken) {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const installationID = yield this.getInstallationID();
                const requestBody = {
                    InstallationID: installationID,
                };
                const response = yield axios_1.default.post(`${agent_1.API_SERVER_URI}/user/connect`, requestBody, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${jwtToken}`, // JWT token in the header
                    },
                });
                if (response.status !== 200) {
                    throw new Error(`Failed to authenticate: ${response.data.Error}`);
                }
                return { response };
            }
            catch (err) {
                logger_1.Logger.error("Failed to authenticate:", err.message);
                throw new Error(`Failed to authenticate: ${err.message}`);
            }
        });
    }
    generateRandomState() {
        return [...Array(30)].map(() => Math.random().toString(36)[2]).join('');
    }
    signInViaGitHubVSCode() {
        return __awaiter(this, void 0, void 0, function* () {
            logger_1.Logger.info("Signing in via GitHub with VS Code");
            try {
                const result = yield this.getGitHubAccessToken();
                if (!result) {
                    logger_1.Logger.info('Failed to get the session or email.');
                    vscode.window.showInformationMessage('(Keploy) Failed to sign in Keploy!');
                    this.silentSignOut();
                    return;
                }
                const accessToken = result.accessToken;
                const resp = yield this.validateGHLogin(accessToken);
                logger_1.Logger.info("Response from validateGHLogin:", resp);
                if (!resp.isValid) {
                    vscode.window.showErrorMessage(`(Keploy) Failed to authenticate: ${resp.error}`);
                    this.silentSignOut();
                    return;
                }
                if (!resp.jwtToken) {
                    vscode.window.showErrorMessage('(Keploy) Failed to get JWT token from server.');
                    this.silentSignOut();
                    return;
                }
                const authState = {
                    accessToken: accessToken,
                    jwtToken: resp.jwtToken,
                    signedIn: true,
                    authType: auth_1.AuthType.VSCODE_GITHUB,
                };
                // set the Auth state
                this.keploy.SetAuthState(authState);
                vscode.commands.executeCommand('setContext', cmd_1.KeployContextKeys.SIGNED_IN, true);
                vscode.commands.executeCommand('setContext', cmd_1.KeployContextKeys.SIGNED_OUT, false);
            }
            catch (err) {
                logger_1.Logger.error("Failed to signIn github with vscode:", err.message);
                vscode.window.showErrorMessage(`(Keploy) Error during login ${err}`);
                this.silentSignOut();
                return;
            }
            this.keploy.SendAuthStateToView(auth_1.AUTH_STATUS.SIGNED_IN);
            vscode.window.showInformationMessage('(Keploy) You are now logged in!');
            // setup keploy because login was successful
            yield this.keploy.SetupKeploy();
        });
    }
    silentSignOut() {
        return __awaiter(this, void 0, void 0, function* () {
            logger_1.Logger.info("Signing out silently");
            const authState = {
                accessToken: undefined,
                jwtToken: undefined,
                signedIn: false,
                authType: undefined,
            };
            this.keploy.SetAuthState(authState);
            vscode.commands.executeCommand('setContext', cmd_1.KeployContextKeys.SIGNED_IN, false);
            vscode.commands.executeCommand('setContext', cmd_1.KeployContextKeys.SIGNED_OUT, true);
            this.keploy.SendAuthStateToView(auth_1.AUTH_STATUS.SIGNED_OUT);
        });
    }
    signOut() {
        return __awaiter(this, void 0, void 0, function* () {
            // set the Auth state to undefined
            const authState = {
                accessToken: undefined,
                jwtToken: undefined,
                signedIn: false,
                authType: undefined,
            };
            this.keploy.SetAuthState(authState);
            vscode.commands.executeCommand('setContext', cmd_1.KeployContextKeys.SIGNED_IN, false);
            vscode.commands.executeCommand('setContext', cmd_1.KeployContextKeys.SIGNED_OUT, true);
            vscode.window.showInformationMessage('(Keploy) You have been signed out.');
            this.keploy.SendAuthStateToView(auth_1.AUTH_STATUS.SIGNED_OUT);
            logger_1.Logger.info("User is logging out. Performing necessary actions...");
            // change the ui to welcome page
            // shut down the server
            this.keploy.ShutDown();
        });
    }
    validateGHLogin(token) {
        return __awaiter(this, void 0, void 0, function* () {
            const url = `${agent_1.API_SERVER_URI}/auth/github`;
            const installationID = yield this.getInstallationID();
            const requestBody = {
                gitHubToken: token,
                platform: "vscode",
                installationID: installationID,
            };
            logger_1.Logger.info("validate github login Request Body:", requestBody);
            try {
                const response = yield axios_1.default.post(url, requestBody, {
                    headers: { 'Content-Type': 'application/json' },
                });
                if (response.status !== axios_1.HttpStatusCode.Ok) {
                    throw new Error(`Failed to authenticate: ${response.data.error}`);
                }
                return {
                    emailID: response.data.emailID,
                    isValid: response.data.isValid,
                    jwtToken: response.data.jwtToken,
                    error: response.data.error,
                };
            }
            catch (err) {
                logger_1.Logger.error("Failed to authenticate:", err.message);
                throw new Error(`Failed to authenticate: ${err.message}`);
            }
        });
    }
    getGitHubAccessToken() {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const session = yield vscode.authentication.getSession('github', ['user:email', 'public_repo'], { createIfNone: true });
                if (session) {
                    const accessToken = session.accessToken;
                    logger_1.Logger.info('Access Token:', accessToken);
                    // Fetch the user's email
                    const email = yield this.fetchGitHubEmail(accessToken);
                    const owner = 'keploy';
                    const repo = 'keploy';
                    yield this.starGitHubRepo(accessToken, owner, repo);
                    return { accessToken, email };
                }
                else {
                    vscode.window.showErrorMessage('(Keploy) Failed to get GitHub session.');
                }
            }
            catch (error) {
                vscode.window.showErrorMessage(`(Keploy) Error: ${error}`);
            }
        });
    }
    fetchGitHubEmail(accessToken) {
        return __awaiter(this, void 0, void 0, function* () {
            var _a;
            try {
                const response = yield axios_1.default.get('https://api.github.com/user/emails', {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'Accept': 'application/vnd.github.v3+json',
                    }
                });
                const emails = response.data;
                const primaryEmail = emails.find((email) => email.primary && email.verified);
                return primaryEmail ? primaryEmail.email : null;
            }
            catch (error) {
                if (axios_1.default.isAxiosError(error)) {
                    vscode.window.showErrorMessage(`(Keploy) Failed to fetch email: ${((_a = error.response) === null || _a === void 0 ? void 0 : _a.status) || error.message}`);
                }
                else {
                    vscode.window.showErrorMessage(`(Keploy) Unexpected error: ${error}`);
                }
                return null;
            }
        });
    }
    starGitHubRepo(accessToken, owner, repo) {
        return __awaiter(this, void 0, void 0, function* () {
            logger_1.Logger.debug('⭐ Starring the repository:', owner, repo, accessToken);
            try {
                const response = yield axios_1.default.put(`https://api.github.com/user/starred/${owner}/${repo}`, null, {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'Accept': 'application/vnd.github+json',
                        'Content-Length': '0',
                    },
                });
                if (response.status === 204) {
                    logger_1.Logger.debug(`Successfully starred the repository`);
                }
                else {
                    logger_1.Logger.debug(`Failed to star repository. GitHub API responded with status ${response.status}`);
                }
            }
            catch (error) {
                logger_1.Logger.debug('Failed to star repository:', error);
            }
        });
    }
    // Reads the content of a file and returns it as a string.
    // If the file cannot be read, it throws an error.
    readFile(filePath) {
        try {
            return fs.readFileSync(filePath, 'utf-8').trim();
        }
        catch (err) {
            throw new Error(`Error reading file ${filePath}: ${err}`);
        }
    }
    machineID() {
        let id = "";
        try {
            id = this.readFile(this.dbusPath);
        }
        catch (err) {
            // Try the fallback path
            try {
                id = this.readFile(this.dbusPathEtc);
            }
            catch (err) {
                logger_1.Logger.error("Failed to read machine ID from both paths:", err);
                throw new Error("Failed to get machine ID");
            }
        }
        return id;
    }
    extractID(output) {
        const lines = output.split('\n');
        for (let line of lines) {
            if (line.includes('IOPlatformUUID')) {
                const parts = line.split('" = "');
                if (parts.length === 2) {
                    return parts[1].trim().replace('"', '');
                }
            }
        }
        throw new Error("Failed to extract 'IOPlatformUUID' value from `ioreg` output.");
    }
    getWindowsUUID() {
        return new Promise((resolve, reject) => {
            const regKey = new winreg_1.default({
                hive: winreg_1.default.HKLM,
                key: '\\SOFTWARE\\Microsoft\\Cryptography'
            });
            regKey.get('MachineGuid', (err, item) => {
                if (err) {
                    reject('Failed to retrieve Windows UUID from registry'); // Directly reject with a string message
                }
                else if (item && item.value) {
                    resolve(item.value); // Directly resolve with the string value from the registry
                }
                else {
                    reject('MachineGuid not found in registry'); // Handle case where value isn't found
                }
            });
        });
    }
    getInstallationID() {
        return __awaiter(this, void 0, void 0, function* () {
            let id;
            try {
                const platform = os_1.default.platform();
                switch (platform) {
                    case agent_1.OS.MAC:
                        // macOS specific command to get the IOPlatformUUID
                        const output = (0, child_process_1.execSync)('ioreg -rd1 -c IOPlatformExpertDevice').toString();
                        id = this.extractID(output);
                        break;
                    case agent_1.OS.LINUX:
                        // Use the new machineID function for Linux
                        id = this.machineID();
                        break;
                    case agent_1.OS.WINDOWS:
                        id = yield this.getWindowsUUID(); // Await the Promise from getWindowsUUID
                        break;
                    default:
                        throw new Error(`Unsupported platform: ${platform}`);
                }
                if (!id) {
                    logger_1.Logger.error("Got empty machine id");
                    throw new Error("Empty machine id");
                }
                logger_1.Logger.info("Installation ID:", id);
                return id;
            }
            catch (err) {
                logger_1.Logger.error("Failed to get installation ID:", err);
                throw new Error("Failed to get installation ID");
            }
        });
    }
}
exports.Auth = Auth;
//# sourceMappingURL=auth.js.map