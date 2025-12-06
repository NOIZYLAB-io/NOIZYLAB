---
description: Watch this rule if you want to make or run tests
globs: 
alwaysApply: false
---
# Testing Guide для VS Code Speech-to-Text Extension

## 📁 Структура тестов

Тесты организованы в директории:
- `src/test/integration/` - Integration тесты для полного workflow (9 файлов)
- `src/test/unit/` - Unit тесты для отдельных модулей (скомпилированные .js файлы)
- `src/test/mocks/` - Моки для внешних API и VS Code
- `src/test/fixtures/` - Тестовые данные и fixtures
- `src/test/` - Основные тестовые файлы и настройки

## 🔧 Конфигурация тестирования

### Основные файлы конфигурации:
- [.mocharc.json](mdc:.mocharc.json) - Настройки Mocha (BDD UI, timeout 10s, setup)
- [package.json](mdc:package.json) - Скрипты тестирования и nyc конфигурация
- [src/test/setup.ts](mdc:src/test/setup.ts) - Глобальная настройка тестовой среды
- [src/test/index.ts](mdc:src/test/index.ts) - Точка входа для тестов

### Доступные скрипты:
```bash
npm run test              # Основные тесты через vscode-test
npm run test:unit         # Unit тесты через Mocha
npm run test:integration  # Integration тесты через vscode-test
npm run test:roo       # Специальные тесты для Roo Code IDE
npm run pretest           # Компиляция и линтинг перед тестами
npm run compile:tsc       # Компиляция TypeScript для тестов
```

## 🎭 Моки и заглушки

### Web Audio API моки - [webAudioMocks.ts](mdc:src/test/mocks/webAudioMocks.ts):
- `MockMediaRecorder` - для записи аудио
- `MockMediaStream` - для медиа потоков
- `MockBlob`, `MockFormData` - для данных
- `setupWebAudioMocks()` / `cleanupWebAudioMocks()` - настройка/очистка

### VS Code API моки - [vscodeMocks.ts](mdc:src/test/mocks/vscodeMocks.ts):
- `mockVscode` - основной объект VS Code API
- `setActiveEditor(language)` - установка активного редактора
- `setupVSCodeMocks()` / `resetVSCodeMocks()` - настройка/сброс
- Моки для команд, настроек, статус-бара и UI элементов

### FFmpeg моки - [ffmpegMocks.ts](mdc:src/test/mocks/ffmpegMocks.ts):
- `MockChildProcess` - мок для процессов FFmpeg
- `MockTempFile` - временные файлы
- `mockWhich`, `mockTmp`, `mockChildProcess` - системные модули
- `mockPlatformCommands` - платформо-специфические команды
- `setupFFmpegMocks()` / `cleanupFFmpegMocks()` - настройка/очистка

### Тестовые данные - [testData.ts](mdc:src/test/fixtures/testData.ts):
- `testApiResponses` - ответы OpenAI API
- `testUserSettings` - пользовательские настройки
- `testLanguageConfigs` - конфигурации языков

## 📋 Существующие тесты

### Integration тесты (9 файлов):
- [extension.activation.test.ts](mdc:src/test/integration/extension.activation.test.ts) - Активация расширения
- [commands.test.ts](mdc:src/test/integration/commands.test.ts) - Регистрация и выполнение команд
- [command.status.test.ts](mdc:src/test/integration/command.status.test.ts) - Статус команд
- [keybindings.test.ts](mdc:src/test/integration/keybindings.test.ts) - Горячие клавиши
- [recording.start.test.ts](mdc:src/test/integration/recording.start.test.ts) - Запуск записи
- [recording.debug.test.ts](mdc:src/test/integration/recording.debug.test.ts) - Отладка записи
- [recording.real.test.ts](mdc:src/test/integration/recording.real.test.ts) - Реальные тесты записи
- [statusbar.integration.test.ts](mdc:src/test/integration/statusbar.integration.test.ts) - Интеграция статус-бара
- [statusbar.recording.test.ts](mdc:src/test/integration/statusbar.recording.test.ts) - Индикация записи в статус-баре

