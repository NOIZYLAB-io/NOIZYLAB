"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const should = require("should");
const path = require("path");
const sinon = require("sinon");
const baselines = require("./baselines/baselines");
const templates = require("../templates/templates");
const testContext_1 = require("./testContext");
const mainController_1 = require("../controllers/mainController");
let testContext;
describe('MainController: main controller operations', function () {
    before(async function () {
        testContext = (0, testContext_1.createContext)();
        await templates.loadTemplates(path.join(__dirname, '..', '..', 'resources', 'templates'));
        await baselines.loadBaselines();
    });
    afterEach(function () {
        sinon.restore();
    });
    it('Should create new instance without error', async function () {
        should.doesNotThrow(() => new mainController_1.default(testContext.context), 'Creating controller should not throw an error');
    });
    it('Should activate and deactivate without error', async function () {
        let controller = new mainController_1.default(testContext.context);
        should.notEqual(controller.extensionContext, undefined);
        should.doesNotThrow(() => controller.activate(), 'activate() should not throw an error');
        should.doesNotThrow(() => controller.dispose(), 'dispose() should not throw an error');
    });
});
//# sourceMappingURL=mainController.test.js.map