"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.CreateProjectFromDatabaseDialog = void 0;
const vscode = require("vscode");
const constants = require("../common/constants");
const newProjectTool = require("../tools/newProjectTool");
const path = require("path");
const iconHelper_1 = require("../common/iconHelper");
const uiConstants_1 = require("../common/uiConstants");
const promise_1 = require("../common/promise");
const utils_1 = require("./utils");
const utils_2 = require("../common/utils");
class CreateProjectFromDatabaseDialog {
    profile;
    dialog;
    createProjectFromDatabaseTab;
    sourceConnectionTextBox;
    selectConnectionButton;
    sourceDatabaseDropDown;
    projectNameTextBox;
    projectLocationTextBox;
    folderStructureDropDown;
    includePermissionsCheckbox;
    sdkStyleCheckbox;
    formBuilder;
    connectionId;
    toDispose = [];
    initDialogComplete = new promise_1.Deferred();
    createProjectFromDatabaseCallback;
    constructor(profile) {
        this.profile = profile;
        this.dialog = (0, utils_2.getAzdataApi)().window.createModelViewDialog(constants.createProjectFromDatabaseDialogName, 'createProjectFromDatabaseDialog');
        this.createProjectFromDatabaseTab = (0, utils_2.getAzdataApi)().window.createTab(constants.createProjectFromDatabaseDialogName);
        this.dialog.registerCloseValidator(async () => {
            return this.validate();
        });
    }
    async openDialog() {
        this.initializeDialog();
        this.dialog.okButton.label = constants.createProjectDialogOkButtonText;
        this.dialog.okButton.enabled = false;
        this.toDispose.push(this.dialog.okButton.onClick(async () => await this.handleCreateButtonClick()));
        this.dialog.cancelButton.label = constants.cancelButtonText;
        let connected = false;
        // make sure the connection profile passed in has sufficient information to attempt to connect
        if (this.profile && this.profile?.serverName) {
            const connections = await (0, utils_2.getAzdataApi)().connection.getConnections(true);
            connected = !!connections.find(c => c.connectionId === this.profile.id);
            if (!connected) {
                // if the connection clicked on isn't currently connected, try to connect
                const result = await (0, utils_2.getAzdataApi)().connection.connect(this.profile, true, false);
                connected = result.connected;
                if (!result.connected) {
                    // if can't connect automatically, open connection dialog with the info from the profile
                    const connection = await (0, utils_2.getAzdataApi)().connection.openConnectionDialog(undefined, this.profile, {
                        saveConnection: false,
                        showDashboard: false,
                        showConnectionDialogOnError: true,
                        showFirewallRuleOnError: true
                    });
                    connected = !!connection;
                    // update these fields if connection was successful, to ensure they match the connection made
                    if (connected) {
                        this.profile.id = connection.connectionId;
                        this.profile.databaseName = connection.options['databaseName'];
                        this.profile.serverName = connection.options['server'];
                        this.profile.userName = connection.options['user'];
                    }
                }
                else {
                    // Successfully connectted, update connection Id as received.
                    this.profile.id = result.connectionId;
                }
            }
        }
        (0, utils_2.getAzdataApi)().window.openDialog(this.dialog);
        await this.initDialogComplete.promise;
        if (connected) {
            await this.updateConnectionComponents((0, utils_1.getConnectionName)(this.profile), this.profile.id, this.profile.databaseName);
        }
        this.tryEnableCreateButton();
    }
    dispose() {
        this.toDispose.forEach(disposable => disposable.dispose());
    }
    initializeDialog() {
        this.initializeCreateProjectFromDatabaseTab();
        this.dialog.content = [this.createProjectFromDatabaseTab];
    }
    initializeCreateProjectFromDatabaseTab() {
        this.createProjectFromDatabaseTab.registerContent(async (view) => {
            const connectionRow = this.createConnectionRow(view);
            const databaseRow = this.createDatabaseRow(view);
            const sourceDatabaseFormSection = view.modelBuilder.groupContainer().withLayout({
                header: constants.sourceDatabase,
                collapsible: false,
                collapsed: false
            }).withItems([connectionRow, databaseRow]).component();
            const projectNameRow = this.createProjectNameRow(view);
            const projectLocationRow = this.createProjectLocationRow(view);
            const targetProjectFormSection = view.modelBuilder.groupContainer().withLayout({
                header: constants.targetProject,
                collapsible: false,
                collapsed: false
            }).withItems([projectNameRow, projectLocationRow]).component();
            const folderStructureRow = this.createFolderStructureRow(view);
            this.includePermissionsCheckbox = view.modelBuilder.checkBox().withProps({
                label: constants.includePermissionsLabel,
            }).component();
            // could also potentially be radio buttons once there's a term to refer to "legacy" style sqlprojs
            this.sdkStyleCheckbox = view.modelBuilder.checkBox().withProps({
                checked: true,
                label: constants.sdkStyleProject
            }).component();
            const sdkLearnMore = view.modelBuilder.hyperlink().withProps({
                label: constants.learnMore,
                url: constants.sdkLearnMoreUrl
            }).component();
            const sdkFormComponentGroup = view.modelBuilder.flexContainer()
                .withLayout({ flexFlow: 'row', alignItems: 'baseline' })
                .withItems([this.sdkStyleCheckbox, sdkLearnMore], { CSSStyles: { flex: '0 0 auto', 'margin-right': '10px' } })
                .component();
            const settingsFormSection = view.modelBuilder.groupContainer().withLayout({
                header: constants.createProjectSettings,
                collapsible: false,
                collapsed: false
            }).withItems([folderStructureRow, this.includePermissionsCheckbox, sdkFormComponentGroup]).component();
            this.formBuilder = view.modelBuilder.formContainer()
                .withFormItems([
                {
                    title: '',
                    components: [
                        {
                            component: sourceDatabaseFormSection,
                        }
                    ]
                },
                {
                    title: '',
                    components: [
                        {
                            component: targetProjectFormSection,
                        }
                    ]
                },
                {
                    title: '',
                    components: [
                        {
                            component: settingsFormSection
                        }
                    ]
                }
            ], {
                horizontal: false,
                titleFontSize: uiConstants_1.cssStyles.titleFontSize
            })
                .withLayout({
                width: '100%',
                padding: '10px 10px 0 20px'
            });
            let formModel = this.formBuilder.component();
            await view.initializeModel(formModel);
            await this.selectConnectionButton?.focus();
            this.initDialogComplete?.resolve();
        });
    }
    createConnectionRow(view) {
        const sourceConnectionTextBox = this.createSourceConnectionComponent(view);
        const selectConnectionButton = this.createSelectConnectionButton(view);
        const serverLabel = view.modelBuilder.text().withProps({
            value: constants.server,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseLabelWidth
        }).component();
        const connectionRow = view.modelBuilder.flexContainer().withItems([serverLabel, sourceConnectionTextBox], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-bottom': '-5px', 'margin-top': '-10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        connectionRow.addItem(selectConnectionButton, { CSSStyles: { 'margin-right': '0px', 'margin-bottom': '-5px', 'margin-top': '-10px' } });
        return connectionRow;
    }
    createDatabaseRow(view) {
        this.sourceDatabaseDropDown = view.modelBuilder.dropDown().withProps({
            ariaLabel: constants.databaseNameLabel,
            required: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseTextboxWidth
        }).component();
        this.sourceDatabaseDropDown.onValueChanged(() => {
            this.setProjectName();
            this.tryEnableCreateButton();
        });
        const databaseLabel = view.modelBuilder.text().withProps({
            value: constants.databaseNameLabel,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseLabelWidth
        }).component();
        const databaseRow = view.modelBuilder.flexContainer().withItems([databaseLabel, this.sourceDatabaseDropDown], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-bottom': '-10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        return databaseRow;
    }
    setProjectName() {
        this.projectNameTextBox.value = newProjectTool.defaultProjectNameFromDb((0, utils_2.sanitizeStringForFilename)(this.sourceDatabaseDropDown.value));
    }
    createSourceConnectionComponent(view) {
        this.sourceConnectionTextBox = view.modelBuilder.inputBox().withProps({
            value: '',
            placeHolder: constants.selectConnection,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseTextboxWidth,
            enabled: false
        }).component();
        this.sourceConnectionTextBox.onTextChanged(() => {
            this.tryEnableCreateButton();
        });
        return this.sourceConnectionTextBox;
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
            let connection = await (0, utils_2.getAzdataApi)().connection.openConnectionDialog(undefined, undefined, {
                saveConnection: false,
                showDashboard: false,
                showConnectionDialogOnError: true,
                showFirewallRuleOnError: true
            });
            this.connectionId = connection.connectionId;
            let connectionTextboxValue;
            connectionTextboxValue = (0, utils_1.getConnectionName)(connection);
            await this.updateConnectionComponents(connectionTextboxValue, this.connectionId, connection.options.database);
        });
        return this.selectConnectionButton;
    }
    async updateConnectionComponents(connectionTextboxValue, connectionId, databaseName) {
        this.sourceConnectionTextBox.value = connectionTextboxValue;
        void this.sourceConnectionTextBox.updateProperty('title', connectionTextboxValue);
        // populate database dropdown with the databases for this connection
        if (connectionId) {
            this.sourceDatabaseDropDown.loading = true;
            let databaseValues;
            try {
                databaseValues = (await (0, utils_2.getAzdataApi)().connection.listDatabases(connectionId))
                    // filter out system dbs
                    .filter(db => !constants.systemDbs.includes(db));
            }
            catch (e) {
                // if the user doesn't have access to master, just set the database of the connection profile
                databaseValues = [databaseName];
                console.warn(e);
            }
            this.sourceDatabaseDropDown.values = databaseValues;
            this.sourceDatabaseDropDown.loading = false;
            this.connectionId = connectionId;
        }
        // change the database inputbox value to the connection's database if there is one
        if (databaseName && databaseName !== constants.master) {
            this.sourceDatabaseDropDown.value = databaseName;
        }
        // change icon to the one without a plus sign
        this.selectConnectionButton.iconPath = iconHelper_1.IconPathHelper.connect;
    }
    createProjectNameRow(view) {
        this.projectNameTextBox = view.modelBuilder.inputBox().withValidation(component => (0, utils_2.isValidBasename)(component.value))
            .withProps({
            ariaLabel: constants.projectNameLabel,
            placeHolder: constants.projectNamePlaceholderText,
            required: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseTextboxWidth
        }).component();
        this.projectNameTextBox.onTextChanged(text => {
            const errorMessage = (0, utils_2.isValidBasenameErrorMessage)(text);
            if (errorMessage !== undefined) {
                // Set validation error message if project name is invalid
                void this.projectNameTextBox.updateProperty('validationErrorMessage', errorMessage);
            }
            else {
                this.projectNameTextBox.value = this.projectNameTextBox.value?.trim();
                void this.projectNameTextBox.updateProperty('title', this.projectNameTextBox.value);
                this.tryEnableCreateButton();
            }
        });
        const projectNameLabel = view.modelBuilder.text().withProps({
            value: constants.projectNameLabel,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseLabelWidth
        }).component();
        const projectNameRow = view.modelBuilder.flexContainer().withItems([projectNameLabel, this.projectNameTextBox], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-bottom': '-5px', 'margin-top': '-10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        return projectNameRow;
    }
    createProjectLocationRow(view) {
        const browseFolderButton = this.createBrowseFolderButton(view);
        this.projectLocationTextBox = view.modelBuilder.inputBox().withProps({
            value: '',
            ariaLabel: constants.location,
            placeHolder: constants.projectLocationPlaceholderText,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseTextboxWidth,
            required: true
        }).component();
        this.projectLocationTextBox.onTextChanged(() => {
            void this.projectLocationTextBox.updateProperty('title', this.projectLocationTextBox.value);
            this.tryEnableCreateButton();
        });
        const projectLocationLabel = view.modelBuilder.text().withProps({
            value: constants.location,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseLabelWidth
        }).component();
        const projectLocationRow = view.modelBuilder.flexContainer().withItems([projectLocationLabel, this.projectLocationTextBox], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-bottom': '-10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        projectLocationRow.addItem(browseFolderButton, { CSSStyles: { 'margin-right': '0px', 'margin-bottom': '-10px' } });
        return projectLocationRow;
    }
    createBrowseFolderButton(view) {
        const browseFolderButton = view.modelBuilder.button().withProps({
            ariaLabel: constants.browseButtonText,
            title: constants.browseButtonText,
            iconPath: iconHelper_1.IconPathHelper.folder_blue,
            height: '18px',
            width: '18px'
        }).component();
        browseFolderButton.onDidClick(async () => {
            let folderUris = await vscode.window.showOpenDialog({
                canSelectFiles: false,
                canSelectFolders: true,
                canSelectMany: false,
                openLabel: constants.selectString,
                defaultUri: newProjectTool.defaultProjectSaveLocation()
            });
            if (!folderUris || folderUris.length === 0) {
                return;
            }
            this.projectLocationTextBox.value = folderUris[0].fsPath;
            void this.projectLocationTextBox.updateProperty('title', folderUris[0].fsPath);
        });
        return browseFolderButton;
    }
    createFolderStructureRow(view) {
        this.folderStructureDropDown = view.modelBuilder.dropDown().withProps({
            values: [constants.file, constants.flat, constants.objectType, constants.schema, constants.schemaObjectType],
            value: constants.schemaObjectType,
            ariaLabel: constants.folderStructureLabel,
            required: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseTextboxWidth
        }).component();
        this.folderStructureDropDown.onValueChanged(() => {
            this.tryEnableCreateButton();
        });
        const folderStructureLabel = view.modelBuilder.text().withProps({
            value: constants.folderStructureLabel,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseLabelWidth
        }).component();
        const folderStructureRow = view.modelBuilder.flexContainer().withItems([folderStructureLabel, this.folderStructureDropDown], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-top': '-10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        return folderStructureRow;
    }
    // only enable Create button if all fields are filled
    tryEnableCreateButton() {
        if (this.sourceConnectionTextBox.value && this.sourceDatabaseDropDown.value
            && this.projectNameTextBox.value && this.projectLocationTextBox.value) {
            this.dialog.okButton.enabled = true;
        }
        else {
            this.dialog.okButton.enabled = false;
        }
    }
    async handleCreateButtonClick() {
        const azdataApi = (0, utils_2.getAzdataApi)();
        const connectionUri = await azdataApi.connection.getUriForConnection(this.connectionId);
        const model = {
            connectionUri: connectionUri,
            database: this.sourceDatabaseDropDown.value,
            projName: this.projectNameTextBox.value,
            filePath: this.projectLocationTextBox.value,
            version: '1.0.0.0',
            extractTarget: (0, utils_1.mapExtractTargetEnum)(this.folderStructureDropDown.value),
            sdkStyle: this.sdkStyleCheckbox?.checked,
            includePermissions: this.includePermissionsCheckbox?.checked
        };
        azdataApi.window.closeDialog(this.dialog);
        await this.createProjectFromDatabaseCallback(model, this.connectionId);
        this.dispose();
    }
    async validate() {
        try {
            // the selected location should be an existing directory
            const parentDirectoryExists = await (0, utils_2.exists)(this.projectLocationTextBox.value);
            if (!parentDirectoryExists) {
                this.showErrorMessage(constants.ProjectParentDirectoryNotExistError(this.projectLocationTextBox.value));
                return false;
            }
            // there shouldn't be an existing sub directory with the same name as the project in the selected location
            const projectDirectoryExists = await (0, utils_2.exists)(path.join(this.projectLocationTextBox.value, this.projectNameTextBox.value));
            if (projectDirectoryExists) {
                this.showErrorMessage(constants.ProjectDirectoryAlreadyExistError(this.projectNameTextBox.value, this.projectLocationTextBox.value));
                return false;
            }
            if (await (0, utils_2.getDataWorkspaceExtensionApi)().validateWorkspace() === false) {
                return false;
            }
            return true;
        }
        catch (err) {
            this.showErrorMessage(err?.message ? err.message : err);
            return false;
        }
    }
    showErrorMessage(message) {
        this.dialog.message = {
            text: message,
            level: (0, utils_2.getAzdataApi)().window.MessageLevel.Error
        };
    }
}
exports.CreateProjectFromDatabaseDialog = CreateProjectFromDatabaseDialog;
//# sourceMappingURL=createProjectFromDatabaseDialog.js.map