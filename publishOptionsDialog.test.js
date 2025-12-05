"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const should = require("should");
const testUtils = require("../testUtils");
const testData = require("../testContext");
const baselines = require("../baselines/baselines");
const TypeMoq = require("typemoq");
const publishOptionsDialog_1 = require("../../dialogs/publishOptionsDialog");
const publishDatabaseDialog_1 = require("../../dialogs/publishDatabaseDialog");
const project_1 = require("../../models/project");
const sinon = require("sinon");
describe('Publish Database Options Dialog', () => {
    before(async function () {
        await baselines.loadBaselines();
    });
    after(async function () {
        await testUtils.deleteGeneratedTestFolder();
    });
    it('Should open dialog successfully ', async function () {
        const proj = new project_1.Project('');
        sinon.stub(proj, 'getProjectTargetVersion').returns('150');
        const publishDatabaseDialog = new publishDatabaseDialog_1.PublishDatabaseDialog(new project_1.Project(''));
        const optionsDialog = new publishOptionsDialog_1.PublishOptionsDialog(testData.getDeploymentOptions(), publishDatabaseDialog);
        optionsDialog.openDialog();
        // Verify the dialog should exists
        should.notEqual(optionsDialog.dialog, undefined);
    });
    it('Should deployment options gets initialized correctly with sample test project', async function () {
        // Create new sample test project
        const project = await testUtils.createTestProject(this.test, baselines.openProjectFileBaseline);
        const dialog = TypeMoq.Mock.ofType(publishDatabaseDialog_1.PublishDatabaseDialog, undefined, undefined, project);
        dialog.setup(x => x.getDeploymentOptions()).returns(() => { return Promise.resolve(testData.mockDacFxOptionsResult.deploymentOptions); });
        const options = await dialog.object.getDeploymentOptions();
        const optionsDialog = new publishOptionsDialog_1.PublishOptionsDialog(options, new publishDatabaseDialog_1.PublishDatabaseDialog(project));
        // Verify the options model should exists
        should.notEqual(optionsDialog.optionsModel, undefined);
        // Verify the deployment options should exists
        should.notEqual(optionsDialog.optionsModel.deploymentOptions, undefined);
        Object.entries(optionsDialog.optionsModel.deploymentOptions.booleanOptionsDictionary).forEach(option => {
            // Validate the value and description as expected
            should.equal(option[1].value, false);
            should.equal(option[1].description, 'Sample Description text');
        });
    });
});
//# sourceMappingURL=publishOptionsDialog.test.js.map