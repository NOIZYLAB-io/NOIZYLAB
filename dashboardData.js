"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Status = exports.PublishData = exports.DashboardData = void 0;
class DashboardData {
    projectFile;
    status;
    target;
    timeToCompleteAction;
    startDate;
    constructor(projectFile, status, target, startDate) {
        this.projectFile = projectFile;
        this.status = status;
        this.target = target;
        this.timeToCompleteAction = '';
        this.startDate = startDate;
    }
}
exports.DashboardData = DashboardData;
class PublishData extends DashboardData {
    targetServer;
    targetDatabase;
    constructor(projectFile, status, target, startDate, targetDatabase, targetServer) {
        super(projectFile, status, target, startDate);
        this.targetDatabase = targetDatabase;
        this.targetServer = targetServer;
    }
}
exports.PublishData = PublishData;
var Status;
(function (Status) {
    Status[Status["success"] = 0] = "success";
    Status[Status["failed"] = 1] = "failed";
    Status[Status["inProgress"] = 2] = "inProgress";
})(Status || (exports.Status = Status = {}));
//# sourceMappingURL=dashboardData.js.map