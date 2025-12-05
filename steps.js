"use strict";
// Right now it is redundant because it is defined in "src/@types/events.ts", this is done because we can't embed enums in typescript.
// The idea in future will be declaring some common types and use them properly with repeated usage.
Object.defineProperty(exports, "__esModule", { value: true });
exports.StepType = void 0;
var StepType;
(function (StepType) {
    StepType["Lang"] = "language";
    StepType["TestType"] = "testType";
    StepType["InitialCoverage"] = "initialCoverage";
    StepType["CalculatedCoverage"] = "calculatedCoverage";
    StepType["Libraries"] = "libraries";
    StepType["Functions"] = "functions";
    StepType["TestGenerationInfo"] = "testGenerationInfo";
    StepType["TestGeneration"] = "testGeneration";
    StepType["TestGenerationFailure"] = "testGenerationFailure";
    StepType["Iteration"] = "iteration";
    StepType["ErrorMsg"] = "errorMsg";
    StepType["NewLibraries"] = "newLibraries";
    StepType["TestRun"] = "testRun";
    StepType["TestRunStatus"] = "testRunStatus";
    StepType["CoverageIncreased"] = "coverageIncreased";
    StepType["RunSummary"] = "runSummary";
    StepType["Summary"] = "summary";
    StepType["Abort"] = "abort";
    StepType["Completed"] = "completed";
})(StepType || (exports.StepType = StepType = {}));
//# sourceMappingURL=steps.js.map