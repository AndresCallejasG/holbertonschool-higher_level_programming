#!/usr/bin/node
/**
 * computes and prints a factorial
 */
function fact (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * fact(n - 1);
}
const factorial = fact(parseInt(process.argv[2]));
console.log(factorial);