### Unit тесты:
- `ConfigurationManager.*.test.ts` - **55 тестов ConfigurationManager** ✅
- `AudioRecorder.test.js` - Тесты аудио рекордера
- `WhisperClient.test.js` - Тесты клиента Whisper API
- `StatusBarManager.test.js` - Тесты менеджера статус-бара
- `TextInserter.test.js` - Тесты вставки текста
- `ErrorHandler.test.js` - Тесты обработки ошибок
- `RetryManager.test.js` - Тесты менеджера повторов
- `FFmpegAudioRecorder.test.js` - Тесты FFmpeg рекордера
- `AudioQualityManager.test.js` - Тесты менеджера качества аудио
- `ContextManager.test.js` - Тесты менеджера контекста
- `ToggleRecording.test.js` - Тесты переключения записи
- `Roo CodeIntegration.test.js` - Тесты интеграции с Roo Code

### Основные тесты:
- [extension.test.ts](mdc:src/test/extension.test.ts) - Базовые тесты расширения

## ✅ Создание новых тестов

### Шаблон Integration теста:
```typescript
import * as assert from 'assert';
import * as vscode from 'vscode';
import { setupVSCodeMocks, resetVSCodeMocks } from '../mocks/vscodeMocks';
import { setupFFmpegMocks, cleanupFFmpegMocks } from '../mocks/ffmpegMocks';

describe('Your Integration Tests', () => {
    let extension: vscode.Extension<any> | undefined;

    before(async () => {
        setupVSCodeMocks();
        setupFFmpegMocks();
        
        // Получаем расширение
        extension = vscode.extensions.getExtension('speak-y.speech-to-text-whisper');
        assert.ok(extension, 'Extension should be found');
        
        // Активируем расширение
        if (!extension.isActive) {
            await extension.activate();
        }
    });

    after(() => {
        resetVSCodeMocks();
        cleanupFFmpegMocks();
    });

    describe('Feature Tests', () => {
        it('Should test specific feature', async () => {
            // Arrange
            const expectedResult = 'expected';
            
            // Act
            const result = await vscode.commands.executeCommand('your.command');
            
            // Assert
            assert.strictEqual(result, expectedResult);
        });
    });
});
```

### Шаблон Unit теста:
```typescript
import * as assert from 'assert';
import * as sinon from 'sinon';
import { YourModule } from '../../path/to/YourModule';
import { setupWebAudioMocks, cleanupWebAudioMocks } from '../mocks/webAudioMocks';
import { setupVSCodeMocks, resetVSCodeMocks } from '../mocks/vscodeMocks';

describe('YourModule Unit Tests', () => {
    let yourModule: YourModule;
    let clock: sinon.SinonFakeTimers;

    beforeEach(() => {
        setupWebAudioMocks();
        setupVSCodeMocks(); 
        clock = sinon.useFakeTimers();
        yourModule = new YourModule();
    });

    afterEach(() => {
        cleanupWebAudioMocks();
        resetVSCodeMocks();
        clock.restore();
        sinon.restore();
    });

    describe('Method Tests', () => {
        it('Should do something', async () => {
            // Arrange
            const expectedResult = 'expected';
            
            // Act
            const result = await yourModule.doSomething();
            
            // Assert
            assert.strictEqual(result, expectedResult);
        });
    });
});
```

## 🔐 Тестирование Singleton паттернов (ConfigurationManager и подобных)

### ⚠️ Проблема с мокированием vscode модуля
В среде VS Code Extension Host мокирование модуля `vscode` **НЕ РАБОТАЕТ** из-за особенностей загрузки модулей. 

**❌ НЕ используйте:**
```typescript
// Этот подход НЕ РАБОТАЕТ в Extension Host!
import * as vscode from 'vscode';
const mockConfig = sinon.stub(vscode.workspace, 'getConfiguration');
```

