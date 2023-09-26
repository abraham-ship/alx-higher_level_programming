#!/usr/bin/node

const fs = require('fs');
const ags = process.argv[2];
const data = process.argv[3];

fs.writeFile(ags, data, 'utf-8', (err) => {
  if (err) throw err;
});
