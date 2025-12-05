"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const should = require("should");
const path = require("path");
const vscode = require("vscode");
const baselines = require("../baselines/baselines");
const templates = require("../../templates/templates");
const testUtils = require("../testUtils");
const TypeMoq = require("typemoq");
const publishDatabaseDialog_1 = require("../../dialogs/publishDatabaseDialog");
const project_1 = require("../../models/project");
const projectController_1 = require("../../controllers/projectController");
const constants_1 = require("../../common/constants");
const testContext_1 = require("../testContext");
let testContext;
describe('Publish Database Dialog', () => {
    before(async function () {
        await templates.loadTemplates(path.join(__dirname, '..', '..', '..', 'resources', 'templates'));
        await baselines.loadBaselines();
        testContext = (0, testContext_1.createContext)();
    });
    after(async function () {
        await testUtils.deleteGeneratedTestFolder();
    });
    it('Should open dialog successfully ', async function () {
        const projController = new projectController_1.ProjectsController(testContext.outputChannel);
        const projFileDir = await testUtils.generateTestFolderPath(this.test);
        const projFilePath = await projController.createNewProject({
            newProjName: 'TestProjectName',
            folderUri: vscode.Uri.file(projFileDir),
            projectTypeId: constants_1.emptySqlDatabaseProjectTypeId,
            configureDefaultBuild: true,
            projectGuid: 'BA5EBA11-C0DE-5EA7-ACED-BABB1E70A575',
            sdkStyle: false
        });
        const project = await project_1.Project.openProject(projFilePath);
        const publishDatabaseDialog = new publishDatabaseDialog_1.PublishDatabaseDialog(project);
        publishDatabaseDialog.openDialog();
        should.notEqual(publishDatabaseDialog.publishTab, undefined);
    });
    it('Should create default database name correctly ', async function () {
        const projController = new projectController_1.ProjectsController(testContext.outputChannel);
        const projFileDir = await testUtils.generateTestFolderPath(this.test);
        const projFilePath = await projController.createNewProject({
            newProjName: 'TestProjectName',
            folderUri: vscode.Uri.file(projFileDir),
            projectTypeId: constants_1.emptySqlDatabaseProjectTypeId,
            configureDefaultBuild: true,
            projectGuid: 'BA5EBA11-C0DE-5EA7-ACED-BABB1E70A575',
            sdkStyle: false
        });
        const project = new project_1.Project(projFilePath);
        const publishDatabaseDialog = new publishDatabaseDialog_1.PublishDatabaseDialog(project);
        should.equal(publishDatabaseDialog.getDefaultDatabaseName(), project.projectFileName);
    });
    it('Should include all info in publish profile', async function () {
        const proj = await testUtils.createTestProject(this.test, baselines.openProjectFileBaseline);
        const dialog = TypeMoq.Mock.ofType(publishDatabaseDialog_1.PublishDatabaseDialog, undefined, undefined, proj);
        dialog.setup(x => x.getConnectionUri()).returns(() => { return Promise.resolve('Mock|Connection|Uri'); });
        dialog.setup(x => x.targetDatabaseName).returns(() => 'MockDatabaseName');
        dialog.setup(x => x.getSqlCmdVariablesForPublish()).returns(() => proj.sqlCmdVariables);
        dialog.setup(x => x.getDeploymentOptions()).returns(() => { return Promise.resolve(testContext_1.mockDacFxOptionsResult.deploymentOptions); });
        dialog.setup(x => x.getServerName()).returns(() => 'MockServer');
        dialog.object.publishToExistingServer = true;
        dialog.callBase = true;
        let profile;
        const expectedPublish = {
            databaseName: 'MockDatabaseName',
            serverName: 'MockServer',
            connectionUri: 'Mock|Connection|Uri',
            sqlCmdVariables: new Map([
                ['ProdDatabaseName', 'MyProdDatabase'],
                ['BackupDatabaseName', 'MyBackupDatabase']
            ]),
            deploymentOptions: testContext_1.mockDacFxOptionsResult.deploymentOptions,
            publishProfileUri: undefined
        };
        dialog.object.publish = (_, prof) => { profile = prof; };
        await dialog.object.publishClick();
        should(profile).deepEqual(expectedPublish);
        const expectedGenScript = {
            databaseName: 'MockDatabaseName',
            serverName: 'MockServer',
            connectionUri: 'Mock|Connection|Uri',
            sqlCmdVariables: new Map([
                ['ProdDatabaseName', 'MyProdDatabase'],
                ['BackupDatabaseName', 'MyBackupDatabase']
            ]),
            deploymentOptions: testContext_1.mockDacFxOptionsResult.deploymentOptions,
            publishProfileUri: undefined
        };
        dialog.object.generateScript = (_, prof) => { profile = prof; };
        await dialog.object.generateScriptClick();
        should(profile).deepEqual(expectedGenScript);
        const expectedContainerPublishProfile = {
            dockerSettings: {
                dbName: 'MockDatabaseName',
                dockerBaseImage: 'mcr.microsoft.com/mssql/server',
                password: '',
                port: 1433,
                serverName: 'localhost',
                userName: 'sa',
                dockerBaseImageEula: 'https://aka.ms/mcr/osslegalnotice'
            },
            sqlProjectPublishSettings: {
                databaseName: 'MockDatabaseName',
                serverName: 'localhost',
                connectionUri: '',
                sqlCmdVariables: new Map([
                    ['ProdDatabaseName', 'MyProdDatabase'],
                    ['BackupDatabaseName', 'MyBackupDatabase']
                ]),
                deploymentOptions: testContext_1.mockDacFxOptionsResult.deploymentOptions,
                publishProfileUri: undefined
            }
        };
        dialog.object.publishToExistingServer = false;
        let deployProfile;
        dialog.object.publishToContainer = (_, prof) => { deployProfile = prof; };
        await dialog.object.publishClick();
        should(deployProfile).deepEqual(expectedContainerPublishProfile);
    });
});
//# sourceMappingURL=publishDatabaseDialog.test.js.map