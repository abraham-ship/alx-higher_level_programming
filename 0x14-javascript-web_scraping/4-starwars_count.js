#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

let count = 0;
request.get(url, (err, response, body) => {
  if (err) throw err;

  const movieData = JSON.parse(body);
  const characters = movieData.characters;
  characters.forEach((characterUrl) => {
    const characterId = characterUrl.split('/').slice(-2, -1)[0];
    if (characterId === '18') {
      count += 1;
    }
  });
  console.log(count);
});
