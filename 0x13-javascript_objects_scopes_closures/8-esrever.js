#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const len = list.length - 1;

  for (let i = len; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
