#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) throw err;

  const movieData = JSON.parse(body);
  const id = 18;
  const filmsWithWedgeAntilles = movieData.filter((film) =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)
  );
  const numberofmovies = filmsWithWedgeAntilles.length;
  console.log(numberofmovies);
});
