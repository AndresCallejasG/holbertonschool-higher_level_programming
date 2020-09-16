#!/usr/bin/node
/**
 * prints x times “C is fun”
 * if the first argument can’t be converted to an integer
 * print “Missing number of occurrences”
 */
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) { console.log('C is fun'); }
}
