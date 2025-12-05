"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.mockFailedConnectionResult = exports.mockConnectionResult = void 0;
exports.createContext = createContext;
const should = require("should");
const sinon = require("sinon");
const baselines = require("../baselines/baselines");
const testUtils = require("../testUtils");
const deployService_1 = require("../../models/deploy/deployService");
const project_1 = require("../../models/project");
const vscode = require("vscode");
const azdata = require("azdata");
const UUID = require("vscode-languageclient/lib/utils/uuid");
const constants = require("../../common/constants");
const shellExecutionHelper_1 = require("../../tools/shellExecutionHelper");
const TypeMoq = require("typemoq");
const azureSqlClient_1 = require("../../models/deploy/azureSqlClient");
const connectionService_1 = require("../../models/connections/connectionService");
exports.mockConnectionResult = {
    connected: true,
    connectionId: 'id',
    errorMessage: '',
    errorCode: 0
};
exports.mockFailedConnectionResult = {
    connected: false,
    connectionId: 'id',
    errorMessage: 'Failed to connect',
    errorCode: 0
};
function createContext() {
    return {
        outputChannel: {
            name: '',
            append: () => { },
            appendLine: () => { },
            clear: () => { },
            show: () => { },
            hide: () => { },
            dispose: () => { },
            replace: () => { }
        },
        azureSqlClient: TypeMoq.Mock.ofType(azureSqlClient_1.AzureSqlClient)
    };
}
let sandbox;
describe('deploy service', function () {
    before(async function () {
        await baselines.loadBaselines();
    });
    afterEach(function () {
        sandbox.restore();
        sinon.restore();
    });
    beforeEach(() => {
        sandbox = sinon.createSandbox();
    });
    after(async function () {
        await testUtils.deleteGeneratedTestFolder();
    });
    it('Should deploy a database to docker container successfully', async function () {
        const testContext = createContext();
        const deployProfile = {
            sqlProjectPublishSettings: {
                databaseName: 'dbName',
                serverName: 'serverName',
                connectionUri: 'connectionUri'
            },
            dockerSettings: {
                dbName: 'test',
                password: 'PLACEHOLDER',
                port: 1433,
                serverName: 'localhost',
                userName: 'sa',
                dockerBaseImage: 'image',
                connectionRetryTimeout: 1,
                dockerBaseImageEula: ''
            }
        };
        const projFilePath = await testUtils.createTestSqlProjFile(this.test, baselines.newProjectFileBaseline);
        const project1 = await project_1.Project.openProject(vscode.Uri.file(projFilePath).fsPath);
        const shellExecutionHelper = TypeMoq.Mock.ofType(shellExecutionHelper_1.ShellExecutionHelper);
        shellExecutionHelper.setup(x => x.runStreamedCommand(TypeMoq.It.isAny(), undefined, TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.resolve('id'));
        const deployService = new deployService_1.DeployService(testContext.azureSqlClient.object, testContext.outputChannel, shellExecutionHelper.object);
        sandbox.stub(azdata.connection, 'connect').returns(Promise.resolve(exports.mockConnectionResult));
        sandbox.stub(azdata.connection, 'getUriForConnection').returns(Promise.resolve('connection'));
        sandbox.stub(vscode.window, 'showQuickPick').returns(Promise.resolve(constants.yesString));
        sandbox.stub(azdata.tasks, 'startBackgroundOperation').callThrough();
        let connection = await deployService.deployToContainer(deployProfile, project1);
        should(connection).equals('connection');
    });
    it('Should fail the deploy if docker is not running', async function () {
        const testContext = createContext();
        const deployProfile = {
            sqlProjectPublishSettings: {
                databaseName: 'dbName',
                serverName: 'serverName',
                connectionUri: 'connectionUri'
            },
            dockerSettings: {
                dbName: 'test',
                password: 'PLACEHOLDER',
                port: 1433,
                serverName: 'localhost',
                userName: 'sa',
                dockerBaseImage: 'image',
                connectionRetryTimeout: 1,
                dockerBaseImageEula: ''
            }
        };
        const projFilePath = await testUtils.createTestSqlProjFile(this.test, baselines.newProjectFileBaseline);
        const project1 = await project_1.Project.openProject(vscode.Uri.file(projFilePath).fsPath);
        const shellExecutionHelper = TypeMoq.Mock.ofType(shellExecutionHelper_1.ShellExecutionHelper);
        shellExecutionHelper.setup(x => x.runStreamedCommand(TypeMoq.It.isAny(), undefined, TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.reject('error'));
        const deployService = new deployService_1.DeployService(testContext.azureSqlClient.object, testContext.outputChannel, shellExecutionHelper.object);
        sandbox.stub(azdata.tasks, 'startBackgroundOperation').callThrough();
        await should(deployService.deployToContainer(deployProfile, project1)).rejected();
    });
    it('Should retry connecting to the server', async function () {
        const testContext = createContext();
        const localDbSettings = {
            dbName: 'test',
            password: 'PLACEHOLDER',
            port: 1433,
            serverName: 'localhost',
            userName: 'sa',
            dockerBaseImage: 'image',
            connectionRetryTimeout: 1,
            dockerBaseImageEula: ''
        };
        const shellExecutionHelper = TypeMoq.Mock.ofType(shellExecutionHelper_1.ShellExecutionHelper);
        shellExecutionHelper.setup(x => x.runStreamedCommand(TypeMoq.It.isAny(), undefined, TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.resolve('id'));
        const connectionService = new connectionService_1.ConnectionService(testContext.outputChannel);
        let connectionStub = sandbox.stub(azdata.connection, 'connect');
        connectionStub.onFirstCall().returns(Promise.resolve(exports.mockFailedConnectionResult));
        connectionStub.onSecondCall().returns(Promise.resolve(exports.mockConnectionResult));
        sandbox.stub(azdata.connection, 'getUriForConnection').returns(Promise.resolve('connection'));
        sandbox.stub(azdata.tasks, 'startBackgroundOperation').callThrough();
        let connection = await connectionService.getConnection(localDbSettings, false, 'master');
        should(connection).equals('connection');
    });
    it('Should clean a list of docker images successfully', async function () {
        const testContext = createContext();
        const shellExecutionHelper = TypeMoq.Mock.ofType(shellExecutionHelper_1.ShellExecutionHelper);
        shellExecutionHelper.setup(x => x.runStreamedCommand(TypeMoq.It.isAny(), undefined, TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.resolve(`id
		id2
		id3`));
        const deployService = new deployService_1.DeployService(testContext.azureSqlClient.object, testContext.outputChannel, shellExecutionHelper.object);
        const ids = await deployService.getCurrentDockerContainer('label');
        await deployService.cleanDockerObjects(ids, ['docker stop', 'docker rm']);
        shellExecutionHelper.verify(x => x.runStreamedCommand(TypeMoq.It.isAny(), undefined, TypeMoq.It.isAny(), TypeMoq.It.isAny()), TypeMoq.Times.exactly(7));
    });
    it('Should create docker image info correctly', () => {
        const id = UUID.generateUuid().toLocaleLowerCase();
        const baseImage = 'baseImage:latest';
        const tag = baseImage.replace(':', '-').replace(constants.sqlServerDockerRegistry, '').replace(/[^a-zA-Z0-9_,\-]/g, '').toLocaleLowerCase();
        should((0, deployService_1.getDockerImageSpec)('project-name123_test', baseImage, id)).deepEqual({
            label: `${constants.dockerImageLabelPrefix}-project-name123_test`,
            containerName: `${constants.dockerImageNamePrefix}-project-name123_test-${id}`,
            tag: `${constants.dockerImageNamePrefix}-project-name123_test-${tag}`
        });
        should((0, deployService_1.getDockerImageSpec)('project-name1', baseImage, id)).deepEqual({
            label: `${constants.dockerImageLabelPrefix}-project-name1`,
            containerName: `${constants.dockerImageNamePrefix}-project-name1-${id}`,
            tag: `${constants.dockerImageNamePrefix}-project-name1-${tag}`
        });
        should((0, deployService_1.getDockerImageSpec)('project-name2$#', baseImage, id)).deepEqual({
            label: `${constants.dockerImageLabelPrefix}-project-name2`,
            containerName: `${constants.dockerImageNamePrefix}-project-name2-${id}`,
            tag: `${constants.dockerImageNamePrefix}-project-name2-${tag}`
        });
        should((0, deployService_1.getDockerImageSpec)('project - name3', baseImage, id)).deepEqual({
            label: `${constants.dockerImageLabelPrefix}-project-name3`,
            containerName: `${constants.dockerImageNamePrefix}-project-name3-${id}`,
            tag: `${constants.dockerImageNamePrefix}-project-name3-${tag}`
        });
        should((0, deployService_1.getDockerImageSpec)('project_name4', baseImage, id)).deepEqual({
            label: `${constants.dockerImageLabelPrefix}-project_name4`,
            containerName: `${constants.dockerImageNamePrefix}-project_name4-${id}`,
            tag: `${constants.dockerImageNamePrefix}-project_name4-${tag}`
        });
        const reallyLongName = new Array(128 + 1).join('a').replace(/[^a-zA-Z0-9_,\-]/g, '');
        const imageProjectName = reallyLongName.substring(0, 128 - (constants.dockerImageNamePrefix.length + tag.length + 2));
        should((0, deployService_1.getDockerImageSpec)(reallyLongName, baseImage, id)).deepEqual({
            label: `${constants.dockerImageLabelPrefix}-${imageProjectName}`,
            containerName: `${constants.dockerImageNamePrefix}-${imageProjectName}-${id}`,
            tag: `${constants.dockerImageNamePrefix}-${imageProjectName}-${tag}`
        });
    });
    it('Should create a new Azure SQL server successfully', async function () {
        const testContext = createContext();
        const deployProfile = {
            sqlDbSetting: {
                dbName: 'test',
                password: 'PLACEHOLDER',
                port: 1433,
                serverName: 'localhost',
                userName: 'sa',
                connectionRetryTimeout: 1,
                resourceGroupName: 'resourceGroups',
                session: {
                    subscription: {
                        subscriptionId: 'subscriptionId',
                    }, token: {
                        key: '',
                        token: '',
                        tokenType: '',
                    },
                    tenantId: '',
                    account: undefined
                },
                location: 'location'
            }
        };
        const fullyQualifiedDomainName = 'servername';
        const shellExecutionHelper = TypeMoq.Mock.ofType(shellExecutionHelper_1.ShellExecutionHelper);
        shellExecutionHelper.setup(x => x.runStreamedCommand(TypeMoq.It.isAny(), undefined, TypeMoq.It.isAny(), TypeMoq.It.isAny())).returns(() => Promise.resolve('id'));
        const session = deployProfile?.sqlDbSetting?.session;
        if (deployProfile?.sqlDbSetting?.session && session) {
            testContext.azureSqlClient.setup(x => x.createOrUpdateServer(session, deployProfile.sqlDbSetting?.resourceGroupName || '', deployProfile.sqlDbSetting?.serverName || '', {
                location: deployProfile?.sqlDbSetting?.location || '',
                administratorLogin: deployProfile?.sqlDbSetting?.userName,
                administratorLoginPassword: deployProfile?.sqlDbSetting?.password
            })).returns(() => Promise.resolve(fullyQualifiedDomainName));
        }
        sandbox.stub(azdata.connection, 'connect').returns(Promise.resolve(exports.mockConnectionResult));
        sandbox.stub(azdata.connection, 'getUriForConnection').returns(Promise.resolve('connection'));
        const deployService = new deployService_1.DeployService(testContext.azureSqlClient.object, testContext.outputChannel, shellExecutionHelper.object);
        let connection = await deployService.createNewAzureSqlServer(deployProfile);
        should(deployProfile.sqlDbSetting?.serverName).equal(fullyQualifiedDomainName);
        should(connection).equals('connection');
    });
});
//# sourceMappingURL=deployService.test.js.map