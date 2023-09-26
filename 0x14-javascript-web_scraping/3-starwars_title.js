#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, response, body) => {
  if (err) throw err;

  const movieData = JSON.parse(body);
  console.log(`Title: ${movieData.title}`);
});
