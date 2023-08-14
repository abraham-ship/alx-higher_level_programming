#!/usr/bin/node
const args = process.argv.slice(2).map(Number); // Convert arguments to an array of numbers

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a); // Sort the array in descending order
  console.log(args[1]);
}
