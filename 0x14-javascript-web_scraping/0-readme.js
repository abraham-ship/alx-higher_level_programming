#!/usr/bin/node

const ags = process.argv[2];
const fs = require('fs');

fs.readFile(ags, 'utf-8', (err, data) => {
	if (err) throw err;

	console.log(data);
});
