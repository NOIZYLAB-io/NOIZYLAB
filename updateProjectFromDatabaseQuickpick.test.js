"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");
const should = require("should");
const sinon = require("sinon");
const baselines = require("../baselines/baselines");
const testUtils = require("../testUtils");
const utils = require("../../common/utils");
const constants = require("../../common/constants");
const updateProjectFromDatabaseQuickpick_1 = require("../../dialogs/updateProjectFromDatabaseQuickpick");
describe('Update Project From Database Quickpicks', () => {
    before(async function () {
        await baselines.loadBaselines();
    });
    afterEach(function () {
        sinon.restore();
    });
    after(async function () {
        await testUtils.deleteGeneratedTestFolder();
    });
    it('Should build UpdateProjectDataModel when user selects workspace project and Update action', async function () {
        // Arrange - create a test project and stub utils & quickpicks
        const project = await testUtils.createTestProject(this.test, baselines.openProjectFileBaseline);
        const projectFilePath = project.projectFilePath.toLowerCase();
        // Stub workspace project enumeration to return the created project
        sinon.stub(utils, 'getSqlProjectsInWorkspace').resolves([vscode.Uri.file(projectFilePath)]);
        // Stub the vscode-mssql API provider used by the quickpick flow
        const connectionProfile = {
            user: 'user',
            password: 'pw',
            server: 'serverName',
            database: 'TestDB',
            authenticationType: 'SqlLogin',
            options: { connectionName: 'MockConnection' }
        };
        sinon.stub(utils, 'getVscodeMssqlApi').resolves({
            promptForConnection: sinon.stub().resolves(connectionProfile),
            connect: sinon.stub().resolves('MockUri'),
            listDatabases: sinon.stub().resolves([connectionProfile.database])
        });
        // Stub QuickPick flows:
        // Call 0 -> project selection (workspace project)
        // Call 1 -> action selection (Update)
        const showQP = sinon.stub(vscode.window, 'showQuickPick');
        showQP.onCall(0).resolves(projectFilePath);
        showQP.onCall(1).resolves(constants.updateActionRadioButtonLabel);
        // Capture the model produced by the callback
        let capturedModel;
        const cb = async (m) => { capturedModel = m; };
        // Act - pass undefined for projectFilePath to trigger prompt
        await (0, updateProjectFromDatabaseQuickpick_1.UpdateProjectFromDatabaseWithQuickpick)(undefined, undefined, cb);
        // Assert
        should(capturedModel).not.be.undefined();
        should.equal(capturedModel.sourceEndpointInfo.databaseName, connectionProfile.database, 'Source database should match selected database');
        should.equal(capturedModel.sourceEndpointInfo.serverDisplayName, connectionProfile.server, 'Source server display name should match connection profile server');
        should.equal(capturedModel.targetEndpointInfo.projectFilePath, projectFilePath, 'Target project file path should be the selected workspace project');
        should.equal(capturedModel.action, 1 /* UpdateProjectAction.Update */, 'Action should be Update');
    });
    it('Should not invoke callback when user cancels project selection', async function () {
        // Arrange - stub getVscodeMssqlApi to return a profile with a database (so no DB pick)
        const connectionProfile = {
            user: 'user',
            password: 'pw',
            server: 'serverName',
            database: 'TestDB',
            authenticationType: 'SqlLogin',
            options: { connectionName: 'MockConnection' }
        };
        sinon.stub(utils, 'getVscodeMssqlApi').resolves({
            promptForConnection: sinon.stub().resolves(connectionProfile),
            connect: sinon.stub().resolves('MockUri'),
            listDatabases: sinon.stub().resolves([connectionProfile.database])
        });
        // Workspace may contain projects, but user cancels at project selection
        sinon.stub(utils, 'getSqlProjectsInWorkspace').resolves([]);
        // Simulate user cancelling project quickpick
        const showQP = sinon.stub(vscode.window, 'showQuickPick');
        showQP.onCall(0).resolves(undefined); // user cancels at project selection
        const spyCb = sinon.spy();
        // Act - pass undefined for projectFilePath to trigger prompt
        await (0, updateProjectFromDatabaseQuickpick_1.UpdateProjectFromDatabaseWithQuickpick)(undefined, undefined, spyCb);
        // Assert - callback should not be called
        should(spyCb.notCalled).be.true();
    });
    it('Should use provided project file path without prompting when passed as parameter', async function () {
        // Arrange - create a test project
        const project = await testUtils.createTestProject(this.test, baselines.openProjectFileBaseline);
        const providedProjectPath = project.projectFilePath.toLowerCase();
        // Stub the vscode-mssql API provider
        const connectionProfile = {
            user: 'user',
            password: 'pw',
            server: 'serverName',
            database: 'TestDB',
            authenticationType: 'SqlLogin',
            options: { connectionName: 'MockConnection' }
        };
        sinon.stub(utils, 'getVscodeMssqlApi').resolves({
            promptForConnection: sinon.stub().resolves(connectionProfile),
            connect: sinon.stub().resolves('MockUri'),
            listDatabases: sinon.stub().resolves([connectionProfile.database])
        });
        // Stub QuickPick - should only be called once for action selection (not for project selection)
        const showQP = sinon.stub(vscode.window, 'showQuickPick');
        showQP.onCall(0).resolves(constants.compareActionRadioButtonLabel); // Only action selection
        // Spy on getSqlProjectsInWorkspace to ensure it's NOT called when project path is provided
        const getProjectsSpy = sinon.stub(utils, 'getSqlProjectsInWorkspace');
        // Capture the model produced by the callback
        let capturedModel;
        const cb = async (m) => { capturedModel = m; };
        // Act - pass the project file path as second parameter
        await (0, updateProjectFromDatabaseQuickpick_1.UpdateProjectFromDatabaseWithQuickpick)(undefined, providedProjectPath, cb);
        // Assert
        should(capturedModel).not.be.undefined();
        should.equal(capturedModel.targetEndpointInfo.projectFilePath, providedProjectPath, 'Target project file path should be the provided project path, not prompted');
        should.equal(capturedModel.action, 0 /* UpdateProjectAction.Compare */, 'Action should be Compare');
        // Verify that project selection was skipped
        should(getProjectsSpy.notCalled).be.true('getSqlProjectsInWorkspace should not be called when project path is provided');
        should.equal(showQP.callCount, 1, 'QuickPick should only be shown once (for action), not for project selection');
    });
    it('Should prompt for project when no project file path is provided as parameter', async function () {
        // Arrange - create a test project
        const project = await testUtils.createTestProject(this.test, baselines.openProjectFileBaseline);
        const workspaceProjectPath = project.projectFilePath.toLowerCase();
        // Stub workspace project enumeration to return the created project
        sinon.stub(utils, 'getSqlProjectsInWorkspace').resolves([vscode.Uri.file(workspaceProjectPath)]);
        // Stub the vscode-mssql API provider
        const connectionProfile = {
            user: 'user',
            password: 'pw',
            server: 'serverName',
            database: 'TestDB',
            authenticationType: 'SqlLogin',
            options: { connectionName: 'MockConnection' }
        };
        sinon.stub(utils, 'getVscodeMssqlApi').resolves({
            promptForConnection: sinon.stub().resolves(connectionProfile),
            connect: sinon.stub().resolves('MockUri'),
            listDatabases: sinon.stub().resolves([connectionProfile.database])
        });
        // Stub QuickPick - should be called twice (project selection and action selection)
        const showQP = sinon.stub(vscode.window, 'showQuickPick');
        showQP.onCall(0).resolves(workspaceProjectPath); // Project selection
        showQP.onCall(1).resolves(constants.updateActionRadioButtonLabel); // Action selection
        // Capture the model produced by the callback
        let capturedModel;
        const cb = async (m) => { capturedModel = m; };
        // Act - pass undefined for project file path to trigger prompt
        await (0, updateProjectFromDatabaseQuickpick_1.UpdateProjectFromDatabaseWithQuickpick)(undefined, undefined, cb);
        // Assert
        should(capturedModel).not.be.undefined();
        should.equal(capturedModel.targetEndpointInfo.projectFilePath, workspaceProjectPath, 'Target project file path should be the selected workspace project');
        should.equal(capturedModel.action, 1 /* UpdateProjectAction.Update */, 'Action should be Update');
        should.equal(showQP.callCount, 2, 'QuickPick should be shown twice (project and action selection)');
    });
});
//# sourceMappingURL=updateProjectFromDatabaseQuickpick.test.js.map