import { Agent, FolderItem, Status } from "./@types/agent";
import { InstallationProgress } from "./@types/progress";
import { Lens, FunctionName } from "./@types/lens";
import { Watcher } from "./@types/watcher";
import { Auth, AUTH_STATUS, AuthState } from "./@types/auth";
import { Command } from "./@types/cmd";
import { RunConfig, TestGenInfo, UTGService } from "./@types/utg";
import { View, Page, UserStats } from "./@types/view";
import { ToggleStepMessage } from "./@types/steps";
// import { View, MessagePayloads, StepsInfo, Page } from "./@types/view";

export abstract class Abstract implements Agent, Auth, Command, Lens, UTGService, Watcher, View {

  /** ================== Agent Methods ================== */

  abstract GetKeployInstallationProgress(): InstallationProgress;
  abstract ClearKeployInstallationProgress(): void;
  abstract KeployStatusMessenger(Server_Status: Status.ACTIVE | Status.INACTIVE | Status.INSTALLING): Promise<void>;


  /** ================== Auth Methods ================== */

  abstract SetAuthState(state: AuthState): void;
  abstract SendAuthStateToView(authStatus: AUTH_STATUS): void;


  /** ================== Command Methods ================== */

  abstract SignInViaGitHubVSCode(): Promise<void>;
  abstract SignInViaKeploy(): void; // Common with View & UTG Methods
  abstract SignOut(): void; // Common with View & UTG Methods
  abstract ClearKeployState(): void;
  abstract Utg(conf: RunConfig): void;

  /** ================== Lens Methods ================== */

  abstract GetAllFunctionsInFile(filePath: string, fileExtension: string): Promise<FunctionName[]>;

  /** ================== UTGService Methods ================== */

  abstract GetSubscriptionEnded(): boolean;
  abstract SetSubscriptionEnded(status: boolean): void;
  abstract GetFilePath(): string;
  abstract SetFilePath(filePath: string): void;
  abstract GetUTGExecutionStatus(): boolean;
  abstract SetUTGExecutionStatus(status: boolean): void;
  abstract GetAuthState(): AuthState; // common with Agent Methods
  abstract GenerateUT(request: any, signal?: AbortSignal): Promise<ReadableStream<Uint8Array>>;
  abstract SendTestGenInfoToView(data: TestGenInfo): void;
  abstract SaveTestHistory(data: TestGenInfo): void;
  abstract SaveUTGConf(conf: RunConfig): void;

  /** ================== View Methods ================== */
  abstract GetFolderState(): Map<string, boolean>;
  abstract SetFolderState(state: Map<string, boolean>): void;
  abstract SetCurrentPage(page: Page): void;
  abstract GetCurrentPage(): Page;
  abstract GetTestGenInfo(): TestGenInfo;
  abstract GetUTGRunConf(): RunConfig;
  abstract ToggleStep(toggleconf: ToggleStepMessage): void;
  abstract GetProjectFolderStructure(workspaceRoot: string): Promise<{ folderItem: FolderItem[], folderState: Map<string, boolean> }>;
  abstract GetUserStats(): Promise<UserStats>;
  abstract GetServerStatus(): Status;


  /** ================== Watcher Methods ================== */

  abstract GetExtensionVersion(): string;

  abstract SetExtensionVersion(version: string): void;

  abstract CleanUpState(): void;

  /** ================== Common Methods ================== */


  abstract AbortUtg(): void;

  abstract SetupKeploy(): Promise<void>;

  abstract ShutDown(): void;
}
