"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.readPublishProfile = readPublishProfile;
exports.load = load;
exports.savePublishProfile = savePublishProfile;
exports.promptToSaveProfile = promptToSaveProfile;
exports.promptForSavingProfile = promptForSavingProfile;
const xmldom = require("@xmldom/xmldom");
const constants = require("../../common/constants");
const utils = require("../../common/utils");
const vscode = require("vscode");
const path = require("path");
const fs_1 = require("fs");
const sqlConnectionStringSource_1 = require("../dataSources/sqlConnectionStringSource");
const telemetry_1 = require("../../common/telemetry");
async function readPublishProfile(profileUri) {
    try {
        const dacFxService = await utils.getDacFxService();
        const profile = await load(profileUri, dacFxService);
        return profile;
    }
    catch (e) {
        void vscode.window.showErrorMessage(constants.profileReadError(e));
        throw e;
    }
}
/**
 * parses the specified file to load publish settings
 */
async function load(profileUri, dacfxService) {
    const profileText = await fs_1.promises.readFile(profileUri.fsPath);
    const profileXmlDoc = new xmldom.DOMParser().parseFromString(profileText.toString());
    // read target database name
    let targetDbName = '';
    let targetDatabaseNameCount = profileXmlDoc.documentElement.getElementsByTagName(constants.targetDatabaseName).length;
    if (targetDatabaseNameCount > 0) {
        // if there is more than one TargetDatabaseName nodes, SSDT uses the name in the last one so we'll do the same here
        targetDbName = profileXmlDoc.documentElement.getElementsByTagName(constants.targetDatabaseName)[targetDatabaseNameCount - 1].textContent;
    }
    const connectionInfo = await readConnectionString(profileXmlDoc);
    const optionsResult = await dacfxService.getOptionsFromProfile(profileUri.fsPath);
    // get all SQLCMD variables to include from the profile
    const sqlCmdVariables = utils.readSqlCmdVariables(profileXmlDoc, true);
    telemetry_1.TelemetryReporter.createActionEvent(telemetry_1.TelemetryViews.SqlProjectPublishDialog, telemetry_1.TelemetryActions.profileLoaded)
        .withAdditionalProperties({
        hasTargetDbName: (!!targetDbName).toString(),
        hasConnectionString: (!!connectionInfo?.connectionId).toString(),
        hasSqlCmdVariables: (sqlCmdVariables.size > 0).toString()
    }).send();
    return {
        databaseName: targetDbName,
        serverName: connectionInfo.server,
        connectionId: connectionInfo.connectionId,
        connection: connectionInfo.connection,
        sqlCmdVariables: sqlCmdVariables,
        options: optionsResult.deploymentOptions
    };
}
async function readConnectionString(xmlDoc) {
    let targetConnection = '';
    let connId = '';
    let server = '';
    if (xmlDoc.documentElement.getElementsByTagName(constants.targetConnectionString).length > 0) {
        const targetConnectionString = xmlDoc.documentElement.getElementsByTagName(constants.TargetConnectionString)[0].textContent;
        const dataSource = new sqlConnectionStringSource_1.SqlConnectionDataSource('', targetConnectionString);
        let username = '';
        const connectionProfile = dataSource.getConnectionProfile();
        try {
            const azdataApi = utils.getAzdataApi();
            if (dataSource.integratedSecurity) {
                if (azdataApi) {
                    const connectionResult = await utils.getAzdataApi().connection.connect(connectionProfile, false, false);
                    if (!connectionResult.connected) {
                        const connection = await utils.getAzdataApi().connection.openConnectionDialog(undefined, connectionProfile, {
                            saveConnection: false,
                            showDashboard: false,
                            showConnectionDialogOnError: true,
                            showFirewallRuleOnError: true
                        });
                        connId = connection.connectionId;
                    }
                    else {
                        connId = connectionResult.connectionId;
                    }
                }
                else {
                    // TODO@chgagnon - hook up VS Code MSSQL
                }
                server = dataSource.server;
                username = constants.defaultUser;
            }
            else {
                if (azdataApi) {
                    const connection = await utils.getAzdataApi().connection.openConnectionDialog(undefined, connectionProfile, {
                        saveConnection: false,
                        showDashboard: false,
                        showConnectionDialogOnError: true,
                        showFirewallRuleOnError: true
                    });
                    connId = connection.connectionId;
                    server = connection.options['server'];
                    username = connection.options['user'];
                }
                else {
                    // TODO@chgagnon - hook up VS Code MSSQL
                }
            }
            targetConnection = `${server} (${username})`;
        }
        catch (err) {
            throw new Error(constants.unableToCreatePublishConnection(utils.getErrorMessage(err)));
        }
    }
    return {
        connectionId: connId,
        connection: targetConnection,
        server: server
    };
}
/**
 * saves publish settings to the specified profile file
 */
async function savePublishProfile(profilePath, databaseName, connectionString, sqlCommandVariableValues, deploymentOptions) {
    const dacFxService = await utils.getDacFxService();
    if (utils.getAzdataApi()) {
        await dacFxService.savePublishProfile(profilePath, databaseName, connectionString, sqlCommandVariableValues, deploymentOptions);
    }
    else {
        await dacFxService.savePublishProfile(profilePath, databaseName, connectionString, sqlCommandVariableValues, deploymentOptions);
    }
}
function promptToSaveProfile(project, publishProfileUri) {
    return vscode.window.showSaveDialog({
        defaultUri: publishProfileUri ?? vscode.Uri.file(path.join(project.projectFolderPath, `${project.projectFileName}_1.publish.xml`)),
        saveLabel: constants.save,
        filters: {
            'Publish files': ['publish.xml'],
        }
    });
}
/**
 * Prompt to save publish profile and add to the tree
 * @param project
 * @param settings Publish settings
 * @returns
 */
