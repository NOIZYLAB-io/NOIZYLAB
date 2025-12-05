"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getPublishToDockerSettings = getPublishToDockerSettings;
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
const vscode = require("vscode");
const constants = require("../common/constants");
const utils = require("../common/utils");
const uiUtils = require("./utils");
const publishDatabaseQuickpick_1 = require("./publishDatabaseQuickpick");
/**
 * Gets the settings for publishing a database to docker container using only VS Code-native APIs such as QuickPick
 */
async function getPublishToDockerSettings(project) {
    const target = project.getProjectTargetVersion();
    const name = uiUtils.getPublishServerName(target);
    // Deploy to docker selected
    let portNumber = await vscode.window.showInputBox({
        title: constants.enterPortNumber(name),
        ignoreFocusOut: true,
        value: constants.defaultPortNumber,
        validateInput: input => !utils.validateSqlServerPortNumber(input) ? constants.portMustBeNumber : undefined
    });
    // Return when user hits escape
    if (!portNumber) {
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
    const imageInfo = uiUtils.getDockerBaseImage(target);
    if (!imageInfo) {
        return undefined;
    }
    const eulaAccepted = await launchEulaQuickPick(imageInfo);
    if (!eulaAccepted) {
        return undefined;
    }
    let imageTags = await uiUtils.getImageTags(imageInfo, target);
    let imageTagsItems = imageTags.map(tag => { return { label: tag }; });
    if (imageInfo.defaultTag) {
        // move the default to be the first one in the list
        const defaultIndex = imageTagsItems.findIndex(i => i.label === imageInfo.defaultTag);
        if (defaultIndex > -1) {
            imageTagsItems.splice(defaultIndex, 1);
        }
        // add default next to the default value
        imageTagsItems.unshift({ label: imageInfo.defaultTag, description: constants.defaultQuickPickItem });
    }
    const imageTag = await vscode.window.showQuickPick(imageTagsItems, { title: constants.selectImageTag(name), ignoreFocusOut: true });
    if (!imageTag) {
        return undefined;
    }
    // Add the image tag if it's not the latest
    let imageName = imageInfo.name;
    if (imageTag && imageTag.label !== constants.dockerImageDefaultTag) {
        imageName = `${imageName}:${imageTag.label}`;
    }
    const dockerSettings = {
        serverName: constants.defaultLocalServerName,
        userName: constants.defaultLocalServerAdminName,
        dbName: project.projectFileName,
        password: password,
        port: +portNumber,
        dockerBaseImage: imageName,
        dockerBaseImageEula: imageInfo.agreementInfo.link.url
    };
    let deploySettings = await (0, publishDatabaseQuickpick_1.getPublishDatabaseSettings)(project, false);
    // Return when user hits escape
    if (!deploySettings) {
        return undefined;
    }
    // Server name should be set to localhost
    deploySettings.serverName = dockerSettings.serverName;
    // Get the database name from deploy settings
    dockerSettings.dbName = deploySettings.databaseName;
    return {
        dockerSettings,
        sqlProjectPublishSettings: deploySettings,
    };
}
async function launchEulaQuickPick(imageInfo) {
    let eulaAccepted = false;
    const agreementInfo = imageInfo?.agreementInfo;
    if (agreementInfo) {
        const openEulaButton = {
            iconPath: new vscode.ThemeIcon('link-external'),
            tooltip: constants.openEulaString
        };
        const quickPick = vscode.window.createQuickPick();
        quickPick.items = [{ label: constants.yesString },
            { label: constants.noString }];
        quickPick.title = uiUtils.getAgreementDisplayText(agreementInfo);
        quickPick.ignoreFocusOut = true;
        quickPick.buttons = [openEulaButton];
        const disposables = [];
        try {
            const eulaAcceptedPromise = new Promise((resolve) => {
                disposables.push(quickPick.onDidHide(() => {
                    resolve(false);
                }), quickPick.onDidTriggerButton(async () => {
                    await vscode.env.openExternal(vscode.Uri.parse(agreementInfo.link.url));
                }), quickPick.onDidChangeSelection((item) => {
                    resolve(item[0].label === constants.yesString);
                }));
            });
            quickPick.show();
            eulaAccepted = await eulaAcceptedPromise;
            quickPick.hide();
        }
        finally {
            disposables.forEach(d => d.dispose());
        }
        return eulaAccepted;
    }
    return false;
}
//# sourceMappingURL=publishToDockerQuickpick.js.map