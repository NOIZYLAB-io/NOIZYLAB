"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.registerCommandsOutput = exports.registerCommandsInputOutput = exports.registerCommandsInput = exports.getConfigValue = void 0;
var _vscode = require("vscode");
var _constants = require("./constants");
var registerCommandsOutput = exports.registerCommandsOutput = function registerCommandsOutput(context, cmd) {
  context.subscriptions.push(_vscode.commands.registerCommand(cmd.key, function () {
    return editorInsert(cmd.callback);
  }));
};
var registerCommandsInputOutput = exports.registerCommandsInputOutput = function registerCommandsInputOutput(context, cmd) {
  context.subscriptions.push(_vscode.commands.registerCommand(cmd.key, function () {
    return _vscode.window.showInputBox({
      prompt: cmd.prompt,
      placeHolder: !cmd.placeHolder ? '' : cmd.placeHolder
    }).then(function (inputValue) {
      if (!cmd.validation || cmd.validation(inputValue)) {
        editorInsert(cmd.callback, {
          inputValue: inputValue
        });
      } else {
        _vscode.window.showErrorMessage(cmd.errorMsg);
      }
    });
  }));
};
var registerCommandsInput = exports.registerCommandsInput = function registerCommandsInput(context, cmd) {
  context.subscriptions.push(_vscode.commands.registerCommand(cmd.key, function () {
    return _vscode.window.showInputBox({
      prompt: cmd.prompt,
      placeHolder: !cmd.placeHolder ? '' : cmd.placeHolder
    }).then(function (inputValue) {
      if (!cmd.validation || cmd.validation(inputValue)) {
        cmd.callback(inputValue);
        if (cmd.infoMsg) {
          _vscode.window.showInformationMessage(cmd.infoMsg);
        }
      } else {
        _vscode.window.showErrorMessage(cmd.errorMsg);
      }
    });
  }));
};
var editorInsert = function editorInsert(generator) {
  var params = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
  var editor = _vscode.window.activeTextEditor;
  if (!editor) {
    _vscode.window.showErrorMessage(_constants.MSG_NO_ACTIVE_TEXT_EDITOR);
    return;
  }
  var generateDifferentValues = getConfigValue('vscodeRandom.multipleEditors.generateDifferentValues');
  var initialValue = generator(params);
  var newSelections = [];
  editor.edit(function (builder) {
    editor.selections.map(function (selection) {
      var text = generateDifferentValues ? generator(params) : initialValue;
      builder.replace(selection, text);
      newSelections.push(getEndPosition(selection, text));
    });
  }).then(function () {
    editor.selections = newSelections;
  });
};
var getEndPosition = function getEndPosition(selection, text) {
  var endPosition = new _vscode.Position(selection.start.line, selection.start.character + text.length);
  return new _vscode.Selection(endPosition, endPosition);
};
var getConfigValue = exports.getConfigValue = function getConfigValue(settingKey) {
  var lastPos = settingKey.lastIndexOf('.');
  var keyGroup = settingKey.substring(0, lastPos);
  var key = settingKey.substring(lastPos + 1);
  return _vscode.workspace.getConfiguration(keyGroup).get(key);
};