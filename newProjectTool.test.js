"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
const should = require("should");
const TypeMoq = require("typemoq");
const sinon = require("sinon");
const newProjectTool = require("../tools/newProjectTool");
const testUtils_1 = require("./testUtils");
let previousSetting;
let testFolderPath;
describe('NewProjectTool: New project tool tests', function () {
    const projectConfigurationKey = 'projects';
    const projectSaveLocationKey = 'defaultProjectSaveLocation';
    beforeEach(async function () {
        previousSetting = await vscode.workspace.getConfiguration(projectConfigurationKey)[projectSaveLocationKey];
        testFolderPath = await (0, testUtils_1.generateTestFolderPath)(this.test);
        // set the default project folder path to the test folder
        await vscode.workspace.getConfiguration(projectConfigurationKey).update(projectSaveLocationKey, testFolderPath, true);
        const dataWorkspaceMock = TypeMoq.Mock.ofType();
        dataWorkspaceMock.setup(x => x.defaultProjectSaveLocation).returns(() => vscode.Uri.file(testFolderPath));
        sinon.stub(vscode.extensions, 'getExtension').returns({ exports: dataWorkspaceMock.object });
    });
    after(async function () {
        await (0, testUtils_1.deleteGeneratedTestFolder)();
    });
    afterEach(async function () {
        // reset the default project folder path to the previous setting
        await vscode.workspace.getConfiguration(projectConfigurationKey).update(projectSaveLocationKey, previousSetting, true);
        sinon.restore();
    });
    it('Should generate correct default project names', async function () {
        should(newProjectTool.defaultProjectNameNewProj()).equal('DatabaseProject1');
        should(newProjectTool.defaultProjectNameFromDb('master')).equal('DatabaseProjectmaster');
    });
    it('Should auto-increment default project names for new projects', async function () {
        should(newProjectTool.defaultProjectNameNewProj()).equal('DatabaseProject1');
        await (0, testUtils_1.createTestFile)(this.test, '', 'DatabaseProject1', testFolderPath);
        should(newProjectTool.defaultProjectNameNewProj()).equal('DatabaseProject2');
        await (0, testUtils_1.createTestFile)(this.test, '', 'DatabaseProject2', testFolderPath);
        should(newProjectTool.defaultProjectNameNewProj()).equal('DatabaseProject3');
    });
    it('Should auto-increment default project names for create project for database', async function () {
        should(newProjectTool.defaultProjectNameFromDb('master')).equal('DatabaseProjectmaster');
        await (0, testUtils_1.createTestFile)(this.test, '', 'DatabaseProjectmaster', testFolderPath);
        should(newProjectTool.defaultProjectNameFromDb('master')).equal('DatabaseProjectmaster2');
        await (0, testUtils_1.createTestFile)(this.test, '', 'DatabaseProjectmaster2', testFolderPath);
        should(newProjectTool.defaultProjectNameFromDb('master')).equal('DatabaseProjectmaster3');
    });
    it('Should not return a project name if undefined is passed in ', async function () {
        should(newProjectTool.defaultProjectNameFromDb(undefined)).equal('');
        should(newProjectTool.defaultProjectNameFromDb('')).equal('');
        should(newProjectTool.defaultProjectNameFromDb('test')).equal('DatabaseProjecttest');
    });
});
//# sourceMappingURL=newProjectTool.test.js.map