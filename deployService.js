"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.DeployService = void 0;
exports.getDockerImageSpec = getDockerImageSpec;
const UUID = require("vscode-languageclient/lib/utils/uuid");
const constants = require("../../common/constants");
const utils = require("../../common/utils");
const vscode = require("vscode");
const shellExecutionHelper_1 = require("../../tools/shellExecutionHelper");
const azureSqlClient_1 = require("./azureSqlClient");
const connectionService_1 = require("../connections/connectionService");
class DeployService {
    _azureSqlClient;
    _outputChannel;
    constructor(_azureSqlClient = new azureSqlClient_1.AzureSqlClient(), _outputChannel, shellExecutionHelper = undefined) {
        this._azureSqlClient = _azureSqlClient;
        this._outputChannel = _outputChannel;
        this._shellExecutionHelper = shellExecutionHelper ?? new shellExecutionHelper_1.ShellExecutionHelper(this._outputChannel);
        this._connectionService = new connectionService_1.ConnectionService(this._outputChannel);
    }
    _shellExecutionHelper;
    _connectionService;
    async verifyDocker() {
        try {
            await this.executeCommand(`docker version --format {{.Server.APIVersion}}`);
            // TODO verify min version
        }
        catch (error) {
            throw Error(constants.dockerNotRunningError(utils.getErrorMessage(error)));
        }
    }
    /**
     * Creates a new Azure Sql server and tries to connect to the new server. If connection fails because of firewall rule, it prompts user to add firewall rule settings
     * @param profile Azure Sql server settings
     * @returns connection url for the new server
     */
    async createNewAzureSqlServer(profile) {
        if (!profile?.sqlDbSetting) {
            return undefined;
        }
        this.logToOutput(constants.creatingAzureSqlServer(profile?.sqlDbSetting?.serverName));
        // Create the server
        const server = await this._azureSqlClient.createOrUpdateServer(profile.sqlDbSetting.session, profile?.sqlDbSetting.resourceGroupName, profile?.sqlDbSetting.serverName, {
            location: profile?.sqlDbSetting?.location,
            administratorLogin: profile?.sqlDbSetting.userName,
            administratorLoginPassword: profile?.sqlDbSetting.password
        });
        if (server) {
            this._outputChannel.appendLine(constants.serverCreated);
            profile.sqlDbSetting.serverName = server;
            this.logToOutput(constants.azureSqlServerCreated(profile?.sqlDbSetting?.serverName));
            // Connect to the server
            return await this._connectionService.getConnection(profile.sqlDbSetting, false, constants.master);
        }
        return undefined;
    }
    async deployToContainer(profile, project) {
        return await this.executeTask(constants.deployDbTaskName, async () => {
            await this.verifyDocker();
            this.logToOutput(constants.dockerImageMessage);
            this.logToOutput(profile.dockerSettings.dockerBaseImage);
            this.logToOutput(constants.dockerImageEulaMessage);
            this.logToOutput(profile.dockerSettings.dockerBaseImageEula);
            const imageSpec = getDockerImageSpec(project.projectFileName, profile.dockerSettings.dockerBaseImage);
            // If profile name is not set use the docker name to have a unique name
            if (!profile.dockerSettings.profileName) {
                profile.dockerSettings.profileName = imageSpec.containerName;
            }
            await this.cleanDockerObjectsIfNeeded(imageSpec.label);
            this.logToOutput(constants.creatingDeploymentSettingsMessage);
            // Create commands
            //
            this.logToOutput(constants.runningDockerMessage);
            // Building the image and running the docker
            //
            const createdDockerId = await this.runDockerContainer(imageSpec, profile.dockerSettings);
            this.logToOutput(`Docker container created. Id: ${createdDockerId}`);
            // Waiting a bit to make sure docker container doesn't crash
            //
            const runningDockerId = await utils.retry('Validating the docker container', async () => {
                return this.executeCommand(`docker ps -q -a --filter label=${imageSpec.label} -q`);
            }, (dockerId) => {
                return Promise.resolve({ validated: dockerId !== undefined, errorMessage: constants.dockerContainerNotRunningErrorMessage });
            }, (dockerId) => {
                return Promise.resolve(dockerId);
            }, this._outputChannel);
            if (runningDockerId) {
                this.logToOutput(constants.dockerContainerCreatedMessage(runningDockerId));
                return await this._connectionService.getConnection(profile.dockerSettings, false, 'master');
            }
            else {
                this.logToOutput(constants.dockerContainerFailedToRunErrorMessage);
                if (createdDockerId) {
                    // Get the docker logs if docker was created but crashed
                    await this.executeCommand(constants.dockerLogMessage(createdDockerId));
                }
            }
            return undefined;
        });
    }
    async runDockerContainer(dockerImageSpec, profile) {
        // Sensitive data to remove from output console
        const sensitiveData = [profile.password];
        // Running commands to build the docker image
        await this.executeCommand(`docker pull ${profile.dockerBaseImage}`);
        await this.executeCommand(`docker run -p ${profile.port}:1433 -e "MSSQL_SA_PASSWORD=${profile.password}" -e "ACCEPT_EULA=Y" -e "MSSQL_PID=Developer" --label ${dockerImageSpec.label} -d --name ${dockerImageSpec.containerName} ${profile.dockerBaseImage} `, sensitiveData);
        return await this.executeCommand(`docker ps -q -a --filter label=${dockerImageSpec.label} -q`);
    }
    async executeTask(taskName, task) {
        const azdataApi = utils.getAzdataApi();
        if (azdataApi) {
            return new Promise((resolve, reject) => {
                let msgTaskName = taskName;
                azdataApi.tasks.startBackgroundOperation({
                    displayName: msgTaskName,
                    description: msgTaskName,
                    isCancelable: false,
                    operation: async (op) => {
                        try {
                            let result = await task();
                            op.updateStatus(azdataApi.TaskStatus.Succeeded);
                            resolve(result);
                        }
                        catch (error) {
                            let errorMsg = constants.taskFailedError(taskName, error ? error.message : '');
                            op.updateStatus(azdataApi.TaskStatus.Failed, errorMsg);
                            reject(errorMsg);
                        }
                    }
                });
            });
        }
        else {
            return await task();
        }
    }
    logToOutput(message) {
        this._outputChannel.appendLine(message);
    }
    async executeCommand(cmd, sensitiveData = [], timeout = 5 * 60 * 1000) {
        return await this._shellExecutionHelper.runStreamedCommand(cmd, undefined, sensitiveData, timeout);
    }
    async getCurrentDockerContainer(imageLabel) {
        const currentIds = await this.executeCommand(`docker ps -q -a --filter label=${imageLabel}`);
        return currentIds ? currentIds.split(/\r?\n/) : [];
    }
    /**
     * Checks if any containers with the specified label already exist, and if they do prompt the user whether they want to clean them up
     * @param imageLabel The label of the container to search for
     */
    async cleanDockerObjectsIfNeeded(imageLabel) {
        this.logToOutput(constants.cleaningDockerImagesMessage);
        // Clean up existing docker image
        const containerIds = await this.getCurrentDockerContainer(imageLabel);
        if (containerIds.length > 0) {
            const result = await vscode.window.showQuickPick([constants.yesString, constants.noString], {
                title: constants.containerAlreadyExistForProject,
                ignoreFocusOut: true
            });
            if (result === constants.yesString) {
                this.logToOutput(constants.cleaningDockerImagesMessage);
                await this.cleanDockerObjects(containerIds, ['docker stop', 'docker rm']);
            }
        }
    }
    async cleanDockerObjects(ids, commandsToClean) {
        for (let index = 0; index < ids.length; index++) {
            const id = ids[index];
            if (id) {
                for (let commandId = 0; commandId < commandsToClean.length; commandId++) {
                    const command = commandsToClean[commandId];
                    await this.executeCommand(`${command} ${id}`);
                }
            }
        }
    }
}
exports.DeployService = DeployService;
function getDockerImageSpec(projectName, baseImage, imageUniqueId) {
    imageUniqueId = imageUniqueId ?? UUID.generateUuid();
    // Remove unsupported characters
    //
    // docker image name and tag can only include letters, digits, underscore, period and dash
    const regexForDockerImageName = /[^a-zA-Z0-9_,\-]/g;
    let imageProjectName = projectName.replace(regexForDockerImageName, '');
    const tagMaxLength = 128;
    const tag = baseImage.replace(':', '-').replace(constants.sqlServerDockerRegistry, '').replace(regexForDockerImageName, '');
    // cut the name if it's too long
    //
    imageProjectName = imageProjectName.substring(0, tagMaxLength - (constants.dockerImageNamePrefix.length + tag.length + 2));
    const imageLabel = `${constants.dockerImageLabelPrefix}-${imageProjectName}`.toLocaleLowerCase();
    const imageTag = `${constants.dockerImageNamePrefix}-${imageProjectName}-${tag}`.toLocaleLowerCase();
    const dockerName = `${constants.dockerImageNamePrefix}-${imageProjectName}-${imageUniqueId}`.toLocaleLowerCase();
    return { label: imageLabel, tag: imageTag, containerName: dockerName };
}
//# sourceMappingURL=deployService.js.map