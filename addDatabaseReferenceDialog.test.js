"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const should = require("should");
const path = require("path");
const sinon = require("sinon");
const vscode = require("vscode");
const TypeMoq = require("typemoq");
const baselines = require("../baselines/baselines");
const templates = require("../../templates/templates");
const testUtils = require("../testUtils");
const constants = require("../../common/constants");
const addDatabaseReferenceDialog_1 = require("../../dialogs/addDatabaseReferenceDialog");
describe('Add Database Reference Dialog', () => {
    before(async function () {
        await templates.loadTemplates(path.join(__dirname, '..', '..', '..', 'resources', 'templates'));
        await baselines.loadBaselines();
    });
    beforeEach(function () {
        // const dataWorkspaceMock = TypeMoq.Mock.ofType<dataworkspace.IExtension>();
        // dataWorkspaceMock.setup(x => x.getProjectsInWorkspace(TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.resolve([]));
        // sinon.stub(vscode.extensions, 'getExtension').withArgs('Microsoft.data-workspace').returns(<any>{ exports: dataWorkspaceMock.object });
    });
    afterEach(function () {
        sinon.restore();
    });
    after(async function () {
        await testUtils.deleteGeneratedTestFolder();
    });
    it('Should open dialog successfully', async function () {
        const project = await testUtils.createTestProject(this.test, baselines.newProjectFileBaseline);
        const dataWorkspaceMock = TypeMoq.Mock.ofType();
        dataWorkspaceMock.setup(x => x.getProjectsInWorkspace(TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.resolve([]));
        sinon.stub(vscode.extensions, 'getExtension').withArgs('Microsoft.data-workspace').returns({ exports: dataWorkspaceMock.object });
        const dialog = new addDatabaseReferenceDialog_1.AddDatabaseReferenceDialog(project);
        await dialog.openDialog();
        should.notEqual(dialog.addDatabaseReferenceTab, undefined);
    });
    it('Should enable ok button correctly', async function () {
        const project = await testUtils.createTestProject(this.test, baselines.newProjectFileBaseline);
        const dataWorkspaceMock = TypeMoq.Mock.ofType();
        dataWorkspaceMock.setup(x => x.getProjectsInWorkspace(TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.resolve([]));
        sinon.stub(vscode.extensions, 'getExtension').withArgs('Microsoft.data-workspace').returns({ exports: dataWorkspaceMock.object });
        const dialog = new addDatabaseReferenceDialog_1.AddDatabaseReferenceDialog(project);
        await dialog.openDialog();
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled since initial type of systemDb has default values filled');
        should(dialog.currentReferencedDatabaseType).equal(addDatabaseReferenceDialog_1.ReferencedDatabaseType.systemDb);
        // empty db name textbox
        dialog.databaseNameTextbox.value = '';
        dialog.tryEnableAddReferenceButton();
        should(dialog.dialog.okButton.enabled).equal(false, 'Ok button should be disabled after clearing the database name textbox');
        // fill in db name and ok button should be enabled
        dialog.databaseNameTextbox.value = 'master';
        dialog.tryEnableAddReferenceButton();
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled after the database name textbox is filled');
        // change to dacpac reference
        dialog.dacpacRadioButtonClick();
        should(dialog.currentReferencedDatabaseType).equal(addDatabaseReferenceDialog_1.ReferencedDatabaseType.dacpac);
        should(dialog.locationDropdown?.value).equal(constants.differentDbSameServer);
        should(dialog.databaseNameTextbox.value).equal('', 'database name text box should be empty because no dacpac has been selected');
        should(dialog.dialog.okButton.enabled).equal(false, 'Ok button should not be enabled because dacpac input box is not filled');
        // fill in dacpac textbox and database name text box
        dialog.dacpacTextbox.value = 'testDb.dacpac';
        dialog.databaseNameTextbox.value = 'testDb';
        dialog.tryEnableAddReferenceButton();
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled after the dacpac textbox is filled');
        // change location to different database, different server
        dialog.locationDropdown.value = constants.differentDbDifferentServer;
        dialog.updateEnabledInputBoxes();
        dialog.tryEnableAddReferenceButton();
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled because server fields are filled');
        // change location to same database
        dialog.locationDropdown.value = constants.sameDatabase;
        dialog.updateEnabledInputBoxes();
        dialog.tryEnableAddReferenceButton();
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled because only dacpac location is needed for a reference located on the same database');
        // switch to project
        dialog.projectRadioButtonClick();
        should(dialog.dialog.okButton.enabled).equal(false, 'Ok button should not be enabled because there are no projects in the dropdown');
        // change reference type back to system db
        dialog.systemDbRadioButtonClick();
        should(dialog.locationDropdown?.value).equal(constants.differentDbSameServer);
        should(dialog.databaseNameTextbox?.value).equal('master', `Database name textbox should be set to master. Actual:${dialog.databaseNameTextbox?.value}`);
        should(dialog.dialog.okButton.enabled).equal(true, 'Ok button should be enabled because database name is filled');
    });
    it('Should enable and disable input boxes depending on the reference type', async function () {
        const project = await testUtils.createTestProject(this.test, baselines.newProjectFileBaseline);
        const dataWorkspaceMock = TypeMoq.Mock.ofType();
        dataWorkspaceMock.setup(x => x.getProjectsInWorkspace(TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.resolve([]));
        sinon.stub(vscode.extensions, 'getExtension').withArgs('Microsoft.data-workspace').returns({ exports: dataWorkspaceMock.object });
        const dialog = new addDatabaseReferenceDialog_1.AddDatabaseReferenceDialog(project);
        await dialog.openDialog();
        // dialog starts with system db because there aren't any other projects in the workspace
        should(dialog.currentReferencedDatabaseType).equal(addDatabaseReferenceDialog_1.ReferencedDatabaseType.systemDb);
        validateInputBoxEnabledStates(dialog, { databaseNameEnabled: true, databaseVariableEnabled: false, serverNameEnabled: false, serverVariabledEnabled: false });
        // change to dacpac reference
        dialog.dacpacRadioButtonClick();
        should(dialog.currentReferencedDatabaseType).equal(addDatabaseReferenceDialog_1.ReferencedDatabaseType.dacpac);
        should(dialog.locationDropdown.value).equal(constants.differentDbSameServer);
        validateInputBoxEnabledStates(dialog, { databaseNameEnabled: true, databaseVariableEnabled: true, serverNameEnabled: false, serverVariabledEnabled: false });
        // change location to different db, different server
        dialog.locationDropdown.value = constants.differentDbDifferentServer;
        dialog.updateEnabledInputBoxes();
        validateInputBoxEnabledStates(dialog, { databaseNameEnabled: true, databaseVariableEnabled: true, serverNameEnabled: true, serverVariabledEnabled: true });
        // change location to same db
        dialog.locationDropdown.value = constants.sameDatabase;
        dialog.updateEnabledInputBoxes();
        validateInputBoxEnabledStates(dialog, { databaseNameEnabled: false, databaseVariableEnabled: false, serverNameEnabled: false, serverVariabledEnabled: false });
        // change to project reference
        dialog.projectRadioButtonClick();
        should(dialog.currentReferencedDatabaseType).equal(addDatabaseReferenceDialog_1.ReferencedDatabaseType.project);
        should(dialog.locationDropdown.value).equal(constants.sameDatabase);
        validateInputBoxEnabledStates(dialog, { databaseNameEnabled: false, databaseVariableEnabled: false, serverNameEnabled: false, serverVariabledEnabled: false });
    });
});
function validateInputBoxEnabledStates(dialog, expectedStates) {
    should(dialog.databaseNameTextbox?.enabled).equal(expectedStates.databaseNameEnabled, `Database name text box should be ${expectedStates.databaseNameEnabled}. Actual: ${dialog.databaseNameTextbox?.enabled}`);
    should(dialog.databaseVariableTextbox?.enabled).equal(expectedStates.databaseVariableEnabled, `Database variable text box should be ${expectedStates.databaseVariableEnabled}. Actual: ${dialog.databaseVariableTextbox?.enabled}`);
    should(dialog.serverNameTextbox?.enabled).equal(expectedStates.serverNameEnabled, `Server name text box should be ${expectedStates.serverNameEnabled}. Actual: ${dialog.serverNameTextbox?.enabled}`);
    should(dialog.serverVariableTextbox?.enabled).equal(expectedStates.serverVariabledEnabled, `Server variable text box should be ${expectedStates.serverVariabledEnabled}. Actual: ${dialog.serverVariableTextbox?.enabled}`);
}
//# sourceMappingURL=addDatabaseReferenceDialog.test.js.map