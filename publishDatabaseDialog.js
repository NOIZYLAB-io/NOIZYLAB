"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.PublishDatabaseDialog = void 0;
exports.promptForPublishProfile = promptForPublishProfile;
const vscode = require("vscode");
const constants = require("../common/constants");
const utils = require("../common/utils");
const uiUtils = require("./utils");
const path = require("path");
const iconHelper_1 = require("../common/iconHelper");
const uiConstants_1 = require("../common/uiConstants");
const utils_1 = require("./utils");
const telemetry_1 = require("../common/telemetry");
const promise_1 = require("../common/promise");
const publishOptionsDialog_1 = require("./publishOptionsDialog");
const publishProfile_1 = require("../models/publishProfile/publishProfile");
class PublishDatabaseDialog {
    project;
    dialog;
    publishTab;
    targetConnectionTextBox;
    dataSourcesDropDown;
    targetDatabaseDropDown;
    targetDatabaseTextBox;
    selectConnectionButton;
    existingServerRadioButton;
    dockerServerRadioButton;
    eulaCheckBox;
    sqlCmdVariablesTable;
    sqlCmdVariablesFormComponentGroup;
    revertSqlCmdVarsButton;
    loadProfileTextBox;
    formBuilder;
    connectionRow;
    databaseRow;
    localDbSection;
    imageTagDropDown;
    serverAdminPasswordTextBox;
    serverConfigAdminPasswordTextBox;
    serverPortTextBox;
    existingServerSelected = true;
    connectionId;
    connectionIsDataSource;
    sqlCmdVars;
    deploymentOptions;
    serverName;
    optionsButton;
    publishOptionsDialog;
    publishOptionsModified = false;
    publishProfileUri;
    completionPromise = new promise_1.Deferred();
    toDispose = [];
    publish;
    publishToContainer;
    generateScript;
    readPublishProfile;
    savePublishProfile;
    constructor(project) {
        this.project = project;
        this.dialog = utils.getAzdataApi().window.createModelViewDialog(constants.publishDialogName, 'sqlProjectPublishDialog');
        this.toDispose.push(this.dialog.onClosed(_ => this.completionPromise.resolve()));
        this.publishTab = utils.getAzdataApi().window.createTab(constants.publishDialogName);
    }
    openDialog() {
        this.initializeDialog();
        this.dialog.okButton.label = constants.publish;
        this.dialog.okButton.enabled = false;
        this.toDispose.push(this.dialog.okButton.onClick(async () => await this.publishClick()));
        this.dialog.cancelButton.label = constants.cancelButtonText;
        let generateScriptButton = utils.getAzdataApi().window.createButton(constants.generateScriptButtonText);
        this.toDispose.push(generateScriptButton.onClick(async () => await this.generateScriptClick()));
        generateScriptButton.enabled = false;
        this.dialog.customButtons = [];
        this.dialog.customButtons.push(generateScriptButton);
        utils.getAzdataApi().window.openDialog(this.dialog);
    }
    set publishToExistingServer(v) {
        this.existingServerSelected = v;
    }
    waitForClose() {
        return this.completionPromise.promise;
    }
    dispose() {
        this.toDispose.forEach(disposable => disposable.dispose());
    }
    initializeDialog() {
        this.initializePublishTab();
        this.dialog.content = [this.publishTab];
    }
    initializePublishTab() {
        this.publishTab.registerContent(async (view) => {
            const flexRadioButtonsModel = this.createPublishTypeRadioButtons(view);
            await this.createLocalDbInfoRow(view);
            this.sqlCmdVariablesTable = this.createSqlCmdTable(view);
            this.revertSqlCmdVarsButton = this.createRevertSqlCmdVarsButton(view);
            this.sqlCmdVariablesFormComponentGroup = {
                components: [
                    {
                        title: '',
                        component: this.revertSqlCmdVarsButton
                    },
                    {
                        title: '',
                        component: this.sqlCmdVariablesTable
                    }
                ],
                title: constants.sqlCmdVariables
            };
            // Get the default deployment option and set
            const options = await this.getDefaultDeploymentOptions();
            this.setDeploymentOptions(options);
            const profileRow = this.createProfileSection(view);
            this.connectionRow = this.createConnectionRow(view);
            this.databaseRow = this.createDatabaseRow(view);
            const displayOptionsButton = this.createOptionsButton(view);
            const horizontalFormSection = view.modelBuilder.flexContainer().withLayout({ flexFlow: 'column' }).component();
            horizontalFormSection.addItems([this.databaseRow]);
            this.formBuilder = view.modelBuilder.formContainer()
                .withFormItems([
                {
                    title: '',
                    components: [
                        {
                            component: flexRadioButtonsModel,
                            title: ''
                        },
                        {
                            component: profileRow,
                            title: constants.profile
                        },
                        {
                            component: this.connectionRow,
                            title: ''
                        },
                        {
                            component: horizontalFormSection,
                            title: ''
                        },
                        /* TODO : enable using this when data source creation is enabled
                        {
                            title: constants.selectConnectionRadioButtonsTitle,
                            component: selectConnectionRadioButtons
                        },*/
                        {
                            component: displayOptionsButton,
                            title: ''
                        }
                    ]
                }
            ], {
                horizontal: false,
                titleFontSize: uiConstants_1.cssStyles.titleFontSize
            })
                .withLayout({
                width: '100%'
            });
            // add SQLCMD variables table if the project has any
            if (this.project.sqlCmdVariables.size > 0) {
                this.formBuilder.addFormItem(this.sqlCmdVariablesFormComponentGroup);
            }
            let formModel = this.formBuilder.component();
            await view.initializeModel(formModel);
        });
    }
    async getConnectionUri() {
        try {
            // if target connection is a data source, have to check if already connected or if connection dialog needs to be opened
            let connId;
            if (this.connectionIsDataSource) {
                const dataSource = this.dataSourcesDropDown.value.dataSource;
                const connProfile = dataSource.getConnectionProfile();
                if (dataSource.integratedSecurity) {
                    const connResult = await utils.getAzdataApi().connection.connect(connProfile, false, false);
                    utils.throwIfNotConnected(connResult);
                    connId = connResult.connectionId;
                }
                else {
                    connId = (await utils.getAzdataApi().connection.openConnectionDialog(undefined, connProfile, {
                        saveConnection: false,
                        showDashboard: false,
                        showConnectionDialogOnError: true,
                        showFirewallRuleOnError: true
                    })).connectionId;
                }
            }
            else {
                if (!this.connectionId) {
                    throw new Error('Connection not defined.');
                }
                connId = this.connectionId;
            }
            return await utils.getAzdataApi().connection.getUriForConnection(connId);
        }
        catch (err) {
            throw new Error(constants.unableToCreatePublishConnection + ': ' + utils.getErrorMessage(err));
        }
    }
    async publishClick() {
        if (this.existingServerSelected) {
            const settings = {
                databaseName: this.targetDatabaseName,
                serverName: this.getServerName(),
                connectionUri: await this.getConnectionUri(),
                sqlCmdVariables: this.getSqlCmdVariablesForPublish(),
                deploymentOptions: await this.getDeploymentOptions(),
                publishProfileUri: this.publishProfileUri
            };
            utils.getAzdataApi().window.closeDialog(this.dialog);
            await this.publish(this.project, settings);
        }
        else {
            const imageInfo = (0, utils_1.getDockerBaseImage)(this.project.getProjectTargetVersion());
            const imageName = imageInfo?.name;
            const imageTag = this.imageTagDropDown?.value;
            let dockerBaseImage = imageName;
            // Add the image tag if it's not the latest
            if (imageTag && imageTag !== constants.dockerImageDefaultTag) {
                dockerBaseImage = `${imageName}:${imageTag}`;
            }
            const settings = {
                dockerSettings: {
                    dbName: this.targetDatabaseName,
                    dockerBaseImage: dockerBaseImage,
                    dockerBaseImageEula: imageInfo?.agreementInfo?.link?.url || '',
                    password: this.serverAdminPasswordTextBox?.value || '',
                    port: +(this.serverPortTextBox?.value || constants.defaultPortNumber),
                    serverName: constants.defaultLocalServerName,
                    userName: constants.defaultLocalServerAdminName
                },
                sqlProjectPublishSettings: {
                    databaseName: this.targetDatabaseName,
                    serverName: constants.defaultLocalServerName,
                    connectionUri: '',
                    sqlCmdVariables: this.getSqlCmdVariablesForPublish(),
                    deploymentOptions: await this.getDeploymentOptions(),
                    publishProfileUri: this.publishProfileUri
                }
            };
            utils.getAzdataApi().window.closeDialog(this.dialog);
            await this.publishToContainer(this.project, settings);
        }
        this.dispose();
    }
    async generateScriptClick() {
        telemetry_1.TelemetryReporter.sendActionEvent(telemetry_1.TelemetryViews.SqlProjectPublishDialog, telemetry_1.TelemetryActions.generateScriptClicked);
        const sqlCmdVars = this.getSqlCmdVariablesForPublish();
        const settings = {
            databaseName: this.targetDatabaseName,
            serverName: this.getServerName(),
            connectionUri: await this.getConnectionUri(),
            sqlCmdVariables: sqlCmdVars,
            deploymentOptions: await this.getDeploymentOptions(),
            publishProfileUri: this.publishProfileUri
        };
        utils.getAzdataApi().window.closeDialog(this.dialog);
        await this.generateScript?.(this.project, settings);
        this.dispose();
    }
    async getDeploymentOptions() {
        if (!this.deploymentOptions) {
            // We only use the dialog in ADS context currently so safe to cast to the mssql DeploymentOptions here
            this.deploymentOptions = await utils.getDefaultPublishDeploymentOptions(this.project);
        }
        return this.deploymentOptions;
    }
    getSqlCmdVariablesForPublish() {
        // get SQLCMD variables from table
        let sqlCmdVariables = this.sqlCmdVars ?? new Map();
        return sqlCmdVariables;
    }
    get targetDatabaseName() {
        if (this.existingServerSelected) {
            return this.targetDatabaseDropDown?.value ?? '';
        }
        else {
            return this.targetDatabaseTextBox?.value || '';
        }
    }
    set targetDatabaseName(value) {
        this.targetDatabaseDropDown.values = [];
        this.targetDatabaseDropDown.values?.push(value);
        this.targetDatabaseDropDown.value = value;
        if (this.targetDatabaseTextBox) {
            this.targetDatabaseTextBox.value = value;
        }
    }
    getDefaultDatabaseName() {
        return this.project.projectFileName;
    }
    getServerName() {
        return this.serverName;
    }
    createPublishTypeRadioButtons(view) {
        const name = (0, utils_1.getPublishServerName)(this.project.getProjectTargetVersion());
        const publishToLabel = view.modelBuilder.text().withProps({
            value: constants.publishTo,
            width: uiConstants_1.cssStyles.publishDialogLabelWidth
        }).component();
        this.existingServerRadioButton = view.modelBuilder.radioButton()
            .withProps({
            name: 'publishType',
            label: constants.publishToExistingServer(name)
        }).component();
        this.existingServerRadioButton.checked = true;
        this.existingServerRadioButton.onDidChangeCheckedState((checked) => {
            this.onPublishTypeChange(checked, view);
        });
        this.dockerServerRadioButton = view.modelBuilder.radioButton()
            .withProps({
            name: 'publishType',
            label: name === constants.AzureSqlServerName ? constants.publishToDockerContainerPreview(name) : constants.publishToDockerContainer(name)
        }).component();
        this.dockerServerRadioButton.onDidChangeCheckedState((checked) => {
            this.onPublishTypeChange(!checked, view);
        });
        const radioButtonContainer = view.modelBuilder.flexContainer()
            .withLayout({ flexFlow: 'column' })
            .withItems([this.existingServerRadioButton, this.dockerServerRadioButton])
            .withProps({ ariaRole: 'radiogroup', ariaLabel: constants.publishTo })
            .component();
        let flexRadioButtonsModel = view.modelBuilder.flexContainer()
            .withLayout({ flexFlow: 'row', alignItems: 'baseline' })
            .withItems([publishToLabel, radioButtonContainer], { CSSStyles: { flex: '0 0 auto', 'margin-right': '10px' } })
            .component();
        return flexRadioButtonsModel;
    }
    onPublishTypeChange(existingServer, view) {
        this.existingServerSelected = existingServer;
        this.createDatabaseRow(view);
        this.tryEnableGenerateScriptAndPublishButtons();
        if (existingServer) {
            if (this.localDbSection) {
                this.formBuilder.removeFormItem({
                    title: '',
                    component: this.localDbSection
                });
            }
            if (this.connectionRow) {
                this.formBuilder.insertFormItem({
                    title: '',
                    component: this.connectionRow
                }, 3);
            }
        }
        else {
            if (this.connectionRow) {
                this.formBuilder.removeFormItem({
                    title: '',
                    component: this.connectionRow
                });
            }
            if (this.localDbSection) {
                this.formBuilder.insertFormItem({
                    title: '',
                    component: this.localDbSection
                }, 2);
            }
        }
    }
    createTargetConnectionComponent(view) {
        this.targetConnectionTextBox = view.modelBuilder.inputBox().withProps({
            value: '',
            ariaLabel: constants.targetConnectionLabel,
            placeHolder: constants.selectConnection,
            width: uiConstants_1.cssStyles.publishDialogTextboxWidth,
            enabled: false
        }).component();
        this.targetConnectionTextBox.onTextChanged(() => {
            this.tryEnableGenerateScriptAndPublishButtons();
        });
        return this.targetConnectionTextBox;
    }
    createProfileSection(view) {
        const selectProfileButton = this.createSelectProfileButton(view);
        const saveProfileAsButton = this.createSaveProfileAsButton(view);
        this.loadProfileTextBox = view.modelBuilder.inputBox().withProps({
            placeHolder: constants.loadProfilePlaceholderText,
            ariaLabel: constants.profile,
            width: '200px',
            enabled: false
        }).component();
        const buttonsList = view.modelBuilder.flexContainer().withItems([selectProfileButton, saveProfileAsButton], { flex: '0 0 auto', CSSStyles: { 'margin-right': '5px', 'text-align': 'justify' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        const profileRow = view.modelBuilder.flexContainer().withItems([this.loadProfileTextBox, buttonsList], { flex: '0 0 auto', CSSStyles: { 'margin-right': '15px', 'text-align': 'justify' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        return profileRow;
    }
    createConnectionRow(view) {
        this.targetConnectionTextBox = this.createTargetConnectionComponent(view);
        const selectConnectionButton = this.createSelectConnectionButton(view);
        const serverLabel = view.modelBuilder.text().withProps({
            value: constants.server,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.publishDialogLabelWidth
        }).component();
        const connectionRow = view.modelBuilder.flexContainer().withItems([serverLabel, this.targetConnectionTextBox], { flex: '0 0 auto', CSSStyles: { 'margin': '-8px 10px -15px 0' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        connectionRow.insertItem(selectConnectionButton, 2, { CSSStyles: { 'margin-right': '0px' } });
        return connectionRow;
    }
    async createLocalDbInfoRow(view) {
        const name = (0, utils_1.getPublishServerName)(this.project.getProjectTargetVersion());
        this.serverPortTextBox = view.modelBuilder.inputBox().withProps({
            value: constants.defaultPortNumber,
            ariaLabel: constants.serverPortNumber(name),
            placeHolder: constants.serverPortNumber(name),
            width: uiConstants_1.cssStyles.publishDialogTextboxWidth,
            enabled: true,
            inputType: 'number',
            validationErrorMessage: constants.portMustBeNumber,
            required: true
        }).withValidation(component => utils.validateSqlServerPortNumber(component.value)).component();
        this.serverPortTextBox.onTextChanged(() => {
            this.tryEnableGenerateScriptAndPublishButtons();
        });
        const serverPortRow = this.createFormRow(view, constants.serverPortNumber(name), this.serverPortTextBox);
        this.serverAdminPasswordTextBox = view.modelBuilder.inputBox().withProps({
            value: '',
            ariaLabel: constants.serverPassword(name),
            placeHolder: constants.serverPassword(name),
            width: uiConstants_1.cssStyles.publishDialogTextboxWidth,
            enabled: true,
            inputType: 'password',
            validationErrorMessage: constants.invalidSQLPasswordMessage(name),
            required: true
        }).withValidation(component => !utils.isEmptyString(component.value) && utils.isValidSQLPassword(component.value || '')).component();
        const serverPasswordRow = this.createFormRow(view, constants.serverPassword(name), this.serverAdminPasswordTextBox);
        this.serverConfigAdminPasswordTextBox = view.modelBuilder.inputBox().withProps({
            value: '',
            ariaLabel: constants.confirmServerPassword(name),
            placeHolder: constants.confirmServerPassword(name),
            width: uiConstants_1.cssStyles.publishDialogTextboxWidth,
            enabled: true,
            inputType: 'password',
            validationErrorMessage: constants.passwordNotMatch(name),
            required: true
        }).withValidation(component => component.value === this.serverAdminPasswordTextBox?.value).component();
        this.serverAdminPasswordTextBox.onTextChanged(() => {
            this.tryEnableGenerateScriptAndPublishButtons();
            if (this.serverConfigAdminPasswordTextBox) {
                this.serverConfigAdminPasswordTextBox.value = '';
            }
        });
        this.serverConfigAdminPasswordTextBox.onTextChanged(() => {
            this.tryEnableGenerateScriptAndPublishButtons();
        });
        const serverConfirmPasswordRow = this.createFormRow(view, constants.confirmServerPassword(name), this.serverConfigAdminPasswordTextBox);
        const imageInfo = (0, utils_1.getDockerBaseImage)(this.project.getProjectTargetVersion());
        const imageTags = await uiUtils.getImageTags(imageInfo, this.project.getProjectTargetVersion(), true);
        this.imageTagDropDown = view.modelBuilder.dropDown().withProps({
            values: imageTags,
            value: imageTags[0],
            ariaLabel: constants.imageTag,
            width: uiConstants_1.cssStyles.publishDialogTextboxWidth,
            enabled: true,
            editable: true,
            required: true,
            fireOnTextChange: true
        }).component();
        this.imageTagDropDown.onValueChanged(() => {
            this.tryEnableGenerateScriptAndPublishButtons();
        });
        const agreementInfo = imageInfo.agreementInfo;
        const imageTagDropDownRow = this.createFormRow(view, constants.imageTag, this.imageTagDropDown);
        this.eulaCheckBox = view.modelBuilder.checkBox().withProps({
            ariaLabel: (0, utils_1.getAgreementDisplayText)(agreementInfo),
            required: true
        }).component();
        this.eulaCheckBox.onChanged(() => {
            this.tryEnableGenerateScriptAndPublishButtons();
        });
        const eulaRow = view.modelBuilder.flexContainer().withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        this.localDbSection = view.modelBuilder.flexContainer().withLayout({ flexFlow: 'column' }).component();
        this.localDbSection.addItems([serverPortRow, serverPasswordRow, serverConfirmPasswordRow, imageTagDropDownRow, eulaRow]);
        this.eulaCheckBox.checked = false;
        if (imageInfo?.agreementInfo.link) {
            const text = view.modelBuilder.text().withProps({
                value: constants.eulaAgreementTemplate,
                links: [imageInfo.agreementInfo.link],
                requiredIndicator: true
            }).component();
            if (eulaRow && this.eulaCheckBox) {
                eulaRow?.clearItems();
                eulaRow?.addItems([this.eulaCheckBox, text], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px' } });
            }
        }
        return this.localDbSection;
    }
    createFormRow(view, label, component) {
        const labelComponent = view.modelBuilder.text().withProps({
            value: label,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.publishDialogLabelWidth
        }).component();
        return view.modelBuilder.flexContainer().withItems([labelComponent, component], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
    }
    createDatabaseRow(view) {
        let databaseComponent;
        if (!this.existingServerSelected) {
            if (this.targetDatabaseTextBox === undefined) {
                this.targetDatabaseTextBox = view.modelBuilder.inputBox().withProps({
                    ariaLabel: constants.databaseNameLabel,
                    required: true,
                    width: uiConstants_1.cssStyles.publishDialogDropdownWidth,
                    value: this.getDefaultDatabaseName()
                }).component();
            }
            databaseComponent = this.targetDatabaseTextBox;
        }
        else {
            if (this.targetDatabaseDropDown === undefined) {
                this.targetDatabaseDropDown = view.modelBuilder.dropDown().withProps({
                    values: [this.getDefaultDatabaseName()],
                    value: this.getDefaultDatabaseName(),
                    ariaLabel: constants.databaseNameLabel,
                    required: true,
                    width: uiConstants_1.cssStyles.publishDialogDropdownWidth,
                    editable: true,
                    fireOnTextChange: true
                }).component();
                this.targetDatabaseDropDown.onValueChanged(() => {
                    this.tryEnableGenerateScriptAndPublishButtons();
                });
            }
            databaseComponent = this.targetDatabaseDropDown;
        }
        const databaseLabel = view.modelBuilder.text().withProps({
            value: constants.databaseNameLabel,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.publishDialogLabelWidth
        }).component();
        const itemLayout = { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px' } };
        if (this.databaseRow === undefined) {
            this.databaseRow = view.modelBuilder.flexContainer().withItems([databaseLabel, databaseComponent], itemLayout).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        }
        else {
            this.databaseRow.clearItems();
            this.databaseRow.addItems([databaseLabel, databaseComponent], itemLayout);
        }
        return this.databaseRow;
    }
    createSqlCmdTable(view) {
        this.sqlCmdVars = this.project.sqlCmdVariables;
        const table = view.modelBuilder.declarativeTable().withProps({
            ariaLabel: constants.sqlCmdVariables,
            dataValues: this.convertSqlCmdVarsToTableFormat(this.sqlCmdVars),
            columns: [
                {
                    displayName: constants.sqlCmdVariableColumn,
                    valueType: utils.getAzdataApi().DeclarativeDataType.string,
                    width: '50%',
                    isReadOnly: true,
                    headerCssStyles: uiConstants_1.cssStyles.tableHeader,
                    rowCssStyles: uiConstants_1.cssStyles.tableRow
                },
                {
                    displayName: constants.sqlCmdValueColumn,
                    valueType: utils.getAzdataApi().DeclarativeDataType.string,
                    width: '50%',
                    isReadOnly: false,
                    headerCssStyles: uiConstants_1.cssStyles.tableHeader,
                    rowCssStyles: uiConstants_1.cssStyles.tableRow
                }
            ],
            width: '420px'
        }).component();
        table.onDataChanged(() => {
            this.sqlCmdVars = new Map();
            table.dataValues?.forEach((row) => {
                this.sqlCmdVars?.set(row[0].value, row[1].value);
            });
            this.updateRevertSqlCmdVarsButtonState();
            this.tryEnableGenerateScriptAndPublishButtons();
        });
        return table;
    }
    createRevertSqlCmdVarsButton(view) {
        let loadSqlCmdVarsButton = view.modelBuilder.button().withProps({
            label: constants.revertSqlCmdVarsButtonTitle,
            title: constants.revertSqlCmdVarsButtonTitle,
            ariaLabel: constants.revertSqlCmdVarsButtonTitle,
            width: '210px',
            iconPath: iconHelper_1.IconPathHelper.refresh,
            height: '18px',
            CSSStyles: { 'font-size': '13px' },
            enabled: false // start disabled because no SQLCMD variable values have been edited yet
        }).component();
        loadSqlCmdVarsButton.onDidClick(async () => {
            for (const key of this.sqlCmdVars.keys()) {
                this.sqlCmdVars.set(key, this.getDefaultSqlCmdValue(key));
            }
            const data = this.convertSqlCmdVarsToTableFormat(this.sqlCmdVars);
            await this.sqlCmdVariablesTable.updateProperties({
                dataValues: data
            });
            this.updateRevertSqlCmdVarsButtonState();
            this.tryEnableGenerateScriptAndPublishButtons();
        });
        return loadSqlCmdVarsButton;
    }
    /**
     * Gets the default value of a SQLCMD variable for a project
     * @param varName
     * @returns value defined in the sqlproj file, or blank string if not defined
     */
    getDefaultSqlCmdValue(varName) {
        return this.project.sqlCmdVariables.get(varName) ?? '';
    }
    createSelectConnectionButton(view) {
        this.selectConnectionButton = view.modelBuilder.button().withProps({
            ariaLabel: constants.selectConnection,
            title: constants.selectConnection,
            iconPath: iconHelper_1.IconPathHelper.selectConnection,
            height: '16px',
            width: '16px'
        }).component();
        this.selectConnectionButton.onDidClick(async () => {
            let connection = await utils.getAzdataApi().connection.openConnectionDialog(undefined, undefined, {
                saveConnection: false,
                showDashboard: false,
                showConnectionDialogOnError: true,
                showFirewallRuleOnError: true
            });
            this.connectionId = connection.connectionId;
            this.serverName = connection.options['server'];
            let connectionTextboxValue = (0, utils_1.getConnectionName)(connection);
            await this.updateConnectionComponents(connectionTextboxValue, this.connectionId, connection.options.database);
        });
        return this.selectConnectionButton;
    }
    async updateConnectionComponents(connectionTextboxValue, connectionId, database) {
        this.targetConnectionTextBox.value = connectionTextboxValue;
        await this.targetConnectionTextBox.updateProperty('title', connectionTextboxValue);
        if (database && database !== constants.master) {
            this.targetDatabaseName = database;
        }
        // populate database dropdown with the databases for this connection
        if (connectionId) {
            const databaseValues = (await utils.getAzdataApi().connection.listDatabases(connectionId))
                // filter out system dbs
                .filter(db => !constants.systemDbs.includes(db));
            this.targetDatabaseDropDown.values = databaseValues;
            // change icon to the one without a plus sign
            this.selectConnectionButton.iconPath = iconHelper_1.IconPathHelper.connect;
        }
    }
    createSelectProfileButton(view) {
        let loadProfileButton = view.modelBuilder.button().withProps({
            label: constants.selectProfile,
            title: constants.selectProfile,
            ariaLabel: constants.selectProfile,
            width: '90px',
            height: '25px',
            secondary: true,
        }).component();
        loadProfileButton.onDidClick(async () => {
            const fileUris = await promptForPublishProfile(this.project.projectFolderPath);
            if (!fileUris || fileUris.length === 0) {
                return;
            }
            if (this.readPublishProfile) {
                const result = await this.readPublishProfile(fileUris[0]);
                // clear out old database dropdown values. They'll get populated later if there was a connection specified in the profile
                this.targetDatabaseName = '';
                this.connectionId = result.connectionId;
                this.serverName = result.serverName;
                await this.updateConnectionComponents(result.connection, this.connectionId, result.databaseName);
                // set options coming from the publish profiles to deployment options
                this.setDeploymentOptions(result.options);
                if (result.sqlCmdVariables.size) {
                    // add SQLCMD Variables table if it wasn't there before and the profile had sqlcmd variables
                    if (this.project.sqlCmdVariables.size === 0 && this.sqlCmdVars?.size === 0) {
                        this.formBuilder?.addFormItem(this.sqlCmdVariablesFormComponentGroup);
                    }
                }
                else if (this.project.sqlCmdVariables.size === 0) {
                    // remove the table if there are no SQLCMD variables in the project and loaded profile
                    this.formBuilder?.removeFormItem(this.sqlCmdVariablesFormComponentGroup);
                }
                for (let key of result.sqlCmdVariables.keys()) {
                    this.sqlCmdVars?.set(key, result.sqlCmdVariables.get(key));
                }
                this.updateRevertSqlCmdVarsButtonState();
                this.deploymentOptions = result.options;
                const data = this.convertSqlCmdVarsToTableFormat(this.getSqlCmdVariablesForPublish());
                await this.sqlCmdVariablesTable.updateProperties({
                    dataValues: data
                });
                // show file path in text box and hover text
                this.loadProfileTextBox.value = fileUris[0].fsPath;
                await this.loadProfileTextBox.updateProperty('title', fileUris[0].fsPath);
                this.publishProfileUri = fileUris[0];
            }
        });
        return loadProfileButton;
    }
    createSaveProfileAsButton(view) {
        let saveProfileAsButton = view.modelBuilder.button().withProps({
            label: constants.saveProfileAsButtonText,
            title: constants.saveProfileAsButtonText,
            ariaLabel: constants.saveProfileAsButtonText,
            width: uiConstants_1.cssStyles.PublishingOptionsButtonWidth,
            height: '25px',
            secondary: true
        }).component();
        saveProfileAsButton.onDidClick(async () => {
            const filePath = await (0, publishProfile_1.promptToSaveProfile)(this.project, this.publishProfileUri);
            if (!filePath) {
                return;
            }
            if (this.savePublishProfile) {
                const targetConnectionString = this.connectionId ? await utils.getAzdataApi().connection.getConnectionString(this.connectionId, false) : '';
                const targetDatabaseName = this.targetDatabaseName ?? '';
                const deploymentOptions = await this.getDeploymentOptions();
                await this.savePublishProfile(filePath.fsPath, targetDatabaseName, targetConnectionString, this.getSqlCmdVariablesForPublish(), deploymentOptions);
                telemetry_1.TelemetryReporter.sendActionEvent(telemetry_1.TelemetryViews.SqlProjectPublishDialog, telemetry_1.TelemetryActions.profileSaved);
            }
            this.publishProfileUri = filePath;
            await this.project.addNoneItem(path.relative(this.project.projectFolderPath, filePath.fsPath));
            void vscode.commands.executeCommand(constants.refreshDataWorkspaceCommand); //refresh data workspace to load the newly added profile to the tree
        });
        return saveProfileAsButton;
    }
    convertSqlCmdVarsToTableFormat(sqlCmdVars) {
        let data = [];
        for (const [key, value] of sqlCmdVars) {
            data.push([{ value: key }, { value: value }]);
        }
        return data;
    }
    /**
     * Enables or disables "Revert SQLCMD variable values" button depending on whether there are changes
     *  */
    updateRevertSqlCmdVarsButtonState() {
        // no SQLCMD vars -> no button to update state for
        if (!this.revertSqlCmdVarsButton) {
            return;
        }
        let revertButtonEnabled = false;
        for (const key of this.sqlCmdVars.keys()) {
            if (this.sqlCmdVars.get(key) !== this.getDefaultSqlCmdValue(key)) {
                revertButtonEnabled = true;
                break;
            }
        }
        this.revertSqlCmdVarsButton.enabled = revertButtonEnabled;
    }
    // only enable "Generate Script" and "Publish" buttons if all fields are filled
    tryEnableGenerateScriptAndPublishButtons() {
        let publishEnabled = false;
        let generateScriptEnabled = false;
        if (this.existingServerRadioButton?.checked) {
            if ((this.targetConnectionTextBox.value && this.targetDatabaseDropDown.value
                || this.connectionIsDataSource && this.targetDatabaseDropDown.value)
                && this.allSqlCmdVariablesFilled()) {
                publishEnabled = true;
                generateScriptEnabled = true;
            }
        }
        else if (utils.validateSqlServerPortNumber(this.serverPortTextBox?.value) &&
            !utils.isEmptyString(this.serverAdminPasswordTextBox?.value) &&
            utils.isValidSQLPassword(this.serverAdminPasswordTextBox?.value || '', constants.defaultLocalServerAdminName) &&
            this.serverAdminPasswordTextBox?.value === this.serverConfigAdminPasswordTextBox?.value
            && this.imageTagDropDown.value && this.eulaCheckBox?.checked) {
            publishEnabled = true; // only publish is supported for container
        }
        this.dialog.okButton.enabled = publishEnabled;
        this.dialog.customButtons[0].enabled = generateScriptEnabled;
    }
    allSqlCmdVariablesFilled() {
        for (let key in this.sqlCmdVars) {
            if (this.sqlCmdVars.get(key) === '' || this.sqlCmdVars.get(key) === undefined) {
                return false;
            }
        }
        return true;
    }
    /*
     * Creates Display options container with a 'configure options' button
     */
    createOptionsButton(view) {
        this.optionsButton = view.modelBuilder.button().withProps({
            label: constants.AdvancedOptionsButton,
            secondary: true,
            width: uiConstants_1.cssStyles.PublishingOptionsButtonWidth
        }).component();
        const optionsRow = view.modelBuilder.flexContainer().withItems([this.optionsButton], { CSSStyles: { flex: '0 0 auto', 'margin': '-8px 0 0 307px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        this.toDispose.push(this.optionsButton.onDidClick(async () => {
            telemetry_1.TelemetryReporter.sendActionEvent(telemetry_1.TelemetryViews.SqlProjectPublishDialog, telemetry_1.TelemetryActions.publishOptionsOpened);
            // Create fresh options dialog with default selections each time when creating the 'configure options' button
            this.publishOptionsDialog = new publishOptionsDialog_1.PublishOptionsDialog(this.deploymentOptions, this);
            this.publishOptionsDialog.openDialog();
        }));
        return optionsRow;
    }
    /*
    * Gets the default deployment options from the dacfx service
    */
    async getDefaultDeploymentOptions() {
        const defaultDeploymentOptions = await utils.getDefaultPublishDeploymentOptions(this.project);
        if (defaultDeploymentOptions && defaultDeploymentOptions.excludeObjectTypes !== undefined) {
            // For publish dialog no default exclude options should exists
            defaultDeploymentOptions.excludeObjectTypes.value = [];
        }
        return defaultDeploymentOptions;
    }
    /*
    * Sets the default deployment options to deployment options model object
    */
    setDeploymentOptions(deploymentOptions) {
        this.deploymentOptions = deploymentOptions;
    }
}
exports.PublishDatabaseDialog = PublishDatabaseDialog;
function promptForPublishProfile(defaultPath) {
    return vscode.window.showOpenDialog({
        title: constants.selectProfile,
        canSelectFiles: true,
        canSelectFolders: false,
        canSelectMany: false,
        defaultUri: vscode.Uri.file(defaultPath),
        filters: {
            [constants.publishSettingsFiles]: ['publish.xml']
        }
    });
}
//# sourceMappingURL=publishDatabaseDialog.js.map