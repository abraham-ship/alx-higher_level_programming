#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, 'utf-8', (err, response, body) => {
  if (err) throw err;

  const movieData = JSON.parse(body);
  console.log(`Title: ${movieData.title}`);
});
