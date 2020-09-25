#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      occurrences += 1;
    }
  }
  return occurrences;
};
