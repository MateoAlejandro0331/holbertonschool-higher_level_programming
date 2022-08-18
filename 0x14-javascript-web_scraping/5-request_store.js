#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

axios.get(url).then(function (response) {
  fs.writeFile(file, response.data, (error) => {
    if (error) {
      console.log(error);
    }
  });
});
