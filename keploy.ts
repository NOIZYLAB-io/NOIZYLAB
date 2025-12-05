import * as vscode from 'vscode';
import { Abstract } from "./abstract";
import { InstallationProgress } from './@types/progress';
import { GlobalState } from './platform/state/global';
import { FunctionName, Lens } from './@types/lens';
import { CodeLensProvider } from './providers/lens';
import { ViewProvider } from './providers/view';
import { ServerManager } from './platform/agent/keploy';
import { Agent, FolderItem, Status } from './@types/agent';
import { Watcher } from './@types/watcher';
import { FileWatcher } from './util/watcher';
import { AUTH_STATUS, Auth as AuthI, AuthState } from './@types/auth';
import { WorkspaceState } from './platform/state/workspace';
import { Auth } from './platform/auth/auth';
import { Commands } from './cmd/cmd';
import { Command, KeployContextKeys } from './@types/cmd';
import { UTG } from './service/utg/utg';
import { RunConfig, TestGenInfo, UTGService } from './@types/utg';
import { isTokenExpired } from './util/util';
import { AuthType } from './@types/auth';
import { View, Page, UserStats } from './@types/view';
import { Logger } from './util/logger';
import { ToggleStepMessage } from './@types/steps';

export class Keploy extends Abstract {

    private context: vscode.ExtensionContext;
    private globalState: GlobalState;
    private workspaceState: WorkspaceState;

    private agent: ServerManager;
    private view: ViewProvider;
    private auth: Auth;
    private watcher: FileWatcher;
    private utg: UTG;
    private workspaceRoot: string;

    constructor(context: vscode.ExtensionContext) {
        super();
        this.context = context;

        // initialize all the necessary components
        this.globalState = new GlobalState(this.context.globalState);
        this.workspaceState = new WorkspaceState(this.context.workspaceState);

        this.agent = new ServerManager(this as Agent);

        new CodeLensProvider(this.context.subscriptions, this as Lens);

        new Commands(this.context.subscriptions, this as Command);

        this.auth = new Auth(this.context.subscriptions, this as AuthI);

        this.watcher = new FileWatcher(this.context.subscriptions, this as Watcher);


        // set workspace root
        this.workspaceRoot = vscode.workspace.workspaceFolders
            ? vscode.workspace.workspaceFolders[0].uri.fsPath
            : '';
        this.workspaceState.SetWorkspaceRoot(this.workspaceRoot);

        Logger.info("Workspace Root:", this.workspaceRoot);

        this.utg = new UTG(this as UTGService, this.workspaceRoot);
        this.view = new ViewProvider(this.context, this as View, this.workspaceRoot);

    }


    async Start(): Promise<void> {

        if (!this.workspaceRoot) {
            Logger.info("Workspace root not found");
            vscode.window.showErrorMessage("(Keploy) Workspace root not found, please open a workspace");
            throw new Error("Workspace root not found");
        }

        // start the watcher
        this.watcher.startWatching();

        try {
            Logger.info("Checking authentication...");
            await this.checkAuthentication();
        } catch (error: any) {
            Logger.error("Error while checking authentication:", error);
            vscode.window.showErrorMessage("(Keploy) Error while checking authentication: " + error.message);
        }
    }

    async Stop(): Promise<void> {
        this.utg.abortUtg();
        await this.agent.closeSession(this.workspaceRoot);
        this.workspaceState.CleanUp(); // clean up workspace state
    }

    private async checkAuthentication() {
        // Get the auth state
        let authState: AuthState = this.globalState.GetAuthState();

        if (!authState) {
            Logger.info("Auth state not found");
            vscode.commands.executeCommand('setContext', KeployContextKeys.SIGNED_IN, false);
            vscode.commands.executeCommand('setContext', KeployContextKeys.SIGNED_OUT, true);
            Logger.warn("Auth state not found. Please sign in to continue");
            return;
        }

        let isSignedIn = authState.signedIn || !!authState.jwtToken; // Check if signed in OR has JWT token

        if (authState.jwtToken && isTokenExpired(authState.jwtToken)) {
            Logger.warn("JWT token expired. Hence signing out and attempting to sign in again...");

            // Sign out and clear the token
            this.SignOut();

            vscode.window.showWarningMessage("(Keploy) Your session has expired. Trying to sign in again...");

            // Reauthenticate based on AuthType
            if (authState.authType === AuthType.VSCODE_GITHUB) {
                await this.SignInViaGitHubVSCode();
            } else {
                this.SignInViaKeploy();
            }
            return;
        }

        if (isSignedIn) {
            vscode.commands.executeCommand('setContext', KeployContextKeys.SIGNED_IN, true);
            vscode.commands.executeCommand('setContext', KeployContextKeys.SIGNED_OUT, false);
            vscode.window.showInformationMessage('(Keploy) You are already signed in!');

            if (!authState.signedIn) {
                Logger.info('JWT token found; updating signed-in state');
                this.globalState.SetAuthState({ ...authState, signedIn: true });
            }

            // Setup and start the Keploy agent as the user is signed in
            this.agent.setupKeploy();
        } else {
            Logger.warn("User is not signed in and no token found");
            vscode.commands.executeCommand('setContext', KeployContextKeys.SIGNED_IN, false);
            vscode.commands.executeCommand('setContext', KeployContextKeys.SIGNED_OUT, true);
            Logger.warn("Please sign in to continue");
        }
    }


