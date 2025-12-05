"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const ts_mockito_1 = require("ts-mockito");
const explainFile_1 = require("../../commands/explainFile");
suite('Explain file command - test suite', () => {
    let editor;
    let mockedEditor;
    let openAiApi;
    let mockedOpenAiApi;
    setup(() => {
        mockedEditor = (0, ts_mockito_1.mock)();
        editor = (0, ts_mockito_1.instance)(mockedEditor);
        mockedOpenAiApi = (0, ts_mockito_1.mock)();
        openAiApi = (0, ts_mockito_1.instance)(mockedOpenAiApi);
    });
    test('when the user explains a file with content the API is called', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getCurrentFileContents()).thenReturn('some content');
        await (0, explainFile_1.explainFileCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).once();
    });
    test('when the user explains a file with no content the API is not called', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getCurrentFileContents()).thenReturn('');
        await (0, explainFile_1.explainFileCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).never();
    });
    test('when the API returns a response, it is written to the console', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getCurrentFileContents()).thenReturn('some content');
        (0, ts_mockito_1.when)(mockedOpenAiApi.makeRequestWithLoadingIndicator((0, ts_mockito_1.anything)(), editor)).thenReturn(Promise.resolve('some response'));
        await (0, explainFile_1.explainFileCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedEditor.writeToConsole('some response')).once();
    });
    test('when the file is empty, an error is shown', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getCurrentFileContents()).thenReturn('');
        await (0, explainFile_1.explainFileCommand)(editor, openAiApi);
        (0, ts_mockito_1.verify)(mockedEditor.showErrorMessage('The file is empty')).once();
    });
});
//# sourceMappingURL=explainFile.test.js.map