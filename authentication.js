"use strict";
// import { request } from "http";
// const http = require('http');
// export function waitForAuthentication() {
//     return new Promise((resolve, reject) => {
//         const server = http.createServer(async (req, res) => {
//             try {
//                 if (req.url.indexOf('/oauth2callback') > -1) {
//                     let body = [];
//                     req.on('data',(chunk) => {
//                         body.push(chunk);
//                     }).on('end',() => {
//                         body = Buffer.concat(body).toString();
//                         console.log(body);
//                         resolve(body);
//                     });
//                 }
//             } catch (e) {
//                 reject(e);
//                 console.log(e);
//             }
//         }).listen(3001);
//     });
// }
//# sourceMappingURL=authentication.js.map