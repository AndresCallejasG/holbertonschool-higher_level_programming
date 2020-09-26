#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

for (const k in dict) {
  if (!(dict[k] in newDict)) {
    newDict[dict[k]] = [];
  }
  newDict[dict[k]].push(k);
}
console.log(newDict);
