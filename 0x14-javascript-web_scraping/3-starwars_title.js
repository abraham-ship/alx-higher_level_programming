#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, response, body) => {
  if (err) throw err;

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(`Title: ${movieData.title}`);
  }
});
