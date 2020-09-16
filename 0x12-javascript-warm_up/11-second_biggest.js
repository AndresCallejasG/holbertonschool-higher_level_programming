#!/usr/bin/node
/**
 * searches the second biggest integer in the list of arguments.
 */
const nums = process.argv.slice(2);
if (nums.length === 0 | nums.length === 1) {
  console.log(0);
} else {
  nums.sort(function (a, b) {
    return b - a;
  });
  console.log(parseInt(nums[1]));
}
