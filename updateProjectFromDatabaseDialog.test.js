"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const azdata = require("azdata");
const should = require("should");
const sinon = require("sinon");
const vscode = require("vscode");
const baselines = require("../baselines/baselines");
const testUtils = require("../testUtils");
const updateProjectFromDatabaseDialog_1 = require("../../dialogs/updateProjectFromDatabaseDialog");
const testContext_1 = require("../testContext");
describe('Update Project From Database Dialog', () => {
    before(async function () {
        await baselines.loadBaselines();
    });
    afterEach(function () {
        sinon.restore();
    });
    after(async function () {
        await testUtils.deleteGeneratedTestFolder();
    });
    it('Should populate endpoints correctly when no context passed', async function () {
        const dialog = new updateProjectFromDatabaseDialog_1.UpdateProjectFromDatabaseDialog(undefined, undefined, []);
        await dialog.openDialog();
        should.equal(dialog.serverDropdown.value, undefined, `Server dropdown should not be populated, but instead was "${dialog.serverDropdown.value}".`);
        should.equal(dialog.databaseDropdown.value, undefined, `Database dropdown should not be populated, but instead was "${dialog.databaseDropdown.value}".`);
        should.equal(dialog.projectFileDropdown.value, '', `Project file dropdown should not be populated, but instead was "${dialog.projectFileDropdown.value}".`);
        should.equal(dialog.dialog.okButton.enabled, false, 'Okay button should be disabled.');
    });
    it('Should populate endpoints correctly when Project context is passed', async function () {
        const project = await testUtils.createTestProject(this.test, baselines.openProjectFileBaseline);
        const dialog = new updateProjectFromDatabaseDialog_1.UpdateProjectFromDatabaseDialog(undefined, project, testContext_1.mockURIList);
        await dialog.openDialog();
        should.equal(dialog.serverDropdown.value, undefined, `Server dropdown should not be populated, but instead was "${dialog.serverDropdown.value}".`);
        should.equal(dialog.databaseDropdown.value, undefined, `Database dropdown should not be populated, but instead was "${dialog.databaseDropdown.value}".`);
        should.equal(dialog.projectFileDropdown.value, project.projectFilePath, `Project file dropdown should be the sqlproj path (${project.projectFilePath}), but instead was "${dialog.projectFileDropdown.value}".`);
        should.equal(dialog.dialog.okButton.enabled, false, 'Okay button should be disabled.');
    });
    it('Should populate endpoints correctly when Connection context is passed', async function () {
        sinon.stub(azdata.connection, 'getConnections').resolves([testContext_1.mockConnectionProfile]);
        sinon.stub(azdata.connection, 'listDatabases').resolves([testContext_1.mockConnectionProfile.databaseName]);
        const profile = testContext_1.mockConnectionProfile;
        const dialog = new updateProjectFromDatabaseDialog_1.UpdateProjectFromDatabaseDialog(profile, undefined, []);
        await dialog.openDialog();
        await dialog.populatedInputsPromise;
        should.equal(dialog.serverDropdown.value.displayName, profile.options['connectionName'], `Server dropdown should be "${profile.options['connectionName']}", but instead was "${dialog.serverDropdown.value.displayName}".`);
        should.equal(dialog.databaseDropdown.value, profile.databaseName, `Database dropdown should be "${profile.databaseName}", but instead was "${dialog.databaseDropdown.value}".`);
        should.equal(dialog.projectFileDropdown.value, '', `Project file dropdown should not be populated, but instead was "${dialog.projectFileDropdown.value}".`);
        should.equal(dialog.dialog.okButton.enabled, false, 'Okay button should be disabled.');
    });
    it('Should populate endpoints correctly when context is complete', async function () {
        const project = await testUtils.createTestProject(this.test, baselines.openProjectFileBaseline);
        sinon.stub(azdata.connection, 'getConnections').resolves([testContext_1.mockConnectionProfile]);
        sinon.stub(azdata.connection, 'listDatabases').resolves([testContext_1.mockConnectionProfile.databaseName]);
        const profile = testContext_1.mockConnectionProfile;
        const dialog = new updateProjectFromDatabaseDialog_1.UpdateProjectFromDatabaseDialog(profile, project, testContext_1.mockURIList);
        await dialog.openDialog();
        await dialog.populatedInputsPromise;
        let uriList = [];
        testContext_1.mockURIList.forEach(projectUri => {
            uriList.push(projectUri.fsPath);
        });
        should.equal(dialog.serverDropdown.value.displayName, profile.options['connectionName'], `Server dropdown should be "${profile.options['connectionName']}", but instead was "${dialog.serverDropdown.value.displayName}".`);
        should.equal(dialog.databaseDropdown.value, profile.databaseName, `Database dropdown should as "${profile.databaseName}", but instead was "${dialog.databaseDropdown.value}".`);
        should.equal(dialog.projectFileDropdown.value, project.projectFilePath, `Project file dropdown should be the sqlproj path (${project.projectFilePath}), but instead was "${dialog.projectFileDropdown.value}".`);
        should.deepEqual(dialog.projectFileDropdown.values, uriList, `Project file dropdown list should be the sqlproj path (${testContext_1.mockURIList}), but instead was "${dialog.projectFileDropdown.values}".`);
        should.equal(dialog.dialog.okButton.enabled, true, 'Okay button should be enabled when dialog is complete.');
    });
    it('Should populate endpoints correctly when Connection context and workspace with projects is provided', async function () {
        sinon.stub(azdata.connection, 'getConnections').resolves([testContext_1.mockConnectionProfile]);
        sinon.stub(azdata.connection, 'listDatabases').resolves([testContext_1.mockConnectionProfile.databaseName]);
        const profile = testContext_1.mockConnectionProfile;
        const dialog = new updateProjectFromDatabaseDialog_1.UpdateProjectFromDatabaseDialog(profile, undefined, testContext_1.mockURIList);
        await dialog.openDialog();
        await dialog.populatedInputsPromise;
        let uriList = [];
        testContext_1.mockURIList.forEach(projectUri => {
            uriList.push(projectUri.fsPath);
        });
        should.equal(dialog.serverDropdown.value.displayName, profile.options['connectionName'], `Server dropdown should be "${profile.options['connectionName']}", but instead was "${dialog.serverDropdown.value.displayName}".`);
        should.equal(dialog.databaseDropdown.value, profile.databaseName, `Database dropdown should be "${profile.databaseName}", but instead was "${dialog.databaseDropdown.value}".`);
        should.equal(dialog.projectFileDropdown.value, uriList[0], `Project file dropdown should be the first project listed in the workspace URI list (${uriList[0]}), but instead was "${dialog.projectFileDropdown.value}".`);
        should.deepEqual(dialog.projectFileDropdown.values, uriList, `Project file dropdown list should be the workspace URI list (${testContext_1.mockURIList}), but instead was "${dialog.projectFileDropdown.values}".`);
        should.equal(dialog.dialog.okButton.enabled, true, 'Okay button should be enabled when dialog is complete.');
    });
    it('Should successfully complete the handleUpdateButtonClick method call and connect to appropriate call back properties when Connection context and workspace with projects is provided', async function () {
        const project = await testUtils.createTestProject(this.test, baselines.openProjectFileBaseline);
        sinon.stub(azdata.connection, 'getConnections').resolves([testContext_1.mockConnectionProfile]);
        sinon.stub(azdata.connection, 'listDatabases').resolves([testContext_1.mockConnectionProfile.databaseName]);
        sinon.stub(azdata.connection, 'getUriForConnection').resolves('MockUri');
        sinon.stub(azdata.connection, 'getCredentials').resolves({ ['credentials']: 'credentials' });
        const projectFilePath = project.projectFilePath.toLowerCase();
        const profile = testContext_1.mockConnectionProfile;
        testContext_1.mockURIList.unshift(vscode.Uri.file(projectFilePath));
        const dialog = new updateProjectFromDatabaseDialog_1.UpdateProjectFromDatabaseDialog(profile, undefined, testContext_1.mockURIList);
        await dialog.openDialog();
        await dialog.populatedInputsPromise;
        let uriList = [];
        testContext_1.mockURIList.forEach(projectUri => {
            uriList.push(projectUri.fsPath);
        });
        // verify the handleUpdateButtonClick method goes through successfully
        let model;
        const testProjectEndpointInfo = { ...testContext_1.mockProjectEndpointInfo };
        testProjectEndpointInfo.projectFilePath = projectFilePath;
        const expectedUpdateProjectDataModel = {
            sourceEndpointInfo: testContext_1.mockDatabaseEndpointInfo,
            targetEndpointInfo: testProjectEndpointInfo,
            action: 0
        };
        dialog.updateProjectFromDatabaseCallback = (m) => { model = m; };
        await dialog.handleUpdateButtonClick();
        should(model).deepEqual(expectedUpdateProjectDataModel);
    });
});
//# sourceMappingURL=updateProjectFromDatabaseDialog.test.js.map