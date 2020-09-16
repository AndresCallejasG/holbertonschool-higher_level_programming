#!/usr/bin/node
/**
 * prints the addition of 2 integers
 * function with this prototype: function add(a, b)
 */
add(process.argv[2], process.argv[3]);
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
