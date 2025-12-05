"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const should = require("should");
const azdata = require("azdata");
const sinon = require("sinon");
const utils = require("../../common/utils");
const newProjectTool = require("../../tools/newProjectTool");
const createProjectFromDatabaseDialog_1 = require("../../dialogs/createProjectFromDatabaseDialog");
const testContext_1 = require("../testContext");
describe('Create Project From Database Dialog', () => {
    afterEach(function () {
        sinon.restore();
    });
    it('Should open dialog successfully', async function () {
        sinon.stub(azdata.connection, 'getConnections').resolves([]);
        sinon.stub(azdata.connection, 'connect').resolves({ connected: true, connectionId: '0', errorMessage: '', errorCode: 0 });
        sinon.stub(azdata.connection, 'listDatabases').resolves([]);
        const dialog = new createProjectFromDatabaseDialog_1.CreateProjectFromDatabaseDialog(testContext_1.mockConnectionProfile);
        await dialog.openDialog();
        should.notEqual(dialog.createProjectFromDatabaseTab, undefined);
    });
    it('Should enable ok button correctly with a connection profile', async function () {
        sinon.stub(azdata.connection, 'getConnections').resolves([]);
        sinon.stub(azdata.connection, 'connect').resolves({ connected: true, connectionId: '0', errorMessage: '', errorCode: 0 });
        sinon.stub(azdata.connection, 'listDatabases').resolves([]);
        const dialog = new createProjectFromDatabaseDialog_1.CreateProjectFromDatabaseDialog(testContext_1.mockConnectionProfile);
        await dialog.openDialog(); // should set connection details
        should(dialog.dialog.okButton.enabled).equal(false);
        // fill in project name and ok button should not be enabled
        dialog.projectNameTextBox.value = 'testProject';
        dialog.tryEnableCreateButton();
        should(dialog.dialog.okButton.enabled).equal(false, 'Ok button should not be enabled because project location is not filled');
        // fill in project location and ok button should be enabled
        dialog.projectLocationTextBox.value = 'testLocation';
        dialog.tryEnableCreateButton();
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled since all the required fields are filled');
    });
    it('Should enable ok button correctly without a connection profile', async function () {
        const dialog = new createProjectFromDatabaseDialog_1.CreateProjectFromDatabaseDialog(undefined);
        await dialog.openDialog();
        should(dialog.dialog.okButton.enabled).equal(false, 'Ok button should not be enabled because all the required details are not filled');
        // fill in project name and ok button should not be enabled
        dialog.projectNameTextBox.value = 'testProject';
        dialog.tryEnableCreateButton();
        should(dialog.dialog.okButton.enabled).equal(false, 'Ok button should not be enabled because source database details and project location are not filled');
        // fill in project location and ok button not should be enabled
        dialog.projectLocationTextBox.value = 'testLocation';
        dialog.tryEnableCreateButton();
        should(dialog.dialog.okButton.enabled).equal(false, 'Ok button should not be enabled because source database details are not filled');
        // fill in server name and ok button not should be enabled
        dialog.sourceConnectionTextBox.value = 'testServer';
        dialog.tryEnableCreateButton();
        should(dialog.dialog.okButton.enabled).equal(false, 'Ok button should not be enabled because source database is not filled');
        // fill in database name and ok button should be enabled
        dialog.sourceDatabaseDropDown.value = 'testDatabase';
        dialog.tryEnableCreateButton();
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled since all the required fields are filled');
        // update folder structure information and ok button should still be enabled
        dialog.folderStructureDropDown.value = 'Object Type';
        dialog.tryEnableCreateButton();
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled since all the required fields are filled');
    });
    it('Should create default project name correctly when database information is populated', async function () {
        sinon.stub(azdata.connection, 'getConnections').resolves([]);
        sinon.stub(azdata.connection, 'connect').resolves({ connected: true, connectionId: '0', errorMessage: '', errorCode: 0 });
        sinon.stub(azdata.connection, 'listDatabases').resolves(['My Database']);
        sinon.stub(utils, 'sanitizeStringForFilename').returns('My Database');
        sinon.stub(newProjectTool, 'defaultProjectNameFromDb').returns('DatabaseProjectMy Database');
        const dialog = new createProjectFromDatabaseDialog_1.CreateProjectFromDatabaseDialog(testContext_1.mockConnectionProfile);
        await dialog.openDialog();
        dialog.setProjectName();
        should.equal(dialog.projectNameTextBox.value, 'DatabaseProjectMy Database');
    });
    it('Should include all info in import data model and connect to appropriate call back properties', async function () {
        const stubUri = 'My URI';
        const dialog = new createProjectFromDatabaseDialog_1.CreateProjectFromDatabaseDialog(testContext_1.mockConnectionProfile);
        sinon.stub(azdata.connection, 'getConnections').resolves([]);
        sinon.stub(azdata.connection, 'connect').resolves({ connected: true, connectionId: '0', errorMessage: '', errorCode: 0 });
        sinon.stub(azdata.connection, 'listDatabases').resolves(['My Database']);
        sinon.stub(azdata.connection, 'getUriForConnection').resolves(stubUri);
        await dialog.openDialog();
        dialog.projectNameTextBox.value = 'testProject';
        dialog.projectLocationTextBox.value = 'testLocation';
        let model;
        const expectedImportDataModel = {
            connectionUri: stubUri,
            database: 'My Database',
            projName: 'testProject',
            filePath: 'testLocation',
            version: '1.0.0.0',
            extractTarget: 5 /* mssql.ExtractTarget.schemaObjectType */,
            sdkStyle: true,
            includePermissions: undefined
        };
        dialog.createProjectFromDatabaseCallback = (m) => { model = m; };
        await dialog.handleCreateButtonClick();
        should(model).deepEqual(expectedImportDataModel);
    });
});
//# sourceMappingURL=createProjectFromDatabaseDialog.test.js.map