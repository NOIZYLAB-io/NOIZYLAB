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
exports.ViewProvider = void 0;
const vscode = __importStar(require("vscode"));
const view_1 = require("../@types/view");
const uuid_1 = require("uuid");
const auth_1 = require("../@types/auth");
const util_1 = require("../util/util");
const progressTracker_1 = require("../util/progressTracker");
const logger_1 = require("../util/logger");
const utg_1 = require("../@types/utg");
const db_1 = require("../platform/json/testHistory/db");
const agent_1 = require("../@types/agent");
const path_1 = __importDefault(require("path"));
class ViewProvider {
    constructor(context, viewApi, WorkspaceRoot) {
        this._extensionUri = context.extensionUri;
        const viewDisposable = vscode.window.registerWebviewViewProvider(view_1.VIEW_ID, this);
        context.subscriptions.push(viewDisposable);
        /**
         * Initialiazing all of the viewApi's
         */
        this._viewApi = viewApi;
        /**
         * Initializaing the workspace root
         */
        this.WorkSpaceRoot = WorkspaceRoot;
        /**
         * Initializing the test history storage
         */
        this._historyStorage = new db_1.TestHistoryStorage(context);
        this._historyStorage.initializeStorage().then(() => {
            logger_1.Logger.info("Test history storage initialized successfully");
        }).catch((error) => {
            logger_1.Logger.error("Failed to initialize test history storage:", error);
        });
        this.historyOpt = {
            showHistory: false,
            runId: "",
        };
        this._viewApi.SetCurrentPage(view_1.Page.HOME);
        logger_1.Logger.info(`View Provider initialized with ${view_1.Page.HOME} Page`);
    }
    _setupProgressMonitoring() {
        var _a;
        logger_1.Logger.info("Setting up progress monitoring");
        // Dispose of any existing subscription
        (_a = this._progressSubscription) === null || _a === void 0 ? void 0 : _a.dispose();
        // Subscribe to progress updates
        this._progressSubscription = progressTracker_1.progressEmitter.event(progress => {
            if (this._view) {
                logger_1.Logger.info("Progress update:", progress);
                this.updateDataInSvelte({
                    command: view_1.MessageType.INSTALL_PROGRESS,
                    createdAt: Date.now(),
                    value: {
                        progress
                    }
                });
            }
        });
    }
    updateDataInSvelte(message) {
        if (!this._view) {
            return;
        }
        // We must still pass `any` to postMessage because that's how
        // VS Code defines `postMessage(message: any)`.
        logger_1.Logger.info("Sending message to svelte:", message);
        this._view.webview.postMessage(message);
    }
    RenderPageWithData(page, initialData) {
        return __awaiter(this, void 0, void 0, function* () {
            logger_1.Logger.info(`Rendering ${page} page`);
            const isRendered = yield this.renderPage(page);
            if (!isRendered) {
                return false;
            }
            ; // Only send data if the page successfully rendered
            if (initialData) {
                this.updateDataInSvelte(initialData);
            }
            logger_1.Logger.info(`${page} page rendered with initial data:`, initialData);
            return true;
        });
    }
    renderPage(page) {
        return __awaiter(this, void 0, void 0, function* () {
            if (!this._view) {
                logger_1.Logger.error("Webview not available");
                return false;
            }
            let webviewView = this._view;
            let sveltePageJs = null;
            let sveltePageCss = null;
            try {
                switch (page) {
                    case view_1.Page.HOME:
                        sveltePageJs = webviewView.webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "out", "compiled", "Home.js"));
                        sveltePageCss = webviewView.webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "out", "compiled", "Home.css"));
                        break;
                    case view_1.Page.STEPS:
                        sveltePageJs = webviewView.webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "out", "compiled", "StepsForUtg.js"));
                        sveltePageCss = webviewView.webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "out", "compiled", "StepsForUtg.css"));
                        break;
                    case view_1.Page.TEST_HISTORY:
                        sveltePageJs = webviewView.webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "out", "compiled", "TestHistory.js"));
                        sveltePageCss = webviewView.webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "out", "compiled", "TestHistory.css"));
                        break;
                    case view_1.Page.FOLDER_TREE:
                        sveltePageJs = webviewView.webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "out", "compiled", "TreeView.js"));
                        sveltePageCss = webviewView.webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "out", "compiled", "TreeView.css"));
                        break;
                }
                if (!sveltePageJs || !sveltePageCss) {
                    throw new Error("Page resources not properly assigned.");
                }
                webviewView.webview.html = this._getHtmlForWebview(webviewView.webview, sveltePageCss, sveltePageJs);
            }
            catch (error) {
                vscode.window.showErrorMessage(`(Keploy) Failed to open ${page} page ${error}`);
                return false;
            }
            // set the current page in the workspace context
            this._viewApi.SetCurrentPage(page);
            return true;
        });
    }
    // This method is called when the webview is first loaded, this is called just after the activate method execution is completed
    resolveWebviewView(webviewView, _context, _token) {
        logger_1.Logger.info("Resolving webview view");
        this._view = webviewView;
        webviewView.webview.options = {
            // Allow scripts in the webview
            enableScripts: true,
            localResourceRoots: [
                this._extensionUri,
                vscode.Uri.joinPath(this._extensionUri, "out", "compiled"),
                vscode.Uri.joinPath(this._extensionUri, "media"),
                vscode.Uri.joinPath(this._extensionUri, "sidebar"),
            ],
        };
        // setup keploy server progress monitoring
        this._setupProgressMonitoring();
        // Render the first home page
        this.renderPage(view_1.Page.HOME);
        // activate the listeners
        this.activateChangeVisibilityListener();
        this.activateReceiveMessageListener();
    }
    activateChangeVisibilityListener() {
        if (!this._view) {
            logger_1.Logger.error("Webview not available");
            return;
        }
        // it is called when the visibility of the webview changes
        this._view.onDidChangeVisibility(() => __awaiter(this, void 0, void 0, function* () {
            if (!this._view) {
                logger_1.Logger.error("Webview not available");
                return;
            }
            logger_1.Logger.info("Webview visibility changed");
            if (!this._view.visible) {
                logger_1.Logger.info("Webview is not visible");
                return;
            }
            logger_1.Logger.info("Webview is visible");
            // get the current page
            const currentPage = this._viewApi.GetCurrentPage();
            const authState = this._viewApi.GetAuthState();
            // Check if authentication is required for this page
            const isStepsWithHistory = currentPage === view_1.Page.STEPS && this.historyOpt.showHistory;
            const isAuthRequired = currentPage !== view_1.Page.TEST_HISTORY || isStepsWithHistory;
            if (!authState.signedIn && isAuthRequired) {
                this.SendAuthStateToView(auth_1.AUTH_STATUS.SIGNED_OUT);
                return;
            }
            if (isAuthRequired && (0, util_1.isTokenExpired)(authState.jwtToken)) {
                this.SendAuthStateToView(auth_1.AUTH_STATUS.SIGNED_OUT);
                this._viewApi.SignOut();
                vscode.window.showWarningMessage("(Keploy) Your session has expired. Please sign in again.");
                return;
            }
            switch (currentPage) {
                case view_1.Page.HOME:
                    this.renderPage(view_1.Page.HOME);
                    break;
                case view_1.Page.STEPS:
                    const showOpts = this.getHistoryOpts();
                    if (!showOpts.showHistory) { //show the live steps
                        const utginfo = this._viewApi.GetTestGenInfo();
                        logger_1.Logger.info("fetched test gen info after visibility changes:", utginfo);
                        this.RenderPageWithData(view_1.Page.STEPS, { command: view_1.MessageType.STEPSPAGE_PROPS, createdAt: Date.now(), value: { testgenInfo: utginfo, isHistory: false } });
                        break;
                    }
                    const runId = showOpts.runId;
                    try {
                        const result = yield this._historyStorage.getHistory();
                        const testDetails = result.find(t => t.id === runId);
                        if (!testDetails) {
                            logger_1.Logger.error(`Test run with ID ${runId} not found`);
                            vscode.window.showErrorMessage("(Keploy) Test run not found");
                            break;
                        }
                        // show the history
                        this.RenderPageWithData(view_1.Page.STEPS, { command: view_1.MessageType.STEPSPAGE_PROPS, createdAt: Date.now(), value: { testgenInfo: testDetails.testGenInfo, isHistory: true } });
                    }
                    catch (error) {
                        logger_1.Logger.error(`Error while fetching test run for id: ${runId}:`, error);
                        vscode.window.showErrorMessage("(Keploy) Failed to fetch test history");
                    }
                    break;
                case view_1.Page.TEST_HISTORY:
                    logger_1.Logger.info("showing test history after visibility changes");
                    this.renderPage(view_1.Page.TEST_HISTORY);
                    break;
                case view_1.Page.FOLDER_TREE:
                    logger_1.Logger.info("showing folder tree after visibility changes");
                    this.renderPage(view_1.Page.FOLDER_TREE);
                    break;
            }
        }));
    }
    activateReceiveMessageListener() {
        if (!this._view) {
            logger_1.Logger.error("Webview not available");
            return;
        }
        this._view.webview.onDidReceiveMessage((data) => __awaiter(this, void 0, void 0, function* () {
            const { command: type, createdAt: _time } = data;
            let page = this._viewApi.GetCurrentPage();
            switch (type) {
                case view_1.MessageType.READY:
                    logger_1.Logger.info("Webview is ready for page :", page);
                    page = data.value.page;
                    // send the initial data for the page
                    const initialData = yield this.getInitialDataForPage(page);
                    if (initialData) {
                        this.updateDataInSvelte(initialData);
                    }
                    else {
                        logger_1.Logger.error("Failed to get initial data for page:", page);
                    }
                    break;
                case view_1.MessageType.NAVIGATE:
                    page = data.value.page;
                    this.renderPage(page);
                    break;
                case view_1.MessageType.SIGN_IN:
                    try {
                        this._viewApi.SignInViaKeploy();
                    }
                    catch (error) {
                        logger_1.Logger.error('Error while signing in:', error);
                        vscode.window.showErrorMessage('(Keploy) Failed to sign in. Please try again.');
                    }
                    break;
                case view_1.MessageType.STOP_UTG:
                    try {
                        logger_1.Logger.info("user has stopped utg");
                        this._viewApi.AbortUtg();
                    }
                    catch (error) {
                        logger_1.Logger.error("Error while stopping UTG", error);
                    }
                    break;
                case view_1.MessageType.RETRY_UTG:
                    try {
                        const conf = this._viewApi.GetUTGRunConf();
                        logger_1.Logger.info("user has retried utg with conf: ", conf);
                        /**Retrying with saved UTG Conf */
                        this._viewApi.Utg(conf);
                    }
                    catch (error) {
                        logger_1.Logger.error("Error while retrying UTG", error);
                    }
                    break;
                case view_1.MessageType.TOGGLE_STEP:
                    try {
                        const toggleconf = data.value;
                        this._viewApi.ToggleStep(toggleconf);
                    }
                    catch (error) {
                        logger_1.Logger.error("Error while toggling step", error);
                    }
                    break;
                // Svelte is requesting test history, which eventually involves reading from the filesystem.
                // Since it's an I/O-bound operation, it can be time-consuming and should be treated accordingly.
                case view_1.MessageType.FETCH_TEST_HISTORY:
                    try {
                        // set history opts to false because post this flow user will select a particular history to view, so need to reset the older one
                        this.setHistoryOpts(false, "");
                        const testHistory = yield this._historyStorage.getTestRunMetadata();
                        this.updateDataInSvelte({ command: view_1.MessageType.TEST_HISTORY_PROPS, createdAt: Date.now(), value: { testHistory } });
                    }
                    catch (error) {
                        logger_1.Logger.error("Error while fetching test history", error);
                        vscode.window.showErrorMessage("(Keploy) Failed to fetch test history");
                        this.updateDataInSvelte({ command: view_1.MessageType.ERROR, createdAt: Date.now(), value: "Failed to fetch test history" });
                    }
                    break;
                case view_1.MessageType.FETCH_TESTRUN:
                    try {
                        const runId = data.value.runId;
                        // set history opts to show the test history even if the visibility changes
                        this.setHistoryOpts(true, runId);
                        const result = yield this._historyStorage.getHistory();
                        const testDetails = result.find(t => t.id === runId);
                        if (!testDetails) {
                            logger_1.Logger.error(`Test run with ID ${runId} not found`);
                            vscode.window.showErrorMessage("(Keploy) Test run not found");
                            return;
                        }
                        // show the history
                        this.RenderPageWithData(view_1.Page.STEPS, { command: view_1.MessageType.STEPSPAGE_PROPS, createdAt: Date.now(), value: { testgenInfo: testDetails.testGenInfo, isHistory: true } });
                    }
                    catch (error) {
                        logger_1.Logger.error(`Error while fetching test run for id: ${data.value.runId}:`, error);
                        vscode.window.showErrorMessage("(Keploy) Failed to fetch test history");
                    }
                    break;
                case view_1.MessageType.OPEN_FILE:
                    try {
                        const filePath = data.value.filePath;
                        yield (0, util_1.openFile)(filePath);
                        logger_1.Logger.info("Opened file: ", filePath);
                    }
                    catch (error) {
                        logger_1.Logger.error(`Failed to open the file.`, error);
                    }
                    break;
                case view_1.MessageType.FIND_FUNCTION:
                    try {
                        const { filePath, functionName } = data.value;
                        yield (0, util_1.findFunction)(filePath, functionName);
                        logger_1.Logger.info(`Located the function ${functionName} in the file:`, filePath);
                    }
                    catch (error) {
                        logger_1.Logger.error(`Failed to locate the function in the file:`, error);
                    }
                    break;
                case view_1.MessageType.FIND_TEST_FILE:
                    try {
                        const { functionName, testFilePath } = data.value;
                        yield (0, util_1.findTestFile)(functionName, testFilePath);
                        logger_1.Logger.info(`Located the function ${functionName} in the testfile:`, testFilePath);
                    }
                    catch (error) {
                        logger_1.Logger.info("Failed to open the testfile", error);
                    }
                    break;
                case view_1.MessageType.RUN_UTG:
                    try {
                        const utgmessage = data.value;
                        this.runUTGByFileType(utgmessage);
                    }
                    catch (error) {
                        logger_1.Logger.info("Failed to run the utg from the treeview", error);
                    }
                    break;
                case view_1.MessageType.LOAD_FUNCTIONS:
                    try {
                        let filepath = data.value.filePath;
                        let fileExtension = path_1.default.extname(filepath);
                        if (!filepath || !fileExtension) {
                            logger_1.Logger.error("Filepath or extension name is not present");
                            return;
                        }
                        yield this.sendFunctions(filepath, fileExtension);
                    }
                    catch (error) {
                        logger_1.Logger.info("Failed to load functon for file with error: ", error);
                    }
                    break;
                case view_1.MessageType.SET_FOLDER_STATE:
                    try {
                        const currentfolderstate = this._viewApi.GetFolderState();
                        const newFolderStateObj = data.value.folderstate;
                        const mergedState = this.mergeFolderStates(currentfolderstate, newFolderStateObj);
                        this._viewApi.SetFolderState(mergedState);
                        logger_1.Logger.info("Merged folder state saved:", mergedState);
                    }
                    catch (err) {
                        logger_1.Logger.info("Failed to set the folder state: ", err);
                    }
                    break;
            }
        }));
    }
    _getHtmlForWebview(webview, compiledCSSUri, scriptUri) {
        const styleResetUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "reset.css"));
        const styleMainUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "sidebar", "sidebar.css"));
        const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "media", "vscode.css"));
        const styleAppUri = webview.asWebviewUri(vscode.Uri.joinPath(this._extensionUri, "webviews", "app.css"));
        // Use a nonce to only allow a specific script to be run.
        const nonce = (0, util_1.getNonce)();
        return `<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="Content-Security-Policy" content="img-src https: data:; style-src 'unsafe-inline' ${webview.cspSource}; script-src 'nonce-${nonce}';">   
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&display=swap" rel="stylesheet"> 
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
                    <link href="${styleResetUri}" rel="stylesheet">
                    <link href="${styleVSCodeUri}" rel="stylesheet">
                    <link href="${styleMainUri}" rel="stylesheet">
                    <link href="${styleAppUri}" rel="stylesheet">
                    <link href="${compiledCSSUri}" rel="stylesheet">
                </head>
                <body style="background-color: var(--vscode-titleBar-activeBackground);">
                </body>
                <script nonce="${nonce}" src="${scriptUri}"></script>
                </html>`;
    }
    getInitialDataForPage(page) {
        return __awaiter(this, void 0, void 0, function* () {
            let initialData;
            switch (page) {
                case view_1.Page.HOME:
                    // get the auth status
                    const authState = this._viewApi.GetAuthState();
                    const serverstatus = this._viewApi.GetServerStatus();
                    initialData = {
                        command: view_1.MessageType.HOMEPAGE_PROPS,
                        createdAt: Date.now(),
                        value: { authStatus: authState.signedIn ? auth_1.AUTH_STATUS.SIGNED_IN : auth_1.AUTH_STATUS.SIGNED_OUT, serverStatus: serverstatus }
                    };
                    break;
                case view_1.Page.FOLDER_TREE:
                    /**Because there are many variable went ahead with destructuring and using them directly */
                    const [treeviewdata, { failedTests, noCoverageTests, passedTests }] = yield Promise.all([
                        this._viewApi.GetProjectFolderStructure(this.WorkSpaceRoot),
                        this._viewApi.GetUserStats()
                    ]);
                    const workspaceName = path_1.default.basename(this.WorkSpaceRoot);
                    logger_1.Logger.info("Here is the treeview structure and state", treeviewdata);
                    /**Setting the folder structure state before sending to the svelte */
                    const folderstructure = this.updateFolderStructureState(treeviewdata.folderItem, treeviewdata.folderState);
                    initialData = {
                        command: view_1.MessageType.FOLDER_TREE_PROPS,
                        createdAt: Date.now(),
                        value: {
                            treeviewdata: folderstructure,
                            workspaceName,
                            failedTests,
                            noCoverageTests,
                            passedTests,
                        }
                    };
                    break;
            }
            return initialData;
        });
    }
    setHistoryOpts(showHistory, runId) {
        this.historyOpt = {
            showHistory: showHistory,
            runId: runId,
        };
    }
    getHistoryOpts() {
        return this.historyOpt;
    }
    /**This is used to update the current folder structure according to the folderstate */
    updateFolderStructureState(folderStructure, folderState) {
        // Normalize folderState to a real Map
        if (!(folderState instanceof Map)) {
            logger_1.Logger.warn("folderState is not a Map, converting from plain object:", folderState);
            folderState = new Map(Object.entries(folderState));
        }
        return folderStructure.map(item => {
            const isCollapsed = folderState.has(item.fullPath)
                ? folderState.get(item.fullPath)
                : item.collapsed;
            const updatedChildren = item.children
                ? this.updateFolderStructureState(item.children, folderState)
                : [];
            return Object.assign(Object.assign({}, item), { collapsed: isCollapsed, children: updatedChildren });
        });
    }
    /**This function updates the older key value pair and append the new key value paris */
    mergeFolderStates(currentState, newState) {
        for (const [key, value] of Object.entries(newState)) {
            currentState.set(key, value);
        }
        return currentState;
    }
    runUTGByFileType(utgmessage) {
        return __awaiter(this, void 0, void 0, function* () {
            const { target, args } = utgmessage;
            const conf = {
                filePath: "",
                functionName: "",
                singleUtgTest: false,
                additional_prompts: "",
            };
            /**
             * Handles UTG (Unit Test Generation) execution based on the target type.
             *
             * Targets:
             * - PLAY.FUNCTION: Generate tests for a specific function.
             * - PLAY.FILE: Generate tests for an entire file.
             * - PLAY.ADDITIONAL_PROMPTS: Generate tests for a file using additional prompts.
             */
            this.renderPage(view_1.Page.STEPS);
            switch (target) {
                case agent_1.PLAY.FILE: {
                    const { filepath } = args;
                    if (!filepath) {
                        logger_1.Logger.error("File path not provided for UTG");
                        return;
                    }
                    conf.filePath = filepath;
                    conf.singleUtgTest = false;
                    this._viewApi.Utg(conf);
                    break;
                }
                case agent_1.PLAY.FUNCTION: {
                    const { filepath, functioname } = args;
                    if (!filepath || !functioname) {
                        logger_1.Logger.error("File path or function name not provided for function-level UTG");
                        return;
                    }
                    conf.filePath = filepath;
                    conf.functionName = functioname;
                    conf.singleUtgTest = true;
                    this._viewApi.Utg(conf);
                    break;
                }
                case agent_1.PLAY.ADDITIONAL_PROMPTS: {
                    const { filepath, additionalprompts } = args;
                    if (!filepath) {
                        logger_1.Logger.error("Missing filepath for UTG");
                        return;
                    }
                    if (!additionalprompts) {
                        logger_1.Logger.error("going with the empty additional prompts");
                    }
                    conf.filePath = filepath;
                    conf.additional_prompts = additionalprompts;
                    conf.singleUtgTest = false;
                    this._viewApi.Utg(conf);
                    break;
                }
            }
        });
    }
    /**Extracts the functions and send to Foldertree page */
    sendFunctions(filePath, fileExtension) {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const structure = yield this._viewApi.GetAllFunctionsInFile(filePath, fileExtension);
                const functions = [];
                for (let index = 0; index < structure.length; index++) {
                    const functionitem = {
                        id: (0, uuid_1.v4)().toString(),
                        label: structure[index].name,
                        fullPath: filePath,
                        itemType: agent_1.ItemType.Function,
                        collapsed: false,
                    };
                    functions.push(functionitem);
                }
                const functionpayload = {
                    command: view_1.MessageType.LOAD_FUNCTIONS,
                    createdAt: Date.now(),
                    value: {
                        functions,
                        filePath: filePath
                    }
                };
                this.updateDataInSvelte(functionpayload);
            }
            catch (err) {
                logger_1.Logger.error("Failed to fetch function Name in view", err);
            }
        });
    }
    /*
    * Different functions to handle the messages from the webview
    */
    SaveTestHistory(data) {
        if (data.testStatus === utg_1.TestStatus.IDLE || data.testStatus === utg_1.TestStatus.PROGRESS) {
            logger_1.Logger.info("Test is still running, not saving the history");
            return;
        }
        logger_1.Logger.info("Saving test history with status: ", data.testStatus);
        try {
            this._historyStorage.saveTestResult({
                id: (0, uuid_1.v4)(),
                timestamp: new Date(),
                testGenInfo: data
            });
        }
        catch (error) {
            logger_1.Logger.error("Error while saving test history: ", error);
            return;
        }
        logger_1.Logger.info("Test history saved successfully");
    }
    SendTestGenInfoToView(data) {
        // get the current auth state
        const authState = this._viewApi.GetAuthState();
        // if the user is not signed in, show the sign in page
        if (!authState.signedIn) {
            logger_1.Logger.info("not sending data to svelte as user is not signed in");
            return;
        }
        const message = {
            command: view_1.MessageType.GEN_INFO,
            createdAt: Date.now(),
            value: { testgenInfo: data, isHistory: false }
        };
        const currentPage = this._viewApi.GetCurrentPage();
        if (currentPage !== view_1.Page.STEPS || this.historyOpt.showHistory) { // if the page is not steps or if the user is viewing history
            this.setHistoryOpts(false, ""); // reset the history opts
            this.RenderPageWithData(view_1.Page.STEPS, message);
            return;
        }
        logger_1.Logger.info(`Sending steps to svelte: ${JSON.stringify(message.value)}`);
        this.updateDataInSvelte(message);
    }
    SendAuthStateToView(authStatus) {
        const message = {
            command: view_1.MessageType.AUTH_STATUS,
            createdAt: Date.now(),
            value: { status: authStatus }
        };
        // only render the home page if the user is signed out and the page was not already home else send the auth status to svelte
        const currentPage = this._viewApi.GetCurrentPage();
        logger_1.Logger.info(`Sending auth status to svelte: ${authStatus} with current page: ${currentPage}`);
        if (authStatus === auth_1.AUTH_STATUS.SIGNED_OUT && currentPage !== view_1.Page.HOME) {
            this.RenderPageWithData(view_1.Page.HOME, message);
            return;
        }
        this.updateDataInSvelte(message);
    }
    UpdateKeployServerStatus(Server_Status) {
        return __awaiter(this, void 0, void 0, function* () {
            const message = {
                command: view_1.MessageType.KEPLOY_STATUS,
                createdAt: Date.now(),
                value: { status: Server_Status }
            };
            this.updateDataInSvelte(message);
            logger_1.Logger.info("Sending server status to svelte:", Server_Status);
        });
    }
}
exports.ViewProvider = ViewProvider;
//# sourceMappingURL=view.js.map