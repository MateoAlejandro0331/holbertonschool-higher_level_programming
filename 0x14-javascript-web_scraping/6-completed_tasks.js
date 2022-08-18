#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url).then(function (response) {
  const obj = response.data;
  const task = {};
  let complete = false;
  for (let i = 0; i < obj.length; i++) {
    complete = obj[i].completed;
    if (String(obj[i].userId) in task) {
      if (complete === true) {
        task[String(obj[i].userId)] += 1;
      }
    } else {
      if (complete === true) {
        task[String(obj[i].userId)] = 1;
      }
    }
  }
  console.log(task);
});
