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
Object.defineProperty(exports, "__esModule", { value: true });
exports.Keploy = void 0;
const vscode = __importStar(require("vscode"));
const abstract_1 = require("./abstract");
const global_1 = require("./platform/state/global");
const lens_1 = require("./providers/lens");
const view_1 = require("./providers/view");
const keploy_1 = require("./platform/agent/keploy");
const watcher_1 = require("./util/watcher");
const workspace_1 = require("./platform/state/workspace");
const auth_1 = require("./platform/auth/auth");
const cmd_1 = require("./cmd/cmd");
const cmd_2 = require("./@types/cmd");
const utg_1 = require("./service/utg/utg");
const util_1 = require("./util/util");
const auth_2 = require("./@types/auth");
const logger_1 = require("./util/logger");
class Keploy extends abstract_1.Abstract {
    constructor(context) {
        super();
        this.context = context;
        // initialize all the necessary components
        this.globalState = new global_1.GlobalState(this.context.globalState);
        this.workspaceState = new workspace_1.WorkspaceState(this.context.workspaceState);
        this.agent = new keploy_1.ServerManager(this);
        new lens_1.CodeLensProvider(this.context.subscriptions, this);
        new cmd_1.Commands(this.context.subscriptions, this);
        this.auth = new auth_1.Auth(this.context.subscriptions, this);
        this.watcher = new watcher_1.FileWatcher(this.context.subscriptions, this);
        // set workspace root
        this.workspaceRoot = vscode.workspace.workspaceFolders
            ? vscode.workspace.workspaceFolders[0].uri.fsPath
            : '';
        this.workspaceState.SetWorkspaceRoot(this.workspaceRoot);
        logger_1.Logger.info("Workspace Root:", this.workspaceRoot);
        this.utg = new utg_1.UTG(this, this.workspaceRoot);
        this.view = new view_1.ViewProvider(this.context, this, this.workspaceRoot);
    }
    Start() {
        return __awaiter(this, void 0, void 0, function* () {
            if (!this.workspaceRoot) {
                logger_1.Logger.info("Workspace root not found");
                vscode.window.showErrorMessage("(Keploy) Workspace root not found, please open a workspace");
                throw new Error("Workspace root not found");
            }
            // start the watcher
            this.watcher.startWatching();
            try {
                logger_1.Logger.info("Checking authentication...");
                yield this.checkAuthentication();
            }
            catch (error) {
                logger_1.Logger.error("Error while checking authentication:", error);
                vscode.window.showErrorMessage("(Keploy) Error while checking authentication: " + error.message);
            }
        });
    }
    Stop() {
        return __awaiter(this, void 0, void 0, function* () {
            this.utg.abortUtg();
            yield this.agent.closeSession(this.workspaceRoot);
            this.workspaceState.CleanUp(); // clean up workspace state
        });
    }
    checkAuthentication() {
        return __awaiter(this, void 0, void 0, function* () {
            // Get the auth state
            let authState = this.globalState.GetAuthState();
            if (!authState) {
                logger_1.Logger.info("Auth state not found");
                vscode.commands.executeCommand('setContext', cmd_2.KeployContextKeys.SIGNED_IN, false);
                vscode.commands.executeCommand('setContext', cmd_2.KeployContextKeys.SIGNED_OUT, true);
                logger_1.Logger.warn("Auth state not found. Please sign in to continue");
                return;
            }
            let isSignedIn = authState.signedIn || !!authState.jwtToken; // Check if signed in OR has JWT token
            if (authState.jwtToken && (0, util_1.isTokenExpired)(authState.jwtToken)) {
                logger_1.Logger.warn("JWT token expired. Hence signing out and attempting to sign in again...");
                // Sign out and clear the token
                this.SignOut();
                vscode.window.showWarningMessage("(Keploy) Your session has expired. Trying to sign in again...");
                // Reauthenticate based on AuthType
                if (authState.authType === auth_2.AuthType.VSCODE_GITHUB) {
                    yield this.SignInViaGitHubVSCode();
                }
                else {
                    this.SignInViaKeploy();
                }
                return;
            }
            if (isSignedIn) {
                vscode.commands.executeCommand('setContext', cmd_2.KeployContextKeys.SIGNED_IN, true);
                vscode.commands.executeCommand('setContext', cmd_2.KeployContextKeys.SIGNED_OUT, false);
                vscode.window.showInformationMessage('(Keploy) You are already signed in!');
                if (!authState.signedIn) {
                    logger_1.Logger.info('JWT token found; updating signed-in state');
                    this.globalState.SetAuthState(Object.assign(Object.assign({}, authState), { signedIn: true }));
                }
                // Setup and start the Keploy agent as the user is signed in
                this.agent.setupKeploy();
            }
            else {
                logger_1.Logger.warn("User is not signed in and no token found");
                vscode.commands.executeCommand('setContext', cmd_2.KeployContextKeys.SIGNED_IN, false);
                vscode.commands.executeCommand('setContext', cmd_2.KeployContextKeys.SIGNED_OUT, true);
                logger_1.Logger.warn("Please sign in to continue");
            }
        });
    }
    // Functions to clear the extension state (useful for testing and debugging)
    ClearKeployState() {
        return __awaiter(this, void 0, void 0, function* () {
            this.CleanUpState();
            this.SignOut();
            // restart the extension
            vscode.commands.executeCommand("workbench.action.reloadWindow");
        });
    }
    /** ================== Keploy Interface Methods ================== */
    /** ================== Agent Methods ================== */
    GetKeployInstallationProgress() {
        return this.globalState.GetKeployInstallationProgress();
    }
    ClearKeployInstallationProgress() {
        this.globalState.ClearKeployInstallationProgress();
    }
    KeployStatusMessenger(Server_Status) {
        /**Saving the  status here for further use. */
        this.globalState.SetCurrentServerStatus(Server_Status);
        return this.view.UpdateKeployServerStatus(Server_Status);
    }
    /** ================== Auth Methods ================== */
    SetAuthState(state) {
        this.globalState.SetAuthState(state);
    }
    SendAuthStateToView(authStatus) {
        this.view.SendAuthStateToView(authStatus);
    }
    /** ================== Command Methods ================== */ // common with some other methods as well.
    SignInViaGitHubVSCode() {
        return __awaiter(this, void 0, void 0, function* () {
            yield this.auth.signInViaGitHubVSCode();
        });
    }
    SignInViaKeploy() {
        this.auth.signInViaKeploy();
    }
    SignOut() {
        this.auth.signOut();
    }
    Utg(conf) {
        // it should open the sidebar if it was not opened.
        vscode.commands.executeCommand('workbench.view.extension.Keploy-Sidebar');
        const { filePath, functionName, singleUtgTest, additional_prompts } = conf;
        this.utg.runUtg(filePath, functionName, singleUtgTest, additional_prompts);
    }
    /** ================== Lens Methods ================== */
    GetAllFunctionsInFile(filePath, fileExtension) {
        return this.agent.getAllFunctionsInFile(filePath, fileExtension);
    }
    /** ================== UTGService Methods ================== */
    GetSubscriptionEnded() {
        return this.globalState.GetSubscriptionEnded();
    }
    SetSubscriptionEnded(status) {
        this.globalState.SetSubscriptionEnded(status);
    }
    GetFilePath() {
        return this.workspaceState.GetFilePath();
    }
    SetFilePath(filePath) {
        this.workspaceState.SetFilePath(filePath);
    }
    GetUTGExecutionStatus() {
        return this.workspaceState.GetUTGExecutionStatus();
    }
    SetUTGExecutionStatus(status) {
        this.workspaceState.SetUTGExecutionStatus(status);
    }
    GetAuthState() {
        return this.globalState.GetAuthState();
    }
    GetFolderState() {
        return this.workspaceState.GetFolderState();
    }
    SetFolderState(state) {
        this.workspaceState.SetFolderState(state);
    }
    GenerateUT(request, signal) {
        return this.agent.generateUT(request, signal);
    }
    SendTestGenInfoToView(data) {
        this.view.SendTestGenInfoToView(data);
    }
    SaveTestHistory(data) {
        this.view.SaveTestHistory(data);
    }
    SaveUTGConf(conf) {
        this.workspaceState.SaveUTGConf(conf);
    }
    /** ================== View Methods ================== */
    SetCurrentPage(page) {
        this.workspaceState.SetCurrentPage(page);
    }
    GetCurrentPage() {
        return this.workspaceState.GetCurrentPage();
    }
    GetProjectFolderStructure(workspaceRoot) {
        return this.agent.getProjectFolderStructure(workspaceRoot);
    }
    GetServerStatus() {
        return this.globalState.GetCurrentServerStatus();
    }
    GetUserStats() {
        return this.agent.getTestsData();
    }
    AbortUtg() {
        this.utg.abortUtg();
    }
    GetSessionCount(token) {
        return this.utg.getSessionCount(token);
    }
    GetTestGenInfo() {
        return this.utg.GetTestGenInfo();
    }
    GetUTGRunConf() {
        return this.workspaceState.GetUtgConf();
    }
    ToggleStep(toggleconf) {
        this.utg.ToggleTests(toggleconf);
    }
    /** ================== Watcher Methods ================== */
    GetExtensionVersion() {
        return this.globalState.GetExtensionVersion();
    }
    SetExtensionVersion(version) {
        this.globalState.SetExtensionVersion(version);
    }
    CleanUpState() {
        this.globalState.CleanUp();
        this.workspaceState.CleanUp();
    }
    /** ================== Commmon Methods ================== */
    SetupKeploy() {
        return __awaiter(this, void 0, void 0, function* () {
            yield this.agent.setupKeploy();
        });
    }
    ShutDown() {
        this.agent.shutdown();
    }
}
exports.Keploy = Keploy;
//# sourceMappingURL=keploy.js.map