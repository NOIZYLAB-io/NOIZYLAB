"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const applescript = require("applescript");
const path = require("path");
const vscode_1 = require("vscode");
const os_1 = require("os");
const fs = require("fs");
const Config_1 = require("./Config");
class iTunes {
    constructor() {
        this._application = "itunes";
        const version = os_1.release();
        const majorVersion = version.split(".")[0] || 0;
        if (majorVersion >= 19) {
            this._application = "music";
        }
    }
    getAppState() {
        return this.executeScript("appState");
    }
    getCurrentTrack() {
        return this.executeScript("currentTrack", false);
    }
    play() {
        this.executeScript("play");
    }
    pause() {
        this.executeScript("pause");
    }
    nextTrack() {
        this.executeScript("nextTrack");
    }
    previousTrack() {
        this.executeScript("previousTrack");
    }
    open() {
        this.executeScript("open");
    }
    unmute() {
        this.executeScript("unmute");
    }
    mute() {
        this.executeScript("mute");
    }
    like() {
        this.executeScript("likeTrack");
    }
    dislikeTrack() {
        this.executeScript("dislikeTrack");
    }
    dislikeTrackAndSkip() {
        this.executeScript("dislikeTrackAndSkip");
    }
    shuffle(enable) {
        if (enable === true) {
            this.executeScript("shuffleOn");
        }
        else {
            this.executeScript("shuffleOff");
        }
    }
    addTrack() {
        this.executeScript("addToLibrary");
    }
    setRepeat(repeat) {
        this.executeScript(`repeatSet${repeat}`)
            .then((result) => {
            if (result == null) {
                vscode_1.window.showErrorMessage("Visual Studio Code hasn't access to Accessibilty of your macOS. Please enable at System Preferences -> Security & Privacy");
            }
        })
            .catch(() => {
            vscode_1.window.showErrorMessage("Visual Studio Code hasn't access to Accessibilty of your macOS. Please enable at System Preferences -> Security & Privacy");
        });
    }
    saveArt() {
        return this.executeScript("saveArt", false);
    }
    getScript(filename, app = "music", language = "en") {
        const file = path.resolve(__dirname, `../../scripts/${app}/${language}/${filename}.applescript`);
        if (fs.existsSync(file)) {
            return file;
        }
        return path.resolve(__dirname, `../../scripts/${app}/en/${filename}.applescript`);
    }
    executeScript(filename, isJson = true) {
        return new Promise((resolve, reject) => {
            const language = Config_1.default.Instance.getLanguageOverride();
            const script = this.getScript(filename, this._application, language);
            applescript.execFile(script, (err, result) => {
                if (err) {
                    reject(err);
                }
                if (result != null) {
                    try {
                        if (isJson === true) {
                            const parsedString = JSON.parse(result.toString());
                            resolve(parsedString);
                        }
                        else {
                            resolve(result);
                        }
                    }
                    catch (exception) { }
                }
                else {
                    resolve({});
                }
            });
        });
    }
}
exports.default = iTunes;
//# sourceMappingURL=iTunes.js.map