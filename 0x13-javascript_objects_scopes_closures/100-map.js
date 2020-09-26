#!/usr/bin/node
const data = require('./100-data').list;
console.log(data);

const newList = data.map(function (num, index) {
  return num * index;
});
console.log(newList);
