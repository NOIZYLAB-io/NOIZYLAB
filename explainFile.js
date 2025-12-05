"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.explainFileCommand = void 0;
const explainFileCommand = async (editor, openAiApi) => {
    const fileContents = editor.getCurrentFileContents();
    if (fileContents.length > 0) {
        const prompt = `Explain the following ${editor.getCurrentFileExtension()} code: ${fileContents}`;
        const response = await openAiApi.makeRequestWithLoadingIndicator(prompt, editor);
        if (response !== undefined) {
            editor.writeToConsole(response);
        }
    }
    else {
        void editor.showErrorMessage('The file is empty');
    }
};
exports.explainFileCommand = explainFileCommand;
//# sourceMappingURL=explainFile.js.map