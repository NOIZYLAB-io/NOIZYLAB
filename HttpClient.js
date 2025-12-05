"use strict";
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
Object.defineProperty(exports, "__esModule", { value: true });
exports.HttpClient = void 0;
const os = require("os");
const fs = require("fs");
const request = require("request");
const axios_1 = require("axios");
const constants = require("../common/constants");
const DownloadTimeoutMs = 20000;
/**
 * Class includes method for making http request
 */
class HttpClient {
    static cache = new Map();
    /**
     * Makes http GET request to the given url. If useCache is set to true, returns the result from cache if exists
     * @param url url to make http GET request against
     * @param useCache if true and result is already cached the cached value will be returned
     * @returns result of http GET request
     */
    static async getRequest(url, useCache = false) {
        if (useCache) {
            if (HttpClient.cache.has(url)) {
                return HttpClient.cache.get(url);
            }
        }
        const config = {
            headers: {
                'Content-Type': 'application/json'
            },
            validateStatus: () => true // Never throw
        };
        const response = await axios_1.default.get(url, config);
        if (response.status !== 200) {
            let errorMessage = [];
            errorMessage.push(response.status.toString());
            errorMessage.push(response.statusText);
            if (response.data?.error) {
                errorMessage.push(`${response.data?.error?.code} : ${response.data?.error?.message}`);
            }
            throw new Error(errorMessage.join(os.EOL));
        }
        if (useCache) {
            HttpClient.cache.set(url, response.data);
        }
        return response.data;
    }
    /**
     * Gets a file/fileContents at the given URL. Function is copied from Machine Learning extension extensions/machine-learning/src/common/httpClient.ts
     * @param downloadUrl The URL to download the file from
     * @param targetPath The path to download the file to
     * @param outputChannel The output channel to output status messages to
     * @returns Full path to the downloaded file or the contents of the file at the given downloadUrl
     */
    download(downloadUrl, targetPath, outputChannel) {
        return new Promise((resolve, reject) => {
            let totalMegaBytes = undefined;
            let receivedBytes = 0;
            let printThreshold = 0.1;
            let downloadRequest = request.get(downloadUrl, { timeout: DownloadTimeoutMs })
                .on('error', downloadError => {
                outputChannel?.appendLine(constants.downloadError);
                reject(downloadError);
            })
                .on('response', (response) => {
                if (response.statusCode !== 200) {
                    outputChannel?.appendLine(constants.downloadError);
                    return reject(response.statusMessage);
                }
                let contentLength = response.headers['content-length'];
                let totalBytes = parseInt(contentLength || '0');
                totalMegaBytes = totalBytes / (1024 * 1024);
                outputChannel?.appendLine(`${constants.downloading} ${downloadUrl} (0 / ${totalMegaBytes.toFixed(2)} MB)`);
            })
                .on('data', (data) => {
                receivedBytes += data.length;
                if (totalMegaBytes) {
                    let receivedMegaBytes = receivedBytes / (1024 * 1024);
                    let percentage = receivedMegaBytes / totalMegaBytes;
                    if (percentage >= printThreshold) {
                        outputChannel?.appendLine(`${constants.downloadProgress} (${receivedMegaBytes.toFixed(2)} / ${totalMegaBytes.toFixed(2)} MB)`);
                        printThreshold += 0.1;
                    }
                }
            });
            downloadRequest.pipe(fs.createWriteStream(targetPath))
                .on('close', async () => {
                resolve();
            })
                .on('error', (downloadError) => {
                reject(downloadError);
                downloadRequest.abort();
            });
        });
    }
}
exports.HttpClient = HttpClient;
//# sourceMappingURL=httpClient.js.map