### ✅ Правильный подход: мокирование приватных методов

**Рабочий паттерн для тестирования ConfigurationManager:**
```typescript
import * as assert from 'assert';
import * as sinon from 'sinon';
import { ConfigurationManager } from '../../core/ConfigurationManager';

describe('ConfigurationManager Tests', () => {
    let configManager: ConfigurationManager;
    let sandbox: sinon.SinonSandbox;

    beforeEach(() => {
        // Создаем песочницу sinon
        sandbox = sinon.createSandbox();
        
        // ⚡ ВАЖНО: Сбрасываем singleton перед каждым тестом
        (ConfigurationManager as any).instance = null;
        
        // Создаем новый экземпляр
        configManager = ConfigurationManager.getInstance();
        
        // ✅ Мокаем приватный метод loadConfiguration
        const loadConfigurationStub = sandbox.stub(configManager as any, 'loadConfiguration');
        loadConfigurationStub.returns({
            whisper: {
                apiKey: 'test-api-key',
                language: 'auto', 
                whisperModel: 'whisper-1',
                prompt: '',
                temperature: 0.1,
                timeout: 30000,
                maxRetries: 3
            },
            audio: {
                audioQuality: 'standard',
                ffmpegPath: '',
                maxRecordingDuration: 60,
                silenceDetection: true,
                silenceDuration: 3,
                silenceThreshold: 50,
                inputDevice: 'auto'
            },
            ui: {
                showStatusBar: true
            }
        });
    });

    afterEach(() => {
        // ⚡ ВАЖНО: Очищаем ресурсы и песочницу
        configManager.dispose();
        sandbox.restore();
    });

    it('должен возвращать замоканную конфигурацию', () => {
        const config = configManager.getConfiguration();
        assert.strictEqual(config.whisper.apiKey, 'test-api-key');
        assert.strictEqual(config.audio.audioQuality, 'standard');
    });

    it('должен работать с кэшем конфигурации', () => {
        const config1 = configManager.getConfiguration();
        const config2 = configManager.getConfiguration();
        
        // Они должны быть одинаковыми (кэшированы)
        assert.strictEqual(config1, config2);
        
        // Очищаем кэш для тестирования обновления
        (configManager as any).invalidateCache();
        
        // Меняем мок для проверки перезагрузки
        const loadStub = (configManager as any).loadConfiguration;
        loadStub.returns({
            whisper: { apiKey: 'new-key', /* остальные поля */ },
            audio: { /* поля аудио */ },
            ui: { /* поля UI */ }
        });
        
        const config3 = configManager.getConfiguration();
        assert.strictEqual(config3.whisper.apiKey, 'new-key');
    });
});
```

### 🎯 Ключевые принципы для Singleton тестов:

1. **Сброс singleton:** `(ConfigurationManager as any).instance = null;`
2. **Мокирование приватных методов:** `sandbox.stub(instance as any, 'privateMethod')`
3. **Очистка ресурсов:** `instance.dispose()` + `sandbox.restore()`
4. **Тестирование кэша:** Используйте `invalidateCache()` для проверки перезагрузки

### 📂 Примеры успешных тестов ConfigurationManager:
- [ConfigurationManager.working.test.ts](mdc:src/test/unit/ConfigurationManager.working.test.ts) - 5 тестов ✅
- [ConfigurationManager.basic.test.ts](mdc:src/test/unit/ConfigurationManager.basic.test.ts) - 3 теста ✅  
- [ConfigurationManager.comprehensive.test.ts](mdc:src/test/unit/ConfigurationManager.comprehensive.test.ts) - 11 тестов ✅
- [ConfigurationManager.application-integration.test.ts](mdc:src/test/unit/ConfigurationManager.application-integration.test.ts) - 19 тестов ✅
- [ConfigurationManager.settings-validation.test.ts](mdc:src/test/unit/ConfigurationManager.settings-validation.test.ts) - 12 тестов ✅
- [ConfigurationManager.simple.test.ts](mdc:src/test/unit/ConfigurationManager.simple.test.ts) - 8 тестов ✅

