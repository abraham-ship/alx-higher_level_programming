#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) throw err;

  const todos = JSON.parse(body);
  const completed = {};
  for (const task of todos) {
    if (task.completed === true) {
      if (!(task.userId in completed)) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  }
  console.log(completed);
});
