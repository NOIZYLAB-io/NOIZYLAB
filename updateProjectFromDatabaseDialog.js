"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.UpdateProjectFromDatabaseDialog = void 0;
const vscode = require("vscode");
const constants = require("../common/constants");
const newProjectTool = require("../tools/newProjectTool");
const promise_1 = require("../common/promise");
const project_1 = require("../models/project");
const uiConstants_1 = require("../common/uiConstants");
const iconHelper_1 = require("../common/iconHelper");
const utils_1 = require("../common/utils");
const path = require("path");
const utils_2 = require("./utils");
class UpdateProjectFromDatabaseDialog {
    project;
    workspaceProjects;
    dialog;
    serverDropdown;
    databaseDropdown;
    projectFileDropdown;
    compareActionRadioButton;
    updateProjectFromDatabaseTab;
    connectionButton;
    folderStructureDropDown;
    updateActionRadioButton;
    formBuilder;
    connectionId;
    profile;
    action;
    toDispose = [];
    initDialogPromise = new promise_1.Deferred();
    populatedInputsPromise = new promise_1.Deferred();
    updateProjectFromDatabaseCallback;
    constructor(connection, project, workspaceProjects) {
        this.project = project;
        this.workspaceProjects = workspaceProjects;
        if (connection && 'connectionName' in connection) {
            this.profile = connection;
        }
        // need to set profile when database is updated as well as here
        // see what schemaCompare is doing!
        this.dialog = (0, utils_1.getAzdataApi)().window.createModelViewDialog(constants.updateProjectFromDatabaseDialogName, 'updateProjectFromDatabaseDialog');
        this.updateProjectFromDatabaseTab = (0, utils_1.getAzdataApi)().window.createTab(constants.updateProjectFromDatabaseDialogName);
        this.dialog.registerCloseValidator(async () => {
            return this.validate();
        });
        this.toDispose.push(this.dialog.onClosed(_ => this.initDialogPromise.resolve()));
    }
    async openDialog() {
        let connection = await (0, utils_1.getAzdataApi)().connection.getCurrentConnection();
        if (connection) {
            this.connectionId = connection.connectionId;
        }
        this.initializeDialog();
        this.dialog.okButton.label = constants.updateText;
        this.dialog.okButton.enabled = false;
        this.toDispose.push(this.dialog.okButton.onClick(async () => await this.handleUpdateButtonClick()));
        this.dialog.cancelButton.label = constants.cancelButtonText;
        (0, utils_1.getAzdataApi)().window.openDialog(this.dialog);
        await this.initDialogPromise;
        this.tryEnableUpdateButton();
    }
    dispose() {
        this.toDispose.forEach(disposable => disposable.dispose());
    }
    initializeDialog() {
        this.initializeUpdateProjectFromDatabaseTab();
        this.dialog.content = [this.updateProjectFromDatabaseTab];
    }
    initializeUpdateProjectFromDatabaseTab() {
        this.updateProjectFromDatabaseTab.registerContent(async (view) => {
            const connectionRow = this.createServerRow(view);
            const databaseRow = this.createDatabaseRow(view);
            await this.populateServerDropdown();
            const sourceDatabaseFormSection = view.modelBuilder.groupContainer().withLayout({
                header: constants.sourceDatabase,
                collapsible: false,
                collapsed: false
            }).withItems([connectionRow, databaseRow]).component();
            const projectLocationRow = this.createProjectLocationRow(view);
            const folderStructureRow = this.createFolderStructureRow(view);
            const targetProjectFormSection = view.modelBuilder.groupContainer().withLayout({
                header: constants.TargetDatabase,
                collapsible: false,
                collapsed: false
            }).withItems([projectLocationRow, folderStructureRow]).component();
            const actionRow = await this.createActionRow(view);
            const actionFormSection = view.modelBuilder.groupContainer().withLayout({
                header: constants.updateAction,
                collapsible: false,
                collapsed: false
            }).withItems([actionRow]).component();
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
                            component: actionFormSection,
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
            await this.connectionButton?.focus();
            this.initDialogPromise.resolve();
        });
    }
    createServerRow(view) {
        this.createServerComponent(view);
        const serverLabel = view.modelBuilder.text().withProps({
            value: constants.server,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.updateProjectFromDatabaseLabelWidth
        }).component();
        const connectionRow = view.modelBuilder.flexContainer().withItems([serverLabel, this.serverDropdown], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-bottom': '-5px', 'margin-top': '-10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        connectionRow.addItem(this.connectionButton, { CSSStyles: { 'margin-right': '0px', 'margin-bottom': '-5px', 'margin-top': '-10px' } });
        return connectionRow;
    }
    createDatabaseRow(view) {
        this.createDatabaseComponent(view);
        const databaseLabel = view.modelBuilder.text().withProps({
            value: constants.databaseNameLabel,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.updateProjectFromDatabaseLabelWidth
        }).component();
        const databaseRow = view.modelBuilder.flexContainer().withItems([databaseLabel, this.databaseDropdown], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-bottom': '-10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        return databaseRow;
    }
    createServerComponent(view) {
        this.serverDropdown = view.modelBuilder.dropDown().withProps({
            editable: true,
            fireOnTextChange: true,
            width: uiConstants_1.cssStyles.updateProjectFromDatabaseTextboxWidth,
            ariaLabel: constants.server,
            required: true
        }).component();
        this.createConnectionButton(view);
        this.serverDropdown.onValueChanged(() => {
            this.tryEnableUpdateButton();
        });
    }
    createDatabaseComponent(view) {
        this.databaseDropdown = view.modelBuilder.dropDown().withProps({
            editable: true,
            fireOnTextChange: true,
            width: uiConstants_1.cssStyles.updateProjectFromDatabaseTextboxWidth,
            ariaLabel: constants.databaseNameLabel,
            required: true
        }).component();
        this.databaseDropdown.onValueChanged(() => {
            this.tryEnableUpdateButton();
        });
    }
    async populateServerDropdown() {
        this.serverDropdown.loading = true;
        const values = await this.getServerValues();
        if (values && values.length > 0) {
            await this.serverDropdown.updateProperties({
                values: values,
                value: values[0]
            });
        }
        this.serverDropdown.loading = false;
        if (this.serverDropdown.value) {
            await this.populateDatabaseDropdown();
        }
        this.tryEnableUpdateButton();
        this.populatedInputsPromise.resolve();
    }
    async populateDatabaseDropdown() {
        const connectionProfile = this.serverDropdown.value.connection;
        this.databaseDropdown.loading = true;
        await this.databaseDropdown.updateProperties({
            values: [],
            value: undefined
        });
        let values = [];
        try {
            values = await this.getDatabaseValues(connectionProfile.connectionId);
            // move system dbs to the bottom of the list so it's easier to find user dbs
            const systemDbs = values.filter(db => constants.systemDbs.includes(db));
            values = values.filter(db => !constants.systemDbs.includes(db)).concat(systemDbs);
        }
        catch (e) {
            // if the user doesn't have access to master, just set the database of the connection profile
            values = [connectionProfile.databaseName];
            console.warn(e);
        }
        if (values && values.length > 0) {
            await this.databaseDropdown.updateProperties({
                values: values,
                value: values[0],
            });
            // change the database dropdown value to the connection's database if there is one
            if (connectionProfile.options.database && connectionProfile.options.database !== constants.master) {
                this.databaseDropdown.value = connectionProfile.options.database;
            }
        }
        this.databaseDropdown.loading = false;
    }
    async getServerValues() {
        let cons = await (0, utils_1.getAzdataApi)().connection.getConnections(/* activeConnectionsOnly */ true);
        // This user has no active connections
        if (!cons || cons.length === 0) {
            return undefined;
        }
        // Update connection icon to "connected" state
        this.connectionButton.iconPath = iconHelper_1.IconPathHelper.connect;
        // reverse list so that most recent connections are first
        cons.reverse();
        let count = -1;
        let idx = -1;
        let values = cons.map(c => {
            count++;
            let usr = c.options.user;
            if (!usr) {
                usr = constants.defaultUser;
            }
            let srv = c.options.server;
            let finalName = `${srv} (${usr})`;
            if (c.options.connectionName) {
                finalName = c.options.connectionName;
            }
            if (c.connectionId === this.connectionId) {
                idx = count;
            }
            return {
                connection: c,
                displayName: finalName,
                name: srv,
            };
        });
        // move server of current connection to the top of the list so it is the default
        if (idx >= 1) {
            let tmp = values[0];
            values[0] = values[idx];
            values[idx] = tmp;
        }
        values = values.reduce((uniqueValues, conn) => {
            let exists = uniqueValues.find(x => x.displayName === conn.displayName);
            if (!exists) {
                uniqueValues.push(conn);
            }
            return uniqueValues;
        }, []);
        return values;
    }
    async getDatabaseValues(connectionId) {
        let idx = -1;
        let count = -1;
        let values = (await (0, utils_1.getAzdataApi)().connection.listDatabases(connectionId)).sort((a, b) => a.localeCompare(b)).map(db => {
            count++;
            // put currently selected db at the top of the dropdown if there is one
            if (this.profile && this.profile.databaseName && this.profile.databaseName === db) {
                idx = count;
            }
            return db;
        });
        if (idx >= 0) {
            let tmp = values[0];
            values[0] = values[idx];
            values[idx] = tmp;
        }
        return values;
    }
    createConnectionButton(view) {
        this.connectionButton = view.modelBuilder.button().withProps({
            ariaLabel: constants.selectConnection,
            title: constants.selectConnection,
            iconPath: iconHelper_1.IconPathHelper.selectConnection,
            height: '20px',
            width: '20px'
        }).component();
        this.connectionButton.onDidClick(async () => {
            await this.connectionButtonClick();
            this.connectionButton.iconPath = iconHelper_1.IconPathHelper.connect;
        });
    }
    async connectionButtonClick() {
        let connection = await (0, utils_1.getAzdataApi)().connection.openConnectionDialog(undefined, undefined, {
            saveConnection: false,
            showDashboard: false,
            showConnectionDialogOnError: true,
            showFirewallRuleOnError: true
        });
        if (connection) {
            this.connectionId = connection.connectionId;
            await this.populateServerDropdown();
        }
    }
    createProjectLocationRow(view) {
        const browseFolderButton = this.createBrowseFileButton(view);
        let values = [];
        this.workspaceProjects.forEach(projectUri => {
            values.push(projectUri.fsPath);
        });
        const value = this.project ? this.project.projectFilePath : (values[0] ?? '');
        this.projectFileDropdown = view.modelBuilder.dropDown().withProps({
            editable: true,
            fireOnTextChange: true,
            value: value,
            values: values,
            width: uiConstants_1.cssStyles.updateProjectFromDatabaseTextboxWidth,
            ariaLabel: constants.location,
            required: true
        }).component();
        this.projectFileDropdown.onValueChanged(async () => {
            await this.projectFileDropdown.updateProperty('title', this.projectFileDropdown.value);
            this.tryEnableUpdateButton();
        });
        const projectLocationLabel = view.modelBuilder.text().withProps({
            value: constants.projectLocationLabel,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.updateProjectFromDatabaseLabelWidth
        }).component();
        const projectLocationRow = view.modelBuilder.flexContainer().withItems([projectLocationLabel,], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-bottom': '-5px', 'margin-top': '-7px' } }).component();
        projectLocationRow.addItem(this.projectFileDropdown, { CSSStyles: { 'margin-right': '10px' } });
        projectLocationRow.addItem(browseFolderButton, { CSSStyles: { 'margin-top': '2px' } });
        return projectLocationRow;
    }
    createBrowseFileButton(view) {
        const browseFolderButton = view.modelBuilder.button().withProps({
            ariaLabel: constants.browseButtonText,
            title: constants.browseButtonText,
            iconPath: iconHelper_1.IconPathHelper.folder_blue,
            height: '18px',
            width: '18px'
        }).component();
        browseFolderButton.onDidClick(async () => {
            let fileUris = await vscode.window.showOpenDialog({
                canSelectFiles: true,
                canSelectFolders: false,
                canSelectMany: false,
                openLabel: constants.selectString,
                defaultUri: newProjectTool.defaultProjectSaveLocation(),
                filters: {
                    'Files': ['sqlproj']
                }
            });
            if (!fileUris || fileUris.length === 0) {
                return;
            }
            this.projectFileDropdown.value = fileUris[0].fsPath;
            await this.projectFileDropdown.updateProperty('title', fileUris[0].fsPath);
        });
        return browseFolderButton;
    }
    createFolderStructureRow(view) {
        this.folderStructureDropDown = view.modelBuilder.dropDown().withProps({
            values: [constants.file, constants.flat, constants.objectType, constants.schema, constants.schemaObjectType],
            value: constants.schemaObjectType,
            ariaLabel: constants.folderStructureLabel,
            required: true,
            width: uiConstants_1.cssStyles.updateProjectFromDatabaseTextboxWidth
        }).component();
        this.folderStructureDropDown.onValueChanged(() => {
            this.tryEnableUpdateButton();
        });
        const folderStructureLabel = view.modelBuilder.text().withProps({
            value: constants.folderStructureLabel,
            requiredIndicator: true,
            width: uiConstants_1.cssStyles.createProjectFromDatabaseLabelWidth
        }).component();
        const folderStructureRow = view.modelBuilder.flexContainer().withItems([folderStructureLabel, this.folderStructureDropDown], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-bottom': '-10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        return folderStructureRow;
    }
    async createActionRow(view) {
        this.compareActionRadioButton = view.modelBuilder.radioButton().withProps({
            name: 'action',
            label: constants.compareActionRadioButtonLabel,
            checked: true
        }).component();
        this.updateActionRadioButton = view.modelBuilder.radioButton().withProps({
            name: 'action',
            label: constants.updateActionRadioButtonLabel
        }).component();
        await this.compareActionRadioButton.updateProperties({ checked: true });
        this.action = 0 /* UpdateProjectAction.Compare */;
        this.compareActionRadioButton.onDidChangeCheckedState((checked) => {
            if (checked) {
                this.action = 0 /* UpdateProjectAction.Compare */;
                this.tryEnableUpdateButton();
            }
        });
        this.updateActionRadioButton.onDidChangeCheckedState((checked) => {
            if (checked) {
                this.action = 1 /* UpdateProjectAction.Update */;
                this.tryEnableUpdateButton();
            }
        });
        let radioButtons = view.modelBuilder.flexContainer()
            .withLayout({ flexFlow: 'column' })
            .withItems([this.compareActionRadioButton, this.updateActionRadioButton])
            .withProps({ ariaRole: 'radiogroup', ariaLabel: constants.actionLabel })
            .component();
        const actionLabel = view.modelBuilder.text().withProps({
            value: constants.actionLabel,
            width: uiConstants_1.cssStyles.updateProjectFromDatabaseLabelWidth
        }).component();
        const actionRow = view.modelBuilder.flexContainer().withItems([actionLabel], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px', 'margin-top': '-17px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        actionRow.addItem(radioButtons);
        return actionRow;
    }
    // only enable Update button if all fields are filled
    tryEnableUpdateButton() {
        if (this.serverDropdown?.value
            && this.databaseDropdown?.value
            && this.projectFileDropdown?.value
            && this.folderStructureDropDown?.value
            && this.action !== undefined) {
            this.dialog.okButton.enabled = true;
        }
        else {
            this.dialog.okButton.enabled = false;
        }
    }
    async handleUpdateButtonClick() {
        const serverDropdownValue = this.serverDropdown.value;
        const ownerUri = await (0, utils_1.getAzdataApi)().connection.getUriForConnection(serverDropdownValue.connection.connectionId);
        let connection = (await (0, utils_1.getAzdataApi)().connection.getConnections(true)).filter(con => con.connectionId === serverDropdownValue.connection.connectionId)[0];
        connection.databaseName = this.databaseDropdown.value;
        const credentials = await (0, utils_1.getAzdataApi)().connection.getCredentials(connection.connectionId);
        if (credentials.hasOwnProperty('password')) {
            connection.password = connection.options.password = credentials.password;
        }
        const projectFilePath = this.projectFileDropdown.value;
        this.project = await project_1.Project.openProject(projectFilePath);
        const connectionDetails = {
            id: connection.connectionId,
            userName: connection.userName,
            password: connection.password,
            serverName: connection.serverName,
            databaseName: connection.databaseName,
            connectionName: connection.connectionName,
            providerName: connection.providerId,
            groupId: connection.groupId,
            groupFullName: connection.groupFullName,
            authenticationType: connection.authenticationType,
            savePassword: connection.savePassword,
            saveProfile: connection.saveProfile,
            options: connection.options,
        };
        const sourceEndpointInfo = {
            endpointType: 0 /* mssql.SchemaCompareEndpointType.Database */,
            databaseName: this.databaseDropdown.value,
            serverDisplayName: serverDropdownValue.displayName,
            serverName: serverDropdownValue.name,
            connectionDetails: connectionDetails,
            ownerUri: ownerUri,
            projectFilePath: '',
            extractTarget: 5 /* mssql.ExtractTarget.schemaObjectType */,
            targetScripts: [],
            dataSchemaProvider: '',
            packageFilePath: '',
            connectionName: serverDropdownValue.connection.options.connectionName
        };
        const targetEndpointInfo = {
            endpointType: 2 /* mssql.SchemaCompareEndpointType.Project */,
            projectFilePath: projectFilePath,
            extractTarget: (0, utils_2.mapExtractTargetEnum)(this.folderStructureDropDown.value),
            targetScripts: [],
            dataSchemaProvider: this.project.getProjectTargetVersion(),
            connectionDetails: connectionDetails,
            databaseName: '',
            serverDisplayName: '',
            serverName: '',
            ownerUri: '',
            packageFilePath: '',
        };
        const model = {
            sourceEndpointInfo: sourceEndpointInfo,
            targetEndpointInfo: targetEndpointInfo,
            action: this.action
        };
        void this.updateProjectFromDatabaseCallback(model);
        this.dispose();
    }
    async validate() {
        try {
            if (await (0, utils_1.getDataWorkspaceExtensionApi)().validateWorkspace() === false) {
                return false;
            }
            // the selected location should be an existing directory
            const parentDirectoryExists = await (0, utils_1.exists)(path.dirname(this.projectFileDropdown.value));
            if (!parentDirectoryExists) {
                this.showErrorMessage(constants.ProjectParentDirectoryNotExistError(this.projectFileDropdown.value));
                return false;
            }
            // the selected location must contain a .sqlproj file
            const fileExists = await (0, utils_1.exists)(this.projectFileDropdown.value);
            if (!fileExists) {
                this.showErrorMessage(constants.noSqlProjFile);
                return false;
            }
            // schema compare extension must be downloaded
            if (!vscode.extensions.getExtension(constants.schemaCompareExtensionId)) {
                this.showErrorMessage(constants.noSchemaCompareExtension);
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
            level: (0, utils_1.getAzdataApi)().window.MessageLevel.Error
        };
    }
}
exports.UpdateProjectFromDatabaseDialog = UpdateProjectFromDatabaseDialog;
//# sourceMappingURL=updateProjectFromDatabaseDialog.js.map