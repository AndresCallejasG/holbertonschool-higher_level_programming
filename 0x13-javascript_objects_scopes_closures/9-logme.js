#!/usr/bin/node
let ctn = 0;

exports.logMe = function (item) {
  console.log(ctn + ': ' + item);
  ctn++;
};
