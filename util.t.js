"use strict";
// import * as vscode from "vscode";
// const showDialog = vscode.window.showInformationMessage;
// const showWarning = vscode.window.showWarningMessage;
// export function getAvailableExtensionPacks(context: vscode.ExtensionContext) {
//   return availableExtensions(readExtensions(context));
// }
// function readExtensions(context: vscode.ExtensionContext) {
//   const dependentExts: string[] = context.extension.packageJSON.extensionPack;
//   const extensions = dependentExts
//     .map(name => vscode.extensions.getExtension(name))
//     .filter(ext => ext);
//   const missingExtNames = dependentExts
//     .filter(name => dependentExts.includes(ex))
//     .map(ext => ext!.id);
//   if (missingExtNames.length)
//     showWarning(
//       `Warning: These extensions are missing: "${missingExtNames.join(", ")}"`
//     );
//   return extensions;
// }
// interface ExtensionNameValue {
//   name: string;
//   value: vscode.Extension<any> | undefined;
// }
// const availableExtensions = (extensions: ExtensionNameValue[]) =>
//   extensions
//     .map(ext => ext.value)
//     .filter(ext => ext) as vscode.Extension<any>[];
// const missingExtensions = (extensions: ExtensionNameValue[]) =>
//   extensions.filter(ext => !ext.value).map(ext => ext.name);
// export function extensionActivation(
//   context: vscode.ExtensionContext,
//   state: "activate" | "deactivate" = "activate"
// ) {
//   getAvailableExtensionPacks(context).forEach(extension =>
//     extension
//       .activate()
//       .then(() =>
//         vscode.commands.executeCommand(`${extension.packageJSON.name}.${state}`)
//       )
//   );
//   showDialog(`${context.extension.packageJSON.displayName} is ${state}d!`);
// }
// export function firstTimeActivation(context: vscode.ExtensionContext) {
//   const version = context.extension.packageJSON.version ?? "1.0.0";
//   const previousVersion = context.globalState.get(context.extension.id);
//   if (previousVersion === version) return;
//   extensionActivation(context);
//   context.globalState.update(context.extension.id, version);
// }
// export function extensionReset(context: vscode.ExtensionContext) {
//   context.globalState.update(context.extension.id, undefined);
//   extensionActivation(context, "deactivate");
// }
//# sourceMappingURL=util.t.js.map