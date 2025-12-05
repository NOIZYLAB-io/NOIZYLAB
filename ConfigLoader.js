"use strict";

// ../server/src/frameworks/Truffle/ConfigLoader.ts
var import_process = require("process");
var config = require(import_process.argv[2]);
process.send(config);
