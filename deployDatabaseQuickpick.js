"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.launchDeployAppIntegrationQuickpick = launchDeployAppIntegrationQuickpick;
exports.launchCreateAzureServerQuickPick = launchCreateAzureServerQuickPick;
const vscode = require("vscode");
const constants = require("../common/constants");
const utils = require("../common/utils");
const uiUtils = require("./utils");
const path = require("path");
const fse = require("fs-extra");
const deployProfile_1 = require("../models/deploy/deployProfile");
const publishDatabaseQuickpick_1 = require("./publishDatabaseQuickpick");
/**
 * Create flow for Deploying a database using only VS Code-native APIs such as QuickPick
 */
async function launchDeployAppIntegrationQuickpick(project) {
    let envVarName = '';
    const integrateWithAzureFunctions = true; //TODO: get value from settings or quickpick
    //TODO: find a better way to find if AF or local settings is in the project
    //
    const localSettings = path.join(project.projectFolderPath, constants.azureFunctionLocalSettingsFileName);
    const settingExist = await fse.pathExists(localSettings);
    if (integrateWithAzureFunctions && settingExist) {
        // Ask user to update app settings or not
        //
        let choices = {};
        let options = {
            placeHolder: constants.appSettingPrompt
        };
        choices[constants.yesString] = true;
        choices[constants.noString] = false;
        let result = await vscode.window.showQuickPick(Object.keys(choices).map(c => {
            return {
                label: c
            };
        }), options);
        // Return when user hits escape
        if (!result) {
            return undefined;
        }
        if (result !== undefined && choices[result.label] || false) {
            envVarName = await vscode.window.showInputBox({
                title: constants.enterConnectionStringEnvName,
                ignoreFocusOut: true,
                value: constants.defaultConnectionStringEnvVarName,
                validateInput: input => utils.isEmptyString(input) ? constants.valueCannotBeEmpty : undefined,
                placeHolder: constants.enterConnectionStringEnvNameDescription
            });
            // Return when user hits escape
            if (!envVarName) {
                return undefined;
            }
        }
    }
    return {
        envVariableName: envVarName,
        appSettingFile: settingExist ? localSettings : undefined,
        appSettingType: settingExist ? deployProfile_1.AppSettingType.AzureFunction : deployProfile_1.AppSettingType.None
    };
}
async function launchCreateAzureServerQuickPick(project, azureSqlClient) {
    const name = uiUtils.getPublishServerName(project.getProjectTargetVersion());
    const accounts = await azureSqlClient.getAccounts();
    const accountOptions = accounts.map(x => x.displayInfo?.displayName || '');
    accountOptions.unshift(constants.azureAddAccount);
    let account;
    let accountOption = await vscode.window.showQuickPick(accountOptions, { title: constants.azureAccounts, ignoreFocusOut: true });
    // Return when user hits escape
    if (!accountOption) {
        return undefined;
    }
    if (accountOption === constants.azureAddAccount) {
        account = await azureSqlClient.getAccount();
    }
    else {
        account = accounts.find(x => x.displayInfo.displayName === accountOption);
    }
    if (!account) {
        return undefined;
    }
    const sessions = await azureSqlClient.getSessions(account);
    const subscriptionName = await vscode.window.showQuickPick(sessions.map(x => x.subscription.displayName || ''), { title: constants.azureSubscription, ignoreFocusOut: true });
    // Return when user hits escape
    if (!subscriptionName) {
        return undefined;
    }
    const session = sessions.find(x => x.subscription.displayName === subscriptionName);
    if (!session?.subscription?.subscriptionId) {
        return undefined;
    }
    const resourceGroups = await azureSqlClient.getResourceGroups(session);
    const resourceGroupName = await vscode.window.showQuickPick(resourceGroups.map(x => x.name || ''), { title: constants.resourceGroup, ignoreFocusOut: true });
    // Return when user hits escape
    if (!resourceGroupName) {
        return undefined;
    }
    const resourceGroup = resourceGroups.find(x => x.name === resourceGroupName);
    // Return resource group is invalid
    if (!resourceGroup) {
        return undefined;
    }
    let locations = await azureSqlClient.getLocations(session);
    if (resourceGroup.location) {
        const defaultLocation = locations.find(x => x.name === resourceGroup.location);
        if (defaultLocation) {
            locations = locations.filter(x => x.name !== defaultLocation.name);
            locations.unshift(defaultLocation);
        }
    }
    let locationName = await vscode.window.showQuickPick(locations.map(x => x.name || ''), { title: constants.azureLocation, ignoreFocusOut: true, placeHolder: resourceGroup?.location });
    // Return when user hits escape
    if (!locationName) {
        return undefined;
    }
    let serverName = '';
    serverName = await vscode.window.showInputBox({
        title: constants.azureServerName,
        ignoreFocusOut: true,
        value: serverName,
        password: false
    });
    // Return when user hits escape
    if (!serverName) {
        return undefined;
    }
    let user = '';
    user = await vscode.window.showInputBox({
        title: constants.enterUser(name),
        ignoreFocusOut: true,
        value: user,
        password: false
    });
    // Return when user hits escape
    if (!user) {
        return undefined;
    }
    let password = '';
    password = await vscode.window.showInputBox({
        title: constants.enterPassword(name),
        ignoreFocusOut: true,
        value: password,
        validateInput: input => !utils.isValidSQLPassword(input) ? constants.invalidSQLPasswordMessage(name) : undefined,
        password: true
    });
    // Return when user hits escape
    if (!password) {
        return undefined;
    }
    let confirmPassword = '';
    confirmPassword = await vscode.window.showInputBox({
        title: constants.confirmPassword(name),
        ignoreFocusOut: true,
        value: confirmPassword,
        validateInput: input => input !== password ? constants.passwordNotMatch(name) : undefined,
        password: true
    });
    // Return when user hits escape
    if (!confirmPassword) {
        return undefined;
    }
    let settings = await (0, publishDatabaseQuickpick_1.getPublishDatabaseSettings)(project, false);
    return {
        // TODO add tenant
        deploySettings: settings,
        sqlDbSetting: {
            tenantId: session.tenantId,
            accountId: session.account.key.id,
            serverName: serverName,
            userName: user,
            password: password,
            port: 1433,
            dbName: '',
            session: session,
            resourceGroupName: resourceGroup.name || '',
            location: locationName
        }
    };
}
//# sourceMappingURL=deployDatabaseQuickpick.js.map