async function promptForSavingProfile(project, settings) {
    const result = await vscode.window.showInformationMessage(constants.saveProfile, constants.yesString, constants.noString);
    if (result === constants.yesString) {
        let publishProfileUri;
        if (settings) {
            if (isISqlProjectPublishSettings(settings)) {
                publishProfileUri = settings.publishProfileUri;
            }
            else if (isISqlDbDeployProfile(settings)) {
                publishProfileUri = settings.deploySettings?.publishProfileUri;
            }
            else if (isIPublishToDockerSettings(settings)) {
                publishProfileUri = settings.sqlProjectPublishSettings.publishProfileUri;
            }
        }
        const filePath = await promptToSaveProfile(project, publishProfileUri);
        if (!filePath) {
            return;
        }
        const targetConnectionString = await getConnectionString(settings);
        const targetDatabaseName = getDatabaseName(settings, project.projectFileName);
        const deploymentOptions = await getDeploymentOptions(settings, project);
        const sqlCmdVariables = getSqlCmdVariables(settings);
        await savePublishProfile(filePath.fsPath, targetDatabaseName, targetConnectionString, sqlCmdVariables, deploymentOptions);
        setProfileParameters(settings, filePath);
        await project.addNoneItem(path.relative(project.projectFolderPath, filePath.fsPath));
        void vscode.commands.executeCommand(constants.refreshDataWorkspaceCommand); //refresh data workspace to load the newly added profile to the tree
    }
}
/**
 * Function to confirm the Publish to existing server workflow
 * @param settings
 * @returns true if the settings is of type ISqlProjectPublishSettings
 */
function isISqlProjectPublishSettings(settings) {
    if (settings.connectionUri) {
        return true;
    }
    return false;
}
/**
 * Function to confirm the Publish to New Azure server workflow
 * @param settings
 * @returns true if the settings is of type ISqlDbDeployProfile
 */
function isISqlDbDeployProfile(settings) {
    if (settings.deploySettings) {
        return true;
    }
    return false;
}
/**
 * Function to confirm the Publish to Docker workflow
 * @param settings
 * @returns true if the settings is of type IPublishToDockerSettings
 */
function isIPublishToDockerSettings(settings) {
    if (settings.dockerSettings) {
        return true;
    }
    return false;
}
async function getConnectionString(settings) {
    let connectionUri = '';
    let connectionString = '';
    if (settings) {
        if (isISqlProjectPublishSettings(settings)) {
            connectionUri = settings.connectionUri;
        }
        else if (isISqlDbDeployProfile(settings)) {
            connectionUri = settings.deploySettings?.connectionUri ?? '';
        }
        else if (isIPublishToDockerSettings(settings)) {
            connectionUri = settings.sqlProjectPublishSettings.connectionUri;
        }
    }
    if (connectionUri) {
        connectionString = await (await utils.getVscodeMssqlApi()).getConnectionString(connectionUri, false);
    }
    return connectionString;
}
function getDatabaseName(settings, projectName) {
    let databaseName = projectName;
    if (settings) {
        if (isISqlProjectPublishSettings(settings)) {
            databaseName = settings.databaseName;
        }
        else if (isISqlDbDeployProfile(settings)) {
            databaseName = settings.deploySettings?.databaseName ?? '';
        }
        else if (isIPublishToDockerSettings(settings)) {
            databaseName = settings.sqlProjectPublishSettings.databaseName;
        }
    }
    return databaseName;
}
async function getDeploymentOptions(settings, project) {
    let deploymentOptions;
    if (settings) {
        if (isISqlProjectPublishSettings(settings)) {
            deploymentOptions = settings.deploymentOptions;
        }
        else if (isISqlDbDeployProfile(settings)) {
            deploymentOptions = settings.deploySettings?.deploymentOptions;
        }
        else if (isIPublishToDockerSettings(settings)) {
            deploymentOptions = settings.sqlProjectPublishSettings.deploymentOptions;
        }
    }
    else {
        deploymentOptions = await utils.getDefaultPublishDeploymentOptions(project);
    }
    return deploymentOptions;
}
function getSqlCmdVariables(settings) {
    let sqlCmdVariables;
    if (settings) {
        if (isISqlProjectPublishSettings(settings)) {
            sqlCmdVariables = settings.sqlCmdVariables;
        }
        else if (isISqlDbDeployProfile(settings)) {
            sqlCmdVariables = settings.deploySettings?.sqlCmdVariables;
        }
        else if (isIPublishToDockerSettings(settings)) {
            sqlCmdVariables = settings.sqlProjectPublishSettings.sqlCmdVariables;
        }
    }
    return sqlCmdVariables;
}
function setProfileParameters(settings, profilePath) {
    if (settings) {
        if (isISqlProjectPublishSettings(settings)) {
            settings.publishProfileUri = profilePath;
        }
        else if (isISqlDbDeployProfile(settings)) {
            if (settings.deploySettings) {
                settings.deploySettings.publishProfileUri = profilePath;
            }
        }
        else if (isIPublishToDockerSettings(settings)) {
            settings.sqlProjectPublishSettings.publishProfileUri = profilePath;
        }
    }
}
//# sourceMappingURL=publishProfile.js.map