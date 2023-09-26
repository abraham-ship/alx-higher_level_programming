#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const outputPath = process.argv[3];

request(url, (err, response, body) => {
  if (err) throw err;

  fs.writeFile(outputPath, body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
