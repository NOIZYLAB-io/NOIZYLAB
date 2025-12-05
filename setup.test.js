"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const ts_mockito_1 = require("ts-mockito");
const setup_1 = require("../../commands/setup");
suite('Setup command - test suite', () => {
    let editor;
    let mockedEditor;
    setup(() => {
        mockedEditor = (0, ts_mockito_1.mock)();
        editor = (0, ts_mockito_1.instance)(mockedEditor);
    });
    test('tests that the user is prompted for an API key', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your OpenAI API Key', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'Invalid API Key', true))
            .thenReturn(Promise.resolve('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'));
        await (0, setup_1.setupCommand)(editor);
        (0, ts_mockito_1.verify)(mockedEditor.getUserInput('Enter your OpenAI API Key', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'Invalid API Key', true)).once();
    });
    test('when the user enters an API key, it is stored', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your OpenAI API Key', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'Invalid API Key', true))
            .thenReturn(Promise.resolve('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'));
        await (0, setup_1.setupCommand)(editor);
        (0, ts_mockito_1.verify)(mockedEditor.setSecret('openai-api-key', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')).once();
    });
    test('when the user does not enter an API key, storage is not called', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your OpenAI API Key', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'Invalid API Key', true))
            .thenReturn(Promise.resolve(undefined));
        await (0, setup_1.setupCommand)(editor);
        (0, ts_mockito_1.verify)(mockedEditor.setSecret((0, ts_mockito_1.anything)(), (0, ts_mockito_1.anything)())).never();
    });
    test('when the key length is zero, its not sent to secret storage', async () => {
        (0, ts_mockito_1.when)(mockedEditor.getUserInput('Enter your OpenAI API Key', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'Invalid API Key', true))
            .thenReturn(Promise.resolve(''));
        await (0, setup_1.setupCommand)(editor);
        (0, ts_mockito_1.verify)(mockedEditor.setSecret((0, ts_mockito_1.anything)(), (0, ts_mockito_1.anything)())).never();
    });
});
//# sourceMappingURL=setup.test.js.map