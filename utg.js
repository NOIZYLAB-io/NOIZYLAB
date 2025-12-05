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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.UTG = void 0;
const vscode_1 = __importDefault(require("vscode"));
const axios_1 = __importDefault(require("axios"));
const agent_1 = require("../../@types/agent");
const util_1 = require("../../util/util");
const logger_1 = require("../../util/logger");
const events_1 = require("./events");
class UTG {
    constructor(keploy, workspaceRoot) {
        this.keploy = keploy;
        this.workspaceRoot = workspaceRoot;
        this.eventHandler = new events_1.StepsEventHandler();
    }
    GetTestGenInfo() {
        return this.eventHandler.GetTestGenInfo();
    }
    ToggleTests(toggleconf) {
        const ToggledSteps = this.eventHandler.ToggleStep(toggleconf);
        this.keploy.SendTestGenInfoToView(ToggledSteps);
    }
    runUtg(filePath, functionName, singleUtgTest, additional_prompts) {
        return __awaiter(this, void 0, void 0, function* () {
            // get the auth state
            const authState = this.keploy.GetAuthState();
            if (!authState.signedIn) {
                this.keploy.SignInViaKeploy();
                return;
            }
            // get the subscription status
            let subscriptionEnded = this.keploy.GetSubscriptionEnded();
            if (subscriptionEnded) {
                // redirect to pricing page
                try {
                    if (!authState.jwtToken) {
                        logger_1.Logger.info("token not found");
                        return;
                    }
                    const apiResponse = (yield this.getSessionCount(authState.jwtToken)) || 'no response';
                    const response = JSON.parse(apiResponse);
                    logger_1.Logger.info("Get Session Count Response:", response);
                    if (response.usedCall >= response.totalCall) {
                        const redirectUrl = `${agent_1.KEPLOY_APP_URI}/signin?take_to_pricing=true`;
                        logger_1.Logger.info("Opening pricing page:", redirectUrl);
                        vscode_1.default.env.openExternal(vscode_1.default.Uri.parse(redirectUrl));
                        return;
                    }
                    // subscription is active
                    logger_1.Logger.info("Subscription is active");
                    this.keploy.SetSubscriptionEnded(false);
                    subscriptionEnded = false;
                }
                catch (error) {
                    logger_1.Logger.error('Subscription renewal error:', error);
                    logger_1.Logger.info("Signing Out");
                    this.keploy.SignOut();
                    vscode_1.default.window.showErrorMessage('(Keploy) Subscription renewal error');
                    return;
                }
            }
            // here the subscription is active
            logger_1.Logger.info("UTG Details:", { filePath, functionName, additionalPrompts: additional_prompts, singleUtgTest });
            this.keploy.SetFilePath(filePath);
            // get utg execution status
            const utgExecutionStatus = this.keploy.GetUTGExecutionStatus();
            if (utgExecutionStatus) {
                logger_1.Logger.info("UTG execution status is true, test generation is already in progress for file path:", filePath);
                vscode_1.default.window.showWarningMessage('(Keploy) Test generation is already in progress');
                return;
            }
            if (singleUtgTest) {
                logger_1.Logger.info("Generating UT for function:", functionName);
            }
            else {
                logger_1.Logger.info("Generating UT for entire file");
                functionName = "";
            }
            /**Saving the current Execution Status here*/
            this.keploy.SetUTGExecutionStatus(true);
            /**Helpful for retrying utg */
            const conf = {
                filePath: filePath,
                functionName: functionName,
                singleUtgTest: singleUtgTest,
                additional_prompts: additional_prompts
            };
            /** Saving UTG Conf*/
            this.keploy.SaveUTGConf(conf);
            try {
                // Generate tests
                yield this.generateUT(filePath, functionName, additional_prompts);
                // set the utg execution status to false because the test generation is completed for the file path
                this.keploy.SetUTGExecutionStatus(false);
                // delay for 2 seconds
                (0, util_1.delay)(2000);
                if (!authState.jwtToken) {
                    logger_1.Logger.info("token not found");
                    return;
                }
                try {
                    const apiResponse = (yield this.getSessionCount(authState.jwtToken)) || 'no response';
                    const response = JSON.parse(apiResponse);
                    // this.keploy.Messenger({ type: MessageType.UPDATE_API_RESPONSE, value: apiResponse });
                    logger_1.Logger.info("Get Session Count Response:", response);
                    if (response.usedCall === response.totalCall) {
                        logger_1.Logger.info("Session limit reached");
                        this.keploy.SetSubscriptionEnded(true);
                        return;
                    }
                }
                catch (error) {
                    logger_1.Logger.error("Error getting session count after test generation:", error);
                    return;
                }
            }
            catch (error) {
                this.keploy.SetUTGExecutionStatus(false);
                vscode_1.default.window.showErrorMessage('(Keploy) Error occurred in Keploy UTG: ' + error);
            }
            finally {
                // save the test history
                this.keploy.SaveTestHistory(this.eventHandler.GetTestRunResult());
            }
        });
    }
    abortUtg() {
        if (!this.controller) {
            logger_1.Logger.info("No active UTG execution to abort");
            return;
        }
        this.controller.abort();
        logger_1.Logger.info("UTG execution aborted");
    }
    getSessionCount(token) {
        return __awaiter(this, void 0, void 0, function* () {
            const url = `${agent_1.API_SERVER_URI}/ai/call/count`;
            try {
                const response = yield axios_1.default.get(url, {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });
                return JSON.stringify(response.data); // Return the API response data as a string
            }
            catch (error) {
                if (axios_1.default.isAxiosError(error)) {
                    // Handle axios-specific error
                    logger_1.Logger.info(`API call failed: ${error.message}`);
                }
                else {
                    // Handle oth   er errors (in case they are not Axios errors)
                    logger_1.Logger.info('An unknown error occurred.');
                }
                return null; // Return null in case of error
            }
        });
    }
    generateUT(sourceFilePath, functionUnderTest, additional_prompts) {
        return __awaiter(this, void 0, void 0, function* () {
            this.controller = new AbortController();
            const signal = this.controller.signal; // Use the signal for the API request
            // Prepare the API request payload
            const requestPayload = {
                sourceFilePath,
                rootDir: this.workspaceRoot,
                additionalPrompt: additional_prompts || undefined,
                functionUnderTest: functionUnderTest || undefined,
            };
            // reset the event handle to handle the new test generation event
            this.eventHandler.Reset();
            // get the empty test info (just to start the page)
            const emptyTestInfo = this.eventHandler.GetTestGenInfo();
            this.keploy.SendTestGenInfoToView(emptyTestInfo);
            try {
                // Make the API call to generate tests
                logger_1.Logger.info("Sending generateTests request with payload:", requestPayload);
                const responseStream = yield this.keploy.GenerateUT(requestPayload, signal);
                if (!responseStream || !responseStream.getReader) {
                    logger_1.Logger.error("Response is not a readable stream.");
                    throw new Error("Response is not a readable stream.");
                }
                // Process the streaming response
                const reader = responseStream.getReader();
                const decoder = new TextDecoder("utf-8");
                logger_1.Logger.info("Streaming response data...");
                let streamClosed = false;
                let chunkCount = 0;
                try {
                    while (!streamClosed) {
                        if (signal.aborted) {
                            logger_1.Logger.info("UT generation aborted; stopping the stream");
                            yield reader.cancel();
                            const abortInfo = this.eventHandler.HandleAbort("UT generation aborted.");
                            this.keploy.SendTestGenInfoToView(abortInfo);
                            break;
                        }
                        const data = yield reader.read();
                        streamClosed = data.done;
                        if (!data.value) {
                            continue;
                        }
                        chunkCount++;
                        const chunk = decoder.decode(data.value, { stream: true });
                        logger_1.Logger.info(chunkCount.toString(), ". Received chunk:", chunk);
                        const genInfo = this.eventHandler.HandleChunk(chunk, chunkCount);
                        //Sending Generated Info to webview
                        this.keploy.SendTestGenInfoToView(genInfo);
                    }
                    if (streamClosed) {
                        if (signal.aborted) {
                            logger_1.Logger.info("UT generation aborted; stopping the stream");
                            const abortInfo = this.eventHandler.HandleAbort("Test generation stopped by user ⚠️");
                            // send the abortInfo to the steps Page
                            this.keploy.SendTestGenInfoToView(abortInfo);
                            return;
                        }
                        // if the stream is closed without any data or the last event not error or complete then handle the close stream event
                        logger_1.Logger.info("Stream closed. Handling close stream event...");
                        const { info, unexpectedClose } = this.eventHandler.HandleCloseStream(sourceFilePath);
                        if (unexpectedClose) {
                            vscode_1.default.window.showWarningMessage("(Keploy) Test generation request closed unexpectedly.");
                            this.keploy.SendTestGenInfoToView(info); // send the info to the steps Page
                        }
                    }
                }
                catch (error) {
                    if (signal.aborted) {
                        logger_1.Logger.info("Streaming aborted intentionally.");
                        const abortInfo = this.eventHandler.HandleAbort("Streaming aborted intentionally.");
                        // send the abortInfo to the steps Page
                        this.keploy.SendTestGenInfoToView(abortInfo);
                        return;
                    }
                    const errorInfo = this.eventHandler.HandleError(error, sourceFilePath);
                    vscode_1.default.window.showWarningMessage("(Keploy) Test generation request closed unexpectedly.");
                    // send the errorInfo to the steps Page
                    this.keploy.SendTestGenInfoToView(errorInfo);
                    logger_1.Logger.error("Connection broken or streaming failed:", error.message);
                    return;
                }
            }
            catch (error) { //TODO: need to handle this catch properly.
                if (signal.aborted) {
                    logger_1.Logger.info("UT generation aborted intentionally.");
                    const abortInfo = this.eventHandler.HandleAbort("UT generation aborted intentionally.");
                    // send the abortInfo to the steps Page
                    this.keploy.SendTestGenInfoToView(abortInfo);
                    return;
                }
                const errorInfo = this.eventHandler.HandleError(error, sourceFilePath);
                vscode_1.default.window.showWarningMessage("(Keploy) Test generation request closed unexpectedly.");
                // send the errorInfo to the steps Page
                this.keploy.SendTestGenInfoToView(errorInfo);
                logger_1.Logger.error("Error generating UT:", error.message);
                return;
            }
            logger_1.Logger.info("Streaming completed...");
        });
    }
}
exports.UTG = UTG;
//# sourceMappingURL=utg.js.map