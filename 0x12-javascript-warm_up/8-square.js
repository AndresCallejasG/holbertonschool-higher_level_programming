#!/usr/bin/node
/**
 * script that prints a square using the character X
 * If the first arg can’t be converted to an integer print “Missing size”
 *
 */
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    const line = 'X';
    console.log(line.repeat(size));
  }
}
