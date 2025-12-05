"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
const should = require("should");
const os = require("os");
const vscode = require("vscode");
const path = require("path");
const buildHelper_1 = require("../tools/buildHelper");
const testContext_1 = require("./testContext");
describe('BuildHelper: Build Helper tests', function () {
    it('Should get correct build arguments for legacy-style projects', function () {
        // update settings and validate
        const buildHelper = new buildHelper_1.BuildHelper();
        const resultArgs = buildHelper.constructBuildArguments('dummy\\dll path', 1 /* ProjectType.LegacyStyle */);
        // Check that it returns an array
        should(resultArgs).be.Array();
        should(resultArgs.length).equal(3); // 3 arguments for legacy projects
        // Check individual arguments
        should(resultArgs[0]).equal('/p:NetCoreBuild=true');
        if (os.platform() === 'win32') {
            should(resultArgs[1]).equal('/p:SystemDacpacsLocation="dummy\\\\dll path"');
            should(resultArgs[2]).equal('/p:NETCoreTargetsPath="dummy\\\\dll path"');
        }
        else {
            should(resultArgs[1]).equal('/p:SystemDacpacsLocation="dummy/dll path"');
            should(resultArgs[2]).equal('/p:NETCoreTargetsPath="dummy/dll path"');
        }
    });
    it('Should get correct build arguments for SDK-style projects', function () {
        // update settings and validate
        const buildHelper = new buildHelper_1.BuildHelper();
        const resultArgs = buildHelper.constructBuildArguments('dummy\\dll path', 0 /* ProjectType.SdkStyle */);
        // Check that it returns an array
        should(resultArgs).be.Array();
        should(resultArgs.length).equal(2); // 2 arguments for SDK projects (no NETCoreTargetsPath)
        // Check individual arguments
        should(resultArgs[0]).equal('/p:NetCoreBuild=true');
        if (os.platform() === 'win32') {
            should(resultArgs[1]).equal('/p:SystemDacpacsLocation="dummy\\\\dll path"');
        }
        else {
            should(resultArgs[1]).equal('/p:SystemDacpacsLocation="dummy/dll path"');
        }
    });
    it('Should get correct build folder', async function () {
        const testContext = (0, testContext_1.createContext)();
        const buildHelper = new buildHelper_1.BuildHelper();
        await buildHelper.createBuildDirFolder(testContext.outputChannel);
        // get expected path for build
        let expectedPath = vscode.extensions.getExtension('Microsoft.sql-database-projects')?.extensionPath ?? 'EmptyPath';
        expectedPath = path.join(expectedPath, 'BuildDirectory');
        should(buildHelper.extensionBuildDirPath).equal(expectedPath);
    });
});
//# sourceMappingURL=buildHelper.test.js.map