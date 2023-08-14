#!/usr/bin/node
const numberOfOccurrences = parseInt(process.argv[2]);

if (!isNaN(numberOfOccurrences)) {
  for (let i = 0; i < numberOfOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
