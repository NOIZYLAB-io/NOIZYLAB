"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.AddDatabaseReferenceDialog = exports.ReferencedDatabaseType = void 0;
exports.getSystemDbOptions = getSystemDbOptions;
exports.promptDacpacLocation = promptDacpacLocation;
const vscode = require("vscode");
const path = require("path");
const constants = require("../common/constants");
const utils = require("../common/utils");
const uiConstants_1 = require("../common/uiConstants");
const iconHelper_1 = require("../common/iconHelper");
const promise_1 = require("../common/promise");
const telemetry_1 = require("../common/telemetry");
const utils_1 = require("./utils");
var ReferencedDatabaseType;
(function (ReferencedDatabaseType) {
    ReferencedDatabaseType[ReferencedDatabaseType["project"] = 0] = "project";
    ReferencedDatabaseType[ReferencedDatabaseType["systemDb"] = 1] = "systemDb";
    ReferencedDatabaseType[ReferencedDatabaseType["dacpac"] = 2] = "dacpac";
    ReferencedDatabaseType[ReferencedDatabaseType["nupkg"] = 3] = "nupkg";
})(ReferencedDatabaseType || (exports.ReferencedDatabaseType = ReferencedDatabaseType = {}));
class AddDatabaseReferenceDialog {
    project;
    dialog;
    addDatabaseReferenceTab;
    view;
    formBuilder;
    projectDropdown;
    projectFormComponent;
    systemDatabaseDropdown;
    systemDatabaseFormComponent;
    dacpacTextbox;
    dacpacFormComponent;
    nupkgNameTextbox;
    nupkgVersionTextbox;
    nupkgFormComponent;
    locationDropdown;
    databaseNameTextbox;
    databaseVariableTextbox;
    serverNameTextbox;
    serverVariableTextbox;
    suppressMissingDependenciesErrorsCheckbox;
    exampleUsage;
    projectRadioButton;
    systemDatabaseRadioButton;
    systemDatabaseArtifactRefRadioButton;
    systemDatabasePackageRefRadioButton;
    systemDbRefRadioButtonsComponent;
    systemDbRefType = 0 /* SystemDbReferenceType.ArtifactReference */;
    currentReferencedDatabaseType;
    databaseNameTextboxLabel;
    serverNameTextboxLabel;
    serverVariableTextboxLabel;
    toDispose = [];
    initDialogComplete = new promise_1.Deferred();
    addReference;
    constructor(project) {
        this.project = project;
        this.dialog = utils.getAzdataApi().window.createModelViewDialog(constants.addDatabaseReferenceDialogName, 'addDatabaseReferencesDialog');
        this.addDatabaseReferenceTab = utils.getAzdataApi().window.createTab(constants.addDatabaseReferenceDialogName);
        this.dialog.registerCloseValidator(async () => {
            return this.validate();
        });
    }
    validate() {
        // only support adding dacpacs that are on the same drive as the sqlproj
        if (this.currentReferencedDatabaseType === ReferencedDatabaseType.dacpac) {
            const projectDrive = path.parse(this.project.projectFilePath).root;
            const dacpacDrive = path.parse(this.dacpacTextbox.value).root;
            if (projectDrive !== dacpacDrive) {
                this.dialog.message = {
                    text: constants.dacpacNotOnSameDrive(this.project.projectFilePath),
                    level: utils.getAzdataApi().window.MessageLevel.Error
                };
                return false;
            }
        }
        return true;
    }
    async openDialog() {
        this.initializeDialog();
        this.dialog.okButton.label = constants.addDatabaseReferenceOkButtonText;
        this.dialog.okButton.enabled = false;
        this.toDispose.push(this.dialog.okButton.onClick(async () => await this.addReferenceClick()));
        this.dialog.cancelButton.label = constants.cancelButtonText;
        utils.getAzdataApi().window.openDialog(this.dialog);
        await this.initDialogComplete.promise;
    }
    dispose() {
        this.toDispose.forEach(disposable => disposable.dispose());
    }
    initializeDialog() {
        this.initializeTab();
        this.dialog.content = [this.addDatabaseReferenceTab];
    }
    initializeTab() {
        this.addDatabaseReferenceTab.registerContent(async (view) => {
            this.view = view;
            this.projectFormComponent = await this.createProjectDropdown();
            const radioButtonGroup = this.createReferenceTypeRadioButtons();
            this.systemDatabaseFormComponent = this.createSystemDatabaseDropdown();
            this.dacpacFormComponent = this.createDacpacTextbox();
            this.nupkgFormComponent = this.createNupkgFormComponentGroup();
            const locationDropdown = this.createLocationDropdown();
            const variableSection = this.createVariableSection();
            this.systemDbRefRadioButtonsComponent = this.createSystemDbReferenceTypeRadioButtons();
            this.suppressMissingDependenciesErrorsCheckbox = view.modelBuilder.checkBox().withProps({
                label: constants.suppressMissingDependenciesErrors
            }).component();
            const exampleUsage = this.createExampleUsage();
            this.formBuilder = view.modelBuilder.formContainer()
                .withFormItems([
                {
                    title: '',
                    components: [
                        radioButtonGroup,
                        this.currentReferencedDatabaseType === ReferencedDatabaseType.project ? this.projectFormComponent : this.systemDatabaseFormComponent,
                        locationDropdown,
                        variableSection,
                        exampleUsage,
                        {
                            component: this.suppressMissingDependenciesErrorsCheckbox
                        }
                    ]
                }
            ], {
                horizontal: false
            })
                .withLayout({
                width: '100%'
            });
            let formModel = this.formBuilder.component();
            await view.initializeModel(formModel);
            this.updateEnabledInputBoxes();
            if (this.currentReferencedDatabaseType === ReferencedDatabaseType.project) {
                await this.projectRadioButton?.focus();
            }
            else {
                await this.systemDatabaseRadioButton?.focus();
                this.insertSystemDatabaseReferenceTypeComponent();
            }
            this.initDialogComplete.resolve();
        });
    }
    async addReferenceClick() {
        let referenceSettings;
        if (this.currentReferencedDatabaseType === ReferencedDatabaseType.systemDb) {
            const systemDbRef = {
                databaseVariableLiteralValue: this.databaseNameTextbox?.value,
                systemDb: utils.getSystemDatabase(this.systemDatabaseDropdown?.value),
                suppressMissingDependenciesErrors: this.suppressMissingDependenciesErrorsCheckbox?.checked,
                systemDbReferenceType: this.systemDbRefType
            };
            referenceSettings = systemDbRef;
        }
        else {
            if (this.currentReferencedDatabaseType === ReferencedDatabaseType.project) {
                const projRef = {
                    projectName: this.projectDropdown?.value,
                    projectGuid: '',
                    projectRelativePath: undefined,
                    suppressMissingDependenciesErrors: this.suppressMissingDependenciesErrorsCheckbox?.checked
                };
                referenceSettings = projRef;
            }
            else if (this.currentReferencedDatabaseType === ReferencedDatabaseType.dacpac) {
                const dacpacRef = {
                    databaseName: (0, utils_1.ensureSetOrDefined)(this.databaseNameTextbox?.value),
                    dacpacFileLocation: vscode.Uri.file(this.dacpacTextbox?.value),
                    suppressMissingDependenciesErrors: this.suppressMissingDependenciesErrorsCheckbox?.checked
                };
                referenceSettings = dacpacRef;
            }
            else { // this.currentReferencedDatabaseType === ReferencedDatabaseType.nupkg
                const nupkgRef = {
                    packageName: this.nupkgNameTextbox?.value,
                    packageVersion: this.nupkgVersionTextbox?.value,
                    suppressMissingDependenciesErrors: this.suppressMissingDependenciesErrorsCheckbox?.checked
                };
                referenceSettings = nupkgRef;
            }
            const dbServerValues = {
                dbName: this.databaseNameTextbox?.value,
                dbVariable: this.databaseVariableTextbox?.value,
                serverName: this.serverNameTextbox?.value,
                serverVariable: this.serverVariableTextbox?.value
            };
            (0, utils_1.populateResultWithVars)(referenceSettings, dbServerValues);
        }
        telemetry_1.TelemetryReporter.createActionEvent(telemetry_1.TelemetryViews.ProjectTree, telemetry_1.TelemetryActions.addDatabaseReference)
            .withAdditionalProperties({ referencedDatabaseType: this.currentReferencedDatabaseType.toString() })
            .send();
        await this.addReference(this.project, referenceSettings);
        this.dispose();
    }
    createReferenceTypeRadioButtons() {
        this.projectRadioButton = this.view.modelBuilder.radioButton()
            .withProps({
            name: 'referencedDatabaseType',
            label: constants.projectLabel
        }).component();
        this.projectRadioButton.onDidChangeCheckedState((checked) => {
            if (checked) {
                this.projectRadioButtonClick();
            }
        });
        this.systemDatabaseRadioButton = this.view.modelBuilder.radioButton()
            .withProps({
            name: 'referencedDatabaseType',
            label: constants.systemDatabase
        }).component();
        this.systemDatabaseRadioButton.onDidChangeCheckedState((checked) => {
            if (checked) {
                this.systemDbRadioButtonClick();
            }
        });
        const dacpacRadioButton = this.view.modelBuilder.radioButton()
            .withProps({
            name: 'referencedDatabaseType',
            label: constants.dacpacText
        }).component();
        dacpacRadioButton.onDidChangeCheckedState((checked) => {
            if (checked) {
                this.dacpacRadioButtonClick();
            }
        });
        const nupkgRadioButton = this.view.modelBuilder.radioButton()
            .withProps({
            name: 'referencedDatabaseType',
            label: constants.nupkgText
        }).component();
        nupkgRadioButton.onDidChangeCheckedState((checked) => {
            if (checked) {
                this.nupkgRadioButtonClick();
            }
        });
        if (this.projectDropdown?.values?.length) {
            this.projectRadioButton.checked = true;
            this.currentReferencedDatabaseType = ReferencedDatabaseType.project;
        }
        else {
            this.systemDatabaseRadioButton.checked = true;
            this.currentReferencedDatabaseType = ReferencedDatabaseType.systemDb;
            // disable projects radio button if there aren't any projects that can be added as a reference
            this.projectRadioButton.enabled = false;
        }
        const radioButtons = [this.projectRadioButton, this.systemDatabaseRadioButton, dacpacRadioButton];
        // only add the nupkg radio button for SDK-style projects
        if (this.project.sqlProjStyle === 0 /* ProjectType.SdkStyle */) {
            radioButtons.push(nupkgRadioButton);
        }
        let flexRadioButtonsModel = this.view.modelBuilder.flexContainer()
            .withLayout({ flexFlow: 'column' })
            .withItems(radioButtons)
            .withProps({ ariaRole: 'radiogroup', ariaLabel: constants.referenceRadioButtonsGroupTitle })
            .component();
        return {
            component: flexRadioButtonsModel,
            title: constants.referenceRadioButtonsGroupTitle
        };
    }
    createSystemDbReferenceTypeRadioButtons() {
        this.systemDatabasePackageRefRadioButton = this.view.modelBuilder.radioButton()
            .withProps({
            name: 'systemDbRefType',
            label: constants.packageReference
        }).component();
        this.systemDatabasePackageRefRadioButton.onDidChangeCheckedState((checked) => {
            if (checked) {
                this.systemDbRefType = 1 /* SystemDbReferenceType.PackageReference */;
            }
        });
        this.systemDatabaseArtifactRefRadioButton = this.view.modelBuilder.radioButton()
            .withProps({
            name: 'systemDbRefType',
            label: constants.artifactReference
        }).component();
        this.systemDatabaseArtifactRefRadioButton.onDidChangeCheckedState((checked) => {
            if (checked) {
                this.systemDbRefType = 0 /* SystemDbReferenceType.ArtifactReference */;
            }
        });
        const radioButtons = [this.systemDatabasePackageRefRadioButton, this.systemDatabaseArtifactRefRadioButton];
        const flexRadioButtonsModel = this.view.modelBuilder.flexContainer()
            .withLayout({ flexFlow: 'column' })
            .withItems(radioButtons)
            .withProps({ ariaRole: 'radiogroup', ariaLabel: constants.referenceTypeRadioButtonsGroupTitle })
            .component();
        // default to PackageReference for SDK-style projects
        this.systemDatabasePackageRefRadioButton.checked = true;
        return {
            component: flexRadioButtonsModel,
            title: constants.referenceTypeRadioButtonsGroupTitle
        };
    }
    insertSystemDatabaseReferenceTypeComponent() {
        // add the radio buttons to choose ArtifactReference or PackageReference if it's an SDK-syle project
        if (this.project.sqlProjStyle === 0 /* ProjectType.SdkStyle */) {
            this.formBuilder.insertFormItem(this.systemDbRefRadioButtonsComponent, 3);
            this.systemDbRefType = 1 /* SystemDbReferenceType.PackageReference */;
        }
    }
    projectRadioButtonClick() {
        this.formBuilder.removeFormItem(this.dacpacFormComponent);
        this.formBuilder.removeFormItem(this.systemDatabaseFormComponent);
        this.formBuilder.removeFormItem(this.nupkgFormComponent);
        this.formBuilder.removeFormItem(this.systemDbRefRadioButtonsComponent);
        this.formBuilder.insertFormItem(this.projectFormComponent, 2);
        this.locationDropdown.values = constants.locationDropdownValues;
        this.currentReferencedDatabaseType = ReferencedDatabaseType.project;
        this.updateEnabledInputBoxes();
        this.tryEnableAddReferenceButton();
        this.updateExampleUsage();
    }
    systemDbRadioButtonClick() {
        this.formBuilder.removeFormItem(this.dacpacFormComponent);
        this.formBuilder.removeFormItem(this.projectFormComponent);
        this.formBuilder.removeFormItem(this.nupkgFormComponent);
        this.formBuilder.insertFormItem(this.systemDatabaseFormComponent, 2);
        this.insertSystemDatabaseReferenceTypeComponent();
        // update dropdown values because only different database, same server is a valid location for system db references
        this.locationDropdown.values = constants.systemDbLocationDropdownValues;
        this.locationDropdown.value = constants.differentDbSameServer;
        this.currentReferencedDatabaseType = ReferencedDatabaseType.systemDb;
        this.updateEnabledInputBoxes();
        this.tryEnableAddReferenceButton();
        this.updateExampleUsage();
    }
    dacpacRadioButtonClick() {
        this.formBuilder.removeFormItem(this.systemDatabaseFormComponent);
        this.formBuilder.removeFormItem(this.projectFormComponent);
        this.formBuilder.removeFormItem(this.nupkgFormComponent);
        this.formBuilder.removeFormItem(this.systemDbRefRadioButtonsComponent);
        this.formBuilder.insertFormItem(this.dacpacFormComponent, 2);
        this.locationDropdown.values = constants.locationDropdownValues;
        this.currentReferencedDatabaseType = ReferencedDatabaseType.dacpac;
        this.updateEnabledInputBoxes();
        this.tryEnableAddReferenceButton();
        this.updateExampleUsage();
    }
    nupkgRadioButtonClick() {
        this.formBuilder.removeFormItem(this.systemDatabaseFormComponent);
        this.formBuilder.removeFormItem(this.projectFormComponent);
        this.formBuilder.removeFormItem(this.dacpacFormComponent);
        this.formBuilder.removeFormItem(this.systemDbRefRadioButtonsComponent);
        this.formBuilder.insertFormItem(this.nupkgFormComponent, 2);
        this.locationDropdown.values = constants.locationDropdownValues;
        this.currentReferencedDatabaseType = ReferencedDatabaseType.nupkg;
        this.updateEnabledInputBoxes();
        this.tryEnableAddReferenceButton();
        this.updateExampleUsage();
    }
    async createProjectDropdown() {
        this.projectDropdown = this.view.modelBuilder.dropDown().withProps({
            ariaLabel: constants.databaseProject,
            required: true
        }).component();
        this.projectDropdown.onValueChanged(() => {
            this.setDefaultDatabaseValues();
        });
        // get projects in workspace and filter to only sql projects
        let projectFiles = await utils.getSqlProjectsInWorkspace();
        // filter out current project
        projectFiles = projectFiles.filter(p => p.fsPath !== this.project.projectFilePath);
        this.projectDropdown.values = projectFiles.map(p => path.parse(p.fsPath).name);
        return {
            component: this.projectDropdown,
            title: constants.databaseProject
        };
    }
    createSystemDatabaseDropdown() {
        this.systemDatabaseDropdown = this.view.modelBuilder.dropDown().withProps({
            values: getSystemDbOptions(this.project),
            ariaLabel: constants.databaseNameLabel,
            required: true
        }).component();
        this.systemDatabaseDropdown.onValueChanged(() => {
            this.setDefaultDatabaseValues();
        });
        return {
            component: this.systemDatabaseDropdown,
            title: constants.databaseNameLabel
        };
    }
    createDacpacTextbox() {
        this.dacpacTextbox = this.view.modelBuilder.inputBox().withProps({
            ariaLabel: constants.dacpacText,
            placeHolder: constants.selectDacpac,
            width: '400px',
            required: true
        }).component();
        this.dacpacTextbox.onTextChanged(() => {
            this.setDefaultDatabaseValues();
            this.tryEnableAddReferenceButton();
            this.updateExampleUsage();
        });
        const loadDacpacButton = this.createLoadDacpacButton();
        const databaseRow = this.view.modelBuilder.flexContainer().withItems([this.dacpacTextbox], { flex: '0 0 auto', CSSStyles: { 'margin-right': '10px' } }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        databaseRow.insertItem(loadDacpacButton, 1);
        return {
            component: databaseRow,
            title: constants.dacpacText
        };
    }
    createNupkgFormComponentGroup() {
        this.nupkgNameTextbox = this.view.modelBuilder.inputBox().withProps({
            ariaLabel: constants.nupkgText,
            placeHolder: constants.nupkgNamePlaceholder,
            required: true
        }).component();
        this.nupkgVersionTextbox = this.view.modelBuilder.inputBox().withProps({
            ariaLabel: constants.version,
            placeHolder: constants.versionPlaceholder,
            required: true
        }).component();
        return {
            components: [
                {
                    title: constants.nupkgText,
                    component: this.nupkgNameTextbox
                },
                {
                    title: constants.version,
                    component: this.nupkgVersionTextbox
                }
            ],
            title: ''
        };
    }
    createLoadDacpacButton() {
        const loadDacpacButton = this.view.modelBuilder.button().withProps({
            ariaLabel: constants.selectDacpac,
            iconPath: iconHelper_1.IconPathHelper.folder_blue,
            height: '18px',
            width: '18px'
        }).component();
        loadDacpacButton.onDidClick(async () => {
            let fileUris = await promptDacpacLocation();
            if (!fileUris || fileUris.length === 0) {
                return;
            }
            this.dacpacTextbox.value = fileUris[0].fsPath;
        });
        return loadDacpacButton;
    }
    createLocationDropdown() {
        this.locationDropdown = this.view.modelBuilder.dropDown().withProps({
            ariaLabel: constants.location,
            values: this.currentReferencedDatabaseType === ReferencedDatabaseType.systemDb ? constants.systemDbLocationDropdownValues : constants.locationDropdownValues
        }).component();
        this.locationDropdown.value = constants.differentDbSameServer;
        this.locationDropdown.onValueChanged(() => {
            this.updateEnabledInputBoxes();
            this.tryEnableAddReferenceButton();
            this.updateExampleUsage();
        });
        return {
            component: this.locationDropdown,
            title: constants.location
        };
    }
    /**
     * Update the enabled input boxes based on what the location of the database reference selected in the dropdown is
     */
    updateEnabledInputBoxes() {
        const isSystemDb = this.currentReferencedDatabaseType === ReferencedDatabaseType.systemDb;
        if (this.locationDropdown?.value === constants.sameDatabase) {
            this.databaseNameTextbox.enabled = false;
            this.databaseVariableTextbox.enabled = false;
            this.serverNameTextbox.enabled = false;
            this.serverVariableTextbox.enabled = false;
            // update required property of the the textbox
            this.databaseNameTextbox.required = false;
            this.serverNameTextbox.required = false;
            this.serverVariableTextbox.required = false;
            // update required indicator
            this.databaseNameTextboxLabel.requiredIndicator = false;
            this.serverNameTextboxLabel.requiredIndicator = false;
            this.serverVariableTextboxLabel.requiredIndicator = false;
            // clear values in disabled fields
            this.databaseNameTextbox.value = '';
            this.databaseVariableTextbox.value = '';
            this.serverNameTextbox.value = '';
            this.serverVariableTextbox.value = '';
        }
        else if (this.locationDropdown?.value === constants.differentDbSameServer) {
            this.databaseNameTextbox.enabled = true;
            this.databaseVariableTextbox.enabled = !isSystemDb; // database variable is only enabled for non-system database references
            this.serverNameTextbox.enabled = false;
            this.serverVariableTextbox.enabled = false;
            // update required property of the the textbox
            this.databaseNameTextbox.required = true;
            this.serverNameTextbox.required = false;
            this.serverVariableTextbox.required = false;
            // update required indicator
            this.databaseNameTextboxLabel.requiredIndicator = true;
            this.serverNameTextboxLabel.requiredIndicator = false;
            this.serverVariableTextboxLabel.requiredIndicator = false;
            // clear values in disabled fields
            this.databaseVariableTextbox.value = isSystemDb ? '' : this.databaseVariableTextbox.value;
            this.serverNameTextbox.value = '';
            this.serverVariableTextbox.value = '';
            // add default values in enabled fields
            this.setDefaultDatabaseValues();
        }
        else if (this.locationDropdown?.value === constants.differentDbDifferentServer) {
            this.databaseNameTextbox.enabled = true;
            this.databaseVariableTextbox.enabled = true;
            this.serverNameTextbox.enabled = true;
            this.serverVariableTextbox.enabled = true;
            // update required property of the the textbox
            this.databaseNameTextbox.required = true;
            this.serverNameTextbox.required = true;
            this.serverVariableTextbox.required = true;
            // update required indicator
            this.databaseNameTextboxLabel.requiredIndicator = true;
            this.serverNameTextboxLabel.requiredIndicator = true;
            this.serverVariableTextboxLabel.requiredIndicator = true;
            // add default values in enabled fields
            this.setDefaultDatabaseValues();
            this.serverNameTextbox.value = constants.otherServer;
            this.serverVariableTextbox.value = constants.otherSeverVariable;
        }
    }
    /**
     * Sets the default values in the database name and variable text boxes if they are enabled
     */
    setDefaultDatabaseValues() {
        if (this.databaseNameTextbox.enabled) {
            switch (this.currentReferencedDatabaseType) {
                case ReferencedDatabaseType.project: {
                    this.databaseNameTextbox.value = this.projectDropdown?.value;
                    this.databaseVariableTextbox.value = `${this.projectDropdown?.value}`;
                    break;
                }
                case ReferencedDatabaseType.systemDb: {
                    this.databaseNameTextbox.value = this.systemDatabaseDropdown?.value;
                    break;
                }
                case ReferencedDatabaseType.dacpac: {
                    const dacpacName = this.dacpacTextbox.value ? path.parse(this.dacpacTextbox.value).name : '';
                    this.databaseNameTextbox.value = dacpacName;
                    this.databaseVariableTextbox.value = dacpacName ? `${dacpacName}` : '';
                    break;
                }
                case ReferencedDatabaseType.nupkg: {
                    const nupkgName = this.nupkgNameTextbox.value ? path.parse(this.nupkgNameTextbox.value).name : '';
                    this.databaseNameTextbox.value = nupkgName;
                    this.databaseVariableTextbox.value = nupkgName ? `${nupkgName}` : '';
                    break;
                }
            }
        }
    }
    createVariableSection() {
        // database name row
        this.databaseNameTextboxLabel = this.createLabel(constants.databaseName, true);
        this.databaseNameTextbox = this.createInputBox(constants.databaseName, true, true);
        const databaseNameRow = this.view.modelBuilder.flexContainer().withItems([this.databaseNameTextboxLabel, this.databaseNameTextbox], { flex: '0 0 auto' }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        // database variable row
        this.databaseVariableTextbox = this.createInputBox(constants.databaseVariable, false, false);
        const databaseVariableRow = this.view.modelBuilder.flexContainer().withItems([this.createLabel(constants.databaseVariable), this.databaseVariableTextbox], { flex: '0 0 auto' }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        // server name row
        this.serverNameTextboxLabel = this.createLabel(constants.serverName, false);
        this.serverNameTextbox = this.createInputBox(constants.serverName, false, false);
        const serverNameRow = this.view.modelBuilder.flexContainer().withItems([this.serverNameTextboxLabel, this.serverNameTextbox], { flex: '0 0 auto' }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        // server variable row
        this.serverVariableTextboxLabel = this.createLabel(constants.serverVariable, false);
        this.serverVariableTextbox = this.createInputBox(constants.serverVariable, false, false);
        const serverVariableRow = this.view.modelBuilder.flexContainer().withItems([this.serverVariableTextboxLabel, this.serverVariableTextbox], { flex: '0 0 auto' }).withLayout({ flexFlow: 'row', alignItems: 'center' }).component();
        const variableSection = this.view.modelBuilder.flexContainer().withItems([databaseNameRow, databaseVariableRow, serverNameRow, serverVariableRow]).withLayout({ flexFlow: 'column' }).withProps({ CSSStyles: { 'margin-bottom': '25px' } }).component();
        this.setDefaultDatabaseValues();
        return {
            component: variableSection,
            title: ''
        };
    }
    createLabel(value, required = false) {
        const label = this.view.modelBuilder.text().withProps({
            value: value,
            width: uiConstants_1.cssStyles.addDatabaseReferenceDialogLabelWidth,
            requiredIndicator: required
        }).component();
        return label;
    }
    createInputBox(ariaLabel, enabled, required) {
        const inputBox = this.view.modelBuilder.inputBox().withProps({
            ariaLabel: ariaLabel,
            enabled: enabled,
            width: uiConstants_1.cssStyles.addDatabaseReferenceInputboxWidth,
            required: required
        }).component();
        inputBox.onTextChanged(() => {
            this.tryEnableAddReferenceButton();
            this.updateExampleUsage();
        });
        return inputBox;
    }
    createExampleUsage() {
        this.exampleUsage = this.view.modelBuilder.text().withProps({
            value: this.currentReferencedDatabaseType === ReferencedDatabaseType.project ? constants.databaseNameRequiredVariableOptional : constants.systemDatabaseReferenceRequired,
            CSSStyles: { 'user-select': 'text' }
        }).component();
        const exampleUsageWrapper = this.view.modelBuilder.flexContainer().withItems([this.exampleUsage], { CSSStyles: { 'width': '415px', 'height': '80px', 'padding': '0 10px', 'border': '1px solid #8a8886', 'font-style': 'italic' } }).component();
        return {
            component: exampleUsageWrapper,
            title: constants.exampleUsage
        };
    }
    updateExampleUsage() {
        let newText = '';
        let fontStyle = uiConstants_1.cssStyles.fontStyle.normal; // font-style should be normal for example usage and italics if showing message that a required field needs to be filled
        switch (this.locationDropdown.value) {
            case constants.sameDatabase: {
                newText = constants.sameDatabaseExampleUsage;
                break;
            }
            case constants.differentDbSameServer: {
                if (!this.databaseNameTextbox?.value) {
                    newText = this.currentReferencedDatabaseType === ReferencedDatabaseType.systemDb ? constants.enterSystemDbName : constants.databaseNameRequiredVariableOptional;
                    fontStyle = uiConstants_1.cssStyles.fontStyle.italics;
                }
                else {
                    const db = this.databaseVariableTextbox?.value ? utils.formatSqlCmdVariable(this.databaseVariableTextbox?.value) : this.databaseNameTextbox.value;
                    newText = constants.differentDbSameServerExampleUsage(db);
                }
                break;
            }
            case constants.differentDbDifferentServer: {
                if (!this.databaseNameTextbox?.value || !this.serverNameTextbox?.value || !this.serverVariableTextbox?.value) {
                    newText = constants.databaseNameServerNameVariableRequired;
                    fontStyle = uiConstants_1.cssStyles.fontStyle.italics;
                }
                else {
                    const server = utils.formatSqlCmdVariable(this.serverVariableTextbox.value);
                    const db = this.databaseVariableTextbox?.value ? utils.formatSqlCmdVariable(this.databaseVariableTextbox?.value) : this.databaseNameTextbox.value;
                    newText = constants.differentDbDifferentServerExampleUsage(server, db);
                }
                break;
            }
        }
        // check for invalid variables
        if (!this.validSqlCmdVariables()) {
            newText = utils.validateSqlCmdVariableName(this.databaseVariableTextbox?.value) ?? utils.validateSqlCmdVariableName(this.serverVariableTextbox.value);
        }
        this.exampleUsage.value = newText;
        void this.exampleUsage?.updateCssStyles({ 'font-style': fontStyle });
    }
    validSqlCmdVariables() {
        if (this.databaseVariableTextbox?.enabled && this.databaseVariableTextbox?.value && utils.validateSqlCmdVariableName(this.databaseVariableTextbox?.value)
            || this.serverVariableTextbox?.enabled && this.serverVariableTextbox?.value && utils.validateSqlCmdVariableName(this.serverVariableTextbox?.value)) {
            return false;
        }
        return true;
    }
    /**
     * Only enable Add reference button if all enabled fields are filled
     */
    tryEnableAddReferenceButton() {
        switch (this.currentReferencedDatabaseType) {
            case ReferencedDatabaseType.project: {
                this.dialog.okButton.enabled = this.projectRequiredFieldsFilled();
                break;
            }
            case ReferencedDatabaseType.systemDb: {
                this.dialog.okButton.enabled = !!this.databaseNameTextbox?.value;
                break;
            }
            case ReferencedDatabaseType.dacpac: {
                this.dialog.okButton.enabled = this.dacpacRequiredFieldsFilled();
                break;
            }
            case ReferencedDatabaseType.nupkg: {
                this.dialog.okButton.enabled = this.nupkgRequiredFieldsFilled();
                break;
            }
        }
    }
    dacpacRequiredFieldsFilled() {
        return !!this.dacpacTextbox?.value
            && this.validSqlCmdVariables()
            && ((this.locationDropdown?.value === constants.sameDatabase)
                || (this.locationDropdown?.value === constants.differentDbSameServer && this.differentDatabaseSameServerRequiredFieldsFilled())
                || ((this.locationDropdown?.value === constants.differentDbDifferentServer && this.differentDatabaseDifferentServerRequiredFieldsFilled())));
    }
    projectRequiredFieldsFilled() {
        return !!this.projectDropdown?.value &&
            ((this.locationDropdown?.value === constants.sameDatabase)
                || (this.locationDropdown?.value === constants.differentDbSameServer && this.differentDatabaseSameServerRequiredFieldsFilled())
                || ((this.locationDropdown?.value === constants.differentDbDifferentServer && this.differentDatabaseDifferentServerRequiredFieldsFilled())));
    }
    nupkgRequiredFieldsFilled() {
        return !!this.nupkgNameTextbox?.value
            && !!this.nupkgVersionTextbox?.value
            && ((this.locationDropdown?.value === constants.sameDatabase)
                || (this.locationDropdown?.value === constants.differentDbSameServer && this.differentDatabaseSameServerRequiredFieldsFilled())
                || ((this.locationDropdown?.value === constants.differentDbDifferentServer && this.differentDatabaseDifferentServerRequiredFieldsFilled())));
    }
    differentDatabaseSameServerRequiredFieldsFilled() {
        return !!this.databaseNameTextbox?.value;
    }
    differentDatabaseDifferentServerRequiredFieldsFilled() {
        return !!this.databaseNameTextbox?.value && !!this.serverNameTextbox?.value && !!this.serverVariableTextbox?.value;
    }
}
exports.AddDatabaseReferenceDialog = AddDatabaseReferenceDialog;
function getSystemDbOptions(project) {
    const projectTargetVersion = project.getProjectTargetVersion().toLowerCase();
    // only master is a valid system db reference for projects targeting Azure and DW
    if (projectTargetVersion.includes('azure') || projectTargetVersion.includes('dw')) {
        return [constants.master];
    }
    return [constants.master, constants.msdb];
}
async function promptDacpacLocation() {
    return await vscode.window.showOpenDialog({
        canSelectFiles: true,
        canSelectFolders: false,
        canSelectMany: false,
        defaultUri: vscode.workspace.workspaceFolders ? vscode.workspace.workspaceFolders[0].uri : undefined,
        openLabel: constants.selectString,
        title: constants.selectDacpac,
        filters: {
            [constants.dacpacFiles]: ['dacpac'],
        }
    });
}
//# sourceMappingURL=addDatabaseReferenceDialog.js.map