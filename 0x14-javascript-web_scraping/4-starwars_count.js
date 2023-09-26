#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let count = 0;
request.get(url, (err, response, body) => {
  if (err) throw err;

  const movieData = JSON.parse(body);
  const character = movieData.characters;
  for (const chars of character) {
    if (chars.includes('18')) {
      count += 1;
    }
  }
  console.log(count);
});
