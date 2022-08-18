#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url).then(function (response) {
  // console.log(response.data.results[0].characters);
  for (const string of response.data.results[0].characters) {
    if (string.search('18') > 0) {
      axios.get(string).then(function (response1) {
        console.log(response1.data.films.length);
      });
      break;
    }
  }
})
  .catch(function (error) {
    if (error.response) {
      console.log('code:', error.response.status);
    }
  });
