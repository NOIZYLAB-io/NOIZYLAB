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

const vscode = require('vscode');

function isWindows()            { return process.platform === 'win32'; }
function getFileSeparator()     { return isWindows() ? '\\' : '/'; }
function getExeName()           { return isWindows() ? "cmaj.exe" : "cmaj"; }
function isFileType (f, type)   { return f != null && typeof f.path == "string" && f.path.endsWith (type); }
function isPatchFile (f)        { return isFileType (f, ".cmajorpatch"); }
function isCmajorFile (f)       { return isFileType (f, ".cmajor"); }
function getParentPath (f)      { return vscode.Uri.file (f.fsPath.substring (0, f.fsPath.lastIndexOf (getFileSeparator()))); }

function getFilename (f)        { return f.split (getFileSeparator()).pop(); }
function getSibling (f, child)  { return vscode.Uri.joinPath (getParentPath (f), child); }
function getFilenameStem (f)    { let name = getFilename (f); const i = name.lastIndexOf ("."); return i < 0 ? name : name.substring (0, i); }

async function getFileStatIfExists (f)
{
    try
    {
        return await vscode.workspace.fs.stat (f);
    }
    catch (e)
    {}

    return undefined;
}

function makeSafeIdentifier (name)
{
    let name2 = "";

    for (c of name)
    {
        if (" ,./;:".includes (c))
            name2 += '_';
        else if ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_".includes (c))
            name2 += c;
    }

    if ("0123456789".includes (name2[0]))
        name2 = "_" + name2;

    return name2;
}

function writeToFile (file, text)
{
    function stringToArray (s)
    {
        const a = new Uint8Array (s.length);
        const encoder = new TextEncoder();
        encoder.encodeInto (s, a);
        return a;
    }

    return vscode.workspace.fs.writeFile (file, stringToArray (text));
}

async function findPatchContaining (cmajorFile)
{
    const patches = await vscode.workspace.findFiles ("**" + getFileSeparator() + "*.cmajorpatch", null);

    if (patches.length == 1)
        return patches[0];

    for (const p of patches)
    {
        const patchFolder = getParentPath (p);

        if (cmajorFile.fsPath.startsWith (patchFolder.fsPath + getFileSeparator()))
            return p;
    }

    return undefined;
}

async function findActivePatchFile()
{
    if (vscode.window.activeTextEditor && vscode.window.activeTextEditor.document)
    {
        const f = vscode.window.activeTextEditor.document.uri;

        if (isPatchFile (f))
            return f;

        if (f)
        {
            const patch = findPatchContaining (f);

            if (patch)
                return patch;
        }
    }

    return undefined;
}

function findActiveTestFile()
{
    if (vscode.window.activeTextEditor && vscode.window.activeTextEditor.document.uri)
    {
        const f = vscode.window.activeTextEditor.document.uri;

        if (isFileType (f, ".cmajtest"))
            return f;
    }

    return undefined;
}

async function findCmajTool (extensionUri)
{
    let location = vscode.workspace.getConfiguration ("cmajor").get ("commandLineToolLocation");

    if (location && typeof location == "string")
    {
        let f = vscode.Uri.file (location);

        let stats = await getFileStatIfExists (f);

        if (stats)
        {
            if (stats.type == vscode.FileType.File && stats.size > 0)
                return f;

            if (stats.type == vscode.FileType.Directory)
            {
                f = vscode.Uri.joinPath (f, getExeName());
                stats = await getFileStatIfExists (f);

                if (stats && stats.type == vscode.FileType.File && stats.size > 0)
                    return f;
            }
        }
    }

    const binFolder = vscode.Uri.joinPath (extensionUri, "bin");
    const tool = vscode.Uri.joinPath (binFolder, getExeName());
    stats = await getFileStatIfExists (tool);

    if (stats && stats.type == vscode.FileType.File && stats.size > 0)
        return tool;

    return undefined;
}

function showMissingCmajToolError()
{
    vscode.window.showErrorMessage ("Cmajor: Can't find the cmaj command-line app - maybe try re-installing the VScode extension, or check the path in the Cmajor extension settings?");
}

module.exports = {
    isWindows,
    getFileSeparator,
    getExeName,
    getSibling,
    getFilenameStem,
    makeSafeIdentifier,
    writeToFile,
    isFileType,
    isPatchFile,
    isCmajorFile,
    getParentPath,
    findActivePatchFile,
    findActiveTestFile,
    findCmajTool,
    showMissingCmajToolError,
    getFileStatIfExists
}
