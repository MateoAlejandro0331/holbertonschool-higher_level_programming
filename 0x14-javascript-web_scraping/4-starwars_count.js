#!/usr/bin/node

const axios = require('axios');
const ApiURL = process.argv[2];

axios.get(ApiURL).then((response) => {
  let count = 0;
  for (const result of response.data.results) {
    for (const character of result.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
