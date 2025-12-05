//
//     ,ad888ba,                              88
//    d8"'    "8b
//   d8            88,dba,,adba,   ,aPP8A.A8  88     The Cmajor Toolkit
//   Y8,           88    88    88  88     88  88
//    Y8a.   .a8P  88    88    88  88,   ,88  88     (C)2024 Cmajor Software Ltd
//     '"Y888Y"'   88    88    88  '"8bbP"Y8  88     https://cmajor.dev
//                                           ,88
//                                        888P"
//
//  The Cmajor project is subject to commercial or open-source licensing.
//  You may use it under the terms of the GPLv3 (see www.gnu.org/licenses), or
//  visit https://cmajor.dev to learn about our commercial licence options.
//
//  CMAJOR IS PROVIDED "AS IS" WITHOUT ANY WARRANTY, AND ALL WARRANTIES, WHETHER
//  EXPRESSED OR IMPLIED, INCLUDING MERCHANTABILITY AND FITNESS FOR PURPOSE, ARE
//  DISCLAIMED.

const vscode      = require('vscode');
const patchPanel  = require ("./cmaj_patch_runner_panel.js");
const createPatch = require ("./cmaj_create_new_patch.js");
const helpers     = require ("./cmaj_helpers.js");

let overriddenRunCommand = null;
let subscriptions = [];
let extensionUri = null;
let isDevMode = false;

function activate (context)
{
    extensionUri = context.extensionUri;

    let disposable = vscode.commands.registerCommand ('cmajor.run', runActiveCmajorDoc);
    context.subscriptions.push (disposable);

    disposable = vscode.commands.registerCommand ('cmajor.check', checkForErrors);
    context.subscriptions.push (disposable);

    disposable = vscode.commands.registerCommand ('cmajor.create.patch', createPatch.createNewPatch);
    context.subscriptions.push (disposable);

    disposable = vscode.commands.registerCommand ('cmajor.show.examples', showExamples);
    context.subscriptions.push (disposable);

    disposable = vscode.commands.registerCommand ('cmajor.show.docs', showDocs);
    context.subscriptions.push (disposable);

    disposable = vscode.commands.registerCommand ('cmajor.generate.webaudio', generateWebAudioHtml);
    context.subscriptions.push (disposable);

    disposable = vscode.commands.registerCommand ('cmajor.generate.wam', generateWam);
    context.subscriptions.push (disposable);

    disposable = vscode.commands.registerCommand ('cmajor.generate.juceplugin', generateJUCEPlugin);
    context.subscriptions.push (disposable);

    disposable = vscode.commands.registerCommand ('cmajor.generate.clapplugin', generateCLAPPlugin);
    context.subscriptions.push (disposable);

    overriddenRunCommand = vscode.commands.registerCommand ("workbench.action.debug.start", interceptStartDebugging);
    context.subscriptions.push (overriddenRunCommand);
    subscriptions = context.subscriptions;

    isDevMode = (context.extensionMode === vscode.ExtensionMode.Development);

    patchPanel.registerSerialiser (extensionUri, isDevMode);

    if (isDevMode)
        patchPanel.serverAssetLocation
            = "--assetFolder=" + vscode.Uri.joinPath (extensionUri, "../../../cmajor").fsPath;
}

function deactivate()
{
}

async function interceptStartDebugging (args)
{
    if (await runActiveCmajorDoc())
        return;

    // To invoke the default debug command, need to first delete our overridden one..
    const index = subscriptions.indexOf (overriddenRunCommand);
    overriddenRunCommand.dispose();

    await vscode.commands.executeCommand ("workbench.action.debug.start", args);

    // ..then re-override it
    overriddenRunCommand = vscode.commands.registerCommand ("workbench.action.debug.start", interceptStartDebugging);

    if (index >= 0)
        subscriptions[index] = overriddenRunCommand;
    else
        subscriptions.push (overriddenRunCommand);
}

//==============================================================================
async function runActiveCmajorDoc()
{
    const testFile = helpers.findActiveTestFile();

    if (testFile)
        return invokeTest (testFile);

    const patchFileUri = await helpers.findActivePatchFile();

    if (patchFileUri)
    {
        patchPanel.showPanel (patchFileUri, extensionUri, isDevMode);
        return true;
    }

    if (vscode.window.activeTextEditor
         && vscode.window.activeTextEditor.document
         && (helpers.isCmajorFile (vscode.window.activeTextEditor.document.uri)
              || helpers.isPatchFile (vscode.window.activeTextEditor.document.uri)))
    {
        if (showWorkspaceNeededError())
            return true;

        vscode.window.showErrorMessage ("Cmajor: Couldn't locate the .cmajorpatch file to which this .cmajor file belongs");
        return true;
    }

    return false;
}

