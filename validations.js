"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.isValidYear = exports.isValidRegEx = exports.isValidIntRange = exports.isValid = exports.isStringWithComma = exports.isNumber = void 0;
var isNumber = exports.isNumber = function isNumber(value) {
  return value && Number.isInteger(+value);
};
var isValid = exports.isValid = function isValid(value) {
  var maxLength = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : null;
  return !!value && (!maxLength || value.length <= maxLength);
};
var isValidIntRange = exports.isValidIntRange = function isValidIntRange(value) {
  if (!value) {
    return false;
  }
  var integerValues = value.split('-');
  if (integerValues.length !== 2) {
    return false;
  }
  return isNumber(integerValues[0]) && isNumber(integerValues[1]) && +integerValues[0] <= +integerValues[1];
};
var isStringWithComma = exports.isStringWithComma = function isStringWithComma(value) {
  if (!value || typeof value !== 'string') {
    return false;
  }
  return value.indexOf(',') > -1;
};
var isValidRegEx = exports.isValidRegEx = function isValidRegEx(value) {
  try {
    new RegExp(value);
    return true;
  } catch (e) {
    return false;
  }
};
var isValidYear = exports.isValidYear = function isValidYear(value) {
  if (value === '') {
    return true;
  }
  if (!value) {
    return false;
  }
  return isNumber(value) && +value <= 2999 && +value >= 1970;
};