**Результат: 55 тестов прошли без ошибок! 🎉**

## 🎯 Тестовые сценарии

### Integration тесты покрывают:
1. **Активация расширения** - загрузка, регистрация команд, инициализация
2. **Команды** - регистрация, выполнение, контекст, производительность
3. **Горячие клавиши** - привязки, функциональность, конфликты
4. **Запись аудио** - старт, отладка, реальные тесты
5. **Статус-бар** - интеграция, индикация состояний, анимация
6. **FFmpeg интеграция** - диагностика, инициализация
7. **Roo Code IDE интеграция** - специфичные функции

### Unit тесты покрывают:
1. **Конфигурация** - ConfigurationManager, валидация, настройки
2. **Аудио компоненты** - запись, качество, FFmpeg
3. **API клиенты** - Whisper, обработка ошибок, повторы
4. **UI компоненты** - статус-бар, вставка текста
5. **Утилиты** - контекст, переключение режимов

## 🔍 Рекомендации по тестированию

### Что тестировать:
1. **Основную функциональность** - запись, транскрипция, вставка текста
2. **Error handling** - ошибки API, отсутствие микрофона, неверные настройки
3. **Edge cases** - пустые данные, большие файлы, timeout'ы
4. **VS Code integration** - команды, настройки, активные редакторы
5. **Multi-platform support** - Windows, macOS, Linux
6. **FFmpeg integration** - обнаружение, запуск, обработка ошибок
7. **Roo Code IDE features** - специфичные команды и интеграции
8. **Configuration management** - валидация, кэширование, слушатели изменений

### Лучшие практики:
- Используйте `describe/it` для BDD стиля (Mocha настроен на BDD)
- **НЕ мокайте модуль `vscode`** в Extension Host - мокайте приватные методы
- Мокайте внешние API (fetch, getUserMedia, child_process)
- **Сбрасывайте singleton** экземпляры в `beforeEach`
- Тестируйте как успешные сценарии, так и ошибки
- Проверяйте вызовы функций через `sinon.SinonStub`
- Используйте `before/after` для setup/teardown
- Стремитесь к покрытию 80%+ (настроено в nyc)

### Отладка тестов:
```bash
# Запуск конкретного unit теста
npx mocha out/test/unit/ConfigurationManager.basic.test.js

# Запуск всех тестов ConfigurationManager
npm test -- --grep "ConfigurationManager"

# Запуск с подробным выводом
npx mocha out/test/unit/ConfigurationManager.basic.test.js --reporter=tap

# Компиляция без запуска
npm run compile:tsc

# Запуск integration тестов
npm run test:integration
```

## 📊 Покрытие кода

Цели покрытия (настроены в [package.json](mdc:package.json)):
- **Lines**: 80%
- **Statements**: 80%  
- **Functions**: 80%
- **Branches**: 70%

### Включенные в покрытие:
- `out/core/**/*.js`
- `out/ui/**/*.js`
- `out/utils/**/*.js`
- `out/integrations/**/*.js`

### Исключенные из покрытия:
- `out/test/**/*.js`
- `out/**/*.test.js`
- `out/mocks/**/*.js`

Отчеты генерируются в `coverage/` директории после запуска тестов с покрытием.

## 🚀 Специальные возможности

### Диагностические тесты:
- [diagnostic.ts](mdc:src/test/diagnostic.ts) - Диагностические утилиты
- Проверка доступности FFmpeg
- Тестирование аудио устройств
- Анализ производительности

### Roo Code IDE интеграция:
- Специальные тесты для Roo Code IDE функций
- Тестирование чат интеграции
- Проверка специфичных команд

### Платформо-специфичное тестирование:
- Windows (DirectShow)
- macOS (AVFoundation)  
- Linux (PulseAudio)
- Автоматическое определение платформы в тестах
