#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, (err, response) => {
  if (err) throw err;

  console.log(`code: ${response.statusCode}`);
});