//==============================================================================
async function invokeTest (testFile)
{
    return invokeTool ([ "test", vscode.workspace.asRelativePath (testFile, false) ]);
}

//==============================================================================
async function checkForErrors()
{
    const testFile = helpers.findActiveTestFile();

    if (testFile)
        return invokeTest (testFile);

    const patchFileUri = await helpers.findActivePatchFile();

    if (patchFileUri)
        return invokeTool ([ "play", "--dry-run", "--stop-on-error", vscode.workspace.asRelativePath (patchFileUri, false) ]);
}

//==============================================================================
async function showExamples()
{
    const examplesFolder = vscode.Uri.joinPath (extensionUri, "examples");
    let stats = await helpers.getFileStatIfExists (examplesFolder);

    if (stats && stats.type == vscode.FileType.Directory)
        return vscode.commands.executeCommand ('vscode.openFolder', examplesFolder,
                                               {
                                                   forceNewWindow: true,
                                                   noRecentEntry: true
                                               });

    return vscode.env.openExternal (vscode.Uri.parse ("https://github.com/cmajor-lang/cmajor/tree/main/examples/patches"));
}

//==============================================================================
function showDocs()
{
    return vscode.env.openExternal (vscode.Uri.parse ("https://cmajor.dev/"));
}

//==============================================================================
async function generateWebAudioHtml()
{
    generateExport ("webaudio-html", "Export HTML/Javascript");
}

async function generateWam()
{
    generateExport ("wam", "Export Web Audio Module");
}

async function generateCLAPPlugin()
{
    generateExport ("clap", "Export CLAP Plugin");
}

async function generateJUCEPlugin()
{
    generateExport ("juce", "Export JUCE Plugin");
}

async function generateExport (type, dialogTitle)
{
    const patchFileUri = await helpers.findActivePatchFile();

    if (! patchFileUri)
    {
        vscode.window.showErrorMessage ("Cmajor: To export a project, focus on the .cmajorpatch file you want to export");
        return;
    }

    const targetFile = await vscode.window.showSaveDialog ({
        title: "Choose a folder in which to save the exported project",
        saveLabel: dialogTitle
    });

    if (targetFile)
    {
        const args = [ "generate",
                       "--target=" + type,
                       "--output=" + targetFile.fsPath,
                       patchFileUri.fsPath ];

        return invokeTool (args);
    }
}

//==============================================================================
async function invokeTool (args)
{
    if (! args)
        return false;

    const commandUri = await helpers.findCmajTool (extensionUri);

    if (! commandUri)
    {
        showMissingCmajToolError();
        return true;
    }

    for (term of vscode.window.terminals)
        if (term.source == "Cmajor")
            term.dispose();

    if (! vscode.workspace.workspaceFolders)
        return showWorkspaceNeededError();

    // NB: sending a dummy command first because otherwise, the problems panel
    // won't be refreshed until after our run terminates, and any stale errors
    // would hang around while running.
    await vscode.tasks.executeTask (createShellTask ("Cmajor Helper", "echo \"\""));
    await vscode.tasks.executeTask (createShellTask ("Cmajor", commandUri.fsPath, args));

    setTimeout (() => {
        for (term of vscode.window.terminals)
            if (term.name == "Cmajor Helper")
                term.dispose();
    }, 500);

    return true;
}

function createShellTask (name, command, args)
{
    const task = new vscode.Task ({ type: "shell" },
                                  vscode.TaskScope.Workspace,
                                  name,
                                  "Cmajor",
                                  new vscode.ShellExecution (command, args),
                                  [ "$cmajor1", "$cmajor2" ]);

    task.presentationOptions = {
        reveal: vscode.TaskRevealKind.Always,
        panel: vscode.TaskPanelKind.Dedicated,
        clear: true,
        showReuseMessage: true
    };

    task.group = vscode.TaskGroup.Test;
    task.definition.command = "dummy"; // suppresses a buggy error message

    return task;
}

function showWorkspaceNeededError()
{
    vscode.window.showErrorMessage ("Cmajor: To build Cmajor code, VScode must have an open workspace folder that contains your Cmajor files");
    return true;
}

module.exports = {
    activate,
    deactivate
}