    // Functions to clear the extension state (useful for testing and debugging)

    async ClearKeployState() {
        this.CleanUpState();
        this.SignOut();
        // restart the extension
        vscode.commands.executeCommand("workbench.action.reloadWindow");
    }


    /** ================== Keploy Interface Methods ================== */

    /** ================== Agent Methods ================== */

    GetKeployInstallationProgress(): InstallationProgress {
        return this.globalState.GetKeployInstallationProgress();
    }

    ClearKeployInstallationProgress(): void {
        this.globalState.ClearKeployInstallationProgress();
    }

    KeployStatusMessenger(Server_Status: Status.ACTIVE | Status.INACTIVE | Status.INSTALLING): Promise<void> {
        /**Saving the  status here for further use. */
        this.globalState.SetCurrentServerStatus(Server_Status);

        return this.view.UpdateKeployServerStatus(Server_Status);
    }

    /** ================== Auth Methods ================== */


    SetAuthState(state: AuthState): void {
        this.globalState.SetAuthState(state);
    }

    SendAuthStateToView(authStatus: AUTH_STATUS): void {
        this.view.SendAuthStateToView(authStatus);
    }


    /** ================== Command Methods ================== */ // common with some other methods as well.

    async SignInViaGitHubVSCode(): Promise<void> {
        await this.auth.signInViaGitHubVSCode();
    }

    SignInViaKeploy(): void {
        this.auth.signInViaKeploy();
    }

    SignOut(): void {
        this.auth.signOut();
    }

    Utg(conf: RunConfig): void {
        // it should open the sidebar if it was not opened.
        vscode.commands.executeCommand('workbench.view.extension.Keploy-Sidebar');
        const { filePath, functionName, singleUtgTest, additional_prompts } = conf;
        this.utg.runUtg(filePath, functionName, singleUtgTest, additional_prompts);
    }


    /** ================== Lens Methods ================== */
    GetAllFunctionsInFile(filePath: string, fileExtension: string): Promise<FunctionName[]> {
        return this.agent.getAllFunctionsInFile(filePath, fileExtension);
    }


    /** ================== UTGService Methods ================== */

    GetSubscriptionEnded(): boolean {
        return this.globalState.GetSubscriptionEnded();
    }

    SetSubscriptionEnded(status: boolean): void {
        this.globalState.SetSubscriptionEnded(status);
    }

    GetFilePath(): string {
        return this.workspaceState.GetFilePath();
    }

    SetFilePath(filePath: string): void {
        this.workspaceState.SetFilePath(filePath);
    }

    GetUTGExecutionStatus(): boolean {
        return this.workspaceState.GetUTGExecutionStatus();
    }

    SetUTGExecutionStatus(status: boolean): void {
        this.workspaceState.SetUTGExecutionStatus(status);
    }

    GetAuthState(): AuthState {
        return this.globalState.GetAuthState();
    }

    GetFolderState(): Map<string, boolean> {
        return this.workspaceState.GetFolderState();
    }

    SetFolderState(state: Map<string, boolean>): void {
        this.workspaceState.SetFolderState(state);
    }

    GenerateUT(request: any, signal?: AbortSignal): Promise<ReadableStream<Uint8Array>> {
        return this.agent.generateUT(request, signal);
    }

    SendTestGenInfoToView(data: TestGenInfo): void {
        this.view.SendTestGenInfoToView(data);
    }

    SaveTestHistory(data: TestGenInfo): void {
        this.view.SaveTestHistory(data);
    }

    SaveUTGConf(conf: RunConfig): void {
        this.workspaceState.SaveUTGConf(conf);
    }


    /** ================== View Methods ================== */


    SetCurrentPage(page: Page): void {
        this.workspaceState.SetCurrentPage(page);
    }

    GetCurrentPage(): Page {
        return this.workspaceState.GetCurrentPage();
    }

    GetProjectFolderStructure(workspaceRoot: string): Promise<{ folderItem: FolderItem[], folderState: Map<string, boolean> }> {
        return this.agent.getProjectFolderStructure(workspaceRoot);
    }

    GetServerStatus(): Status {
        return this.globalState.GetCurrentServerStatus();
    }


    GetUserStats(): Promise<UserStats> {
        return this.agent.getTestsData();
    }

    AbortUtg(): void {
        this.utg.abortUtg();
    }

    GetSessionCount(token: string): Promise<string | null> {
        return this.utg.getSessionCount(token);
    }

    GetTestGenInfo(): TestGenInfo {
        return this.utg.GetTestGenInfo();
    }

    GetUTGRunConf(): RunConfig {
        return this.workspaceState.GetUtgConf();
    }

    ToggleStep(toggleconf: ToggleStepMessage): void {
        this.utg.ToggleTests(toggleconf);
    }

    /** ================== Watcher Methods ================== */

    GetExtensionVersion(): string {
        return this.globalState.GetExtensionVersion();
    }

    SetExtensionVersion(version: string): void {
        this.globalState.SetExtensionVersion(version);
    }

    CleanUpState(): void {
        this.globalState.CleanUp();
        this.workspaceState.CleanUp();
    }

    /** ================== Commmon Methods ================== */

    async SetupKeploy(): Promise<void> {
        await this.agent.setupKeploy();
    }

    ShutDown(): void {
        this.agent.shutdown();
    }

}
