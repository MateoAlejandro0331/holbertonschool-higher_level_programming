#!/usr/bin/node

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url).then(function (response) {
  for (const character of response.data.characters) {
    axios.get(character).then(function (response1) {
      console.log(response1.data.name);
    });
  }
});
